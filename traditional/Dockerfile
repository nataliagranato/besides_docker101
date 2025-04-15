
FROM ubuntu:24.04@sha256:1e622c5f073b4f6bfad6632f2616c7f59ef256e96fe78bf6a595d1dc4376ac02

RUN apt-get update && apt-get install nginx -y && rm -rf /var/lib/apt/lists/*

EXPOSE 80

COPY index.html /var/www/html/

WORKDIR /var/www/html/

CMD ["nginx", "-g", "daemon off;"]

ENV APP_VERSION 1.0.0