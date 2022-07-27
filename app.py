import os
from flask import Flask,render_template, request

app = Flask(__name__)
 
@app.route('/')
def form():  
    return render_template('form.html')
 
port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)  

    
#app.run(host='localhost', port=5000)
