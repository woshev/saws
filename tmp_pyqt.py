import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QWidget

class SimpleTable(QTableWidget):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.initUI()

    def initUI(self):
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)

        # Добавляем данные в таблицу для примера
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                item = QTableWidgetItem("Row {}, Col {}".format(row, col))
                self.setItem(row, col, item)

        # Подключаем событие itemEntered
        self.itemEntered.connect(self.onItemEntered)

    def onItemEntered(self, item):
        self.parent().updateStatusLabel(item.row(), item.column())

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.table = SimpleTable(5, 5)  # Создаем таблицу размером 5x5
        layout.addWidget(self.table)
        self.statusLabel = QLabel()
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Simple Table")
        self.show()

    def updateStatusLabel(self, row, col):
        self.statusLabel.setText(f"Row: {row}, Col: {col}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
