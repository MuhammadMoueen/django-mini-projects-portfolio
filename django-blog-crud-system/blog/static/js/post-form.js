/**
 * Post Form Character Counter
 * Tracks and displays character count for title and content fields
 */

document.addEventListener('DOMContentLoaded', function() {
    const titleInput = document.querySelector('input[name="title"]');
    const contentInput = document.querySelector('textarea[name="content"]');
    const titleCount = document.getElementById('titleCount');
    const contentCount = document.getElementById('contentCount');
    
    // Skip if elements don't exist on the page
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
    
    // Attach event listeners
    titleInput.addEventListener('input', updateTitleCount);
    contentInput.addEventListener('input', updateContentCount);
    
    // Initialize counts
    updateTitleCount();
    updateContentCount();
});
