/**
 * Main JavaScript for Django Auth Dashboard
 */

// Auto-dismiss alert messages
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.message-alert[data-auto-dismiss="true"]');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 1000);
    });
});
