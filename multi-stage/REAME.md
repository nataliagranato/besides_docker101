# Multi stage build

Este é um exemplo de Dockerfile que utiliza a técnica de multi-stage build. Nessa abordagem utilizamos múltiplos estágios para construir a imagem Docker. No primeiro estágio, utilizamos uma imagem com um sistema operacional completo para compilar o código-fonte do nosso aplicativo. No segundo estágio, copiamos o binário gerado no primeiro estágio para uma imagem menor e mais segura, sem um sistema operacional.
