# Mini Space Shooter – Python + Pygame + FastAPI

A 2D space shooter game developed as part of the Mega Task project.  
The game includes level progression, boss fights, a health system, and an **online leaderboard integration**.

A FastAPI backend and a basic automated test file are also included.

---

## Overview

Mini Space Shooter is an arcade-style game built with Python and Pygame.  
The player controls a spaceship, defeats descending UFO enemies, and progresses through eight increasingly difficult levels.

At the end of the game, the player’s name and final score are automatically sent to an online leaderboard service.

This project demonstrates:
- Game loop and collision logic  
- Difficulty scaling  
- FastAPI backend integration  
- Online leaderboard support  
- Clean GitHub project structure  

---

## Features

### Gameplay
- Left / Right spaceship movement  
- Shooting mechanics  
- UFO enemies  

### Levels & Bosses
- Levels 1–8 with increasing difficulty  
- Boss fight (Level 4)  
- Final Boss (Level 8)  

### Game States
- Player name input  
- Three-life system  
- Game Over and Victory screens  

---

## Online Leaderboard

- Player enters a name at game start  
- Score increases by defeating enemies and bosses  
- Final score is sent via HTTP request when the game ends  

🔗 **Leaderboard / Backend Endpoint:**  
https://mini-space-shooter-backend.onrender.com

---

## Backend (FastAPI)

A FastAPI backend is included in the `backend/` folder and deployed on Render to receive player score data.

---

## How to Run the Game Locally

```bash
git clone https://github.com/Ummu-Bozdemir/mini-space-shooter.git
cd mini-space-shooter
pip install -r requirements.txt
python main.py
 ``` 
 ---

 ## Project Links
 
GitHub Repository:
https://github.com/Ummu-Bozdemir/mini-space-shooter

Backend (Render):
https://mini-space-shooter-backend.onrender.com

Medium Article:
https://medium.com/@ummuzdemir/building-my-mini-space-shooter-game-with-python-pygame-75c3dd06a2d3

StudentHub Project Page:
https://student-hub.base44.app/projectdetail?id=6917a32617bca03c94f2c906

Technologies Used
Python 3

Pygame

FastAPI

Requests

Render