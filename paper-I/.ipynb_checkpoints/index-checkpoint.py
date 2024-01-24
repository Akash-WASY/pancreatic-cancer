import pandas as pd
df = pd.read_excel('27_genelist_02_06_22.xlsx', sheet_name=0, engine='openpyxl')
u_columns = df['UCSC_RefGene_Name'].unique()
df2 = pd.read_excel('27_genelist_02_06_22.xlsx', sheet_name=1, engine='openpyxl')

cg_id = dict()
for col in u_columns:
    result  = df2.loc[df2['UCSC_RefGene_Name'] == col,'ProbeID']
    cg_id.update({col:list(result)})


print(cg_id)

