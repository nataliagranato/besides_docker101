FROM cgr.dev/chainguard/python:latest@sha256:172a288df4aeb380077d5efabdbda0da08766c8b97f9c3270266bbc0bb47c1b0 as builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/linky/venv/bin:$PATH"

WORKDIR /linky

RUN python -m venv /linky/venv
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest@sha256:172a288df4aeb380077d5efabdbda0da08766c8b97f9c3270266bbc0bb47c1b0

WORKDIR /linky

ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

COPY linky.py linky.png ./
COPY --from=builder /linky/venv /venv

ENTRYPOINT [ "python", "/linky/linky.py" ]
