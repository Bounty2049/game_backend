FROM python:3.10.14

WORKDIR /django

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 

RUN apt update && apt upgrade -y

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "game.wsgi:application"]