# Ather_Energy_2048


2048 is a single-player sliding tile puzzle game. The objective of the game is to slide numbered tiles on a grid to combine them to create a tile with the number 2048, however, one can continue to play the game after reaching the goal.

## What's this about?

This is a little version of popular game 2048  designed using Python-Tkinter module.

# Discussion Objectives

## ● Design principles used
The design of solution was implemented with a GUI module in Python (tkinter), Here we would having
board of 4x4 size and two numbers by default, the task is used to gain the highest number on the tiles
by moving tiles in any direction without filling entire grid. There is no specific optimized
algorithm as there is random nature in game.

## ● Thoughts
As by solving the game, came to the conclusion that we need to traverse each and every cell in the gird and perform operation in order to get the target number.
So, here all the operations are broken into functions, and GUI was implemented as a class, each functionality was broken down into a 
small functions inorder to have a high readability.

## ● Problem Solution
The solution is to traverse throughout the grid and to  maintain a large value at any corner, This
make the chances to win high.

## ● Problems faced while designing the solution  
- The matrix manipulation is always needed to be taken care.
- Merging the cells with the curcial conditions.
- Buttons arrangement in tkinter window is little hetic.

## ● Code walkthrough
A sneky detail was provided in  **2048_game.py** file, where the functionality  of each function 
is broken down, The entire documentation would be here.

## ● Scope of making this an 8x8 from 4x4

As the solution is generic, by increasing grid size doesn't have more impact on
the code, but while solving we need to taken care as cells increases its hard to keep
the high value at corner of the grid. Here, there's a varibale **(size)** to change the grid size.

## ● Change from 2048 to 4096 as end number
Absolutely, Yes! we can change upto a certain value, Here,there's a varibale **(highest)** to change the number.
A higher tile of  **2^17** possible with 16 squares.


## Installation

Clone the project
```bash
  https://github.com/ran93r1210/Ather_Energy_2048.git
```
Go to the project directory
```bash
    cd my-project
```
Setting up virtual environment
Go to the project directory
```bash
    python -m venv my-name-virtual-env
    source my-name-virtual-env/bin/activate 
```
Install dependencies
```bash
    pip install -r requirements.txt
```
Run 
```bash
      python 2048.py
```


## Screenshots
- Working 2048 game.

![App Screenshot](https://github.com/ran93r1210/Ather_Energy_2048/blob/main/Assets/2048.png)



## Tech Stack

**Language :** Python


