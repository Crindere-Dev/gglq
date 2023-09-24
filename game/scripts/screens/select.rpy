screen test_select_hover:
    image "test_select_hover.png"

screen text_select:
    image "test_select.png"


screen pick:
    imagemap:
        ground "test_select"
        hotspot((684, 41, 579, 493)) hovered ShowTransient("test_select_hover") unhovered Hide("test_select_hover") clicked Jump("guy")


screen continue():
    vbox:
        textbutton "Continue?" action Jump("continue")