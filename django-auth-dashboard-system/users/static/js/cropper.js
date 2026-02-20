/**
 * Image Cropper Module
 * Handles profile picture cropping with Croppie.js
 */

document.addEventListener('DOMContentLoaded', function() {
    let croppieInstance = null;
    let isProcessing = false;
    
    const elements = {
        imageInput: document.getElementById('imageInput'),
        selectImageBtn: document.getElementById('selectImageBtn'),
        cropperModal: document.getElementById('cropperModal') ? new bootstrap.Modal(document.getElementById('cropperModal'), {
            backdrop: 'static',
            keyboard: false
        }) : null,
        zoomSlider: document.getElementById('zoomSlider'),
        cropButton: document.getElementById('cropButton'),
        currentAvatar: document.getElementById('currentAvatar'),
        modalElement: document.getElementById('cropperModal')
    };
    
    // Exit if cropper elements don't exist
    if (!elements.modalElement) return;
    
    const initializeCropper = () => {
        const cropperElement = document.getElementById('imageCropper');
        
        return new Croppie(cropperElement, {
            viewport: { 
                width: 300, 
                height: 300, 
                type: 'circle' 
            },
            boundary: { 
                width: 500, 
                height: 500 
            },
            showZoomer: false,
            enableOrientation: false,
            enableResize: false,
            mouseWheelZoom: false,
            enableExif: false
        });
    };
    
    const destroyCropper = () => {
        if (croppieInstance) {
            try {
                croppieInstance.destroy();
            } catch (e) {
                console.error('Error destroying cropper:', e);
            }
            croppieInstance = null;
        }
    };
    
    const updateAvatar = (base64Image) => {
        if (elements.currentAvatar.tagName === 'IMG') {
            elements.currentAvatar.src = base64Image;
        } else {
            const img = document.createElement('img');
            img.src = base64Image;
            img.className = 'avatar-preview';
            img.id = 'currentAvatar';
            elements.currentAvatar.parentNode.replaceChild(img, elements.currentAvatar);
            elements.currentAvatar = img;
        }
    };
    
    // Modal event listeners
    elements.modalElement.addEventListener('show.bs.modal', function() {
        document.body.classList.add('cropper-active');
    });
    
    elements.modalElement.addEventListener('hidden.bs.modal', function() {
        document.body.classList.remove('cropper-active');
        destroyCropper();
        elements.imageInput.value = '';
        isProcessing = false;
    });
    
    // Select image button
    elements.selectImageBtn.addEventListener('click', () => {
        if (!isProcessing) elements.imageInput.click();
    });
    
    // Image file selection handler
    elements.imageInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (!file || isProcessing) return;
        
        if (!file.type.startsWith('image/')) {
            alert('Please select a valid image file.');
            this.value = '';
            return;
        }
        
        isProcessing = true;
        const reader = new FileReader();
        
        reader.onload = function(event) {
            destroyCropper();
            elements.cropperModal.show();
            
            setTimeout(() => {
                try {
                    croppieInstance = initializeCropper();
                    croppieInstance.bind({
                        url: event.target.result,
                        zoom: 0
                    }).then(() => {
                        elements.zoomSlider.value = 0;
                        isProcessing = false;
                    }).catch(err => {
                        console.error('Bind error:', err);
                        isProcessing = false;
                    });
                } catch (error) {
                    console.error('Cropper init error:', error);
                    isProcessing = false;
                }
            }, 200);
        };
        
        reader.onerror = () => {
            alert('Failed to read image file.');
            isProcessing = false;
        };
        
        reader.readAsDataURL(file);
    });
    
    // Zoom slider handler
    elements.zoomSlider.addEventListener('input', function() {
        if (!croppieInstance || isProcessing) return;
        
        try {
            croppieInstance.setZoom(parseFloat(this.value));
        } catch (e) {
            console.error('Zoom error:', e);
        }
    });
    
    // Crop button handler
    elements.cropButton.addEventListener('click', function() {
        if (!croppieInstance || isProcessing) return;
        
        isProcessing = true;
        elements.cropButton.disabled = true;
        
        croppieInstance.result({
            type: 'base64',
            size: 'viewport',
            format: 'png',
            quality: 1,
            circle: false
        }).then(function(base64) {
            document.getElementById('croppedImage').value = base64;
            updateAvatar(base64);
            elements.cropperModal.hide();
        }).catch(function(error) {
            console.error('Crop failed:', error);
            alert('Failed to crop image. Please try again.');
        }).finally(function() {
            elements.cropButton.disabled = false;
            isProcessing = false;
        });
    });
});
