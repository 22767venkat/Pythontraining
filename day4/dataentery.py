import pyodbc
server='.'
database='venkat'
username='sa'
password='venkat@123'
cxcn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


mycursor=cxcn.cursor()
res=mycursor.execute("select empno,sal,comm,(sal+comm) as salary from emp")
myrecs=res.fetchall();
print(myrecs)