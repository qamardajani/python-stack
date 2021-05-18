from flask import Flask, render_template,request,redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def res():
    print('<h1>Submitted info</h1>')
    # print(request.form)
    user_name=request.form['name']
    user_location=request.form['locate']
    user_lang=request.form['language']
    user_mess=request.form['message']
    return render_template("show.html",user_name_temp=user_name,user_location_temp=user_location,user_lang_temp=user_lang,user_mess_temp=user_mess)

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, render_template, request, redirect
# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     name_from_form = request.form['name']
#     email_from_form = request.form['email']
#     return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)
