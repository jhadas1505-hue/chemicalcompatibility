import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from database import get_chemical_database, get_ghs_images
from analyzer import analyze_compatibility
import json
import os

st.set_page_config(
    page_title="CHECKCOMCHEMISTRY",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== CSS STYLE (SAMA DENGAN KODE ANDA) =====
st.markdown("""
<style>
    body { background-color: #1a1a2e; color: #eaeaea; }
    .main { background-color: #16213e; color: #eaeaea; }
    .main-title { font-size: 48px; font-weight: bold; background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; margin-bottom: 20px; }
    .section-title { font-size: 28px; font-weight: bold; color: #00d4ff; border-bottom: 3px solid #00d4ff; padding-bottom: 10px; margin-top: 20px; }
    .status-card { padding: 30px; border-radius: 15px; font-weight: bold; font-size: 24px; text-align: center; box-shadow: 0 8px 16px rgba(0,0,0,0.3); margin: 20px 0; animation: slideIn 0.6s ease-out; }
    .safe { background: linear-gradient(135deg, #00d97e 0%, #00a85e 100%); color: white; border: 3px solid #00a85e; }
    .danger { background: linear-gradient(135deg, #ff006e 0%, #c90050 100%); color: white; border: 3px solid #c90050; }
    .warning { background: linear-gradient(135deg, #ffa500 0%, #cc8400 100%); color: white; border: 3px solid #cc8400; }
    @keyframes slideIn { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes popIn { 0% { transform: scale(0); opacity: 0; } 50% { transform: scale(1.1); } 100% { transform: scale(1); opacity: 1; } }
    .ghs-icon-container { text-align: center; margin: 20px 0; }
    .ghs-icon { display: inline-block; animation: popIn 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); filter: drop-shadow(0 10px 20px rgba(0,0,0,0.4)); transition: transform 0.3s ease; }
    .ghs-icon:hover { transform: scale(1.1) rotateZ(5deg); }
    .chemical-card { background: #0f3460; border-radius: 15px; padding: 20px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3); transition: all 0.3s ease; animation: slideIn 0.6s ease-out; border: 2px solid #00d4ff; }
    .chemical-card:hover { transform: translateY(-10px); box-shadow: 0 8px 25px rgba(0,212,255,0.3); }
    .chemical-name { font-weight: bold; color: #00d4ff; margin-top: 15px; font-size: 14px; }
    .chemical-category { color: #ffa500; font-size: 12px; margin-top: 8px; font-weight: 600; }
    .danger-badge { display: inline-block; background: #ff006e; color: white; padding: 5px 10px; border-radius: 20px; font-size: 12px; margin-top: 8px; animation: popIn 0.8s ease-out; }
    .warning-badge { display: inline-block; background: #ffa500; color: white; padding: 5px 10px; border-radius: 20px; font-size: 12px; margin-top: 8px; animation: popIn 0.8s ease-out; }
    .safe-badge { display: inline-block; background: #00d97e; color: white; padding: 5px 10px; border-radius: 20px; font-size: 12px; margin-top: 8px; animation: popIn 0.8s ease-out; }
    .info-box { background: #0f3460; border-left: 5px solid #00d4ff; padding: 15px; border-radius: 8px; margin: 15px 0; color: #eaeaea; }
    .metric-card { background: #0f3460; padding: 20px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.3); text-align: center; margin: 10px; border: 2px solid #00d4ff; }
    .metric-value { font-size: 36px; font-weight: bold; color: #00d4ff; margin: 10px 0; }
    .metric-label { color: #ffa500; font-weight: bold; }
    .stButton > button { background: linear-gradient(135deg, #00d4ff 0%, #0099cc 100%); color: white; border: none; padding: 12px 24px; border-radius: 8px; font-weight: bold; transition: all 0.3s ease; }
    .stButton > button:hover { transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0, 212, 255, 0.4); }
    .favorite-card { background: linear-gradient(135deg, #0f3460 0%, #1a4d6d 100%); border-radius: 15px; padding: 20px; margin: 15px 0; border: 2px solid #ff006e; box-shadow: 0 4px 15px rgba(255,0,110,0.2); animation: slideIn 0.6s ease-out; }
    .favorite-card:hover { box-shadow: 0 8px 25px rgba(255,0,110,0.4); transform: translateY(-5px); }
    .favorite-title { color: #ff006e; font-weight: bold; font-size: 18px; margin-bottom: 10px; }
    .favorite-info { color: #eaeaea; font-size: 14px; margin: 5px 0; }
</style>
""", unsafe_allow_html=True)

# ===== SESSION STATE =====
if "history" not in st.session_state:
    st.session_state.history = []
if "favorites" not in st.session_state:
    st.session_state.favorites = []  # ← PASTIKAN INISIALISASI BENAR

# ===== SIDEBAR =====
st.sidebar.markdown("""
<div style='text-align:center; padding:20px 0;'>
    <h1 style='font-size:40px; margin:0;'>🧪</h1>
    <h2 style='font-size:20px; margin:5px 0; color:#00d4ff;'>Checkcomchemistry</h2>
    <p style='font-size:12px; color:#ffa500;'>Politeknik AKA Bogor</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "📌 MENU UTAMA",
    ["🏠 Home", "🔍 Cek Kompatibilitas", "📊 Dashboard", "❤️ Favorit", "📚 Panduan", "🧪 Database", "⚙️ Pengaturan"]
)

# ===== HOME =====
if menu == "🏠 Home":
    st.markdown("<div class='main-title'>🧪 CHECKCOMCHEMISTRY</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-box'>
        <h3 style='color:#00d4ff;'>🎯 Selamat Datang di Checkcomchemistry</h3>
        <p>Sistem manajemen keamanan bahan kimia dengan visualisasi 3D GHS yang canggih, database 500+ bahan kimia, dan analisis real-time.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <div style='font-size:40px;'>🔍</div>
            <div class='metric-label'>CEK KOMPATIBILITAS</div>
            <p style='font-size:12px; color:#eaeaea;'>Analisis real-time dengan visualisasi 3D</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <div style='font-size:40px;'>📊</div>
            <div class='metric-label'>DASHBOARD ANALYTICS</div>
            <p style='font-size:12px; color:#eaeaea;'>Visualisasi data keamanan lengkap</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <div style='font-size:40px;'>❤️</div>
            <div class='metric-label'>FAVORIT MENU</div>
            <p style='font-size:12px; color:#eaeaea;'>Simpan & akses favorit dengan one-click</p>
        </div>
        """, unsafe_allow_html=True)

# ===== CEK KOMPATIBILITAS =====
elif menu == "🔍 Cek Kompatibilitas":
    st.markdown("<h2 class='section-title'>🔍 Cek Kompatibilitas Bahan Kimia</h2>", unsafe_allow_html=True)
    
    chemical_db = get_chemical_database()
    ghs_images = get_ghs_images()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Bahan Kimia 1** 🧪")
        chem1 = st.selectbox("Pilih bahan pertama", list(chemical_db.keys()), key="chem1", label_visibility="collapsed")
    with col2:
        st.markdown("**Bahan Kimia 2** 🧪")
        chem2 = st.selectbox("Pilih bahan kedua", list(chemical_db.keys()), key="chem2", label_visibility="collapsed")
    
    col1, col2 = st.columns(2)
    with col1:
        check_btn = st.button("✅ Cek Sekarang", use_container_width=True, key="check_btn")
    with col2:
        clear_all = st.button("🧹 Hapus Semua", use_container_width=True, key="clear_all_btn")
    
    if clear_all:
        st.session_state.history = []
        st.success("✅ Semua data riwayat dihapus!")
        st.rerun()
    
    if check_btn:
        with st.spinner("🔬 Menganalisis kombinasi bahan kimia..."):
            import time
            time.sleep(1.2)
        
        t1 = chemical_db[chem1]
        t2 = chemical_db[chem2]
        status, penjelasan, penyimpanan = analyze_compatibility(t1, t2)
        
        status_class = "safe" if "AMAN" in status else ("danger" if "BERBAHAYA" in status else "warning")
        
        st.markdown(f"<div class='status-card {status_class}'>{status}</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='chemical-card'>", unsafe_allow_html=True)
            image_path = ghs_images.get(t1)
            if image_path and os.path.exists(image_path):
                st.image(image_path, width=120)
            else:
                st.warning(f"Gambar tidak ditemukan untuk {t1}")
            st.markdown(f"<div class='chemical-name'>{chem1}</div><div class='chemical-category'>{t1}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='chemical-card'>", unsafe_allow_html=True)
            image_path2 = ghs_images.get(t2)
            if image_path2 and os.path.exists(image_path2):
                st.image(image_path2, width=120)
            else:
                st.warning(f"Gambar tidak ditemukan untuk {t2}")
            st.markdown(f"<div class='chemical-name'>{chem2}</div><div class='chemical-category'>{t2}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🧠 Penjelasan Hasil")
            st.info(penjelasan)
        with col2:
            st.markdown("### 📦 Rekomendasi Penyimpanan")
            st.warning(penyimpanan)
        
        # SIMPAN KE HISTORY
        record = {
            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Bahan 1": chem1,
            "Bahan 2": chem2,
            "Kategori 1": t1,
            "Kategori 2": t2,
            "Hasil": status.replace("❌ ", "").replace("⚠️ ", "").replace("✅ ", ""),
        }
        st.session_state.history.append(record)
        
        # SIMPAN DATA UNTUK FAVORIT
        favorite_data = {
            "id": len(st.session_state.favorites) + 1,
            "chem1": chem1,
            "chem2": chem2,
            "cat1": t1,
            "cat2": t2,
            "status": status.replace("❌ ", "").replace("⚠️ ", "").replace("✅ ", ""),
            "penjelasan": penjelasan,
            "penyimpanan": penyimpanan,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
