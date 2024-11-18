import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QListWidget, QDateEdit, QTimeEdit
from PyQt5.QtCore import QDate, QTime, Qt  
from PyQt5.QtGui import QColor, QFont

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List Application")
        self.setGeometry(100, 100, 600, 600)
        self.setStyleSheet("background-color: #e0f7fa;")  

        # Main layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(30, 30, 30, 30)  

        self.title_label = QLabel("To-Do List", self)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold; color: #00796b;")
        self.title_label.setAlignment(Qt.AlignCenter)  
        self.layout.addWidget(self.title_label)

        self.task_title_input = QLineEdit(self)
        self.task_title_input.setPlaceholderText("Enter task title")
        self.task_title_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 16px;
                border: 2px solid #00796b;
                border-radius: 5px;
                background-color: #ffffff;
            }
        """)
        self.layout.addWidget(self.task_title_input)

        self.date_time_layout = QHBoxLayout()
        self.date_time_layout.setSpacing(15)

        self.date_label = QLabel("Select Date:", self)
        self.date_label.setStyleSheet("font-size: 14px; color: #00796b;")
        self.date_picker = QDateEdit(self)
        self.date_picker.setDate(QDate.currentDate())
        self.date_picker.setStyleSheet("""
            QDateEdit {
                padding: 8px;
                font-size: 14px;
                border: 2px solid #00796b;
                border-radius: 5px;
                background-color: #ffffff;
            }
        """)
        self.date_time_layout.addWidget(self.date_label)
        self.date_time_layout.addWidget(self.date_picker)

        # Time picker
        self.time_label = QLabel("Select Time:", self)
        self.time_label.setStyleSheet("font-size: 14px; color: #00796b;")
        self.time_picker = QTimeEdit(self)
        self.time_picker.setTime(QTime.currentTime())
        self.time_picker.setStyleSheet("""
            QTimeEdit {
                padding: 8px;
                font-size: 14px;
                border: 2px solid #00796b;
                border-radius: 5px;
                background-color: #ffffff;
            }
        """)
        self.date_time_layout.addWidget(self.time_label)
        self.date_time_layout.addWidget(self.time_picker)

        self.layout.addLayout(self.date_time_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(20)

        self.add_button = QPushButton("Add Task", self)
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: #00796b;
                color: white;
                font-size: 16px;
                padding: 12px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #004d40;
            }
        """)
        self.add_button.clicked.connect(self.add_task)
        self.buttons_layout.addWidget(self.add_button)

        self.update_button = QPushButton("Update Task", self)
        self.update_button.setStyleSheet("""
            QPushButton {
                background-color: #00796b;
                color: white;
                font-size: 16px;
                padding: 12px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #004d40;
            }
        """)
        self.update_button.clicked.connect(self.update_task)
        self.buttons_layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete Task", self)
        self.delete_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                font-size: 16px;
                padding: 12px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #c62828;
            }
        """)
        self.delete_button.clicked.connect(self.delete_task)
        self.buttons_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.buttons_layout)

        # Task Listbox with custom styles
        self.task_list_widget = QListWidget(self)
        self.task_list_widget.setStyleSheet("""
            QListWidget {
                font-size: 16px;
                border: 2px solid #00796b;
                border-radius: 5px;
                background-color: #ffffff;
            }
        """)
        self.layout.addWidget(self.task_list_widget)

        self.setLayout(self.layout)

    def add_task(self):
        # Get input values
        title = self.task_title_input.text()
        date = self.date_picker.date().toString("yyyy-MM-dd")
        time = self.time_picker.time().toString("HH:mm")

        if title and date and time:
            task = f"{title} - {date} {time}"
            self.task_list_widget.addItem(task)

            # Clear input fields after adding task
            self.task_title_input.clear()
            self.date_picker.setDate(QDate.currentDate())
            self.time_picker.setTime(QTime.currentTime())
        else:
            self.show_error("All fields are required!")

    def update_task(self):
        selected_task = self.task_list_widget.currentItem()
        if selected_task:
            title = self.task_title_input.text()
            date = self.date_picker.date().toString("yyyy-MM-dd")
            time = self.time_picker.time().toString("HH:mm")

            if title and date and time:
                updated_task = f"{title} - {date} {time}"
                selected_task.setText(updated_task)

                self.task_title_input.clear()
                self.date_picker.setDate(QDate.currentDate())
                self.time_picker.setTime(QTime.currentTime())
            else:
                self.show_error("All fields are required!")
        else:
            self.show_error("Please select a task to update.")

    def delete_task(self):
        selected_task = self.task_list_widget.currentItem()
        if selected_task:
            self.task_list_widget.takeItem(self.task_list_widget.row(selected_task))
        else:
            self.show_error("Please select a task to delete.")

    def show_error(self, message):
        from PyQt5.QtWidgets import QMessageBox
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
