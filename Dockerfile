FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP="src/run.py"

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]