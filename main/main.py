from flask import *
from flask_login import login_required, current_user
from logging import *
from . import db
app = Blueprint('main', __name__) # inicializace appky
@app.route('/') # landing page, klidne si dejte landing page login nebo rozcestnik, zalezi uz na vas.
def index():
    if current_user.is_authenticated: 
        return redirect(url_for('main.rozcestnik')) #pokud neni user prihlasen bude zde
    else:
        return render_template('index.html') #pokud je prihlasen bude redirectnut na rozcestnik, neni pro nej duvod na tuto stranku chodit.

@app.route('/rozcestnik')
@login_required
def rozcestnik():
    return render_template('rozcestnik.html')
@app.route("/prvni_ukol") #definovani url
@login_required # pusti vas na stranku co je definovana o radek vys pouze kdyz jste prihlaseni
def prvni_ukol_stranka():
    return render_template("prvni_ukol.html", name=current_user.name) #nastavuje ze jste prihlaseni pod xxxxx jmenem je 

@app.route('/prvni_ukol', methods=['POST'])
@login_required
def prvni_ukol():
    odpoved = request.form["answer"] # timto zpusobem dostaneme ze stranky odpoved
    if odpoved == "nejaka vase odpoved":
        return True #udelejte si uz jak chcete, princip chapete:D
    print(odpoved)
    #with open("answers", "w+") as myfile:
    #    myfile.write(text) # text by tady bylo napriklad vysledky ukolu, urcite zahashovat!
    # - toto si udelejte jak chcete, proste lokalni ukladani kdyby ukladani na serveru padlo lol?
    return redirect("/rozcestnik") # vraci zpatky na rozcestnik, udelejte si jak chce
@app.route("/druhy_ukol")
@login_required
def druhy_ukol_stranka():
    return render_template('druhy_ukol.html')

@app.route('/druhy_ukol', methods=['POST'])
def login():
    answer = request.form['answer']
    #with open("answers", "w+") as myfile:
    #    myfile.write(text)
    return redirect("/rozcestnik")