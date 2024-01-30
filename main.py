from flask import Flask, render_template, request
import forms
app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado() :

    if request.methods == "POST" :
        numero1 = request.form.get("n1")
        numero2 = request.form.get("n2")
        res_suma = numero1 + numero2
        res_resta = numero1 - numero2
        res_multiplicacion = numero1 * numero2
        res_division = numero1 / numero2

        if request.form.get("suma") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_suma)
        elif request.form.get("resta") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_resta)
        elif request.form.get("multiplicacion") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_multiplicacion)
        elif request.form.get("division") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_division)
    return "No aplica"


@app.route("/alumnos", methods=['GET','POST'])
def alumnos():

    alumno_clase = forms.UserForm(request.form)
    if request.method == 'POST':
        pass 
    return render_template("alumnos.html", form=alumno_clase)

if __name__ == "__main__":
    app.run(debug=True)

