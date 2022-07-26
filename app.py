from flask import Flask,render_template, request
import pyodbc
 
app = Flask(__name__)
 
server = 'workreportserver.database.windows.net'
database = 'WorkReportDB'
username = 'it'
password = 'ctspl!123'
driver= '{SQL Server}'
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


    
    
app.run(host='localhost', port=5000)
