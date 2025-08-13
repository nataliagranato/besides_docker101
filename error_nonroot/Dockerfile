FROM ubuntu:latest@sha256:7c06e91f61fa88c08cc74f7e1b7c69ae24910d745357e0dfe1d2c0322aaf20f9
RUN apt-get update && apt-get install -y nginx
USER root
CMD ["nginx", "-g", "daemon off;"]
