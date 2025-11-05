from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QPushButton, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
from styles import labels_style, buttons_style


# Функция для получения размеров экрана
def window_sizes():
    screen = QApplication.primaryScreen() # Получаем объект QScreen для основного экрана
    screen_size = screen.size() # Получаем объект QSize с размерами экрана (высота и ширина)
    screen_width = screen_size.width() # Получаем ширину экрана
    screen_height = screen_size.height() # Получаем высоту экрана
    return int(screen_width * 0.6), int(screen_height * 0.8)



# Создаем класс главного окна
class OrdersMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MAXMATools") # Задаем название окна

        # Создаем экземпляр главного окна
        central_widget = QWidget() # Создаем экземпляр центрального виджета
        self.setCentralWidget(central_widget) # Устанавливаем его экземпляр как центральный виджет
        layout = QGridLayout(central_widget) # Устанавливаем макет-сетку и привязываем к central_widget
        self.setStyleSheet("background-color: #ffffff;") # Задаем цвет background'а

        # Создаем баннер
        banner = QLabel() # Создаем экземпляр класса QLabel() под баннер
        pixmap = QPixmap('images (1).jpg') # Делаем ссылку на изображение
        banner.setPixmap(
            pixmap.scaledToWidth(400, Qt.TransformationMode.SmoothTransformation))  # Масштабируем по ширине
        banner.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Выравнивание по центру
        layout.addWidget(banner, 1, 2, 1, 1) # Размещаем баннер в нашем layout по координатам

        # Создадим заголовок меню
        label = QLabel('Внутренние инструменты MAXMA', central_widget) # Создаем надпись с названием и присваиваем его главному виджету
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) # Тут выровняли лейбл по центру
        label.setStyleSheet(labels_style) # Присваиваем заголовку стили
        layout.addWidget(label, 2, 2, 1, 1) # Добавили этот виджет на ма сетку главного окна

        # Пустой лейбл
        label1 = QLabel(central_widget)  # Создаем надпись с названием и присваиваем его главному виджету
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Тут выровняли лейбл по центру
        label1.setStyleSheet(labels_style)
        layout.addWidget(label1, 3, 2, 1, 1)  # Добавили этот виджет на ма сетку главного окна

        # Создаем кнопку для выбора PluginMaker
        button_plugin_maker = QPushButton('Подготовить плагины IIKO')
        button_plugin_maker.setStyleSheet(buttons_style)
        button_plugin_maker.setMinimumSize(250, 40)
        button_plugin_maker.setMaximumSize(250, 80)
        layout.addWidget(button_plugin_maker, 4, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        button_plugin_maker.clicked.connect(self.pm_main_window)

        # Создаем кнопку для выбора OldOrders
        button_old_orders = QPushButton('Проверить файл импорта покупок')
        button_old_orders.setStyleSheet(buttons_style)
        button_old_orders.setMinimumSize(250, 40)
        button_old_orders.setMaximumSize(250, 80)
        layout.addWidget(button_old_orders, 5, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        button_old_orders.clicked.connect(self.oo_file_check)

        # Получаем размеры экрана
        screen = QApplication.primaryScreen() # Получаем объект QScreen для основного экрана
        screen_size = screen.size() # Получаем объект QSize с размерами экрана (высота и ширина)
        screen_width = screen_size.width() # Получаем ширину экрана
        screen_height = screen_size.height() # Получаем высоту экрана

        # Чтобы не тянуло на весь экран, задаем размеры 60% и 80% от самого экрана
        window_width = int(screen_width * 0.6) # Ширина окна как 60% от ширины экрана
        window_height = int(screen_height * 0.8) # Высота окна как 80% от высоты экрана
        self.resize(window_width, window_height) # Устанавливаем размеры окна

        self.center_window(screen) # Вызываем центровку окна
        self.setMinimumSize(int(screen_width * 0.5), int(screen_height * 0.5)) # Нельзя сделать окно меньше 50% экрана



    def center_window(self, screen):
        window_geometry = self.frameGeometry() # Получаем геометрию окна вместе с рамкой и заголовком
        screen_center = screen.availableGeometry().center() # Получаем координаты центра окна
        window_geometry.moveCenter(screen_center) # Перемещаем центр геометрии окна в центр экрана
        self.move(window_geometry.topLeft()) # Перемещаем окно так, чтобы его верхний угол совпадал с вычисленным значением

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def pm_main_window(self):
        self.close()
        self.show_window = PlVersionChoise()
        self.show_window.show()

    def oo_file_check(self):
        self.close()
        self.show_window = OOFileCheckMW()
        self.show_window.show()

# Создаем класс окна для отображения версий ПлагинМейкера
class PlVersionChoise(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MAXMATools - Подготовка плагинов") # Задаем название окна

        # Экземпляр окна для выбора версии ПлагинМейкера
        central_widget = QWidget() # Создаем экземпляр центрального виджета
        self.setCentralWidget(central_widget)  # Устанавливаем его экземпляр как центральный виджет
        layout = QGridLayout(central_widget)  # Устанавливаем макет-сетку и привязываем к central_widget
        self.setStyleSheet("background-color: #ffffff;")  # Задаем цвет background'а

        banner = QLabel()  # Создаем экземпляр класса QLabel() под баннер
        pixmap = QPixmap('images (1).jpg')  # Делаем ссылку на изображение
        banner.setPixmap(
            pixmap.scaledToWidth(400, Qt.TransformationMode.SmoothTransformation))  # Масштабируем по ширине
        banner.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Выравнивание по центру
        layout.addWidget(banner, 1, 2, 1, 1)  # Размещаем баннер в нашем layout по координатам

        window_width, window_height = window_sizes()

        self.resize(window_width, window_height)  # Устанавливаем размеры окна


class OOFileCheckMW(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MAXMATools - Проверка файла покупок")  # Задаем название окна

        # Экземпляр окна для выбора версии ПлагинМейкера
        central_widget = QWidget()  # Создаем экземпляр центрального виджета
        self.setCentralWidget(central_widget)  # Устанавливаем его экземпляр как центральный виджет
        layout = QGridLayout(central_widget)  # Устанавливаем макет-сетку и привязываем к central_widget
        self.setStyleSheet("background-color: #ffffff;")  # Задаем цвет background'а

        banner = QLabel()  # Создаем экземпляр класса QLabel() под баннер
        pixmap = QPixmap('images (1).jpg')  # Делаем ссылку на изображение
        banner.setPixmap(
            pixmap.scaledToWidth(400, Qt.TransformationMode.SmoothTransformation))  # Масштабируем по ширине
        banner.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Выравнивание по центру
        layout.addWidget(banner, 1, 2, 1, 1)  # Размещаем баннер в нашем layout по координатам

        window_width, window_height = window_sizes()

        self.resize(window_width, window_height)  # Устанавливаем размеры окна

        # Создаем кнопку Возврата в главное меню
        button_back = QPushButton('Вернуться в меню') # Создаем экземпляр кнопки
        button_back.setStyleSheet(buttons_style) # Задаем стиль кнопки
        button_back.setMinimumSize(250, 40) # Задаем минимальный размер кнопки
        button_back.setMaximumSize(250, 80) # Задаем максимальный размер кнопки
        layout.addWidget(button_back, 4, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter) # Задаем положение в сетке
        button_back.clicked.connect(self.back_to_main_menu) # Сигнал при нажатии кнопки

        # Создаем заголовок поля пут
        label_file_path = QLabel('Путь выбранного файла', central_widget)
        label_file_path.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Тут выровняли лейбл по центру
        label_file_path.setStyleSheet(labels_style)  # Присваиваем заголовку стили
        layout.addWidget(label_file_path, 2, 1, 2, 1)

        # Создаем кнопку для загрузки файла
        button_upload = QPushButton('Загрузить файл')
        button_upload.setStyleSheet(buttons_style)
        button_upload.setMinimumSize(250, 40)  # Задаем минимальный размер кнопки
        button_upload.setMaximumSize(250, 80)  # Задаем максимальный размер кнопки
        layout.addWidget(button_upload, 3, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)  # Задаем положение в сетке
        button_upload.clicked.connect(self.select_file_qt)



    def back_to_main_menu(self):
            self.close() # Закрыть существующее окно
            self.show_window = OrdersMainWindow() # Создаем экземпляр главного окна
            self.show_window.show() # Отображаем главное окно


    def select_file_qt(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,  # self — ссылка на родительское окно (обычно QWidget)
            "Выберите файл",
            "",  # начальная директория (пусто — домашняя папка)
            "Таблицы (*.xlsx)"  # фильтры
        )











