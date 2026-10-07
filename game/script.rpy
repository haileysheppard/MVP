define m = Character("Eufrid")
define c = Character("Cordula")
define e = Character("Emil")
define s = Character("Síofra")

image MC happy = "Test2.png"
image MC sad = "Test3.png"
image Edel1 = "Edel.png"
image Emil1 = "Emil1.png"
image bakery1 = "images/BakeryFinal.png"
image placeholder1 = "images/placeholder1.png"
image placeholder2 = "images/placeholder2.jpg"
image nothing = "images/Blank.jpg"
image town = "images/PLACEHOLDERTOWN.png"
image start = "images/PlaceholderStart.png"

default visited = set()

screen Nothing():
    imagemap:
        ground "start"
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
    "Freedom and Life are earned by those alone who conquer them each day anew"
    "To live is to keep moving forward, no matter what."
    "The world does not wait for anyone."
    
    call screen Nothing
    m "What is that...?"

label dialogue:
    m "..."
    "You need to get moving"
    m "..."
    "There is no point in standing around."
    m "..."

    jump town

label town: 
    scene town
    m "And with that prepartions for tomorrow are complete!"
    m "Now that I have some free time I might as well wander around for a bit."

    menu:
        "What should I do?"

        "Go to the bakery":
            jump bakery

        "Stay here":
            $ stayhere = True
            jump StayHere
        
   
    jump bakery                     

label StayHere:
    m "I should take a break and rest for a bit."
    m "I deserve it after all that hard work."

    jump FadetoBlack


label FadetoBlack:
    play audio "audio/Twinkle.mp3"
    scene nothing
    m "zzz..."
    jump Stayhere2

label Stayhere2:
    play audio "audio/Clap.mp3"
    scene town
    m "???"

    show Emil1
    e "Sorry that was louder than I thought it would be."
    e "But I just couldn't help myself when I saw you dozing here!"
    m "What the hell Emil! I was so happily sleeping!"
    e "... On a rickety, old bench?"
    m "Yes! What's so wrong with using public property!"
    e "You're such a strange person."
    m "(This is Emil. We have known each other since we were kids.)"
    m "(Normally, he works at the bakery.)"
    m "Why are you not at work?"
    e "... Just out for a little walk."

    menu:
        "How should I respond"

        "Believe him":
            m "Sounds reasonable enough. Your boss is too nice to you."
            e "...Yeah"
            jump Emil_2
        "Question him":
            $ QuestionHim = True
            m "Your boss really lets you just wander around during working hours?"
            e "Yes. That woman has the kindest soul of anyone I know!"
            m "(Yeah right.)"
            jump Emil_2

    label Emil_2:
        e "Welp. I should really get back to work."
        m "Okay. See you at the festival tomorrow!"
        m "(What an odd person.)"

return




return

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
    play audio "audio/Door.mp3"
    m "?"
    show Emil1
    e "Hello Eufrid. What are you doing here?"
    m "(This is just the person I was looking for.)"
    m "(This is Emil. We have known each other since we were kids.)"
    m "(Currently, he works at the bakery.)"
    e "Eufrid...?"
    m "Sorry, what were you saying?"
    e "I was just asking you what you are doing here."
    
    menu:
        "How should I respond"

        "Just wandering around":
            e "I guess that makes sense."
            m "Well, I guess I should get a move on. Wouldn't want to distract you."
            e "Don't worry about it! It was nice to see you!"
            jump after_chat

        "None of your business":
            $ NoneOfYourBusiness = True
            e "What do you mean none of my business.!"
            m "I don't think your boss would agree with that."
            e "That's not the point right now. Stop messing around."
            m "I was just wandering around. Don't be so dramatic"
            m "I was just about to leave anyways."
            e "Okay... see you later."
            jump after_chat

        "Nothing":
            $ Nothing = True
            e "Doesn't seem like nothing. But who am I to judge."
            m "Yeah. Who are you to judge?"
            e "... I'm just gonna get back to work."
            m "(I guess that means I should leave.)"

            jump after_chat
label after_chat:
    m "Bye! See you at the festival!"

    