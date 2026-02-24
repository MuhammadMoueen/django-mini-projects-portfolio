# Django Movies API System

A modern Django web application for managing a movie database with a RESTful API backend and dynamic frontend powered by JavaScript. This project demonstrates a hybrid architecture combining traditional Django templates with REST API endpoints for data fetching and management.

## Features

### Backend (Django REST Framework)
- **RESTful API Endpoints** for all entities (Movies, Actors, Directors, Genres, Languages)
- **Pagination** with configurable page sizes (12 items per page)
- **Search & Ordering** capabilities on list endpoints
- **Data Validation** with custom serializers
- **Optimized Queries** using `select_related` and `prefetch_related`
- **Nested Serializers** for related data (e.g., movies include genre/language/director details)

### Frontend (JavaScript + Django Templates)
- **Dynamic Data Loading** via Fetch API
- **Loading States** with spinners
- **Error Handling** with user-friendly messages
- **Pagination Controls** for browsing large datasets
- **Responsive Design** with Bootstrap 5
- **Clean UI** with Font Awesome icons

### Data Models
- **Movie**: Title, description, duration, release date, rating, poster image, genre, language, director, actors (many-to-many)
- **Actor**: First name, last name, date of birth
- **Director**: First name, last name, date of birth
- **Genre**: Name (e.g., Action, Comedy, Drama)
- **Language**: Name (e.g., English, Spanish, French)

## Technology Stack

- **Backend Framework**: Django 5.2.7
- **API Framework**: Django REST Framework 3.16.1
- **Database**: SQLite (development)
- **Frontend**: Vanilla JavaScript (ES6+)
- **CSS Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.4.0
- **Image Processing**: Pillow 11.2.0

## Project Structure

```
django-movies-api-system/
├── main/                           # Main Django app
│   ├── models.py                   # Data models (Movie, Actor, Director, Genre, Language)
│   ├── views.py                    # Traditional Django views for forms
│   ├── api_views.py                # API ViewSets for REST endpoints
│   ├── serializers.py              # DRF serializers with validation
│   ├── api_urls.py                 # API URL routing
│   ├── urls.py                     # Traditional URL routing
│   ├── forms.py                    # Django forms for create/edit
│   ├── admin.py                    # Django admin configuration
│   ├── templates/                  # HTML templates
│   │   ├── base.html               # Base template with navigation
│   │   ├── movie_list.html         # Movies listing (API-powered)
│   │   ├── actor_list.html         # Actors listing (API-powered)
│   │   ├── director_list.html      # Directors listing (API-powered)
│   │   ├── language_list.html      # Languages listing (API-powered)
│   │   ├── genre_list.html         # Genres listing (API-powered)
│   │   ├── movie_edit.html         # Movie create/edit form
│   │   └── model_form.html         # Generic form template
│   └── migrations/                 # Database migrations
├── movies/                         # Django project settings
│   ├── settings.py                 # Project configuration
│   ├── urls.py                     # Root URL routing
│   ├── wsgi.py                     # WSGI configuration
│   └── asgi.py                     # ASGI configuration
├── static/                         # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css               # Global styles
│   └── js/
│       ├── script.js               # Common JavaScript (delete confirmations)
│       ├── api-movies.js           # Movies API client
│       ├── api-actors.js           # Actors API client
│       ├── api-directors.js        # Directors API client
│       ├── api-languages.js        # Languages API client
│       └── api-genres.js           # Genres API client
├── media/                          # User-uploaded files (movie posters)
├── db.sqlite3                      # SQLite database
├── manage.py                       # Django management script
└── requirements.txt                # Python dependencies

```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-movies-api-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files (production)**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Main application: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/
   - API root: http://localhost:8000/api/

## API Documentation

### Base URL
```
http://localhost:8000/api/
```

### Endpoints

#### Movies
- `GET /api/movies/` - List all movies (paginated)
  - Query params: `?page=1`, `?search=inception`, `?ordering=-release_date`
- `GET /api/movies/{id}/` - Retrieve a specific movie
- `POST /api/movies/` - Create a new movie
- `PUT /api/movies/{id}/` - Update a movie
- `PATCH /api/movies/{id}/` - Partial update a movie
- `DELETE /api/movies/{id}/` - Delete a movie

#### Actors
- `GET /api/actors/` - List all actors (paginated)
  - Query params: `?search=smith`, `?ordering=last_name`
- `GET /api/actors/{id}/` - Retrieve a specific actor
- `POST /api/actors/` - Create a new actor
- `PUT /api/actors/{id}/` - Update an actor
- `DELETE /api/actors/{id}/` - Delete an actor

#### Directors
- `GET /api/directors/` - List all directors (paginated)
  - Query params: `?search=nolan`, `?ordering=last_name`
- `GET /api/directors/{id}/` - Retrieve a specific director
- `POST /api/directors/` - Create a new director
- `PUT /api/directors/{id}/` - Update a director
- `DELETE /api/directors/{id}/` - Delete a director

