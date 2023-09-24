# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
default show_quick_menu = True




# The game starts here.

label start:
    scene test
    
    show screen pick
    ""

label guy:
    scene test

    show testguy  with dissolve
    show screen continue
    ""

label continue:
    hide screen pick
    hide screen continue
    scene test
    "booo"
    return
