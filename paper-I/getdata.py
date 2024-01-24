#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


df = pd.read_excel('27_genelist_02_06_22.xlsx', sheet_name=0, engine='openpyxl')


# In[14]:


df


# In[5]:


u_columns = df['UCSC_RefGene_Name'].unique()


# In[6]:


len(u_columns)  #number of unique columns


# In[7]:


df2 = pd.read_excel('27_genelist_02_06_22.xlsx', sheet_name=1, engine='openpyxl')
df2


# In[48]:


cg_id = dict()
all_cg_id = list()
for col in u_columns:
    result  = df2.loc[df2['UCSC_RefGene_Name'] == col,'ProbeID']
    cg_id.update({col:list(result)})
    all_cg_id = all_cg_id +list(result)

print(cg_id)


# In[43]:


print(all_cg_id)
# lengths = [len(v) for v in cg_id.values()]
# sum(lengths)
len(all_cg_id)


# In[9]:


df3 = pd.read_csv("TCGA_PAAD_182_norm_beta.csv")
df3


# In[57]:


df4 = pd.read_csv("clinical.tsv", sep='\t')
df4['case_submitter_id'] = df4['case_submitter_id'].str.replace('-','_')
df5= df4[["case_submitter_id","days_to_death"]]
df5


# In[32]:


writer = pd.ExcelWriter('cgid_dtd.xlsx', engine='xlsxwriter')
df5.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()


# In[55]:


df6 = df3[df3['ProbeID'].isin(all_cg_id)]    


# In[56]:


df6


# In[ ]:




