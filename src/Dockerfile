FROM cgr.dev/chainguard/python:latest-dev as builder
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt --user

FROM cgr.dev/chainguard/python:latest 
WORKDIR /app
COPY --from=builder /home/nonroot/.local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages
COPY --from=builder /app /app

ENV REDIS_HOST="redis-server"

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
