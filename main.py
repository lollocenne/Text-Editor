from PyQt5.QtWidgets import QMainWindow, QTextEdit, QToolBar, QPushButton, QSpinBox, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont, QTextCharFormat, QColor
from PyQt5.QtCore import Qt


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
        self.currentColor = QColor(0, 0, 0)
        
        # Create the toolbar
        self.createToolbar()
    
    def createToolbar(self):
        # Create a toolbar
        toolbar = QToolBar("Tools", self)
        self.addToolBar(toolbar)
        
        # Create a widget to center the items
        toolbarWidget = QWidget()
        toolbarLayout = QHBoxLayout()
        
        # Add stretch on the left to push elements to the center
        toolbarLayout.addStretch()
        
        SPACE_ELEMETS: int = 50
        
        # Set the current formatting for the new text
        def applyCurrentFormatting():
            charFormat = QTextCharFormat()
            charFormat.setFontWeight(QFont.Bold if self.currentBold else QFont.Normal)
            charFormat.setFontPointSize(self.currentFontSize)
            charFormat.setForeground(self.currentColor)
            self.textContainer.setCurrentCharFormat(charFormat)
        
        def toggleBold():
            self.currentBold = not self.currentBold
            boldButton.setStyleSheet(
                "background-color: lightgray;" if self.currentBold else ""
            )
            applyCurrentFormatting()
        
        def changeSize(size: int):
            self.currentFontSize = size
            applyCurrentFormatting()
        
        def changeColor():
            r = self.redSpinbox.value()
            g = self.greenSpinbox.value()
            b = self.blueSpinbox.value()
            self.currentColor = QColor(r, g, b)
            applyCurrentFormatting()
        
        # Bold button
        boldButton = QPushButton("Bold", self)
        boldButton.setCheckable(True)
        boldButton.clicked.connect(toggleBold)
        toolbarLayout.addWidget(boldButton)
        
        # Spacer between Bold and Size controls
        toolbarLayout.addSpacerItem(QSpacerItem(SPACE_ELEMETS, 0, QSizePolicy.Fixed, QSizePolicy.Minimum))
        
        # Font size spinbox
        sizeLabel = QLabel("Size:")
        toolbarLayout.addWidget(sizeLabel)
        
        self.fontSizeSpinbox = QSpinBox(self)
        self.fontSizeSpinbox.setRange(1, 99)
        self.fontSizeSpinbox.setValue(self.currentFontSize)
        self.fontSizeSpinbox.valueChanged.connect(changeSize)
        toolbarLayout.addWidget(self.fontSizeSpinbox)
        
        # Spacer between Size and Color controls
        toolbarLayout.addSpacerItem(QSpacerItem(SPACE_ELEMETS, 0, QSizePolicy.Fixed, QSizePolicy.Minimum))
        
        # Add RGB color controls
        colorLabel = QLabel("Color:")
        toolbarLayout.addWidget(colorLabel)
        
        # Red
        self.redSpinbox = QSpinBox(self)
        self.redSpinbox.setRange(0, 255)
        self.redSpinbox.setPrefix("R: ")
        self.redSpinbox.valueChanged.connect(changeColor)
        toolbarLayout.addWidget(self.redSpinbox)
        
        # Green
        self.greenSpinbox = QSpinBox(self)
        self.greenSpinbox.setRange(0, 255)
        self.greenSpinbox.setPrefix("G: ")
        self.greenSpinbox.valueChanged.connect(changeColor)
        toolbarLayout.addWidget(self.greenSpinbox)
        
        # Blue
        self.blueSpinbox = QSpinBox(self)
        self.blueSpinbox.setRange(0, 255)
        self.blueSpinbox.setPrefix("B: ")
        self.blueSpinbox.valueChanged.connect(changeColor)
        toolbarLayout.addWidget(self.blueSpinbox)
        
        # Add stretch on the right to keep elements centered
        toolbarLayout.addStretch()
        
        # Set the layout on the widget and add it to the toolbar
        toolbarWidget.setLayout(toolbarLayout)
        toolbar.addWidget(toolbarWidget)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec_())
