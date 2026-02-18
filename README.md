\# Vidly (Django)



A modern Django web app inspired by the Vidly project.



\## Features

\- Movies list (Bootstrap)

\- Movie detail page

\- Sort by Title / Genre / Price (Asc/Desc)

\- Admin panel (Movies, Genres, Customers, Rentals)

\- Seed data via fixtures



## Screenshots 

###Movies_page 
[Vidly.pdf](https://github.com/user-attachments/files/25394402/Vidly.pdf)

###Admin_page
<img width="1899" height="750" alt="Admin2" src="https://github.com/user-attachments/assets/7e5c4778-69d6-45a4-8926-900c78614091" />
<img width="1893" height="703" alt="Admin1" src="https://github.com/user-attachments/assets/481c4c6b-7a26-4de7-a082-b55ba6bf16db" />




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





