init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("text.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
$ loc = Character(what_font="cour.ttf", callback=callback)


define c = Character(None, 
window_background=None,
what_xalign=0.5,
what_textalign=0.5,
what_layout='subtitle',
what_size = 50,
what_outlines=[( 5, "#5871CC", 0, 0 )],
what_italics=True,
what_font = "cock.ttf",
callback = callback
)

define narrator = Character(
    None,
    window_background=None,
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle',
    what_size = 50,
    what_italics=True,      
)