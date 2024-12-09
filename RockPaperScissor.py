import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class RockPaperScissorsGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock-Paper-Scissors Game")
        self.setGeometry(100, 100, 400, 400)
        
        # Scores
        self.user_score = 0
        self.computer_score = 0
        
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Set background color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#f0f8ff"))  # Alice Blue
        self.setPalette(palette)
        
        # Labels
        self.result_label = QLabel("Welcome to Rock-Paper-Scissors!", self)
        self.result_label.setFont(QFont("Arial", 14))
        self.result_label.setStyleSheet("color: #4b0082;")  # Indigo
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)
        
        self.score_label = QLabel("Scores - You: 0, Computer: 0", self)
        self.score_label.setFont(QFont("Arial", 12))
        self.score_label.setStyleSheet("color: #2e8b57;")  # SeaGreen
        self.score_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.score_label)
        
        # Buttons
        self.rock_button = QPushButton("Rock", self)
        self.paper_button = QPushButton("Paper", self)
        self.scissors_button = QPushButton("Scissors", self)
        
        # Style buttons with unique colors
        self.rock_button.setStyleSheet("""
            QPushButton {
                background-color: #ff6347;  /* Tomato */
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #e55341;  /* Darker Tomato */
            }
        """)
        self.paper_button.setStyleSheet("""
            QPushButton {
                background-color: #4682b4;  /* Steel Blue */
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #3a6a92;  /* Darker Steel Blue */
            }
        """)
        self.scissors_button.setStyleSheet("""
            QPushButton {
                background-color: #32cd32;  /* Lime Green */
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2da82d;  /* Darker Lime Green */
            }
        """)
        
        # Connect buttons to actions
        self.rock_button.clicked.connect(lambda: self.play_round("rock"))
        self.paper_button.clicked.connect(lambda: self.play_round("paper"))
        self.scissors_button.clicked.connect(lambda: self.play_round("scissors"))
        
        # Add buttons to layout
        self.layout.addWidget(self.rock_button)
        self.layout.addWidget(self.paper_button)
        self.layout.addWidget(self.scissors_button)
    
    def get_computer_choice(self):
        """Generate a random choice for the computer."""
        return random.choice(["rock", "paper", "scissors"])
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner of a round."""
        if user_choice == computer_choice:
            return "tie"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            return "user"
        else:
            return "computer"
    
    def play_round(self, user_choice):
        """Play a round of Rock-Paper-Scissors."""
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        
        if result == "user":
            self.user_score += 1
            message = "You win this round!"
        elif result == "computer":
            self.computer_score += 1
            message = "Computer wins this round!"
        else:
            message = "It's a tie!"
        
        # Update result and scores
        self.result_label.setText(
            f"You chose: {user_choice}, Computer chose: {computer_choice}\n{message}"
        )
        self.score_label.setText(f"Scores - You: {self.user_score}, Computer: {self.computer_score}")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RockPaperScissorsGame()
    window.show()
    sys.exit(app.exec_())
