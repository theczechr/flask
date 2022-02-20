from flask import *
from flask_login import current_user, login_required
from logging import *

from sqlalchemy import all_
from . import db, bodovani
from .models import Body
from main.odpovedi import *
all_users = {}
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
    return render_template('rozcestnik.html', stav=Body.query.filter_by(name=current_user.name).first())

@app.route('/register', methods=['GET','POST'])
def register():
    all_list = []
    spravne = 0
    spravne_odpovedi = [0,0,0,1,3,0,2,1,1,3,1,1,0,2,3,2,0,3,2,0,2,0,3,0,0]
    form = MyForm()
    if request.method == "POST": 
        if form.validate_on_submit():
            all_answers = form.data
            all_answers.pop('csrf_token') 
            print(all_answers)
            for value in all_answers.values():
                all_list.append(value)
            all_users[current_user.id] = all_list
            
            for i in range(len(all_list)):
                if spravne_odpovedi[i] == all_list[i]:
                    spravne +=1
            
            print(spravne)
            print(all_users)

            existuje = Body.query.filter_by(name=current_user.name).first()
            if existuje:
                existuje.pocet_bodu = spravne
                existuje.odeslano = True
                bodovani.session.commit()

            else:
                data = Body(name=str(current_user.name), pocet_bodu=spravne, odeslano=True)
                bodovani.session.add(data)
                bodovani.session.commit()
        else:
            print(form.errors)
        
        return render_template('rozcestnik.html', stav=Body.query.filter_by(name=current_user.name).first())

    else:
        return render_template('signup.html', form=form)



@app.route("/prvni_ukol") #definovani url
@login_required # pusti vas na stranku co je definovana RadioField(u'Full Name')(u'Full Name')RadioField(u'Full Name')RadioField(u'Full Name') radek vys pouze kdyz jste prihlaseni
def prvni_ukol_stranka():
    return render_template("prvni_ukol.html", name=current_user.name) #nastavuje ze jste prihlaseni pod xxxxx jmenem je 

@app.route('/prvni_ukol', methods=['POST'])
@login_required
def prvni_ukol():
    odpoved = "ano"
    current_user.odpoved = request.form["answer"] # timto zpusobem dostaneme ze stranky odpoved
    if current_user.odpoved == odpoved:
        spravne = True
        print(current_user)
    return render_template("rozcestnik.html", odpoved="gj") # vraci zpatky na rozcestnik, udelejte si jak chce
@app.route("/druhy_ukol")
@login_required
def druhy_ukol_stranka():
    return render_template('druhy_ukol.html')

@app.route('/druhy_ukol', methods=['POST'])
def login():
    answer = request.form['answer']
    return redirect("/rozcestnik")
    