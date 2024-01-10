from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic

from PyQt5.QtGui import QPixmap
import os



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(os.path.join(os.path.split(__file__)[0], "watermark_front.ui"), self)


        self.browse_button.clicked.connect(self.browse_image)



    def browse_image(self):
        image_path, _ = QFileDialog.getOpenFileName(self, 'Selectionne une image', '', 'All Files (*)')
        self.image_label.setPixmap(QPixmap(image_path))