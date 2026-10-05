define m = Character("Eufrid")
define c = Character("Cordula")
define e = Character("Emil")
define s = Character("Síofra")

image MC happy = "Test2.png"
image MC sad = "Test3.png"
image Edel1 = "Edel.png"
image rean1 = "rean.png"
image bakery1 = "images/BakeryFinal.png"
image placeholder1 = "images/placeholder1.png"
image placeholder2 = "images/placeholder2.jpg"
image nothing = "images/nothing.jpg"

default visited = set()

screen Nothing():
    imagemap:
        ground "images/Blank.jpg"
        hotspot (613, 240, 620, 510) action Jump("dialogue") tooltip "..."

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 0.75

screen forest_path():
    imagemap:
        ground "images/BakeryFinal.png"

        hotspot (233, 345, 419, 191) action Return("Bread")      tooltip "Bread"
        hotspot (660, 164, 406, 177) action Return("Jars")       tooltip "Jars"
        hotspot (664, 628, 372, 108) action Return("Pastries")   tooltip "Pastries"
        hotspot (0, 611, 394, 247)   action Return("FreshBread") tooltip "Fresh Bread"

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" xalign 0.5 yalign 0.75

label start:
    show MC happy
    m "..."
    m "There's nothing here"
    call screen Nothing
    m "What is that...?"

label dialogue:
    show MC sad
    m "..."
    "You need to get moving"
    m "..."
    "There is no point in standing around."
    m "..."

    play music "audio/VillageTest.mp3"
    jump bakery                      # <-- don't fall through into the next label

label bakery:
    scene bakery1

label bakery_loop:
    call screen forest_path
    $ spot = _return

    if spot == "Bread":
        m "Wow, it looks like they are prepping a lot."
        m "I guess it makes sense, the festival starts tomorrow..."
        m "Maybe I should've done more prep..."

    elif spot == "Jars":
        m "I see these jars everyday yet I still don't know what they are for."

    elif spot == "Pastries":
        m "Wow, that smells divine."
        m "I wonder if they could sneak me a piece..."

    elif spot == "FreshBread":
        m "Looks freshly made."
        m "I wonder if they made it."

    $ visited.add(spot)

    if len(visited) == 4:
        jump all_viewed

    jump bakery_loop

label all_viewed:
    m "They don't seem to be coming back anytime soon. I should probably leave."
    jump placeholder1                # <-- otherwise it just runs into whatever label is next

label placeholder1:
    scene placeholder1
    menu:
        "Who should I talk to?"

        "Emil":
            show rean1
            "Hey Emil"

        "Cordula":
            show Edel1
            $ cordula = True
            "Hey Cordula"

label after_placeholder1:
    "Now what."
    menu:
        "Maybe I should go back to the bakery."

        "Go back":
            jump bakery

        "Stay here":
            $ stay = True
            "Welp I'm done"

    return