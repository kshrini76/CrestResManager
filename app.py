from flask import Flask,render_template, request
import pyodbc
 
app = Flask(__name__)
 
@app.route('/')
def form():  
    return render_template('form.html')
 
  
    
app.run(host='localhost', port=5000)
