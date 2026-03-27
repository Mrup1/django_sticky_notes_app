# Sticky Notes App

A personal Sticky Notes web application built with Django. It allows users to register, log in, and manage their own private collection of colored sticky notes.

Created by: Subhan Rauf (22p9389)

## Setup Instructions

1. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # OR: venv\Scripts\activate on Windows
   ```

2. **Install Django**:
   ```bash
   pip install django
   ```

3. **Apply Database Migrations**:
   In the directory containing `manage.py`, run:
   ```bash
   python manage.py migrate
   ```

4. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/`. You can register a new account to start creating notes.

## Features Included
- Complete user registration and authentication cycle
- Create, Read, Update, and Delete notes cleanly
- Dedicated user ownership (users only see their own notes)
- Aesthetic UI designed with pure CSS / Glassmorphism
- Custom color-picker for sticky notes
