# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define morb = ImageDissolve("images/cooolio.png", 1.0, time_warp=_warper.easeout)


label splashscreen:
 scene black
with Pause (1)

show splash with morb
with Pause(2)
hide splash with morb
return


# The game starts here.

label start:
    $ quick_menu = False
    scene test with morb
    show screen pick with pixellate
    ""

label guy:
    scene test
    show may_base with dissolve
    call screen select
    ""

label continue:
    hide screen pick
    hide screen continue
    scene black with morb
    
    "ladderrrr"
    return
