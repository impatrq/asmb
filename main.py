from flask import Flask, render_template, redirect, url_for
from flask_wtf import CSRFProtect
from SQLFunctions import *
from TimeFunctions import getDay
import ast
app = Flask(__name__)
app.secret_key = 'eyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'  
csrf = CSRFProtect(app)



@app.route("/")
def index():
    adminName = "admin"
    n = 100
    return render_template("index.html", entradas = getNInOut(n), entradasPrioritarias = getInOutFromWatchlist(adminName, n), empleadosVigilados = getEmployeesInWatchList(adminName), cambiosAdmins = getAdminChanges(n))
    
@app.route("/entradas")
def entradas():
    return render_template("entradas.html", entradas = getAllInOut(), diaActual = getDay())

@app.route("/entrada/id/<idEntrada>")
def entrada(idEntrada): 
    return render_template("entrada.html", entrada = getInOut(idEntrada), datosEmpleado = getEmployeeData(1))

@app.route("/empleado/id/<idEmpleado>")  
def empleado(idEmpleado):
    return render_template("empleado.html", datosEmpleado = getEmployeeData(idEmpleado))

@app.route("/empleado/id/<idEmpleado>/EntradasRecientes")
def entradasRecientes(idEmpleado):
    n = 20
    return render_template("entradasRecientes.html", entradasEmpleado = getInFrom(idEmpleado, n), salidasEmpleado = getOutFrom(idEmpleado, n), nombre = getEmployeeName(idEmpleado), diaActual = getDay())

@app.route("/empleados")
def empleados():
    return render_template("empleados.html")

@app.route("/estados")
def estados():
    estados = getAllEstadosCabinas()
    e = list()
    for mac, time, date, states, n in estados:
        e.append((mac, time, date, ast.literal_eval(states), n))
    
    return render_template("estados.html", estados = e)







if __name__ == "__main__":
    app.run(debug=True)