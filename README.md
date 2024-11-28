# File Content Processor 🗂️

A user-friendly GUI application for finding and manipulating text in files. Features a modern interface with dark/light theme support, regular expression capabilities, and automatic backup creation before any modifications.
![image](https://github.com/user-attachments/assets/fc4b683c-c918-4145-9e91-6beca4faf1ef)


## 🚀 Features

- Modern graphical interface with dark/light theme support
- Support for multiple text-based file formats
- Regular expression search support
- Case-sensitive/insensitive text search
- Three operation modes:
  - Replace matched text
  - Replace entire line
  - Delete matching lines
- Automatic backup creation
- Clear operation feedback
- File type validation

## 💻 System Requirements

### For Developers (Source Code)
- Python 3.6 or higher
- Required Python packages:
  - tkinter (usually comes with Python)
  - sv-ttk (for theme support)
  - pyinstaller (for building executable)

## 📥 Installation & Setup

### From Source Code
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/file-content-processor.git
   cd file-content-processor
   ```

2. Install required packages:
   ```bash
   pip install sv-ttk pyinstaller
   ```

3. Build the executable:
   ```bash
   pyinstaller --onefile --windowed --name FileContentProcessor file_replacer.py
   ```
   Or use the provided build script:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

## 📝 Supported File Types

- Text Files (.txt)
- Log Files (.log)
- Web Files (.html, .htm, .css, .js)
- Data Files (.csv, .json, .xml, .yaml, .yml)
- Programming Files (.py, .cpp, .h, .cs, .java)
- Configuration Files (.cfg, .ini)
- Script Files (.bat, .ps1, .sh)
- Documentation Files (.md)
- Database Files (.sql)
- Other text-based files

## 🎯 How to Use

1. Launch the application
2. Click "Select File" to choose your file
3. Configure search options:
   - Enter the text to find
   - Toggle "Use Regular Expression" if needed
   - Toggle "Case Sensitive" as required
4. Choose your operation:
   - **Replace matched text**: Replaces only the matched text
   - **Replace entire line**: Replaces the whole line containing the match
   - **Delete line**: Removes lines containing the matched text
5. If replacing, enter your replacement text
6. Click "Process File" to execute the operation
7. Use "Toggle Dark mode" button to switch between light and dark themes

## 💾 Backup System

- Automatic backup creation before any modifications
- Backup files are created in the same directory as the source file
- Backup filename format: `originalname.extension.backup`
- Always keeps the latest backup
- Easy reversion using the "Revert Last Change" button

## ⚠️ Important Notes

1. **Search Options**:
   - Regular expression support for advanced pattern matching
   - Optional case-sensitivity
2. **File Access**:
   - Files must not be locked by other programs
   - User must have read/write permissions
   - Sufficient disk space needed for backup creation
3. **Text Encoding**: Files should use UTF-8 encoding
4. **Large Files**: Processing speed depends on file size and system capabilities

## 🔒 Safety Features

- Automatic backup creation
- One-click revert functionality
- File type validation
- Error handling with user-friendly messages
- Read/write permission checking
- Binary file detection

## 🐛 Troubleshooting

1. **"File appears to be binary or corrupted"**
   - Ensure the file is a text-based file
   - Check file encoding

2. **"No permission to access file"**
   - Check file permissions
   - Run as administrator if necessary

3. **"File is locked"**
   - Close any programs using the file
   - Check if file is marked as read-only

4. **"Invalid regular expression"**
   - Check your regex pattern syntax
   - Disable regex mode for literal string matching

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
