document.addEventListener('DOMContentLoaded', function() {
    const directorsContainer = document.getElementById('directors-tbody');
    const loadingElement = document.getElementById('loading');
    const errorElement = document.getElementById('error-message');
    const noDataElement = document.getElementById('no-data');
    
    async function loadDirectors(page = 1) {
        try {
            loadingElement.style.display = 'block';
            errorElement.style.display = 'none';
            if (noDataElement) noDataElement.style.display = 'none';
            
            const response = await fetch(`/api/directors/?page=${page}`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            loadingElement.style.display = 'none';
            
            if (data.results && data.results.length > 0) {
                renderDirectors(data.results);
                renderPagination(data);
            } else {
                showNoData();
            }
        } catch (error) {
            console.error('Error loading directors:', error);
            loadingElement.style.display = 'none';
            errorElement.style.display = 'block';
            errorElement.textContent = 'Failed to load directors. Please try again later.';
        }
    }
    
    function renderDirectors(directors) {
        directorsContainer.innerHTML = '';
        
        directors.forEach(director => {
            const row = createDirectorRow(director);
            directorsContainer.appendChild(row);
        });
    }
    
    function createDirectorRow(director) {
        const tr = document.createElement('tr');
        
        const dobDisplay = director.dob 
            ? new Date(director.dob).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
            : '<span class="badge bg-secondary">Not Specified</span>';
        
        tr.innerHTML = `
            <td><strong>${director.first_name} ${director.last_name}</strong></td>
            <td>${dobDisplay}</td>
            <td>
                <a href="/directors/edit/${director.id}/" class="btn btn-sm btn-info">
                    <i class="fas fa-edit"></i> Edit
                </a>
                <form method="POST" action="/directors/delete/${director.id}/" style="display: inline;">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${getCSRFToken()}">
                    <button type="submit" class="btn btn-sm btn-danger" onclick="return confirm('Are you sure you want to delete this director?');">
                        <i class="fas fa-trash"></i> Delete
                    </button>
                </form>
            </td>
        `;
        
        return tr;
    }
    
    function renderPagination(data) {
        const paginationContainer = document.getElementById('pagination');
        if (!paginationContainer) return;
        
        paginationContainer.innerHTML = '';
        
        if (!data.previous && !data.next) {
            return;
        }
        
        const nav = document.createElement('nav');
        nav.setAttribute('aria-label', 'Directors pagination');
        
        const ul = document.createElement('ul');
        ul.className = 'pagination justify-content-center mt-4';
        
        if (data.previous) {
            const prevPage = new URL(data.previous).searchParams.get('page') || 1;
            ul.innerHTML += `
                <li class="page-item">
                    <a class="page-link" href="#" onclick="loadDirectors(${prevPage}); return false;">Previous</a>
                </li>
            `;
        }
        
        if (data.next) {
            const nextPage = new URL(data.next).searchParams.get('page');
            ul.innerHTML += `
                <li class="page-item">
                    <a class="page-link" href="#" onclick="loadDirectors(${nextPage}); return false;">Next</a>
                </li>
            `;
        }
        
        nav.appendChild(ul);
        paginationContainer.appendChild(nav);
    }
    
    function showNoData() {
        const tableContainer = document.getElementById('table-container');
        if (tableContainer) tableContainer.style.display = 'none';
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
    
    window.loadDirectors = loadDirectors;
    
    loadDirectors();
});
