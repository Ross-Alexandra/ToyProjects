# Evil Hangman
## Description
Evil hangman is a variant of the hangman game where 
the word chooser (usually a computer) will change the
word as the game is played. This word will **always**
match a word that is valid (aka, if you guess 'b', it
will choose a new word that doesn't have 'b' in it.)
This can... expectedly... get quite difficult as there
are a lot of words out there.

## Setup
### Backend
The backend (and cool end) of this project is written 
in Python3 so you will need to have that installed.

From there, the backend uses no external dependancies.
and thus setup is done!

### Front-end (WIP)
The frontend of this project is a normal old React app
which connects to a backend socket server to play the
game. Rather than redevleoping evil hangman in JS
and doing a purely web-design for the frontend I decided
that it would be more interesting to learn how to do 
socket connections. Thus, this frontend was born.

Beyond the normal setup for a React App, nothing special
is required.

## Running
The easiest way to try out evil hangman is via the CLI.
To do this, simply go to the root directory 
`.../evilHangman/` and run
```
python -m hangman.hangman
```

Further, there are arguments which can be passed to
make the game easier/more fun. These arguments can
be access using the `--help` switch, however they are
also provided at the bottom of this document for
convenience.

> Note the frontend of this project is still a work
in progress. Thus, this experience is not complete.


If you would like a more modern experience, then you 
can also run the frontend webapp and play from there!
To run the webapp, simply navigate to the 
`evilHangman/web/hangman` directory and run
```
npm start
```

To start the backend socket server, you will need to
also run 
```
python -m hangman.hangman -s
```

## CLI Usage
```
usage: __main__.py [-h] [-a ATTEMPTS] [-c LETTER_COUNT] [-d DICTIONARY] [-s]

A fun game of hangman... with a twist!

optional arguments:
  -h, --help            show this help message and exit
  -a ATTEMPTS, --attempts ATTEMPTS
                        The number of attempts a player gets
  -c LETTER_COUNT, --letter-count LETTER_COUNT
                        The number of letter a word should have
  -d DICTIONARY, --dictionary DICTIONARY
                        The file to load the dictionary from
  -s, --server          Run a socket server rather than a CLI interface.
PS C:\Users\Ross Alexandra\git\local\evilHangman> 
```