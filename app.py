from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = '192.168.1.25'
app.config['MYSQL_USER'] = 'crest'
app.config['MYSQL_PASSWORD'] = 'crest@123'
app.config['MYSQL_DB'] = 'flask'
app.config['MYSQL_PORT'] = 3308
 
mysql = MySQL(app)
 
@app.route('/')
def form():    
    cursor = mysql.connection.cursor()
    cursor.execute("select * from info_table") 
    data = cursor.fetchall()
    cursor.close()
    return render_template('form.html', value=data)
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':        
        return ''
     
    if request.method == 'POST':        
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
                        
        cursor.execute("select * from info_table") 
        data = cursor.fetchall()
        cursor.close()
        
        return render_template('form.html', value=data)


    
    
app.run(host='localhost', port=5000)
