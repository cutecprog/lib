"""Hold generic shell keyboard reading code in this file"""

def getch():
        """Get one to four characters press at once and return them

        """
        from sys import stdin
        from termios import tcgetattr, tcsetattr, TCSADRAIN
        from tty import setraw
        from os import read
        fd = stdin.fileno()
        old_settings = tcgetattr(fd)
        try:
                setraw(fd)
                ch = read(fd, 12)
        finally:
                tcsetattr(fd, TCSADRAIN, old_settings)
        return ch

def loc(pos):
        """Return string to move cursor to pos

        """
        y, x = pos
        return '\033[%s;%sH' % (str(y),str(x))

class Key:
        """Hold special characters

        """
        UP_ARROW     = '\033[A'
        DOWN_ARROW   = '\033[B'
        RIGHT_ARROW  = '\033[C'
        LEFT_ARROW   = '\033[D'
        ESC          = '\033'
        BACKSPACE    = '\033[3~'
        HBAR         = '\xe2\x94\x80'
        VBAR         = '\xe2\x94\x82'
        TL_CORNER    = '\xe2\x94\x8c'
        TR_CORNER    = '\xe2\x94\x90'
        BL_CORNER    = '\xe2\x94\x94'
        BR_CORNER    = '\xe2\x94\x98'
        TV_WORM      = '\xe2\x95\xb9'
        BV_WORM      = '\xe2\x95\xbb'
        BL_WORM      = '\xe2\x94\x93'
        BR_WORM      = '\xe2\x94\x8f'
        TL_WORM      = '\xe2\x94\x9b'
        TR_WORM      = '\xe2\x94\x97'
        H_WORM       = '\xe2\x94\x81'
        T_SQUARE     = '\033[7m\xe2\x96\x85\033[0m' 
        B_SQUARE     = '\xe2\x96\x85'
        HEART        = '\xe2\x99\xa5'
        EMPTY_HEART  = '\xe2\x99\xa1'
        SQUARE       = '\xe2\x96\xa0'
        EMPTY_SQUARE = '\xe2\x96\xa1'

class Cursor(object):
        """Hold a position one a terminal screen

        """
        def __init__(self, position, symbol):
                self.pos = position
                self.sym = symbol

        def __repr__(self):
                """Return printable string for symbol at position

                """
                return loc(self.pos) + self.sym
