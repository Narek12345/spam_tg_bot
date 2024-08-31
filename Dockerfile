FROM python:3.10-slim

COPY requirements.txt .
RUN pip install --upgrade pip
RUN python3 -m pip install --no-dependencies -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "bot.py"]
