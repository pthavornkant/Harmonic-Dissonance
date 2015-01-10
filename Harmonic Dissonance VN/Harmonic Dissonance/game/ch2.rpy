# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# refer to ch1(script.rpy) for previous definitions


# Declare characters used by this game.
# Lawche, Fiosi, and Archie already defined

label ch2:
    
    stop music fadeout 1.0
    scene grounds with fade
    
    "Chapter 2"

    #Meeting Archie
    show lawche_n_f at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "{i}They must still be wrapping things up in there. Doesn't seem like there's anyone out here.{/i}"
    hide lawche_n_f
    show archie_h_f at Position(xpos = 0.55, xanchor=0.5, ypos=0.63, yanchor=0.5) with dissolve
    show lawche_s_f at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Archie "Yo! Haven’t seen you around here before, you the {b}rehabilitator{/b} guy?"
    hide lawche_s_f
    show lawche_s at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "!"
    hide archie_h_f
    show archie_l_f at Position(xpos = 0.55, xanchor=0.5, ypos=0.63, yanchor=0.5)
    Archie "Woops, looks like I surprised you!"
    show lawche_n at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "Ahem. Yes, you are correct. Nice to meet you, I’m Agent Lawche. You’re Archie, if I’m not mistaken."
    show archie_h_f at Position(xpos = 0.55, xanchor=0.5, ypos=0.63, yanchor=0.5)
    Archie "And you are not! So you're mister {b}rehabilitator,{/b} huh?"
    Archie "A guy came by the other day telling us you'd be coming. Though he didn't talk to me much."
    Archie "So who're you gonna be giving the ol' treatment, doc Lawche?"
    Lawche "Well, three people from this circ-"
    show archie_b_f at Position(xpos = 0.55, xanchor=0.5, ypos=0.63, yanchor=0.5)
    Archie "The R.E.A.L."
    Lawche "Right... well, yes, within the R.E.A.L."
    hide archie_b_f
    show archie_h_f at Position(xpos = 0.55, xanchor=0.5, ypos=0.63, yanchor=0.5)
    Lawche "One is your Ringmaster, one Fiosi Bando."
    Lawche "The second is your star acrobat, Miss Tasia Devoir."
    Lawche "The last… well, I have yet to see her, I don’t think she was in the performance either, Miss Pomme Frazz."
    Archie "Those three? Is there something wrong with them?"
    Lawche "Well of course. {b}Synth-tech.{/b} Illegal {b}synth-tech{/b} at that."
    Archie "Other than the illegal part, it doesn’t sound too wrong."
    hide archie_h_f
    show archie_l_f at Position(xpos = 0.55, xanchor=0.5, ypos=0.63, yanchor=0.5)
    Archie "Oh! You know there’s a joke in there somewhere about illegal integration."
    Lawche "When it was just communicating with plants and pets, I didn’t think there was anything wrong either."
    hide archie_l_f
    show archie_h_f at Position(xpos = 0.55, xanchor=0.5, ypos=0.63, yanchor=0.5)
    hide lawche_n
    show lawche_a at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "But Synth-tech on people? It's not like prosthetics. People tried to make cyborgs a reality!"
    Lawche "As far as I know, only the government’s got a decent grip on the situation too."
    Lawche "They were smart to have laws to regulate it, but you always have those who break laws..."
    Archie "Well I can't say I particularly agree or disagree with any of that!"
    hide lawche_a
    show lawche_i at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Archie "But anyway, Lawchey, no matter how attached people are to their technology, it’s still just equipment for us."
    hide lawche_i
    show lawche_n at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Archie "And we’ll still be human regardless."
    Archie "Hopefully your distaste for {b}synth-tech{/b} doesn't cause you to forget that!"
    hide lawche_n
    show lawche_h at Position(xpos = 0.88, xanchor=0.5, ypos=0.61, yanchor=0.5)
    Lawche "I would hope not. Otherwise, that'd be rather unprofessional of me, no?"
    Archie "Good, good! The performers should be out soon, so you'd best ready yourself too."
    show archie_l_f at Position(xpos = 0.55, xanchor=0.5, ypos=0.63, yanchor=0.5)
    Archie "After all, now is when you put on the show for us right?"
    
    
   
    
    return