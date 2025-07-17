FROM ubuntu:latest@sha256:c4570d2f4665d5d118ae29fb494dee4f8db8fcfaee0e37a2e19b827f399070d3
RUN apt-get update && apt-get install -y nginx
USER root
CMD ["nginx", "-g", "daemon off;"]
