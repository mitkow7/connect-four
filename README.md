# 🎮 Connect Four

Welcome to the Connect Four game! This is a console-based implementation of the classic Connect Four game, where two players take turns dropping colored discs into a vertical grid. The objective is to be the first player to form a horizontal, vertical, or diagonal line of four discs.

## ✨ Features

- 👥 Two-player mode
- 🖥️ Console-based UI
- 🕹️ Simple and intuitive game mechanics
- 🔧 Board size customization
- 🏆 Victory detection for horizontal, vertical, and diagonal lines

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### 📋 Prerequisites

- 🐍 Python 3.6 or higher

### 🛠️ Installation

1. Clone the repository:
```bash
  git clone https://github.com/mitkow7/connect-four.git
  cd connect-four
 ```

### ▶️ Running the Game

To start the game, simply run the following command:
```bash
python connect_four.py
```

## 🎲 How to Play

1. The game is played on a grid that is 6 rows by 7 columns.
2. Players take turns choosing a column to drop their disc into.
3. The disc will occupy the lowest available space within the chosen column.
4. The first player to align four of their discs horizontally, vertically, or diagonally wins the game.
5. If the board fills up before either player achieves four in a row, the game ends in a draw.

## ⚙️ Customization

You can customize the board size by modifying the `ROWS` and `COLUMNS` constants in `connect_four.py`:
```python
ROWS = 6
COLUMNS = 7
```

## 🤝 Contributing

Contributions are welcome! If you have any suggestions or find any bugs, please open an issue or submit a pull request.

###