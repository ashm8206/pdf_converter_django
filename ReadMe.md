```
---
Author: Aishwarya Mali
Date:   09/16/24
---
```

### Table of Contents

- [Project](#project)
- [Architecture](#architecture)
- [Code design](#code-design)
- [Run Job](#running-job)
- [Output](#output)
- [References](#references)

## Project

This project demonstrates a simple asynchronous workflow queue, used to run long running processes in the background without affecting User experience

### Project Outcomes:

Use Distributed task Queue Celery with Redis Backend to perform long-running tasks in the background, without affecting main process in web app

## Architecture

[![Celery Explanation Video](https://img.youtube.com/vi/hFIkEGtW6vE/0.jpg)](https://www.youtube.com/watch?v=hFIkEGtW6vE)

## Code design

![Code Organization ](https://github.com/ashm8206/pdf_converter_django/blob/main/img_to_pdf_app/imgs/CodeOrganization.png)

## Running job

1. Create Python Env

```bash
python3 -m venv pdf_uploader
source pdf_uploader/bin/activate`
```

2. Install Libraries

```
python3 -m pip install django celery redis fpdf
```

3. Setup Django

```
django-admin startproject image_to_pdf_app
cd image_to_pdf_app
django-admin startapp pdf_converter
```

_**Add app to Installed_apps in settings.py**_

4. Freeze Requirements

```
python3 -m pip freeze > requirements.text
```

5. Run Project

#### Run Redis Server

```
redis-server
```

#### Run Celery

```
celery -A image_to_pdf_app worker --loglevel=info
```

#### Run Django App

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Output

### Landing Page

![Landing](https://github.com/ashm8206/pdf_converter_django/blob/main/img_to_pdf_app/imgs/IndexPage.png)

### Wait for Process Page

![Wait](https://github.com/ashm8206/pdf_converter_django/blob/main/img_to_pdf_app/imgs/Async_Run_wait_page.png)

### PDF Converted Page

![Converted](https://github.com/ashm8206/pdf_converter_django/blob/main/img_to_pdf_app/imgs/Converted_Page.png)

## References

1. [Celery Explanation By SKonik](https://www.youtube.com/@s_konik)
