# The script of the game goes in this file.

#text effect animation

transform text_effect:
    parallel:
        block:
            linear 0.1 xoffset -2 yoffset 2 
            linear 0.1 xoffset 3 yoffset -3 
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha .2
            linear 1.0 alpha .9
            linear 1.0 alpha .2
            repeat

#shake effect
transform shake:
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    zoom 0.3
    repeat 5
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define teacher = Character("Teacher Smitzel", color="#208e37")
define joanna = Character("Joanna", color="#e61270")
define karel = Character("Karel", color="#dac624")
define helda_friend = Character("??", color="#0b43c3")
define helda = Character("Helda", color="e4b68a")
define tax_farmer_1 = Character("Tax Farmer 1", color="4a4744")
define tax_farmer_2 = Character("Tax Farmer 2", color="4a4744")
define commoner_1 = Character("Commoner 1", color="#c77f35")
define commoner_2 = Character("Commoner 2", color="#c77f35")
define mattieu = Character("Mathieu", color="#a09f95")
define louis = Character("Louis", color="#e2314c")
define louis = Character("Louis", color="#e2314c")
define lewis = Character("Lewis", color="#e2314c")


#toggle voice mute
screen voice_toggle:
    vbox:
        textbutton "Mute Tax farmer 1" action ToggleVoiceMute("tax_farmer_1")
        textbutton "Mute Tax farmer 2" action ToggleVoiceMute("tax_farmer_2")
        textbutton "Commoner 1" action ToggleVoiceMute("commoner_1")
        textbutton "Mute Commoner 2" action ToggleVoiceMute("commoner_2")
        textbutton "Mute Mattieu" action ToggleVoiceMute("mattieu")
        textbutton "Mute Louis" action ToggleVoiceMute("louis")


#define background size
define default_pos = Position(xalign=0, yalign=0)
transform default_size:
    zoom 1.2


#define character size
define char_pos = Position(xalign=0, yalign=0)
transform char_size:
    zoom 1.8,
    


#define karel size
define karel_pos = Position(xalign= 1800, yalign=150)
transform karel_size:
    zoom 0.2,
    hover

#define farright position on screen
define farright = Position(xpos=0.85)

#define farright position on screen
define farleft = Position(xpos=0.1)




#splashscreen
label splashscreen:
    scene black
    with Pause(1)
    show text "MindGarden Games presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    
    show text "Heads of State" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    return










# init python early:
#     def config.default_textshader = "typewriter"
# # The game starts here.

