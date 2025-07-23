import random
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap, QImageReader

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.poses = ["Раком","Миссионерская","Ложки","У стенки","Наездница","Супружеская", "Дельфин","Крючок", "Петля"]
        self.images = { "Раком" : "cancer.png", "Миссионерская" : "mission.png", "Ложки" : "lozki.png",
                            "У стенки" : "wall.png", "Наездница" : "rider.png", "Супружеская" : "christ.png",
                            "Дельфин" : "dolphin.png", "Крючок" :"kruk.png", "Петля" : "petla.jpg"}

        self.button = QtWidgets.QPushButton("Рандом")
        self.text = QtWidgets.QLabel("Выбор позы",
                                     alignment=QtCore.Qt.AlignCenter)
        self.imageLabel = QtWidgets.QLabel(" ",alignment=QtCore.Qt.AlignCenter)
        self.imageLabel.setGeometry(30, 30, 100, 100)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.imageLabel)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.sexRandomize)

    

    @QtCore.Slot()
    def load_and_display_image(self):
    #Загружает изображение и отображает его в QLabel.

    #Args:
    #   self.root: Путь к файлу изображения.
    #    label: Объект QLabel для отображения изображения.

        try:
            image_reader = QImageReader(self.root)
            if not image_reader.canRead():
                raise Exception(f"Не удалось прочитать файл изображения: {self.root}")

            image = image_reader.read()
            if image.isNull():
                raise Exception(f"Не удалось загрузить изображение: {self.root}")

            pixmap = QPixmap.fromImage(image)
            self.imageLabel.setPixmap(pixmap)
            #self.imageLabel.setScaledContents(True) # Масштабирует изображение, чтобы соответствовать размерам QLabel
        except Exception as e:
            print(f"Ошибка: {e}")
    @QtCore.Slot()
    def sexRandomize(self):
        self.cp = random.choice(self.poses)                 #choice pose
        self.root = self.images[self.cp]
        self.text.setText(self.cp)
        self.load_and_display_image()
        

if __name__ == "__main__":
        app = QtWidgets.QApplication([])

        widget = MyWidget()
        widget.resize(800, 600)
        widget.show()

        sys.exit(app.exec())
