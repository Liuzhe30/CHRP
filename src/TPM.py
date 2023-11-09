import numpy as numpy
import pandas as pd
from rnanorm import TPM

data = pd.read_csv('../dataset/ens.csv',index_col=0)
data_T = data.T

data_T = data_T.loc[:, (data_T != 0).any(axis=0)]
print(data_T.head())

gtf_path = 'Homo_sapiens.GRCh37.75.gtf'

tpm = TPM(gtf_path).set_output(transform='pandas')
tpm_data = tpm.fit_transform(data_T)
#print(tpm_data.head())

tpm_data = tpm_data.dropna(axis=1, how='all')
#print(tpm_data.head())
tpm_final = tpm_data.T
print(tpm_final.head())
print(tpm_final.shape)

# mapping gene names
mapping = pd.read_csv('../dataset/ens_name_mapping.csv',index_col=0)
merged = tpm_final.join(mapping)
print(merged.head())
print(merged.shape)

merged.to_csv('../dataset/final_TPM.csv')