FROM python:3.13-slim-bullseye

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./src .

CMD ["python" ,"-m", "http.server", "8000"]