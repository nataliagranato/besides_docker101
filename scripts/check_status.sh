#!/bin/bash

# URL a ser verificada
URL="https://senhas.nataliagranato.xyz/health"

# Faz a requisição e captura o código de status HTTP
status_code=$(curl -o /dev/null -s -w "%{http_code}" "$URL")

# Verifica o código de status e exibe uma mensagem informativa
if [ "$status_code" -eq 200 ]; then
  echo "A URL $URL está acessível. Código de status HTTP: $status_code"
else
  echo "A URL $URL não está acessível. Código de status HTTP: $status_code"
fi