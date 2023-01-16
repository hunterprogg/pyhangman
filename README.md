# PyHangman

Hangman in Python

## Setup

Create a virtual environment, if you name it venv-pyhangman in the top-level directory of this project, Git will ignore it. You can do that like so: python3 -m venv venv-pyhangman.

Source your virtual environment, like this: source venv-pyhangman/bin/activate, then run pip install -r venv_requirements.txt to pull down all of the dependencies.

This depends on the UNIX directionary being in ```/usr/share/dict/words```

## Running

After sourcing the environment as per the setup instructions you can simply run it like so:

```python3 hangman.py```
```
   ___
  /   |
 |    0
 |   -|-
 |   / 
/ \

o f f i c i a l l _ 

Guesses: s t h n e 

Choose a letter or make a guess: y
Good guess! y is in the word.
You found all the letters in officially. You win!```