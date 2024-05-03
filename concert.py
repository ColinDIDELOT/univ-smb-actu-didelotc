# save this as app.py
from flask import Flask
from flask import render_template
import json
import os
from flask import request


app = Flask(__name__)

@app.route("/")
def start():
    return render_template('start.html')

@app.route("/jazz")
def Jazz():
    with open('JSONS/Actualite2.json') as f:
        data = json.load(f)
    return render_template('Jazz.html', data=data)

@app.route("/Rock")
def rock():
    with open('JSONS/Actualite1.json') as f:
        data = json.load(f)
    return render_template('Rock.html', data=data)

@app.route("/electro")
def electro():
    with open('JSONS/Actualite3.json') as f:
        data = json.load(f)
    return render_template('electro.html', data=data)

@app.route("/commentaire", methods=['GET,POST'])
def commentaire():
    if request.method == 'POST':
        return commentaires()
    else:
        return render_template('commentaire.html')

def commentaires():
    return "merci de votre commentaire"


if __name__ == '__main__':
    app.run(debug=True)