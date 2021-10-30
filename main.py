from flask import Flask, render_template, request, make_response, session, flash, g, redirect, url_for
from flask_wtf import CSRFProtect
from SQLFunctions import getAllInOut, getInOut

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'  
csrf = CSRFProtect(app)




@app.route("/")
def index():
    return redirect(url_for('entradas'))


@app.route("/entradas")
def entradas():
    return render_template("entradas.html", entradas = getAllInOut())


@app.route("/ey/<id>")
def ey(id):
    print('EYYYYYYYYYYY', id)
    return render_template("entradaN.html", entrada = getInOut(1))





































if __name__ == "__main__":
    app.run(debug=True)