define m = Character("Eufrid", image="Test")
image MC happy = "Test2.png"
image MC sad = "Test3.png"

define c = Character("Cordula")
image Edel1 = "Edel.png"

define e = Character("Emil")
image rean1 = "rean.png" 

define s = Character("Síofra")
image placeholder1 = "images/placeholder1.png"
image placeholder2 = "images/placeholder2.jpg"
image nothing = "images/nothing.jpg"

screen Nothing():
    "..."
    "You need to get moving."
    "..."
    "There is no point in stnading around."
    "..."

    imagemap:
        ground "images/Blank.jpg"
        hotspot (613, 240, 620, 510) action Jump("dialogue") tooltip "..."

    $ tooltip = GetTooltip()
    
    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 0.75

screen forest_path():
    imagemap:
        ground "images/bakery1.png"
        # hover "images/FOREST_hover.jpg"   # optional: shows a highlight on hover

        # hotspot (x, y, width, height)
        hotspot (242, 199, 120, 100) action Jump("placeholder1") tooltip "Mysterious noises are coming from this area."
        hotspot (378, 172, 120, 100) action Jump("nothing") tooltip "Nothing of note."

    $ tooltip = GetTooltip()

    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 0.75

# The game starts here.

label start:
    show MC happy
    m "..."
    m "There's nothing here"
    call screen Nothing
    m "What is that...?"


label dialogue:
    show MC sad

    m "Huh?"
    m "Where is this...?"
    play music "audio/VillageTest.mp3"

    call screen forest_path


label placeholder1:
    scene placeholder1
    menu:
        "Who should I talk to?"

        "Emil":
            show rean1
            "Hey Emil"

        "Cordula":
            show Edel1
            $ cordula = "True"

            "Hey Cordula"

    
label after_placeholder1:
    "Now what."
menu: 
    "Maybe I should go back to the bakery."

    "Go back":
        call screen forest_path
    
    "Stay here":
        $ stay = "True"

        "Welp I'm done"

return
label nothing:
    scene nothing
    "Ahh so normal..."
    return