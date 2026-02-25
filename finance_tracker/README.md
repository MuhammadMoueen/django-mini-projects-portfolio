# Finance Tracker

A professional finance tracking system built with Django REST Framework featuring a modern Black & White UI theme with smooth animations.

## Features

- **User Authentication**: Secure registration and login system with token-based authentication
- **Income Tracking**: Add, view, and delete income records
- **Expense Tracking**: Add, view, and delete expense records
- **Category Management**: Organize finances with customizable categories
- **Financial Reports**: Real-time summaries, monthly reports, and category-wise spending analysis
- **Professional UI**: Modern Black & White theme with smooth CSS animations
- **Secure API**: Token-based authentication ensures users only access their own data
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Tech Stack

- **Backend**: Django 5.2.7, Django REST Framework 3.15.2
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Authentication**: Token-based authentication
- **API**: RESTful API architecture

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd finance_tracker
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create superuser (optional)
```bash
python manage.py createsuperuser
```

6. Run development server
```bash
python manage.py runserver
```

7. Access the application at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/profile/` - Get user profile

### Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create category
- `GET /api/categories/{id}/` - Get category details
- `PUT /api/categories/{id}/` - Update category
- `DELETE /api/categories/{id}/` - Delete category

### Income
- `GET /api/incomes/` - List all incomes
- `POST /api/incomes/` - Create income
- `GET /api/incomes/{id}/` - Get income details
- `PUT /api/incomes/{id}/` - Update income
- `DELETE /api/incomes/{id}/` - Delete income

### Expenses
- `GET /api/expenses/` - List all expenses
- `POST /api/expenses/` - Create expense
- `GET /api/expenses/{id}/` - Get expense details
- `PUT /api/expenses/{id}/` - Update expense
- `DELETE /api/expenses/{id}/` - Delete expense

### Reports
- `GET /api/summary/` - Get financial summary (total income, expense, balance)
- `GET /api/monthly-report/` - Get monthly report (accepts year and month params)
- `GET /api/category-report/` - Get category-wise spending report

## Project Structure

```
finance_tracker/
├── api/                      # Main API application
│   ├── models.py            # Database models
│   ├── serializers.py       # API serializers
│   ├── views.py             # API views
│   ├── admin.py             # Admin configuration
│   └── urls.py              # API URLs
├── finance_tracker/         # Project settings
│   ├── settings.py          # Django settings
│   └── urls.py              # Main URL configuration
├── static/                  # Static files
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   └── js/
│       ├── main.js          # Global JavaScript
│       └── dashboard.js     # Dashboard functionality
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── login.html          # Login page
│   ├── signup.html         # Signup page
│   └── dashboard.html      # Dashboard page
├── requirements.txt         # Python dependencies
└── manage.py               # Django management script
```

## Usage

1. **Sign Up**: Create a new account at `/signup/`
2. **Login**: Access your dashboard at `/login/`
3. **Add Categories**: System automatically creates default categories
4. **Track Income**: Add income records with amount, date, category, and notes
5. **Track Expenses**: Add expense records similarly
6. **View Summary**: See real-time totals and current balance
7. **Manage Records**: View and delete transactions from the dashboard

## Security

- Token-based authentication for API access
- User-specific data isolation
- Password validation and hashing
- CSRF protection enabled
- Input validation on all forms

## License

MIT License
