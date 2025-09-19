import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        

def main():
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    