# File Content Processor 🗂️

A simple, user-friendly GUI application for finding and replacing/deleting text in files. The application supports various text-based file formats and automatically creates backups before making any changes.
![image](https://github.com/user-attachments/assets/791257ef-e8fb-4f98-ab45-fb929be0c2b0)


## 🚀 Features

- Simple and intuitive graphical interface
- Support for multiple text-based file formats
- Case-sensitive text search
- Two operation modes: Replace or Delete
- Automatic backup creation
- Clear operation feedback
- File type validation

## 💻 System Requirements

### Minimum Requirements
- Operating System: Windows 7/8/10/11 (32-bit or 64-bit)
- RAM: 256MB (512MB+ recommended)
- Disk Space: 50MB
- Display: 800x600 resolution or higher

### For Developers (Source Code)
- Python 3.6 or higher
- Required Python packages:
  - tkinter (usually comes with Python)
  - pyinstaller (for building executable)

## 📥 Installation & Setup

### Option 1: Executable (Windows Users)
1. Download the latest release of `FileContentProcessor.exe`
2. No installation needed - just double-click to run
3. No additional dependencies required

### Option 2: From Source Code
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/file-content-processor.git
   cd file-content-processor
   ```

2. Install PyInstaller (if you want to build the executable):
   ```bash
   pip install pyinstaller
   ```

3. Build the executable:
   ```bash
   pyinstaller --onefile --windowed --name FileContentProcessor file_processor.py
   ```
   Or use the provided build script:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

4. Run directly with Python:
   ```bash
   python file_processor.py
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
3. Enter the text you want to find (Case Sensitive)
4. Choose your operation:
   - **Replace with text**: Replaces found text with new text
   - **Delete lines**: Removes entire lines containing the found text
5. If replacing, enter your replacement text
6. Click "Process File" to execute the operation

## 💾 Backup System

- Automatic backup creation before any modifications
- Backup files are created in the same directory as the source file
- Backup filename format: `originalname.extension.backup`
- Always keeps the latest backup
- Restoring from backup:
  1. Delete or rename the modified file
  2. Remove the `.backup` extension from the backup file

## ⚠️ Important Notes

1. **Case Sensitivity**: All text searches are case-sensitive
2. **File Access**:
   - Files must not be locked by other programs
   - User must have read/write permissions
   - Sufficient disk space needed for backup creation
3. **Text Encoding**: Files should use UTF-8 encoding
4. **Large Files**: Processing speed depends on file size and system capabilities

## 🔒 Safety Features

- Automatic backup creation
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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

