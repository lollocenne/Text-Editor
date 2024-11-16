import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create the window
        self.setWindowTitle("Text Editor")
        self.setGeometry(500, 200, 700, 600)
        self.showMaximized()
        
        # Create the part where the text will be
        self.textContainer = QTextEdit(self)
        self.setCentralWidget(self.textContainer)
        
        # Font
        font = self.textContainer.font()
        font.setPointSize(14)
        self.textContainer.setFont(font)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
