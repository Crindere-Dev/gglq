# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")





# The game starts here.

label start:
    $ quick_menu = False
    scene test
    
    show screen pick
    ""

label guy:
    scene test
    show may_base with dissolve
    call screen select
    ""

label continue:
    hide screen pick
    hide screen continue
    scene black with pixellate
    
    "ladderrrr"
    return
