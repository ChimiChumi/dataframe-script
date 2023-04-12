import pandas as pd

# loading excel tables
df1 = pd.read_excel('1.xlsx')   # 1st input table with current employees
df1['cnp'] = df1['cnp'].astype(str)

df2 = pd.read_excel('2.xls', skiprows=4)  # 2nd input table with all employees
df2['CNP posesor card'] = df2['CNP posesor card'].astype(str)

# filter valid data based on 'cnp' as key. Only considers mutual values.
valid_data = pd.merge(df1, df2, left_on='cnp',
                      right_on='CNP posesor card', how='inner')

# filter values which are missing in the first table
invalid_data = df2[~df2['CNP posesor card'].isin(df1['cnp'])]


# extract values after filtering
nume = valid_data['Nume'].str.upper()
prenume = valid_data['Prenume'].str.upper()
cnp = valid_data['cnp'].astype(str)
serie_card = valid_data['Serie card'].astype(str)
tickets = valid_data['Nr. de tichete']

nume_extra = invalid_data['Nume\nposesor card'].str.upper()
prenume_extra = invalid_data['Prenume posesor card'].str.upper()
cnp_extra = invalid_data['CNP posesor card']


# create new result tables for valid and extra data
valid_res = pd.DataFrame(
    {'Nume': nume, 'Prenume': prenume, 'CNP': cnp, 'Serie card': serie_card, 'Nr. de tichete': tickets})
extra_res = pd.DataFrame(
    {'Nume': nume_extra, 'Prenume': prenume_extra, 'CNP': cnp_extra})

# sort by name
valid_res.sort_values(by='Nume', inplace=True)
extra_res.sort_values(by='Nume', inplace=True)

# save to separate Excel sheets
valid_res.to_excel('final.xlsx', sheet_name='Sheet1', index=False)
extra_res.to_excel('extra.xlsx', sheet_name='Sheet1', index=False)


print("\n Generation successful!\n")
