# Contributing to Blog CRUD System

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the existing style
6. Issue that pull request!

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to all classes and functions
- Keep functions focused and small
- Comment complex logic

## Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Development Setup

1. Clone your fork of the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run tests: `python manage.py test`

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Test on different screen sizes for UI changes
- Test with different user roles (guest, authenticated, admin)

## Bug Reports

Great Bug Reports tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening)

## Feature Requests

We track feature requests as GitHub issues. When creating a feature request:

- Use a clear and descriptive title
- Provide a detailed description of the proposed feature
- Explain why this feature would be useful
- List any alternative solutions you've considered

## Code of Conduct

- Be respectful and inclusive
- Focus on what is best for the community
- Show empathy towards other community members
- Accept constructive criticism gracefully

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Questions?

Feel free to open an issue with your question or contact the maintainers directly.

## Recognition

Contributors will be recognized in the project README and CHANGELOG.

Thank you for contributing to make this project better!
