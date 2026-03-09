import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import date
import mysql.connector
import ttkbootstrap as tb
from ttkbootstrap.constants import *
# DATABASE CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naitik4710",
    database="library"
)
cursor = db.cursor()
class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Library Management System")
        self.root.geometry("1200x700")
        
        # Initialize ttkbootstrap style using a lighter, more colorful theme
        self.style = tb.Style(theme="flatly")
        # Use a larger, cleaner default font across the app
        self.style.configure('.', font=('Helvetica', 12))
        # Define a standard entry width for compact forms
        self.entry_width = 30
        
        # Custom colors map (may be used later for manual overrides)
        self.colors = {
            'primary': '#0d6efd',
            'secondary': '#6c757d', 
            'success': '#198754',
            'danger': '#dc3545',
            'warning': '#ffc107',
            'info': '#0dcaf0',
            'light': '#f8f9fa',
            'dark': '#212529'
        }
        
        # ensure notifications table exists when the application starts
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notifications (
                    notif_id INT AUTO_INCREMENT PRIMARY KEY,
                    notif_type VARCHAR(20),
                    student_id VARCHAR(255),
                    book_id VARCHAR(255) NULL,
                    reservation_id INT NULL,
                    message TEXT,
                    status VARCHAR(20) DEFAULT 'pending',
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            db.commit()
        except Exception:
            pass
        
        self.show_login_screen()
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    # ==================== LOGIN SCREENS ====================
    def show_login_screen(self):
        """Main login menu"""
        self.clear_window()
        
        # Create main container
        main_frame = tb.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left side - Welcome content
        left_frame = tb.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))
        
        # Welcome section
        welcome_frame = tb.Frame(left_frame, bootstyle="card")
        welcome_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        title_label = tb.Label(welcome_frame, text="📚", font=("Helvetica", 50, "bold"), bootstyle="primary")
        title_label.pack(pady=(40, 10))
        
        subtitle_label = tb.Label(welcome_frame, text="Library Management System", 
                                font=("Helvetica", 26, "bold"), bootstyle="inverse-dark")
        subtitle_label.pack(pady=(0, 10))
        
        desc_label = tb.Label(welcome_frame, 
                            text="Manage your library efficiently with our\ncomprehensive digital solution.\n\nAccess books, track students, and\nstreamline library operations.",
                            font=("Helvetica", 14), bootstyle="secondary", justify=tk.CENTER)
        desc_label.pack(pady=(0, 40))
        
        # Features list
        features_frame = tb.Frame(welcome_frame)
        features_frame.pack(pady=(0, 20))
        
        features = [
            "📖 Book Management",
            "👨‍🎓 Student Records", 
            "📊 Issue & Return Tracking",
            "🔍 Advanced Search"
        ]
        
        for feature in features:
            feature_label = tb.Label(features_frame, text=feature, 
                                   font=("Helvetica", 12), bootstyle="info")
            feature_label.pack(anchor=tk.W, pady=2)
        
        # Right side - Login cards
        right_frame = tb.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Admin login card
        admin_card = tb.Frame(right_frame, bootstyle="card")
        admin_card.pack(fill=tk.X, pady=(0, 20))
        
        admin_title = tb.Label(admin_card, text="🔐 Admin Access", 
                             font=("Helvetica", 18, "bold"), bootstyle="primary")
        admin_title.pack(pady=(20, 15))
        
        admin_desc = tb.Label(admin_card, text="Full system administration\nand management tools", 
                            font=("Helvetica", 12), bootstyle="secondary", justify=tk.CENTER)
        admin_desc.pack(pady=(0, 20))
        
        admin_btn = tb.Button(admin_card, text="Admin Login", 
                            command=self.show_admin_login, 
                            bootstyle="primary-outline", width=20)
        admin_btn.pack(pady=(0, 20))
        
        # Student login card
        student_card = tb.Frame(right_frame, bootstyle="card")
        student_card.pack(fill=tk.X, pady=(0, 20))
        
        student_title = tb.Label(student_card, text="👨‍🎓 Student Portal", 
                               font=("Helvetica", 18, "bold"), bootstyle="success")
        student_title.pack(pady=(20, 15))
        
        student_desc = tb.Label(student_card, text="View issued books and\npersonal library records", 
                              font=("Helvetica", 12), bootstyle="secondary", justify=tk.CENTER)
        student_desc.pack(pady=(0, 20))
        
        student_btn = tb.Button(student_card, text="Student Login", 
                              command=self.show_student_login, 
                              bootstyle="success-outline", width=20)
        student_btn.pack(pady=(0, 20))
        
        # Exit button
        exit_btn = tb.Button(right_frame, text="❌ Exit Application", 
                           command=self.root.quit, 
                           bootstyle="danger-outline", width=25)
        exit_btn.pack(pady=(10, 0))
    def show_admin_login(self):
        """Admin login screen"""
        self.clear_window()
        
        # Center the login form
        main_frame = tb.Frame(self.root)
        main_frame.pack(expand=True)
        
        # Login card - increased height for better layout
        login_frame = tb.Frame(main_frame, bootstyle="card", width=400, height=410)
        login_frame.pack(padx=50, pady=50)
        login_frame.pack_propagate(False)
        
        # Header
        header_frame = tb.Frame(login_frame, bootstyle="primary")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tb.Label(header_frame, text="🔐 Admin Login", 
                             font=("Helvetica", 20, "bold"), bootstyle="inverse-primary")
        title_label.pack(pady=15)
        
        # Form content
        form_frame = tb.Frame(login_frame)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 30))
        
        # Password field
        pass_label = tb.Label(form_frame, text="Administrator Password", 
                            font=("Helvetica", 12), bootstyle="secondary")
        pass_label.pack(anchor=tk.W, pady=(20, 5))
        
        self.admin_pass_entry = tb.Entry(form_frame, show="*", 
                                       font=("Helvetica", 12), width=self.entry_width, bootstyle="primary")
        self.admin_pass_entry.pack(fill=tk.X, pady=(0, 20))
        
        # Buttons
        btn_frame = tb.Frame(form_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        login_btn = tb.Button(btn_frame, text="🔓 Login", 
                            command=self.verify_admin, 
                            bootstyle="primary", width=12)
        login_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        back_btn = tb.Button(btn_frame, text="⬅️ Back", 
                           command=self.show_login_screen, 
                           bootstyle="secondary-outline", width=12)
        back_btn.pack(side=tk.LEFT)
        
        # Reset Password button - for admin too
        reset_frame = tb.Frame(form_frame)
        reset_frame.pack(fill=tk.X, pady=(15, 0))
        
        reset_btn = tb.Button(reset_frame, text="🔑 Reset Password", 
                            command=lambda: self.show_forgot_password("admin"), 
                            bootstyle="warning-outline", width=28)
        reset_btn.pack(pady=(0, 5))
        
        # Help text
        help_frame = tb.Frame(form_frame)
        help_frame.pack(fill=tk.X, pady=(5, 0))
        
        help_text = tb.Label(help_frame, text="Forgot your password? Click the button above", 
                           font=("Helvetica", 9), bootstyle="secondary")
        help_text.pack(side=tk.RIGHT)
        
        # Bind enter key
        self.admin_pass_entry.bind("<Return>", lambda e: self.verify_admin())
        self.admin_pass_entry.focus()
    
    def verify_admin(self):
        password = self.admin_pass_entry.get()
        default_password = "Naitik47100"
        
        # Try to read from saved password file first
        try:
            with open("admin_password.txt", "r") as f:
                saved_password = f.read().strip()
                if saved_password:
                    default_password = saved_password
        except FileNotFoundError:
            pass  # Use default if file doesn't exist
        
        if password == default_password:
            self.show_admin_menu()
        else:
            messagebox.showerror("Error", "Wrong password!")
    def show_student_login(self):
        """Student login screen"""
        self.clear_window()
        
        # Center the login form
        main_frame = tb.Frame(self.root)
        main_frame.pack(expand=True)
        
        # Login card - increased height to accommodate all elements
        login_frame = tb.Frame(main_frame, bootstyle="card", width=400, height=420)
        login_frame.pack(padx=50, pady=50)
        login_frame.pack_propagate(False)
        
        # Header
        header_frame = tb.Frame(login_frame, bootstyle="success")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tb.Label(header_frame, text="👨‍🎓 Student Portal", 
                             font=("Helvetica", 20, "bold"), bootstyle="inverse-success")
        title_label.pack(pady=15)
        
        # Form content
        form_frame = tb.Frame(login_frame)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 30))
        
        # Student ID field
        id_label = tb.Label(form_frame, text="Student ID", 
                          font=("Helvetica", 12), bootstyle="secondary")
        id_label.pack(anchor=tk.W, pady=(20, 5))
        
        self.student_id_entry = tb.Entry(form_frame, font=("Helvetica", 12), width=self.entry_width, bootstyle="success")
        self.student_id_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Password field
        pass_label = tb.Label(form_frame, text="Password", 
                            font=("Helvetica", 12), bootstyle="secondary")
        pass_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.student_pass_entry = tb.Entry(form_frame, show="*", 
                                         font=("Helvetica", 12), width=self.entry_width, bootstyle="success")
        self.student_pass_entry.pack(fill=tk.X, pady=(0, 20))
        
        # Buttons
        btn_frame = tb.Frame(form_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        login_btn = tb.Button(btn_frame, text="🔓 Login", 
                            command=self.verify_student, 
                            bootstyle="success", width=12)
        login_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        back_btn = tb.Button(btn_frame, text="⬅️ Back", 
                           command=self.show_login_screen, 
                           bootstyle="secondary-outline", width=12)
        back_btn.pack(side=tk.LEFT)
        
        # Reset Password button - more prominent
        reset_frame = tb.Frame(form_frame)
        reset_frame.pack(fill=tk.X, pady=(15, 0))
        
        reset_btn = tb.Button(reset_frame, text="🔑 Reset Password", 
                            command=lambda: self.show_forgot_password("student"), 
                            bootstyle="warning-outline", width=28)
        reset_btn.pack(pady=(0, 5))
        
        # Forgot password link (kept for accessibility)
        forgot_frame = tb.Frame(form_frame)
        forgot_frame.pack(fill=tk.X, pady=(5, 0))
        
        forgot_link = tb.Label(forgot_frame, text="Forgot your password? Click the button above", 
                             font=("Helvetica", 9), bootstyle="secondary")
        forgot_link.pack(side=tk.RIGHT)
        
        # Bind enter key
        self.student_id_entry.bind("<Return>", lambda e: self.student_pass_entry.focus())
        self.student_pass_entry.bind("<Return>", lambda e: self.verify_student())
        self.student_id_entry.focus()
    
    def verify_student(self):
        try:
            sid = int(self.student_id_entry.get())
            password = self.student_pass_entry.get()
            cursor.execute("SELECT * FROM students WHERE student_id=%s AND password=%s", (sid, password))
            result = cursor.fetchone()
            if result:
                self.show_student_books(sid)
            else:
                messagebox.showerror("Error", "Invalid login credentials!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid student ID!")
    
    def show_forgot_password(self, user_type):
        """Forgot password screen"""
        self.clear_window()
        
        # Center the form
        main_frame = tb.Frame(self.root)
        main_frame.pack(expand=True)
        
        # Password reset card - increased height for student form
        height_size = 550 if user_type == "student" else 450
        reset_frame = tb.Frame(main_frame, bootstyle="card", width=450, height=height_size)
        reset_frame.pack(padx=50, pady=50)
        reset_frame.pack_propagate(False)
        
        # Header
        header_frame = tb.Frame(reset_frame, bootstyle="warning")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_text = "🔑 Reset Admin Password" if user_type == "admin" else "🔑 Reset Student Password"
        title_label = tb.Label(header_frame, text=title_text, 
                             font=("Helvetica", 18, "bold"), bootstyle="inverse-warning")
        title_label.pack(pady=15)
        
        # Form content
        form_frame = tb.Frame(reset_frame)
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 30))
        
        if user_type == "student":
            # Student ID field
            id_label = tb.Label(form_frame, text="Student ID *", 
                              font=("Helvetica", 12, "bold"), bootstyle="secondary")
            id_label.pack(anchor=tk.W, pady=(20, 5))
            
            id_info = tb.Label(form_frame, text="Enter your student ID to verify your identity", 
                             font=("Helvetica", 9), bootstyle="secondary")
            id_info.pack(anchor=tk.W, pady=(0, 5))
            
            self.reset_student_id_entry = tb.Entry(form_frame, font=("Helvetica", 12), bootstyle="warning", width=self.entry_width)
            self.reset_student_id_entry.pack(fill=tk.X, pady=(0, 15))
        else:
            # Admin uses security code instead of password
            code_label = tb.Label(form_frame, text="Admin Security Code *", 
                                 font=("Helvetica", 12, "bold"), bootstyle="secondary")
            code_label.pack(anchor=tk.W, pady=(20, 5))
            
            self.admin_verify_entry = tb.Entry(form_frame, show="*", font=("Helvetica", 12), bootstyle="warning", width=self.entry_width)
            self.admin_verify_entry.pack(fill=tk.X, pady=(0, 15))
            
            code_hint = tb.Label(form_frame, text="(Use security code instead of password)", 
                               font=("Helvetica", 10), bootstyle="secondary")
            code_hint.pack(anchor=tk.W, pady=(0, 10))
        
        # New password field
        pass_label = tb.Label(form_frame, text="New Password *", 
                            font=("Helvetica", 12, "bold"), bootstyle="secondary")
        pass_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.new_pass_entry = tb.Entry(form_frame, show="*", font=("Helvetica", 12), bootstyle="warning", width=self.entry_width)
        self.new_pass_entry.pack(fill=tk.X, pady=(0, 10))
        
        # Confirm password field
        confirm_label = tb.Label(form_frame, text="Confirm New Password *", 
                               font=("Helvetica", 12, "bold"), bootstyle="secondary")
        confirm_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.confirm_pass_entry = tb.Entry(form_frame, show="*", font=("Helvetica", 12), bootstyle="warning", width=self.entry_width)
        self.confirm_pass_entry.pack(fill=tk.X, pady=(0, 20))
        
        # Buttons
        btn_frame = tb.Frame(form_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        reset_btn = tb.Button(btn_frame, text="🔄 Reset Password", 
                            command=lambda: self.reset_password(user_type), 
                            bootstyle="warning", width=15)
        reset_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        back_btn = tb.Button(btn_frame, text="⬅️ Back", 
                           command=self.show_login_screen, 
                           bootstyle="secondary-outline", width=12)
        back_btn.pack(side=tk.LEFT)
    
    def reset_password(self, user_type):
        """Reset password for user"""
        new_pass = self.new_pass_entry.get()
        confirm_pass = self.confirm_pass_entry.get()
        
        if not new_pass or not confirm_pass:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        if new_pass != confirm_pass:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        try:
            if user_type == "student":
                student_id = self.reset_student_id_entry.get()
                if not student_id:
                    messagebox.showerror("Error", "Please enter student ID!")
                    return
                
                # Check if student exists
                cursor.execute("SELECT * FROM students WHERE student_id=%s", (student_id,))
                if cursor.fetchone():
                    # queue a notification instead of changing password immediately
                    self.add_notification('password_reset', student_id, None, 'Forgot password request')
                    messagebox.showinfo("Request Sent", "Your password reset request has been sent to the admin.")
                    self.show_login_screen()
                else:
                    messagebox.showerror("Error", "Student ID not found!")
                    
            else:  # admin
                admin_code = self.admin_verify_entry.get()
                if not admin_code:
                    messagebox.showerror("Error", "Please enter admin security code!")
                    return
                    
                if admin_code == "SECRET123":  # security code for resetting admin password
                    # Use the new password provided by user, not hardcoded
                    admin_pass_file = "admin_password.txt"
                    try:
                        with open(admin_pass_file, 'w') as f:
                            f.write(new_pass)
                        messagebox.showinfo("Success", f"Admin password has been reset successfully!")
                        self.show_login_screen()
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to reset password: {str(e)}")
                else:
                    messagebox.showerror("Error", "Invalid security code!")
                    
        except Exception as e:
            messagebox.showerror("Error", str(e))
    # ==================== ADMIN MENU ====================
    def show_admin_menu(self):
        """Admin dashboard with sidebar navigation"""
        self.clear_window()
        
        # Main container
        main_frame = tb.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Sidebar
        sidebar = tb.Frame(main_frame, bootstyle="dark", width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)
        
        # Sidebar header
        sidebar_header = tb.Frame(sidebar, bootstyle="primary")
        sidebar_header.pack(fill=tk.X, pady=(0, 20))
        
        header_label = tb.Label(sidebar_header, text="🎯 Admin Panel", 
                              font=("Helvetica", 16, "bold"), bootstyle="inverse-primary")
        header_label.pack(pady=15)
        
        # Navigation buttons
        nav_buttons = [
            ("📚 Books", "primary", self.show_books_section),
            ("👨‍🎓 Students", "success", self.show_students_section),
            ("📖 Issue Books", "info", self.show_issue_section),
            ("📊 Reports", "warning", self.show_reports_section),
            ("� Notifications", "info", self.show_notifications),
            ("�🚪 Logout", "danger", self.confirm_logout)
        ]
        
        for text, style, command in nav_buttons:
            btn = tb.Button(sidebar, text=text, command=command, 
                          bootstyle=f"{style}-outline", width=20)
            btn.pack(pady=5, padx=10)
        
        # Main content area
        self.content_frame = tb.Frame(main_frame, bootstyle="card")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Show default section (Books)
        self.show_books_section()
    
    def show_books_section(self):
        """Books management section"""
        self.clear_content()
        
        # Section header
        header_frame = tb.Frame(self.content_frame, bootstyle="primary")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        section_title = tb.Label(header_frame, text="📚 Books Management", 
                               font=("Helvetica", 20, "bold"), bootstyle="inverse-primary")
        section_title.pack(pady=15)
        
        # Action buttons
        actions_frame = tb.Frame(self.content_frame)
        actions_frame.pack(fill=tk.X, pady=(0, 20))
        
        book_actions = [
            ("➕ Add Book", "success", self.show_add_book),
            ("👁️ View Books", "primary", self.show_view_books),
            ("🔍 Search Book", "info", self.show_search_book),
            ("✏️ Update Book", "warning", self.show_update_book),
            ("🗑️ Delete Book", "danger", self.show_delete_book)
        ]
        
        for text, style, command in book_actions:
            btn = tb.Button(actions_frame, text=text, command=command, 
                          bootstyle=style, width=15)
            btn.pack(side=tk.LEFT, padx=5)
        
        # Quick stats
        stats_frame = tb.Frame(self.content_frame, bootstyle="card")
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Get book count
        cursor.execute("SELECT COUNT(*) FROM books")
        book_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT SUM(quantity) FROM books")
        total_qty = cursor.fetchone()[0] or 0
        
        stats_label = tb.Label(stats_frame, 
                             text=f"📊 Total Books: {book_count} | Total Copies: {total_qty}", 
                             font=("Helvetica", 14), bootstyle="secondary")
        stats_label.pack(pady=15)
    
    def show_students_section(self):
        """Students management section"""
        self.clear_content()
        
        # Section header
        header_frame = tb.Frame(self.content_frame, bootstyle="success")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        section_title = tb.Label(header_frame, text="👨‍🎓 Students Management", 
                               font=("Helvetica", 20, "bold"), bootstyle="inverse-success")
        section_title.pack(pady=15)
        
        # Action buttons
        actions_frame = tb.Frame(self.content_frame)
        actions_frame.pack(fill=tk.X, pady=(0, 20))
        
        student_actions = [
            ("➕ Add Student", "success", self.show_add_student),
            ("👁️ View Students", "primary", self.show_view_students),
            ("🗑️ Delete Student", "danger", self.show_delete_student)
        ]
        
        for text, style, command in student_actions:
            btn = tb.Button(actions_frame, text=text, command=command, 
                          bootstyle=style, width=15)
            btn.pack(side=tk.LEFT, padx=5)
        
        # Quick stats
        stats_frame = tb.Frame(self.content_frame, bootstyle="card")
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Get student count
        cursor.execute("SELECT COUNT(*) FROM students")
        student_count = cursor.fetchone()[0]
        
        stats_label = tb.Label(stats_frame, 
                             text=f"📊 Total Students: {student_count}", 
                             font=("Helvetica", 14), bootstyle="secondary")
        stats_label.pack(pady=15)
    
    def show_issue_section(self):
        """Issue/Return books section"""
        self.clear_content()
        
        # Section header
        header_frame = tb.Frame(self.content_frame, bootstyle="info")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        section_title = tb.Label(header_frame, text="📖 Issue & Return Books", 
                               font=("Helvetica", 20, "bold"), bootstyle="inverse-info")
        section_title.pack(pady=15)
        
        # Action buttons
        actions_frame = tb.Frame(self.content_frame)
        actions_frame.pack(fill=tk.X, pady=(0, 20))
        
        issue_actions = [
            ("📖 Issue Book", "success", self.show_issue_book),
            ("↩️ Return Book", "warning", self.show_return_book),
            ("📊 Issued Books", "primary", self.show_issued_books)
        ]
        
        for text, style, command in issue_actions:
            btn = tb.Button(actions_frame, text=text, command=command, 
                          bootstyle=style, width=15)
            btn.pack(side=tk.LEFT, padx=5)
        
        # Quick stats
        stats_frame = tb.Frame(self.content_frame, bootstyle="card")
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Get issued books count
        cursor.execute("SELECT COUNT(*) FROM issued_books WHERE return_date IS NULL")
        issued_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM issued_books WHERE return_date IS NOT NULL")
        returned_count = cursor.fetchone()[0]
        
        stats_label = tb.Label(stats_frame, 
                             text=f"📊 Currently Issued: {issued_count} | Total Returned: {returned_count}", 
                             font=("Helvetica", 14), bootstyle="secondary")
        stats_label.pack(pady=15)
    
    def show_reports_section(self):
        """Reports and analytics section"""
        self.clear_content()
        
        # Section header
        header_frame = tb.Frame(self.content_frame, bootstyle="warning")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        section_title = tb.Label(header_frame, text="📊 Reports & Analytics", 
                               font=("Helvetica", 20, "bold"), bootstyle="inverse-warning")
        section_title.pack(pady=15)
        
        # Report cards
        reports_frame = tb.Frame(self.content_frame)
        reports_frame.pack(fill=tk.BOTH, expand=True)
        
        # System overview
        overview_card = tb.Frame(reports_frame, bootstyle="card")
        overview_card.pack(fill=tk.X, pady=(0, 10))
        
        overview_title = tb.Label(overview_card, text="📈 System Overview", 
                                font=("Helvetica", 16, "bold"), bootstyle="primary")
        overview_title.pack(pady=(15, 10))
        
        # Get stats
        cursor.execute("SELECT COUNT(*) FROM books")
        books = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM students")
        students = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM issued_books WHERE return_date IS NULL")
        issued = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM reservations WHERE status='pending'")
        pending_reservations = cursor.fetchone()[0]
        
        stats_text = f"Total Books: {books} | Total Students: {students} | Books Currently Issued: {issued} | Pending Reservations: {pending_reservations}"
        overview_stats = tb.Label(overview_card, text=stats_text, 
                                font=("Helvetica", 12), bootstyle="secondary")
        overview_stats.pack(pady=(0, 15))
        
        # Total issued books report
        issued_report_card = tb.Frame(reports_frame, bootstyle="card")
        issued_report_card.pack(fill=tk.X, pady=(0, 10))
        
        issued_title = tb.Label(issued_report_card, text="📊 Total Issued Books Report", 
                              font=("Helvetica", 16, "bold"), bootstyle="success")
        issued_title.pack(pady=(15, 10))
        
        # Get detailed issued books stats
        cursor.execute("SELECT COUNT(*) FROM issued_books")
        total_issued_ever = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM issued_books WHERE return_date IS NULL")
        currently_issued = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM issued_books WHERE return_date IS NOT NULL")
        returned_books = cursor.fetchone()[0]
        
        # Books by category
        cursor.execute("""
            SELECT b.category, COUNT(ib.issue_id) as count 
            FROM issued_books ib 
            JOIN books b ON ib.book_id = b.book_id 
            GROUP BY b.category 
            ORDER BY count DESC 
            LIMIT 5
        """)
        category_stats = cursor.fetchall()
        
        issued_stats = f"Total Ever Issued: {total_issued_ever} | Currently Issued: {currently_issued} | Returned: {returned_books}"
        issued_stats_label = tb.Label(issued_report_card, text=issued_stats, 
                                    font=("Helvetica", 12), bootstyle="secondary")
        issued_stats_label.pack(pady=(0, 10))
        
        if category_stats:
            category_text = "Most Issued Categories: " + ", ".join([f"{cat}: {cnt}" for cat, cnt in category_stats])
            category_label = tb.Label(issued_report_card, text=category_text, 
                                    font=("Helvetica", 12), bootstyle="info")
            category_label.pack(pady=(0, 15))
        
        # Database backup section
        backup_card = tb.Frame(reports_frame, bootstyle="card")
        backup_card.pack(fill=tk.X, pady=(0, 10))
        
        backup_title = tb.Label(backup_card, text="💾 Database Backup", 
                              font=("Helvetica", 16, "bold"), bootstyle="danger")
        backup_title.pack(pady=(15, 10))
        
        backup_desc = tb.Label(backup_card, text="Create a backup of the entire library database", 
                             font=("Helvetica", 12), bootstyle="secondary")
        backup_desc.pack(pady=(0, 15))
        
        backup_btn = tb.Button(backup_card, text="📦 Create Backup", 
                             command=self.create_database_backup, 
                             bootstyle="danger", width=15)
        backup_btn.pack(pady=(0, 15))
        
        # Recent activity
        activity_card = tb.Frame(reports_frame, bootstyle="card")
        activity_card.pack(fill=tk.BOTH, expand=True)
        
        activity_title = tb.Label(activity_card, text="🕒 Recent Activity", 
                                font=("Helvetica", 16, "bold"), bootstyle="warning")
        activity_title.pack(pady=(15, 10))
        
        # Get recent issues
        cursor.execute("SELECT * FROM issued_books ORDER BY issue_date DESC LIMIT 5")
        recent = cursor.fetchall()
        
        if recent:
            for issue in recent:
                activity_text = f"Book ID {issue[1]} issued to Student ID {issue[2]} on {issue[3]}"
                if issue[4]:  # return date
                    activity_text += f" (Returned: {issue[4]})"
                activity_label = tb.Label(activity_card, text=activity_text, 
                                        font=("Helvetica", 12), bootstyle="secondary")
                activity_label.pack(anchor=tk.W, padx=15, pady=2)
        else:
            no_activity = tb.Label(activity_card, text="No recent activity", 
                                 font=("Helvetica", 12), bootstyle="secondary")
            no_activity.pack(pady=10)
    
    def create_database_backup(self):
        """Create a backup of the database"""
        try:
            from datetime import datetime
            import os
            
            # Create backups directory if it doesn't exist
            backup_dir = "backups"
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            # Generate backup filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"{backup_dir}/library_backup_{timestamp}.sql"
            
            # For Windows, we'll create a simple SQL dump using Python
            # This avoids dependency on mysqldump being installed
            
            with open(backup_file, 'w', encoding='utf-8') as f:
                # Write header
                f.write(f"-- Library Management System Database Backup\n")
                f.write(f"-- Created on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("-- " + "="*50 + "\n\n")
                
                # Backup books table
                f.write("-- Books table\n")
                cursor.execute("SELECT * FROM books")
                books = cursor.fetchall()
                for book in books:
                    f.write(f"INSERT INTO books (book_id, title, category, author, quantity) VALUES ({book[0]}, '{book[1].replace(chr(39), chr(39)*2)}', '{book[2]}', '{book[3].replace(chr(39), chr(39)*2)}', {book[4]});\n")
                
                f.write("\n")
                
                # Backup students table
                f.write("-- Students table\n")
                cursor.execute("SELECT * FROM students")
                students = cursor.fetchall()
                for student in students:
                    f.write(f"INSERT INTO students (student_id, name, class, section, password) VALUES ({student[0]}, '{student[1].replace(chr(39), chr(39)*2)}', '{student[2]}', '{student[3]}', '{student[4]}');\n")
                
                f.write("\n")
                
                # Backup issued_books table
                f.write("-- Issued books table\n")
                cursor.execute("SELECT * FROM issued_books")
                issued = cursor.fetchall()
                for issue in issued:
                    return_date = f"'{issue[4]}'" if issue[4] else "NULL"
                    f.write(f"INSERT INTO issued_books (issue_id, book_id, student_id, issue_date, return_date) VALUES ({issue[0]}, {issue[1]}, {issue[2]}, '{issue[3]}', {return_date});\n")
                
                f.write("\n")
                
                # Backup reservations table
                f.write("-- Reservations table\n")
                cursor.execute("SELECT * FROM reservations")
                reservations = cursor.fetchall()
                for res in reservations:
                    f.write(f"INSERT INTO reservations (reservation_id, book_id, student_id, reservation_date, status) VALUES ({res[0]}, {res[1]}, {res[2]}, '{res[3]}', '{res[4]}');\n")
                
                f.write("\n-- Backup completed successfully\n")
            
            messagebox.showinfo("Success", f"Database backup created successfully!\nFile: {backup_file}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Backup creation failed: {str(e)}")
    
    def clear_content(self):
        """Clear the main content area"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def confirm_logout(self):
        """Ask admin to confirm logging out."""
        if messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?"):
            self.show_login_screen()

    def validate_numeric_input(self, value, field_name, max_length=20):
        """Ensure that an input is numeric and within an acceptable length.

        The character limit was raised to 20 to avoid complaints about student ID length.
        """
        if not value:
            messagebox.showerror("Error", f"{field_name} cannot be empty!")
            return False
        if not value.isdigit():
            messagebox.showerror("Error", f"{field_name} must contain only digits.")
            return False
        if len(value) > max_length:
            messagebox.showerror("Error", f"{field_name} cannot exceed {max_length} characters.")
            return False
        return True
    # ==================== BOOK OPERATIONS ====================
    def show_add_book(self):
        """Add book form"""
        self.clear_window()
        frame = ttk.Frame(self.root, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=30)
        title = ttk.Label(frame, text="📚 ADD NEW BOOK", style="Title.TLabel")
        title.pack(pady=20)
        # Center the form content
        form_frame = ttk.Frame(frame, style="Card.TFrame")
        form_frame.pack(pady=20, padx=40)
        fields = {}
        labels = ["Book ID:", "Title:", "Category:", "Author:", "Quantity:"]
        for label_text in labels:
            ttk.Label(form_frame, text=label_text, style="Subtitle.TLabel").pack(anchor=tk.W, pady=8)
            entry = ttk.Entry(form_frame, width=self.entry_width, font=("Helvetica", 12))
            entry.pack(anchor=tk.W, pady=5)
            fields[label_text] = entry
        def add():
            try:
                sql = "INSERT INTO books(book_id,title,category,author,quantity) VALUES(%s,%s,%s,%s,%s)"
                cursor.execute(sql, (
                    fields["Book ID:"].get(),
                    fields["Title:"].get(),
                    fields["Category:"].get(),
                    fields["Author:"].get(),
                    int(fields["Quantity:"].get())
                ))
                db.commit()
                messagebox.showinfo("Success", "Book added successfully!")
                self.show_admin_menu()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        btn_frame = ttk.Frame(frame, style="Card.TFrame")
        btn_frame.pack(pady=25)
        ttk.Button(btn_frame, text="💾 Save", command=add, style="Success.TButton").pack(side=tk.LEFT, padx=15)
        ttk.Button(btn_frame, text="❌ Cancel", command=self.show_admin_menu, style="Danger.TButton").pack(side=tk.LEFT, padx=15)
    def show_view_books(self):
        """View all books with filtering"""
        self.clear_window()
        
        # Header
        header_frame = tb.Frame(self.root, bootstyle="primary")
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        title_label = tb.Label(header_frame, text="📚 All Books", 
                             font=("Helvetica", 22, "bold"), bootstyle="inverse-primary")
        title_label.pack(pady=15)
        
        # Filter section
        filter_frame = tb.Frame(self.root, bootstyle="card")
        filter_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        
        # Filter controls
        controls_frame = tb.Frame(filter_frame)
        controls_frame.pack(fill=tk.X, padx=20, pady=15)
        
        tb.Label(controls_frame, text="Filter by:", font=("Helvetica", 12), bootstyle="secondary").grid(row=0, column=0, padx=(0, 10), pady=5, sticky=tk.W)
        
        self.view_filter_var = tk.StringVar(value="all")
        filter_combo = tb.Combobox(controls_frame, textvariable=self.view_filter_var, 
                                 values=["all", "title", "category", "author"], 
                                 bootstyle="primary", width=15)
        filter_combo.grid(row=0, column=1, padx=(0, 15), pady=5)
        
        tb.Label(controls_frame, text="Search:", font=("Helvetica", 12), bootstyle="secondary").grid(row=0, column=2, padx=(0, 10), pady=5, sticky=tk.W)
        
        self.view_search_entry = tb.Entry(controls_frame, bootstyle="primary", width=25, font=("Helvetica",12))
        self.view_search_entry.grid(row=0, column=3, padx=(0, 15), pady=5)
        
        filter_btn = tb.Button(controls_frame, text="🔍 Filter", 
                             command=self.filter_books_view, bootstyle="primary")
        filter_btn.grid(row=0, column=4, padx=(0, 10), pady=5)
        
        clear_btn = tb.Button(controls_frame, text="🧹 Clear", 
                            command=self.clear_books_filter, bootstyle="secondary-outline")
        clear_btn.grid(row=0, column=5, padx=(0, 10), pady=5)
        
        # Books table
        table_frame = tb.Frame(self.root, bootstyle="card")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # Create treeview
        columns = ("ID", "Title", "Category", "Author", "Qty")
        self.books_tree = tb.Treeview(table_frame, columns=columns, height=15, 
                                    bootstyle="primary", show="headings")
        
        # Configure columns
        self.books_tree.column("ID", width=80, anchor=tk.CENTER)
        self.books_tree.column("Title", width=250, anchor=tk.W)
        self.books_tree.column("Category", width=150, anchor=tk.W)
        self.books_tree.column("Author", width=200, anchor=tk.W)
        self.books_tree.column("Qty", width=80, anchor=tk.CENTER)
        
        # Configure headings
        self.books_tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.books_tree.heading("Title", text="Title", anchor=tk.W)
        self.books_tree.heading("Category", text="Category", anchor=tk.W)
        self.books_tree.heading("Author", text="Author", anchor=tk.W)
        self.books_tree.heading("Qty", text="Qty", anchor=tk.CENTER)
        
        # Add scrollbar
        scrollbar = tb.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.books_tree.yview, bootstyle="primary-round")
        self.books_tree.configure(yscrollcommand=scrollbar.set)
        
        self.books_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=15)
        
        # Load all books initially
        self.load_all_books()
        
        # Back button
        back_frame = tb.Frame(self.root)
        back_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        back_btn = tb.Button(back_frame, text="⬅️ Back", 
                           command=self.show_admin_menu, 
                           bootstyle="secondary-outline", width=15)
        back_btn.pack(side=tk.LEFT)
    
    def load_all_books(self):
        """Load all books into the treeview"""
        # Clear existing items
        for item in self.books_tree.get_children():
            self.books_tree.delete(item)
        
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        
        for book in books:
            self.books_tree.insert("", tk.END, values=(book[0], book[1], book[2], book[3], book[4]))
    
    def filter_books_view(self):
        """Filter books based on search criteria"""
        # Clear existing items
        for item in self.books_tree.get_children():
            self.books_tree.delete(item)
        
        filter_by = self.view_filter_var.get()
        search_val = self.view_search_entry.get().strip()
        
        if filter_by == "all" or not search_val:
            # Load all books
            self.load_all_books()
        else:
            # Filter books
            cursor.execute(f"SELECT * FROM books WHERE {filter_by} LIKE %s", (f"%{search_val}%",))
            books = cursor.fetchall()
            
            for book in books:
                self.books_tree.insert("", tk.END, values=(book[0], book[1], book[2], book[3], book[4]))
    
    def clear_books_filter(self):
        """Clear filter and show all books"""
        self.view_filter_var.set("all")
        self.view_search_entry.delete(0, tk.END)
        self.load_all_books()
    def show_search_book(self):
        """Search book"""
        self.clear_window()
        frame = ttk.Frame(self.root, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        title = ttk.Label(frame, text="🔍 SEARCH BOOKS", style="Title.TLabel")
        title.pack(pady=20)
        
        # Results section - Create FIRST before defining functions that reference it
        result_frame = ttk.Frame(frame, style="Card.TFrame")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)
        columns = ("ID", "Title", "Category", "Author", "Qty")
        tree = ttk.Treeview(result_frame, columns=columns, height=12)
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("ID", anchor=tk.CENTER, width=80)
        tree.column("Title", anchor=tk.W, width=220)
        tree.column("Category", anchor=tk.W, width=130)
        tree.column("Author", anchor=tk.W, width=170)
        tree.column("Qty", anchor=tk.CENTER, width=60)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Title", text="Title", anchor=tk.W)
        tree.heading("Category", text="Category", anchor=tk.W)
        tree.heading("Author", text="Author", anchor=tk.W)
        tree.heading("Qty", text="Qty", anchor=tk.CENTER)
        tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Filter section
        filter_frame = ttk.Frame(frame, style="Card.TFrame")
        filter_frame.pack(pady=15, padx=40, fill=tk.X)
        # Filter options
        ttk.Label(filter_frame, text="Filter by:", style="Subtitle.TLabel").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.filter_var = tk.StringVar(value="title")
        filter_combo = ttk.Combobox(filter_frame, textvariable=self.filter_var, 
                                   values=["title", "category", "author"], 
                                   state="readonly", width=15, font=("Helvetica", 12))
        filter_combo.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(filter_frame, text="Search:", style="Subtitle.TLabel").grid(row=0, column=2, padx=5, pady=5)
        self.search_entry = ttk.Entry(filter_frame, width=25, font=("Helvetica", 12))
        self.search_entry.grid(row=0, column=3, padx=5, pady=5)
        
        def search():
            """Search and filter books in treeview"""
            for item in tree.get_children():
                tree.delete(item)
            search_val = self.search_entry.get()
            filter_by = self.filter_var.get()
            if search_val.strip():
                cursor.execute(f"SELECT * FROM books WHERE {filter_by} LIKE %s", (f"%{search_val}%",))
            else:
                cursor.execute("SELECT * FROM books")
            results = cursor.fetchall()
            for book in results:
                tree.insert(parent="", index="end", values=(book[0], book[1], book[2], book[3], book[4]))
        
        def clear_filters():
            """Clear search filters and reload all books"""
            self.search_entry.delete(0, tk.END)
            self.filter_var.set("title")
            search()
        
        ttk.Button(filter_frame, text="🔍 Search", command=search, style="Primary.TButton").grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(filter_frame, text="🧹 Clear", command=clear_filters, style="Danger.TButton").grid(row=0, column=5, padx=5, pady=5)
        # Load all books initially
        search()
        btn_frame = ttk.Frame(frame, style="Card.TFrame")
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="⬅️ Back", command=self.show_admin_menu, style="Primary.TButton").pack(side=tk.LEFT, padx=10)
    def show_update_book(self):
        """Update book quantity"""
        self.clear_window()
        frame = ttk.Frame(self.root, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)
        title = ttk.Label(frame, text="✏️ UPDATE BOOK", style="Title.TLabel")
        title.pack(pady=25)
        form_frame = ttk.Frame(frame, style="Card.TFrame")
        form_frame.pack(pady=20, padx=40)
        ttk.Label(form_frame, text="Book ID:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=10)
        id_entry = ttk.Entry(form_frame, width=self.entry_width, font=("Helvetica", 12))
        id_entry.pack(anchor=tk.W, pady=5)
        ttk.Label(form_frame, text="New Quantity:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=10)
        qty_entry = ttk.Entry(form_frame, width=self.entry_width, font=("Helvetica", 12))
        qty_entry.pack(anchor=tk.W, pady=5)
        def update():
            bid = id_entry.get().strip()
            if not self.validate_numeric_input(bid, "Book ID"):
                return
            qty_val = qty_entry.get().strip()
            if not qty_val.isdigit():
                messagebox.showerror("Error", "Quantity must be a number.")
                return
            try:
                cursor.execute("UPDATE books SET quantity=%s WHERE book_id=%s", 
                             (int(qty_val), bid))
                db.commit()
                messagebox.showinfo("Success", "Book updated successfully!")
                self.show_admin_menu()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        btn_frame = ttk.Frame(frame, style="Card.TFrame")
        btn_frame.pack(pady=25)
        ttk.Button(btn_frame, text="💾 Update", command=update, style="Success.TButton").pack(side=tk.LEFT, padx=15)
        ttk.Button(btn_frame, text="❌ Cancel", command=self.show_admin_menu, style="Danger.TButton").pack(side=tk.LEFT, padx=15)
    def show_delete_book(self):
        """Delete book"""
        self.clear_window()
        frame = ttk.Frame(self.root, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        title = ttk.Label(frame, text="🗑️ DELETE BOOK", style="Title.TLabel")
        title.pack(pady=20)
        # Filter section
        filter_frame = ttk.Frame(frame, style="Card.TFrame")
        filter_frame.pack(pady=15, padx=40, fill=tk.X)
        ttk.Label(filter_frame, text="Filter by:", style="Subtitle.TLabel").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.delete_filter_var = tk.StringVar(value="title")
        filter_combo = ttk.Combobox(filter_frame, textvariable=self.delete_filter_var, 
                                   values=["title", "category", "author"], 
                                   state="readonly", width=15, font=("Helvetica", 12))
        filter_combo.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(filter_frame, text="Search:", style="Subtitle.TLabel").grid(row=0, column=2, padx=5, pady=5)
        self.delete_search_entry = ttk.Entry(filter_frame, width=25, font=("Helvetica", 12))
        self.delete_search_entry.grid(row=0, column=3, padx=5, pady=5)
        def filter_books():
            for item in tree.get_children():
                tree.delete(item)
            search_val = self.delete_search_entry.get()
            filter_by = self.delete_filter_var.get()
            if search_val.strip():
                cursor.execute(f"SELECT * FROM books WHERE {filter_by} LIKE %s", (f"%{search_val}%",))
            else:
                cursor.execute("SELECT * FROM books")
            results = cursor.fetchall()
            for book in results:
                tree.insert(parent="", index="end", values=(book[0], book[1], book[2], book[3], book[4]))
        def clear_filters():
            self.delete_search_entry.delete(0, tk.END)
            self.delete_filter_var.set("title")
            filter_books()
        ttk.Button(filter_frame, text="🔍 Filter", command=filter_books, style="Primary.TButton").grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(filter_frame, text="🧹 Clear", command=clear_filters, style="Danger.TButton").grid(row=0, column=5, padx=5, pady=5)
        # Books list section
        list_frame = ttk.Frame(frame, style="Card.TFrame")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)
        columns = ("ID", "Title", "Category", "Author", "Qty")
        tree = ttk.Treeview(list_frame, columns=columns, height=10)
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("ID", anchor=tk.CENTER, width=80)
        tree.column("Title", anchor=tk.W, width=220)
        tree.column("Category", anchor=tk.W, width=130)
        tree.column("Author", anchor=tk.W, width=170)
        tree.column("Qty", anchor=tk.CENTER, width=60)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Title", text="Title", anchor=tk.W)
        tree.heading("Category", text="Category", anchor=tk.W)
        tree.heading("Author", text="Author", anchor=tk.W)
        tree.heading("Qty", text="Qty", anchor=tk.CENTER)
        tree.pack(fill=tk.BOTH, expand=True, pady=10)
        # bind selection to id entry
        def select_book(event):
            sel = tree.focus()
            if sel:
                vals = tree.item(sel,'values')
                id_entry.delete(0,tk.END)
                id_entry.insert(0, vals[0])
        tree.bind("<<TreeviewSelect>>", select_book)
        # Load all books initially
        filter_books()
        # Delete section
        delete_frame = ttk.Frame(frame, style="Card.TFrame")
        delete_frame.pack(pady=15, padx=40, fill=tk.X)
        ttk.Label(delete_frame, text="Enter Book ID to Delete:", style="Subtitle.TLabel").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        id_entry = ttk.Entry(delete_frame, width=20, font=("Helvetica", 12))
        id_entry.grid(row=0, column=1, padx=5, pady=5)
        def delete():
            bid = id_entry.get().strip()
            if not self.validate_numeric_input(bid, "Book ID"):
                return
            if messagebox.askyesno("Confirm", "Are you sure you want to delete this book?"):
                try:
                    cursor.execute("DELETE FROM books WHERE book_id=%s", (bid,))
                    db.commit()
                    messagebox.showinfo("Success", "Book deleted successfully!")
                    filter_books()  # Refresh the list
                    id_entry.delete(0, tk.END)
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        ttk.Button(delete_frame, text="🗑️ Delete", command=delete, style="Danger.TButton").grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(delete_frame, text="⬅️ Back", command=self.show_admin_menu, style="Primary.TButton").grid(row=0, column=3, padx=5, pady=5)
    # ==================== STUDENT OPERATIONS ====================
    def show_add_student(self):
        """Add student"""
        self.clear_window()
        frame = ttk.Frame(self.root, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=30)
        title = ttk.Label(frame, text="👨‍🎓 ADD NEW STUDENT", style="Title.TLabel")
        title.pack(pady=20)
        form_frame = ttk.Frame(frame, style="Card.TFrame")
        form_frame.pack(pady=20, padx=40)
        ttk.Label(form_frame, text="Student ID:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=8)
        id_entry = ttk.Entry(form_frame, width=self.entry_width, font=("Helvetica", 12))
        id_entry.pack(anchor=tk.W, pady=5)
        ttk.Label(form_frame, text="Student Name:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=8)
        name_entry = ttk.Entry(form_frame, width=self.entry_width, font=("Helvetica", 12))
        name_entry.pack(anchor=tk.W, pady=5)
        ttk.Label(form_frame, text="Class:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=8)
        class_entry = ttk.Entry(form_frame, width=self.entry_width, font=("Helvetica", 12))
        class_entry.pack(anchor=tk.W, pady=5)
        ttk.Label(form_frame, text="Section:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=8)
        section_entry = ttk.Entry(form_frame, width=self.entry_width, font=("Helvetica", 12))
        section_entry.pack(anchor=tk.W, pady=5)
        ttk.Label(form_frame, text="Password:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=8)
        pass_entry = ttk.Entry(form_frame, show="*", width=self.entry_width, font=("Helvetica", 12))
        pass_entry.pack(anchor=tk.W, pady=5)
        ttk.Label(form_frame, text="Confirm Password:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=8)
        confirm_entry = ttk.Entry(form_frame, show="*", width=self.entry_width, font=("Helvetica", 12))
        confirm_entry.pack(anchor=tk.W, pady=5)
        def add():
            sid_val = id_entry.get().strip()
            if not self.validate_numeric_input(sid_val, "Student ID"):
                return
            if pass_entry.get() != confirm_entry.get():
                messagebox.showerror("Error", "Passwords do not match!")
                return
            try:
                cursor.execute("INSERT INTO students(student_id,name,class,section,password) VALUES(%s,%s,%s,%s,%s)",
                             (int(sid_val), name_entry.get(), class_entry.get(), section_entry.get(), pass_entry.get()))
                db.commit()
                messagebox.showinfo("Success", "Student added successfully!")
                self.show_admin_menu()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        btn_frame = ttk.Frame(frame, style="Card.TFrame")
        btn_frame.pack(pady=25)
        ttk.Button(btn_frame, text="💾 Save", command=add, style="Success.TButton").pack(side=tk.LEFT, padx=15)
        ttk.Button(btn_frame, text="❌ Cancel", command=self.show_admin_menu, style="Danger.TButton").pack(side=tk.LEFT, padx=15)
    def show_view_students(self):
        """View all students with modern UI"""
        self.clear_window()
        
        # Header
        header_frame = tb.Frame(self.root, bootstyle="success")
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        title_label = tb.Label(header_frame, text="📋 All Students", 
                             font=("Helvetica", 22, "bold"), bootstyle="inverse-success")
        title_label.pack(pady=15)
        
        # Students table
        table_frame = tb.Frame(self.root, bootstyle="card")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create treeview
        columns = ("S.No", "Student ID", "Name", "Class", "Section", "Password")
        self.students_tree = tb.Treeview(table_frame, columns=columns, height=15, 
                                       bootstyle="success", show="headings")
        
        # Configure columns
        self.students_tree.column("S.No", width=60, anchor=tk.CENTER)
        self.students_tree.column("Student ID", width=120, anchor=tk.CENTER)
        self.students_tree.column("Name", width=200, anchor=tk.W)
        self.students_tree.column("Class", width=100, anchor=tk.CENTER)
        self.students_tree.column("Section", width=100, anchor=tk.CENTER)
        self.students_tree.column("Password", width=200, anchor=tk.W)
        
        # Configure headings
        self.students_tree.heading("S.No", text="S.No", anchor=tk.CENTER)
        self.students_tree.heading("Student ID", text="Student ID", anchor=tk.CENTER)
        self.students_tree.heading("Name", text="Name", anchor=tk.W)
        self.students_tree.heading("Class", text="Class", anchor=tk.CENTER)
        self.students_tree.heading("Section", text="Section", anchor=tk.CENTER)
        self.students_tree.heading("Password", text="Password", anchor=tk.W)
        
        # Add scrollbar
        scrollbar = tb.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.students_tree.yview, bootstyle="success-round")
        self.students_tree.configure(yscrollcommand=scrollbar.set)
        
        self.students_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=15)
        
        # Load all students
        self.load_all_students()
        
        # Back button
        back_frame = tb.Frame(self.root)
        back_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        back_btn = tb.Button(back_frame, text="⬅️ Back", 
                           command=self.show_admin_menu, 
                           bootstyle="secondary-outline", width=15)
        back_btn.pack(side=tk.LEFT)
    
    def load_all_students(self):
        """Load all students into the treeview"""
        # Clear existing items
        for item in self.students_tree.get_children():
            self.students_tree.delete(item)
        
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        
        for i, student in enumerate(students, 1):
            self.students_tree.insert("", tk.END, values=(i, student[0], student[1], 
                                                        student[3] or "", student[4] or "", student[2]))
    def show_delete_student(self):
        """Delete student"""
        self.clear_window()
        frame = ttk.Frame(self.root, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        title = ttk.Label(frame, text="🗑️ DELETE STUDENT", style="Title.TLabel")
        title.pack(pady=20)
        
        # Students list section - Create FIRST before functions that reference it
        list_frame = ttk.Frame(frame, style="Card.TFrame")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)
        columns = ("S.No", "Student ID", "Name", "Class", "Section", "Password")
        tree = ttk.Treeview(list_frame, columns=columns, height=10)
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("S.No", anchor=tk.CENTER, width=60)
        tree.column("Student ID", anchor=tk.CENTER, width=100)
        tree.column("Name", anchor=tk.W, width=200)
        tree.column("Class", anchor=tk.CENTER, width=80)
        tree.column("Section", anchor=tk.CENTER, width=80)
        tree.column("Password", anchor=tk.W, width=250)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("S.No", text="S.No", anchor=tk.CENTER)
        tree.heading("Student ID", text="Student ID", anchor=tk.CENTER)
        tree.heading("Name", text="Name", anchor=tk.W)
        tree.heading("Class", text="Class", anchor=tk.CENTER)
        tree.heading("Section", text="Section", anchor=tk.CENTER)
        tree.heading("Password", text="Password", anchor=tk.W)
        tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Filter section
        filter_frame = ttk.Frame(frame, style="Card.TFrame")
        filter_frame.pack(pady=15, padx=40, fill=tk.X)
        ttk.Label(filter_frame, text="Filter by:", style="Subtitle.TLabel").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.delete_student_filter_var = tk.StringVar(value="name")
        filter_combo = ttk.Combobox(filter_frame, textvariable=self.delete_student_filter_var, 
                                   values=["name", "student_id", "class"], 
                                   state="readonly", width=15, font=("Helvetica", 12))
        filter_combo.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(filter_frame, text="Search:", style="Subtitle.TLabel").grid(row=0, column=2, padx=5, pady=5)
        self.delete_student_search_entry = ttk.Entry(filter_frame, width=25, font=("Helvetica", 12))
        self.delete_student_search_entry.grid(row=0, column=3, padx=5, pady=5)
        
        def filter_students():
            """Filter and display students"""
            for item in tree.get_children():
                tree.delete(item)
            search_val = self.delete_student_search_entry.get()
            filter_by = self.delete_student_filter_var.get()
            if search_val.strip():
                cursor.execute(f"SELECT * FROM students WHERE {filter_by} LIKE %s", (f"%{search_val}%",))
            else:
                cursor.execute("SELECT * FROM students")
            results = cursor.fetchall()
            for i, student in enumerate(results, 1):
                tree.insert(parent="", index="end", values=(i, student[0], student[1], student[3] or "", student[4] or "", student[2]))
        
        def clear_filters():
            """Clear search filters"""
            self.delete_student_search_entry.delete(0, tk.END)
            self.delete_student_filter_var.set("name")
            filter_students()
        
        ttk.Button(filter_frame, text="🔍 Filter", command=filter_students, style="Primary.TButton").grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(filter_frame, text="🧹 Clear", command=clear_filters, style="Danger.TButton").grid(row=0, column=5, padx=5, pady=5)
        
        # Bind selection to id entry
        def select_student(event):
            """Populate ID entry when student selected"""
            sel = tree.focus()
            if sel:
                vals = tree.item(sel, 'values')
                id_entry.delete(0, tk.END)
                id_entry.insert(0, vals[1])
        
        tree.bind("<<TreeviewSelect>>", select_student)
        
        # Load all students initially
        filter_students()
        
        # Delete section
        delete_frame = ttk.Frame(frame, style="Card.TFrame")
        delete_frame.pack(pady=15, padx=40, fill=tk.X)
        ttk.Label(delete_frame, text="Enter Student ID to Delete:", style="Subtitle.TLabel").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        id_entry = ttk.Entry(delete_frame, width=20, font=("Helvetica", 12))
        id_entry.grid(row=0, column=1, padx=5, pady=5)
        def delete():
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?\nThis action cannot be undone."):
                try:
                    cursor.execute("DELETE FROM students WHERE student_id=%s", (id_entry.get(),))
                    db.commit()
                    messagebox.showinfo("Success", "Student deleted successfully!")
                    filter_students()  # Refresh the list
                    id_entry.delete(0, tk.END)
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        ttk.Button(delete_frame, text="🗑️ Delete", command=delete, style="Danger.TButton").grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(delete_frame, text="⬅️ Back", command=self.show_admin_menu, style="Primary.TButton").grid(row=0, column=3, padx=5, pady=5)
    def show_issue_book(self):
        """Issue book to student"""
        self.clear_window()
        frame = ttk.Frame(self.root, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)
        title = ttk.Label(frame, text="📖 ISSUE BOOK", style="Title.TLabel")
        title.pack(pady=25)
        form_frame = ttk.Frame(frame, style="Card.TFrame")
        form_frame.pack(pady=20, padx=40, side=tk.LEFT)
        ttk.Label(form_frame, text="Book ID:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=10)
        book_entry = ttk.Entry(form_frame, width=self.entry_width, font=("Helvetica", 12))
        book_entry.pack(anchor=tk.W, pady=5)
        ttk.Label(form_frame, text="Student ID:", style="Subtitle.TLabel").pack(anchor=tk.W, pady=10)
        student_entry = ttk.Entry(form_frame, width=self.entry_width, font=("Helvetica", 12))
        student_entry.pack(anchor=tk.W, pady=5)
        # small list of available books for quick selection
        list_frame = ttk.Frame(frame, style="Card.TFrame")
        list_frame.pack(padx=20, pady=20, side=tk.RIGHT, fill=tk.BOTH, expand=True)
        ttk.Label(list_frame, text="Available Books", style="Subtitle.TLabel").pack(pady=5)
        cols = ("ID","Title","Qty")
        books_tree = ttk.Treeview(list_frame, columns=cols, show="headings", height=10)
        for c,w in zip(cols,(60,200,60)):
            books_tree.column(c, anchor=tk.W if c=="Title" else tk.CENTER, width=w)
            books_tree.heading(c, text=c)
        books_tree.pack(fill=tk.BOTH, expand=True)
        # load available books
        cursor.execute("SELECT book_id,title,quantity FROM books WHERE quantity>0")
        for b in cursor.fetchall():
            books_tree.insert("", tk.END, values=b)
        def choose_book(event):
            sel = books_tree.focus()
            if sel:
                vals = books_tree.item(sel,'values')
                book_entry.delete(0,tk.END)
                book_entry.insert(0, vals[0])
        books_tree.bind("<<TreeviewSelect>>", choose_book)
        def issue():
            # Validation
            bid = book_entry.get().strip()
            sid = student_entry.get().strip()
            if not self.validate_numeric_input(bid, "Book ID") or not self.validate_numeric_input(sid, "Student ID"):
                return
            try:
                book_id = int(bid)
                student_id = int(sid)
                
                # Check if student exists FIRST
                cursor.execute("SELECT * FROM students WHERE student_id=%s", (student_id,))
                if not cursor.fetchone():
                    messagebox.showerror("Error", "Student ID does not exist!")
                    return
                
                # Check if book exists and is available
                cursor.execute("SELECT quantity FROM books WHERE book_id=%s", (book_id,))
                qty = cursor.fetchone()
                if not qty or qty[0] <= 0:
                    messagebox.showerror("Error", "Book not available!")
                    return
                
                # Check if student already has this book issued (no duplicates)
                cursor.execute("SELECT * FROM issued_books WHERE book_id=%s AND student_id=%s AND return_date IS NULL", 
                             (book_id, student_id))
                existing_issue = cursor.fetchone()
                if existing_issue:
                    messagebox.showerror("Error", "This student already has this book issued!")
                    return
                
                # Check if student has reached the 3-book limit
                cursor.execute("SELECT COUNT(*) FROM issued_books WHERE student_id=%s AND return_date IS NULL", 
                             (student_id,))
                current_books = cursor.fetchone()[0]
                if current_books >= 3:
                    messagebox.showerror("Error", "Student has reached the maximum limit of 3 books!")
                    return
                
                # Issue the book
                cursor.execute(
                    "INSERT INTO issued_books(book_id,student_id,issue_date) VALUES(%s,%s,%s)",
                    (book_id, student_id, date.today())
                )
                cursor.execute("UPDATE books SET quantity=quantity-1 WHERE book_id=%s", (book_id,))
                db.commit()
                messagebox.showinfo("Success", "Book issued successfully!")
                self.show_admin_menu()
                
            except Exception as e:
                messagebox.showerror("Error", str(e))
        btn_frame = ttk.Frame(frame, style="Card.TFrame")
        btn_frame.pack(pady=25)
        ttk.Button(btn_frame, text="📖 Issue", command=issue, style="Success.TButton").pack(side=tk.LEFT, padx=15)
        ttk.Button(btn_frame, text="❌ Cancel", command=self.show_admin_menu, style="Danger.TButton").pack(side=tk.LEFT, padx=15)
    def show_return_book(self):
        """Return book using selection rather than typing an issue id"""
        self.clear_window()
        frame = ttk.Frame(self.root, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        title = ttk.Label(frame, text="↩️ RETURN BOOK", style="Title.TLabel")
        title.pack(pady=20)
        # issued list
        # optional filter by student or book id
        filter_frame = tb.Frame(frame)
        filter_frame.pack(fill=tk.X, padx=20, pady=(0,10))
        tb.Label(filter_frame, text="Filter (Student or Book ID):", font=("Helvetica",12)).pack(side=tk.LEFT)
        self.return_filter_entry = ttk.Entry(filter_frame, width=15, font=("Helvetica",12))
        self.return_filter_entry.pack(side=tk.LEFT, padx=5)
        
        tree_frame = tb.Frame(frame, bootstyle="card")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0,20))
        cols = ("Issue ID","Book ID","Student ID","Issue Date")
        self.return_tree = tb.Treeview(tree_frame, columns=cols, show="headings", height=10)
        for c,w in zip(cols,(80,80,100,120)):
            self.return_tree.column(c, anchor=tk.CENTER, width=w)
            self.return_tree.heading(c, text=c)
        self.return_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tb.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.return_tree.yview, bootstyle="info-round")
        self.return_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # filter function now that tree exists
        def apply_filter():
            fval = self.return_filter_entry.get().strip()
            for item in self.return_tree.get_children():
                self.return_tree.delete(item)
            if fval.isdigit():
                cursor.execute("SELECT issue_id, book_id, student_id, issue_date FROM issued_books WHERE return_date IS NULL AND (student_id=%s OR book_id=%s)", (fval,fval))
            else:
                cursor.execute("SELECT issue_id, book_id, student_id, issue_date FROM issued_books WHERE return_date IS NULL")
            for row in cursor.fetchall():
                self.return_tree.insert("", tk.END, values=row)
        ttk.Button(filter_frame, text="🔍", command=apply_filter, bootstyle="primary").pack(side=tk.LEFT)
        
        # Load issued books data
        cursor.execute("SELECT issue_id, book_id, student_id, issue_date FROM issued_books WHERE return_date IS NULL")
        for row in cursor.fetchall():
            self.return_tree.insert("", tk.END, values=row)
        # info area
        info_frame = tb.Frame(frame, style="Card.TFrame")
        info_frame.pack(fill=tk.X, padx=20, pady=(0,20))
        ttk.Label(info_frame, text="Selected Issue ID:", style="Subtitle.TLabel").grid(row=0,column=0,sticky=tk.W, padx=5, pady=5)
        self.selected_issue_var = tk.StringVar()
        ttk.Entry(info_frame, textvariable=self.selected_issue_var, width=15, state="readonly").grid(row=0,column=1,padx=5,pady=5)
        ttk.Label(info_frame, text="Return Date (YYYY-MM-DD):", style="Subtitle.TLabel").grid(row=1,column=0,sticky=tk.W, padx=5, pady=5)
        self.return_date_entry = ttk.Entry(info_frame, width=20, font=("Helvetica",12))
        self.return_date_entry.grid(row=1,column=1,padx=5,pady=5)
        # set today default
        self.return_date_entry.insert(0, date.today().isoformat())
        def on_select(event):
            sel = self.return_tree.focus()
            if sel:
                vals = self.return_tree.item(sel,'values')
                self.selected_issue_var.set(vals[0])
        self.return_tree.bind("<<TreeviewSelect>>", on_select)
        def ret():
            iid = self.selected_issue_var.get()
            if not iid:
                messagebox.showerror("Error","Select an issued book first")
                return
            rd = self.return_date_entry.get().strip()
            try:
                cursor.execute("SELECT book_id FROM issued_books WHERE issue_id=%s", (iid,))
                book = cursor.fetchone()
                if not book:
                    messagebox.showerror("Error","Selected issue not found")
                    return
                cursor.execute("UPDATE issued_books SET return_date=%s WHERE issue_id=%s", (rd, iid))
                cursor.execute("UPDATE books SET quantity=quantity+1 WHERE book_id=%s", (book[0],))
                db.commit()
                messagebox.showinfo("Success","Book returned successfully!")
                self.show_admin_menu()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        btn_frame = ttk.Frame(frame, style="Card.TFrame")
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="↩️ Return", command=ret, style="Success.TButton").pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="❌ Cancel", command=self.show_admin_menu, style="Danger.TButton").pack(side=tk.LEFT, padx=10)
    def show_issued_books(self):
        """View all issued books"""
        self.clear_window()
        frame = ttk.Frame(self.root, style="Card.TFrame")
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        title = ttk.Label(frame, text="📊 ISSUED BOOKS", style="Title.TLabel")
        title.pack(pady=20)
        columns = ("Issue ID", "Book ID", "Student ID", "Issue Date", "Return Date")
        tree = ttk.Treeview(frame, columns=columns, height=18)
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Issue ID", anchor=tk.CENTER, width=80)
        tree.column("Book ID", anchor=tk.CENTER, width=80)
        tree.column("Student ID", anchor=tk.CENTER, width=100)
        tree.column("Issue Date", anchor=tk.CENTER, width=120)
        tree.column("Return Date", anchor=tk.CENTER, width=120)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Issue ID", text="Issue ID", anchor=tk.CENTER)
        tree.heading("Book ID", text="Book ID", anchor=tk.CENTER)
        tree.heading("Student ID", text="Student ID", anchor=tk.CENTER)
        tree.heading("Issue Date", text="Issue Date", anchor=tk.CENTER)
        tree.heading("Return Date", text="Return Date", anchor=tk.CENTER)
        cursor.execute("SELECT * FROM issued_books")
        issued = cursor.fetchall()
        for issue in issued:
            tree.insert(parent="", index="end", values=issue)
        tree.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)
        ttk.Button(frame, text="⬅️ Back", command=self.show_admin_menu, style="Primary.TButton").pack(pady=15)
    # ==================== STUDENT MENU ====================
    def show_student_books(self, sid):
        """Show books issued to student with reservation option"""
        self.clear_window()
        
        # Header
        header_frame = tb.Frame(self.root, bootstyle="success")
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        title_label = tb.Label(header_frame, text=f"📚 My Books (Student ID: {sid})", 
                             font=("Helvetica", 22, "bold"), bootstyle="inverse-success")
        title_label.pack(pady=15)
        
        # Action buttons
        actions_frame = tb.Frame(self.root, bootstyle="card")
        actions_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        
        btn_frame = tb.Frame(actions_frame)
        btn_frame.pack(fill=tk.X, padx=20, pady=15)
        
        reserve_btn = tb.Button(btn_frame, text="📖 Reserve Book", 
                              command=lambda: self.show_reserve_book(sid), 
                              bootstyle="info", width=15)
        reserve_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        my_reservations_btn = tb.Button(btn_frame, text="📋 My Reservations", 
                                      command=lambda: self.show_my_reservations(sid), 
                                      bootstyle="warning", width=15)
        my_reservations_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Issued books table
        table_frame = tb.Frame(self.root, bootstyle="card")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # Create treeview
        columns = ("Issue ID", "Book ID", "Issue Date", "Return Date")
        self.student_books_tree = tb.Treeview(table_frame, columns=columns, height=12, 
                                            bootstyle="success", show="headings")
        
        # Configure columns
        self.student_books_tree.column("Issue ID", width=100, anchor=tk.CENTER)
        self.student_books_tree.column("Book ID", width=100, anchor=tk.CENTER)
        self.student_books_tree.column("Issue Date", width=150, anchor=tk.CENTER)
        self.student_books_tree.column("Return Date", width=150, anchor=tk.CENTER)
        
        # Configure headings
        self.student_books_tree.heading("Issue ID", text="Issue ID", anchor=tk.CENTER)
        self.student_books_tree.heading("Book ID", text="Book ID", anchor=tk.CENTER)
        self.student_books_tree.heading("Issue Date", text="Issue Date", anchor=tk.CENTER)
        self.student_books_tree.heading("Return Date", text="Return Date", anchor=tk.CENTER)
        
        # Add scrollbar
        scrollbar = tb.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.student_books_tree.yview, bootstyle="success-round")
        self.student_books_tree.configure(yscrollcommand=scrollbar.set)
        
        self.student_books_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=15)
        
        # Load issued books
        self.load_student_books(sid)
        
        # Back button
        back_frame = tb.Frame(self.root)
        back_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        back_btn = tb.Button(back_frame, text="⬅️ Back to Login", 
                           command=self.show_login_screen, 
                           bootstyle="secondary-outline", width=15)
        back_btn.pack(side=tk.LEFT)
    
    def load_student_books(self, sid):
        """Load student's issued books"""
        # Clear existing items
        for item in self.student_books_tree.get_children():
            self.student_books_tree.delete(item)
        
        cursor.execute("SELECT * FROM issued_books WHERE student_id=%s", (sid,))
        books = cursor.fetchall()
        
        for book in books:
            self.student_books_tree.insert("", tk.END, values=book[1:])
    
    def show_reserve_book(self, sid):
        """Show book reservation screen"""
        self.clear_window()
        
        # Header
        header_frame = tb.Frame(self.root, bootstyle="info")
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        title_label = tb.Label(header_frame, text="📖 Reserve a Book", 
                             font=("Helvetica", 22, "bold"), bootstyle="inverse-info")
        title_label.pack(pady=15)
        
        # Available books table
        table_frame = tb.Frame(self.root, bootstyle="card")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create treeview for available books
        columns = ("ID", "Title", "Category", "Author", "Available")
        self.reserve_books_tree = tb.Treeview(table_frame, columns=columns, height=12, 
                                            bootstyle="info", show="headings")
        
        # Configure columns
        self.reserve_books_tree.column("ID", width=80, anchor=tk.CENTER)
        self.reserve_books_tree.column("Title", width=250, anchor=tk.W)
        self.reserve_books_tree.column("Category", width=150, anchor=tk.W)
        self.reserve_books_tree.column("Author", width=200, anchor=tk.W)
        self.reserve_books_tree.column("Available", width=100, anchor=tk.CENTER)
        
        # Configure headings
        self.reserve_books_tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.reserve_books_tree.heading("Title", text="Title", anchor=tk.W)
        self.reserve_books_tree.heading("Category", text="Category", anchor=tk.W)
        self.reserve_books_tree.heading("Author", text="Author", anchor=tk.W)
        self.reserve_books_tree.heading("Available", text="Available", anchor=tk.CENTER)
        
        # Add scrollbar
        scrollbar = tb.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.reserve_books_tree.yview, bootstyle="info-round")
        self.reserve_books_tree.configure(yscrollcommand=scrollbar.set)
        
        self.reserve_books_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=15)
        
        # bind selection to book id entry
        def choose_book(event):
            sel = self.reserve_books_tree.focus()
            if sel:
                vals = self.reserve_books_tree.item(sel,'values')
                self.reserve_book_id_entry.delete(0, tk.END)
                self.reserve_book_id_entry.insert(0, vals[0])
        self.reserve_books_tree.bind("<<TreeviewSelect>>", choose_book)
        
        # Load available books
        self.load_available_books()
        
        # Reservation form
        form_frame = tb.Frame(self.root, bootstyle="card")
        form_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        form_content = tb.Frame(form_frame)
        form_content.pack(fill=tk.X, padx=20, pady=15)
        
        tb.Label(form_content, text="Enter Book ID to Reserve:", 
                font=("Helvetica", 12), bootstyle="secondary").grid(row=0, column=0, padx=(0, 10), pady=5, sticky=tk.W)
        
        self.reserve_book_id_entry = tb.Entry(form_content, bootstyle="info", width=20)
        self.reserve_book_id_entry.grid(row=0, column=1, padx=(0, 15), pady=5)
        
        reserve_btn = tb.Button(form_content, text="📖 Reserve", 
                              command=lambda: self.reserve_book(sid), 
                              bootstyle="info", width=12)
        reserve_btn.grid(row=0, column=2, padx=(0, 10), pady=5)
        
        back_btn = tb.Button(form_content, text="⬅️ Back", 
                           command=lambda: self.show_student_books(sid), 
                           bootstyle="secondary-outline", width=12)
        back_btn.grid(row=0, column=3, padx=(0, 10), pady=5)
    
    def load_available_books(self):
        """Load all books and indicate availability for reservation"""
        # Clear existing items
        for item in self.reserve_books_tree.get_children():
            self.reserve_books_tree.delete(item)
        
        # Get all books and show availability
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        
        for book in books:
            status = "Available" if book[4] > 0 else "Issued"
            self.reserve_books_tree.insert("", tk.END, values=(book[0], book[1], book[2], book[3], status))
    
    def reserve_book(self, sid):
        """Reserve a book for student"""
        book_id = self.reserve_book_id_entry.get().strip()
        
        if not book_id:
            messagebox.showerror("Error", "Please enter a book ID!")
            return
        if not self.validate_numeric_input(book_id, "Book ID"):
            return
        
        try:
            book_id = int(book_id)
            
            # Check if book exists
            cursor.execute("SELECT * FROM books WHERE book_id=%s", (book_id,))
            book = cursor.fetchone()
            if not book:
                messagebox.showerror("Error", "Book ID not found in library records.")
                return
            
            # Inform user if book is currently available; they can issue directly or still reserve
            if book[4] > 0:
                response = messagebox.askyesno("Book Available",
                                               "This book is currently available for issue. Do you still want to place a reservation?")
                if not response:
                    return
            
            # Check if student already has this book issued
            cursor.execute("SELECT * FROM issued_books WHERE student_id=%s AND book_id=%s AND return_date IS NULL", 
                         (sid, book_id))
            if cursor.fetchone():
                messagebox.showerror("Error", "You already have this book issued!")
                return
            
            # Check if student already reserved this book
            cursor.execute("SELECT * FROM reservations WHERE student_id=%s AND book_id=%s AND status='pending'", 
                         (sid, book_id))
            if cursor.fetchone():
                messagebox.showerror("Error", "You already have a pending reservation for this book!")
                return
            
            # Create reservation
            cursor.execute("INSERT INTO reservations(student_id, book_id, reservation_date) VALUES(%s, %s, %s)",
                         (sid, book_id, date.today()))
            db.commit()
            
            messagebox.showinfo("Success", "Book reserved successfully! You will be notified when it's available.")
            self.reserve_book_id_entry.delete(0, tk.END)
            self.load_available_books()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid book ID!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def show_my_reservations(self, sid):
        """Show student's reservations"""
        self.clear_window()
        
        # Header
        header_frame = tb.Frame(self.root, bootstyle="warning")
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        title_label = tb.Label(header_frame, text="📋 My Reservations", 
                             font=("Helvetica", 22, "bold"), bootstyle="inverse-warning")
        title_label.pack(pady=15)
        
        # Reservations table
        table_frame = tb.Frame(self.root, bootstyle="card")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create treeview
        columns = ("Reservation ID", "Book ID", "Book Title", "Reservation Date", "Status")
        self.reservations_tree = tb.Treeview(table_frame, columns=columns, height=12, 
                                           bootstyle="warning", show="headings")
        
        # Configure columns
        self.reservations_tree.column("Reservation ID", width=120, anchor=tk.CENTER)
        self.reservations_tree.column("Book ID", width=100, anchor=tk.CENTER)
        self.reservations_tree.column("Book Title", width=250, anchor=tk.W)
        self.reservations_tree.column("Reservation Date", width=150, anchor=tk.CENTER)
        self.reservations_tree.column("Status", width=100, anchor=tk.CENTER)
        
        # Configure headings
        self.reservations_tree.heading("Reservation ID", text="Reservation ID", anchor=tk.CENTER)
        self.reservations_tree.heading("Book ID", text="Book ID", anchor=tk.CENTER)
        self.reservations_tree.heading("Book Title", text="Book Title", anchor=tk.W)
        self.reservations_tree.heading("Reservation Date", text="Reservation Date", anchor=tk.CENTER)
        self.reservations_tree.heading("Status", text="Status", anchor=tk.CENTER)
        
        # Add scrollbar
        scrollbar = tb.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.reservations_tree.yview, bootstyle="warning-round")
        self.reservations_tree.configure(yscrollcommand=scrollbar.set)
        
        self.reservations_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=15)
        
        # Load reservations
        self.load_student_reservations(sid)
        
        # Back button
        back_frame = tb.Frame(self.root)
        back_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        back_btn = tb.Button(back_frame, text="⬅️ Back", 
                           command=lambda: self.show_student_books(sid), 
                           bootstyle="secondary-outline", width=15)
        back_btn.pack(side=tk.LEFT)
    
    def load_student_reservations(self, sid):
        """Load student's reservations"""
        # Clear existing items
        for item in self.reservations_tree.get_children():
            self.reservations_tree.delete(item)
        
        cursor.execute("""
            SELECT r.reservation_id, r.book_id, b.title, r.reservation_date, r.status 
            FROM reservations r 
            JOIN books b ON r.book_id = b.book_id 
            WHERE r.student_id=%s 
            ORDER BY r.reservation_date DESC
        """, (sid,))
        reservations = cursor.fetchall()
        
        for reservation in reservations:
            res_id, book_id, title, rdate, status = reservation
            display = status
            if status == 'pending':
                cursor.execute("SELECT quantity FROM books WHERE book_id=%s", (book_id,))
                qty_row = cursor.fetchone()
                qty = qty_row[0] if qty_row else 0
                if qty > 0:
                    display = 'available'
            self.reservations_tree.insert("", tk.END, values=(res_id, book_id, title, rdate, display))
    
    # ==================== NOTIFICATION SYSTEM ====================
    def add_notification(self, notif_type, student_id, book_id=None, message=""):
        """Add a notification to the database"""
        try:
            cursor.execute("""
                INSERT INTO notifications (notif_type, student_id, book_id, message, status) 
                VALUES (%s, %s, %s, %s, 'pending')
            """, (notif_type, student_id, book_id, message))
            db.commit()
        except Exception as e:
            # Log error for debugging instead of silently failing
            print(f"Warning: Failed to add notification - {str(e)}")
    
    def show_notifications(self):
        """Admin notifications dashboard"""
        self.clear_content()
        
        # Section header
        header_frame = tb.Frame(self.content_frame, bootstyle="info")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        section_title = tb.Label(header_frame, text="🔔 Notifications & Requests", 
                               font=("Helvetica", 20, "bold"), bootstyle="inverse-info")
        section_title.pack(pady=15)
        
        # Tabs for different notification types
        tabs_frame = tb.Frame(self.content_frame)
        tabs_frame.pack(fill=tk.X, pady=(0, 20))
        
        tab_buttons = [
            ("All", "all", "primary"),
            ("Reservations", "reservation", "warning"),
            ("Password Resets", "password_reset", "danger"),
        ]
        
        for label, notif_type, style in tab_buttons:
            tb.Button(tabs_frame, text=label, 
                     command=lambda t=notif_type: self.filter_notifications(t), 
                     bootstyle=style, width=15).pack(side=tk.LEFT, padx=5)
        
        # Notifications table
        table_frame = tb.Frame(self.content_frame, bootstyle="card")
        table_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        columns = ("ID", "Type", "Student", "Book ID", "Message", "Status", "Date")
        self.notif_tree = tb.Treeview(table_frame, columns=columns, height=12, 
                                     bootstyle="info", show="headings")
        
        self.notif_tree.column("ID", width=50, anchor=tk.CENTER)
        self.notif_tree.column("Type", width=100, anchor=tk.CENTER)
        self.notif_tree.column("Student", width=100, anchor=tk.CENTER)
        self.notif_tree.column("Book ID", width=80, anchor=tk.CENTER)
        self.notif_tree.column("Message", width=250, anchor=tk.W)
        self.notif_tree.column("Status", width=100, anchor=tk.CENTER)
        self.notif_tree.column("Date", width=130, anchor=tk.CENTER)
        
        for col in columns:
            self.notif_tree.heading(col, text=col, anchor=tk.W)
        
        scrollbar = tb.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.notif_tree.yview, bootstyle="info-round")
        self.notif_tree.configure(yscrollcommand=scrollbar.set)
        
        self.notif_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=15)
        
        self.load_all_notifications()
        
        # Action buttons
        action_frame = tb.Frame(self.content_frame)
        action_frame.pack(fill=tk.X, pady=(0, 10))
        
        tb.Button(action_frame, text="✅ Approve", 
                 command=self.approve_notification, 
                 bootstyle="success", width=15).pack(side=tk.LEFT, padx=5)
        
        tb.Button(action_frame, text="❌ Delete", 
                 command=self.delete_notification, 
                 bootstyle="danger", width=15).pack(side=tk.LEFT, padx=5)
        
        tb.Button(action_frame, text="🔄 Refresh", 
                 command=lambda: self.load_all_notifications(), 
                 bootstyle="secondary", width=15).pack(side=tk.LEFT, padx=5)
    
    def load_all_notifications(self):
        """Load all notifications"""
        for item in self.notif_tree.get_children():
            self.notif_tree.delete(item)
        
        cursor.execute("""
            SELECT notif_id, notif_type, student_id, book_id, message, status, created_at 
            FROM notifications 
            ORDER BY created_at DESC
        """)
        notifs = cursor.fetchall()
        
        for notif in notifs:
            notif_id, ntype, sid, bid, msg, status, created = notif
            display_type = "Reservation" if ntype == "reservation" else "Password Reset" if ntype == "password_reset" else ntype
            self.notif_tree.insert("", tk.END, values=(notif_id, display_type, sid, bid or "-", msg, status, created))
    
    def filter_notifications(self, notif_type):
        """Filter notifications by type"""
        for item in self.notif_tree.get_children():
            self.notif_tree.delete(item)
        
        if notif_type == "all":
            cursor.execute("""
                SELECT notif_id, notif_type, student_id, book_id, message, status, created_at 
                FROM notifications 
                ORDER BY created_at DESC
            """)
        else:
            cursor.execute("""
                SELECT notif_id, notif_type, student_id, book_id, message, status, created_at 
                FROM notifications 
                WHERE notif_type=%s 
                ORDER BY created_at DESC
            """, (notif_type,))
        
        notifs = cursor.fetchall()
        
        for notif in notifs:
            notif_id, ntype, sid, bid, msg, status, created = notif
            display_type = "Reservation" if ntype == "reservation" else "Password Reset" if ntype == "password_reset" else ntype
            self.notif_tree.insert("", tk.END, values=(notif_id, display_type, sid, bid or "-", msg, status, created))
    
    def approve_notification(self):
        """Handle approval of a notification (updates reservation or password)"""
        selected = self.notif_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a notification!")
            return
        
        item = selected[0]
        values = self.notif_tree.item(item)["values"]
        notif_id = values[0]
        
        # Get notification details
        cursor.execute("""
            SELECT notif_type, student_id, book_id FROM notifications WHERE notif_id=%s
        """, (notif_id,))
        result = cursor.fetchone()
        
        if not result:
            messagebox.showerror("Error", "Notification not found!")
            return
        
        notif_type, student_id, book_id = result
        
        if notif_type == "reservation":
            # Mark reservation as approved
            cursor.execute("""
                UPDATE reservations SET status='approved' 
                WHERE book_id=%s AND student_id=%s AND status='pending'
            """, (book_id, student_id))
            db.commit()
            messagebox.showinfo("Success", f"Reservation for student {student_id} approved!")
        
        elif notif_type == "password_reset":
            # Show dialog for admin to set new password for student
            new_pass = tk.simpledialog.askstring("Reset Password", f"Enter new password for student {student_id}:")
            if new_pass:
                cursor.execute("""
                    UPDATE students SET password=%s WHERE student_id=%s
                """, (new_pass, student_id))
                db.commit()
                messagebox.showinfo("Success", f"Password reset for student {student_id}!")
        
        # Mark notification as handled
        cursor.execute("""
            UPDATE notifications SET status='handled' WHERE notif_id=%s
        """, (notif_id,))
        db.commit()
        
        self.load_all_notifications()
    
    def delete_notification(self):
        """Delete a notification"""
        selected = self.notif_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a notification!")
            return
        
        item = selected[0]
        values = self.notif_tree.item(item)["values"]
        notif_id = values[0]
        
        if messagebox.askyesno("Confirm", "Delete this notification?"):
            cursor.execute("DELETE FROM notifications WHERE notif_id=%s", (notif_id,))
            db.commit()
            messagebox.showinfo("Success", "Notification deleted!")
            self.load_all_notifications()

if __name__ == "__main__":
    root = tb.Window(themename="darkly")
    app = LibraryGUI(root)
    root.mainloop()
