FROM cgr.dev/chainguard/python:latest@sha256:7104953a948fcdfcc1305a4140d65e3be95846b109f1fee9c4f8988e215632bc@sha256:249a806fb678cb7325406516f2880a5e1425c85ba5b47eca17a9335c687f13da as builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/linky/venv/bin:$PATH"

WORKDIR /linky

RUN python -m venv /linky/venv
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest@sha256:7104953a948fcdfcc1305a4140d65e3be95846b109f1fee9c4f8988e215632bc

WORKDIR /linky

ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

COPY linky.py linky.png ./
COPY --from=builder /linky/venv /venv

ENTRYPOINT [ "python", "/linky/linky.py" ]
