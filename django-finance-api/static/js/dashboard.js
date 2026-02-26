// Dashboard functionality for Finance Tracker

// Authentication check - redirect if not logged in
const token = localStorage.getItem('token');
const user = JSON.parse(localStorage.getItem('user') || '{}');

if (!token) {
    window.location.href = '/login/';
}

// API request headers with authentication token
const apiHeaders = {
    'Content-Type': 'application/json',
    'Authorization': `Token ${token}`
};

// Load profile picture and display name
async function loadProfilePic() {
    try {
        const response = await fetch('/api/auth/profile/', {
            headers: apiHeaders
        });
        const data = await response.json();
        const profilePicUrl = data.profile_picture || '/static/images/default-avatar.svg';
        document.getElementById('navProfilePic').src = profilePicUrl;
        
        // Set display name (full name if available, otherwise username)
        const displayName = data.first_name && data.last_name 
            ? `${data.first_name} ${data.last_name}` 
            : data.username || user.username || 'User';
        document.getElementById('navDisplayName').textContent = displayName;
    } catch (error) {
        document.getElementById('navProfilePic').src = '/static/images/default-avatar.svg';
        document.getElementById('navDisplayName').textContent = user.username || 'User';
    }
}

// Dropdown toggle
document.getElementById('profileBtn').addEventListener('click', function(e) {
    e.stopPropagation();
    document.getElementById('dropdownMenu').classList.toggle('show');
});

// Close dropdown when clicking outside
window.addEventListener('click', function(e) {
    if (!e.target.matches('.profile-btn') && !e.target.closest('.profile-dropdown')) {
        document.getElementById('dropdownMenu').classList.remove('show');
    }
});

// Logout handler
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

// Chart instances
let incomeExpenseChart = null;
let categoryChart = null;

// Load financial summary from API
async function loadSummary() {
    try {
        const response = await fetch('/api/summary/', {
            headers: apiHeaders
        });
        const data = await response.json();
        
        document.getElementById('totalIncome').textContent = formatCurrency(data.total_income);
        document.getElementById('totalExpense').textContent = formatCurrency(data.total_expense);
        document.getElementById('balance').textContent = formatCurrency(data.balance);
        
        // Update charts with new data
        updateCharts(data);
    } catch (error) {
        console.error('Error loading summary:', error);
    }
}

// Initialize and update charts
async function updateCharts(summaryData) {
    try {
        // Income vs Expense Chart
        if (incomeExpenseChart) {
            incomeExpenseChart.destroy();
        }
        
        const ctx1 = document.getElementById('incomeExpenseChart').getContext('2d');
        incomeExpenseChart = new Chart(ctx1, {
            type: 'bar',
            data: {
                labels: ['Income', 'Expense'],
                datasets: [{
                    label: 'Amount ($)',
                    data: [summaryData.total_income, summaryData.total_expense],
                    backgroundColor: [
                        'rgba(0, 255, 136, 0.6)',
                        'rgba(255, 0, 110, 0.6)'
                    ],
                    borderColor: [
                        'rgba(0, 255, 136, 1)',
                        'rgba(255, 0, 110, 1)'
                    ],
                    borderWidth: 2,
                    borderRadius: 10
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        backgroundColor: 'rgba(26, 26, 46, 0.9)',
                        titleColor: '#fff',
                        bodyColor: '#fff',
                        borderColor: 'rgba(108, 99, 255, 0.5)',
                        borderWidth: 1,
                        padding: 12,
                        displayColors: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(108, 99, 255, 0.1)'
                        },
                        ticks: {
                            color: '#e8e8e8',
                            callback: function(value) {
                                return '$' + value.toLocaleString();
                            }
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        },
                        ticks: {
                            color: '#e8e8e8',
                            font: {
                                size: 14,
                                weight: 'bold'
                            }
                        }
                    }
                }
            }
        });
        
        // Category Expense Chart
        await updateCategoryChart();
        
    } catch (error) {
        console.error('Error updating charts:', error);
    }
}

