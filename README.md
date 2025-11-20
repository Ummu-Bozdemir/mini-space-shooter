Mini Space Shooter – Python + Pygame + FastAPI

A 2D space shooter game developed as part of the Mega Task project.
The game includes movement, enemy waves, level progression, boss fights, a health system, and final win/lose screens.
A FastAPI backend and a basic automated test file are also included.

Overview

Mini Space Shooter is a simple arcade-style game built with Python and Pygame.
The player controls a spaceship, shoots descending UFO enemies, and progresses through eight increasingly difficult levels.

The project demonstrates game loop logic, collision detection, difficulty balancing, backend integration, and clean GitHub structure.

Features

Player spaceship with left/right movement

Bullet shooting mechanics

UFO enemies descending from the top

Level system (Levels 1–8)

Boss battle at Level 4

Final Boss at Level 8

Three-life health system

Game Over screen with restart button

Victory screen

FastAPI backend deployed on Render

Automated test file (tests/test_basic.py)

Installation & Setup
1. Clone the repository
git clone https://github.com/Ummu-Bozdemir/mini-space-shooter
cd mini-space-shooter

2. Install dependencies
pip install -r requirements.txt

3. Run the game
python main.py

Controls

Left Arrow: Move left

Right Arrow: Move right

Space: Shoot

Backend (FastAPI)

The project includes a small backend for demonstration purposes.

Run locally:
uvicorn backend.main:app --reload

Live backend deployment:

https://mini-space-shooter-backend.onrender.com

Running Tests
pytest

Project Links

GitHub:
https://github.com/Ummu-Bozdemir/mini-space-shooter

Backend (Render):
https://mini-space-shooter-backend.onrender.com

Medium Article:
https://medium.com/@ummuzdemir/building-my-mini-space-shooter-game-with-python-pygame-75c3dd06a2d3

StudentHub Page:
https://student-hub.base44.app/projectdetail?id=6917a32617bca03c94f2c906
