
document.addEventListener('DOMContentLoaded', function() {
    const titleInput = document.querySelector('input[name="title"]');
    const contentInput = document.querySelector('textarea[name="content"]');
    const titleCount = document.getElementById('titleCount');
    const contentCount = document.getElementById('contentCount');
    
    if (!titleInput || !contentInput) return;
    
    function updateTitleCount() {
        if (titleCount) {
            titleCount.textContent = titleInput.value.length;
        }
    }
    
    function updateContentCount() {
        if (contentCount) {
            contentCount.textContent = contentInput.value.length;
        }
    }
    
    titleInput.addEventListener('input', updateTitleCount);
    contentInput.addEventListener('input', updateContentCount);
    
    updateTitleCount();
    updateContentCount();
});
