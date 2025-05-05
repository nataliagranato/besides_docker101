FROM cgr.dev/chainguard/python:latest@sha256:46f25c4e4ff281fc374222a34cf1fdc88a0c7d36c6e9f3132ee1e005dd2f1442 as builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/linky/venv/bin:$PATH"

WORKDIR /linky

RUN python -m venv /linky/venv
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest@sha256:46f25c4e4ff281fc374222a34cf1fdc88a0c7d36c6e9f3132ee1e005dd2f1442

WORKDIR /linky

ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

COPY linky.py linky.png ./
COPY --from=builder /linky/venv /venv

ENTRYPOINT [ "python", "/linky/linky.py" ]
