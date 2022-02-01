from flask import *
from flask_login import current_user, login_required, logout_user
from logging import *
from . import db
from main.odpovedi import *
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = MyForm(request.form)
    print(form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
    return render_template('signup.html', form=form)



@app.route("/prvni_ukol") #definovani url
@login_required # pusti vas na stranku co je definovana RadioField(u'Full Name')(u'Full Name')RadioField(u'Full Name')RadioField(u'Full Name') radek vys pouze kdyz jste prihlaseni
def prvni_ukol_stranka():
    return render_template("prvni_ukol.html", name=current_user.name) #nastavuje ze jste prihlaseni pod xxxxx jmenem je 

@app.route('/prvni_ukol', methods=['POST'])
@login_required
def prvni_ukol():
    global spravne
    odpoved = "ano"
    current_user.odpoved = request.form["answer"] # timto zpusobem dostaneme ze stranky odpoved
    if current_user.odpoved == odpoved:
        spravne = True
        print(current_user)
        
    #with open("answers", "w+") as myfile:
    #    myfile.write(text) # text by tady bylo napriklad vysledky ukolu, urcite zahashovat!
    # - toto si udelejte jak chcete, proste lokalni ukladani kdyby ukladani na serveru padlo lol?
    return render_template("rozcestnik.html", odpoved="gj") # vraci zpatky na rozcestnik, udelejte si jak chce
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
    