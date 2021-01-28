from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
import os


app = Flask(__name__)
app.secret_key = '5791628bb0baweAJWoC9j1o2ij12ba23235'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MP_EMAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('MP_USER_PASS')
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guides')
def guides():
    return render_template('guides.html')

@app.route('/zombicide')
def zombicide():
    return render_template('zombicide.html')

@app.route('/wasteland')
def wasteland():
    return render_template('wasteland.html')

@app.route('/bloodrage')
def bloodrage():
    return render_template('bloodrage.html')

@app.route('/swrebellion')
def swrebellion():
    return render_template('swrebellion.html')

@app.route('/risingsun')
def risingsun():
    return render_template('risingsun.html')

@app.route('/jade')
def jade():
    return render_template('jade.html')

@app.route('/taintedgrail')
def taintedgrail():
    return render_template('taintedgrail.html')

@app.route('/materials')
def materials():
    return render_template('materials.html')

@app.route('/diysundrop')
def diysundrop():
    return render_template('diysundrop.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(subject=f"Miniatures Palace Msg from {name}", body=f"E-Mail:Name: {name}\nEmail: {email}\nMessage: {message}", 
        sender=os.environ.get('MP_EMAIL'), recipients=[os.environ.get('MP_EMAIL')])
        mail.send(msg)
        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
