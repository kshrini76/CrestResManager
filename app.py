from flask import Flask,render_template, request

app = Flask(__name__)
 
@app.route('/')
def form():  
    return render_template('form.html')
 
  
app.run(debug = True)
    
#app.run(host='localhost', port=5000)
