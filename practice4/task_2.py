import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QRadioButton, QSlider, QComboBox, \
    QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QTextEdit, QFileDialog, QFormLayout, QSpinBox, QButtonGroup
from PyQt6.QtCore import Qt


class Windown(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Главная страница")  # Прописываем параметры окна
        self.setGeometry(400, 400, 500, 500)

        # Виджеты для ввода данных
        self.data_name = QLineEdit(self)
        self.data_surname = QLineEdit(self)
        self.data_last_name = QLineEdit(self)
        self.data_age = QLineEdit(self)
        self.label2 = QLabel("")
        self.label3 = QLabel("")

        # Создаем ползунки для роста человека
        self.data_human_growth = QSlider(Qt.Orientation.Horizontal, self)
        self.data_human_growth.setRange(140, 230)
        self.data_human_growth.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.data_human_growth.valueChanged.connect(self.update)
        self.result_label = QLabel('', self)

        # Создаем ползунки для веса человека
        self.data_human_weight = QSlider(Qt.Orientation.Horizontal, self)
        self.data_human_weight.setRange(35, 200)
        self.data_human_weight.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.data_human_weight.valueChanged.connect(self.update1)
        self.result_label1 = QLabel('', self)

        # Создаем переключатель пола
        self.data_gender_men = QRadioButton("Мужской", self)
        self.data_gender_women = QRadioButton("Женский", self)
        self.btngroup1 = QButtonGroup()
        self.btngroup1.addButton(self.data_gender_men)
        self.btngroup1.addButton(self.data_gender_women)
        self.data_gender_men.toggled.connect(self.onClicked)
        self.data_gender_women.toggled.connect(self.onClicked)

        # Создаем переключатель для семейного положения
        self.data_position1 = QRadioButton("Свободен", self)
        self.data_position2 = QRadioButton("В отношениях", self)
        self.btngroup2 = QButtonGroup()
        self.btngroup2.addButton(self.data_position1)
        self.btngroup2.addButton(self.data_position2)
        self.data_position1.toggled.connect(self.onClicked2)
        self.data_position2.toggled.connect(self.onClicked2)

        # Делаем список профессий
        self.data_type_activity = QComboBox(self)
        self.data_type_activity.addItem("Программист")
        self.data_type_activity.addItem("Архитектор")
        self.data_type_activity.addItem("Врач")
        self.data_type_activity.addItem("Сантехник")
        self.data_type_activity.addItem("Учитель")
        self.data_type_activity.addItem("Преподаватель")

        # Создаем кнопку для сохранения данных
        self.save_data_button = QPushButton("Внести данные", self)
        self.save_data_button.clicked.connect(self.data_save)
        self.save_data_button.clicked.connect(self.displayMessageBox)

        self.data_button_check = QPushButton("Просмотр данных", self)
        self.data_button_check.clicked.connect(self.show_window_2)

        # Создаем макет окна(для изменения размеров)
        layout = QVBoxLayout()

        # Создаем макет для виджетов и размещаем их в окне приложения
        layout_name = QHBoxLayout()
        layout_name.addWidget(QLabel("Имя: "))
        layout_name.addWidget(self.data_name)
        layout.addLayout(layout_name)

        layout_surname = QHBoxLayout()
        layout_surname.addWidget(QLabel("Фамилия: "))
        layout_surname.addWidget(self.data_surname)
        layout.addLayout(layout_surname)

        layout_last_name = QHBoxLayout()
        layout_last_name.addWidget(QLabel("Отчество: "))
        layout_last_name.addWidget(self.data_last_name)
        layout.addLayout(layout_last_name)

        layout_age = QHBoxLayout()
        layout_age.addWidget(QLabel("Возраст: "))
        layout_age.addWidget(self.data_age)
        layout.addLayout(layout_age)

        layout_human_growth = QHBoxLayout()
        layout_human_growth.addWidget(QLabel("Рост: "))
        layout_human_growth.addWidget(self.data_human_growth)
        layout.addLayout(layout_human_growth)
        layout_result_label = QHBoxLayout()
        layout_result_label.addWidget(self.result_label)
        layout.addLayout(layout_result_label)

        layout_human_weight = QHBoxLayout()
        layout_human_weight.addWidget(QLabel("Вес: "))
        layout_human_weight.addWidget(self.data_human_weight)
        layout.addLayout(layout_human_weight)
        layout_result_label1 = QHBoxLayout()
        layout_result_label1.addWidget(self.result_label1)
        layout.addLayout(layout_result_label1)

        layout_gender = QHBoxLayout()
        layout_gender.addWidget(QLabel("Пол: "))
        layout_gender.addWidget(self.data_gender_men)
        layout_gender.addWidget(self.data_gender_women)
        layout.addLayout(layout_gender)

        layout_position = QHBoxLayout()
        layout_position.addWidget(QLabel("Семейное положение: "))
        layout_position.addWidget(self.data_position1)
        layout_position.addWidget(self.data_position2)
        layout.addLayout(layout_position)

        layout_type_activity = QHBoxLayout()
        layout_type_activity.addWidget(QLabel("Должность: "))
        layout_type_activity.addWidget(self.data_type_activity)
        layout.addLayout(layout_type_activity)

        layout.addWidget(self.save_data_button)
        layout.addWidget(self.data_button_check)

        # Добавляем в центральный виджет наш макет
        Widget = QWidget()
        Widget.setLayout(layout)
        self.setCentralWidget(Widget)
        self.show()

    def update(self, value):
        self.result_label.setText(f'Значение: {value}')

    def update1(self, value):
        self.result_label1.setText(f'Значение: {value}')

    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label2.setText(radioBtn.text())

    def onClicked2(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label3.setText(radioBtn.text())

    def displayMessageBox(self):
        QMessageBox.about(self, "Информация", "Данные записаны в файл")

    def data_save(self):
        dict_data = {"Имя": self.data_name.text(), "Фамилия": self.data_surname.text(),
                     "Отчество": self.data_last_name.text(), "Возраст": self.data_age.text(),
                     "Рост": self.data_human_growth.value(), "Вес": self.data_human_weight.value(),
                     "Пол": self.label2.text(),
                     "Семейное положение": self.label3.text(),
                     "Должность": self.data_type_activity.currentText()}

        with open("Data_test", "a") as file:
            for key, value in dict_data.items():
                file.write(f"{key}: {value}\n")
            file.write('\n')

    def show_window_2(self):
        self.window2 = File()
        self.window2.show()


class File(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Содержимое файла")
        self.setGeometry(400, 400, 500, 500)

        self.widget_text = QTextEdit(self)

        layout_text = QVBoxLayout()
        layout_text.addWidget(self.widget_text)
        self.setLayout(layout_text)

        with open("Data_test", 'r') as file:
            file3 = file.read()
            self.widget_text.setText(file3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Windown()
    main.show()
    sys.exit(app.exec())
