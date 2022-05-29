import os

class View:
    """
    view contains two attributes title and content and a show class method to display them.
    """
    def __init__(self, title: str, content: str):
        """constructor
        Args:
            title (str): capitalized view title
            content (str): view content: it is a str which allows to present the data
        """
        self.title = title.upper()
        self.content = content

    def show(self):
        """
        - display of title and content separated by a line
        - console cls after each display
        """
        os.system("cls")
        print(self.title)
        print("-" * len(self.title))
        print(self.content)
    