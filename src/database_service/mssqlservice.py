from sqlalchemy import create_engine
import pyodbc

print('hola')

# import pyodbc
# server = 'localhost'
# database = 'SampleDB'
# username = 'sa'
# password = 'your_password'
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()


engine = create_engine("mssql+pyodbc://sa:<YourStrong!Passw0rd>@172.17.0.2:1433/master?driver=ODBC+Driver+17+for+SQL+Server")
# engine = create_engine("mssql+pyodbc://sa:<YourStrong!Passw0rd>@localhost:1433/master")
connection = engine.connect()

r = connection.execute('SELECT optname, value, major_version, minor_version, revision, install_failures FROM master.dbo.MSreplication_options;')
# r2 = connection.execute('CREATE TABLE Employees (Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY, Name NVARCHAR(50), Location NVARCHAR(50));')
# r3 = connection.execute("INSERT INTO Employees (Name, Location) VALUES (N'Jared', N'Australia'), (N'Nikita', N'India'), (N'Tom', N'Germany');")

for row in r:
    print(row)

connection.close()
