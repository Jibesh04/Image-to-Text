import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import io

class ImageDisplay(QtWidgets.QMainWindow):
    def __init__(self):
        super(ImageDisplay, self).__init__()

        self.image_label = QtWidgets.QLabel()
        self.setCentralWidget(self.image_label)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Image Display")
        self.setGeometry(100, 100, 400, 400)

    def open_image(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Image")
        if file_path:
            with open(file_path, 'rb') as f:
                img_data = f.read()

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(img_data)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.KeepAspectRatio))
            else:
                print("Failed to load image:", file_path)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ImageDisplay()
    window.show()

    # Open the image when the application starts
    window.open_image()

    sys.exit(app.exec_())
