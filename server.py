# From the Generator directory imported the PasswordGenerator.py for the use of PasswordGenerator Function :-
from Generator import PasswordGenerator
# Using flask for the framework
from flask import Flask, render_template, request

app = Flask("Password Generator")

@app.route("/password")
def password():
    length = request.args.get("PasswordLength")
    return PasswordGenerator.PasswordGenerator(length)

@app.route("/")
def renderIndexPage():
    return render_template('index.html') #referencing the index.html file in templates for the server.

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
    
    
