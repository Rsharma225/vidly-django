\# Vidly (Django)



A modern Django web app inspired by the Vidly project.



\## Features

\- Movies list (Bootstrap)

\- Movie detail page

\- Sort by Title / Genre / Price (Asc/Desc)

\- Admin panel (Movies, Genres, Customers, Rentals)

\- Seed data via fixtures



\## Setup (Windows)

```bash

git clone <repo-url>

cd vidly

py -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

python manage.py migrate

python manage.py loaddata fixtures/movies\_200.json

python manage.py createsuperuser

python manage.py runserver



