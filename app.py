import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="kompatibelkimia",
    page_icon="🧪",
    layout="wide"
)

# Database contoh
chemical_db = {

    # =========================
    # FLAMMABLE (Mudah Terbakar)
    # =========================
    "Aseton (C3H6O)": "Flammable",
    "Metanol (CH3OH)": "Flammable",
    "Etanol (C2H5OH)": "Flammable",
    "Isopropanol (C3H8O)": "Flammable",
    "Toluena (C7H8)": "Flammable",
    "Xilena (C8H10)": "Flammable",
    "Heksana (C6H14)": "Flammable",
    "Sikloheksana (C6H12)": "Flammable",
    "Dietil Eter (C4H10O)": "Flammable",
    "Benzena (C6H6)": "Flammable",
    "Asetonitril (C2H3N)": "Flammable",
    "Etil Asetat (C4H8O2)": "Flammable",
    "Propanol (C3H8O)": "Flammable",
    "Butanol (C4H10O)": "Flammable",
    "Tetrahidrofuran (C4H8O)": "Flammable",

    # =========================
    # CORROSIVE (Korosif)
    # =========================
    "Asam Klorida (HCl)": "Corrosive",
    "Asam Sulfat (H2SO4)": "Corrosive",
    "Asam Nitrat (HNO3)": "Corrosive",
    "Asam Fosfat (H3PO4)": "Corrosive",
    "Asam Asetat Glasial (CH3COOH)": "Corrosive",
    "Natrium Hidroksida (NaOH)": "Corrosive",
    "Kalium Hidroksida (KOH)": "Corrosive",
    "Amonium Hidroksida (NH4OH)": "Corrosive",
    "Asam Format (HCOOH)": "Corrosive",
    "Asam Bromida (HBr)": "Corrosive",
    "Asam Fluorida (HF)": "Corrosive",
    "Asam Perklorat (HClO4)": "Corrosive",

    # =========================
    # OXIDATOR
    # =========================
    "Kalium Permanganat (KMnO4)": "Oxidator",
    "Kalium Dikromat (K2Cr2O7)": "Oxidator",
    "Hidrogen Peroksida 30% (H2O2)": "Oxidator",
    "Hidrogen Peroksida 50% (H2O2)": "Oxidator",
    "Kalium Klorat (KClO3)": "Oxidator",
    "Kalium Perklorat (KClO4)": "Oxidator",
    "Natrium Nitrat (NaNO3)": "Oxidator",
    "Amonium Nitrat (NH4NO3)": "Oxidator",
    "Natrium Klorit (NaClO2)": "Oxidator",
    "Natrium Hipoklorit (NaClO)": "Oxidator",
    "Kalsium Hipoklorit [Ca(ClO)2]": "Oxidator",
    "Kalium Nitrat (KNO3)": "Oxidator",

    # =========================
    # TOXIC (Beracun)
    # =========================
    "Merkuri (Hg)": "Toxic",
    "Timbal Nitrat [Pb(NO3)2]": "Toxic",
    "Kadmium Sulfat (CdSO4)": "Toxic",
    "Formaldehida (CH2O)": "Toxic",
    "Fenol (C6H5OH)": "Toxic",
    "Natrium Sianida (NaCN)": "Toxic",
    "Kalium Sianida (KCN)": "Toxic",
    "Arsen Trioksida (As2O3)": "Toxic",
    "Kromium(VI) Oksida (CrO3)": "Toxic",
    "Raksa(II) Klorida (HgCl2)": "Toxic",
    "Metilen Klorida (CH2Cl2)": "Toxic",
    "Kloroform (CHCl3)": "Toxic",
    "Karbon Tetraklorida (CCl4)": "Toxic",
    "Anilin (C6H7N)": "Toxic",
    "Piridina (C5H5N)": "Toxic"
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
