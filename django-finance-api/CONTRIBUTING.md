# Contributing to Finance Tracker

Thank you for considering contributing to Finance Tracker! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/finance_tracker.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/Mac: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`

## Development Workflow

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run tests: `python manage.py test`
4. Commit your changes: `git commit -m "Add descriptive message"`
5. Push to your fork: `git push origin feature/your-feature-name`
6. Create a Pull Request

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Write unit tests for new features

## Testing

- Run all tests before submitting PR: `python manage.py test`
- Add tests for new features
- Maintain test coverage above 80%

## Commit Messages

- Use clear and descriptive commit messages
- Start with a verb in present tense (Add, Fix, Update, Remove)
- Keep first line under 50 characters
- Add detailed description if needed

## Pull Request Guidelines

- Provide clear description of changes
- Reference related issues
- Include screenshots for UI changes
- Ensure all tests pass
- Update documentation if needed

## Code Review

- Be respectful and constructive
- Respond to feedback promptly
- Make requested changes in separate commits

## Questions?

Feel free to open an issue for any questions or concerns.
