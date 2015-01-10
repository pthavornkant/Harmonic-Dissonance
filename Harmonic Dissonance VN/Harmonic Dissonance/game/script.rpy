# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image lawche_f = "lawche_full.png"
image lawche_n = "lawche_neutral.png"
image lawche_s = "lawche_shock.png"
image lawche_v = "lawche_vibrant.png"
image lawche_i = "lawche_irritated.png"
image lawche_a = "lawche_angry.png"
image lawche_h = "lawche_happy.png"
image lawche_n_f = im.Flip("lawche_neutral.png", horizontal=True)
image lawche_s_f = im.Flip("lawche_shock.png", horizontal=True)
image lawche_v_f = im.Flip("lawche_vibrant.png", horizontal=True)
image lawche_h_f = im.Flip("lawche_happy.png", horizontal=True)
image lawche_i_f = im.Flip("lawche_irritated.png", horizontal=True)
image lawche_a_f = im.Flip("lawche_angry.png", horizontal=True)

image fiosi_f = "fiosi_full.png"
image fiosi_h = "fiosi_happy.png"
image fiosi_h_f = im.Flip("fiosi_happy.png", horizontal=True)

image tasia_f = "tasia_full.png"

image archie_f = "archie_full.png"
image archie_h = "archie_happy.png"
image archie_l = "archie_laugh.png"
image archie_b = "archie_blink.png"
image archie_h_f = im.Flip("archie_happy.png", horizontal=True)
image archie_l_f = im.Flip("archie_laugh.png", horizontal=True)
image archie_b_f = im.Flip("archie_blink.png", horizontal=True)

image pomme_f = "pomme_full.png"
image pomme_h = "pomme_happy.png"
image pomme_p = "pomme_pouty.png"
image pomme_a = "pomme_angry.png"
image pomme_h_f = im.Flip("pomme_happy.png", horizontal=True)
image pomme_p_f = im.Flip("pomme_pouty.png", horizontal=True)
image pomme_a_f = im.Flip("pomme_angry.png", horizontal=True)

image dog = "dog.png"
image rooster = "rooster.png"
image fox = "fox.png"

image inside = "realcircusbw.jpg"
image outside = "c1illust.jpg"
image tasia_show = "c1illustbottom.jpg"
image grounds = "c1grounds.jpg"

image tsuda = "tsuda2.png"
image dfm = "yuuta.png"


# Declare characters used by this game.
define Lawche = Character('Lawche', color = "#8b0000")
define Fiosi = Character('Fiosi Bando', color = "#000000")
define Archie = Character('Archie', color = "#daa520")


# List of Color Values
# http://www.renpy.org/wiki/renpy/doc/cookbook/SVG_color_names
# Quick Summary of used colors...
# #daa520 = goldenrod, #8b0000 = dark red, #deb887 = dark brown
# #000000 = black

# Positioning Notes
# (xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5) = Far right position. (Right above text box)
# Position(xpos = 0.5, xanchor = 0.5, ypos = 0.55, yanchor = 0.5) = Centered for full images.
# (xpos = 0.12, xanchor=0.5, ypos=0.61, yanchor=0.5) = Far left position. (Right above text box)

