import re


class FileProcessor:
    @staticmethod
    def process_file(file_path, search_text, replacement_text, use_regex, case_sensitive, operation):
        """Processes the file based on the specified operation."""
        # Handle empty search text
        if not search_text.strip():
            raise ValueError("Search text cannot be empty.")

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        if operation == "delete":
            lines = content.splitlines()
            modified_lines = [
                line for line in lines if not FileProcessor._matches(line, search_text, use_regex, case_sensitive)
            ]
            changes = len(lines) - len(modified_lines)
            modified_content = "\n".join(modified_lines)
        elif operation == "replace_line":
            lines = content.splitlines()
            modified_lines = []
            changes = 0
            for line in lines:
                if FileProcessor._matches(line, search_text, use_regex, case_sensitive):
                    modified_lines.append(replacement_text)
                    changes += 1
                else:
                    modified_lines.append(line)
            modified_content = "\n".join(modified_lines)
        else:  # replace_string
            if use_regex:
                flags = 0 if case_sensitive else re.IGNORECASE
                pattern = re.compile(search_text, flags)
                modified_content, changes = pattern.subn(replacement_text, content)
            else:
                if case_sensitive:
                    modified_content = content.replace(search_text, replacement_text)
                    changes = content.count(search_text)
                else:
                    # Perform a case-insensitive replacement
                    pattern = re.compile(re.escape(search_text), re.IGNORECASE)
                    modified_content, changes = pattern.subn(replacement_text, content)

        # Write the modified content back
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(modified_content)

        return changes

    @staticmethod
    def _matches(line, search_text, use_regex, case_sensitive):
        """Determines if a line matches the search text."""
        if use_regex:
            flags = 0 if case_sensitive else re.IGNORECASE
            return bool(re.search(search_text, line, flags))
        else:
            if case_sensitive:
                return search_text in line
            else:
                return search_text.lower() in line.lower()
