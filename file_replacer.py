import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from datetime import datetime
import shutil

class FileProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Content Processor")
        self.root.geometry("600x550")
        self.root.configure(bg='#f0f0f0')
        
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
        
        # File selection button
        self.select_button = tk.Button(
            self.main_frame,
            text="Select File",
            command=self.select_file,
            width=20,
            bg='#4a90e2',
            fg='white',
            font=("Arial", 10),
            relief=tk.RAISED,
            cursor="hand2"
        )
        self.select_button.pack(pady=(0, 10))
        
        # Selected file label
        self.file_label = tk.Label(
            self.main_frame,
            text="No file selected",
            bg='#f0f0f0',
            wraplength=500
        )
        self.file_label.pack(pady=(0, 20))
        
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
        self.text_to_find.insert(0, 'DefaultValue="0"')
        self.text_to_find.pack(pady=(0, 20))
        
        # Operation selection frame
        self.operation_frame = tk.LabelFrame(
            self.main_frame,
            text="Operation",
            bg='#f0f0f0',
            padx=10,
            pady=10
        )
        self.operation_frame.pack(pady=(0, 20), fill='x')
        
        # Operation selection
        self.operation_var = tk.StringVar(value="replace")
        
        self.replace_radio = tk.Radiobutton(
            self.operation_frame,
            text="Replace with text",
            variable=self.operation_var,
            value="replace",
            command=self.toggle_replacement_entry,
            bg='#f0f0f0'
        )
        self.replace_radio.pack(anchor='w')
        
        self.delete_radio = tk.Radiobutton(
            self.operation_frame,
            text="Delete line",
            variable=self.operation_var,
            value="delete",
            command=self.toggle_replacement_entry,
            bg='#f0f0f0'
        )
        self.delete_radio.pack(anchor='w')
        
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
        self.replacement_text.insert(0, "replace text here")
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

    def toggle_replacement_entry(self):
        if self.operation_var.get() == "delete":
            self.replacement_frame.pack_forget()
        else:
            self.replacement_frame.pack(fill='x', pady=(0, 20))

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.selected_file = file_path
            self.file_label.config(text=f"Selected file: {file_path}")
            self.process_button.config(state=tk.NORMAL)
            self.status_label.config(text="")

    def process_file(self):
        if not self.selected_file:
            messagebox.showerror("Error", "No file selected!")
            return
        
        try:
            # Create backup
            backup_path = f"{self.selected_file}.backup"
            shutil.copy2(self.selected_file, backup_path)
            
            # Read file content
            with open(self.selected_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # Process lines
            text_to_find = self.text_to_find.get()
            operation = self.operation_var.get()
            modified_lines = []
            changes = 0
            
            for line in lines:
                if text_to_find in line:
                    if operation == "replace":
                        modified_lines.append(f"{self.replacement_text.get()}\n")
                    # If operation is delete, we skip adding the line
                    changes += 1
                else:
                    modified_lines.append(line)
            
            # Write modified content
            with open(self.selected_file, 'w', encoding='utf-8') as file:
                file.writelines(modified_lines)
            
            # Update status
            action_text = "deleted" if operation == "delete" else "replaced"
            self.status_label.config(
                text=f"Process completed successfully!\n"
                     f"Lines {action_text}: {changes}\n"
                     f"Backup created at: {backup_path}"
            )
            
            messagebox.showinfo("Success", "File processed successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
            self.status_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileProcessorApp(root)
    root.mainloop()