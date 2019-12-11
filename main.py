from flask import Flask, Response, redirect, url_for, render_template, request, flash
from flask_login import LoginManager
from flask_login import UserMixin, login_user, login_required, current_user, logout_user

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

import os
import csv
import utils
import shutil
import datetime

dat = datetime.datetime.now()
datums = dat.strftime("%Y%m%d")

IELADES_VIETA = "uploads"
DATNU_VIETA = "static/dati"

class DatnesForma(FlaskForm):
    datne = FileField(validators=[FileRequired()])


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY=os.environ['SECRET_KEY']
)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_post"


class User(UserMixin):
    def __init__(self, id, parole, vards):
        self.id = id
        self.parole = parole
        self.vards = vards

    def __repr__(self):
        return f"lietotajvards: {self.id} + parole: {self.parole} + vards: {self.vards}"


users = {"test": User("test", "qwerty", "Galvenais testetajs"),
         "gundega": User("gundega", "asdf", "Princese Gundega"),
         "maiga": User("maiga", "parole", "Maiga no Ķekavas"),
         "juris": User("juris", "123", "Juris"),
         "laila": User("laila", "Zanda", "Laila"),
         "natalija": User("natalija", "Zanda", "Natālija"),
         "indra": User("indra", "pk30", "Indra")
         }


@login_manager.user_loader
def load_user(username):
    user = users[username]
    return user


@app.route('/')
def brivie_suni():
    return render_template('index.html')


@app.route('/par')
def par():
    return render_template('BrivieSuni.html')


@app.route('/macibas')
def macibas():
    testuNosaukumuListe = utils.testuSaraksts(DATNU_VIETA)
    #faili = " ".join(failuSaraksts)
    return render_template('macibas.html', faili = testuNosaukumuListe)


@app.route('/parbaude')
def parbaude():
    return render_template('parbaude.html')


@app.route('/login', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        liet_vards = request.form.get('lietotajs')
        parole = request.form.get('parole')
        remember = True if request.form.get('remember') else False
        # check if user actually exists
        print(liet_vards)
        if liet_vards in users:
            user = users[liet_vards]
        else:
            flash('User not found.')
            return redirect(url_for('login_post'))

        if not user or not user.parole == parole:
            flash('Password incorrect.')
            # if user doesn't exist or password is wrong, reload the page
            return redirect(url_for('login_post'))

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('profile'))
    else:
        return render_template('autorizacija.html')

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = DatnesForma()
    if not os.path.exists(IELADES_VIETA):
        os.makedirs(IELADES_VIETA)
    if not os.path.exists(DATNU_VIETA):
        os.makedirs(DATNU_VIETA)

    if request.method == 'POST':
        if form.validate_on_submit():
            f = form.datne.data
            failaNosaukums = secure_filename(f.filename)
            
            if not failaNosaukums.endswith(".csv"):
                flash('Nepareizs datnes formāts! Sistēma atbalsta tikai csv datņu formātus!')
                return redirect(url_for('upload'))

            f.save(os.path.join(IELADES_VIETA, failaNosaukums))
            # faila paarbaude

            (result, message) = utils.datnesStruktuurasParbaude(IELADES_VIETA,failaNosaukums)
            if result:                
                flash(message)
                #os.rename(os.path.join(IELADES_VIETA, failaNosaukums), os.path.join(DATNU_VIETA, failaNosaukums))                
                shutil.move(os.path.join(IELADES_VIETA, failaNosaukums), os.path.join(DATNU_VIETA, str(datums) + '_' + failaNosaukums))       
            else:
                flash(message)
                os.remove(os.path.join(IELADES_VIETA, failaNosaukums))        
        else:
            flash(
                'Notikusi pašreiz nenosakāma kļūda! Testa datne nav veiksmīgi augšupielādēta!')

    return render_template('upload.html', vards=current_user.vards, form=form)


@app.route('/profile')
@login_required
def profile():
    return render_template('profils.html', vards=current_user.vards)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('autorizacija.html')


@app.route('/parbaudei')
@login_required
def parbaudei():
    testuNosaukumuListe = utils.testuSaraksts(DATNU_VIETA)
    #faili = " ".join(failuSaraksts)
    return render_template('parbaude.html', faili = testuNosaukumuListe)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
