FROM python:3.10.14

WORKDIR /django

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 

RUN apt update && apt upgrade -y

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "game.wsgi:application"]