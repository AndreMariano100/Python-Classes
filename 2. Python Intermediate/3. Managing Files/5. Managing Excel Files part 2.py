# Imports --------------------------------------------------------------------------------------------------------------
import pandas as pd
import os

# File Path ------------------------------------------------------------------------------------------------------------
current_path = os.getcwd()
full_path = os.path.join(current_path, 'Files', 'pipe_schedules.xlsx')

# Create DataFrame Object ----------------------------------------------------------------------------------------------
df = pd.read_excel(full_path, sheet_name='pipe_schedules')
print(df)
print(df.columns)

# Filter mask
standard_mask = df['Standard'] == 'ASME B36.10'
standard_nps = df['NPS'] == 10
standard_schedule = df['Schedule'] == 160

print()
result = df[standard_mask & standard_nps & standard_schedule]
print(result)