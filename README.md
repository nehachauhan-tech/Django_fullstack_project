# Django Fullstack Project: Tweetbar

A modern, high-performance Django-based microblogging application featuring a sleek dark theme, real-time image previews, and a secure user authentication system.

## ✨ Features

- **Dark Mode UI**: Premium aesthetics with a consistent dark theme across all pages.
- **Dynamic Navbar**: Brand "Tweetbar" with adaptive navigation (Home, Link, Dropdown) and prominent action buttons.
- **User Authentication**:
  - Secure **Login** and **Registration** with inline field validation.
  - POST-based **Logout** for Django 5.0+ compatibility.
  - Automatic redirect to the login page when creating a tweet as a guest.
- **Microblogging (Tweets)**:
  - Create, view, edit, and delete tweets easily.
  - **Real-time Image Preview** during tweet creation for better UX.
  - Images are handled securely and displayed in styled dark-mode cards.
- **Search Functionality**: A prominent, styled search bar to find tweets.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Django 5.1+
- Pillow (for image processing)
- Bootstrap 5.3+ (via CDN)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/nehachauhan-tech/Django_fullstack_project.git
    cd Django_fullstack_project
    ```

2.  **Install dependencies**:
    ```bash
    pip install django pillow
    ```

3.  **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000/` in your browser.



## 🛠 Built With

- **Backend**: [Django](https://www.djangoproject.com/)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Icons**: Lucide React / Bootstrap Icons
- **Animation**: CSS Micro-interactions

---

## 👨‍💻 Developer

Developed with ❤️ by [Neha Chauhan](https://github.com/nehachauhan-tech)
