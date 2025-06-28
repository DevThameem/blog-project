# My Blog Project

This is a personal blog project where users can read and share articles on various topics.  
The blog features a clean and responsive design built with Bootstrap, easy navigation, and simple content management powered by Django and MySQL.

## 📌 Features

- User-friendly interface for reading articles
- Responsive design for desktop and mobile using Bootstrap
- Categories and tags to organize posts
- Search functionality to find posts quickly
- Admin panel to create, edit, and delete posts powered by Django's admin interface

## 🔧 Technologies Used

- Python
- Django
- MySQL
- Bootstrap (for frontend styling)
- HTML, CSS, JavaScript

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-blog-repo.git
cd your-blog-repo
```

2. Create a virtual environment and activate it:
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3. Install dependencies:
```pip install -r requirements.txt```

4. Configure your MySQL database settings in the Django settings.py file.

5. Apply migrations:
```python manage.py migrate```

6. Create a superuser for admin access:
```python manage.py createsuperuser```

7. Run the development server:
```python manage.py runserver```

8. Open your browser and go to http://localhost:8000 to view the blog.

🧑‍💻 Author:

DevThameem 




