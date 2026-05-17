`# Chess Engine From Scratch

## Overview

This project is a fully functional chess engine built from scratch. It implements all core chess rules, including legal move validation, check/checkmate detection, and an AI decision-making system using the minimax algorithm with alpha-beta pruning.

## Features

- **Board Representation**: An 8x8 chess board with piece positions and turn tracking.
- **Piece Movement Logic**: Valid movement for all chess pieces, including special rules like castling and en passant.
- **Legal Move Generation**: Generates all possible legal moves for a given board state.
- **Check Detection**: Detects when a king is in check and prevents illegal moves that would leave the king in check.
- **Endgame Systems**: Implements checkmate, stalemate detection, and pawn promotion.
- **Evaluation Function**: Scores board states based on material values and positional factors.
- **AI Decision System**: Uses the minimax algorithm with alpha-beta pruning for optimal move selection.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd chess-engine
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the chess engine, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to play against the AI.

## Testing

Unit tests are provided for various components of the chess engine. To run the tests, use:
```
pytest
```

## Future Extensions

- Graphical User Interface (GUI)
- Multiplayer support
- Opening database integration
- Comparison with other chess engines like Stockfish
- Reinforcement learning for improved AI

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.`