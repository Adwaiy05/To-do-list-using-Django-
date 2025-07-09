**To-Do List app**

An app to manage a to-do list, which has been built using Django

**Features:**
- View all pending tasks
- Add any new tasks
- Mark tasks as complete/incomplete
- Edit any task
- Delete any task

_No Java! - just HTML forms and page refreshes_

---

## How to run it locally

### 1. Create a virtual environment for Python
```bash
python -m venv venv
```

### 2. Activate the virtual environment 
- Windows
```bash
venv\Scripts\activate
```

- Mac/Linux
```bash
source venv/bin/activate
```
How do you know if the virtual environment is activated? 
- You should see (venv) at the start of your terminal line.

### 3. Install dependencies
```bash
pip install django
```

### 4. Apply database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the development server
```bash
python manage.py runserver
```

After this, open your web browser and go to: http://127.0.0.1:8000/ . Happy testing!