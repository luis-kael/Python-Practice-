import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
        
    def initUI(self):
        pass    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec_())
    