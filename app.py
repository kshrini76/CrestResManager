from flask import Flask,render_template, request
import pyodbc
import os

app = Flask(__name__)
 
server = 'workreportserver.database.windows.net'
database = 'WorkReportDB'
username = 'it'
password = 'ctspl!123'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn_str = 'DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password
 
 
@app.route('/')
def form():    
    with pyodbc.connect(cnxn_str) as conn:
        with conn.cursor() as cursor:                			
            cursor.execute(f"SELECT Name, Username FROM Users")
            data = cursor.fetchall()
    
    return render_template('form.html', value=data)
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':        
        return ''
     
    if request.method == 'POST':        
##        name = request.form['name']
##        age = request.form['age']
##        cursor = mysql.connection.cursor()
##        
##        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
##        mysql.connection.commit()
                        
        with pyodbc.connect(cnxn_str) as conn:
            with conn.cursor() as cursor:                			
                cursor.execute(f"SELECT Name, Username FROM Users")
                data = cursor.fetchall()
        
        return render_template('form.html', value=data)


    
    
port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port) 
