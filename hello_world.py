from flask import Flask  ##import the Flask class##
from os import environ  ##import the environ dictionary fro os to get access to environment vars from Cloud9##

app=Flask(__name__)  ##creating an instance of the Flask class called app and passing in the __name__ var telling the app
##where it is being run from##

@app.route("/")
@app.route("/hello")
def say_hi():   ##function that returns "Hello World!" The function is decorated twice using the app.route method##
    return "Hello World!"
    
###@app.route("/hello/<name>")
###def hi_person(name):
###    return "Hello {}!".format(name.title())

@app.route("/hello/<name>")
def hello_person(name):
    html="""
    <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten. Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
@app.route("/jedi/<first_name>/<last_name>")
def jedi(first_name, last_name):
    html="""
      <h1>
        Your Jedi name is {}{}
      </h1>
    """
    return html.format(last_name[:3], first_name[:2])
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))