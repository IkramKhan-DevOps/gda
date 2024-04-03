<p>
  <a href="https://exarth.com/">
  <img src="https://exarth.com/static/exarth/theme/logo-red-1000.svg" height="150">
  </a>
</p>
<hr>

# Galiyat Development Authority 😕
_lets build Galiyat_

application detailed down description here

# Applications

1. Website
2. Administration
3. Staff Management
4. Root Administration

# Tools and Technologies


| Category  | Tools and technologies                        |
| --------- | --------------------------------------------- |
| Frontend  | Html, Css, Javascript, JQuery, Ajax, Jinja    |
| Backend   | Django, Django-Rest-Framework``               |
| Databases | SQLite, PostGre                               |
| Server    | Linux based ubuntu server (aws/digital ocean) |

# Development Phases

1. [ ]  Application requirement engineering
2. [ ]  Application design, theme and prototyping
3. [ ]  Application core requirements implementation phase - 1 (core)
4. [ ]  Application core requirements implementation phase - 2 (api and other external services)
5. [ ]  Application core requirements implementation phase - 3 (integrations)
6. [ ]  Application testing, optimization and security checks
7. [ ]  Application Deployment

# Modules

1. [ ]  Authentication and Authorization
2. [ ]  Access and Permission Control System
3. [ ]  Notification Alerts and POP-ups

# Update 1 (0.1)

## Requirements

Please check the detailed down requirements here wrt iterations

### Functional

1. [ ]  Login
2. [ ]  Signup
3. [ ]  Dashboard

### Non-Functional

1. Security
2. Scalability
3. Optimization

---

# EXTRA

## STEPS TO RUN
1. Clone the repository
```bash
git clone https://github.com/IkramKhan-DevOps/gda.git
cd gda
```

1. Install the requirements
2. apply migrations
```bash
pip install -r requirements.txt
python manage.py makemigrations users core service_provider events management dine_stay attractions departments
python manage.py migrate
```

1. Run the server
```bash
python manage.py runserver
```

## NOTE!
- Please make sure to create a virtual environment before installing the requirements
- Please make sure to create a `.env` file and add the required environment variables use `.env.example` as a reference
- Please make sure to create a superuser to access the admin panel

## CONTRIBUTING
This project is supervised Technical Directory of <a href="">Galiyat Development Authority</a> and 
developed and maintained by <a href="https://exarth.com/">Team Exarth</a>. 


