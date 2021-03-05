FROM python:3-alpine

WORKDIR .

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/. .

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "currency-reader:app" ]

EXPOSE 8000
