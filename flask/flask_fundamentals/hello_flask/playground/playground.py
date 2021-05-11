from flask import Flask, render_template  
app = Flask(__name__)                     
@app.route('/play')                           
def play_box():

    return render_template('index2.html')   
@app.route('/play/<num>')                           
def play_box1(num):

    return render_template('index2.html', num=int(num))   

@app.route('/play/<num>/<color1>/<color2>')                           
def play_box2(num,color1,color2):

    return render_template('index2.html', num=int(num) , color1= color , color2 = color)   

    
if __name__=="__main__":
    app.run(debug=True)                   

