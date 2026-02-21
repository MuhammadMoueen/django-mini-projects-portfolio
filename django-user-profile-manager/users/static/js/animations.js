/**
 * Circular Progress Ring Controller
 * Updates the circular SVG progress ring based on completion percentage
 */

document.addEventListener('DOMContentLoaded', function() {
    const progressCircle = document.querySelector('.progress-ring-circle');
    
    if (progressCircle) {
        const percentage = parseInt(progressCircle.getAttribute('data-percentage')) || 0;
        const radius = 110;
        const circumference = 2 * Math.PI * radius;
        
        // Calculate stroke offset for the given percentage
        const offset = circumference - (percentage / 100) * circumference;
        
        // Apply smooth animation after page load
        setTimeout(() => {
            progressCircle.style.strokeDashoffset = offset;
            
            // Add glow effect if 100% complete
            if (percentage === 100) {
                progressCircle.classList.add('complete');
            }
        }, 300);
    }
});

/**
 * Animated Background Bubble Controller
 * Manages floating bubble animations
 */

class BubbleAnimator {
    constructor() {
        this.bubbles = document.querySelectorAll('.bubble');
        this.init();
    }
    
    init() {
        // Bubbles are animated via CSS, this is for future enhancements
        this.bubbles.forEach((bubble, index) => {
            bubble.style.animationDelay = `${index * 3}s`;
        });
    }
}

// Initialize bubble animations if background exists
if (document.querySelector('.animated-background')) {
    new BubbleAnimator();
}