# The game starts here.
label start:

    stop music fadeout 1.0
    scene grounds with fade
    "Chapter 1"

    #Introduction
    "???" "Today, the circus is in town. And today, my job begins as well."
    "???" "Make no mistake though, I'm no circus performer."
    "???" "I can't walk a tightrope while holding a flaming rod."
    "???" "Nor can I fit myself into an unimaginably tiny car with several other people." 
    "???" "I’m no ringmaster, or any sort of acrobat, but I do have business with the circus."

    "???" "I work for the government of the country of Rubato as a {b}rehabilitator.{/b}"
    "???" "My job is to get certain “abnormal people” back into being functional members of society."

    show dfm at right
    show tsuda at left

    "???" "These abnormal people would be those who underwent illegal experimentation involving {b}synth-tech,{/b}"
    "???" "a technological development that’s been taking our country by storm for its’ ability to"
    "???" "connect with our conscious and unconscious thoughts."
    
    hide dfm
    hide tsuda
    
    "???" "Synth-tech all started with plants and animals. The first successful ones assisted in understanding them,"
    "???" "allowing them to have machines speak for them when they had any biological needs."
    "???" "A plant could ask to be watered, pets could ask to be fed or played with."
    "???" "Once robotic limbs were attached to plants so that they could water themselves, "
    "???" "people started getting excessively creative. And so, many unqualified so-called 'scientists'"
    "???" "began to attempt to experiment with synth-tech’s applications."
    "???" "Human synth-tech research was required by law to be under government supervision," 
    "???" "but seeing as how I have my job today, people listened as well as you’d expect them to have." 
    "???" "Long story short, their experiments were colossal failures." 
    "???" "Now we’ve got many people displaced by synth-tech, and this circus housed three such people for me to assist."
    
    show lawche_f at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.55, yanchor = 0.5)
    
    Lawche "I'm agent Lawche. It'll be some time before I can actually meet with my patients."
    Lawche "But I suppose I can read up on information about them while they perform."
    Lawche "For now though, it seems like there's quite a line for this circus."
    
    hide lawche_f

    scene outside with fade

    #Outside of the R.E.A.L.
    Lawche "{i}Quite a crowd. People of all ages and types too. Families, couples, even some loners.{/i}"
    Lawche "{i}Though I doubt those others who came here alone are here for business.{/i}"
    
    "Loud Ringmaster" "C’mon up! This way to the finest troupe you’ll ever see! We are the Resounding Exciting Ardent Legato! Our acts are full of thrills... and very real danger. Gyahahaha!"
    
    show lawche_n at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}Something about that ringmaster seems oddly intimidating.{/i}"
    "Circus Advertisers" "Go ahead, take a flier! See what the R.E.A.L. is all about!"
    Lawche "{i}This is a rather gaudy looking flier. It seems the main act takes up most of it too.{/i}"
    "Flier" "THE HIGH FLYING DAREDEVIL WHO DEFIES DEATH!! SERENE SILVER BEAUTY: TASIA DEVOIR!!"
    "Flier" "As she soars through the air, these gun drones train their aim upon her!" 
    "Flier" "Should she accidentally slip up, these drones shall fire upon her simultaneously!"
    "Flier" "Yet without fear, she dances through the air in a breath-taking silence!"
    "Flier" "It's said that those truly captured by her performance can hear a faint sound... the “Fantasia Melody!”"
    "Flier" "Any couple that can hear it will surely be fated for a successful love life!”"
    Lawche "{i}I suppose that's one way to get lovestruck teens and thrill seekers to visit your circus.{/i}"
    Lawche "{i}The rest of this flier doesn't seem nearly as interesting though.{/i}"
    hide lawche_n
    
    show lawche_s at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}... “The Great Storyteller Archie!”? This circus has a storyteller?{/i}"
    hide lawche_s
    
    show lawche_n at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}Well, I guess a circus with {b}synth-tech{/b} users wouldn't be all too normal anyway.{/i}"
    hide lawche_n
    
    "Young Child" "Mommy, mommy! Look at the lady! She's juggling knives!"
    "Angry Girl" "Hey! I told you that you're not supposed to do that yet! Your act hasn't been approved!"
    "Knife Juggler" "Haha! Enjoy the show everyone! Looks like I've gotta run!"
    
    show lawche_h at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}Heh. Waiting's not so bad if they've got acts like this to pass the time.{/i}"
    hide lawche_h
    

    scene inside with dissolve

    #During the Show

    show lawche_v at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}Inside at last! Finally, a chance to sit down and review my patients.{/i}"
    Lawche "{i}I'll just sit somewhere in the back... there. Now I can read in peace.{/i}"
    hide lawche_v
    
    #Fiosi's Data
    show lawche_n at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    "Document Set #1" "Patient 1: Fiosi Bando. Former up and coming heir to the Bando family mafia."
    "Document Set #1" "The Bando mafia was often involved in trafficking illegal goods."
    "Document Set #1" "Intel states they sold leaked Synth-tech development tools."
    "Document Set #1" "A crackdown on the Bando mafia led to the end of Fiosi's ambitions."
    "Document Set #1" "However, during the crackdown, Fiosi was discovered to have had illegal experiments conducted on himself."
    "Document Set #1" "The nature of his synth-tech is still unknown, but it is known that it causes him issues."
    "Document Set #1" "Fiosi suffers from what appears to be severe anxiety attacks due to the malfunction of his synth-tech."
    "Document Set #1" "Be advised that the rest of the R.E.A.L. is made up of ex-Bando mafia as well."
    "Document Set #1" "Fiosi is an incredibly intimidating individual, and he is aggressive to boot."
    "Document Set #1" "Yet, since the fall of his mafia, he has become the ringleader of the R.E.A.L."
    "Document Set #1" "Due to the circus' wild popularity, it appears he is honestly turning over a new leaf."
    "Document Set #1" "Rehabilitate Fiosi Bando. Curing him of his synth-tech is a top priority."
    hide lawche_n

    show fiosi_f at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.55, yanchor = 0.5)
    Fiosi "ARE..."
    Fiosi "YOU..."
    Fiosi "READY!?"
    
    "Audience" "*cheers & applause*"

    show lawche_s at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}He definitely brings the hype.{/i}"
    hide lawche_s
    
    show lawche_n at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}Ex-mafia huh? So it goes for this kind of job.{/i}"
    Lawche "{i}Seems like the show's starting. The audience can enjoy it.{/i}"
    hide fiosi_f
    Lawche "{i}I've still got two more patients to review after all.{/i}"

    #Tasia's Data
    "Document Set #2" "Patient 2: Tasia Devoir. She lived as an orphan due to the death of her parents after her birth."
    "Document Set #2" "Tasia was kidnapped from an orphanage by the terrorist group Uproar."
    "Document Set #2" "Uproar then conducted synth-tech experimentation on young Tasia for years."
    "Document Set #2" "After years of hunting down Uproar, they were finally eliminated."
    "Document Set #2" "However, after the crackdown, Tasia was nowhere to be found."
    "Document Set #2" "How she suddenly appeared as the R.E.A.L.'s star acrobat is a mystery."
    "Document Set #2" "Regardless, now that we know her whereabouts, it is tantamount that she be rehabilitated."
    "Document Set #2" "Exercise caution, upon interrogating members of Uproar, they revealed Tasia's synth-tech is highly dangerous."
    hide lawche_n

    show lawche_s at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    "Document Set #2" "It is capable of creating powerful soundblasts that may level a city."
    "Document Set #2" "Her synth-tech is also outfitted with gun drones that can shoot down those she deems as hostile."
    "Document Set #2" "However her synth-tech too, has apparently malfunctioned."
    "Document Set #2" "It appears any usage of soundblasts will cause the gundrones to shoot her instead."
    hide lawche_s
    
    show lawche_n at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    "Document Set #2" "Rehabilitate Tasia, and allow her to live without the burdens of her synth-tech."
    "Document Set #2" "It may also be necessary to rehabilitate her socially as well. Her childhood was taken from her."
    "Document Set #2" "We possess no information regarding her personality. Uproar has refused to state anything."

    #Tasia's Performance
    show fiosi_h at Position(xpos = 0.12, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Fiosi "And now for our main act! Our high flying dare devil..."
    Fiosi "The serene silver beauty... ladies and gentlemen, please welcome..."
    Fiosi "TAAAAAAAAASIA DEVOOOOOIIIIR!"
    "Audience" "*crazy cheers and applause intensify*"
    hide lawche_n
    show tasia_f at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.55, yanchor = 0.5)
    Fiosi "She could melt the icy heart of even the most cynical of cynics!"
    Fiosi "Our shining star is here!"

    hide fiosi_h
    hide tasia_f
    
    scene tasia_show with fade
    
    Fiosi "Should she make any errors, the drones aiming at our pretty Tasia will end not only her act, but her life as well!"
    Fiosi "The danger is real, and so too, will be her triumphant performance over all tasks!"
    Fiosi "Please, ladies and gentlemen, give a rousing cheer for our main act, Faaaaaaaan-Tasiaaaaaaa!"
    "Audience" "*hype exands*"
    
    "The crowd gave another resounding cheer full of whistles, squeals and the typical crowd roar of applause. Tasia raised her hand to thank the audience, and then she gestured slightly to notify us that we could stop cheering." 
    "The room was filled with only the sound of the hovering drones. At any moment, it felt like the silence could again be broken by gunfire."
    "I held one hand over the documents and briefcase on my lap and stared intently at the main stage. Tasia gracefully leapt through the air, making no sound of her own." 
    "She spun midair, performing acrobatic stunts, yet still, only the drones made any noise. Even upon landing on a support seemed to refuse to generate even a hint of sound. Tasia’s performance seemed to make the world frictionless and silent, and yet in this world without sound, this world that had death aimed upon her at all times…" 
    "Tasia’s acrobatics made these drones rotate and cause their laser sights to decorate her in lonesome. As the red lights reflected off of her silver outfit, so too did she seem to reflect any feeling of fear or risk. "
    
    "The sound of spotlights flicked on, briefly scaring many members of audience, and focused on Tasia. She swung on a trapeze back and forth until she tossed herself high into the air, and spun higher to the center of the tent’s ceiling, balling herself up as she went."
    "Underneath her, the swing continued to rock back and forth, showing no signs of relenting its’ pendulum pattern. Tasia’s ascent slowed and she unfurled herself stretching her arms out where she seemed to hang midair."
    "She caught onto the swinging trapeze below her successfully. The swing began to loosen and speed its’ way lower with every swing, allowing Tasia to land on the circus floor without hassle. The pre-performance cheering returned, albeit magnified extensively."
    "A few audience members gossiped about how they heard the “Fantasia Melody,” so their love lives were set. I mused to myself what it could possibly mean for someone who came alone and heard it before relinquishing the idea to superstition."
    "Once her act ended, the audience roared back into a crescendo of applause. Such a resounding round of applause, it seemed like it just wouldn't end."
    
    scene inside with fade
    
    #Pomme's Data
    show lawche_h at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}Well, that was certainly worth it.{/i}"
    Lawche "{i}Though if the crowd keeps cheering, this circus will never end. Back to reading for me then.{/i}"
    hide lawche_h
    show lawche_n at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    "Document Set #3" "Patient 3: Pomme Frazz. A runaway who underwent experimentation in youth."
    "Document Set #3" "During the early years of synth-tech development, some groups faked authenticity to gain subjects."
    "Document Set #3" "As a result, Pomme's parents believed one group's claims to be the betterment of child youth."
    "Document Set #3" "She has lived faulty synth-tech throughout her life, and it caused her no harm."
    "Document Set #3" "Her synth-tech appears primarily aesthetic, taking on the appearance of flower petals around her wrists."
    "Document Set #3" "It was originally designed to fire flames, but her synth-tech cannot produce heat."
    "Document Set #3" "Furthermore, the 'flames' she can emit are colorless."
    "Document Set #3" "Nonetheless, these faux flames must be put out like regular flames."
    "Document Set #3" "We allowed her to live with her synth-tech due to the relatively harmless nature of it."
    "Document Set #3" "However, it seems emotional outbursts cause her to lose control of her synth-tech."
    "Document Set #3" "Due to the public nuisance she had caused, we wanted to intervene, but she had run from home by that point."
    "Document Set #3" "She's now in the R.E.A.L. Rehabilitate Ms. Frazz and allow her to resume a normal life."
    "Document Set #3" "Her parents claimed she was relatively normal, aside from Synth-tech issues."

    Lawche "{i}Finally. Someone whose synth-tech won't kill them.{/i}"
    Lawche "{i}Not a kingpin, not someone raised by terrorists, with any luck, she'll be the easiest of the three to handle.{/i}"

    show archie_f at Position(xpos = 0.22, xanchor = 0.5, ypos = 0.55, yanchor = 0.5)
    "???" "Well now ladies and gentlemen, I'm glad you've enjoyed the show thus far!"
    Lawche "{i}Hm? Isn't that... that other guy from the pamphlet? Archie, was it?{/i}"

    Archie "I know you all fancy us a circus, but I like to think of us as something more refined!"
    Archie "A nomadic entertainment troupe if you will!"
    Archie "But enough of that. It's time for our closing act."
    Archie "So please, I hope you'll all enjoy a bit of my story telling!"
    hide archie_f
    hide lawche_n

    # Archie's Story Segment
    show rooster at Position(xpos = 0.88, xanchor=0.5, ypos=0.58, yanchor=0.5)
    show dog at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.585, yanchor = 0.5)
    Archie "Once upon a time, this Rooster and Dog went off together in pursuit of a better life."
    Archie "Their pasts had given them grief, and thus the Rooster spoke to the Dog:"    
    "Rooster" "A better life awaits us if we work together and move on!"
    "Rooster" "Past the forest lies a pasture where we can rest easy and safely for days."    
    "Rooster" "We’ll have to travel for a bit but we’ll be happy there!’"
    Archie "During their journey they would often sleep out by the forest’s trees. "    
    Archie "Every night, the Rooster would say,"
    "Rooster" "Please look out for me down there, as I’m not too strong by myself! I’ll rest up here!"    
    Archie "The Dog would always grumble, as he never liked the idea of taking orders from the Rooster."
    "Dog" "If something just happens to ignore me and get you, don’t blame me!"    
    Archie "They would repeated this daily routine, and every day, the Rooster would crow its’ morning chant."
    hide dog
    show fox at Position(xpos = 0.14, xanchor=0.5, ypos=0.515, yanchor=0.5)
    Archie "But one day, a fox appeared..."
    Archie "The Fox heard the Rooster’s crowing and went up to him."
    "Fox" "How... delectable your voice is! Heheh, come with me Rooster! I can take you to the pasture!"
    "Fox" "You’ll be able to sing to your heart’s content, and your life will rest easy forever!"
    "Children in the Audience" "He’s lying! The fox just wants to eat you! Be careful Mr. Rooster!"
    Archie "So, the Rooster told the Fox:"
    "Rooster" "That sounds like a great idea, but I believe I would need to prepare!"
    "Rooster" "Could you come around to the other side of the tree first?"
    "Fox" "Certainly!"
    Archie "However when the Fox turned to the other side of the tree, he woke the Dog!"
    show dog at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.585, yanchor = 0.5)
    Archie "The Dog, feeling threatened attacked the Fox and drove him away!"
    hide fox
    Archie "The Dog then told the rooster:"
    "Dog" "It appears that I have not neglected my duties, eh, Rooster?"
    Archie "The Rooster smiled, and from that day on, the two became friends, continuing their search of the pasture."
    hide dog
    hide rooster
    Archie "The end."

    "Audience" "*unintelligble gibberish of cheer*"
    "Audience" "*wild rioting of cheer*"
    "Audience" "*cheersm8te*"
    
    #Chapter 1 End
    show lawche_s at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "This... cheering... looks like it could go on for a while."
    hide lawche_s
    show lawche_n at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}Oh well. Seems like the performers are done. I'll head around back to go meet them.{/i}"
    
    
    "Today the circus is in town. Tomorrow it won't be. And neither will I."
    hide lawche_n

    jump ch2

    return
