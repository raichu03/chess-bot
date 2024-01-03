# SIMPLE CHESS BOT

## Overview

Welcome to the Simple Chess Bot! This is a basic chess playing bot written in python. The purpose of this bot is to provide a simple and educational example of how a chess bot can be implemented. I have used MiniMax algorithm for game tree traversing and made s simple evaluation function for bot to know how good is that position. This enables bot to make decisions on itself and can play chess following all the chess rules.

I have used [python-chess](https://pypi.org/project/chess/) to represent chess in computer. This library provides us with all the chess rules availabe for our bot to follow. It also gives us availabe legal chess moves after every move so our bot can traverse through game tree.

I have used MiniMax algorithm to traverse the game tree. Which is easy to implement but is has exponential growth problem. This forces us to search game tree to the depth of 3 or 4, anything above it is too much search tree to traverse using MiniMax.

## Features

* Basic Chess Logic: The bot understands the fundamental rules of the chess, including legal moves for each and chek/checkmate conditions.

* Command Line Interface (CLI): Interact with bot through a command-line interface, making it easy to play against or test.

## Getting Started

### Prerequisites

* [python-3.11.6](https://www.python.org/downloads/), [c++/c](https://www.tutorialspoint.com/cplusplus/cpp_environment_setup.htm), [Git](https://git-scm.com/downloads) installed on your machine.

### Installition

* Clone the repository to your local machine:

```bash
git clone https://github.com/raichu03/chess-bot.git
```

* Navigate to the project directory:

```bash
cd chess-bot
```

* Run the bot:

```bash
python main.py
```

note: running main.py command runs the bot against stockfish, to play it with human player you will have to make some twicks in code
