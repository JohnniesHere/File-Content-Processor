import shutil


def create_backup(file_path):
    backup_path = f"{file_path}.backup"
    shutil.copy2(file_path, backup_path)
    return backup_path
