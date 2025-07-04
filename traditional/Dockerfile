
FROM ubuntu:24.04@sha256:440dcf6a5640b2ae5c77724e68787a906afb8ddee98bf86db94eea8528c2c076

RUN apt-get update && apt-get install nginx -y && rm -rf /var/lib/apt/lists/*

EXPOSE 80

COPY index.html /var/www/html/

WORKDIR /var/www/html/

CMD ["nginx", "-g", "daemon off;"]

ENV APP_VERSION 1.0.0