from wtforms import Form, RadioField, SelectField
from . import db

class MyForm(Form):
    name = RadioField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('GO', 'GO Lang'), ('a', 'b')])
    druha_otazka = RadioField(u"Otazka", choices=[("aaaa", "bb")])
