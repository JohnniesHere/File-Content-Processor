import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from core.file_processor import FileProcessor
from core.backup import create_backup
from ui.theme import ThemeManager


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("File Content Processor")
        self.root.geometry("800x750")

        # Initialize theme manager
        self.theme_manager = ThemeManager(root)
        self.theme_manager.apply_theme("dark")

        # Variables
        self.selected_file = None
        self.backup_file = None

        # Initialize main layout
        self.create_layout()

    def create_layout(self):
        """Creates the main layout."""
        self.main_container = ttk.Frame(self.root, padding="20")
        self.main_container.pack(fill="both", expand=True)

        self.create_header()
        self.create_file_selection()
        self.create_search_options()
        self.create_operation_section()
        self.create_process_section()

    def create_header(self):
        """Creates the header section."""
        header_frame = ttk.Frame(self.main_container)
        header_frame.pack(fill="x", pady=(0, 20))

        ttk.Label(
            header_frame, text="File Content Processor", font=("Arial", 16, "bold")
        ).pack(side="left", padx=10, pady=10)

        ttk.Button(
            header_frame,
            text="Toggle Dark mode",
            command=self.theme_manager.toggle_theme,
        ).pack(side="right", padx=10, pady=10)

    def create_file_selection(self):
        """Creates the file selection section."""
        frame = ttk.Frame(self.main_container)
        frame.pack(fill="x", pady=(0, 20))

        ttk.Button(
            frame, text="Select File", command=self.select_file
        ).pack(side="left", padx=10)

        ttk.Button(
            frame, text="Supported Types", command=self.show_supported_types
        ).pack(side="left", padx=10)

        self.file_label = ttk.Label(frame, text="No file selected")
        self.file_label.pack(side="left", padx=10)

    def create_search_options(self):
        """Creates the search options section."""
        frame = ttk.Frame(self.main_container)
        frame.pack(fill="x", pady=(0, 20))

        ttk.Label(frame, text="Search Options").pack(anchor="w", padx=10, pady=5)

        self.use_regex = tk.BooleanVar(value=False)
        self.case_sensitive = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            frame, text="Use Regular Expression", variable=self.use_regex
        ).pack(anchor="w", padx=10, pady=5)

        ttk.Checkbutton(
            frame, text="Case Sensitive", variable=self.case_sensitive
        ).pack(anchor="w", padx=10, pady=5)

        ttk.Label(frame, text="Text to Find:").pack(anchor="w", padx=10, pady=5)
        self.search_entry = ttk.Entry(frame)
        self.search_entry.pack(fill="x", padx=10, pady=5)
        self.search_entry.insert(0, "Enter text or regex pattern")

    def create_operation_section(self):
        """Creates the operation section."""
        frame = ttk.Frame(self.main_container)
        frame.pack(fill="x", pady=(0, 20))

        ttk.Label(frame, text="Operation").pack(anchor="w", padx=10, pady=5)

        self.operation_var = tk.StringVar(value="replace_string")
        options = [
            ("Replace matched text", "replace_string"),
            ("Replace entire line", "replace_line"),
            ("Delete line", "delete"),
        ]

        for text, value in options:
            ttk.Radiobutton(
                frame, text=text, variable=self.operation_var, value=value, command=self.toggle_replacement_entry
            ).pack(anchor="w", padx=10, pady=5)

        self.replacement_label = ttk.Label(frame, text="Replacement Text:")
        self.replacement_label.pack(anchor="w", padx=10, pady=5)

        self.replacement_entry = ttk.Entry(frame)
        self.replacement_entry.pack(fill="x", padx=10, pady=5)
        self.replacement_entry.insert(0, "Replacement text here")

    def toggle_replacement_entry(self):
        """Toggles the replacement text entry based on the operation selected."""
        if self.operation_var.get() == "delete":
            self.replacement_label.pack_forget()
            self.replacement_entry.pack_forget()
        else:
            self.replacement_label.pack(anchor="w", padx=10, pady=5)
            self.replacement_entry.pack(fill="x", padx=10, pady=5)

    def create_process_section(self):
        """Creates the process section."""
        frame = ttk.Frame(self.main_container)
        frame.pack(fill="x", pady=(0, 20))

        ttk.Button(frame, text="Process File", command=self.process_file).pack(
            fill="x", padx=10, pady=5
        )

        self.revert_button = ttk.Button(
            frame,
            text="Revert Last Change",
            command=self.revert_last_change,
            state="disabled",
        )
        self.revert_button.pack(fill="x", padx=10, pady=5)

    def select_file(self):
        """Handles file selection."""
        file_path = filedialog.askopenfilename(
            title="Select a File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.selected_file = file_path
            self.file_label.config(text=f"Selected file: {file_path}")

            # Check for backup file
            self.backup_file = f"{file_path}.backup"
            if os.path.exists(self.backup_file):
                self.revert_button.config(state="normal")
            else:
                self.revert_button.config(state="disabled")

    def show_supported_types(self):
        """Displays supported file types."""
        supported_types = """Supported File Types:

- Text Files (.txt)
- Log Files (.log)
- Web Files (.html, .css, .js)
- Data Files (.csv, .json, .xml, .yaml)
- Code Files (.py, .cpp, .java, .sh)
- Configuration Files (.cfg, .ini)
- Script Files (.bat, .ps1)
- Documentation Files (.md)
"""
        messagebox.showinfo("Supported Types", supported_types)

    def process_file(self):
        """Processes the selected file."""
        if not self.selected_file:
            messagebox.showerror("Error", "No file selected!")
            return

        search_text = self.search_entry.get()
        replacement_text = self.replacement_entry.get()
        operation = self.operation_var.get()
        use_regex = self.use_regex.get()
        case_sensitive = self.case_sensitive.get()

        try:
            create_backup(self.selected_file)
            changes = FileProcessor.process_file(
                self.selected_file,
                search_text,
                replacement_text,
                use_regex,
                case_sensitive,
                operation,
            )
            messagebox.showinfo("Success", f"File processed successfully!\nChanges: {changes}")
            self.revert_button.config(state="normal")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def revert_last_change(self):
        """Reverts the last change by restoring from the backup file."""
        if not self.backup_file or not os.path.exists(self.backup_file):
            messagebox.showerror("Error", "No backup file found!")
            return

        confirm = messagebox.askyesno(
            "Confirm Revert",
            "Are you sure you want to revert to the last backup? This cannot be undone.",
        )
        if confirm:
            try:
                os.replace(self.backup_file, self.selected_file)
                messagebox.showinfo("Success", "Reverted to the last backup successfully.")
                self.revert_button.config(state="disabled")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
