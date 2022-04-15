import pandas as pd
pd.options.mode.chained_assignment = None # default='warn'
import pyodbc

class clsDBProcs:

    def __init__(self, ServerName, DatabaseName):
        self.ServerName = ServerName,
        self.DatabaseName = DatabaseName

    def getMyConnectionObj(self, ServerName, DatabaseName):

        try:
            # connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + ServerName +';DATABASE=' + DatabaseName + ';Trusted_Connection=yes;')

            myConnection = pyodbc.connect("Driver={SQL Server Native Client 11.0}"
                                        + ";SERVER=" + ServerName
                                        + ";DATABASE=" + DatabaseName
                                        + ";Trusted_Connection=yes")

            return myConnection

        except TimeoutError as e:
            print("couldn't connect for long time")


    def getDataFrame_SQL(self, myConnection, MySQLStr):

        try:
                # Run SQL
            sql_query = pd.read_sql(MySQLStr, myConnection)
                # Convert SQL to DataFrame
            print("now reading data into data frame...")
            df = pd.DataFrame(sql_query)
            # print(df.head())
                # Execute the query
            return df

        except TimeoutError as e:
            print("couldn't connect for long time")


myDBObj  = clsDBProcs('LAPTOP-BSODD31S\SMJ_DEV', 'Investment_DB')
myConnectionObj = myDBObj.getMyConnectionObj('LAPTOP-BSODD31S\SMJ_DEV', 'Investment_DB')
# print(engine.table_names())
sql_query = 'SELECT * FROM [dbo].[StockManagement]'

myDf = myDBObj.getDataFrame_SQL(myConnectionObj, 'SELECT * FROM [dbo].[TickerPriceDaily]')
print(myDf.head())