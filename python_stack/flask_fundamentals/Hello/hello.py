from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
   
    return render_template('index.html', phrase="hello", times=5)  # Return the string 'Hello World!' as a response
@app.route("/<name>") # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return f"hello {name}!"
    

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print("qamar")
#     print("23456")
#     return "username: " + username + ", id: " + id

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
