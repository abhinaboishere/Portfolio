# Abhinabo Mondal | Portfolio Website

A modern personal portfolio website built with Django, designed to showcase a developer's profile, skills, education, projects, and downloadable resume.

## Overview

This project is a personal branding website that presents:

- Professional introduction and summary
- Education background
- Technical skills and capabilities
- Project highlights and work experience style sections
- Hobbies and personal interests
- Resume download option
- Clean, responsive, visually engaging user interface

It serves as a portfolio landing page for personal and professional visibility, especially for recruiters, clients, or collaborators reviewing your background online.

## Tech Stack

- Python
- Django
- HTML
- CSS
- Bootstrap
- Font Awesome

## Project Structure

```text
MyPortfolio/
├── mywebsite/
│   ├── basesite/
│   │   ├── templates/
│   │   │   └── basesite/
│   │   │       └── home.html
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   ├── mywebsite/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── staticfiles/
│   │   ├── css/
│   │   ├── files/
│   │   └── images/
│   ├── manage.py
│   └── db.sqlite3
├── .gitignore
├── README.md
└── venv/
```

## Features

- Responsive single-page portfolio experience
- Modern gradient and card-based design
- Social media/profile links integration
- Skills and education presentation
- Downloadable resume file
- Lightweight Django setup suitable for personal portfolio hosting

## Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd MyPortfolio
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install django
```

4. Run the development server:

```bash
cd mywebsite
python manage.py runserver
```

5. Open your browser at:

```text
http://127.0.0.1:8000/
```

## Default App Behavior

The site loads the portfolio homepage from the `basesite` app, and includes a `download/` route that lets the user download the portfolio content as an HTML file.

## Resume

The project includes a resume file stored in the static assets folder:

```text
mywebsite/staticfiles/files/abhinabo_resume.txt
```

## Why This Project Exists

This portfolio website is intended to:

- present personal identity professionally
- highlight technical strengths and education
- share promising project work
- make it easy for employers or collaborators to evaluate your profile quickly
- serve as a clean online portfolio for GitHub and personal branding

## License

This project is currently intended for personal portfolio use. If you plan to publish or adapt it publicly, you may add a license file to match your intended usage.

## Author

Abhinabo Mondal

---

If you want, I can also create a more advanced version of this README with:

- badges for Python/Django
- screenshot section
- live demo link section
- project goals and achievements
- contributor/contact section
- deployment instructions for Render, Railway, or PythonAnywhere
