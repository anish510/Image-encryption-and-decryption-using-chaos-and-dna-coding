import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QLineEdit, QMessageBox, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import encryption as encr
import decryption as decr

class EncryptedImageWindow(QMainWindow):

    def __init__(self, file_path):
        super().__init__()
        self.title = 'Encrypted Image'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300
        self.file_path = file_path
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width, self.height)

        pixmap = QPixmap(self.file_path)
        pixmap = pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

    def closeEvent(self, event):    
        event.ignore()
        self.show()

class DecryptedImageWindow(QMainWindow):

    def __init__(self, file_path):
        super().__init__()
        self.title = 'Decrypted Image'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300
        self.file_path = file_path
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.width, self.height)

        pixmap = QPixmap(self.file_path)
        pixmap = pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

    def closeEvent(self, event):    
        event.ignore()
        self.show()

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Encryption and Decryption'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(200, 20, 400, 300)

        # file path label
        self.path_label = QLabel('File Path:', self)
        self.path_label.setGeometry(200, 350, 50, 30)

        # file path field
        self.path_field = QLineEdit(self)
        self.path_field.setGeometry(250, 350, 200, 30)
        self.path_field.textChanged.connect(self.load_image) #Added just now

        # browse button
        self.browse_button = QPushButton('Browse', self)
        self.browse_button.setGeometry(480, 350, 100, 30)
        self.browse_button.clicked.connect(self.browse_image)

        # password label
        self.password_label = QLabel('Password:', self)
        self.password_label.setGeometry(200, 400, 50, 30)

        # password field
        self.password_field = QLineEdit(self)
        self.password_field.setGeometry(250, 400, 200, 30)
        self.password_field.setEchoMode(QLineEdit.Password)

        # encrypt button
        self.encrypt_button = QPushButton('Encrypt', self)
        self.encrypt_button.setGeometry(250, 450, 100, 30)
        self.encrypt_button.clicked.connect(self.encrypt_image)

        # decrypt button
        self.decrypt_button = QPushButton('Decrypt', self)
        self.decrypt_button.setGeometry(480, 450, 100, 30)
        self.decrypt_button.clicked.connect(self.decrypt_image)

        self.show()

    def browse_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.xpm *.jpg *.bmp *.tiff *.jpeg);;All Files (*)", options=options)
        if file_name:
            self.path_field.setText(file_name)
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

            self.file_path = file_name

    def load_image(self):
        file_name = self.path_field.text()
        if file_name:
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

    def encrypt_image(self):
        if self.path_field.text():
            if len(self.password_field.text()) >= 8:
                encrypted_file_path = encr.encryption(self.path_field.text(), self.password_field.text())
                if encrypted_file_path:
                    encrypted_window = EncryptedImageWindow(encrypted_file_path)
                    encrypted_window.closeEvent = lambda event: encrypted_window.show()
                    encrypted_window.show()
                    # QMessageBox.information(self, 'Encryption Completed', 'Encryption is completed! Encrypted image is displayed.')
                else:
                    QMessageBox.warning(self, 'Encryption Error', 'Encryption failed!')
            else:
                QMessageBox.warning(self, 'Password Required', 'Password length should be at least 8 characters!')
        else:
            QMessageBox.warning(self, 'Image Required', 'Please select an image!')

    def decrypt_image(self):
        if self.path_field.text():
            if len(self.password_field.text()) >= 8:
                decrypted_file_path = decr.decryption(self.path_field.text(), self.password_field.text())
                if decrypted_file_path:
                    decrypted_window = DecryptedImageWindow(decrypted_file_path)
                    decrypted_window.closeEvent = lambda event: decrypted_window.show()
                    decrypted_window.show()
                    # QMessageBox.information(self, 'Decryption Completed', 'Decryption is completed! Decrypted image is displayed.')
                else:
                    QMessageBox.warning(self, 'Decryption Error', 'Decryption failed!')
            else:
                QMessageBox.warning(self, 'Password Required', 'Password length should be at least 8 characters!')
        else:
            QMessageBox.warning(self, 'Image Required', 'Please select an image!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())