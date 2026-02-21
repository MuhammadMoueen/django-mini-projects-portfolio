document.addEventListener('DOMContentLoaded', function() {
    const fileInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
    let cropper = null;
    let currentInput = null;

    fileInputs.forEach(input => {
        const previewContainer = input.closest('.mb-3')?.querySelector('img');
        
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (!file || !file.type.startsWith('image/')) return;

            currentInput = input;
            const reader = new FileReader();
            
            reader.onload = function(event) {
                showCropModal(event.target.result, file);
            };
            
            reader.readAsDataURL(file);
        });
    });

    function showCropModal(imageSrc, originalFile) {
        const modalHTML = `
            <div class="modal fade" id="cropModal" tabindex="-1">
                <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Crop Profile Picture</h5>
                            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            <div class="crop-container">
                                <img id="cropImage" src="${imageSrc}" style="max-width: 100%;">
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                            <button type="button" class="btn btn-primary" id="cropButton">Crop & Save</button>
                        </div>
                    </div>
                </div>
            </div>
        `;

        document.body.insertAdjacentHTML('beforeend', modalHTML);
        const modal = new bootstrap.Modal(document.getElementById('cropModal'));
        const image = document.getElementById('cropImage');
        
        cropper = new Cropper(image, {
            aspectRatio: 1,
            viewMode: 2,
            dragMode: 'move',
            autoCropArea: 1,
            restore: false,
            guides: true,
            center: true,
            highlight: false,
            cropBoxMovable: true,
            cropBoxResizable: true,
            toggleDragModeOnDblclick: false,
        });

        document.getElementById('cropButton').addEventListener('click', function() {
            const canvas = cropper.getCroppedCanvas({
                width: 400,
                height: 400,
                imageSmoothingEnabled: true,
                imageSmoothingQuality: 'high',
            });

            canvas.toBlob(function(blob) {
                const file = new File([blob], originalFile.name, {
                    type: 'image/jpeg',
                    lastModified: Date.now()
                });

                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(file);
                currentInput.files = dataTransfer.files;

                const preview = document.getElementById('image-preview') || 
                               currentInput.closest('.mb-3')?.querySelector('img');
                
                if (preview) {
                    preview.src = canvas.toDataURL('image/jpeg');
                    preview.style.display = 'block';
                } else {
                    const placeholder = currentInput.closest('.mb-3')?.querySelector('.profile-image-preview-placeholder');
                    if (placeholder) {
                        const newImg = document.createElement('img');
                        newImg.id = 'image-preview';
                        newImg.className = 'profile-image-preview';
                        newImg.src = canvas.toDataURL('image/jpeg');
                        placeholder.parentNode.replaceChild(newImg, placeholder);
                    }
                }

                modal.hide();
            }, 'image/jpeg', 0.9);
        });

        modal.show();
        
        document.getElementById('cropModal').addEventListener('hidden.bs.modal', function() {
            if (cropper) {
                cropper.destroy();
                cropper = null;
            }
            this.remove();
        });
    }
});
