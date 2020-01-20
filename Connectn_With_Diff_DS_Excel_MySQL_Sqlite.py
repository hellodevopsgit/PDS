
#####################Excel_Connection###############################
import os
import pandas as pd
Base='C:/VKHCG' 
sFileDir=Base + '/01-Vermeulen/01-Retrieve/01-EDS/02-Python' 
CurrencyRawData = pd.read_excel('C:/VKHCG/01-Vermeulen/00-RawData/Country_Currency.xlsx')
sColumns = ['Country or territory', 'Currency', 'ISO-4217'] 
CurrencyData = CurrencyRawData[sColumns] 
CurrencyData.rename(columns={'Country or territory': 'Country', 'ISO-4217': 'CurrencyCode'}, inplace=True) 
CurrencyData.dropna(subset=['Currency'],inplace=True) 
CurrencyData['Country'] = CurrencyData['Country'].map(lambda x: x.strip())
CurrencyData['Currency'] = CurrencyData['Currency'].map(lambda x: x.strip()) 
CurrencyData['CurrencyCode'] = CurrencyData['CurrencyCode'].map(lambda x: x.strip())
print(CurrencyData) 
print('~~~~~~ Data from Excel Sheet Retrived Successfully ~~~~~~~ ') 
sFileName=sFileDir + '/Retrieve-Country-Currency.csv'
CurrencyData.to_csv(sFileName, index = False) 

#####################MYSQL_CONNECTION_##############################
import mysql.connector
conn= mysql.connector.connect(host='localhost',database='DataScience',user='root',password='root')
conn.connect
if(conn.is_connected):
    print('###################Connection with mysql is established###################')
else:
    print('Not Connected--Check connection properties')



###################SQLite############################################
import sqlite3 as sq
import pandas as pd
Base='C:/VKHCG' 
sDatabaseName=Base + '01-Vermeulen\04-Transform\SQLite\Vermeulen.db'
conn = sq.connect(sDatabaseName) 
sFileName='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python/IP_DATA_ALL.csv'
print('Loading :',sFileName) 
IP_DATA_ALL_FIX=pd.read_csv(sFileName,header=0,low_memory=False) 
IP_DATA_ALL_FIX.index.names = ['RowIDCSV']
sTable='IP_DATA_ALL' 
print('Storing :',sDatabaseName,' Table:',sTable) 
IP_DATA_ALL_FIX.to_sql(sTable, conn, if_exists="replace") 
print('Loading :',sDatabaseName,' Table:',sTable) 
TestData=pd.read_sql_query("select * from IP_DATA_ALL;", conn)
print('################')
print('## Data Values')
print('################')
print(TestData)
print('################')
print('## Data Profile')
print('################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################') 
print('### Done!! ############################################') 
    
