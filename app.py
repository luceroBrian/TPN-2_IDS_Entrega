from email.mime.text import MIMEText
import smtplib 
from flask import Flask, render_template, redirect, url_for, request

import os
EMAIL = os.environ.get("EMAIL_USER")
PASS = os.environ.get("EMAIL_PASS")


app = Flask(__name__)

@app.route('/')
def index():  
    info_evento = { 
        1:{
            "nombre": "Rally MTB 2025" ,
            "organizador": "club Social y Deportivo Unidos por el deporte" ,
            "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km" ,
            "fecha": "24 de Octubre 2025",
            "horario" : "8am" ,
            "lugar" : "Tandil, Buenos Aires" ,
            "tipo_carrera" : "MTB rural " ,
            "modalidad_costo": {
                1: {"nombre": "corta" , "valor": "100"},
                2: {"nombre": "larga" , "valor": "200"}
                },
            "Auspiciantes": ["SRAM","SPECIALIZED"]

            }
        }
    
    return render_template(
        'index.html',
        diccionario=info_evento
    ) 

@app.route('/events')
def events():   
    return render_template(
        'events.html',
    )
 

@app.route('/show/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        Nombre = request.form.get('Nombre')
        Email = request.form.get('Email') 
        Mensaje = request.form.get('Mensaje') 

        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login("lucerobriandavid1@gmail.com" , "ooevaclvjxfdzqcc")

        msg = MIMEText(f"Asunto: {Nombre} \nMensaje> {Mensaje}")

        msg["From"] = "lucerobriandavid1@gmail.com"
        msg["To"] = Email
        msg["Subject"] = Nombre

        servidor.sendmail("lucerobriandavid1@gmail.com", Email, msg.as_string())

        servidor.quit()

        return render_template('contact.html')

    else:
        return render_template('contact.html')
    



@app.route('/web/register',methods=["GET", "POST"])
def register():   
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email') 
        passd = request.form.get('passd') 
        celular = request.form.get('celular') 
        carrera_c = request.form.get('carrera_c') 
        carrera_l = request.form.get('carrera_l')  

        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login("lucerobriandavid1@gmail.com" , "ooevaclvjxfdzqcc")

        
        msg = MIMEText(f"nombre: {nombre}  \napellido: {apellido} \nemail: {email} \ncontrasena: {passd} \ncelular: {celular} \ncarrera_c: {carrera_c} \ncarrera_l {carrera_l} ")

        msg["From"] = "lucerobriandavid1@gmail.com"
        msg["To"] = email
        msg["Subject"] = email

        servidor.sendmail("lucerobriandavid1@gmail.com", email, msg.as_string())

        servidor.quit()
     
        return 'enviado'

    else:
        return render_template('register.html')

@app.errorhandler(404)
def page_not_fount(e):   
    return render_template(
       '404.html', 404
    )

if __name__ == '__main__':
    app.run("127.0.0.1", port=5001, debug=True)