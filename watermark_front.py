from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic

from PyQt5.QtGui import QPixmap
import os

from hidden_watermark import lsb1_stegano



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(os.path.join(os.path.split(__file__)[0], "watermark_front.ui"), self)


        self.browse_button.clicked.connect(self.browse_image)
        self.watermark_button.clicked.connect(self.watermark_image)



    def browse_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(self, 'Selectionne une image', '', 'All Files (*)')
        self.image_label.setPixmap(QPixmap(self.image_path))
        self.watermark_button.setEnabled(True)
        self.extract_message_button.setEnabled(True)



    def watermark_image(self):
        message = self.message_plain_text_edit.toPlainText()
        lsb1_stegano(self.image_path, message)