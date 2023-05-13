from flask import Flask, request, render_template
from supabaseMgr import SupabaseMgr

app = Flask(__name__)
DbMgr = SupabaseMgr()



@app.route('/',methods=['GET', 'POST'] )
def traccia_risparmi():  # put application's code here

    if request.method == 'GET':
        return render_template('base.html', risparmi_totali=DbMgr.risparmi_totali())
    else:

        value = request.form['valore']
        autore = request.form['autore']

        DbMgr.aggiungi_risparmio(autore, value)
        return render_template('base.html', risparmi_totali=DbMgr.risparmi_totali())
if __name__ == '__main__':
    app.run()
