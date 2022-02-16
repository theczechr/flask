from flask import *
from flask_login import current_user, login_required
from logging import *
from . import db, bodovani
from .models import Body
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
    return render_template('rozcestnik.html',name=current_user.name, stav=Body.query.filter_by(username=current_user.name).first())








@app.route('/prvni_ukol', methods=['GET','POST'])
@login_required
def prvni_ukol():
    if request.method == "POST": 
        odpoved = request.form["answer"]
        existuje = Body.query.filter_by(username=current_user.name).first()
        if existuje:
            existuje.odpoved_1 = odpoved
            bodovani.session.commit()
        else:
            data = Body(id= current_user.id, username=str(current_user.name), odpoved_1=odpoved, odpoved_2="", odpoved_3="")
            bodovani.session.add(data)
            bodovani.session.commit()
        return render_template('rozcestnik.html', stav=Body.query.filter_by(username=current_user.name).first())
    else:
        return render_template("prvni_ukol.html")

@app.route('/druhy_ukol', methods=['GET','POST'])
@login_required
def druhy_ukol():
    if request.method == "POST": 
        odpoved = request.form["answer"]
        existuje = Body.query.filter_by(username=current_user.name).first()
        if existuje:    
            existuje.odpoved_2 = odpoved
            bodovani.session.commit()
        else:
            data = Body(id= current_user.id, username=str(current_user.name), odpoved_1="", odpoved_2=odpoved, odpoved_3="")
            bodovani.session.add(data)
            bodovani.session.commit()
        return render_template('rozcestnik.html', stav=Body.query.filter_by(username=current_user.name).first())
    else:
        return render_template("druhy_ukol.html")

@app.route('/treti_ukol', methods=['GET','POST'])
@login_required
def treti_ukol():
    if request.method == "POST": 
        odpoved = request.form["answer"]
        existuje = Body.query.filter_by(username=current_user.name).first()
        if existuje:
            existuje.odpoved_3 = odpoved
            bodovani.session.commit()
        else:
            data = Body(id= current_user.id, username=str(current_user.name), odpoved_1="", odpoved_2="", odpoved_3=odpoved)
            bodovani.session.add(data)
            bodovani.session.commit()
        return render_template('rozcestnik.html', stav=Body.query.filter_by(username=current_user.name).first())
    else:
        return render_template("druhy_ukol.html")