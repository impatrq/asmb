from flask import Flask, render_template, request, make_response, session, flash, g, redirect, url_for
from flask_wtf import CSRFProtect
from SQLFunctions import *
from TimeFunctions import getDay
import ast
import Forms
from Login import *

app = Flask(__name__)
app.secret_key = 'eyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'  
csrf = CSRFProtect(app)


@app.before_request
def before_request():
    if 'username' not in session and (request.endpoint != 'login'): # or request.endpoint != 'index'
        return redirect(url_for('login'))


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
    return render_template("empleados.html", empleados = getEmployees())

@app.route("/estados")
def estados():
    estados = list()
    for mac, time, date, states, n in getAllEstadosCabinas():
        estados.append((mac, time, date, ast.literal_eval(states), n))
    
    return render_template("estados.html", estados = estados)

@app.route("/empleado/add", methods = ['GET', 'POST'])
def añadirEmpleado():
    newEmployee = Forms.AñadirEmpleadoForm(request.form)

    if request.method == "POST" and newEmployee.validate():
        print(newEmployee.Name.data)
        print(newEmployee.Surname.data)
        
    return render_template("añadirEmpleado.html", form = empleados)


@app.route("/login", methods = ['GET', 'POST'])
def login():

    login = Forms.LoginForm(request.form)

    if request.method == 'POST' and login.validate():
        username = login.username.data
        passw = login.passw.data

        if loginAdmin(username, passw):
            session['username'] = username

            return redirect(url_for("index"))
    else:
        flash("Usuario o contraseña incorrectos")

    return render_template('login.html', form = login)


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("passw", None)

    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)