label start:
    stop music

    # Shows the history classroom background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #ask player their name
    scene black
    $ player_name = renpy.input("What is your name?").capitalize()
    pause 1
    play music "waltznchopin.mp3" fadein 2 volume 0.07
    pause 0.2
    scene bg classroom at default_pos, default_size
    with pixellate
    pause 0.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show smitzel at char_pos, char_size, right
    with dissolve

    # These display lines of dialogue. teacher smitzel is talking
    
    teacher "Before the french revolution came about it was the year 1789, King Louis was in charge, it was an absolute monarchy,  "

    teacher "he had all the power."

    teacher "France was in debt from wars, mainly because they helped America fight its war, hoping to weaken Britain, their longtime rival." 
    teacher "Combined with the lavish lifestyles of the king and upper classes, this led to a financial crisis."
    play sound ahem
    "Teacher Smitzel clears her throat"
    #joanna gets caught sleeping
    teacher "Joanna I see you nodding away you agree with what I’m saying."
    play sound laughing fadeout 0.5
    "The class erupts in laughter"

    show joanna tired at left:
        zoom 0.7

    joanna "Miss, I’m tired. Is this history lecture really necessary? We won’t need any of this in the future..."
    "Teacher smiles"
    teacher "You know students.... "
    teacher "If you really pay attention to the past, you can figure out a lot about what’s happening now, and even get a pretty good idea of what’s coming next."
    "Class mumbles"
    
    teacher "Joanna, thanks for sharing your view. Tomorrow after the test, I’d like each of you to give me a reason why history is useful, other than what I’ve already mentioned."
    #should student mention jaonna name in for leaving tr give hw
    # "The whole class groaned out her name in perfect unison      {shader=wave:u__amplitude=5.0,u__frequency=2.0,u__wavelength=20.0}Joooaaannaa…{/shader}"
    play sound joanna
    "The whole class groaned out her name in perfect unison Joooaaannaa…"
    hide joanna 

    teacher "Now let's continue. Not only wars and bad spending, but harsh winters and poor harvests made food scarce, adding to the people's suffering."
    
    "{i}My eyelids suddenly felt heavy{/i}"
    pause 0.3

    
    #screen slowly closes and opens 3 times before it completely turns black Student falls asleep 
    # Assume current scene is shown

    # First blink
    show screen eyelid_close(opening=False)
    $ renpy.pause(1.9)
    show screen eyelid_close(opening=True)
    $ renpy.pause(1.1)

    # Second blink
    show screen eyelid_close(opening=False)
    $ renpy.pause(1)
    show screen eyelid_close(opening=True)
    $ renpy.pause(1)

    # Final blink before scene change
    show screen eyelid_close(opening=False)
    $ renpy.pause(0.9)

    # Change to new scene while eyelids are closed
    scene bg street at default_pos, default_size
    with None  # No transition, since eyelids are still closed

    # Open eyelids to reveal new scene
    show screen eyelid_close(opening=True)
    $ renpy.pause(1.6)
    hide screen eyelid_close
    
    transform small_button:
        zoom 0.5  # Adjust the zoom level as needed

    #green run button
    screen runButton():
        imagebutton:
            xalign 0.5
            yalign 0.5
            at small_button
            auto "run_button_%s" 
            action Return()

  
    #scene bg street at default_pos, default_size


    show fairy at karel_pos, karel_size with move
    karel "In France they started taxing the commoners heavier than ever before. There was a tax for everything."
    

    hide fairy
    #show tax farmers
    show farmer at left with move:
        zoom 0.8
    hide fairy
    show tax farmer 2 at right with move:
        zoom 0.7
    #begin dialogue
    voice "taxfarmer.ogg"
    tax_farmer_1 "Hey, look at her that peasant is laughing too hard, tax her!"

    voice "taxfarmer2.ogg"
    tax_farmer_2 "And don't forget to pay your income tax. We're adding new tariffs of 50 percent! haha"

    hide farmer   
    hide tax farmer 2

    "!!" #alert
    #"How gready can some people be"
    show helda friend worried at left:
        zoom 0.8

    voice "heldafriend.ogg"
    helda_friend "Ridiculous utterly ridiculous. How are we supposed to get by? Oh Helda I tell you I'm tired so tired of it all. why don't they take money from the clergy or the “nobles” they barely pay anything if nothing at all."
    show helda at right
    voice "helda.ogg"
    helda "Oh how right you are. Why must it be like this?"
    hide helda friend
    hide helda

    



    # This ends the game.

    menu:
        "Someone has to stand up for these people!"

        "confront the tax farmer":
                jump punch
        "walk away":
                "Hmmmm... Should I? Maybe I'm just dreaming." 
                jump court



# pre: show tax farmer
#post: no tax farmer 2
label punch:

    #run to tax farmer
    show tax farmer 2 at right with move:
        zoom 0.7
    pause 4
    hide tax farmer 2
    show tax farmer 2 close at right with ease
    "The tax farmer turns arround as his eyes slowly trail down to my hand on his shoulder. He looks shocked."
    voice "handsoff.ogg"
    tax_farmer_1 "Remove your hand a-"
    
    play sound punch
    scene bg street at default_pos, default_size, Shake((0,0,0,0), 1.0, dist=20)

    "My fist landed where gravity wanted it. Though it felt as if I punched the air, somehow he flew from the blow and was never to be seen again."
    #wow sound
    play sound wow
    hide tax farmer 2
    show fairy at karel_pos, karel_size with move
    karel "Hey [player_name], that's not part of the script!" #[player_name]?
    "Hey it's my dream, alright! Sometimes, you just have to teach them a lesson!"

    







