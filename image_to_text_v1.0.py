from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtGui import QImageReader
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
 
# for image_formats in QImageReader.supportedImageFormats():
#     print(image_formats.data().decode())

class SuccessDialog(QtWidgets.QDialog):
    def __init__(self, message):
        super(SuccessDialog, self).__init__()
        self.setWindowIcon(QtGui.QIcon("Iconocr.png"))
        self.setWindowTitle("Success")
        self.resize(216, 92)
        
        self.success_message = QtWidgets.QLabel(message, self)
        self.success_message.setGeometry(50, 20, 121, 16)
        self.success_message.setAlignment(QtCore.Qt.AlignCenter)
        
        self.ok_button = QtWidgets.QPushButton("OK", self)
        self.ok_button.setGeometry(70, 50, 75, 23)
        self.ok_button.clicked.connect(self.close_success_dialog)

    def close_success_dialog(self):
        self.close()

# Load the UI file
ui_file = "Main Window v0.1.ui"
app = QtWidgets.QApplication([])
window = uic.loadUi(ui_file)

# Perform any necessary connections or modifications to the UI

file_path = ""
image_path = ""

def display_clicked():
    print("Hello World.!")

"""
def dragEnterEvent(event):
    if event.mimeData().hasUrls():
        event.accept()
    else:
        event.ignore()

def dropEvent(event):
    global image_path
    if event.mimeData().hasUrls():
        urls = event.mimeData().urls()
        image_path = urls[0].toLocalFile()
        load_image(image_path)
        event.accept()
    else:
        event.ignore()
"""

def select_image():
    global image_path
    image_dialog = QtWidgets.QFileDialog
    image_path, _ = image_dialog.getOpenFileName(window,"Select Image", "", "Image files (*.png *.jpg *.jpeg)")
    load_image(image_path)

def load_image(image_path):
    window.image_dir_line.setText(image_path)
    if image_path:
        with open(image_path, "rb") as file:
            img_data = file.read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(img_data)
    if not pixmap.isNull():
        window.image_label.setPixmap(pixmap.scaled(window.image_label.size(), QtCore.Qt.KeepAspectRatio))
        window.text_edit.clear()
        window.text_edit.insertPlainText(pytesseract.image_to_string(Image.open(image_path)))
        if window.text_edit.toPlainText != "":
            window.text_dir_button.setEnabled(True)
    else:
        print("Failed to load image:", file_path)


def browse_text_file_directory():
    global file_path
    file_dialog = QtWidgets.QFileDialog
    file_path, _ = file_dialog.getSaveFileName(window, "Export As", "", "Text Files (*.txt)")
    window.text_dir_line.setText(file_path)
    window.save_button.setEnabled(True)

def save_text_file():
    with open(file_path, "w") as file:
        file.write(window.text_edit.toPlainText())
    pop_up = SuccessDialog("Text File Exported")
    pop_up.exec_()
    reset()

def reset():
    window.image_label.clear()
    window.text_edit.clear()
    window.image_label.setText("Image Preview")
    window.image_dir_line.setText("")
    window.text_dir_line.setText("")
    window.save_button.setEnabled(False)

window.setWindowTitle("Image to Text")
window.setWindowIcon(QtGui.QIcon("Iconocr.png"))
window.image_dir_button.clicked.connect(select_image)
window.text_dir_button.clicked.connect(browse_text_file_directory)
window.save_button.clicked.connect(save_text_file)
window.save_button.setEnabled(False)
window.text_dir_button.setEnabled(False)
window.text_dir_line.setReadOnly(True)
window.image_dir_line.setReadOnly(True)
# window.image_label.setAcceptDrops(True)

if __name__ == "__main__":
    # Run the application
    window.show()
    app.exec()
