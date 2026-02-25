const token = localStorage.getItem('token');
const user = JSON.parse(localStorage.getItem('user') || '{}');

if (!token) {
    window.location.href = '/login/';
}

const apiHeaders = {
    'Content-Type': 'application/json',
    'Authorization': `Token ${token}`
};

document.getElementById('userInfo').textContent = user.username || 'User';

document.getElementById('logoutBtn').addEventListener('click', async function(e) {
    e.preventDefault();
    await fetch('/api/auth/logout/', {
        method: 'POST',
        headers: apiHeaders
    });
    localStorage.clear();
    window.location.href = '/login/';
});

async function loadSummary() {
    try {
        const response = await fetch('/api/summary/', {
            headers: apiHeaders
        });
        const data = await response.json();
        
        document.getElementById('totalIncome').textContent = formatCurrency(data.total_income);
        document.getElementById('totalExpense').textContent = formatCurrency(data.total_expense);
        document.getElementById('balance').textContent = formatCurrency(data.balance);
    } catch (error) {
        console.error('Error loading summary:', error);
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
                    <button class="btn btn-secondary" style="padding: 8px 15px; font-size: 14px;" 
                            onclick="deleteIncome(${income.id})">Delete</button>
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
                    <button class="btn btn-secondary" style="padding: 8px 15px; font-size: 14px;" 
                            onclick="deleteExpense(${expense.id})">Delete</button>
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
    
    document.getElementById('incomeTab').style.background = tab === 'income' ? 'var(--black)' : 'var(--white)';
    document.getElementById('incomeTab').style.color = tab === 'income' ? 'var(--white)' : 'var(--black)';
    document.getElementById('expenseTab').style.background = tab === 'expense' ? 'var(--black)' : 'var(--white)';
    document.getElementById('expenseTab').style.color = tab === 'expense' ? 'var(--white)' : 'var(--black)';
}

loadSummary();
loadCategories();
loadIncomes();
loadExpenses();
showTab('income');
