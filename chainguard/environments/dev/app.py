from flask import Flask, render_template, request, jsonify
import redis
import string
import random
import os
from prometheus_client import Counter, generate_latest  # Adicionando a importação necessária

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST")
redis_port = os.environ.get("REDIS_PORT")
redis_user = os.environ.get("REDIS_USER")
redis_pass = os.environ.get("REDIS_PASS")

r = redis.StrictRedis(host=redis_host, port=redis_port, password="", decode_responses=True)

senha_gerada_counter = Counter('senha_gerada', 'Contador de senhas geradas')


def criar_senha(tamanho, incluir_numeros, incluir_caracteres_especiais):
    caracteres = string.ascii_letters

    if incluir_numeros:
        caracteres += string.digits

    if incluir_caracteres_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choices(caracteres, k=tamanho))

    return senha

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tamanho = int(request.form.get('tamanho', 8))
        incluir_numeros = request.form.get('incluir_numeros') == 'on'
        incluir_caracteres_especiais = request.form.get('incluir_caracteres_especiais') == 'on'
        senha = criar_senha(tamanho, incluir_numeros, incluir_caracteres_especiais)

        r.lpush("senhas", senha)
        senha_gerada_counter.inc()
    senhas = r.lrange("senhas", 0, 9)
    if senhas:
        senhas_geradas = [{"id": index + 1, "senha": senha} for index, senha in enumerate(senhas)]
        return render_template('index.html', senhas_geradas=senhas_geradas, senha=senhas_geradas[0]['senha'] or '' )
    return render_template('index.html')


@app.route('/api/gerar-senha', methods=['POST'])
def gerar_senha_api():
    dados = request.get_json()

    tamanho = int(dados.get('tamanho', 8))
    incluir_numeros = dados.get('incluir_numeros', False)
    incluir_caracteres_especiais = dados.get('incluir_caracteres_especiais', False)

    senha = criar_senha(tamanho, incluir_numeros, incluir_caracteres_especiais)
    r.lpush("senhas", senha)
    senha_gerada_counter.inc()

    return jsonify({"senha": senha})

@app.route('/api/senhas', methods=['GET'])
def listar_senhas():
    senhas = r.lrange("senhas", 0, 9)

    resposta = [{"id": index + 1, "senha": senha} for index, senha in enumerate(senhas)]
    return jsonify(resposta)

@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/health')
def ping():
   return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)