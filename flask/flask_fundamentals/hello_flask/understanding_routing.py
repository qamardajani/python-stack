from flask import Flask
app = Flask(__name__)   
@app.route('/')         
def hello_world():
    return "hello world !"
@app.route('/Dojo')         
def hello_dojo():
    return "Dojo!"
@app.route('/say/<name>')         
def the_name(name):
    return f" say {name}"
@app.route('/repeat/<num>/<smth>')         
def the_name2(sum,smth):
    return (smth + " ")* int(num)

if __name__=="__main__":     
    app.run(debug=True)