#### Languages
- `GET /api/languages/` - List all languages (paginated)
  - Query params: `?search=english`, `?ordering=name`
- `GET /api/languages/{id}/` - Retrieve a specific language
- `POST /api/languages/` - Create a new language
- `PUT /api/languages/{id}/` - Update a language
- `DELETE /api/languages/{id}/` - Delete a language

#### Genres
- `GET /api/genres/` - List all genres (paginated)
  - Query params: `?search=action`, `?ordering=name`
- `GET /api/genres/{id}/` - Retrieve a specific genre
- `POST /api/genres/` - Create a new genre
- `PUT /api/genres/{id}/` - Update a genre
- `DELETE /api/genres/{id}/` - Delete a genre

### Response Format

#### List Response (Paginated)
```json
{
  "count": 25,
  "next": "http://localhost:8000/api/movies/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Inception",
      "description": "A thief who steals corporate secrets...",
      "duration": 148,
      "release_date": "2010-07-16",
      "genre_name": "Sci-Fi",
      "language_name": "English",
      "poster_image": "/media/posters/inception.jpg",
      "rating": 8.8
    }
  ]
}
```

#### Detail Response (Movie)
```json
{
  "id": 1,
  "title": "Inception",
  "description": "A thief who steals corporate secrets through dream-sharing technology...",
  "duration": 148,
  "release_date": "2010-07-16",
  "genre": 1,
  "genre_name": "Sci-Fi",
  "language": 1,
  "language_name": "English",
  "director": 1,
  "director_name": "Christopher Nolan",
  "poster_image": "/media/posters/inception.jpg",
  "actors": [1, 2, 3],
  "actors_list": [
    {
      "id": 1,
      "first_name": "Leonardo",
      "last_name": "DiCaprio",
      "dob": "1974-11-11"
    }
  ],
  "rating": 8.8
}
```

### API Features

#### Pagination
All list endpoints support pagination with 12 items per page:
```
GET /api/movies/?page=2
```

#### Search
Search across relevant fields:
```
GET /api/movies/?search=inception
GET /api/actors/?search=dicaprio
```

#### Ordering
Sort results by specified fields:
```
GET /api/movies/?ordering=-release_date  (descending)
GET /api/actors/?ordering=last_name      (ascending)
```

#### Filtering Multiple Parameters
Combine parameters:
```
GET /api/movies/?search=action&ordering=-rating&page=1
```

## Validation Rules

### Movie
- **Title**: Required, max 200 characters
- **Duration**: Positive number, max 1000 minutes
- **Release Date**: Cannot be in the future
- **Rating**: Between 0 and 10
- **Genre**: Required
- **Language**: Required

### Actor / Director
- **First Name**: Required, max 100 characters
- **Last Name**: Required, max 100 characters
- **Date of Birth**: Must be in the past (if provided)

### Genre / Language
- **Name**: Required, max 100 characters, must be unique

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Accessing Django Admin
Create a superuser and visit http://localhost:8000/admin/:
```bash
python manage.py createsuperuser
```

### Loading Sample Data
You can create sample data via the admin panel or Django shell:
```bash
python manage.py shell
```

## Architecture Highlights

### Hybrid Approach
This project demonstrates a modern hybrid architecture:
- **List Views**: API-powered with JavaScript for dynamic loading, pagination, and future search/filter enhancements
- **Forms**: Traditional Django forms for simplified file upload handling (movie posters)
- **Best of Both Worlds**: Combines Django's robust form handling with API flexibility

### Code Quality
- **No AI Comments**: Clean, production-ready code without generated boilerplate
- **No Django Boilerplate**: settings.py and other files stripped of unnecessary comments
- **Consistent Styling**: All CSS in external files, no inline styles
- **Event Delegation**: JavaScript event handlers in external files

### Performance Optimizations
- **Query Optimization**: `select_related()` and `prefetch_related()` to minimize database queries
- **Lazy Loading**: Data loaded on demand via API calls
- **Paginated Responses**: Reduced payload sizes for large datasets

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Django and Django REST Framework
- UI components from Bootstrap 5
- Icons from Font Awesome
- Modern JavaScript (Fetch API, ES6+)

## Future Enhancements

Potential improvements for future versions:
- [ ] Search and filter UI on list pages
- [ ] User authentication and permissions
- [ ] Movie reviews and ratings system
- [ ] Advanced filtering (by genre, year, rating range)
- [ ] Movie watchlist functionality
- [ ] API authentication (Token/JWT)
- [ ] API rate limiting
- [ ] Integration with external movie databases (TMDB, OMDB)
- [ ] Export data (CSV, JSON)
- [ ] Batch operations
- [ ] Docker containerization
- [ ] PostgreSQL for production
- [ ] Deployment guide (AWS, Heroku, DigitalOcean)

## Contact

For questions or suggestions, please open an issue in the repository.

---

**Built with ❤️ Django + REST Framework**
