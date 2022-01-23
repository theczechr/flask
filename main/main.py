from flask import *
from logging import *
from . import db
app = Blueprint('main', __name__)
@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/profile')
#def profile():
#    return render_template('profile.html')
#@app.route('/')
#def login_stranka():
#    return render_template("prihlasovani.html")

@app.route("/prvni_ukol")
def prvni_ukol_stranka():
    return render_template("prvni_ukol.html")

@app.route("/druhy_ukol")
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
