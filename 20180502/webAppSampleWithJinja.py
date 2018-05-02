# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    uname = request.form['username']
    pwd = request.form['password']
    if uname == 'admin' and pwd == 'password':
        return render_template('signin-ok.html', username=uname)
    return render_template('form.html', message='Input wrong', username=uname)

if __name__=='__main__':
    app.run()
