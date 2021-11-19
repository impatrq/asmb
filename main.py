from flask import Flask, render_template, request, make_response, session, flash, g, redirect, url_for
from flask_wtf import CSRFProtect
from SQLFunctions import *
from TimeFunctions import getDay
import ast
import Forms
from Login import *
from server import server_init
import threading

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
    return render_template("index.html", entradas = getNInOut(n), entradasPrioritarias = getInOutFromWatchlist(adminName, n), empleadosVigilados = getEmployeesInWatchListFrom(adminName), cambiosAdmins = getAdminChanges(n))
    
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
    for mac, time, date, states in getAllEstadosCabinas():
        estados.append((mac, time, date, ast.literal_eval(states)))
    
    return render_template("estados.html", estados = estados, cabinas = len(estados))

@app.route("/estado/cabina/id/<macCabina>")
def cabina(macCabina):
    estado = list()

    for mac, time, date, states in getEstadoCabina(macCabina):
        boolStates = [bool(e) for e in ast.literal_eval(states)]
        estado.append((mac, time, date, boolStates))

    return render_template("estadoCabina.html", estado = estado, mac=macCabina)

@app.route("/estado/cabina/id/<macCabina>/*")
def cabinaRecientes(macCabina):
    estados = list()

    for mac, time, date, states in getEstadoCabinaRecientes(macCabina): 
        boolStates = [bool(e) for e in ast.literal_eval(states)]
        estados.append((mac, time, date, boolStates))

    return render_template("estadosRecientesCabina.html", estados = estados)

@app.route("/empleado/add", methods = ['GET', 'POST'])
def añadirEmpleado():
    newEmployee = Forms.AñadirEmpleadoForm(request.form)

    if request.method == "POST" and newEmployee.validate():
        first = newEmployee.Name.data
        last = newEmployee.Surname.data
        email = newEmployee.Email.data
        phone = newEmployee.PhoneNumber.data
        addr = newEmployee.Address.data
        zip = newEmployee.ZipCode.data
        position = newEmployee.Position.data

        if checkEmployee(first, last, email, phone):
            return redirect(url_for('empleado', idEmpleado = getEmployeeId(first, last) ) )
        else:
            createEmployee(first, last, email, phone, addr, zip, position)
            logAdminChange(session['username'], "Añadido empleado: " + first + " " + last)
            return redirect(url_for('empleado', idEmpleado = getEmployeeId(first, last) ) )

    return render_template("añadirEmpleado.html", form = newEmployee)


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

@app.route("/empleados/watchlist/add/<idEmpleado>")
def añadirEmpleadoAWatchlist(idEmpleado):

    addEmployeeToWatchlist(session['username'], idEmpleado)
    first, last = getEmployeeName(idEmpleado)
    logAdminChange(session['username'], "Añadido empleado a watchlist: " + first + " " + last)

    return redirect(url_for("index"))

@app.route("/empleados/watchlist/remove/<idEmpleado>")
def eliminarEmpleadoDeWatchlist(idEmpleado):
    
        removeEmployeeFromWatchlist(session['username'], idEmpleado)
        first, last = getEmployeeName(idEmpleado)
        logAdminChange(session['username'], "Eliminado empleado de watchlist: " + first + " " + last)

        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
    server_thread = threading.Thread(target=server_init)
    #server_thread.start()