async function updateCategoryChart() {
    try {
        const response = await fetch('/api/category-report/', {
            headers: apiHeaders
        });
        const categoryData = await response.json();
        
        if (categoryChart) {
            categoryChart.destroy();
        }
        
        // Filter out categories with zero amounts and limit to top 6
        const filteredData = categoryData
            .filter(item => item.total_amount > 0)
            .sort((a, b) => b.total_amount - a.total_amount)
            .slice(0, 6);
        
        const labels = filteredData.map(item => item.category__name);
        const amounts = filteredData.map(item => item.total_amount);
        
        // Generate vibrant colors
        const colors = [
            'rgba(108, 99, 255, 0.8)',
            'rgba(0, 212, 255, 0.8)',
            'rgba(255, 0, 110, 0.8)',
            'rgba(0, 255, 136, 0.8)',
            'rgba(255, 136, 0, 0.8)',
            'rgba(255, 0, 255, 0.8)'
        ];
        
        const ctx2 = document.getElementById('categoryChart').getContext('2d');
        categoryChart = new Chart(ctx2, {
            type: 'doughnut',
            data: {
                labels: labels.length > 0 ? labels : ['No Data'],
                datasets: [{
                    data: amounts.length > 0 ? amounts : [1],
                    backgroundColor: colors,
                    borderColor: 'rgba(26, 26, 46, 1)',
                    borderWidth: 3,
                    hoverOffset: 15
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: '#e8e8e8',
                            padding: 15,
                            font: {
                                size: 12
                            },
                            generateLabels: function(chart) {
                                const data = chart.data;
                                if (data.labels.length && data.datasets.length) {
                                    return data.labels.map((label, i) => {
                                        const value = data.datasets[0].data[i];
                                        return {
                                            text: `${label}: $${value.toLocaleString()}`,
                                            fillStyle: data.datasets[0].backgroundColor[i],
                                            hidden: false,
                                            index: i
                                        };
                                    });
                                }
                                return [];
                            }
                        }
                    },
                    tooltip: {
                        backgroundColor: 'rgba(26, 26, 46, 0.9)',
                        titleColor: '#fff',
                        bodyColor: '#fff',
                        borderColor: 'rgba(108, 99, 255, 0.5)',
                        borderWidth: 1,
                        padding: 12,
                        callbacks: {
                            label: function(context) {
                                const label = context.label || '';
                                const value = context.parsed || 0;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = ((value / total) * 100).toFixed(1);
                                return `${label}: $${value.toLocaleString()} (${percentage}%)`;
                            }
                        }
                    }
                },
                cutout: '65%'
            }
        });
    } catch (error) {
        console.error('Error loading category chart:', error);
    }
}

async function loadCategories() {
    try {
        const response = await fetch('/api/categories/', {
            headers: apiHeaders
        });
        const categories = await response.json();
        
        const incomeCategories = categories.filter(c => c.category_type === 'income');
        const expenseCategories = categories.filter(c => c.category_type === 'expense');
        
        populateSelect('incomeCategorySelect', incomeCategories);
        populateSelect('expenseCategorySelect', expenseCategories);
        
        if (incomeCategories.length === 0) {
            await createDefaultCategories('income');
        }
        if (expenseCategories.length === 0) {
            await createDefaultCategories('expense');
        }
    } catch (error) {
        console.error('Error loading categories:', error);
    }
}

async function createDefaultCategories(type) {
    const defaults = type === 'income' 
        ? ['Salary', 'Freelance', 'Investment', 'Other Income']
        : ['Food', 'Transport', 'Bills', 'Shopping', 'Entertainment', 'Other Expense'];
    
    for (const name of defaults) {
        await fetch('/api/categories/', {
            method: 'POST',
            headers: apiHeaders,
            body: JSON.stringify({ name, category_type: type })
        });
    }
    await loadCategories();
}

function populateSelect(selectId, categories) {
    const select = document.getElementById(selectId);
    select.innerHTML = '<option value="">Select Category</option>';
    categories.forEach(cat => {
        const option = document.createElement('option');
        option.value = cat.id;
        option.textContent = cat.name;
        select.appendChild(option);
    });
}

