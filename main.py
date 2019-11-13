from flask import Flask, Response, redirect, url_for, render_template, request, flash
from flask_login import LoginManager
from flask_login import UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'bzzbzzbzz'
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

users = { "test": User("test", "qwerty", "Galvenais testetajs"),
        "gundega": User("gundega", "asdf", "Princese Gundega"),
         "maiga": User("maiga", "parole", "Maiga no Ķekavas"),
         "juris": User("juris", "123", "Juris")
         }

@login_manager.user_loader
def load_user(username):
  user = users[username]
  return user


@app.route('/')
def brivie_suni():
    return render_template('index.html')


@app.route('/macibas')
def macibas():
    return render_template('macibas.html')


@app.route('/parbaude')
def parbaude():
    return render_template('parbaude.html')

  
@app.route('/login', methods=['GET','POST'])
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
      return redirect(url_for('login_post')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('profile'))
  else:
    return render_template('autorizacija.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profils.html', vards=current_user.vards)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('autorizacija.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
