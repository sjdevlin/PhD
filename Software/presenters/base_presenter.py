class BasePresenter:
    def __init__(self, view):
        self.view = view

    def show_error(self, message):
        """Common error handling method."""
        self.view.display_error(message)

    def set_active_button(self, button):
        """Highlight the currently active button by changing its color."""
        self.reset_sidebar_button_colors()
        button.config(bg="black", fg="white")

    def reset_sidebar_button_colors(self):
        """Reset all sidebar buttons to their default colors."""
        for button in self.view.sidebar_buttons:
            button.config(bg="gray", fg="black")