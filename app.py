from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("cpfcal.html")

@app.route("/result", methods=["POST"])
def cpfcal():
    name=request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    salary=request.form.get("salary", type=float)
    if not salary:
        return render_template("error.html", message="Missing salary")
    bonus=request.form.get("bonus", type=float)
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

# compute yearly CPF con
    year_cpf_emp  = cpf_emp * 12 + bonus * r_emp 
    year_cpf_self = cpf_self * 12 + bonus * r_self
    year_tot = year_cpf_emp + year_cpf_self

    if year_cpf_emp <= 17340:
        year_cpf_emp = year_cpf_emp
    else:
        year_cpf_emp = 17340

    if year_cpf_self <= 17340:
        year_cpf_self = year_cpf_self
    else:
        year_cpf_self = 20400

    if year_tot <= 37740:
        year_tot = year_tot
    else:
        year_tot = 37740

    emp = ("{:.2f}".format(cpf_emp))
    eme = ("{:.2f}".format(cpf_self))
    tot = ("{:.2f}".format(cpf_tot))
    oa = ("{:.2f}".format(cpf_oa))
    sa = ("{:.2f}".format(cpf_sa))
    ma = ("{:.2f}".format(cpf_ma))
    yr_emp = ("{:.2f}".format(year_cpf_emp))
    yr_eme = ("{:.2f}".format(year_cpf_self))
    yr_tot = ("{:.2f}".format(year_tot))

    return render_template("result.html", name=name, salary=salary, age=age, emp=emp, eme=eme, tot=tot, oa=oa, ma=ma, sa=sa, yr_emp=yr_emp, yr_eme=yr_eme, yr_tot=yr_tot)
