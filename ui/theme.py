import sv_ttk


class ThemeManager:
    def __init__(self, root):
        self.root = root
        self.is_dark_mode = True

    def apply_theme(self, theme: str):
        """Applies the selected theme."""
        sv_ttk.set_theme(theme)
        self.is_dark_mode = theme == "dark"

    def toggle_theme(self):
        """Toggles between dark and light themes."""
        self.is_dark_mode = not self.is_dark_mode
        theme = "dark" if self.is_dark_mode else "light"
        self.apply_theme(theme)
