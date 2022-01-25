from flask import *
from flask_login import login_required, current_user
from logging import *
from . import db
app = Blueprint('main', __name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/rozcestnik")
def rozcestnik():
    return render_template("rozcestnik.html")


@app.route("/prvni_ukol")
@login_required
def prvni_ukol_stranka():
    return render_template("prvni_ukol.html", name=current_user.name)

@app.route("/druhy_ukol")
@login_required
def druhy_ukol_stranka():
    return render_template('druhy_ukol.html')


@app.route('/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form["password"]
    print(username)
    print(password)
    #with open("answers", "w+") as myfile:
    #    myfile.write(text)
    return redirect("/prvni_ukol")

    
@app.route('/prvni_ukol', methods=['POST'])
def prvni_ukol():
    odpoved = request.form["answer"]
    print(odpoved)
    #with open("answers", "w+") as myfile:
    #    myfile.write(text)
    return redirect("/druhy_ukol")

@app.route('/druhy_ukol', methods=['POST'])
def druhy_ukol():
    odpoved = request.form["answer"]
    print(odpoved)
    #with open("answers", "w+") as myfile:
    #    myfile.write(text)
    return redirect("/")
