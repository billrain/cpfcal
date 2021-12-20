from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

RANGE = ["35 and below",
         "36 - 45",
         "46 - 50",
         "51 - 55",
         "56 - 60",
         "61 - 65",
         "66 and above"
         ]

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html", range=RANGE)

@app.route("/result", methods=["POST"])
def cpfcal():
    name=request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    salary=request.form.get("salary", type=float)
    if not salary:
        return render_template("error.html", message="Missing salary")
    age=request.form.get("age")
    if age not in RANGE:
        return render_template("error.html", message="Invalid age")

    if salary <= 6000: salary = salary
    else: salary = 6000

    if age = "35 and below":

    cpf_oa  = salary * 0.23
    cpf_sa  = salary * 0.07
    cpf_ma  = salary * 0.07

    elif age =  "36 - 45":
    cpf_oa  = salary * 0.21
    cpf_sa  = salary * 0.07
    cpf_ma  = salary * 0.09

    cpf_emp  = salary * 0.17
    cpf_self = salary * 0.20
    cpf_tot  = cpf_emp + cpf_self

    return render_template("result.html", name=name, salary=salary, age=age, cpf_emp=cpf_emp,
        cpf_self=cpf_self, cpf_tot=cpf_tot, cpf_oa=cpf_oa, cpf_ma=cpf_ma, cpf_sa=cpf_sa)