label court:

    #Blink transition to next scene tennis court
    #screen slowly closes and opens 3 times
    # Assume current scene is shown

    # First blink
    show screen eyelid_close(opening=False)
    $ renpy.pause(1.2)
    show screen eyelid_close(opening=True)
    $ renpy.pause(1.1)

    # Second blink
    show screen eyelid_close(opening=False)
    $ renpy.pause(1)
    show screen eyelid_close(opening=True)
    $ renpy.pause(1)

    # Final blink before scene change
    show screen eyelid_close(opening=False)
    $ renpy.pause(0.9)

    # Change to new scene while eyelids are closed
    scene bg tennis court at default_pos, default_size
    with None  # No transition, since eyelids are still closed

    # Open eyelids to reveal new scene
    show screen eyelid_close(opening=True)
    $ renpy.pause(1.6)
    hide screen eyelid_close


    
    show fairy at karel_pos, karel_size with move
    karel "In a moment crackling with tension, the voices of France’s common people thundered through the echoing halls of an old tennis court"
    karel "Where they had rushed after being locked out of their usual meeting place by the king’s guards."
    karel "Inside, they spoke of the deep unfairness at the National Assembly, where the rich and powerful always drowned out the common folk’s voices and kept the old rules that favored privilege over justice." 
    karel "On that day, surrounded by dust and the scent of rebellion, ordinary men and women stood together to demand a new, fairer France, daring the world to witness their unity."
    hide fairy
    voice "commonercourt.ogg"
    commoner_1 "They thought they can lock us out and drive us away!"
    voice "commonerconstitution.ogg"
    commoner_2 "Ha, never! We will not separate until we have given France a Constitution. We must act now, or we will never be free."
    
    pause 1
    show fairy at karel_pos, karel_size with move
    karel "Their voices rose in the old tennis court, calling not just for a constitution, but for a nation built on new ideals."
    karel "Liberty. Equality. Fraternity. These words echoed through the crowd, a vow that would change France forever and, in time, an inspiration to people around the world."
    pause 0.5
    hide karel

