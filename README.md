# ColorGrid

## Description

ColorGrid is a programming project developed as part of the first-year curriculum at ENSAE Paris. The game involves a grid-based matching problem with specific rules and constraints.

## Problem Description

Consider an $`\( n \times m \)`$ grid, where $\( n \geq 1 \)$ and $\( m \geq 2 \)$ are integers representing the number of rows and columns, respectively. Each cell in the grid has coordinates $\((i, j)\)$ where $\( i \in \{0, \ldots, n-1\} \)$ is the row index and $\( j \in \{0, \ldots, m-1\} \)$ is the column index. Each cell has two attributes:

- **Color $\( c(i, j) \)$**: An integer in $\(\{0, 1, 2, 3, 4\}\)$ corresponding to a color:
  - 0: White (`'w'`)
  - 1: Red (`'r'`)
  - 2: Blue (`'b'`)
  - 3: Green (`'g'`)
  - 4: Black (`'k'`)

- **Value $\( v(i, j) \)$**: A positive integer.

### Objective

The goal is to select pairs of adjacent cells with the following constraints:

- Cells must be adjacent either horizontally or vertically.
- Black cells cannot be paired.
- White cells can be paired with any other color except black.
- Blue cells can be paired with blue, red, or white cells.
- Red cells can be paired with blue, red, or white cells.
- Green cells can only be paired with green or white cells.

Each cell can only be part of one pair. The objective is to minimize the score calculated as the sum of the absolute differences in values of the paired cells plus the sum of the values of unpaired cells (excluding black cells).

## Directory Structure

```
ColorGrid/
│
├── src/
│   ├── main.py              # Main script to run the game
│   ├── grid.py              # Grid class and related functions
│   ├── pairing.py           # Functions for pairing cells
│   └── utils.py             # Utility functions
│
├── tests/
│   ├── test_grid.py         # Unit tests for grid functionality
│   └── test_pairing.py      # Unit tests for pairing functionality
│
├── data/
│   ├── example_grid.csv     # Example grid data
│   └── ...                  # Additional data files
│
├── README.md                # Project documentation
└── requirements.txt         # Required Python packages
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/arthurdrk/Jeu-appariement-sur-une-grille.git
   cd Jeu-appariement-sur-une-grille
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python src/main.py
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
