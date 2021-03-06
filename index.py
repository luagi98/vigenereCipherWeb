from vigenere import *
from flask import Flask
from flask import render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for
from datetime import datetime
app = Flask(__name__)

# Connection to vigenere database using Mysql
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:@localhost:3306/vigenere'
bd = SQLAlchemy(app)

# Class model encrypted(id,originalText,encryptedtext,dateEncrypted)

class Encrypted(bd.Model):
     __tablename__='encrypted'
     id = bd.Column(bd.Integer,primary_key=True)
     originalText = bd.Column(bd.String(100))
     encryptedText = bd.Column(bd.String(100))
     dateEncrypted = bd.Column(bd.DateTime)

# Class model decrypted(id,encryptedText,decryptedtext,dateDecrypted)

class Decrypted(bd.Model):
     __tablename__='decrypted'
     id = bd.Column(bd.Integer,primary_key=True)
     encryptedText = bd.Column(bd.String(100))
     decryptedText = bd.Column(bd.String(100))
     dateDecrypted = bd.Column(bd.DateTime)
     



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
          bd.session.rollback()
          enc = Encrypted(originalText=text,encryptedText=encryptedText,dateEncrypted=datetime.now())
          # Insert in table "encrypted"
          bd.session.add(enc)
          bd.session.commit()
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
          bd.session.rollback()
          dec = Decrypted(encryptedText=text,decryptedText=decryptedText,dateDecrypted=datetime.now())
          # Insert in table "decrypted"
          bd.session.add(dec)
          bd.session.commit()
          return render_template("crypt.html",method="decrypt",flag=True,cryptedText = decryptedText)
     elif request.method == "GET":
          return render_template('crypt.html',method="decrypt",flag=False)

# Database route, this route shows all the records in vigenere database

@app.route('/project/database')
def database():
     encryptedRecords = Encrypted.query.order_by(Encrypted.id).all()
     decryptedRecords = Decrypted.query.order_by(Decrypted.id).all()
     return render_template('database.html',encryptedRecords=encryptedRecords,decryptedRecords=decryptedRecords)

if __name__ == '__main__':
    app.run(debug=True)
