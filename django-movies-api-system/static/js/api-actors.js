document.addEventListener('DOMContentLoaded', function() {
    const actorsContainer = document.getElementById('actors-tbody');
    const loadingElement = document.getElementById('loading');
    const errorElement = document.getElementById('error-message');
    const noDataElement = document.getElementById('no-data');
    
    async function loadActors(page = 1) {
        try {
            loadingElement.style.display = 'block';
            errorElement.style.display = 'none';
            if (noDataElement) noDataElement.style.display = 'none';
            
            const response = await fetch(`/api/actors/?page=${page}`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            loadingElement.style.display = 'none';
            
            if (data.results && data.results.length > 0) {
                renderActors(data.results);
                renderPagination(data);
            } else {
                showNoData();
            }
        } catch (error) {
            console.error('Error loading actors:', error);
            loadingElement.style.display = 'none';
            errorElement.style.display = 'block';
            errorElement.textContent = 'Failed to load actors. Please try again later.';
        }
    }
    
    function renderActors(actors) {
        actorsContainer.innerHTML = '';
        
        actors.forEach(actor => {
            const row = createActorRow(actor);
            actorsContainer.appendChild(row);
        });
    }
    
    function createActorRow(actor) {
        const tr = document.createElement('tr');
        
        const dobDisplay = actor.dob 
            ? new Date(actor.dob).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
            : '<span class="badge bg-secondary">Not Specified</span>';
        
        tr.innerHTML = `
            <td><strong>${actor.first_name} ${actor.last_name}</strong></td>
            <td>${dobDisplay}</td>
            <td>
                <a href="/actors/edit/${actor.id}/" class="btn btn-sm btn-info">
                    <i class="fas fa-edit"></i> Edit
                </a>
                <form method="POST" action="/actors/delete/${actor.id}/" style="display: inline;">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${getCSRFToken()}">
                    <button type="submit" class="btn btn-sm btn-danger" onclick="return confirm('Are you sure you want to delete this actor?');">
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
        nav.setAttribute('aria-label', 'Actors pagination');
        
        const ul = document.createElement('ul');
        ul.className = 'pagination justify-content-center mt-4';
        
        if (data.previous) {
            const prevPage = new URL(data.previous).searchParams.get('page') || 1;
            ul.innerHTML += `
                <li class="page-item">
                    <a class="page-link" href="#" onclick="loadActors(${prevPage}); return false;">Previous</a>
                </li>
            `;
        }
        
        if (data.next) {
            const nextPage = new URL(data.next).searchParams.get('page');
            ul.innerHTML += `
                <li class="page-item">
                    <a class="page-link" href="#" onclick="loadActors(${nextPage}); return false;">Next</a>
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
    
    window.loadActors = loadActors;
    
    loadActors();
});
