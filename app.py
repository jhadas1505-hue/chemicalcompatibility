import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="kompatibelkimia",
    page_icon="🧪",
    layout="wide"
)

# Database bahan kimia dengan 200+ item, terurut abjad
chemical_db = {
    # FLAMMABLE (Mudah Terbakar)
    "Acetone (C3H6O)": "Flammable",
    "Acetonitrile (C2H3N)": "Flammable",
    "Acrolein (C3H4O)": "Flammable",
    "Allyl Alcohol (C3H6O)": "Flammable",
    "Benzene (C6H6)": "Flammable",
    "Benzyl Alcohol (C7H8O)": "Flammable",
    "Butanal (C4H8O)": "Flammable",
    "Butanol (C4H10O)": "Flammable",
    "Butanone (C4H8O)": "Flammable",
    "Butyl Acetate (C6H12O2)": "Flammable",
    "Carbon Disulfide (CS2)": "Flammable",
    "Cyclohexane (C6H12)": "Flammable",
    "Cyclohexanone (C6H10O)": "Flammable",
    "Cymene (C10H14)": "Flammable",
    "Diethyl Ether (C4H10O)": "Flammable",
    "Diethylamine (C4H11N)": "Flammable",
    "Diisopropyl Ether (C6H14O)": "Flammable",
    "Dimethoxyethane (C4H10O2)": "Flammable",
    "Dimethyl Disulfide (C2H6S2)": "Flammable",
    "Dimethyl Sulfide (C2H6S)": "Flammable",
    "Dimethylamine (C2H7N)": "Flammable",
    "Dimethylformamide (C3H7NO)": "Flammable",
    "Dioxane (C4H8O2)": "Flammable",
    "Ethane (C2H6)": "Flammable",
    "Ethanol (C2H5OH)": "Flammable",
    "Ethyl Acetate (C4H8O2)": "Flammable",
    "Ethyl Acrylate (C5H8O2)": "Flammable",
    "Ethyl Alcohol (C2H5OH)": "Flammable",
    "Ethylamine (C2H7N)": "Flammable",
    "Furan (C4H4O)": "Flammable",
    "Furfural (C5H4O2)": "Flammable",
    "Gasoline": "Flammable",
    "Glycol Ether (C4H10O3)": "Flammable",
    "Heptane (C7H16)": "Flammable",
    "Hexane (C6H14)": "Flammable",
    "Hexanol (C6H14O)": "Flammable",
    "Isopropanol (C3H8O)": "Flammable",
    "Isopropyl Ether (C6H14O)": "Flammable",
    "Kerosene": "Flammable",
    "Methane (CH4)": "Flammable",
    "Methanol (CH3OH)": "Flammable",
    "Methylamine (CH5N)": "Flammable",
    "Methylcyclohexane (C7H14)": "Flammable",
    "Methylene Chloride (CH2Cl2)": "Flammable",
    "Methyl Ethyl Ketone (C4H8O)": "Flammable",
    "Methyl Isobutyl Ketone (C6H12O)": "Flammable",
    "Morpholine (C4H9NO)": "Flammable",
    "Naphtha": "Flammable",
    "Neopentane (C5H12)": "Flammable",
    "Nitromethane (CH3NO2)": "Flammable",
    "Octane (C8H18)": "Flammable",
    "Pentane (C5H12)": "Flammable",
    "Pentanol (C5H12O)": "Flammable",
    "Phenol (C6H5OH)": "Flammable",
    "Pinene (C10H16)": "Flammable",
    "Propane (C3H8)": "Flammable",
    "Propanol (C3H8O)": "Flammable",
    "Propene (C3H6)": "Flammable",
    "Propyl Acetate (C5H10O2)": "Flammable",
    "Propylene (C3H6)": "Flammable",
    "Pyridine (C5H5N)": "Flammable",
    "Styrene (C8H8)": "Flammable",
    "Tetrahydrofuran (C4H8O)": "Flammable",
    "Toluene (C7H8)": "Flammable",
    "Triethylamine (C6H15N)": "Flammable",
    "Turpentine": "Flammable",
    "Vinyl Acetate (C4H6O2)": "Flammable",
    "Vinyl Chloride (C2H3Cl)": "Flammable",
    "Xylene (C8H10)": "Flammable",

    # CORROSIVE (Korosif)
    "Acetic Acid (CH3COOH)": "Corrosive",
    "Acetic Anhydride (C4H6O3)": "Corrosive",
    "Acetyl Chloride (C2H3ClO)": "Corrosive",
    "Aluminum Chloride (AlCl3)": "Corrosive",
    "Ammonia Solution (NH3)": "Corrosive",
    "Ammonium Hydroxide (NH4OH)": "Corrosive",
    "Benzoyl Chloride (C7H5ClO)": "Corrosive",
    "Boron Trichloride (BCl3)": "Corrosive",
    "Boron Trifluoride (BF3)": "Corrosive",
    "Bromic Acid (HBrO3)": "Corrosive",
    "Bromide (HBr)": "Corrosive",
    "Bromine (Br2)": "Corrosive",
    "Butanoic Acid (C4H8O2)": "Corrosive",
    "Butyryl Chloride (C4H7ClO)": "Corrosive",
    "Calcium Oxide (CaO)": "Corrosive",
    "Carbonic Acid (H2CO3)": "Corrosive",
    "Chlorine (Cl2)": "Corrosive",
    "Chloroacetic Acid (C2H3ClO2)": "Corrosive",
    "Chlorosulfonic Acid (HClSO3)": "Corrosive",
    "Chromic Acid (H2CrO4)": "Corrosive",
    "Chromyl Chloride (CrO2Cl2)": "Corrosive",
    "Cresol (C7H8O)": "Corrosive",
    "Cyanuric Acid (C3H3N3O3)": "Corrosive",
    "Dichloroacetic Acid (C2H2Cl2O2)": "Corrosive",
    "Dichloromethane (CH2Cl2)": "Corrosive",
    "Diethyl Sulfate (C4H10O4S)": "Corrosive",
    "Dimethyl Sulfate (C2H6O4S)": "Corrosive",
    "Ethyl Chloroformate (C3H5ClO2)": "Corrosive",
    "Ferrric Chloride (FeCl3)": "Corrosive",
    "Ferrous Chloride (FeCl2)": "Corrosive",
    "Fluorine (F2)": "Corrosive",
    "Formic Acid (HCOOH)": "Corrosive",
    "Fumarole Acid (C4H4O4)": "Corrosive",
    "Hydrazine (N2H4)": "Corrosive",
    "Hydrochloric Acid (HCl)": "Corrosive",
    "Hydrofluoric Acid (HF)": "Corrosive",
    "Hydrogen Bromide (HBr)": "Corrosive",
    "Hydrogen Chloride Gas (HCl)": "Corrosive",
    "Hydrogen Fluoride (HF)": "Corrosive",
    "Hydrogen Iodide (HI)": "Corrosive",
    "Hydrogen Sulfide (H2S)": "Corrosive",
    "Hypochlorous Acid (HClO)": "Corrosive",
    "Iodine (I2)": "Corrosive",
    "Iodine Chloride (ICl)": "Corrosive",
    "Iodine Monochloride (ICl)": "Corrosive",
    "Iron(III) Chloride (FeCl3)": "Corrosive",
    "Isocyanate (NCO)": "Corrosive",
    "Ketene (C2H2O)": "Corrosive",
    "Lactic Acid (C3H6O3)": "Corrosive",
    "Methane Sulfonyl Chloride (CH3SO2Cl)": "Corrosive",
    "Methyl Chloroformate (C2H3ClO2)": "Corrosive",
    "Methyl Isocyanate (C2H3NO)": "Corrosive",
    "Methanesulfonic Acid (CH4O3S)": "Corrosive",
    "Nitric Acid (HNO3)": "Corrosive",
    "Nitrogen Dioxide (NO2)": "Corrosive",
    "Oleum (SO3/H2SO4)": "Corrosive",
    "Oxalic Acid (C2H2O4)": "Corrosive",
    "Perchloric Acid (HClO4)": "Corrosive",
    "Phenol (C6H5OH)": "Corrosive",
    "Phosgene (COCl2)": "Corrosive",
    "Phosphoric Acid (H3PO4)": "Corrosive",
    "Phosphorus Pentachloride (PCl5)": "Corrosive",
    "Phosphorus Pentoxide (P2O5)": "Corrosive",
    "Phosphorus Trichloride (PCl3)": "Corrosive",
    "Phosphoryl Chloride (POCl3)": "Corrosive",
    "Potassium Hydroxide (KOH)": "Corrosive",
    "Propanoic Acid (C3H6O2)": "Corrosive",
    "Propionyl Chloride (C3H5ClO)": "Corrosive",
    "Pyrophosphoric Acid (H4P2O7)": "Corrosive",
    "Resorcinol (C6H6O2)": "Corrosive",
    "Selenium Oxide (SeO2)": "Corrosive",
    "Silicon Tetrachloride (SiCl4)": "Corrosive",
    "Sodium Bisulfate (NaHSO4)": "Corrosive",
    "Sodium Hydroxide (NaOH)": "Corrosive",
    "Sodium Hypochlorite (NaClO)": "Corrosive",
    "Sodium Nitrite (NaNO2)": "Corrosive",
    "Sodium Phosphate (Na3PO4)": "Corrosive",
    "Sulfamic Acid (H3NSO3)": "Corrosive",
    "Sulfur Dioxide (SO2)": "Corrosive",
    "Sulfur Trioxide (SO3)": "Corrosive",
    "Sulfuric Acid (H2SO4)": "Corrosive",
    "Sulfonyl Chloride (SO2Cl2)": "Corrosive",
    "Tellurium Tetrachloride (TeCl4)": "Corrosive",
    "Tetraphosphoric Acid (H6P4O13)": "Corrosive",
    "Thallium Chloride (TlCl)": "Corrosive",
    "Thiophene Dioxide (C4H4O2S)": "Corrosive",
    "Thionyl Chloride (SOCl2)": "Corrosive",
    "Titanium Tetrachloride (TiCl4)": "Corrosive",
    "Trichloroacetic Acid (C2HCl3O2)": "Corrosive",
    "Triethylamine (C6H15N)": "Corrosive",
    "Zinc Chloride (ZnCl2)": "Corrosive",

    # OXIDATOR (Pengoksidasi)
    "Ammonium Dichromate [(NH4)2Cr2O7]": "Oxidator",
    "Ammonium Nitrate (NH4NO3)": "Oxidator",
    "Ammonium Perchlorate (NH4ClO4)": "Oxidator",
    "Barium Nitrate [Ba(NO3)2]": "Oxidator",
    "Barium Perchlorate [Ba(ClO4)2]": "Oxidator",
    "Benzoyl Peroxide (C14H10O4)": "Oxidator",
    "Bleach Powder": "Oxidator",
    "Bromine Pentafluoride (BrF5)": "Oxidator",
    "Calcium Hypochlorite [Ca(ClO)2]": "Oxidator",
    "Calcium Nitrate [Ca(NO3)2]": "Oxidator",
    "Calcium Perchlorate [Ca(ClO4)2]": "Oxidator",
    "Cerric Ammonium Nitrate [Ce(NH4)2(NO3)6]": "Oxidator",
    "Chlorine (Cl2)": "Oxidator",
    "Chlorine Dioxide (ClO2)": "Oxidator",
    "Chlorine Trifluoride (ClF3)": "Oxidator",
    "Chromic Acid (H2CrO4)": "Oxidator",
    "Chromium Trioxide (CrO3)": "Oxidator",
    "Cumene Hydroperoxide (C9H12O2)": "Oxidator",
    "Dichloroisocyanuric Acid (C3HCl2N3O3)": "Oxidator",
    "Fluorine (F2)": "Oxidator",
    "Hydrogen Peroxide 30% (H2O2)": "Oxidator",
    "Hydrogen Peroxide 50% (H2O2)": "Oxidator",
    "Hydrogen Peroxide 70% (H2O2)": "Oxidator",
    "Hypochlorous Acid (HClO)": "Oxidator",
    "Iodine (I2)": "Oxidator",
    "Iodine Pentafluoride (IF5)": "Oxidator",
    "Iron(III) Chloride (FeCl3)": "Oxidator",
    "Iron(III) Nitrate [Fe(NO3)3]": "Oxidator",
    "Iron(III) Perchlorate [Fe(ClO4)3]": "Oxidator",
    "Iron(III) Sulfate [Fe2(SO4)3]": "Oxidator",
    "Lactic Acid Peroxide (C3H6O3)": "Oxidator",
    "Lead Nitrate [Pb(NO3)2]": "Oxidator",
    "Lead Perchlorate [Pb(ClO4)2]": "Oxidator",
    "Lithium Hypochlorite (LiClO)": "Oxidator",
    "Manganese Dioxide (MnO2)": "Oxidator",
    "Mercury(II) Nitrate [Hg(NO3)2]": "Oxidator",
    "Mercury(II) Perchlorate [Hg(ClO4)2]": "Oxidator",
    "Metaperiodate (IO4)": "Oxidator",
    "Methyl Ethyl Ketone Peroxide (C5H10O3)": "Oxidator",
    "Methyl Hydroperoxide (CH4O2)": "Oxidator",
    "Methyltrioxirane (C2H4O3)": "Oxidator",
    "Nitric Acid (HNO3)": "Oxidator",
    "Nitrogen Dioxide (NO2)": "Oxidator",
    "Nitrogen Tetroxide (N2O4)": "Oxidator",
    "Nitrogen Trioxide (NO3)": "Oxidator",
    "Nitrosyl Chloride (NOCl)": "Oxidator",
    "Nitrosyl Fluoride (NOF)": "Oxidator",
    "Nitrous Acid (HNO2)": "Oxidator",
    "Ozone (O3)": "Oxidator",
    "Peracetic Acid (C2H4O3)": "Oxidator",
    "Perchloric Acid (HClO4)": "Oxidator",
    "Performic Acid (CH2O3)": "Oxidator",
    "Periodic Acid (HIO4)": "Oxidator",
    "Permanganate Solution": "Oxidator",
    "Persulfate (S2O8)": "Oxidator",
    "Peroxymonosulfuric Acid (H2SO5)": "Oxidator",
    "Phosphoric Acid (H3PO4)": "Oxidator",
    "Phosphorus Pentoxide (P2O5)": "Oxidator",
    "Potassium Bromate (KBrO3)": "Oxidator",
    "Potassium Chlorate (KClO3)": "Oxidator",
    "Potassium Dichromate (K2Cr2O7)": "Oxidator",
    "Potassium Fluoride (KF)": "Oxidator",
    "Potassium Hypoiodite (KIO)": "Oxidator",
    "Potassium Iodate (KIO3)": "Oxidator",
    "Potassium Nitrate (KNO3)": "Oxidator",
    "Potassium Perchlorate (KClO4)": "Oxidator",
    "Potassium Permanganate (KMnO4)": "Oxidator",
    "Potassium Peroxide (K2O2)": "Oxidator",
    "Potassium Persulfate (K2S2O8)": "Oxidator",
    "Silver Nitrate (AgNO3)": "Oxidator",
    "Sodium Bromate (NaBrO3)": "Oxidator",
    "Sodium Chlorate (NaClO3)": "Oxidator",
    "Sodium Dichromate (Na2Cr2O7)": "Oxidator",
    "Sodium Iodate (NaIO3)": "Oxidator",
    "Sodium Nitrate (NaNO3)": "Oxidator",
    "Sodium Nitrite (NaNO2)": "Oxidator",
    "Sodium Perchlorate (NaClO4)": "Oxidator",
    "Sodium Permanganate (NaMnO4)": "Oxidator",
    "Sodium Peroxide (Na2O2)": "Oxidator",
    "Sodium Persulfate (Na2S2O8)": "Oxidator",
    "Sodium Hypochlorite (NaClO)": "Oxidator",
    "Strontium Nitrate [Sr(NO3)2]": "Oxidator",
    "Strontium Perchlorate [Sr(ClO4)2]": "Oxidator",
    "Sulfuric Acid (H2SO4)": "Oxidator",
    "Sulfur Dioxide (SO2)": "Oxidator",
    "Tert-Butyl Hydroperoxide (C4H10O2)": "Oxidator",
    "Tetranitrile Methane (C(NO2)4)": "Oxidator",
    "Trichloroisocyanuric Acid (C3Cl3N3O3)": "Oxidator",
    "Triphenylmethyl Perchlorate (C19H15ClO4)": "Oxidator",
    "Uranyl Nitrate [UO2(NO3)2]": "Oxidator",
    "Zinc Chlorate [Zn(ClO)2]": "Oxidator",
    "Zinc Nitrate [Zn(NO3)2]": "Oxidator",

    # TOXIC (Beracun)
    "Aniline (C6H7N)": "Toxic",
    "Antimony Trichloride (SbCl3)": "Toxic",
    "Antimony Trioxide (Sb2O3)": "Toxic",
    "Arsenic Pentoxide (As2O5)": "Toxic",
    "Arsenic Trioxide (As2O3)": "Toxic",
    "Benzidine (C12H12N2)": "Toxic",
    "Beryllium Chloride (BeCl2)": "Toxic",
    "Beryllium Oxide (BeO)": "Toxic",
    "Bis(2-ethylhexyl) Phthalate (C24H38O4)": "Toxic",
    "Bismuth Nitrate [Bi(NO3)3]": "Toxic",
    "Bromobenzene (C6H5Br)": "Toxic",
    "Cadmium Acetate [Cd(CH3COO)2]": "Toxic",
    "Cadmium Bromide (CdBr2)": "Toxic",
    "Cadmium Chloride (CdCl2)": "Toxic",
    "Cadmium Cyanide [Cd(CN)2]": "Toxic",
    "Cadmium Nitrate [Cd(NO3)2]": "Toxic",
    "Cadmium Oxide (CdO)": "Toxic",
    "Cadmium Sulfate (CdSO4)": "Toxic",
    "Cadmium Sulfide (CdS)": "Toxic",
    "Carbon Tetrachloride (CCl4)": "Toxic",
    "Cesium Chloride (CsCl)": "Toxic",
    "Chlorinated Paraffin": "Toxic",
    "Chlorobenzene (C6H5Cl)": "Toxic",
    "Chloroform (CHCl3)": "Toxic",
    "Chromic Acid (H2CrO4)": "Toxic",
    "Chromium(III) Acetate [Cr(CH3COO)3]": "Toxic",
    "Chromium(III) Chloride (CrCl3)": "Toxic",
    "Chromium(III) Oxide (Cr2O3)": "Toxic",
    "Chromium(VI) Oxide (CrO3)": "Toxic",
    "Chromium(VI) Trioxide (CrO3)": "Toxic",
    "Chromyl Chloride (CrO2Cl2)": "Toxic",
    "Cobalt Acetate [Co(CH3COO)2]": "Toxic",
    "Cobalt Bromide (CoBr2)": "Toxic",
    "Cobalt Chloride (CoCl2)": "Toxic",
    "Cobalt Nitrate [Co(NO3)2]": "Toxic",
    "Cobalt Oxide (CoO)": "Toxic",
    "Cobalt Sulfate (CoSO4)": "Toxic",
    "Cresols (C7H8O)": "Toxic",
    "Cumene (C9H12)": "Toxic",
    "Cyanamide (CH2N2)": "Toxic",
    "Cyanide (CN)": "Toxic",
    "Dimethyl Sulfate (C2H6O4S)": "Toxic",
    "Dinitrobenzene (C6H4N2O4)": "Toxic",
    "Dinitrophenol (C6H4N2O3)": "Toxic",
    "Dinitrotoluene (C7H6N2O4)": "Toxic",
    "Dioxin (C12H4Cl4O2)": "Toxic",
    "Diethyl Sulfate (C4H10O4S)": "Toxic",
    "Diphenylamine (C12H11N)": "Toxic",
    "Diquinone (C6H4O2)": "Toxic",
    "Dithionite (S2O4)": "Toxic",
    "Endrin (C12H8Cl6O)": "Toxic",
    "Epichlorohydrin (C3H5ClO)": "Toxic",
    "Ethidium Bromide (C21H20BrN3)": "Toxic",
    "Ethylene Dichloride (C2H4Cl2)": "Toxic",
    "Ethylene Oxide (C2H4O)": "Toxic",
    "Ferric Chloride (FeCl3)": "Toxic",
    "Formaldehyde (CH2O)": "Toxic",
    "Formamide (CH3NO)": "Toxic",
    "Formic Acid (HCOOH)": "Toxic",
    "Germanium Tetrachloride (GeCl4)": "Toxic",
    "Glycidol (C3H6O2)": "Toxic",
    "Gold Chloride (AuCl3)": "Toxic",
    "Hafnium Tetrachloride (HfCl4)": "Toxic",
    "Heptachlor (C10H5Cl7)": "Toxic",
    "Hexachlorobenzene (C6Cl6)": "Toxic",
    "Hexachlorobutadiene (C4Cl6)": "Toxic",
    "Hexachlorocyclohexane (C6H6Cl6)": "Toxic",
    "Hexachloroethane (C2Cl6)": "Toxic",
    "Hexamethylphosphoramide (C6H18N3OP)": "Toxic",
    "Hydrazine (N2H4)": "Toxic",
    "Indium Chloride (InCl3)": "Toxic",
    "Iodine (I2)": "Toxic",
    "Iodoform (CHI3)": "Toxic",
    "Isocyanates": "Toxic",
    "Isophorone (C9H14O)": "Toxic",
    "Isosafrole (C10H8O2)": "Toxic",
    "Kepone (C10H10Cl10O)": "Toxic",
    "Ketene (C2H2O)": "Toxic",
    "Lead Acetate [Pb(CH3COO)2]": "Toxic",
    "Lead Arsenate [Pb3(AsO4)2]": "Toxic",
    "Lead Bromide (PbBr2)": "Toxic",
    "Lead Chloride (PbCl2)": "Toxic",
    "Lead Iodide (PbI2)": "Toxic",
    "Lead Nitrate [Pb(NO3)2]": "Toxic",
    "Lead Oxide (PbO)": "Toxic",
    "Lead Phosphate [Pb3(PO4)2]": "Toxic",
    "Lead Selenide (PbSe)": "Toxic",
    "Lead Sulfate (PbSO4)": "Toxic",
    "Lead Telluride (PbTe)": "Toxic",
    "Lindane (C6H6Cl6)": "Toxic",
    "Lithium Chromate (Li2CrO4)": "Toxic",
    "Maleic Hydrazide (C4H4N2O2)": "Toxic",
    "Malononitrile (C3H2N2)": "Toxic",
    "Manganese Chloride (MnCl2)": "Toxic",
    "Manganese Oxide (MnO)": "Toxic",
    "Manganese Sulfate (MnSO4)": "Toxic",
    "Mercury (Hg)": "Toxic",
    "Mercury Acetate [Hg(CH3COO)2]": "Toxic",
    "Mercury Bromide (HgBr2)": "Toxic",
    "Mercury Chloride (HgCl2)": "Toxic",
    "Mercury Cyanide [Hg(CN)2]": "Toxic",
    "Mercury Iodide (HgI2)": "Toxic",
    "Mercury Nitrate [Hg(NO3)2]": "Toxic",
    "Mercury Oxide (HgO)": "Toxic",
    "Mercury Sulfate (HgSO4)": "Toxic",
    "Mercury Sulfide (HgS)": "Toxic",
    "Methylene Chloride (CH2Cl2)": "Toxic",
    "Methyl Chloroform (C2H3Cl3)": "Toxic",
    "Methyl Methacrylate (C5H8O2)": "Toxic",
    "Methyl Parathion (C8H10NO5PS)": "Toxic",
    "Methylene Bis(2-Chloroaniline) (C13H12Cl2N2)": "Toxic",
    "Methylene Diphenyl Diisocyanate (C15H10N2O2)": "Toxic",
    "Molybdenum Trioxide (MoO3)": "Toxic",
    "Mustard Gas (C4H8Cl2S)": "Toxic",
    "Naphthylamine (C10H9N)": "Toxic",
    "Nickel Acetate [Ni(CH3COO)2]": "Toxic",
    "Nickel Bromide (NiBr2)": "Toxic",
    "Nickel Chloride (NiCl2)": "Toxic",
    "Nickel Nitrate [Ni(NO3)2]": "Toxic",
    "Nickel Oxide (NiO)": "Toxic",
    "Nickel Sulfate (NiSO4)": "Toxic",
    "Nickel Sulfide (NiS)": "Toxic",
    "Niobium Pentachloride (NbCl5)": "Toxic",
    "Nitrobenzene (C6H5NO2)": "Toxic",
    "Nitrofluorene (C13H9NO2)": "Toxic",
    "Nitroglycerin (C3H5N3O9)": "Toxic",
    "N-Nitroso Compounds": "Toxic",
    "N-Nitrosodimethylamine (C2H6N2O)": "Toxic",
    "N-Nitrosodi-n-propylamine (C6H14N2O)": "Toxic",
    "N-Nitrosoethylamine (C2H6N2O)": "Toxic",
    "N-Nitrosomorpholine (C4H8N2O2)": "Toxic",
    "N-Nitrosopiperidine (C5H10N2O)": "Toxic",
    "N-Nitrosopyrrolidine (C4H8N2O)": "Toxic",
    "Osmium Tetroxide (OsO4)": "Toxic",
    "Parathion (C10H14NO5PS)": "Toxic",
    "Pentachloroethane (C2Cl5)": "Toxic",
    "Pentachloronitrobenzene (C6Cl5NO2)": "Toxic",
    "Pentachlorophenol (C6HCl5O)": "Toxic",
    "Pentyl Chloride (C5H11Cl)": "Toxic",
    "Phenacetin (C10H13NO2)": "Toxic",
    "Phenanthrene (C14H10)": "Toxic",
    "Phenol (C6H5OH)": "Toxic",
    "Phenolphthalein (C20H14O4)": "Toxic",
    "Phenyl Chloroformate (C7H5ClO2)": "Toxic",
    "Phenylhydrazine (C6H8N2)": "Toxic",
    "Phenyl Isocyanate (C7H5NO)": "Toxic",
    "Phosgene (COCl2)": "Toxic",
    "Phosphine (PH3)": "Toxic",
    "Phosphorus Tribromide (PBr3)": "Toxic",
    "Phosphorus Trichloride (PCl3)": "Toxic",
    "Phosphorus Trioxide (P2O3)": "Toxic",
    "Phosphoryl Chloride (POCl3)": "Toxic",
    "Phthalic Anhydride (C8H4O3)": "Toxic",
    "Picric Acid (C6H3N3O7)": "Toxic",
    "Polonium (Po)": "Toxic",
    "Potassium Bichromate (K2Cr2O7)": "Toxic",
    "Potassium Cyanide (KCN)": "Toxic",
    "Potassium Dichromate (K2Cr2O7)": "Toxic",
    "Potassium Permanganate (KMnO4)": "Toxic",
    "Propane Sultone (C4H8O4S)": "Toxic",
    "Propylene Oxide (C3H6O)": "Toxic",
    "Propyl Isocyanate (C4H7NO)": "Toxic",
    "Pyridine (C5H5N)": "Toxic",
    "Quinone (C6H4O2)": "Toxic",
    "Radioactive Materials": "Toxic",
    "Radon (Rn)": "Toxic",
    "Rectified Turpentine Oil": "Toxic",
    "Resorcinol (C6H6O2)": "Toxic",
    "Ruthenium Tetroxide (RuO4)": "Toxic",
    "Saccharin (C7H5NO3S)": "Toxic",
    "Safrole (C10H8O2)": "Toxic",
    "Selenium (Se)": "Toxic",
    "Selenium Dioxide (SeO2)": "Toxic",
    "Selenium Oxychloride (SeOCl2)": "Toxic",
    "Silane (SiH4)": "Toxic",
    "Silicon Tetrachloride (SiCl4)": "Toxic",
    "Silvex (C9H7Cl3O3)": "Toxic",
    "Sodium Arsenate (Na3AsO4)": "Toxic",
    "Sodium Arsenite (NaAsO2)": "Toxic",
    "Sodium Bichromate (Na2Cr2O7)": "Toxic",
    "Sodium Cyanamide (NaCH2N2)": "Toxic",
    "Sodium Cyanide (NaCN)": "Toxic",
    "Sodium Dichromate (Na2Cr2O7)": "Toxic",
    "Sodium Fluoroacetate (C2H2FNaO2)": "Toxic",
    "Sodium Nitrite (NaNO2)": "Toxic",
    "Sodium Phosphate (Na3PO4)": "Toxic",
    "Stibine (SbH3)": "Toxic",
    "Strontium Chromate (SrCrO4)": "Toxic",
    "Strontium Sulfide (SrS)": "Toxic",
    "Styrene (C8H8)": "Toxic",
    "Sulfur Dichloride (SCl2)": "Toxic",
    "Sulfur Trioxide (SO3)": "Toxic",
    "Tellurium (Te)": "Toxic",
    "Tellurium Oxide (TeO2)": "Toxic",
    "Tetrachlorodibenzo-p-Dioxin (C12H4Cl4O2)": "Toxic",
    "Tetrachloroethane (C2H2Cl4)": "Toxic",
    "Tetrachloroethene (C2Cl4)": "Toxic",
    "Tetrachloromethane (CCl4)": "Toxic",
    "Tetrachloronaphthalene (C10H4Cl4)": "Toxic",
    "Tetrachloropropene (C3H2Cl4)": "Toxic",
    "Tetramethylammonium Hydroxide [(CH3)4NOH]": "Toxic",
    "Tetranitromethane (CN4O8)": "Toxic",
    "Thallium Acetate (TlCH3COO)": "Toxic",
    "Thallium Bromide (TlBr)": "Toxic",
    "Thallium Carbonate (Tl2CO3)": "Toxic",
    "Thallium Chloride (TlCl)": "Toxic",
    "Thallium Iodide (TlI)": "Toxic",
    "Thallium Nitrate (TlNO3)": "Toxic",
    "Thallium Oxide (Tl2O)": "Toxic",
    "Thallium Selenide (Tl2Se)": "Toxic",
    "Thallium Sulfate (Tl2SO4)": "Toxic",
    "Thallium Sulfide (Tl2S)": "Toxic",
    "Thionyl Chloride (SOCl2)": "Toxic",
    "Thiourea (CH4N2S)": "Toxic",
    "Tin(II) Chloride (SnCl2)": "Toxic",
    "Tin(IV) Chloride (SnCl4)": "Toxic",
    "Titanium Tetrachloride (TiCl4)": "Toxic",
    "Toluene (C7H8)": "Toxic",
    "Toluene-2,4-Diisocyanate (C9H6N2O2)": "Toxic",
    "Toluene-2,6-Diisocyanate (C9H6N2O2)": "Toxic",
    "o-Tolidine (C14H16N2)": "Toxic",
    "Toxaphene (C10H10Cl8)": "Toxic",
    "Tributyl Phosphate (C12H27O4P)": "Toxic",
    "Trichloroacetic Acid (C2HCl3O2)": "Toxic",
    "Trichloroethane (C2H3Cl3)": "Toxic",
    "Trichloroethylene (C2HCl3)": "Toxic",
    "Trichloromethane (CHCl3)": "Toxic",
    "Trichloronaphthalene (C10H5Cl3)": "Toxic",
    "Trichlorophenol (C6H3Cl3O)": "Toxic",
    "Tricresyl Phosphate (C21H21O4P)": "Toxic",
    "Triethyl Phosphate (C6H15O4P)": "Toxic",
    "Triethylenediamine (C6H12N2)": "Toxic",
    "Trifluralin (C13H16F3N3O4)": "Toxic",
    "Trimellitic Anhydride (C9H4O5)": "Toxic",
    "Trimethyl Phosphate (C3H9O4P)": "Toxic",
    "Trinitrobenzene (C6H3N3O6)": "Toxic",
    "Trinitrophenol (C6H3N3O7)": "Toxic",
    "Trinitrotoluene (C7H5N3O6)": "Toxic",
    "Trioctyl Phosphate (C24H51O4P)": "Toxic",
    "Triphenyl Phosphate (C18H15O4P)": "Toxic",
    "Tris(2,3-Dibromopropyl)Phosphate (C9H15Br6O4P)": "Toxic",
    "Uraninite (UO2)": "Toxic",
    "Uranium (U)": "Toxic",
    "Uranium Hexafluoride (UF6)": "Toxic",
    "Vanadium Pentoxide (V2O5)": "Toxic",
    "Vanadium Tetrachloride (VCl4)": "Toxic",
    "Vanadium Trichloride (VCl3)": "Toxic",
    "Vinyl Acetate (C4H6O2)": "Toxic",
    "Vinyl Bromide (C2H3Br)": "Toxic",
    "Vinyl Chloride (C2H3Cl)": "Toxic",
    "Vinyl Fluoride (C2H3F)": "Toxic",
    "Vinyl Iodide (C2H3I)": "Toxic",
    "Vinylidene Chloride (C2H2Cl2)": "Toxic",
    "Warfarin (C19H16O4)": "Toxic",
    "Xylene (C8H10)": "Toxic",
    "Zinc Acetate [Zn(CH3COO)2]": "Toxic",
    "Zinc Arsenate [Zn3(AsO4)2]": "Toxic",
    "Zinc Arsenite [Zn(AsO2)2]": "Toxic",
    "Zinc Bromide (ZnBr2)": "Toxic",
    "Zinc Carbonate (ZnCO3)": "Toxic",
    "Zinc Chloride (ZnCl2)": "Toxic",
    "Zinc Cyanide [Zn(CN)2]": "Toxic",
    "Zinc Fluoride (ZnF2)": "Toxic",
    "Zinc Formate [Zn(HCOO)2]": "Toxic",
    "Zinc Oxide (ZnO)": "Toxic",
    "Zinc Phosphide (Zn3P2)": "Toxic",
    "Zinc Selenide (ZnSe)": "Toxic",
    "Zinc Sulfate (ZnSO4)": "Toxic",
    "Zinc Sulfide (ZnS)": "Toxic",
    "Zinc Telluride (ZnTe)": "Toxic",
    "Zirconium Tetrachloride (ZrCl4)": "Toxic",
}

