# 🟡 Pacman AI Game

This repository contains a custom implementation of the classic Pacman game in Python, enhanced with intelligent ghost AI using A* and Greedy algorithms. The game is built with **Pygame** and optimized using **C++ integration** via `ctypes` for performance-critical pathfinding tasks.

---

<img width="477" height="565" alt="391293653-ab45f6c2-2d38-4a72-b2d7-73c5d6c81114" src="https://github.com/user-attachments/assets/4f7ac047-de23-40ee-841e-08c93c961d96" />


## 🖥️ Installation

- Requires Python 3.x (tested on 3.12)
- Works on **Windows only**
- Install dependencies:

```bash
pip install -r requirements.txt
```

- To run the game:

```bash
python main.py
```

---

## 🎮 Gameplay Overview

The game features:
- Smooth grid-based movement
- Dynamic ghost behavior powered by AI
- Intelligent ghost chasing (A*) and fleeing (Greedy)
- Modular codebase for scalability

---

## 🧠 AI Algorithms (Predator vs. Prey)

Ghosts in the game are designed to behave differently based on **Pacman's state**:

### 👹 Predator Mode (A* Search)
When ghosts chase Pacman, they use the **A* algorithm** to calculate the shortest path intelligently:
- Takes both **cost so far (g)** and **heuristic (h)** into account.
- Results in **precise, aggressive tracking**, mimicking a predator.
- Implemented in C++ for performance and integrated with Python.

### 👻 Prey Mode (Greedy Search)
When Pacman eats a power pellet, ghosts switch to fleeing mode using **Greedy search**:
- Chooses the next step based solely on **heuristic distance to safety**.
- Less efficient but more **erratic and reactive**, mimicking prey behavior.
- Prioritizes escape over optimality, adding tension and fun.

This dynamic creates a **prey-predator reversal**, adding depth to gameplay and strategy.

---

## 📷 Interface Preview

![Gameplay Interface](https://github.com/user-attachments/assets/ab45f6c2-2d38-4a72-b2d7-73c5d6c81114)

---

## 🧩 Modules & Structure

### `main.py` — Game Loop
- Initializes game and settings
- Handles input, updates, and rendering
- Manages transitions (menu ↔ game)

### `menu.py` — Main Menu
- Navigation UI
- Handles "Start Game" and "Quit" options

### `init.py` — Game Initialization
- Loads assets and variables
- Sets up Pacman, ghosts, and maze
- Includes utility functions (e.g. `draw_lives`, `setPacmanOrientation`)

### `logic.py` — Core Game Logic
- Controls all object movement and interactions
- Updates score, life, and states based on collisions

### `settings.py` — Maze & Game Config
- Holds the maze design and level configurations
- Implements A* in C++ for faster pathfinding

---

## 📦 Dependencies

- `pygame` — Game engine
- `ctypes` — C++ integration for A*
- `copy`, `sys`, `math`, `heapq`, `time`, `random` — Native utilities

---

## 🔧 Recommendations & Future Improvements

- ✅ **[Done]** Use C++ for A* algorithm for faster ghost pathfinding
- 🚧 Improve Pacman movement to support smoother, pixel-based transitions instead of tile-by-tile
- ⚠️ Add **"ghost warning" state** just before kill-mode expires (e.g. blinking blue)
- 👻 Adjust ghost vulnerability logic: currently ghosts become permanently invulnerable after being eaten once
- 🧱 Replace `getMazeDesign()` with 2D legend (0: dot, 1: pellet, 2: empty, 3: wall) for flexibility *(partially done in `practise.py`)*

---

## 📬 Contact

Built by **Mohamed Magdy Mohamed Mady**  
📧 mohamed.mady2000@gmail.com | [LinkedIn](https://www.linkedin.com/in/mohamed-mady-422b23192)

---
