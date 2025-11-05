from PyQt6.QtWidgets import QApplication

from windows import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv) # Создаем объект QApplication и передаем в него аргументы командной строки
    window = OrdersMainWindow() # Создаем экземпляр класса OrdersMainWindow
    window.show() # Показываем окно на экране
    sys.exit(app.exec()) # Завершаем главный циклы при закрытии окна