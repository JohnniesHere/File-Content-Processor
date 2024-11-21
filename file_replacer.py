import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from datetime import datetime
import shutil
import re

class FileProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Content Processor")
        self.root.geometry("600x750")
        self.root.configure(bg='#f0f0f0')
        
        # Define supported file types
        self.supported_extensions = {
            'Text Files': ['.txt'],
            'Log Files': ['.log'],
            'Web Files': ['.html', '.htm', '.css', '.js'],
            'Data Files': ['.csv', '.json', '.xml', '.yaml', '.yml'],
            'Programming Files': ['.py', '.cpp', '.h', '.cs', '.java'],
            'Configuration Files': ['.cfg', '.ini'],
            'Script Files': ['.bat', '.ps1', '.sh'],
            'Documentation': ['.md'],
            'Database Files': ['.sql'],
            'Other Text Files': ['No extension files']
        }
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg='#f0f0f0')
        self.main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            self.main_frame,
            text="File Content Processor",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0'
        )
        title_label.pack(pady=(0, 20))
        
        # File selection buttons frame
        button_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        button_frame.pack(fill='x', pady=(0, 10))
        
        # File selection button
        self.select_button = tk.Button(
            button_frame,
            text="Select File",
            command=self.select_file,
            width=20,
            bg='#4a90e2',
            fg='white',
            font=("Arial", 10),
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.select_button.pack(side=tk.LEFT, padx=5)
        
        # Info button
        self.info_button = tk.Button(
            button_frame,
            text="Supported File Types",
            command=self.show_supported_types,
            width=20,
            bg='#4a90e2',
            fg='white',
            font=("Arial", 8),
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.info_button.pack(side=tk.LEFT, padx=5)
        
        # Selected file label
        self.file_label = tk.Label(
            self.main_frame,
            text="No file selected",
            bg='#f0f0f0',
            wraplength=500
        )
        self.file_label.pack(pady=(0, 20))
        
        # Search options frame
        search_frame = tk.LabelFrame(
            self.main_frame,
            text="Search Options",
            bg='#f0f0f0',
            padx=10,
            pady=5
        )
        search_frame.pack(fill='x', pady=(0, 10))

        # Regular expression option
        self.use_regex = tk.BooleanVar(value=False)
        self.regex_check = tk.Checkbutton(
            search_frame,
            text="Use Regular Expression",
            variable=self.use_regex,
            bg='#f0f0f0'
        )
        self.regex_check.pack(anchor='w')
        
        # Case sensitive option
        self.case_sensitive = tk.BooleanVar(value=True)
        self.case_check = tk.Checkbutton(
            search_frame,
            text="Case Sensitive",
            variable=self.case_sensitive,
            bg='#f0f0f0'
        )
        self.case_check.pack(anchor='w')
        
        # Text to find entry
        tk.Label(
            self.main_frame,
            text="Text to Find:",
            bg='#f0f0f0',
            font=("Arial", 10)
        ).pack()
        
        self.text_to_find = tk.Entry(
            self.main_frame,
            width=50
        )
        self.text_to_find.insert(0, 'Enter text or regex pattern')
        self.text_to_find.pack(pady=(0, 20))
        
        # Operation selection frame
        self.operation_frame = tk.LabelFrame(
            self.main_frame,
            text="Operation",
            bg='#f0f0f0',
            padx=10,
            pady=5
        )
        self.operation_frame.pack(fill='x', pady=(0, 10))
        
        # Operation selection
        self.operation_var = tk.StringVar(value="replace_string")
        
        self.replace_string_radio = tk.Radiobutton(
            self.operation_frame,
            text="Replace matched text",
            variable=self.operation_var,
            value="replace_string",
            command=self.toggle_replacement_entry,
            bg='#f0f0f0'
        )
        self.replace_string_radio.pack(anchor='w')
        
        self.replace_line_radio = tk.Radiobutton(
            self.operation_frame,
            text="Replace entire line",
            variable=self.operation_var,
            value="replace_line",
            command=self.toggle_replacement_entry,
            bg='#f0f0f0'
        )
        self.replace_line_radio.pack(anchor='w')
        
        self.delete_radio = tk.Radiobutton(
            self.operation_frame,
            text="Delete line",
            variable=self.operation_var,
            value="delete",
            command=self.toggle_replacement_entry,
            bg='#f0f0f0'
        )
        self.delete_radio.pack(anchor='w')
        
        # Help text for regex
        self.help_label = tk.Label(
            self.main_frame,
            text="Regular Expression Help:\n"
                 "• .* = any characters\n"
                 "• \\d = any digit\n"
                 "• \\w = any word character\n"
                 "• [abc] = any character in brackets\n"
                 "• ^ = start of line\n"
                 "• $ = end of line",
            bg='#f0f0f0',
            justify=tk.LEFT,
            font=("Arial", 8)
        )
        self.help_label.pack(pady=(0, 10))
        
        # Replacement text entry
        self.replacement_frame = tk.Frame(
            self.main_frame,
            bg='#f0f0f0'
        )
        self.replacement_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(
            self.replacement_frame,
            text="Replacement Text:",
            bg='#f0f0f0',
            font=("Arial", 10)
        ).pack()
        
        self.replacement_text = tk.Entry(
            self.replacement_frame,
            width=50
        )
        self.replacement_text.insert(0, "Replacement text here")
        self.replacement_text.pack()
        
        # Process button
        self.process_button = tk.Button(
            self.main_frame,
            text="Process File",
            command=self.process_file,
            width=20,
            bg='#2ecc71',
            fg='white',
            font=("Arial", 10),
            relief=tk.RAISED,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.process_button.pack(pady=(0, 20))
        
        # Status label
        self.status_label = tk.Label(
            self.main_frame,
            text="",
            bg='#f0f0f0',
            wraplength=500
        )
        self.status_label.pack(pady=(0, 20))
        
        self.selected_file = None

    def is_text_file(self, filepath):
        """Simple check if file is text file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                file.read(4096)
            return True, None
        except Exception as e:
            return False, str(e)

    def is_supported_extension(self, filepath):
        """Check if file extension is in supported list"""
        ext = os.path.splitext(filepath)[1].lower()
        return any(ext in exts for exts in self.supported_extensions.values())

    def toggle_replacement_entry(self):
        """Show/hide replacement text entry based on operation"""
        if self.operation_var.get() == "delete":
            self.replacement_frame.pack_forget()
        else:
            self.replacement_frame.pack(fill='x', pady=(0, 20))

    def select_file(self):
        """Handle file selection"""
        filetypes = [("All Supported Files", "*.*")]
        for category, extensions in self.supported_extensions.items():
            if extensions != ['No extension files']:  # Skip the "no extension" category
                ext_string = " ".join(f"*{ext}" for ext in extensions)
                filetypes.append((category, ext_string))

        file_path = filedialog.askopenfilename(
            title="Select File",
            filetypes=filetypes
        )
        
        if file_path:
            # Check if file type is supported
            is_text, error = self.is_text_file(file_path)
            
            if not is_text:
                messagebox.showerror(
                    "Unsupported File Type",
                    "This file appears to be binary or corrupted.\n"
                    "Only text-based files are supported."
                )
                return
            
            self.selected_file = file_path
            self.file_label.config(text=f"Selected file: {file_path}")
            self.process_button.config(state=tk.NORMAL)
            self.status_label.config(text="")

    def show_supported_types(self):
        """Show dialog with supported file types"""
        info_text = "Supported File Types:\n\n"
        for category, extensions in self.supported_extensions.items():
            if extensions:
                ext_list = ", ".join(extensions)
                info_text += f"{category}:\n{ext_list}\n\n"
        
        info_text += "\nNotes:\n"
        info_text += "- Files must be text-based\n"
        info_text += "- Files must not be locked by other programs\n"
        info_text += "- Files must have read/write permissions\n"
        info_text += "- Files should use standard text encoding (UTF-8)"
        
        messagebox.showinfo("Supported File Types", info_text)

    def process_file(self):
        """Process the selected file"""
        if not self.selected_file:
            messagebox.showerror("Error", "No file selected!")
            return
        
        try:
            # Create backup
            backup_path = f"{self.selected_file}.backup"
            shutil.copy2(self.selected_file, backup_path)
            
            # Read file content
            with open(self.selected_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Get search parameters
            search_text = self.text_to_find.get()
            operation = self.operation_var.get()
            replacement = self.replacement_text.get()
            use_regex = self.use_regex.get()
            case_sensitive = self.case_sensitive.get()
            
            changes = 0
            modified_content = ""
            
            if use_regex:
                try:
                    flags = 0 if case_sensitive else re.IGNORECASE
                    pattern = re.compile(search_text, flags)
                except re.error as e:
                    messagebox.showerror("Regex Error", f"Invalid regular expression: {str(e)}")
                    return
            
            # Process the content based on operation
            if operation == "delete":
                # Split into lines, filter out matching lines
                lines = content.splitlines()
                if use_regex:
                    modified_lines = [line for line in lines if not pattern.search(line)]
                else:
                    modified_lines = [line for line in lines if not (search_text in line if case_sensitive 
                                    else search_text.lower() in line.lower())]
                changes = len(lines) - len(modified_lines)
                modified_content = '\n'.join(modified_lines)
                if lines and not lines[-1].endswith('\n'):
                    modified_content += '\n'
                
            elif operation == "replace_line":
                lines = content.splitlines()
                modified_lines = []
                for line in lines:
                    if use_regex:
                        if pattern.search(line):
                            modified_lines.append(replacement)
                            changes += 1
                        else:
                            modified_lines.append(line)
                    else:
                        if (search_text in line if case_sensitive 
                            else search_text.lower() in line.lower()):
                            modified_lines.append(replacement)
                            changes += 1
                        else:
                            modified_lines.append(line)
                modified_content = '\n'.join(modified_lines)
                if lines and not lines[-1].endswith('\n'):
                    modified_content += '\n'
                
            else:  # replace_string
                if use_regex:
                    modified_content, count = pattern.subn(replacement, content)
                    changes = count
                else:
                    if case_sensitive:
                        modified_content = content.replace(search_text, replacement)
                        changes = content.count(search_text)
                    else:
                        pattern = re.compile(re.escape(search_text), re.IGNORECASE)
                        modified_content, changes = pattern.subn(replacement, content)
            
            # Write modified content
            with open(self.selected_file, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            
            # Update status
            action_text = "deleted" if operation == "delete" else "replaced"
            self.status_label.config(
                text=f"Process completed successfully!\n"
                     f"Occurrences {action_text}: {changes}\n"
                     f"Backup created at: {backup_path}"
            )
            
            messagebox.showinfo("Success", 
                              f"File processed successfully!\n{changes} occurrences {action_text}.")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
            self.status_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileProcessorApp(root)
    root.mainloop()