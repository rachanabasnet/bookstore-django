# Django Project

## Project Overview
This project is an online bookstore. 
This project includes features such as:
- View the Latest Trending Books
- Add the books to the cart
- Order the books
- User Authentication & Profile Update
- View Order History

---

## Technologies Used
- **Programming Language:** Python
- **Framework:** Django
- **Database:** SQLite
- **Frontend:** HTML & CSS

---

## Installation

### Prerequisites
- Python (>= 3.8)
- Pip
- Virtualenv 

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rachanabasnet/bookstore-django.git
   cd bookstore-django
   ```
   
2. Create and activate virtual environment
   ```bash
   python -m venv env
   source env/bin/activate # For Linux/MacOS
   env\Scripts\activate  # For Windows
   ```
   
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
   
4. Apply database migrations
   ```bash
   python manage.py migrate
   ```
   
5. Run the server
   ```bash
   python manage.py runserver
   ```
