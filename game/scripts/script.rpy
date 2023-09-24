# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


label splashscreen:
 scene black
with Pause (1)

show splash with dissolve
with Pause(2)
hide splash with dissolve
return


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
