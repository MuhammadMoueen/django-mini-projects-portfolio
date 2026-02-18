document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.getElementById('content');
    if (textarea) {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });
    }
    
    const titleInput = document.getElementById('title');
    if (titleInput) {
        titleInput.addEventListener('input', function() {
            const remaining = 200 - this.value.length;
            const helpText = this.nextElementSibling;
            if (remaining < 20) {
                helpText.textContent = `${remaining} characters remaining`;
                helpText.classList.add('text-warning');
            } else {
                helpText.textContent = 'Give your note a clear and descriptive title (max 200 characters)';
                helpText.classList.remove('text-warning');
            }
        });
    }
});
