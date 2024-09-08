# US States Guessing Game

Welcome to the US States Guessing Game! This interactive learning game helps children learn and remember US states in a fun and engaging way. The game challenges users to guess US states by typing them into an input box. Correct guesses will be highlighted on a US map, while incorrect or missed guesses will be tracked and reported in a CSV file for further learning.

## Features

- **Interactive Learning**: Users guess US states, which are then highlighted on a map.
- **Feedback Mechanism**: At the end of the game, a CSV file is generated listing any states that were missed.
- **Engaging UI**: The game uses Turtle graphics to display the map and handle user interaction.
- **Educational Tool**: Designed to help children learn US states in an enjoyable way.

## Getting Started

To run the US States Guessing Game, follow these steps:

### Prerequisites

- Python 3.x
- PyCharm (or any Python IDE)
- Required libraries: `pandas`, `turtle`

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/us-states-guessing-game.git
   cd us-states-guessing-game
   ```

2. **Install Required Libraries:**

   You can install the necessary Python libraries using pip. Open a terminal and run:

   ```bash
   pip install pandas
   ```

3. **Run the Game:**

   Open the project in PyCharm or your preferred Python IDE. Locate the `main.py` file and run it. This will start the game, and you should see the interactive map and input box.

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game:**
   - Run `main.py` to start the game.

2. **Guess the States:**
   - Type the name of a US state into the input box and press Enter.
   - If the guess is correct, the state will be highlighted on the map.
   - If the guess is incorrect, it will not be highlighted.

3. **End of the Game:**
   - At the end of the game, a CSV file will be generated containing the names of any states that were not guessed correctly.

## Libraries Used

- **Turtle**: Used for displaying the US map and handling UI design.
- **Pandas**: Used for generating and managing the CSV file with missing states.

## Contributing

Feel free to contribute to the project! If you have suggestions for improvements or want to add new features, please fork the repository and create a pull request. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy learning and have fun with the US States Guessing Game!
