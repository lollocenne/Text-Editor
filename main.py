from PyQt5.QtWidgets import QMainWindow, QTextEdit, QToolBar, QAction, QSpinBox, QLabel
from PyQt5.QtGui import QFont, QTextCharFormat

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create the window
        self.setWindowTitle("Text Editor")
        self.setGeometry(500, 200, 700, 600)
        self.showMaximized()
        
        # Create the text editing area
        self.textContainer = QTextEdit(self)
        self.setCentralWidget(self.textContainer)
        
        # Font
        font = self.textContainer.font()
        font.setPointSize(14)
        self.textContainer.setFont(font)
        
        # Current formatting
        self.currentBold: bool = False
        self.currentFontSize: int = 14
        
        # Create the toolbar
        self.createToolbar()
    
    def createToolbar(self):
        # Create a toolbar
        toolbar = QToolBar("Tools", self)
        self.addToolBar(toolbar)
        
        # Set the current formatting for the new text
        def applyCurrentFormatting():
            charFormat = QTextCharFormat()
            charFormat.setFontWeight(QFont.Bold if self.currentBold else QFont.Normal)
            charFormat.setFontPointSize(self.currentFontSize)
            self.textContainer.setCurrentCharFormat(charFormat)
        
        def toggleBold(checked):
            self.currentBold = checked
            applyCurrentFormatting()
        
        def changeSize(size):
            self.currentFontSize = size
            applyCurrentFormatting()
        
        # Bold button
        boldAction = QAction("Bold", self)
        boldAction.setCheckable(True)
        boldAction.triggered.connect(toggleBold)
        toolbar.addAction(boldAction)
        
        # Font size button
        toolbar.addWidget(QLabel("Size"))
        self.fontSizeSpinbox = QSpinBox(self)
        self.fontSizeSpinbox.setRange(1, 99)
        self.fontSizeSpinbox.setValue(self.currentFontSize)
        self.fontSizeSpinbox.valueChanged.connect(changeSize)
        toolbar.addWidget(self.fontSizeSpinbox)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
