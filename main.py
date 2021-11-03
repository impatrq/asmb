from flask import Flask, render_template, redirect, url_for
from flask_wtf import CSRFProtect
from SQLFunctions import getAllInOut, getInOut, getInFrom, getOutFrom, getEmployeeName, getEmployeeData
from TimeFunctions import getDay
app = Flask(__name__)
app.secret_key = 'eyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'  
csrf = CSRFProtect(app)



@app.route("/")
def index():
    return redirect(url_for('entradas'))

@app.route("/entradas")
def entradas():
    return render_template("entradas.html", entradas = getAllInOut(), diaActual = getDay())

@app.route("/entrada/<idEntrada>")
def entrada(idEntrada): 
    return render_template("entrada.html", entrada = getInOut(idEntrada), datosEmpleado = getEmployeeData(1))

@app.route("/empleado")  # same q el de arriba
def empleado():
    return render_template("empleado.html", entradasEmpleado = getInFrom(1, 40), salidasEmpleado = getOutFrom(1, 40), nombre = getEmployeeName(1))













if __name__ == "__main__":
    app.run(debug=True)