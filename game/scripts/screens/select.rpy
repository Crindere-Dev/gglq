screen test_select_hover:
    image "test_select_hover.png"

screen text_select:
    image "test_select.png"

screen select_button:
    image "select_button.png"

screen select_button_hover:
    image "select_button_hover.png"

screen pick:
    imagemap:
        ground "test_select"
        hotspot((684, 41, 579, 493)) hovered ShowTransient("test_select_hover") unhovered Hide("test_select_hover") clicked Jump("guy")

screen select:
    imagemap:
        ground "select_button"
        hotspot (1642, 25, 154, 975) hovered ShowTransient("select_button_hover") unhovered Hide("select_button_hover") clicked Jump("continue")
screen continue():
    vbox:
        textbutton "Continue?" action Jump("continue")