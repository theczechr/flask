# flask
Potreba pip install flask flask-login flask-sqlalchemy
pro spusteni souboru(pokud pouzivate vscode powershell, jestli ne, najdete si to, je to legit prvni odkaz na googlu)
do konzole $env:FLASK_APP="main" *enter* 
flask run *enter*
pro import do databaze napr:
sqlite3 "nazev souboru" - v nasem pripade soubor vzdy pojmenovat db.sqlite
.mode "z ceho importujete, tady napriklad csv = (.mode csv)"
.import "jmeno vaseho souboru co importujete, pokud nastavite mode csv, tak importujete napirklad data.csv" user (je to jmeno databaze, ja to nastavil na user tak to tak prosim nechte, uberete si zbytecny problemy) 