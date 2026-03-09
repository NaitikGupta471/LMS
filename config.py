# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Naitik4710',  
    'database': 'library'
}

# Admin Settings
ADMIN_PASSWORD_DEFAULT = "Naitik47100" 
ADMIN_SECURITY_CODE = "SECRET123"    

# Application Settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
DEFAULT_ENTRY_WIDTH = 30
MAX_BOOKS_PER_STUDENT = 3
DEFAULT_THEME = "flatly"

# UI Configuration
FONT_FAMILY = 'Helvetica'
FONT_SIZE_LARGE = 20
FONT_SIZE_MEDIUM = 12
FONT_SIZE_SMALL = 10

# Custom Colors
COLORS = {
    'primary': '#0d6efd',
    'secondary': '#6c757d',
    'success': '#198754',
    'danger': '#dc3545',
    'warning': '#ffc107',
    'info': '#0dcaf0',
    'light': '#f8f9fa',
    'dark': '#212529'
}

# File Paths
ADMIN_PASSWORD_FILE = "admin_password.txt"
BACKUP_DIR = "backups"

# Query Limits
TOP_CATEGORIES_LIMIT = 5
RESULTS_PER_PAGE = 15

# Messages
MSG_SUCCESS_BOOK_ADDED = "Book added successfully!"
MSG_SUCCESS_STUDENT_ADDED = "Student added successfully!"
MSG_SUCCESS_PASSWORD_RESET = "Password has been reset successfully!"
MSG_ERROR_INVALID_ID = "Please enter a valid numeric ID!"
MSG_ERROR_NOT_FOUND = "Record not found!"
MSG_ERROR_INVALID_PASSWORD = "Wrong password!"
