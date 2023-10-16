import os

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from werkzeug.utils import secure_filename

import db

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home', methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        image = request.files['file']

        if image.filename == '':
            print("Image must have a file name")
            return redirect(request.url)

        name = image.filename.split('.')[0]
        print(name)
        category, itemid = name.split('_')

        return redirect('/view_details/'+category+'/'+itemid)

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['Uname']
        password = request.form['Pass']
        status = db.login(email, password)
        if status:
            return redirect('/')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstName']
        secondname = request.form['secondName']
        mobile = request.form['phoneNo']
        email = request.form['email']
        password = request.form['password']
        status = db.insert_data(firstname, secondname, mobile, email, password)
        if status:
            return redirect('/')

    return render_template('register.html')


@app.route('/load_category/<category>')
def load_category(category):
    df = pd.read_csv('data.csv')
    data = df.loc[df["brand"] == category]

    return render_template('category.html', data=data.to_dict("records"))


@app.route('/view_details/<category>/<id>')
def view_details(category, id):
    df = pd.read_csv('data.csv')
    category = df.loc[df["brand"] == category]
    data = category.loc[df["itemId"] == int(id)]
    return render_template('view_details.html', list=data.to_dict("records")[0])


if __name__ == "__main__":
    app.run(debug=True, port=2000)
