# Backend app for game Truth or Lie

# Installation

--> https://github.com/Bounty2049/game_backend.git

--> py/python3 -m venv .venv

--> source .venv/bin/activate (Linux/maxOS)

--> .venv\Scripts\activate (Windows)

--> pip install -r requirements.txt

# Settings

--> cd game

--> py/python3 manage.py makemigrations

--> py/python3 manage.py migrate

--> py/python3 manage.py loaddata ./questions/fixtures/questions.json

# Run 

--> py/python3 manage.py runserver

--> open http://127.0.0.1:8000/ url in your browser
