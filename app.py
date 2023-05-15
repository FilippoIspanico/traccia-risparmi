from flask import Flask, request, render_template, url_for, redirect
from supabaseMgr import SupabaseMgr
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from usersMgr import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
login_manager = LoginManager()
login_manager.init_app(app)


DbMgr = SupabaseMgr()


users = {'Valeria': {'password': 'filippo'},
         'Filippo': {'password': 'valeria'}}


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

session = {}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and password == users[username]['password']:
            session["user"] = username
            user = User(username)
            login_user(user)
            return redirect(url_for('traccia_risparmi'))
        else:
            return 'Invalid username/password combination'
    else:
        return render_template('login.html')



@app.route('/',methods=['GET', 'POST'] )
@login_required
def traccia_risparmi():  # put application's code here

    if request.method == 'GET':
        return render_template(
            'template_di_prova.html',
            risparmi_totali=DbMgr.risparmi_totali(),
            risparmi_valeria=DbMgr.risparmi_attore("Valeria"),
            risparmi_filippo=DbMgr.risparmi_attore("Filippo")
                               )
    else:

        value = request.form['valore']
        print(session["user"])
        DbMgr.aggiungi_risparmio(session["user"], value)

        return render_template(
            'template_di_prova.html',
            risparmi_totali=DbMgr.risparmi_totali(),
            risparmi_valeria=DbMgr.risparmi_attore("Valeria"),
            risparmi_filippo=DbMgr.risparmi_attore("Filippo")
                               )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
