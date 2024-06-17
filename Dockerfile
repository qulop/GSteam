FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP="run.py"

EXPOSE 8021
CMD ["flask", "run"]