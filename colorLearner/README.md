# colorLearner

## Description
While talking with my girlfriend about the different
colors, shape, etc that different fungi can take on
she thought it would be interesting to have a program
which could show you a bunch of colors and learn from
input to try and make the same interesting patterns.

Turns out human reinforced learning without datasets
is **really** slow. So this project isn't that fun
or interesting to play with. But hey, if you have an 
hour and want to make it try and learn to make a zebra
pattern, it's probably possible.

## Setup
Before first run, you will need to have the required
Python packages installed. To do this, simply run
```
pip install -r requirements.txt
```

## Running
The easiest way to start running this program is to
simply run
```
python learner.py
```

This will create a 15x15 grid of randomly generated colors. If you would like to change the number of
"cells", then simply run
```
python learner.py <width>
```
> Please note that as of present only NxN grids are
supported. Aka, only grids whose height match their
width. Hence why only a width option is available.

## Techincal Stack
This project was planned to be a toy from the start.
As such, the stack for this project was simply the
easiest things I could use to get it up and running.

The color display is simply a `pygame` screen using
the `Rect` object to draw the grid of colors.

In order to facilitate learning, `pygan` was used 
to do genetic learning. Each gene in the *organism*
is an integer number from 0 to 16777215 (0xffffff).
This integer number is then converted to hex, then
rgb, then displayed via `pygame`.

Finally, to facilitate both displaying the pattern, 
and taking user input via `stdin` simultaniously, 
Python's `multiprocessing` library is used to spawn
a seperate process for the displaying of relevant info.
This process then communicates with `pygan`'s organisms
(aka, gets new color-grids) via `multiprocessing`'s
`Queue` object.

That's it. `pygan` creates a populaiton of organisms
who's genes are the colors of the squares. Each
organism is then *deflattened* into the NxN grid
of rgb values. Those values are then displayed
in a seperate process, and the user is prompted
to input a fitness value for the generated pattern.