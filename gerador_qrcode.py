import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont
from gerador import GeradorQrcode
from PyQt5.QtCore import QSize


# Step 1: Create main Window
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1020, 780)
        self.setWindowTitle("My Window")
        self.setStyleSheet('background-color: gray')
        self.add_content()

        # self.dadosLabel = QLabel(self)
        # self.dadosLabel.setText("Dados")
        self.line = QLineEdit(self)

        self.line.move(350, 600)
        self.line.resize(350, 32)
        self.line.setStyleSheet('background: white')
        # self.dadosLabel.move(320, 600)
        # self.dadosLabel.setStyleSheet('background-color: white')

# Step 2: Build GUI content
    def add_content(self):
        self.button1 = QPushButton(self)
        self.button1.setGeometry(470, 650, 120, 80)
        self.button1.setStyleSheet(
            'background-color: white; border-image: none;')
        self.button1.setText('Gerar')
        self.button1.clicked.connect(self.button1_clicked)

        self.label = QLabel(self)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Dados do QRCode:')
        self.line = QLineEdit(self)

        # linha
        self.line.move(350, 600)
        self.line.resize(350, 32)
        self.nameLabel.move(460, 570)
        self.nameLabel.resize(200, 32)

        self.pixmap = QLineEdit(self)
        self.pixmap.move(510, 600)

# Step 3: Code GUI actions
    def button1_clicked(self):
        print('Dados QrCode: ' + self.line.text())
        self.dados = self.line.text()
        self.gerar = GeradorQrcode(self.dados)
        self.qrcode = self.gerar.gerar()
        self.pixmap = QPixmap('Qrcode.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.label.move(380, 200)


# Step 4: Make functionisis to run application


def run_app():
    app_objet = QApplication(sys.argv)
    gui = MyWindow()
    gui.show()
    sys.exit(app_objet.exec_())


run_app()
