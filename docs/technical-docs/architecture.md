---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .label }
[Jane Dane]

{: .no_toc }

# Architecture

## Overview
This web application matches students with professors based on a compatibility scoring algorithm.
It is implemented using Flask (Python) with SQLite for persistence and Jinja2 for rendering templates.

The system follows a classic MVC-like structure:
- Model: SQLite database + db.py
- View: Jinja2 templates
- Controller: Flask routes in app.py

## Technology Stack
- Backend: Python (Flask)
- Frontend: HTML, CSS, Jinja
- Database: CURRENTLY SQLite3 BUT SQAlchemy Models have been built an could be implimented. Can be found under Main-Branch models.py
- Deployment: Local / GitHub Pages (docs)

## System Flow
1. Student fills out preference form
2. Preferences are processed by Flask backend
3. Matching algorithm scores all professors
4. Results are ranked and rendered via Jinja templates

## High-Level Diagram
<img width="1066" height="913" alt="grafik" src="https://github.com/user-attachments/assets/a67162b0-baf7-4876-9277-7a355f61fd46" />


## Key Design Principles
- Simplicity 
- Readability over performance
- Modular matching logic


