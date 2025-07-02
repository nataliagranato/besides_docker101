
FROM ubuntu:24.04@sha256:89ef6e43e57cb94a23e4b28715a34444de91f45bd410fce3ce00819f86940a9c

RUN apt-get update && apt-get install nginx -y && rm -rf /var/lib/apt/lists/*

EXPOSE 80

COPY index.html /var/www/html/

WORKDIR /var/www/html/

CMD ["nginx", "-g", "daemon off;"]

ENV APP_VERSION 1.0.0