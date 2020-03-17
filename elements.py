from sqlitedict import *

dictionarydb = SqliteDict("elements.db", autocommit = True) # for accessing db of Table of Elements
element_list = dictionarydb.get('elements',[])
element_list.append({
  "number": 1,"symbol": "H",
  "name": "Hydrogen",
  "mass": 1.00794,
  "standardState": "Gas",
  "bondingType": "Diatomic",
  "meltingPoint": 14,
  "boilingPoint": 20,
  "density": 0.0000899,
  "family": "Nonmetal",
  "discovery": 1766
})
element_list.append({"number": 2,
  "symbol": "He",
  "name": "Helium",
  "mass": 4.002602,
  "standardState": "Gas",
  "bondingType": "Atomic",
  "meltingPoint": "Unknown",
  "boilingPoint": 4,
  "density": 0,
  "family": "Noble Gas",
  "discovery": 1868
})
element_list.append({
  "number": 3,
  "symbol": "Li",
  "name": "Lithium",
  "mass": 6.941,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 454,
  "boilingPoint": 1615,
  "density": 0.54,
  "family": "Alkali Metal",
  "discovery": 1817
})
element_list.append({
  "number": 4,
  "symbol": "Be",
  "name": "Beryllium",
  "mass": 9.012182,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1560,
  "boilingPoint": 2743,
  "density": 1.85,
  "family": "Alkaline Earth Metal",
  "discovery": 1798
}) 
element_list.append({
  "number": 5,
  "symbol": "B",
  "name": "Boron",
  "mass": 10.811,
  "standardState": "Solid",
  "bondingType": "Covalent Network",
  "meltingPoint": 2348,
  "boilingPoint": 4273,
  "density": 2.46,
  "family": "metalloid",
  "discovery": 1807
})
element_list.append({
  "number": 6,
  "symbol": "C",
  "name": "Carbon",
  "mass": 12.0107,
  "standardState": "Solid",
  "bondingType": "Covalent Network",
  "meltingPoint": 3823,
  "boilingPoint": 4300,
  "density": 2.26,
  "family": "nonmetal",
  "discovery": "Officially 1772"
})
element_list.append({
  "number": 7,
  "symbol": "N",
  "name": "Nitrogen",
  "mass": 14.0067,
  "standardState": "Gas",
  "bondingType": "Diatomic",
  "meltingPoint": 63,
  "boilingPoint": 77,
  "density": 0,
  "family": "Nonmetal",
  "discovery": 1772
})
element_list.append({
  "number": 8,
  "symbol": "O",
  "name": "Oxygen",
  "mass": 15.9994,
  "standardState": "Gas",
  "bondingType": "Diatomic",
  "meltingPoint": 55,
  "boilingPoint": 90,
  "density": 0,
  "family": "Nonmetal",
  "discovery": 1774
})
element_list.append({
  "number": 9,
  "symbol": "F",
  "name": "Fluorine",
  "mass": 18.9984032,
  "standardState": "Gas",
  "bondingType": "Atomic",
  "meltingPoint": 54,
  "boilingPoint": 85,
  "density": 0,
  "family": "Halogens",
  "discovery": 1670
}) 
element_list.append({
  "number": 10,
  "symbol": "Ne",
  "name": "Neon",
  "mass": 20.1797,
  "standardState": "Gas",
  "bondingType": "Atomic",
  "meltingPoint": 25,
  "boilingPoint": 27,
  "density": 0,
  "family": "Noble Gas",
  "discovery": 1898
}) 
element_list.append({
  "number": 11,
  "symbol": "Na",
  "name": "Sodium",
  "mass": 22.98976928,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 371,
  "boilingPoint": 1156,
  "density": 0.97,
  "family": "Alkali Metal",
  "discovery": 1807
})
element_list.append({
  "number": 12,
  "symbol": "Mg",
  "name": "Magnesium",
  "mass": 24.305,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 923,
  "boilingPoint": 1363,
  "density": 1.74,
  "family": "Alkaline Earth Metal",
  "discovery": 1808
})
element_list.append({
  "number": 13,
  "symbol": "Al",
  "name": "Aluminum",
  "mass": 26.9815386,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 933,
  "boilingPoint": 2792,
  "density": 2.7,
  "family": "Metal",
  "discovery": "1825"
})
element_list.append({
  "number": 14,
  "symbol": "Si",
  "name": "Silicon",
  "mass": 28.0855,
  "standardState": "Solid",
  "bondingType": "Mtallic",
  "meltingPoint": 1687,
  "boilingPoint": 3173,
  "density": 2.33,
  "family": "Metalloid",
  "discovery": 1854
})
element_list.append({
  "number": 15,
  "symbol": "P",
  "name": "Phosphorus",
  "mass": 30.973762,
  "standardState": "Solid",
  "bondingType": "Covalent Network",
  "meltingPoint": 317,
  "boilingPoint": 554,
  "density": 1.82,
  "family": "Nonmetal",
  "discovery": 1669
})
element_list.append({
  "number": 16,
  "symbol": "S",
  "name": "Sulfur",
  "mass": 32.065,
  "standardState": "Solid",
  "bondingType": "Covalent Network",
  "meltingPoint": 388,
  "boilingPoint": 718,
  "density": 1.96,
  "family": "Nonmetal",
  "discovery": "1777"
})
element_list.append({
  "number": 17,
  "symbol": "Cl",
  "name": "Chlorine",
  "mass": 35.453,
  "standardState": "Gas",
  "bondingType": "Covalent Network",
  "meltingPoint": 172,
  "boilingPoint": 239,
  "density": 0,
  "family": "Halogen",
  "discovery": 1774
})
element_list.append({
  "number": 18,
  "symbol": "Ar",
  "name": "Argon",
  "mass": 39.948,
  "standardState": "Gas",
  "bondingType": "Atomic",
  "meltingPoint": 84,
  "boilingPoint": 87,
  "density": 0,
  "family": "Noble Gas",
  "discovery": 1894
})
element_list.append({
  "number": 19,
  "symbol": "K",
  "name": "Potassium",
  "mass": 39.0983,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 337,
  "boilingPoint": 1032,
  "density": 0.86,
  "family": "Alkali Metal",
  "discovery": 1807
})
element_list.append({
  "number": 20,
  "symbol": "Ca",
  "name": "Calcium",
  "mass": 40.078,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1115,
  "boilingPoint": 1757,
  "density": 1.55,
  "family": "Alkaline Earth Metal",
  "discovery": 1808
})
element_list.append({
  "number": 21,
  "symbol": "Sc",
  "name": "Scandium",
  "mass": 44.955912,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1814,
  "boilingPoint": 3103,
  "density": 2.99,
  "family": "Transition Metal",
  "discovery": 1876
})
element_list.append({
  "number": 22,
  "symbol": "Ti",
  "name": "Titanium",
  "mass": 47.867,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1941,
  "boilingPoint": 3560,
  "density": 4.51,
  "family": "Transition Metal",
  "discovery": 1791
})
element_list.append({
  "number": 23,
  "symbol": "V",
  "name": "Vanadium",
  "mass": 50.9415,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2183,
  "boilingPoint": 3680,
  "density": 6.11,
  "family": "Transition Metal",
  "discovery": 1803
})
element_list.append({
  "number": 24,
  "symbol": "Cr",
  "name": "Chromium",
  "mass": 51.9961,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2180,
  "boilingPoint": 2944,
  "density": 7.14,
  "family": "Transition Metal",
  "discovery": 1797
})
element_list.append({
  "number": 25,
  "symbol": "Mn",
  "name": "Manganese",
  "mass": 54.938045,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1519,
  "boilingPoint": 2334,
  "density": 7.47,
  "family": "Transition Metal",
  "discovery": 1774
})
element_list.append({
  "number": 26,
  "symbol": "Fe",
  "name": "Iron",
  "mass": 55.845,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1811,
  "boilingPoint": 3134,
  "density": 7.87,
  "family": "Transition Metal",
  "discovery": "Approx. 3500 BC"
})
element_list.append({
  "number": 27,
  "symbol": "Co",
  "name": "Cobalt",
  "mass": 58.933195,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1768,
  "boilingPoint": 3200,
  "density": 8.9,
  "family": "Transition Metal",
  "discovery": 1735
})
element_list.append({
  "number": 28,
  "symbol": "Ni",
  "name": "Nickel",
  "mass": 58.6934,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1728,
  "boilingPoint": 3186,
  "density": 8.91,
  "family": "Transition Metal",
  "discovery": 1751
})
element_list.append({
  "number": 29,
  "symbol": "Cu",
  "name": "Copper",
  "mass": 63.546,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1358,
  "boilingPoint": 3200,
  "density": 8.92,
  "family": "Transition Metal",
  "discovery": "9000 BC"
})
element_list.append({
  "number": 30,
  "symbol": "Zn",
  "name": "Zinc",
  "mass": 65.38,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 693,
  "boilingPoint": 1180,
  "density": 7.14,
  "family": "Transition Metal",
  "discovery": 1746
})
element_list.append({
  "number": 31,
  "symbol": "Ga",
  "name": "Gallium",
  "mass": 69.723,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 303,
  "boilingPoint": 2477,
  "density": 5.9,
  "family": "Metal",
  "discovery": 1875
})
element_list.append({
  "number": 32,
  "symbol": "Ge",
  "name": "Germanium",
  "mass": 72.64,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1211,
  "boilingPoint": 3093,
  "density": 5.32,
  "family": "Metalloid",
  "discovery": 1886
})
element_list.append({
  "number": 33,
  "symbol": "As",
  "name": "Arsenic",
  "mass": 74.9216,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1090,
  "boilingPoint": 887,
  "density": 5.73,
  "family": "Metalloid",
  "discovery": 1250
})
element_list.append({
  "number": 34,
  "symbol": "Se",
  "name": "Selenium",
  "mass": 78.96,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 494,
  "boilingPoint": 958,
  "density": 4.82,
  "family": "Nonmetal",
  "discovery": 1817
})
element_list.append({
  "number": 35,
  "symbol": "Br",
  "name": "Bromine",
  "mass": 79.904,
  "standardState": "Liquid",
  "bondingType": "Covalent Network",
  "meltingPoint": 266,
  "boilingPoint": 332,
  "density": 3.12,
  "family": "Halogens",
  "discovery": 1826
})
element_list.append({
  "number": 36,
  "symbol": "Kr",
  "name": "Krypton",
  "mass": 83.798,
  "standardState": "Gas",
  "bondingType": "Atomic",
  "meltingPoint": 116,
  "boilingPoint": 120,
  "density": 0,
  "family": "Noble Gas",
  "discovery": 1898
})
element_list.append({
  "number": 37,
  "symbol": "Rb",
  "name": "Rubidium",
  "mass": 85.4678,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 312,
  "boilingPoint": 961,
  "density": 1.53,
  "family": "Alkali Metal",
  "discovery": 1861
})
element_list.append({
  "number": 38,
  "symbol": "Sr",
  "name": "Strontium",
  "mass": 87.62,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1050,
  "boilingPoint": 1655,
  "density": 2.63,
  "family": "Alkaline Earth Metal",
  "discovery": 1790
})
element_list.append({
  "number": 39,
  "symbol": "Y",
  "name": "Yttrium",
  "mass": 88.90585,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1799,
  "boilingPoint": 3618,
  "density": 4.47,
  "family": "Transition Metal",
  "discovery": 1794
})
element_list.append({
  "number": 40,
  "symbol": "Zr",
  "name": "Zirconium",
  "mass": 91.224,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2128,
  "boilingPoint": 4682,
  "density": 6.51,
  "family": "Transition Metal",
  "discovery": 1789
})
element_list.append({
  "number": 41,
  "symbol": "Nb",
  "name": "Niobium",
  "mass": 92.90638,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2750,
  "boilingPoint": 5017,
  "density": 8.57,
  "family": "Transition Metal",
  "discovery": 1801
})
element_list.append({
  "number": 42,
  "symbol": "Mo",
  "name": "Molybdenum",
  "mass": 95.96,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2896,
  "boilingPoint": 4912,
  "density": 10.28,
  "family": "Transition Metal",
  "discovery": 1778
})
element_list.append({
  "number": 43,
  "symbol": "Tc",
  "name": "Technetium",
  "mass": 98,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2430,
  "boilingPoint": 4538,
  "density": 11.5,
  "family": "Transition Metal",
  "discovery": 1937
})
element_list.append({
  "number": 44,
  "symbol": "Ru",
  "name": "Ruthenium",
  "mass": 101.07,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2607,
  "boilingPoint": 4423,
  "density": 12.37,
  "family": "Transition Metal",
  "discovery": 1827
})
element_list.append({
  "number": 45,
  "symbol": "Rh",
  "name": "Rhodium",
  "mass": 102.9055,
  "standardState": "solid",
  "bondingType": "metallic",
  "meltingPoint": 2237,
  "boilingPoint": 3968,
  "density": 12.45,
  "family": "Transition Metal",
  "discovery": 1803
})
element_list.append({
  "number": 46,
  "symbol": "Pd",
  "name": "Palladium",
  "mass": 106.42,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1828,
  "boilingPoint": 3236,
  "density": 12.02,
  "family": "Transition Metal",
  "discovery": 1803
})
element_list.append({
  "number": 47,
  "symbol": "Ag",
  "name": "Silver",
  "mass": 107.8682,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1235,
  "boilingPoint": 2435,
  "density": 10.49,
  "family": "Transition Metal",
  "discovery": "Approx. 4000 BC"
})
element_list.append({
  "number": 48,
  "symbol": "Cd",
  "name": "Cadmium",
  "mass": 112.411,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 594,
  "boilingPoint": 1040,
  "density": 8.65,
  "family": "Transition Metal",
  "discovery": 1817
})
element_list.append({
  "number": 49,
  "symbol": "In",
  "name": "Indium",
  "mass": 114.818,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 430,
  "boilingPoint": 2345,
  "density": 7.31,
  "family": "Metal",
  "discovery": 1863
})
element_list.append({
  "number": 50,
  "symbol": "Sn",
  "name": "Tin",
  "mass": 118.71,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 505,
  "boilingPoint": 2875,
  "density": 7.31,
  "family": "Metal",
  "discovery": "Approx. 3500 BC"
})
element_list.append({
  "number": 51,
  "symbol": "Sb",
  "name": "Antimony",
  "mass": 121.76,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 904,
  "boilingPoint": 1860,
  "density": 6.7,
  "family": "Metalloid",
  "discovery": "Approx. 3000 BC"
})
element_list.append({
  "number": 52,
  "symbol": "Te",
  "name": "Tellurium",
  "mass": 127.6,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 723,
  "boilingPoint": 1261,
  "density": 6.24,
  "family": "Metalloid",
  "discovery": 1782
})
element_list.append({
  "number": 53,
  "symbol": "I",
  "name": "Iodine",
  "mass": 126.90447,
  "standardState": "Solid",
  "bondingType": "Covalent Network",
  "meltingPoint": 387,
  "boilingPoint": 457,
  "density": 4.94,
  "family": "Halogens",
  "discovery": 1811
})
element_list.append({
  "number": 54,
  "symbol": "Xe",
  "name": "Xenon",
  "mass": 131.293,
  "standardState": "Gas",
  "bondingType": "Atomic",
  "meltingPoint": 161,
  "boilingPoint": 165,
  "density": 0.01,
  "family": "Noble Gas",
  "discovery": 1898
})
element_list.append({
  "number": 55,
  "symbol": "Cs",
  "name": "Cesium",
  "mass": 132.9054519,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 302,
  "boilingPoint": 944,
  "density": 1.88,
  "family": "Alkali Metal",
  "discovery": 1860
})
element_list.append({
  "number": 56,
  "symbol": "Ba",
  "name": "Barium",
  "mass": 137.327,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1000,
  "boilingPoint": 2143,
  "density": 3.51,
  "family": "Alkaline Earth Metal",
  "discovery": 1808
})
element_list.append({
  "number": 57,
  "symbol": "La",
  "name": "Lanthanum",
  "mass": 138.90547,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1193,
  "boilingPoint": 3737,
  "density": 6.15,
  "family": "Lanthanides",
  "discovery": 1839
})
element_list.append({
  "number": 58,
  "symbol": "Ce",
  "name": "Cerium",
  "mass": 140.116,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1071,
  "boilingPoint": 3633,
  "density": 6.69,
  "family": "Lanthanides",
  "discovery": 1803
})
element_list.append({
  "number": 59,
  "symbol": "Pr",
  "name": "Praseodymium",
  "mass": 140.90765,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1204,
  "boilingPoint": 3563,
  "density": 6.64,
  "family": "Lanthanides",
  "discovery": 1885
})
element_list.append({
  "number": 60,
  "symbol": "Nd",
  "name": "Neodymium",
  "mass": 144.242,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1294,
  "boilingPoint": 3373,
  "density": 7.01,
  "family": "Lanthanides",
  "discovery": 1885
})
element_list.append({
  "number": 61,
  "symbol": "Pm",
  "name": "Promethium",
  "mass": 145,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1373,
  "boilingPoint": 3273,
  "density": 7.26,
  "family": "Lanthanides",
  "discovery": 1947
})
element_list.append({
  "number": 62,
  "symbol": "Sm",
  "name": "Samarium",
  "mass": 150.36,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1345,
  "boilingPoint": 2076,
  "density": 7.35,
  "family": "Lanthanides",
  "discovery": 1853
})
element_list.append({
  "number": 63,
  "symbol": "Eu",
  "name": "Europium",
  "mass": 151.964,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1095,
  "boilingPoint": 1800,
  "density": 5.24,
  "family": "Lanthanides",
  "discovery": 1901
})
element_list.append({
  "number": 64,
  "symbol": "Gd",
  "name": "Gadolinium",
  "mass": 157.25,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1586,
  "boilingPoint": 3523,
  "density": 7.9,
  "family": "Lanthanides",
  "discovery": 1880
})
element_list.append({
  "number": 65,
  "symbol": "Tb",
  "name": "Terbium",
  "mass": 158.92535,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1629,
  "boilingPoint": 3503,
  "density": 8.22,
  "family": "Lanthanides",
  "discovery": 1843
})
element_list.append({
  "number": 66,
  "symbol": "Dy",
  "name": "Dysprosium",
  "mass": 162.5,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1685,
  "boilingPoint": 2840,
  "density": 8.55,
  "family": "Lanthanides",
  "discovery": 1886
})
element_list.append({
  "number": 67,
  "symbol": "Ho",
  "name": "Holmium",
  "mass": 164.93032,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1747,
  "boilingPoint": 2973,
  "density": 8.8,
  "family": "Lanthanides",
  "discovery": 1878
})
element_list.append({
  "number": 68,
  "symbol": "Er",
  "name": "Erbium",
  "mass": 167.259,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1770,
  "boilingPoint": 3141,
  "density": 9.07,
  "family": "Lanthanides",
  "discovery": 1842
})
element_list.append({
  "number": 69,
  "symbol": "Tm",
  "name": "Thulium",
  "mass": 168.93421,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1818,
  "boilingPoint": 2223,
  "density": 9.32,
  "family": "Lanthanides",
  "discovery": 1879
})
element_list.append({
  "number": 70,
  "symbol": "Yb",
  "name": "Ytterbium",
  "mass": 173.054,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1092,
  "boilingPoint": 1469,
  "density": 6.57,
  "family": "Lanthanides",
  "discovery": 1878
})
element_list.append({
  "number": 71,
  "symbol": "Lu",
  "name": "Lutetium",
  "mass": 174.9668,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1936,
  "boilingPoint": 3675,
  "density": 9.84,
  "family": "Transition Metal",
  "discovery": 1907
})
element_list.append({
  "number": 72,
  "symbol": "Hf",
  "name": "Hafnium",
  "mass": 178.49,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2506,
  "boilingPoint": 4876,
  "density": 13.31,
  "family": "Transition Metal",
  "discovery": 1923
})
element_list.append({
  "number": 73,
  "symbol": "Ta",
  "name": "Tantalum",
  "mass": 180.94788,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 3290,
  "boilingPoint": 5731,
  "density": 16.65,
  "family": "Transition Metal",
  "discovery": 1802
})
element_list.append({
  "number": 74,
  "symbol": "W",
  "name": "Tungsten",
  "mass": 183.84,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 3695,
  "boilingPoint": 5828,
  "density": 19.25,
  "family": "Transition Metal",
  "discovery": 1783
})
element_list.append({
  "number": 75,
  "symbol": "Re",
  "name": "Rhenium",
  "mass": 186.207,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 3459,
  "boilingPoint": 5869,
  "density": 21.02,
  "family": "Transition Metal",
  "discovery": 1925
})
element_list.append({
  "number": 76,
  "symbol": "Os",
  "name": "Osmium",
  "mass": 190.23,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 3306,
  "boilingPoint": 5285,
  "density": 22.59,
  "family": "Transition Metal",
  "discovery": 1803
})
element_list.append({
  "number": 77,
  "symbol": "Ir",
  "name": "Iridium",
  "mass": 192.217,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2739,
  "boilingPoint": 4701,
  "density": 22.56,
  "family": "Transition Metal",
  "discovery": 1803
})
element_list.append({
  "number": 78,
  "symbol": "Pt",
  "name": "Platinum",
  "mass": 195.084,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2041,
  "boilingPoint": 4098,
  "density": 21.09,
  "family": "Transition Metal",
  "discovery": 1735
})
element_list.append({
  "number": 79,
  "symbol": "Au",
  "name": "Gold",
  "mass": 196.966569,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1337,
  "boilingPoint": 3129,
  "density": 19.3,
  "family": "Transition Metal",
  "discovery": "Approx. 3100 BC"
})
element_list.append({
  "number": 80,
  "symbol": "Hg",
  "name": "Mercury",
  "mass": 200.59,
  "standardState": "Liquid",
  "bondingType": "Metallic",
  "meltingPoint": 234,
  "boilingPoint": 630,
  "density": 13.53,
  "family": "Transition Metal",
  "discovery": "Approx. 1500 BC"
})
element_list.append({
  "number": 81,
  "symbol": "Tl",
  "name": "Thallium",
  "mass": 204.3833,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 577,
  "boilingPoint": 1746,
  "density": 11.85,
  "family": "Metal",
  "discovery": 1861
})
element_list.append({
  "number": 82,
  "symbol": "Pb",
  "name": "Lead",
  "mass": 207.2,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 601,
  "boilingPoint": 2022,
  "density": 11.34,
  "family": "Metal",
  "discovery": "Approx. 3000 BC"
})
element_list.append({
  "number": 83,
  "symbol": "Bi",
  "name": "Bismuth",
  "mass": 208.9804,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 544,
  "boilingPoint": 1837,
  "density": 9.78,
  "family": "metal",
  "discovery": 1753
})
element_list.append({
  "number": 84,
  "symbol": "Po",
  "name": "Polonium",
  "mass": 209,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 527,
  "boilingPoint": 1235,
  "density": 9.2,
  "family": "Metalloid",
  "discovery": 1898
})
element_list.append({
  "number": 85,
  "symbol": "At",
  "name": "Astatine",
  "mass": 210,
  "standardState": "Solid",
  "bondingType": "Covalent Network",
  "meltingPoint": 575,
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Halogens",
  "discovery": 1940
})
element_list.append({
  "number": 86,
  "symbol": "Rn",
  "name": "Radon",
  "mass": 222,
  "standardState": "Sas",
  "bondingType": "Atomic",
  "meltingPoint": 202,
  "boilingPoint": 211,
  "density": 0.01,
  "family": "Noble Gas",
  "discovery": 1900
})
element_list.append({
  "number": 87,
  "symbol": "Fr",
  "name": "Francium",
  "mass": 223,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Alkali Metal",
  "discovery": 1939
})
element_list.append({
  "number": 88,
  "symbol": "Ra",
  "name": "Radium",
  "mass": 226,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 973,
  "boilingPoint": 2010,
  "density": 5,
  "family": "Alkaline Earth Metal",
  "discovery": 1898
})
element_list.append({
  "number": 89,
  "symbol": "Ac",
  "name": "Actinium",
  "mass": 227,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1323,
  "boilingPoint": 3473,
  "density": 10.07,
  "family": "Actinides",
  "discovery": 1899
})
element_list.append({
  "number": 90,
  "symbol": "Th",
  "name": "Thorium",
  "mass": 232.03806,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 2023,
  "boilingPoint": 5093,
  "density": 11.72,
  "family": "Actinides",
  "discovery": 1828
})
element_list.append({
  "number": 91,
  "symbol": "Pa",
  "name": "Protactinium",
  "mass": 231.03588,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1845,
  "boilingPoint": 4273,
  "density": 15.37,
  "family": "Actinides",
  "discovery": 1913
})
element_list.append({
  "number": 92,
  "symbol": "U",
  "name": "Uranium",
  "mass": 238.02891,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1408,
  "boilingPoint": 4200,
  "density": 19.05,
  "family": "Actinides",
  "discovery": 1789
})
element_list.append({
  "number": 93,
  "symbol": "Np",
  "name": "Neptunium",
  "mass": 237,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 917,
  "boilingPoint": 4273,
  "density": 20.45,
  "family": "Actinides",
  "discovery": 1940
})
element_list.append({
  "number": 94,
  "symbol": "Pu",
  "name": "Plutonium",
  "mass": 244,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 913,
  "boilingPoint": 3503,
  "density": 19.82,
  "family": "Actinides",
  "discovery": 1940
})
element_list.append({
  "number": 95,
  "symbol": "Am",
  "name": "Americium",
  "mass": 243,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1449,
  "boilingPoint": 2284,
  "density": 13.67,
  "family": "Actinides",
  "discovery": 1944
})
element_list.append({
  "number": 96,
  "symbol": "Cm",
  "name": "Curium",
  "mass": 247,
  "cpkHexColor": 785,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1618,
  "boilingPoint": 3383,
  "density": 13.51,
  "family": "Actinides",
  "discovery": 1944
})
element_list.append({
  "number": 97,
  "symbol": "Bk",
  "name": "Berkelium",
  "mass": 247,
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1323,
  "boilingPoint": "Unknown",
  "density": 14.78,
  "family": "Actinides",
  "discovery": 1949
})
element_list.append({
  "number": 98,
  "symbol": "Cf",
  "name": "Californium",
  "oxidationStates": [2, 3, 4],
  "standardState": "Solid",
  "bondingType": "Metallic",
  "meltingPoint": 1173,
  "boilingPoint": "Unknown",
  "density": 15.1,
  "family": "Actinides",
  "discovery": 1950
})
element_list.append({
  "number": 99,
  "symbol": "Es",
  "name": "Einsteinium",
  "mass": 252,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": 1133,
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Actinides",
  "discovery": 1952
})
element_list.append({
  "number": 100,
  "symbol": "Fm",
  "name": "Fermium",
  "mass": 257,
  "standardState": "Solid",
  "bondingType": "Ionic",
  "meltingPoint": 1800,
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Actinides",
  "discovery": 1952
})
element_list.append({
  "number": 101,
  "symbol": "Md",
  "name": "Mendelevium",
  "mass": 258,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": 1100,
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Actinides",
  "discovery": 1955
})
element_list.append({
  "number": 102,
  "symbol": "No",
  "name": "Nobelium",
  "mass": 259,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": 1100,
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Actinides",
  "discovery": 1957
})
element_list.append({
  "number": 103,
  "symbol": "Lr",
  "name": "Lawrencium",
  "mass": 262,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": 1900,
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Transition Metal",
  "discovery": 1961
})
element_list.append({
  "number": 104,
  "symbol": "Rf",
  "name": "Rutherfordium",
  "mass": 267,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Transition Metal",
  "discovery": 1969
})
element_list.append({
  "number": 105,
  "symbol": "Db",
  "name": "Dubnium",
  "mass": 268,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Transition Metal",
  "discovery": 1967
})
element_list.append({
  "number": 106,
  "symbol": "Sg",
  "name": "Seaborgium",
  "mass": 271,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Transition Metal",
  "discovery": 1974
})
element_list.append({
  "number": 107,
  "symbol": "Bh",
  "name": "Bohrium",
  "mass": 272,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Transition Metal",
  "discovery": 1976
})
element_list.append({
  "number": 108,
  "symbol": "Hs",
  "name": "Hassium",
  "mass": 270,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Transition Metal",
  "discovery": 1984
})
element_list.append({
  "number": 109,
  "symbol": "Mt",
  "name": "Meitnerium",
  "mass": 276,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "transition metal",
  "discovery": 1982
})
element_list.append({
  "number": 110,
  "symbol": "Ds",
  "name": "Darmstadtium",
  "mass": 281,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Transition Metal",
  "discovery": 1994
})
element_list.append({
  "number": 111,
  "symbol": "Rg",
  "name": "Roentgenium",
  "mass": 280,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Transition Metal",
  "discovery": 1994
})
element_list.append({
  "number": 112,
  "symbol": "Cn",
  "name": "Copernicium",
  "mass": 285,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Transition Metal",
  "discovery": 1996
})
element_list.append({
  "number": 113,
  "symbol": "Nh",
  "name": "Nihonium",
  "mass": 284,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Metal",
  "discovery": 2003
})
element_list.append({
  "number": 114,
  "symbol": "Fl",
  "name": "Flerovium",
  "mass": 289,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Metal",
  "discovery": 1998
})
element_list.append({
  "number": 115,
  "symbol": "Mc",
  "name": "Moscovium",
  "mass": 288,
  "standardState": "Gas",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Halogens",
  "discovery": 2003
})
element_list.append({
  "number": 116,
  "symbol": "Lv",
  "name": "Livermorium",
  "mass": 293,
  "standardState": "Gas",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Noble Gas",
  "discovery": 2000
})
element_list.append({
  "number": 117,
  "symbol": "Ts",
  "name": "Tennessine",
  "mass": 294,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Alkali Metal",
  "discovery": 2010
})
element_list.append({
  "number": 118,
  "symbol": "Og",
  "name": "Oganesson",
  "mass": 294,
  "standardState": "Solid",
  "bondingType": "Covalent",
  "meltingPoint": "Unknown",
  "boilingPoint": "Unknown",
  "density": "Unknown",
  "family": "Alkaline Earth Metal",
  "discovery": 2002
})
dictionarydb["elements"] = element_list
print(dictionarydb["elements"])

dictionarydb.close()