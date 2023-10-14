# Conway's game of life.
simple implimentation of conway's game of life using pygame.

### To run:
1. create a virtual environment using ```python -m venv env```
2. install the dependencies ```pip install -r requirements.txt```
3. navigate to ```/src``` and run ```python run_game.py```


### Rules of the game:
- Birth: A dead cell with exactly three live neighbors becomes a live cell (it's "born").
- Survival: A live cell with two or three live neighbors remains alive; otherwise, it dies.
- Overpopulation: A live cell with more than three live neighbors dies.
- Loneliness: A live cell with fewer than two live neighbors dies.

### Controls:
- ```Space``` - Play/Pause the game
- ```Right-click``` - Manually add/remove a cell
- ```c``` - Clear all cells
- ```g``` - Randomly generate a batch of new cells
