from flask import Flask, render_template  
app = Flask(__name__)                     
@app.route('/play')                           
def play_box():

    return render_template('index1.html', num=int(8), num2=int(8))   
@app.route('/play/<num>')                           
def play_box1(num):

    return render_template('index1.html', num=int(4), num2=int(num))   

@app.route('/play/<x>/<y>')                           
def play_box2(x,y):

    return render_template('index1.html', num=int(x), num2=int(y) ) 

    
if __name__=="__main__":
    app.run(debug=True)                   
