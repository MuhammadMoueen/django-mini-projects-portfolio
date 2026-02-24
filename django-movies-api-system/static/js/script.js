document.addEventListener('DOMContentLoaded', function() {
    const deleteForms = document.querySelectorAll('.delete-form');
    
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const movieTitle = this.closest('.card-body').querySelector('.movie-title')?.textContent || 'this item';
            if (!confirm(`Are you sure you want to delete ${movieTitle}?`)) {
                e.preventDefault();
            }
        });
    });

    const deleteLinks = document.querySelectorAll('.btn-danger[href*="delete"]');
    deleteLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
});