# Urutkan semua bahan secara abjad
chemical_db = dict(sorted(chemical_db.items()))

# Aturan kompatibilitas (pasangan kategori yang TIDAK kompatibel)
incompatible_pairs = {
    ("Flammable", "Oxidator"),
    ("Flammable", "Corrosive"),
    ("Corrosive", "Oxidator"),
    ("Oxidator", "Toxic"),
}

# Fungsi cek kompatibilitas
def check_compatibility(cat1, cat2):
    # Jika kategori sama, selalu kompatibel
    if cat1 == cat2:
        return True
    
    # Cek apakah pasangan ada dalam daftar tidak kompatibel (order tidak penting)
    if (cat1, cat2) in incompatible_pairs or (cat2, cat1) in incompatible_pairs:
        return False
    
    # Selain itu, dianggap kompatibel
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
        index=1 if len(chemical_db) > 1 else 0
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

            if {kategori1, kategori2} == {"Flammable", "Oxidator"}:
                st.warning(
                    "Risiko kebakaran atau ledakan karena oksidator dapat mempercepat pembakaran."
                )

            elif {kategori1, kategori2} == {"Corrosive", "Flammable"}:
                st.warning(
                    "Risiko reaksi berbahaya dan kerusakan wadah penyimpanan."
                )

            elif {kategori1, kategori2} == {"Corrosive", "Oxidator"}:
                st.warning(
                    "Risiko reaksi oksidasi kuat dan pelepasan panas."
                )

            elif {kategori1, kategori2} == {"Toxic", "Oxidator"}:
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
