# Rock, Paper, Scissors Game

This game is a simple implementation of the classic "Rock, Paper, Scissors" game using Python and Pygame. The game sounds have been sourced from Soundsnap, and the icons from Flaticon, both of which offer free licenses for non-commercial projects. For the game, you can click one of the buttons (Rock, Paper, or Scissors). If you win, you will hear the win sound (sounds/win.wav) and your score will increment. If you lose, you will hear the lose sound (sounds/lose.wav) and the computer's score will increment. If you draw, you will hear the draw sound (sounds/draw.wav), and neither your score nor the computer's score will increment.

## Resources

Resources such as images and sound

- [Icons] www.flaticon.com
- [Sound Effects] www.soundsnap.com

Game documentation

- [Pygame Docs] https://www.pygame.org/docs/
- [Pygame Text Render] https://pygame.readthedocs.io/en/latest/4_text/text.html
- [Pygame GameSound] https://www.youtube.com/watch?time_continue=107&v=tEedb5KiaWY&embeds_referring_euri=https%3A%2F%2Fwww.google.com%2F&source_ve_path=MzY4NDIsMjM4NTE&themeRefresh=1

Testing documentation

- [Unit Testing] https://docs.python.org/3/library/unittest.html

Continous Integration

- [Github Actions] https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions
- [Python and Github Actions] https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
- [Tutorial] https://www.vlinkinfo.com/blog/how-to-build-a-cicd-pipeline/

Create diagram

- [Diagram] https://app.diagrams.net/

## Requirements

- Python 3.6 or higher
- Pygame
- Pytest

## Installation

1. Clone this repository: 
``git clone https://yourrepository.com/rock_paper_scissors.git``

2. Navigate to the project directory:
``cd AdvancedPrograming``

3. Install the required packages:
``pip install -r requirements.txt``


## Running the Game

Run the game using Python:
``python game/main.py``


## Automated Testing
To run the automated testing please move to the base directory (In our case AdvancedPrograming)
``cd AdvancedPrograming``

Then run the following command
``python -m unittest discover -s tests``

## Diagrams

The location of Diagrams is as follows:
``/diagram/..``

The diagrams were created using ``draw.io``
