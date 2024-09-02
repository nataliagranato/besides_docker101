#!/bin/sh

# Instalar pacotes do requirements.txt
pip install -r ./requirements.txt

# Executar o comando do Flask
/usr/bin/python3 -m flask run --host=0.0.0.0