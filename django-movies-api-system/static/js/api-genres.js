document.addEventListener('DOMContentLoaded', function() {
    const genresContainer = document.getElementById('genres-container');
    const loadingElement = document.getElementById('loading');
    const errorElement = document.getElementById('error-message');
    const noDataElement = document.getElementById('no-data');
    
    async function loadGenres(page = 1) {
        try {
            loadingElement.style.display = 'block';
            errorElement.style.display = 'none';
            if (noDataElement) noDataElement.style.display = 'none';
            
            const response = await fetch(`/api/genres/?page=${page}`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            loadingElement.style.display = 'none';
            
            if (data.results && data.results.length > 0) {
                renderGenres(data.results);
                renderPagination(data);
            } else {
                showNoData();
            }
        } catch (error) {
            console.error('Error loading genres:', error);
            loadingElement.style.display = 'none';
            errorElement.style.display = 'block';
            errorElement.textContent = 'Failed to load genres. Please try again later.';
        }
    }
    
    function renderGenres(genres) {
        genresContainer.innerHTML = '';
        
        genres.forEach(genre => {
            const card = createGenreCard(genre);
            genresContainer.appendChild(card);
        });
    }
    
    function createGenreCard(genre) {
        const col = document.createElement('div');
        col.className = 'col-md-4';
        
        col.innerHTML = `
            <div class="card h-100 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">
                        <i class="fas fa-tag"></i> ${genre.name}
                    </h5>
                    <div class="d-flex gap-2 mt-3">
                        <a href="/genres/edit/${genre.id}/" class="btn btn-sm btn-info flex-fill">
                            <i class="fas fa-edit"></i> Edit
                        </a>
                        <form method="POST" action="/genres/delete/${genre.id}/" style="display: inline; flex: 1;">
                            <input type="hidden" name="csrfmiddlewaretoken" value="${getCSRFToken()}">
                            <button type="submit" class="btn btn-sm btn-danger w-100" onclick="return confirm('Are you sure you want to delete this genre?');">
                                <i class="fas fa-trash"></i> Delete
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
        nav.setAttribute('aria-label', 'Genres pagination');
        
        const ul = document.createElement('ul');
        ul.className = 'pagination justify-content-center mt-4';
        
        if (data.previous) {
            const prevPage = new URL(data.previous).searchParams.get('page') || 1;
            ul.innerHTML += `
                <li class="page-item">
                    <a class="page-link" href="#" onclick="loadGenres(${prevPage}); return false;">Previous</a>
                </li>
            `;
        }
        
        if (data.next) {
            const nextPage = new URL(data.next).searchParams.get('page');
            ul.innerHTML += `
                <li class="page-item">
                    <a class="page-link" href="#" onclick="loadGenres(${nextPage}); return false;">Next</a>
                </li>
            `;
        }
        
        nav.appendChild(ul);
        paginationContainer.appendChild(nav);
    }
    
    function showNoData() {
        const cardsContainer = document.getElementById('cards-container');
        if (cardsContainer) cardsContainer.style.display = 'none';
        if (noDataElement) noDataElement.style.display = 'block';
    }
    
    function getCSRFToken() {
        // Get CSRF token from cookie
        const name = 'csrftoken';
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue || '';
    }
    
    window.loadGenres = loadGenres;
    
    loadGenres();
});
