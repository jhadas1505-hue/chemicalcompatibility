import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FCOT Chemical Storage Checker",
    page_icon="🧪",
    layout="wide"
)

# Database contoh
chemical_db = {
    "Etanol": "Flammable",
    "Metanol": "Flammable",
    "Aseton": "Flammable",
    "HCl": "Corrosive",
    "H2SO4": "Corrosive",
    "NaOH": "Corrosive",
    "KMnO4": "Oxidator",
    "KClO3": "Oxidator",
    "H2O2": "Oxidator",
    "Benzena": "Toxic",
    "Merkuri": "Toxic",
    "Formaldehida": "Toxic"
}

# Aturan kompatibilitas
compatibility_rules = {
    ("Flammable", "Oxidator"): False,
    ("Oxidator", "Flammable"): False,

    ("Corrosive", "Flammable"): False,
    ("Flammable", "Corrosive"): False,

    ("Corrosive", "Oxidator"): False,
    ("Oxidator", "Corrosive"): False,

    ("Toxic", "Oxidator"): False,
    ("Oxidator", "Toxic"): False,
}

# Fungsi cek kompatibilitas
def check_compatibility(cat1, cat2):

    if (cat1, cat2) in compatibility_rules:
        return False

    return True


# Sidebar
st.sidebar.title("🧪 FCOT Menu")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "Dashboard",
        "Cek Kompatibilitas",
        "Database Bahan Kimia"
    ]
)

# Dashboard
if menu == "Dashboard":

    st.title("🧪 FCOT Chemical Storage Checker")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🔥 Flammable",
                sum(v=="Flammable" for v in chemical_db.values()))

    col2.metric("⚗️ Corrosive",
                sum(v=="Corrosive" for v in chemical_db.values()))

    col3.metric("🧨 Oxidator",
                sum(v=="Oxidator" for v in chemical_db.values()))

    col4.metric("☣ Toxic",
                sum(v=="Toxic" for v in chemical_db.values()))

    st.info(
        "Sistem membantu menentukan kompatibilitas penyimpanan bahan kimia berdasarkan teori FCOT."
    )

# Cek Kompatibilitas
elif menu == "Cek Kompatibilitas":

    st.title("🔍 Cek Kompatibilitas")

    bahan1 = st.selectbox(
        "Pilih Bahan Kimia Pertama",
        list(chemical_db.keys())
    )

    bahan2 = st.selectbox(
        "Pilih Bahan Kimia Kedua",
        list(chemical_db.keys()),
        index=1
    )

    if st.button("Cek Sekarang"):

        kategori1 = chemical_db[bahan1]
        kategori2 = chemical_db[bahan2]

        st.write(f"**{bahan1}** → {kategori1}")
        st.write(f"**{bahan2}** → {kategori2}")

        compatible = check_compatibility(
            kategori1,
            kategori2
        )

        if compatible:

            st.success("✅ KOMPATIBEL")

            st.write(
                "Kedua bahan dapat disimpan pada area yang sama dengan pengawasan standar."
            )

        else:

            st.error("❌ TIDAK KOMPATIBEL")

            if {"Flammable", "Oxidator"} == {kategori1, kategori2}:
                st.warning(
                    "Risiko kebakaran atau ledakan karena oksidator dapat mempercepat pembakaran."
                )

            elif {"Corrosive", "Flammable"} == {kategori1, kategori2}:
                st.warning(
                    "Risiko reaksi berbahaya dan kerusakan wadah penyimpanan."
                )

            elif {"Corrosive", "Oxidator"} == {kategori1, kategori2}:
                st.warning(
                    "Risiko reaksi oksidasi kuat dan pelepasan panas."
                )

            elif {"Toxic", "Oxidator"} == {kategori1, kategori2}:
                st.warning(
                    "Berpotensi menghasilkan gas beracun."
                )

# Database
elif menu == "Database Bahan Kimia":

    st.title("📚 Database Bahan Kimia")

    data = pd.DataFrame({
        "Nama Bahan": chemical_db.keys(),
        "Kategori FCOT": chemical_db.values()
    })

    filter_fcot = st.selectbox(
        "Filter Kategori",
        ["Semua"] + sorted(data["Kategori FCOT"].unique())
    )

    if filter_fcot != "Semua":
        data = data[data["Kategori FCOT"] == filter_fcot]

    st.dataframe(
        data,
        use_container_width=True
    )
