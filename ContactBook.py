import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QWidget
)
from PyQt5.QtCore import Qt

class ContactManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Management System")
        self.setGeometry(100, 100, 600, 400)
        
        # Contact storage
        self.contacts = {}
        
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Input fields for contact details
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter Name")
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Enter Phone Number")
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter Email Address")
        self.address_input = QLineEdit(self)
        self.address_input.setPlaceholderText("Enter Address")
        
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.phone_input)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.address_input)
        
        # Buttons
        self.add_button = QPushButton("Add Contact")
        self.add_button.clicked.connect(self.add_contact)
        self.update_button = QPushButton("Update Contact")
        self.update_button.clicked.connect(self.update_contact)
        self.delete_button = QPushButton("Delete Contact")
        self.delete_button.clicked.connect(self.delete_contact)
        self.search_button = QPushButton("Search Contact")
        self.search_button.clicked.connect(self.search_contact)
        
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.update_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.search_button)
        
        # Table for displaying contacts
        self.contact_table = QTableWidget()
        self.contact_table.setColumnCount(4)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone", "Email", "Address"])
        self.contact_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.layout.addWidget(self.contact_table)
    
    def add_contact(self):
        """Add a new contact."""
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()
        address = self.address_input.text().strip()
        
        if not name or not phone:
            QMessageBox.warning(self, "Input Error", "Name and Phone are required!")
            return
        
        if phone in self.contacts:
            QMessageBox.warning(self, "Duplicate Entry", "A contact with this phone number already exists.")
            return
        
        self.contacts[phone] = {"name": name, "email": email, "address": address}
        self.refresh_table()
        self.clear_inputs()
        QMessageBox.information(self, "Success", "Contact added successfully.")
    
    def update_contact(self):
        """Update an existing contact."""
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()
        address = self.address_input.text().strip()
        
        if not phone:
            QMessageBox.warning(self, "Input Error", "Phone number is required to update a contact!")
            return
        
        if phone not in self.contacts:
            QMessageBox.warning(self, "Not Found", "No contact found with the given phone number.")
            return
        
        self.contacts[phone] = {"name": name, "email": email, "address": address}
        self.refresh_table()
        self.clear_inputs()
        QMessageBox.information(self, "Success", "Contact updated successfully.")
    
    def delete_contact(self):
        """Delete a contact."""
        phone = self.phone_input.text().strip()
        
        if not phone:
            QMessageBox.warning(self, "Input Error", "Phone number is required to delete a contact!")
            return
        
        if phone not in self.contacts:
            QMessageBox.warning(self, "Not Found", "No contact found with the given phone number.")
            return
        
        del self.contacts[phone]
        self.refresh_table()
        self.clear_inputs()
        QMessageBox.information(self, "Success", "Contact deleted successfully.")
    
    def search_contact(self):
        """Search for a contact."""
        query = self.name_input.text().strip()
        if not query:
            QMessageBox.warning(self, "Input Error", "Please enter a name or phone number to search!")
            return
        
        results = [
            (details["name"], phone, details["email"], details["address"])
            for phone, details in self.contacts.items()
            if query.lower() in details["name"].lower() or query in phone
        ]
        
        if results:
            self.contact_table.setRowCount(0)
            for row_data in results:
                self.add_table_row(row_data)
        else:
            QMessageBox.information(self, "Not Found", "No matching contacts found.")
    
    def refresh_table(self):
        """Refresh the contact table to display all contacts."""
        self.contact_table.setRowCount(0)
        for phone, details in self.contacts.items():
            self.add_table_row((details["name"], phone, details["email"], details["address"]))
    
    def add_table_row(self, row_data):
        """Add a row to the table."""
        row = self.contact_table.rowCount()
        self.contact_table.insertRow(row)
        for column, data in enumerate(row_data):
            self.contact_table.setItem(row, column, QTableWidgetItem(data))
    
    def clear_inputs(self):
        """Clear the input fields."""
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.address_input.clear()

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactManager()
    window.show()
    sys.exit(app.exec_())