document.getElementById('incomeForm').addEventListener('submit', async function(e) {
    e.preventDefault();
   
    const formData = new FormData(this);
    const data = Object.fromEntries(formData);
    
    try {
        const response = await fetch('/api/incomes/', {
            method: 'POST',
            headers: apiHeaders,
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            showAlert('Income added successfully!', 'success');
            this.reset();
            loadSummary();
            loadIncomes();
        } else {
            const error = await response.json();
            showAlert(JSON.stringify(error), 'error');
        }
    } catch (error) {
        showAlert('Error adding income', 'error');
    }
});

document.getElementById('expenseForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    const data = Object.fromEntries(formData);
    
    try {
        const response = await fetch('/api/expenses/', {
            method: 'POST',
            headers: apiHeaders,
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            showAlert('Expense added successfully!', 'success');
            this.reset();
            loadSummary();
            loadExpenses();
        } else {
            const error = await response.json();
            showAlert(JSON.stringify(error), 'error');
        }
    } catch (error) {
        showAlert('Error adding expense', 'error');
    }
});

async function loadIncomes() {
    try {
        const response = await fetch('/api/incomes/', {
            headers: apiHeaders
        });
        const incomes = await response.json();
        
        const tbody = document.getElementById('incomeTableBody');
        tbody.innerHTML = '';
        
        incomes.forEach(income => {
            const row = tbody.insertRow();
            row.innerHTML = `
                <td>${formatDate(income.date)}</td>
                <td>${formatCurrency(income.amount)}</td>
                <td>${income.category_name || 'N/A'}</td>
                <td>${income.notes || '-'}</td>
                <td>
                    <button class="btn btn-danger" onclick="deleteIncome(${income.id})">Delete</button>
                </td>
            `;
        });
    } catch (error) {
        console.error('Error loading incomes:', error);
    }
}

async function loadExpenses() {
    try {
        const response = await fetch('/api/expenses/', {
            headers: apiHeaders
        });
        const expenses = await response.json();
        
        const tbody = document.getElementById('expenseTableBody');
        tbody.innerHTML = '';
        
        expenses.forEach(expense => {
            const row = tbody.insertRow();
            row.innerHTML = `
                <td>${formatDate(expense.date)}</td>
                <td>${formatCurrency(expense.amount)}</td>
                <td>${expense.category_name || 'N/A'}</td>
                <td>${expense.notes || '-'}</td>
                <td>
                    <button class="btn btn-danger" onclick="deleteExpense(${expense.id})">Delete</button>
                </td>
            `;
        });
    } catch (error) {
        console.error('Error loading expenses:', error);
    }
}

async function deleteIncome(id) {
    if (!confirm('Are you sure you want to delete this income?')) return;
    
    try {
        const response = await fetch(`/api/incomes/${id}/`, {
            method: 'DELETE',
            headers: apiHeaders
        });
        
        if (response.ok) {
            showAlert('Income deleted successfully', 'success');
            loadSummary();
            loadIncomes();
        }
    } catch (error) {
        showAlert('Error deleting income', 'error');
    }
}

async function deleteExpense(id) {
    if (!confirm('Are you sure you want to delete this expense?')) return;
    
    try {
        const response = await fetch(`/api/expenses/${id}/`, {
            method: 'DELETE',
            headers: apiHeaders
        });
        
        if (response.ok) {
            showAlert('Expense deleted successfully', 'success');
            loadSummary();
            loadExpenses();
        }
    } catch (error) {
        showAlert('Error deleting expense', 'error');
    }
}

function showTab(tab) {
    document.getElementById('incomeList').style.display = tab === 'income' ? 'block' : 'none';
    document.getElementById('expenseList').style.display = tab === 'expense' ? 'block' : 'none';
    
    const incomeTab = document.getElementById('incomeTab');
    const expenseTab = document.getElementById('expenseTab');
    
    if (tab === 'income') {
        incomeTab.classList.add('active');
        expenseTab.classList.remove('active');
    } else {
        expenseTab.classList.add('active');
        incomeTab.classList.remove('active');
    }
}

loadSummary();
loadCategories();
loadIncomes();
loadExpenses();
showTab('income');
