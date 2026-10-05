define m = Character("Eufrid")

define c = Character("Cordula")
image Edel1 = "Edel.png"

define e = Character("Emil")
image rean1 = "rean.png"

define s = Character("Síofra")
image placeholder1 = "images/placeholder1.png"
image placeholder2 = "images/placeholder2.jpg"
image nothing = "images/nothing.jpg"

screen Nothing():

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
        hotspot (233, 345, 419, 191) action Jump("Bread") tooltip "Bread"
        hotspot (660, 164, 406, 177) action Jump("Jars") tooltip "Jars"
        hotspot (664, 628, 372, 108) action Jump("Pastries") tooltip "Pastries"
        hotspot (0, 611, 394, 247) action Jump("FreshBread") tooltip "Fresh Bread"


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
    m "..."
    "You need to get moving"
    m "..."
    "There is no point in standing around."
    m "..."

    play music "audio/VillageTest.mp3"

    call screen forest_path

label FreshBread:
m "Looks freshly made."
m "I wonder if they made it"


label Pastries:
m "Wow, that smells divine." 
m "I wonder if they could sneak me a piece..."

label Jars:
m "I see these jars everyday yet I still don't know what they are for."

label Bread:
m "Wow, it looks like they are prepping a lot."
m "I guess it makes sense, the festival starts tomorrow..."
m "Maybe I should've done more prep..."

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