#BASTILLE SCENE ------------------------------------------------
label bastille:
   # pre: bg tennis court, waltznchoppin music
   # post: no more music
    

    #screen slowly closes and opens 3 times
    # Assume current scene is shown

    # First blink
    show screen eyelid_close(opening=False)
    $ renpy.pause(1.2)
    show screen eyelid_close(opening=True)
    $ renpy.pause(1.1)

    # Second blink
    show screen eyelid_close(opening=False)
    $ renpy.pause(1)
    show screen eyelid_close(opening=True)
    $ renpy.pause(1)

    # Final blink before scene change
    show screen eyelid_close(opening=False)
    $ renpy.pause(0.9)

    # Change to new scene while eyelids are closed
    scene bg bastille at default_pos, default_size
    show fairy at karel_pos, karel_size
    with None  # No transition, since eyelids are still closed

    # Open eyelids to reveal new scene
    show screen eyelid_close(opening=True)
    $ renpy.pause(1.6)
    hide screen eyelid_close


    stop music fadeout 2 
    play music "epic.mp3" fadein 1.2 volume 0.07
    "I suddenly stood in front of a fortress. Karel where did you bring me?"
    karel "To the morning of July 14, 1789, Paris was boiling with anger and fear as rumors spread that the king’s soldiers would crush the people’s uprising. Hundreds gathered at the Bastille,"
    karel "A massive stone fortress that guarded important stores of gunpowder and cannons the revolutionaries needed to defend themselves, as well as a handful of prisoners."
    karel "Tension crackled in the air as the crowd pressed closer, demanding the surrender of the fortress and its weapons,"
    karel "Knowing that taking the Bastille would send a message to the king and all of France that the people would no longer be ignored."
    
    hide fairy
    pause 3
    
    
    voice "bastilleprisoners.ogg"
    commoner_1 "They are taking way too long! Why haven't they released the prisoners yet?"
    voice "commonerhostage.ogg"
    
    "Commoner 2" "They're holding our people as hostages. {size=*1.5}Let's go in!{/size}"

    menu:
        "They think they can get away with this! Let's go in!":

            play music "risk.mp3" fadein 1 volume 0.7 # Plays the background music
            "I shoved forward with the crowd, heart racing, feet pounding the stone."
            "In the courtyard, I searched for a way in, eyes darting for a route to them."
            "Then I felt- That cold, sharp feeling like something was watching me."
            "I looked up."
            "A soldier. High above on the ledge. Rifle aimed. Finger ready."
            play sound "shot.mp3"
            "Then- Time slowed. I saw the bullet spin through the air like a cruel dance."
            call screen runButton
            play sound click
            
            "I tried to run. My brain screamed 'MOVE!' But my legs? Frozen."  

            stop music fadeout 2 # Stops the music with a 2-second fade-out
            
            #shot = true
            jump badclassroom
        
        "Let’s give them time.":
            hide karel
            "The crowd surged forward, but I stayed back, eyes fixed on the cannons we had dragged from the Hôtel des Invalides. If we charged in, we would be easy targets. We waited, tension crackling in the air."
            "Suddenly, shots rang out from the fortress."
            "I gave the order, and the roar of the cannons shattered the morning air, shaking the walls and rattling the windows of Paris itself."
            "Smoke curled and stones flew as the Bastille’s defenses faltered under our fire. The governor’s men fired back, but their numbers were few and their spirits fewer."
            "Hours passed like a storm until finally the drawbridge clattered down, not from our assault but from the governor’s surrender."
            "The gates opened and the crowd poured in, seizing the gunpowder and freeing the prisoners."
            stop music fadeout 0.7

    #Blink transition to next scene tennis court
    #screen slowly closes and opens 3 times
    # Assume current scene is shown

    # First blink
    show screen eyelid_close(opening=False)
    $ renpy.pause(1.2)
    show screen eyelid_close(opening=True)
    $ renpy.pause(1.1)

    # Second blink
    show screen eyelid_close(opening=False)
    $ renpy.pause(1)
    show screen eyelid_close(opening=True)
    $ renpy.pause(1)

    # Final blink before scene change
    show screen eyelid_close(opening=False)
    $ renpy.pause(0.9)

    # Change to new scene while eyelids are closed
    scene bg street at default_pos, default_size
    with None  # No transition, since eyelids are still closed

    # Open eyelids to reveal new scene
    show screen eyelid_close(opening=True)
    $ renpy.pause(1.6)
    hide screen eyelid_close
 
 
 
 
    play music "waltznchopin.mp3" fadein 1 volume 0.4
    pause 1
    





    "The Reign of Terror"

    "I walk with a group of familiar faces. For some reason, my father is in the background with a big sock on his head, tossing fruit into the crowd. None of us seem to notice except me."
    "What’s going on..."
    show matthieu at left with move:
        zoom 1

    voice "matthieu.ogg"
    mattieu "If we truly want a new country then we must get rid of the people who don't hold our values."
    voice "matthieu2.ogg"
    mattieu "Like Robespiere said virtue, without which terror is fatal; terror, without which virtue is powerless."
    #louis disagrees
    show louis angry at right with move:
        zoom 1
    voice "louisdeaths.ogg"
    louis "But too many people are dying and getting arrested as of late. It's getting out hand!"
    voice "louisdeaths2.ogg"
    louis "I can't stand that leader Robespierre of the Jacobins. The Jacobins were supposed to stand for liberty and the people, but now they’re nothing but bloodthirsty fanatics. "
    louis"Robespierre claims it’s all for the good of the Revolution,but he's sending folks to the guillotine just for speaking their minds. Anyone who disagrees with them is marked for death."
    louis "It’s tearing France apart."
    menu:
        "Agree with Louis":
            "Exactly! what if terror becomes the master, not the tool? What if we're the monsters now? What happened to the freedom we fought so hard to win?"  
            
            "The guillotine's blade falls too often, we're drowning in blood, and the wars have already turned this land apart. Are we really building a new world or just trading one nightmare for another?"
            
            
        "Agree with matthieu":
            "C'mon Louis keep your head on."
            play sound huh
            "Look, I'm not one for yelling or rushing into things. But sometimes, the world doesn't give you a choice. If we want freedom, we have to be willing to do what it takes — even if it’s ugly. The guillotine’s harsh, sure. But so is the fight ahead. Better to face it head-on than hope things just get better on their own."
            show louis dissapointed at right:
                zoom 1
                pause 1
            "Louis slowly removes his hand off my shoulder and looks at me in disbelief."
            stop music fadeout 0.7
            jump goodclassroom
        
        "Stay silent":
            stop music fadeout 0.7
            jump goodclassroom


         
label guillotine:
    stop music fadeout 0.3
    scene bg black
    
    play sound "badending.mp3" 

    #Blink transition to nightmare ending
    scene black
    play music "sad.mp3"

    "I see a crowd of people in front of me, but they're all.. quiet? "
    "Something is pressed against my neck. Something rough."
    "Uhm, Karel what's going on?"
    "Silence"
    "I try to move, but I can't. What an odd dream. "
    "Then suddenly I hear a loud hiss."
    play sound test
    show text '{size=72}"This will be your test !"{/size}' at text_effect
    
    $ renpy.pause()

    "test test" #small to big text effect 
    "NOOoooo!" #glitch effect
    stop music fadeout 2
    jump badclassroom


