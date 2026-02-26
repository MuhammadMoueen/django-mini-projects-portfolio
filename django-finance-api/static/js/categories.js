// Categories Management - Finance Tracker

// Authentication check
const token = localStorage.getItem('token');
const user = JSON.parse(localStorage.getItem('user') || '{}');

if (!token) {
    window.location.href = '/login/';
}

// API request headers
const apiHeaders = {
    'Content-Type': 'application/json',
    'Authorization': `Token ${token}`
};

// Display username
document.getElementById('navUsername').textContent = user.username || 'User';

// Load profile picture
async function loadProfilePic() {
    try {
        const response = await fetch('/api/auth/profile/', {
            headers: apiHeaders
        });
        const data = await response.json();
        const profilePicUrl = data.profile_picture || '/static/images/default-avatar.svg';
        document.getElementById('navProfilePic').src = profilePicUrl;
    } catch (error) {
        document.getElementById('navProfilePic').src = '/static/images/default-avatar.svg';
    }
}

// Dropdown toggle
document.getElementById('profileBtn').addEventListener('click', function(e) {
    e.stopPropagation();
    document.getElementById('dropdownMenu').classList.toggle('show');
});

// Close dropdown
window.addEventListener('click', function(e) {
    if (!e.target.matches('.profile-btn') && !e.target.closest('.profile-dropdown')) {
        document.getElementById('dropdownMenu').classList.remove('show');
    }
});

// Logout
document.getElementById('logoutBtn').addEventListener('click', async function(e) {
    e.preventDefault();
    await fetch('/api/auth/logout/', {
        method: 'POST',
        headers: apiHeaders
    });
    localStorage.clear();
    window.location.href = '/login/';
});

loadProfilePic();

// Load all categories
async function loadCategories() {
    try {
        const response = await fetch('/api/categories/', {
            headers: apiHeaders
        });
        const categories = await response.json();
        
        const incomeCategories = categories.filter(c => c.category_type === 'income');
        const expenseCategories = categories.filter(c => c.category_type === 'expense');
        
        displayCategories('incomeCategoriesList', incomeCategories, 'income');
        displayCategories('expenseCategoriesList', expenseCategories, 'expense');
    } catch (error) {
        console.error('Error loading categories:', error);
        showAlert('Error loading categories', 'error');
    }
}

// Display categories in list
function displayCategories(containerId, categories, type) {
    const container = document.getElementById(containerId);
    
    if (categories.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 40px; color: #999;">
                <p style="font-size: 3em; margin-bottom: 10px;">📭</p>
                <p>No ${type} categories yet</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = categories.map(category => `
        <div class="category-item">
            <div class="category-info">
                <span class="category-icon">${type === 'income' ? '📈' : '📉'}</span>
                <span class="category-name">${category.name}</span>
            </div>
            <div class="category-actions">
                <button class="btn-icon-small" onclick="editCategory(${category.id}, '${category.name}', '${type}')" title="Edit">
                    ✏️
                </button>
                <button class="btn-icon-small btn-delete" onclick="deleteCategory(${category.id}, '${category.name}', '${type}')" title="Delete">
                    🗑️
                </button>
            </div>
        </div>
    `).join('');
}

// Add Income Category
document.getElementById('addIncomeCategoryForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    const name = formData.get('name').trim();
    
    if (!name) {
        showAlert('Please enter a category name', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/categories/', {
            method: 'POST',
            headers: apiHeaders,
            body: JSON.stringify({
                name: name,
                category_type: 'income'
            })
        });
        
        if (response.ok) {
            showAlert('Income category added successfully!', 'success');
            this.reset();
            loadCategories();
        } else {
            const error = await response.json();
            showAlert(error.name ? error.name[0] : 'Error adding category', 'error');
        }
    } catch (error) {
        console.error('Error adding income category:', error);
        showAlert('Error adding category', 'error');
    }
});

// Add Expense Category
document.getElementById('addExpenseCategoryForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    const name = formData.get('name').trim();
    
    if (!name) {
        showAlert('Please enter a category name', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/categories/', {
            method: 'POST',
            headers: apiHeaders,
            body: JSON.stringify({
                name: name,
                category_type: 'expense'
            })
        });
        
        if (response.ok) {
            showAlert('Expense category added successfully!', 'success');
            this.reset();
            loadCategories();
        } else {
            const error = await response.json();
            showAlert(error.name ? error.name[0] : 'Error adding category', 'error');
        }
    } catch (error) {
        console.error('Error adding expense category:', error);
        showAlert('Error adding category', 'error');
    }
});

// Edit Category
function editCategory(id, name, type) {
    document.getElementById('editCategoryId').value = id;
    document.getElementById('editCategoryName').value = name;
    document.getElementById('editCategoryType').value = type;
    document.getElementById('editCategoryModal').style.display = 'flex';
}

// Close Edit Modal
function closeEditModal() {
    document.getElementById('editCategoryModal').style.display = 'none';
}

// Close modal on outside click
window.addEventListener('click', function(e) {
    const modal = document.getElementById('editCategoryModal');
    if (e.target === modal) {
        closeEditModal();
    }
});

// Update Category
document.getElementById('editCategoryForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const id = document.getElementById('editCategoryId').value;
    const name = document.getElementById('editCategoryName').value.trim();
    const type = document.getElementById('editCategoryType').value;
    
    if (!name) {
        showAlert('Please enter a category name', 'error');
        return;
    }
    
    try {
        const response = await fetch(`/api/categories/${id}/`, {
            method: 'PUT',
            headers: apiHeaders,
            body: JSON.stringify({
                name: name,
                category_type: type
            })
        });
        
        if (response.ok) {
            showAlert('Category updated successfully!', 'success');
            closeEditModal();
            loadCategories();
        } else {
            const error = await response.json();
            showAlert(error.name ? error.name[0] : 'Error updating category', 'error');
        }
    } catch (error) {
        console.error('Error updating category:', error);
        showAlert('Error updating category', 'error');
    }
});

// Delete Category
async function deleteCategory(id, name, type) {
    if (!confirm(`Are you sure you want to delete the category "${name}"?\n\nNote: Transactions with this category will not be deleted, but will have no category assigned.`)) {
        return;
    }
    
    try {
        const response = await fetch(`/api/categories/${id}/`, {
            method: 'DELETE',
            headers: apiHeaders
        });
        
        if (response.ok) {
            showAlert('Category deleted successfully!', 'success');
            loadCategories();
        } else {
            showAlert('Error deleting category', 'error');
        }
    } catch (error) {
        console.error('Error deleting category:', error);
        showAlert('Error deleting category', 'error');
    }
}

// Show alert messages
function showAlert(message, type) {
    // Remove existing alerts
    const existingAlert = document.querySelector('.alert-message');
    if (existingAlert) {
        existingAlert.remove();
    }
    
    const alert = document.createElement('div');
    alert.className = `alert-message alert-${type}`;
    alert.innerHTML = `
        <span>${message}</span>
        <button class="alert-close" onclick="this.parentElement.remove()">&times;</button>
    `;
    
    document.body.appendChild(alert);
    
    setTimeout(() => {
        if (alert.parentElement) {
            alert.classList.add('fade-out');
            setTimeout(() => alert.remove(), 300);
        }
    }, 5000);
}

// Load categories on page load
loadCategories();
