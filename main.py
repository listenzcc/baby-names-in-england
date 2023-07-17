"""
File: main.py
Author: Chuncheng Zhang
Date: 2023-07-15
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-07-15 ------------------------
# Requirements and constants
import pandas as pd

from rich import print
from pathlib import Path
from tqdm.auto import tqdm


# %% ---- 2023-07-15 ------------------------
# Function and class
# Data is from https://www.ons.gov.uk/search?q=baby+names

raw = pd.read_excel(
    Path('raw/raw-birth-names-in-england-wales-numbers-1996-2021.xlsx'),
    sheet_name="1",
    header=7
)

for col in tqdm(raw.columns, 'Map numbers'):
    if col == 'Name':
        continue
    raw[col] = raw[col].map(lambda x: x if isinstance(x, int) else 0)
# print(raw)
table = raw[['Name', '2021 Rank', '2021 Count']]

print(table)


# %% ---- 2023-07-15 ------------------------
# Play ground
s = table['2021 Count'].sum()
s_mu = s * 0.067
print(s, s_mu)


# %% ---- 2023-07-15 ------------------------
# Pending
selected = table[table['Name'].map(lambda e: e in [
                                   'Muhammad', 'Muhammed', 'Muhamad', 'Mohammad', 'Mohammed', 'Mohamad', 'Mohamed'])]
print(selected)


# %% ---- 2023-07-15 ------------------------
# Pending
k = selected['2021 Count'].sum()
print(s, s_mu, k, k * 3)

# %%
table.sum()
# %%
# %%
