from flask import Flask, render_template, redirect, url_for
from flask_wtf import CSRFProtect
from SQLFunctions import getAllInOut, getInOut, getInFrom, getOutFrom, getEmployeeName, getEmployeeData, getNInOut, getInOutFromWatchlist, getEmployeesInWatchList, getAdminChanges
from TimeFunctions import getDay
app = Flask(__name__)
app.secret_key = 'eyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'  
csrf = CSRFProtect(app)



@app.route("/")
def index():
    adminName = "admin"
    n = 100
    return render_template("index.html", entradas = getNInOut(n), entradasPrioritarias = getInOutFromWatchlist(adminName, n), empleadosVigilados = getEmployeesInWatchList(adminName), cambiosAdmins = getAdminChanges(5))
    
@app.route("/entradas")
def entradas():
    return render_template("entradas.html", entradas = getAllInOut(), diaActual = getDay())

@app.route("/entrada/id/<idEntrada>")
def entrada(idEntrada): 
    return render_template("entrada.html", entrada = getInOut(idEntrada), datosEmpleado = getEmployeeData(1))

@app.route("/empleado/id/<idEmpleado>")  
def empleado(idEmpleado):
    n = 20 
    return render_template("empleado.html", entradasEmpleado = getInFrom(idEmpleado, n), salidasEmpleado = getOutFrom(idEmpleado, n), nombre = getEmployeeName(idEmpleado), diaActual = getDay())













if __name__ == "__main__":
    app.run(debug=True)