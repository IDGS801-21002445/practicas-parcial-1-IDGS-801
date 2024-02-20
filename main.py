import math
from flask import Flask, render_template, request,redirect, url_for
import forms
from io import open

from forms import Traductor,diccionario

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado() :

    if request.method == "POST" :
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
    nom=""
    apa = ""
    ama = ""
    email = ""
    edad =""
    alumno_clase=forms.UserForm(request.form)
    if request.method == "POST" :
        nom = alumno_clase.nombre.data
        apa = alumno_clase.apaterno.data
        ama = alumno_clase.amaterno.data
        email = alumno_clase.email.data
        edad = alumno_clase.edad.data

        print('Nombre: {}'.format(nom))
        print('apaterno: {}'.format(apa))
        print('amaterno: {}'.format(ama))
        print('edad: {}'.format(edad))
        print('email: {}'.format(email))


    return render_template("alumnos.html", form=alumno_clase,nom=nom,apa=apa,ama=ama,email=email)

@app.route("/distancias", methods=['GET','POST'])
def distancia():
    x1 = float
    x2 = float
    y1 = float
    y2 = float
    d  = float
    
    
    distancia=forms.distanciasForm(request.form)
    if request.method == "POST" :
        x1 = distancia.x1.data
        x2 = distancia.x2.data
        y1 = distancia.y1.data
        y2 = distancia.y2.data

        d= math.sqrt(abs((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
        
    return render_template("Distancia.html", form=distancia,d=d)

@app.route("/resistencias", methods=['GET','POST'])
def resitencia():
    ban1 = float
    ban2 = float
    max = ''
    tole = float
    reint = float

    color = ''
    min =''
  
    color_banda_1 = ''
    
    color_banda_2 = ''
    color_banda_3 = ''
    resitencia=forms.Resistencias(request.form)
    if request.method == "POST" :
        
        ban1 = resitencia.ban1.data
        ban2 = resitencia.ban2.data
        ban3 = resitencia.ban3.data
        tole =  resitencia.tole.data 
        print(ban3)
        ohms= resitencia.ban1.data + resitencia.ban2.data
        if resitencia.tole.data == '.05':
            reint = .05
        if resitencia.tole.data == '.1':
            reint = .1

       
      

        if ban1 == '0':
            color_banda_1 = "black"
        elif ban1 == '1':
            color_banda_1 = "brown"
        elif ban1 == '2':
            color_banda_1 = "red"
        elif ban1 == '3':
            color_banda_1 = "orange"
        elif ban1 == '4':
            color_banda_1 = "yellow"
        elif ban1 == '5':
            color_banda_1 = "green"
        elif ban1 == '6':
            color_banda_1 = "blue"
        elif ban1 == '7':
            color_banda_1 = "purple"
        elif ban1 == '8':
            color_banda_1 = "gray"
        elif ban1 == '9':
            color_banda_1 = "white"

        if ban2 == '0':
            color_banda_2 = "black"
        elif ban2 == '1':
            color_banda_2 = "brown"
        elif ban2 == '2':
            color_banda_2 = "red"
        elif ban2 == '3':
            color_banda_2 = "orange"
        elif ban2 == '4':
            color_banda_2 = "yellow"
        elif ban2 == '5':
            color_banda_2 = "green"
        elif ban2 == '6':
            color_banda_2 = "blue"
        elif ban2 == '7':
            color_banda_2 = "purple"
        elif ban2 == '8':
            color_banda_2 = "gray"
        elif ban2 == '9':
            color_banda_2 = "white"

        if ban3 == '1':
            color_banda_3 = "black"
        elif ban3 == '10':
            color_banda_3 = "brown"
        elif ban3 == '100':
            color_banda_3 = "red"
        elif ban3 == '1000':
            color_banda_3 = "orange"
        elif ban3 == '10000':
            color_banda_3 = "yellow"
        elif ban3 == '100000':
            color_banda_3 = "green"
        elif ban3 == '1000000':
            color_banda_3 = "blue"
        elif ban3 == '10000000':
            color_banda_3 = "purple"
        elif ban3 == '100000000':
            color_banda_3 = "gray"
        elif ban3 == '1000000000':
            color_banda_3 = "white"

        tole = float(ohms)*int(ban3)
        max =  tole + float(ohms)*reint
        min =  tole - float(ohms)*reint
    return render_template("resistencias.html",form=resitencia,tole=tole,reint=reint,max=max,min=min,color_banda_1=color_banda_1,color_banda_2=color_banda_2,color_banda_3=color_banda_3)

def colorb(banda):
        if banda == '0':
            color = "black"
        elif banda == '1':
            color = "brown"
        elif banda == '2':
            color = "red"
        elif banda == '3':
            color = "orange"
        elif banda == '4':
            color = "yellow"
        elif banda == '5':
            color = "green"
        elif banda == '6':
            color = "blue"
        elif banda == '7':
            color = "purple"
        elif banda == '8':
            color = "gray"
        elif banda == '9':
            color = "white"

        return color
    
@app.route("/leerArchivos", methods=['GET','POST'])
def diccionario():
    palabra = ''
    word = ''
    read = '' 
    diccionario=forms.diccionario(request.form)
    if request.method == "POST" :
        palabra = diccionario.palabra.data
        word = diccionario.word.data
        idioma = diccionario.idioma.data
        buscar= diccionario.buscar.data
        # archivo1=open('archivo.txt','r')
        # read = archivo1.read()

        if request.form['submit_button'] == 'Registrar':
            archivo1=open('archivo.txt','a')

            archivo1.write(palabra)
            archivo1.write('\n' +word)
            archivo1.close()

            print('Registrar')
            read = 'Registrar'

        if request.form['submit_button'] == 'buscar':
            print('Buscar')
            read = 'buscar'
            traducir = ''

            traducir = buscar_contenido(buscar, idioma)

        # archivo1=open('archivo.txt','r')
        # print(archivo1.read())
        ##Seek reinicia la lectura hasta alguna posición podiendo así leer varias veces un archivo
        # archivo1.seek(0)
        # print(archivo1.read())

        #print(archivo1.readlines())

        
    return render_template("leerArchivos.html", form=diccionario,read=read,traducir=traducir)

def buscar_contenido(palabra_buscar, idioma):
    try:
        with open('archivo.txt', 'r') as archivo:
            lineas = archivo.readlines()

            if idioma == 'Espaniol':
                # Buscar la palabra en español y obtener la traducción en inglés
                for i, linea in enumerate(lineas):
                    if linea.strip() == palabra_buscar:
                        if i + 1 < len(lineas):
                            print(f'Traducción: {lineas[i + 1].strip()}')
                            return f'Traducción: {lineas[i + 1].strip()}'
                        else:
                            return 'No se encontró la traducción'

            elif idioma == 'English':
                # Buscar la palabra en inglés y obtener la traducción en español
                for i, linea in enumerate(lineas):
                    if linea.strip() == palabra_buscar:
                        if i - 1 >= 0:
                            print(f'Traducción: {lineas[i - 1].strip()}')
                            return f'Traducción: {lineas[i - 1].strip()}'
                        else:
                            return 'No se encontró la traducción'

            return f'Palabra no encontrada: {palabra_buscar}'

    except FileNotFoundError:
        return 'El archivo no existe'
    except Exception as e:
        return f'Error al buscar: {str(e)}'


if __name__ == "__main__":

    app.run(debug=True)

