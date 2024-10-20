FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=development  

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
