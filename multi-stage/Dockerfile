 
# Etapa 1: Construção
FROM ubuntu:22.04@sha256:d80997daaa3811b175119350d84305e1ec9129e1799bba0bd1e3120da3ff52c3 AS builder
# A instrução FROM especifica a imagem base para a etapa de construção.
# Neste caso, utiliza a imagem do Ubuntu 22.04 como base.

# Instala o servidor web Nginx e outras dependências necessárias
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*
# Este comando Dockerfile instala o servidor web Nginx no contêiner.
# Ele atualiza o sistema operacional e, em seguida, usa o comando apt-get para instalar o pacote nginx.
# O parâmetro "-y" é usado para confirmar automaticamente todas as perguntas de instalação.
# Por fim, o comando "rm -rf /var/lib/apt/lists/*" remove os arquivos de lista de pacotes desnecessários para economizar espaço em disco.

# Copia o arquivo index.html para o diretório /var/www/html/ dentro do container
COPY index.html /var/www/html/

# Etapa 2: Imagem final
FROM ubuntu:22.04@sha256:d80997daaa3811b175119350d84305e1ec9129e1799bba0bd1e3120da3ff52c3
# A instrução FROM especifica a imagem base para a imagem final.
# Neste caso, utiliza a imagem do Ubuntu 22.04 como base.

# Copia o Nginx instalado e o arquivo index.html da etapa de construção para a imagem final
COPY --from=builder /etc/nginx /etc/nginx
COPY --from=builder /usr/sbin/nginx /usr/sbin/nginx
COPY --from=builder /var/www/html /var/www/html

# Expõe a porta 80 para tráfego HTTP.
EXPOSE 80

# Define o diretório de trabalho como /var/www/html/ dentro do container
WORKDIR /var/www/html/

# O comando CMD especifica o comando a ser executado quando o contêiner é iniciado.
# Neste caso, inicia o servidor Nginx com a opção "daemon off;", que mantém o processo em execução em primeiro plano.
CMD ["nginx", "-g", "daemon off;"]

# Define a variável de ambiente APP_VERSION com o valor 1.0.0.
ENV APP_VERSION 1.0.0
