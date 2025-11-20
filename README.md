# Mini Space Shooter – Python + Pygame + FastAPI

A 2D space shooter game developed as part of the Mega Task project.  
The game includes player movement, enemy waves, level progression, boss fights, a health system, and final win/lose screens.  
A FastAPI backend and a basic automated test file are also included.

---

## Overview

Mini Space Shooter is a simple arcade-style game built with Python and Pygame.  
The player controls a spaceship, shoots descending UFO enemies, and progresses through eight increasingly difficult levels.

This project demonstrates:
- Game loop logic  
- Collision detection  
- Difficulty balancing  
- Backend integration (FastAPI)  
- Clean GitHub project structure  
- Basic automated testing  

---

## Features

### Core Gameplay
- Player spaceship with left/right movement  
- Bullet shooting mechanics  
- UFO enemies descending from the top  

### Level & Difficulty
- Level system (Levels 1–8)  
- Increasing difficulty every level  
- Boss battle at Level 4  
- Final Boss at Level 8  

### Game State Management
- Three-life health system  
- Game Over screen with restart button  
- Victory screen  

---

## Backend (FastAPI)
A small FastAPI backend is included in the `backend/` folder and deployed on Render.

🔗 **Live Backend:**  
https://mini-space-shooter-backend.onrender.com

---

## How to Run the Game Locally

1. Clone the repository
git clone https://github.com/Ummu-Bozdemir/mini-space-shooter.git
cd mini-space-shooter

2. Install dependencies
pip install -r requirements.txt

3. Run the game
python main.py

Project Links

GitHub Repository:
https://github.com/Ummu-Bozdemir/mini-space-shooter

Medium Article:
https://medium.com/@ummuzdemir/building-my-mini-space-shooter-game-with-python-pygame-75c3dd06a2d3

StudentHub Project Page:
https://student-hub.base44.app/projectdetail?id=6917a32617bca03c94f2c906

Backend (Render) URL:
https://mini-space-shooter-backend.onrender.com

Tests

A small automated test file is included in the tests/ folder.
This ensures minimal project structure validation.

Technologies Used

Python 3

Pygame

FastAPI

Render (Deployment)
