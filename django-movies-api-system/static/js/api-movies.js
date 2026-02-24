document.addEventListener('DOMContentLoaded', function() {
    const moviesContainer = document.getElementById('movies-container');
    const loadingElement = document.getElementById('loading');
    const errorElement = document.getElementById('error-message');
    const searchInput = document.getElementById('search-input');
    const clearSearchBtn = document.getElementById('clear-search');
    const sortSelect = document.getElementById('sort-select');
    
    let currentPage = 1;
    let searchQuery = '';
    let sortOrder = '-release_date';
    let searchTimeout = null;
    
    async function loadMovies(page = 1, search = '', ordering = '-release_date') {
        try {
            loadingElement.style.display = 'block';
            errorElement.style.display = 'none';
            
            let url = `/api/movies/?page=${page}&ordering=${ordering}`;
            if (search) {
                url += `&search=${encodeURIComponent(search)}`;
            }
            
            const response = await fetch(url);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            loadingElement.style.display = 'none';
            
            if (data.results && data.results.length > 0) {
                renderMovies(data.results);
                renderPagination(data);
            } else {
                showNoMovies();
            }
        } catch (error) {
            console.error('Error loading movies:', error);
            loadingElement.style.display = 'none';
            errorElement.style.display = 'block';
            errorElement.textContent = 'Failed to load movies. Please try again later.';
        }
    }
    
    function renderMovies(movies) {
        moviesContainer.innerHTML = '';
        
        movies.forEach(movie => {
            const movieCard = createMovieCard(movie);
            moviesContainer.appendChild(movieCard);
        });
    }
    
    function createMovieCard(movie) {
        const col = document.createElement('div');
        col.className = 'col-sm-6 col-md-4 col-lg-3';
        
        const posterHtml = movie.poster_image
            ? `<img src="${movie.poster_image}" alt="${movie.title}" class="movie-poster">`
            : `<div class="poster-placeholder">
                   <i class="fas fa-film fa-4x text-white opacity-50"></i>
               </div>`;
        
        const description = movie.description 
            ? truncateWords(movie.description, 15) 
            : 'No description available';
        
        const genreBadge = movie.genre_name 
            ? `<span class="badge bg-primary info-badge">${movie.genre_name}</span>` 
            : '';
        const languageBadge = movie.language_name 
            ? `<span class="badge bg-info info-badge">${movie.language_name}</span>` 
            : '';
        
        const releaseYear = movie.release_date ? new Date(movie.release_date).getFullYear() : 'N/A';
        const ratingBadge = movie.rating 
            ? `<span class="rating-badge"><i class="fas fa-star"></i> ${movie.rating}</span>` 
            : '';
        
        col.innerHTML = `
            <div class="card movie-card">
                ${posterHtml}
                
                <div class="card-body">
                    <h5 class="movie-title">${movie.title}</h5>
                    <p class="movie-description">${description}</p>
                    
                    <div class="movie-info">
                        ${genreBadge}
                        ${languageBadge}
                    </div>
                    
                    <div class="movie-meta">
                        <small>
                            <i class="fas fa-calendar-alt"></i> ${releaseYear}<br>
                            <i class="fas fa-clock"></i> ${movie.duration || 'N/A'} min
                        </small>
                        ${ratingBadge}
                    </div>
                    
                    <div class="movie-actions">
                        <a href="/movies/edit/${movie.id}/" class="btn btn-edit">
                            <i class="fas fa-edit"></i> Edit
                        </a>
                        <form method="POST" action="/movies/delete/${movie.id}/" class="delete-form">
                            <input type="hidden" name="csrfmiddlewaretoken" value="${getCSRFToken()}">
                            <button type="submit" class="btn-delete w-100">
                                <i class="fas fa-trash-alt"></i> Delete
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        `;
        
        return col;
    }
    
    function renderPagination(data) {
        const paginationContainer = document.getElementById('pagination');
        if (!paginationContainer) return;
        
        paginationContainer.innerHTML = '';
        
        if (!data.previous && !data.next) {
            return;
        }
        
        const nav = document.createElement('nav');
        nav.setAttribute('aria-label', 'Movies pagination');
        
        const ul = document.createElement('ul');
        ul.className = 'pagination justify-content-center mt-4';
        
        if (data.previous) {
            const prevPage = new URL(data.previous).searchParams.get('page') || 1;
            ul.innerHTML += `
                <li class="page-item">
                    <a class="page-link" href="#" data-page="${prevPage}">Previous</a>
                </li>
            `;
        }
        
        if (data.next) {
            const nextPage = new URL(data.next).searchParams.get('page');
            ul.innerHTML += `
                <li class="page-item">
                    <a class="page-link" href="#" data-page="${nextPage}">Next</a>
                </li>
            `;
        }
        
        nav.appendChild(ul);
        paginationContainer.appendChild(nav);
        
        ul.querySelectorAll('a[data-page]').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                currentPage = parseInt(this.getAttribute('data-page'));
                loadMovies(currentPage, searchQuery, sortOrder);
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        });
    }
    
    function showNoMovies() {
        moviesContainer.innerHTML = `
            <div class="col-12">
                <div class="no-movies">
                    <i class="fas fa-film"></i>
                    <h3>${searchQuery ? 'No Movies Found' : 'No Movies Yet'}</h3>
                    <p class="text-muted">${searchQuery ? 'Try adjusting your search criteria' : 'Start building your collection by adding your first movie'}</p>
                    ${!searchQuery ? `<a href="/movies/create/" class="btn btn-primary btn-lg mt-3">
                        <i class="fas fa-plus"></i> Add Your First Movie
                    </a>` : ''}
                </div>
            </div>
        `;
    }
    
    function truncateWords(text, wordLimit) {
        const words = text.split(' ');
        if (words.length > wordLimit) {
            return words.slice(0, wordLimit).join(' ') + '...';
        }
        return text;
    }
    
    function getCSRFToken() {
        const token = document.querySelector('[name=csrfmiddlewaretoken]');
        return token ? token.value : '';
    }
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                searchQuery = this.value.trim();
                currentPage = 1;
                loadMovies(currentPage, searchQuery, sortOrder);
            }, 500);
        });
    }
    
    if (clearSearchBtn) {
        clearSearchBtn.addEventListener('click', function() {
            searchInput.value = '';
            searchQuery = '';
            currentPage = 1;
            loadMovies(currentPage, searchQuery, sortOrder);
        });
    }
    
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            sortOrder = this.value;
            currentPage = 1;
            loadMovies(currentPage, searchQuery, sortOrder);
        });
    }
    
    loadMovies(currentPage, searchQuery, sortOrder);
});
