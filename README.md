#  Trabajo Practico IDS N°2 

# Alumno 
    - Brian David Lucero | 114443

mkdir mi_proyecto
cd mi_proyecto/
sudo apt install python3.12-venv
mkdir .venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install flask
flask run
'export FLASK_DEBUG=True'
'flask run port 5000'
'flak run --port=6969'
deactivate


sudo apt update
sudo apt upgrade -y      ----> tarda
sudo apt install curl -y
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm alias default 22.14.0
node -v                  ---> fijar si esta instalado
sudo apt install nodejs


# - PARA CORRER FLASK SCRIPT
 #!/bin/bash
 
 sudo apt install python3-pip
 
 
 mkdir EjPractico2
 cd EjPractico2
 
 #crear estructura basica
 mkdir .venv
 touch app.py
 mkdir static
 cd static
 mkdir css
 mkdir images
 cd ..
 
 mkdir templates
 
 echo '
 from flask import Flask
 app = Flask(__name__)
 
 @app.route("/")
 def index():
     return "<h1>Hola Mundo!</h1>"
 
 if __name__ == "__main__":
     app.run("127.0.0.1", port="5001", debug=True)' >> app.py
 
 
 #crear entorno virtual
 pipenv install flask
 pipenv shell
 
 #Seteo de variables para correr flask
 export FLASK_APP=app.py
 export FLASK_DEBUG=1
 
 flask run
