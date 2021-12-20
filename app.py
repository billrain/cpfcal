from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def cpfcal():
    name=request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    salary=request.form.get("salary", type=float)
    if not salary:
        return render_template("error.html", message="Missing salary")
    age=request.form.get("age", type=int)
    if not age:
        return render_template("error.html", message="Invalid age")

    if salary <= 6000:
        salary = salary
    else:
        salary = 6000

    r_emp  = 0.17
    r_self = 0.20

    if age <= 35:
        cpf_oa  = salary * 0.23
        cpf_sa  = salary * 0.07
        cpf_ma  = salary * 0.07

    elif age <= 45:
        cpf_oa  = salary * 0.21
        cpf_sa  = salary * 0.07
        cpf_ma  = salary * 0.09

    elif age <= 50:
        cpf_oa  = salary * 0.19
        cpf_sa  = salary * 0.08
        cpf_ma  = salary * 0.10

    elif age <= 55:
        cpf_oa  = salary * 0.15
        cpf_sa  = salary * 0.115
        cpf_ma  = salary * 0.105

    elif age <= 60:
        cpf_oa  = salary * 0.12
        cpf_sa  = salary * 0.035
        cpf_ma  = salary * 0.105
        r_emp   = 0.13
        r_self  = 0.13

    elif age <= 66:
        cpf_oa  = salary * 0.035
        cpf_sa  = salary * 0.025
        cpf_ma  = salary * 0.105
        r_emp   = 0.09
        r_self  = 0.075

    elif age <= 99:
        cpf_oa  = salary * 0.01
        cpf_sa  = salary * 0.01
        cpf_ma  = salary * 0.105
        r_emp   = 0.075
        r_self  = 0.05

    else:
        return render_template("error.html", message="Invalid age")

    cpf_emp  = salary * r_emp
    cpf_self = salary * r_self
    cpf_tot  = cpf_emp + cpf_self

    emp = ("{:.2f}".format(cpf_emp))
    eme = ("{:.2f}".format(cpf_self))
    tot = ("{:.2f}".format(cpf_tot))
    oa = ("{:.2f}".format(cpf_oa))
    sa = ("{:.2f}".format(cpf_sa))
    ma = ("{:.2f}".format(cpf_ma))

    return render_template("result.html", name=name, salary=salary, age=age, emp=emp, eme=eme, tot=tot, oa=oa, ma=ma, sa=sa)
