FROM cgr.dev/chainguard/python:latest@sha256:8d7bf8f0939c186fc2dbfc252a22df0fcc1ecef2490ea3f124aa448e14bf19c9 as builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/linky/venv/bin:$PATH"

WORKDIR /linky

RUN python -m venv /linky/venv
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest@sha256:8d7bf8f0939c186fc2dbfc252a22df0fcc1ecef2490ea3f124aa448e14bf19c9

WORKDIR /linky

ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

COPY linky.py linky.png ./
COPY --from=builder /linky/venv /venv

ENTRYPOINT [ "python", "/linky/linky.py" ]
