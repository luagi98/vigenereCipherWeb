from vigenere import *
from flask import Flask
from flask import render_template,redirect,request
from flask.helpers import url_for
app = Flask(__name__)

# Main route, there is a profile card about me and my contact information

@app.route('/')
def inicio():
     return render_template('index.html')

# Proyect route, you can choose between encrypt, decrypt and see the database associated of this project

@app.route('/project')
def project():
     return render_template('project.html')

# Encrypt route, there is a form where you have to introduce text that you wanna encrypt with vigenere and the password that will be used in the encrypted

@app.route('/project/encrypt',methods=["GET","POST"])
def encrypt():
     if request.method == "POST":
          text = request.form.get("textInput")
          password = request.form.get("cipherPassword")
          encryptedText = code(text,password,["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
          return render_template("crypt.html",method="encrypt",flag=True,cryptedText = encryptedText)
     elif request.method == "GET":
          return render_template('crypt.html',method="encrypt",flag=False)

# Decrypt route, there is a form where you have to introduce text that you wanna decrypt with vigenere and the password that will be used in the decrypted

@app.route('/project/decrypt',methods=["GET","POST"])
def decrypt():
     if request.method == "POST":
          text = request.form.get("textInput")
          password = request.form.get("cipherPassword")
          decryptedText = decode(text,password,["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
          return render_template("crypt.html",method="decrypt",flag=True,cryptedText = decryptedText)
     elif request.method == "GET":
          return render_template('crypt.html',method="decrypt",flag=False)

# Database route, this method isn't already supported

@app.route('/project/database')
def database():
     return render_template('database.html')

if __name__ == '__main__':
    app.run(debug=True)
