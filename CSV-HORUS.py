import pandas as pd
sInputFileName='C:/VKHCG/01-Vermeulen/00-RawData/Country_Code.csv'
InputData=pd.read_csv(sInputFileName,encoding="latin-1")
print(InputData)
ProcessData=InputData
ProcessData.drop('ISO-2-CODE', axis=1,inplace=True)
ProcessData.drop('ISO-3-Code', axis=1,inplace=True)
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
ProcessData.set_index('CountryNumber', inplace=True)
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)
print(ProcessData)
OutputData=ProcessData
sOutputFileName='C:/VKHCG/01-Vermeulen/00-RawData/Country_Code_Generated.csv'
OutputData.to_csv(sOutputFileName, index = False)
print('CSV to HORUS - Done')