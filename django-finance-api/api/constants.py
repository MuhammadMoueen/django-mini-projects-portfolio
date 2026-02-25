# Category type constants
INCOME_TYPE = 'income'
EXPENSE_TYPE = 'expense'

# Available category types for the system
CATEGORY_TYPES = [
    (INCOME_TYPE, 'Income'),
    (EXPENSE_TYPE, 'Expense'),
]

# Default categories for new users - Income
DEFAULT_INCOME_CATEGORIES = [
    'Salary',
    'Freelance',
    'Investment',
    'Business',
    'Gift',
    'Other Income'
]

# Default categories for new users - Expense
DEFAULT_EXPENSE_CATEGORIES = [
    'Food',
    'Transport',
    'Bills',
    'Shopping',
    'Entertainment',
    'Healthcare',
    'Education',
    'Other Expense'
]

# Maximum and minimum amount validation limits
MAX_AMOUNT = 999999999999.99  # Maximum transaction amount
MIN_AMOUNT = 0.01  # Minimum transaction amount
