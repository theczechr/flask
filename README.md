# Flask
**Purkiáda 2022**

## Instalace
`pip install flask flask-login flask-sqlalchemy`

## Spuštění
1. `cd` do nadřazené složky
2. - VS Code PowerShell: `$env:FLASK_APP="main"`
   - Linux: `export FLASK_APP=main`
3. `flask run --host 0.0.0.0 --port xxxx` (po zavření terminálu je opět potřeba nastavit `FLASK_APP`)

| Úloha     | Port |
|-----------|------|
| Robin (ú. 2) | 7722 |
| Valon (ú. 4) | 7724 |
| Adam (ú. 7)  | 7727 |

## Import do databáze
- sqlite3 "nazev souboru" - v nasem pripade soubor vzdy pojmenovat db.sqlite
- .mode "z ceho importujete, tady napriklad csv = (.mode csv)"
- .import "jmeno vaseho souboru co importujete, pokud nastavite mode csv, tak importujete napirklad data.csv" user (je to jmeno databaze, ja to nastavil na user tak to tak prosim nechte, uberete si zbytecny problemy) 
- momentalne je v databazi nahran ucet s username: aaaaa a passw: asd - takze tim se prihlasite pres login
