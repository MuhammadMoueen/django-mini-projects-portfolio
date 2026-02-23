/**
 * Main JavaScript file for BlogSys
 * Contains general site-wide functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    
    /**
     * Auto-submit sort dropdown on change
     * Submits the parent form when sort option is changed
     */
    const sortSelect = document.querySelector('select[name="sort"]');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            this.form.submit();
        });
    }

    /**
     * Auto-dismiss alert messages after 5 seconds
     */
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

});
