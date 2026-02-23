document.addEventListener('DOMContentLoaded', function() {
    const passwordToggles = document.querySelectorAll('.password-toggle-btn');
    
    passwordToggles.forEach(toggleBtn => {
        const targetId = toggleBtn.getAttribute('data-target');
        const passwordInput = document.getElementById(targetId);
        const eyeOpen = toggleBtn.querySelectorAll('.eye-open');
        const eyeClosed = toggleBtn.querySelectorAll('.eye-closed');

        if (toggleBtn && passwordInput) {
            toggleBtn.addEventListener('click', function(e) {
                e.preventDefault();
                
                const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
                passwordInput.setAttribute('type', type);
                
                eyeOpen.forEach(el => {
                    el.style.display = type === 'password' ? 'block' : 'none';
                });
                eyeClosed.forEach(el => {
                    el.style.display = type === 'password' ? 'none' : 'block';
                });
            });
        }
    });

    const fileInput = document.querySelector('input[type="file"][accept*="image"]');
    const profilePreview = document.getElementById('profilePreview');
    
    if (fileInput && profilePreview) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            
            if (file && file.type.startsWith('image/')) {
                const maxSize = 2 * 1024 * 1024;
                if (file.size > maxSize) {
                    alert('File size must be less than 2MB');
                    fileInput.value = '';
                    return;
                }
                
                const reader = new FileReader();
                
                reader.onload = function(event) {
                    if (profilePreview.tagName === 'DIV') {
                        const img = document.createElement('img');
                        img.src = event.target.result;
                        img.alt = 'Profile Preview';
                        img.className = 'profile-pic-preview';
                        img.id = 'profilePreview';
                        profilePreview.parentNode.replaceChild(img, profilePreview);
                    } else {
                        profilePreview.src = event.target.result;
                    }
                };
                
                reader.readAsDataURL(file);
            } else {
                alert('Please select a valid image file (JPG, PNG, GIF)');
                fileInput.value = '';
            }
        });
    }

    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
                
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = submitBtn.getAttribute('data-original-text') || 'Submit';
                }, 3000);
            }
        });
    });

    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    const dropdowns = document.querySelectorAll('.dropdown');
    
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('show.bs.dropdown', function() {
            const menu = this.querySelector('.dropdown-menu');
            if (menu) {
                menu.style.display = 'block';
                menu.classList.add('show');
            }
        });
        
        dropdown.addEventListener('hide.bs.dropdown', function() {
            const menu = this.querySelector('.dropdown-menu');
            if (menu) {
                setTimeout(() => {
                    menu.style.display = '';
                }, 300);
            }
        });
    });
});

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}