label badclassroom:

    play music "waltznchopin.mp3" fadein 0.3
    scene bg classroom at default_pos, default_size
    "AAAAAH!"
    teacher "Alright, that's it for today. Don't forget your test and homework tomorow."
    "Teacher pauses and faces me"
    teacher "Welcome back to earth. How many stars did you count?"
    pause 1
    scene black 
    
    play sound lost
    
    "Thank you for playing!"

    menu:
        "Would you like to make the test?"

        "yes":
            jump quiz
        "no":
            ""
    pause 2
    return


label goodclassroom:
    play music "waltznchopin.mp3" fadein 0.3
    play sound "goodending.mp3" 
    scene bg classroom at default_pos, default_size
    #screen shakes or screen bounces to the left warp
    show lewis
    "A sharp poke in my side jolts me. I squint into the too-bright classroom light, my cheek stuck to the desk."
    lewis "Hey, [player_name], the teacher's coming our way. Wake up! Snap out of it!"
    "I groan, rubbing my eyes."
    "Alright, I’m up."
    "How are you feeling about this test?"
    "He leans in so close I can smell his shampoo."
    lewis "Feel like what? I feel like teacher should cancel this test. That's what."
    "Me? I actually feel like I got this one in the bag for once"
    "I beamed. He freezes."
    lewis "What ?! you slept the entire class period though"
    "I know."


    scene black with dissolve
    hide lewis
    play sound won
    "Thank you for playing!"

    menu:
        "Would you like to make the test?"

        "yes":
            jump quiz
        "no":
            ""
    pause 2


label quiz:
    default correct_answer = 0
    default questions = 7
    #change scenery to following day future dev

    scene bg classroom at default_pos, default_size
    show smitzel at char_pos, char_size, center

    menu: 
        "When did the French Revolution begin?"

        "1776":
            ""
        "1789":
            $ correct_answer += 1

        "1799":
            ""
        "1815":
            ""




    menu:
        "who was the king of France at the start of the Revolution?"
        
        "Louis XIV":
            ""
        "Jean II":
            ""
        "Louis XVI":
            $ correct_answer += 1

        "Jean VI":
            ""
    menu: 
        "Which privelege did the clergy and nobility enjoy before the revolution?"

        "Right to vote":
            ""

        "Exemption from taxes":
            $ correct_answer += 1

        "Freedom to own businesses":
            ""

        "Universal suffrage":
            ""
    

    menu:

        "What event is considered the start of the French Revolution?"

        "The Tennis Court Oath":
            ""

        "The Storming of Bastille":
            $ correct_answer += 1

        "The Reign of Terror":
            ""

        "The execution of Louis XVI":
            ""


    menu:
        "What was the Tennis Court Oath?"
        
        " A promise by the king to reform taxes":
            ""

        "A treaty signed with Austria":
            ""

        "A pledge by the Third Estate not to disband until a constitution was created":
            $ correct_answer += 1

    menu:
        "During the Reign of Terror, who was safe from the guillotine?"

        "No one":
            $ correct_answer += 1

        "the nobility":
            ""

        "only Matthieu":
            ""


    menu:   
        "Which goal was NOT stated in the 'slogan of the Revolution'?"


        "liberty":
            ""

        "equality":
            ""

        "justice":
            ""

        "brotherhood":
            $ correct_answer += 1
    
    $ score = int((correct_answer / questions) * 100)
    if correct_answer == questions:
        hide smitzel fadeout 0.5
        show trophy at truecenter, shake  # Shows the trophy image centered on the screen

        "Whoa, you got every question right!"
        "Are you secretly Maximilien Robespierre in disguise? Or maybe you’ve just been reading Rousseau under the covers. Either way, you’re a revolutionary mastermind!"

        
    elif correct_answer > 3:
        #"Woohoo congratulations you got {correct_answer}/ {questions}!"
        "Woohoo, you got a score of [score]!"
        "Hey, not bad! You got about most of them correct, looks like you’d hold your own in the National Assembly. "
        "Want to try again and see if you can beat your score?"
    
    else:
        "You got a score of [score]"
        "Hey, don’t worry! Even the greatest heroes have off days. Ready for another round? I’ll be here waving my tricolor flag for you!"


    pause 1
















#thanks for playing[player_name]

    return
