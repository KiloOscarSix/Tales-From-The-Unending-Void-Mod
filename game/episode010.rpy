
image ep010_acolyte_sucking_wide_alt_closeup = Movie(play="movies/ep010/ep010_acolyte_sucking_wide_alt.webm")
image ep010_acolyte_sucking_wide_alt = Movie(play="movies/ep010/ep010_acolyte_sucking_wide.webm")
image ep010_celine_fuck_alt = Movie(play="movies/ep010/ep010_celine_fuck_alt.webm")
image ep010_celine_hj = Movie(play="movies/ep010/ep010_celine_hj.webm")
image ep010_erylin_naked_fucking = Movie(play="movies/ep010/ep010_erylin_naked_fucking.webm")
image ep010_erylin_naked_lick_alt_closeup = Movie(play="movies/ep010/ep010_erylin_naked_lick_alt_closeup.webm")
image ep010_erylin_naked_lick_alt = Movie(play="movies/ep010/ep010_erylin_naked_lick_alt.webm")
image ep010_erylin_naked_suck = Movie(play="movies/ep010/ep010_erylin_naked_suck.webm")
image ep010_erylin_naked_swap_fuck_alt = Movie(play="movies/ep010/ep010_erylin_naked_swap_fuck_alt.webm")
image ep010_tentacles_fuck_alt = Movie(play="movies/ep010/ep010_tentacles_fuck_alt.webm")
image ep010_tentacles_fuck = Movie(play="movies/ep010/ep010_tentacles_fuck.webm")
image ep010_vess_penetrate_closeup_alt = Movie(play="movies/ep010/ep010_vess_penetrate_closeup_alt.webm")
image ep010_vess_penetrate_closeup_rub = Movie(play="movies/ep010/ep010_vess_penetrate_closeup_rub.webm")
image ep010_vess_pussy_fucking_closeup = Movie(play="movies/ep010/ep010_vess_pussy_fucking_closeup.webm")
image ep010_vess_fucking = Movie(play="movies/ep010/ep010_vess_pussy_fucking.webm")
image ep010_vess_pussy_penetrate_closeup_anim = Movie(play="movies/ep010/ep010_vess_pussy_penetrate_closeup.webm")
image ep010_vess_pussy_penetrating_closeup_alt = Movie(play="movies/ep010/ep010_vess_pussy_penetrating_closeup_alt.webm")
image ep010_vess_sucking_closeup = Movie(play="movies/ep010/ep010_vess_sucking_closeup.webm")
image ep010_vess_sucking = Movie(play="movies/ep010/ep010_vess_sucking.webm")
image ep010_ziv_naked_cock_suck_alt = Movie(play="movies/ep010/ep010_ziv_naked_cock_suck_alt.webm")
image ep010_ziv_naked_doggy_wide = Movie(play="movies/ep010/ep010_ziv_naked_doggy.webm")
image ep010_ziv_naked_fuck_alt_wide = Movie(play="movies/ep010/ep010_ziv_naked_fuck_alt.webm")
image ep010_ziv_naked_pussy_finger_alt_closeup = Movie(play="movies/ep010/ep010_ziv_naked_pussy_finger_alt_closeup.webm")
image ep010_ziv_naked_pussy_finger_alt = Movie(play="movies/ep010/ep010_ziv_naked_pussy_finger_alt.webm")
image ep010_ziv_naked_pussy_lick = Movie(play="movies/ep010/ep010_ziv_naked_pussy_lick.webm")
image ep010_ziv_naked_sucking_alt_closeup = Movie(play="movies/ep010/ep010_ziv_naked_pussy_lick.webm")
image ep010_ziv_naked_sucking_alt = Movie(play="movies/ep010/ep010_ziv_naked_sucking_alt.webm")


label episode010:
    $ save_name = "Episode 10"

    $ ep010_ra_kiss = False
    $ ep010_ce_truth = False
    $ ep010_ce_love = False
    $ ep010_ce_monogamy = False
    $ celine_romance_ended = False
    $ ep010_na_challenge = False
    $ ep010_na_convince = False
    $ ep010_na_apology = False
    $ ep010_invitation_destroy = False
    $ ep010_warrior_alliance = False
    $ ep010_warrior_alliance_agreed = False
    $ ep010_priest_alliance = False
    $ ep010_priest_alliance_agreed = False
    $ ep010_no_alliance = True
    $ ep010_er_insult = False
    $ ep010_erylin_alliance_options = False
    $ ep010_rahia_alliance_options = False
    $ ep010_er_keo_sex = False
    $ ep010_keodele_fucked = False
    $ ep010_erylin_fucked = False
    $ ep010_erylin_fucked_last = False
    $ ep010_keodele_creampie = False
    $ ep010_erylin_creampie = False
    $ ep010_erylin_talk = False
    $ ep010_rahia_talk = False
    $ ep010_lilly_talk = False
    $ ep010_raene_talk = False
    $ ep010_celine_talk = False
    $ ep010_vess_talk = False
    $ ep010_vess_creampie = False
    $ ep010_vess_love = True
    $ ep010_ziv_talk = False
    $ ep010_ziv_cock_sucked = False
    $ ep010_ziv_pussy_licked = False
    $ ep010_ziv_swallow_received = False
    $ ep010_ziv_facial_received = False
    $ ep010_ziv_hj_given = False
    $ ep010_ziv_creampie = False
    $ ep010_aven_talk = False
    $ ep010_rahia_talk = False
    $ ep010_rahia_truth = False
    $ ep010_rahia_decline = False
    $ ep010_erylin_decline = False
    $ ep010_hunt_investigate = False
    $ ep010_hunt_rescue = False
    $ ep010_athryn_leave = False
    $ ep010_ce_anal = False
    $ ep010_ce_creampie = False
    $ ep010_ce_creampie_second = False

    play music "music/desolate.ogg" fadeout 4 fadein 1.0

    centered "{=chapter_heading}EPISODE 10{/=chapter_heading}"

    $ man_name = "Admiral"
    $ man_portrait = "side_admiral"

    $ woman_name = "Board Member"
    $ woman_portrait = "side_woman"
    $ woman2_name = "Board Member"
    $ woman2_portrait = "side_woman"

    scene ep010_board_admiral_alt with dissolve
    call location_screen (__("Luna"), True) from _call_location_screen_34

    man "Report."
    scene ep010_board with dissolve
    bl "I've tracked the boy and his crew to a planet called Barranthis."
    bl "They seemed to have pissed off a local crime lord here and then vanished without a trace into the Helluvian Belt, a local asteroid field."
    scene expression eye_blink("images/ep010/ep010_board_member") with dissolve
    woman "That name sounds familiar."
    scene expression eye_blink("images/ep010/ep010_board_member_alt") with dissolve
    woman2 "It does."
    woman2 "ConVitæ has a facility there."
    woman2 "I'd say it's very likely they were captured and taken to the ConVitæ research station."
    scene expression eye_blink("images/ep010/ep010_board_member") with dissolve
    woman "Could you check if the facility has any records of prisoners matching the description of the fugitives, Doctor Rivas?"
    $ riv_name = "Dr. Rivas"
    scene expression eye_blink("images/ep010/ep010_board_doctor") with dissolve
    riv "Of course."
    scene expression eye_blink("images/ep010/ep010_board_member_alt") with dissolve
    woman2 "It would be a stroke of luck if they're still held captive."
    scene expression eye_blink("images/ep010/ep010_board_member") with dissolve
    woman "So far, nothing has gone to plan in this whole sordid affair, I wouldn't count my blessings just yet."
    scene expression eye_blink("images/ep010/ep010_board_doctor") with dissolve
    riv "I have word from the director of the facility."
    riv "Apparently, they've dealt with a breakout in recent weeks."
    riv "Several of the escapees match our descriptions."
    scene expression eye_blink("images/ep010/ep010_board_member") with dissolve
    woman "Tell me they were pursued?"
    scene expression eye_blink("images/ep010/ep010_board_doctor") with dissolve
    riv "Negative."
    scene expression eye_blink("images/ep010/ep010_board_member_alt_angry") with dissolve
    woman2 "Why the fuck not?!"
    scene expression eye_blink("images/ep010/ep010_board_doctor") with dissolve
    riv "Their escape was deemed an acceptable loss and those involved have been reprimanded accordingly."
    scene expression eye_blink("images/ep010/ep010_board_member") with dissolve
    woman "So we're in the dark again?!"
    scene ep010_board with dissolve
    bl "I might be able to shed some light on their whereabouts."
    scene expression eye_blink("images/ep010/ep010_board_admiral") with dissolve
    man "Continue your report."
    scene ep010_board with dissolve
    bl "The fugitives have contacted a local forger here on Barranthis."
    bl "He has been quite cooperative after I persuaded him to talk."
    bl "Apparently, he forged invitations and identity papers for them."
    scene expression eye_blink("images/ep010/ep010_board_member_alt") with dissolve
    woman2 "Invitations to what?"
    scene ep010_board with dissolve
    bl "An exclusive party."
    scene expression eye_blink("images/ep010/ep010_board_member") with dissolve
    woman "Why on earth would they want to go to a party?"
    scene ep010_board with dissolve
    bl "Well, the fact that the host was Ranimo Cetruvar should probably answer that question."
    scene expression eye_blink("images/ep010/ep010_board_member_alt_serious") with dissolve
    woman2 "There's a name I don't want to hear."
    woman2 "Fuck that old snake."
    scene expression eye_blink("images/ep010/ep010_board_member") with dissolve
    woman "What did they want with Cetruvar?"
    scene ep010_board with dissolve
    bl "I'm not certain."
    scene expression eye_blink("images/ep010/ep010_board_admiral") with dissolve
    man "An attack on the Sovereignty perhaps?"
    scene expression eye_blink("images/ep010/ep010_board_member_doubt") with dissolve
    woman "Are those kids even capable of that?"
    scene ep010_board_admiral with dissolve
    man "Don't be naive."
    scene ep010_board with dissolve
    bl "I don't know why they would want to seek out Cetruvar, but this suddenly seems like the best lead."
    scene expression eye_blink("images/ep010/ep010_board_admiral") with dissolve
    man "Yes, track down Cetruvar and proceed from there."
    scene ep010_board with dissolve
    bl "Understood."
    bl "Kvi out."
    scene expression eye_blink("images/ep010/ep010_board_member") with dissolve
    woman "At last we're making some progress."

    $ ag_name = "Board Member"
    $ agust_portrait = "side_man"

    scene ep010_board_unknown with dissolve
    ag "Progress?!{w} You call that fucking progress?!"
    ag "You've been on this wild goose chase for almost a year now."
    scene ep010_board_unknown_alt with dissolve
    ag "You assured me this would be resolved quickly."
    ag "Just like you assured me the training mission on Lanan was a piece of cake."
    scene ep010_board_fist with vpunch
    ag "This has cost me my most valuable investment and the only thing we've done up until now is chase my good-for-nothing excuse of a son across the galaxy!"
    scene expression eye_blink("images/ep010/ep010_board_chairwoman_angry") with dissolve
    $ vel_name = "Chairwoman"
    vel "Calm down, Agust!"
    $ ag_name = "Agust"
    $ agust_portrait = "side_agust"
    scene expression eye_blink("images/ep010/ep010_board_agust") with dissolve
    ag "No.{w} I'm fed up with this incompetent shitshow."
    ag "It was your idea to have Eva enlist in the Academy."
    scene expression eye_blink("images/ep010/ep010_board_doctor_serious") with dissolve
    riv "The Academy was the best way to monitor her situation and perform the required medical test without raising suspicion."
    scene expression eye_blink("images/ep010/ep010_board_agust") with dissolve
    ag "She could have just been locked up in the family estate under constant guard and nobody would have been none the wiser."
    ag "Instead she had to risk her life going through that stupid training and-"
    scene expression eye_blink("images/ep010/ep010_board_chairwoman_angry") with vpunch
    vel "ENOUGH!"
    if game.is_special:
        vel "May I remind you, Agust, that your youngest daughter was the only reason you were able to become a member of the board."
    elif True:
        vel "May I remind you, Agust, that Eva was the only reason you were able to become a member of the board."
    scene expression eye_blink("images/ep010/ep010_board_chairwoman_serious") with dissolve
    vel "We are all aware of the potential value Eva represents and we will get her back, make no mistake about that."
    vel "I know you're deeply unhappy with how the situation was handled."
    vel "Commander Szuzume never should have returned to the Academy after the events on Lanan."
    vel "She and her chain of superiors have been dealt with."
    vel "Now, I'm not interested in dwelling on past business."
    scene expression eye_blink("images/ep010/ep010_board_chairwoman_smile") with dissolve
    vel "The Bloodhound is on the trail and it's the best lead we've had in months."
    vel "I don't care if we have to blow up a planet to retrieve that girl, but we will get her back."

    python:
        if game.is_special:
            codex_agust = update_codex_entry(codex_agust, None,
                [
                    __("Agust Algerone Arlington Valenmann de Lonval, wealthy CEO of the trading and manufacturing company VLCo, father to [p_name], Lilly and Eva."),
                    __("Your father has been a secret member of the Sovereignty Council for an unknown period of time, his membership hinging on the perceived value of his daughter Eva.")
                ],
            )
        else:
            codex_agust = update_codex_entry(codex_agust, None,
                [
                    __("Agust Algerone Arlington Valenmann de Lonval, wealthy CEO of the trading and manufacturing company VLCo, father to [p_name]."),
                    __("Your father has been a secret member of the Sovereignty Council for an unknown period of time, his membership hinging on the perceived value of your friend Eva.")
                ],
            )

    play music [ "music/the-spaces-between.ogg", "music/tears-in-rain.ogg", "music/beautiful-oblivion.ogg" ] fadeout 4 fadein 1.0

    scene black with fade

    scene ep010_citadel with dissolve
    "The following days were mostly filled with us trying to get more information on the Hunt that was called."
    "What we knew already was that potential champions had to gather in the courtyard on the day of the Hunt."
    "Anybody could join, but most champions were sponsored by either the priest or the warrior caste."
    if game.is_special:
        "Aunt Nadya had promised to grill Caese about tradition and the girl had agreed to meet us to talk some details."
    elif True:
        "Nadya had promised to grill Caese about tradition and the girl had agreed to meet us to talk some details."
    scene ep010_library with dissolve
    "I thought I was the first to arrive at the library."
    "Thim hadn’t exaggerated about its size and the fact that it was stocked liberally with printed books."
    scene ep010_library_na with dissolve
    if game.is_special:
        "A woman sat at a table amidst a mountain of books, and I had to look twice to determine it was Aunt Nadya."
        c "You look beautiful today, Aunt Nadya, that outfit looks great on you."
    elif True:
        "A woman sat at a table amidst a mountain of books, and I had to look twice to determine it was Nadya."
        c "You look beautiful today, Nadya, that outfit looks great on you."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup_smile") with dissolve
    na "Thank you."
    na "Unfortunately, my other clothes were beyond repair."
    if ep009_na_breasts:
        scene expression eye_blink("images/ep010/ep010_library_na_closeup_doubt") with dissolve
        na "Listen, [p_name_short], could we have a talk about what happened back in that cavern?"
        c "Sure thing."
    scene ep010_library_na_ca with dissolve
    "There wasn’t room for any more conversation, because Caese had arrived at the library."
    na "Good of you to come, Caese."
    cae "Anytime."
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup") with dissolve
    cae "I heard you were interested in joining the Hunt?"
    c "Maybe."
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup_serious") with dissolve
    cae "Well, despite all the heroic talk, the Hunt is very dangerous."
    cae "People come back changed, or they don’t come back at all."
    c "Here I was hoping it would be a fun little excursion..."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup_smile") with dissolve
    na "These things never are."
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup") with dissolve
    cae "Champions are assigned a calgound."
    c "A what?"
    scene ep010_library_na_ca_closeup with dissolve
    na "You’ve seen Erylin ride one."
    c "I’m to ride one of those massive wolf-lion monstrosities?"

    python:
        codex_calgound = add_codex_entry(
            Codex,
            __("Species"),
            __("Calgound"),
            [
                __("Calgounds are a species native to Erigone and used primarily by the Acarhyn populace for hunting in the jungle. The calgound is also the required mount to partake in the so-called ceremonial Hunts."),
                __("The animals are best described as looking like a cross between a lion and a wolf. They're wild animals, but with the proper training they can be ridden like horses."),
            ]
        )

    scene expression eye_blink("images/ep010/ep010_library_ca_closeup") with dissolve
    cae "Yes, that’s a requirement."
    cae "Besides, you wouldn’t get through the jungle without one."
    c "A tank probably could get through?"
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup_smile") with dissolve
    cae "That’s against the rules."
    c "Of course, the rules..."
    c "So, riding a pissed-off monster through the jungle."
    c "What else?"
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup") with dissolve
    cae "All champions ride out at the same time and return once the Prey has been slain."
    cae "During the Hunt, there are very few rules and some of the Hunters abuse that fact."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup") with dissolve
    na "Could you give an example?"
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup_serious") with dissolve
    cae "Some Hunters go after the competition first to finish them off."
    c "Level the playing field, so to speak."
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup") with dissolve
    cae "There’s one example of a Hunt where all the champions were killed before the remaining Hunter perished in the claws of the Prey."
    c "Poetic justice."
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup_smile") with dissolve
    cae "Quite."
    c "I assume I have to kill the beast with some unwieldy Acarhyn sword?"
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup") with dissolve
    cae "Actually no, the choice of weapon is yours."
    c "Great, although they took all of our weapons after we buried ourselves into the surface of your planet."
    cae "A champion has the right to request any weapon they deem necessary for the Hunt."
    c "In that case, I might just order that tank to do the dirty work for me."
    cae "The only rule is that the weapon can be carried and wielded solely by the Hunter."
    c "No tank then, but I’d be equally happy with a rocket launcher."
    c "Any other advice you can give me?"
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup_serious") with dissolve
    cae "Yes, the Hunt isn’t over after you’ve slain the Prey."
    cae "Only when the Hunter returns with a token of their Victory will the Hunt be called over."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup") with dissolve
    na "As we understand it, most of the champions are sponsored by the priestesses or the warriors."
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup_serious") with dissolve
    cae "Yes, some Hunters are independent, but that comes with several disadvantages."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup") with dissolve
    na "Such as?"
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup") with dissolve
    cae "Sponsored Hunters generally have better weapons and training."
    c "There isn’t much time to train anyway."
    cae "True, but allying with a faction also gives Hunters other benefits."
    cae "Those benefits aren’t exactly in accordance with the rules, but as long as nobody knows about them it’s deemed permissible."
    c "What do you mean exactly, performance-enhancing drugs, or something?"
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup_shock") with dissolve
    cae "Oh, no!{w} No, Hunters sometimes get ambushed in the jungle by unknown forces."
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup") with dissolve
    cae "Many assume they’re members of a faction acting against other Hunters."
    cae "Also, Hunters sponsored by the same faction sometimes work together in the field, which isn’t allowed."
    c "So basically the Hunt is a cheater’s free for all?"
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup_smile") with dissolve
    cae "I’m sure the priest caste wouldn’t agree, but yes."
    c "You know, I wasn’t looking forward to this, but after hearing the nitty gritty details I can safely say I really wish I never heard about the whole fucking thing at all."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup_serious") with dissolve
    na "You could always decide to forgo participating."
    c "I feel like this is the best chance we have to get closer to Eva."
    c "Anyway, thanks a lot for your answers, Caese."
    scene expression eye_blink("images/ep010/ep010_library_ca_closeup_smile") with dissolve
    cae "You’re welcome."
    na "I hope it helps us to be better prepared."
    cae "If you need anything else, just let me know."
    scene ep010_library_na_ca_alt with dissolve
    "Caese left us alone among the many books."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup_serious") with dissolve
    na "I’m serious, [p_name], you don’t have to go on this Hunt."
    na "We could find another way to help Eva."
    c "I don’t see any other option."
    c "Erylin has too much influence over her right now."
    if ep008_commander_sex:
        c "Rahia might be willing to ally with us."
    elif ep009_er_accept or ep009_er_consider:
        c "Then again, she may want to ally with us, to strengthen her power even more."
    elif True:
        c "We’re going to prepare as best we can and cheat our way to the top, like true Acarhyn."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup") with dissolve
    na "Whatever you think is best."
    na "Just be careful."
    c "I will."

    if ep009_na_breasts:
        call ep010_na_talk from _call_ep010_na_talk

    scene ep008_erigone_quarters with dissolve

    menu ep010_citadel_conversations:
        "Visit Erylin" if not ep010_erylin_talk:
            $ ep010_erylin_talk = True
            call ep010_erylin from _call_ep010_erylin
            scene ep008_erigone_quarters with dissolve

            play music [ "music/tears-in-rain.ogg", "music/the-spaces-between.ogg", "music/beautiful-oblivion.ogg" ] fadeout 4 fadein 1.0

            jump ep010_citadel_conversations
        "Visit Rahia" if not ep010_rahia_talk:
            $ ep010_rahia_talk = True
            call ep010_rahia from _call_ep010_rahia
            scene ep008_erigone_quarters with dissolve
            jump ep010_citadel_conversations
        "Visit Raene" if ep008_raene_baths and not ep010_raene_talk:
            $ ep010_raene_talk = True
            call ep010_raene from _call_ep010_raene
            scene ep008_erigone_quarters with dissolve

            play music [ "music/beautiful-oblivion.ogg", "music/tears-in-rain.ogg", "music/the-spaces-between.ogg" ] fadeout 4 fadein 1.0

            jump ep010_citadel_conversations
        "Visit Lilly" if not ep010_lilly_talk:
            $ ep010_lilly_talk = True
            call ep010_lilly from _call_ep010_lilly
            scene ep008_erigone_quarters with dissolve
            jump ep010_citadel_conversations
        "Visit Ziv" if not ep010_ziv_talk and ziv_romance:
            $ ep010_ziv_talk = True
            call ep010_ziv from _call_ep010_ziv
            scene ep008_erigone_quarters with dissolve

            play music [ "music/beautiful-oblivion.ogg", "music/tears-in-rain.ogg", "music/the-spaces-between.ogg" ] fadeout 4 fadein 1.0

            jump ep010_citadel_conversations
        "Visit Aven" if not ep010_aven_talk:
            $ ep010_aven_talk = True
            call ep010_aven from _call_ep010_aven
            scene ep008_erigone_quarters with dissolve
            jump ep010_citadel_conversations
        "Visit Vess" if not ep010_vess_talk and ep009_ve_kiss:
            $ ep010_vess_talk = True
            call ep010_vess from _call_ep010_vess
            scene ep008_erigone_quarters with dissolve

            play music [ "music/beautiful-oblivion.ogg", "music/tears-in-rain.ogg", "music/the-spaces-between.ogg" ] fadeout 4 fadein 1.0

            jump ep010_citadel_conversations
        "Visit Céline" if celine_romance and not ep010_celine_talk:
            $ ep010_celine_talk = True
            call ep010_celine from _call_ep010_celine
            scene ep008_erigone_quarters with dissolve

            play music [ "music/beautiful-oblivion.ogg", "music/tears-in-rain.ogg", "music/the-spaces-between.ogg" ] fadeout 4 fadein 1.0

            jump ep010_citadel_conversations

    if not ep010_warrior_alliance and not ep010_priest_alliance and not ep010_no_alliance:
        "It was time to decide whether I’d become a lone Hunter, or allied myself with one of the factions."
        menu:
            "Warrior caste" if not ep010_rahia_decline:
                $ ep010_warrior_alliance = True
                "Rahia and her warrior caste seemed like the strongest option."
                "I relayed a message to her and got a confirmation not long after."
                "The warrior caste would have my back."
            "Priest caste" if not ep010_erylin_decline:
                $ ep010_priest_alliance = True
                "Erylin and her priestess seemed like the obvious choice for an alliance."
                "I relayed a message to her and got a confirmation not long after."
                "The priest caste would have my back...{w} For now..."
            "Solo" if True:
                $ ep010_no_alliance = True
                "Getting embroiled in Acarhyn politics seemed more lethal than killing the monster in the jungle."
                "Me and my crew had overcome worse odds, so I was confident we could handle the Hunt on our own."

    "After submitting my application for the Hunt, I was told to report to the quartermaster."
    scene ep010_quarter_master with dissolve
    "The woman had her wares laid out on a table, and at first glance, the selection was rather unimpressive."
    c "I assume the better weapons are in the back, or something?"
    $ woman_name = "Quartermaster"
    woman "No, I’m afraid this is the selection you may choose from."
    c "Several swords and a rusty spear?"
    if ep010_no_alliance:
        scene expression eye_blink("images/ep010/ep010_quarter_master_closeup_smile") with dissolve
        woman "Yes."
    elif ep010_warrior_alliance:
        scene expression eye_blink("images/ep010/ep010_quarter_master_closeup_sad") with dissolve
        woman "Erylin’s goons were here earlier and confiscated all the quality weaponry."
    elif True:
        scene expression eye_blink("images/ep010/ep010_quarter_master_closeup_smile") with dissolve
        woman "I’m sure your friends in the priesthood will be able to provide you with something."
    scene ep010_quarter_master with dissolve
    "Thoroughly annoyed, I opted out of taking any of the offered weapons."
    if ep010_priest_alliance:
        "I sincerely hoped Erylin would have some hardware for me."
        "After some inquiries, it turned out the priesthood had nothing to offer either."
        "The warrior caste had confiscated all the quality weaponry, leaving the priest caste with some energy weapons that were little better than what I already carried."
        scene black with fade
        "Clearly this Hunt wasn’t going to be decided by who would carry superior weapons, or so I hoped."
    elif True:
        scene black with fade
        "Clearly this Hunt wasn’t going to be decided by who would carry superior weapons, or so I hoped."

    call ep010_hunt from _call_ep010_hunt

    call ep010_thyia from _call_ep010_thyia

    scene ep010_courtyard_ceremony with dissolve
    "The courtyard was packed with Acarhyn, who stepped reverently aside when I crossed towards the wooden stage."
    if ep010_warrior_alliance:
        scene expression eye_blink("images/ep010/ep010_courtyard_ceremony_rahia") with dissolve
        "Rahia was already waiting for me, a big smile on her face."
        "Taking a deep breath, I walked up the steps to the stage and took my place beside Rahia."
        rah "Ready?"
    elif True:
        scene expression eye_blink("images/ep010/ep010_courtyard_ceremony_erylin") with dissolve
        "Erylin was already waiting for me, a big smile on her face."
        "Taking a deep breath, I walked up the steps to the stage and took my place beside Erylin."
        er "Welcome, are you ready?"
    c "Let’s get this over with."
    call credits from _call_credits
    return

label ep010_na_talk:
    play music "music/affirmations.ogg" fadeout 4 fadein 1.0

    "Nadya’s voice dropped to a whisper, even though the library was mostly deserted."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_doubt") with dissolve
    na "About what happened."
    na "The spores of the mushrooms must have had some peculiar effect..."
    na "I can’t think of any other explanation."
    scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_sad") with dissolve
    na "I wanted you to know what happened was entirely inappropriate and I’m very sorry."
    menu:
        "Challenge her [NadyaPath]" if True:
            $ ep010_na_challenge = True
            c "There’s no need for you to apologize in any way."
            "My response had her taken aback and I took advantage of the stunned silence to get my point across."
            c "I think you’re right that the mushroom spores had an effect on us, but not in the way you’re implying."
            c "The spores didn’t change our desires, but heightened what’s already there."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_fear") with dissolve
            na "Keep your voice down!"
            scene ep010_library_empty with dissolve
            "I don’t think anyone took note of our conversation, but I continued in a more conspiratorial tone."
            scene ep010_library_na_conversation with dissolve
            c "I’d be lying to myself if I told you my behavior in that cave came all out of the blue."
            c "True, I would have never acted on any of the urges I felt if it weren’t for those mushrooms..."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_doubt") with dissolve
            na "What are you saying, [p_name]?"
            c "I’m saying that, ever since we met again on Ryūjin Prime, I’ve felt something for you."
            if game.is_special:
                c "Something other than the love of a nephew for his favorite aunt."
            elif True:
                c "Something other than the love of a boy for his dear friend."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_fear") with dissolve
            na "[p_name_short]!{w} No!{w} Stop!"
            c "Alright, I’ll stop."
            c "But I want to know one thing, do you feel the same way about me?"
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_sad") with dissolve
            na "I..."
            c "I know that the events of that night were not something you just underwent."
            "Nadya looked long and hard at me, her initial panic giving way to resignation."
            "She sighed."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_shy") with dissolve
            na "No, I was completely caught up in what we were doing."
            na "At the time it felt so real and so...{w} good."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_sad") with dissolve
            na "But you know it’s wrong, [p_name_short]."
            if game.is_special:
                na "I’m your aunt, I’ve known you for almost your entire life."
            elif True:
                na "I’ve known you for almost your entire life."
                na "Not only that, I could have been your mother!"
            menu:
                "Convince her [NadyaPath]" if True:
                    $ ep010_na_convince = True
                    c "There’s one thing wrong about this whole situation, and that’s denying the feelings underpinning all this."
                    if ep007_na_truth or ep007_na_embrace:
                        c "I still think of that kiss we shared on Almagest."
                    scene ep010_library_na_conversation with dissolve
                    "Nadya opened and closed her mouth, but no sound came out."
                    "I feared panic would overtake her and that she was about to leave me hanging amidst all those books."
                    scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_shy") with dissolve
                    na "I...{w} I don’t know what came over me that night."
                    na "I should’ve known better than to take advantage of you like that."
                    na "And as I said, we weren’t ourselves in the cave."
                    c "You didn’t take advantage of me, Nadya."
                    c "I’m not a little boy anymore and I know what I want."
                    c "I don’t want to sound harsh, but I feel like you’re denying your own feelings."
                    c "Yes, we’ve known each other for a long time, but that doesn’t weaken our relationship, it deepens it."
                    c "All I know is that, whatever objections there might be, you’re a stunningly attractive woman."
                    scene ep010_library_na_conversation_alt with dissolve
                    "Nadya looked around the library skittishly, as if anybody could have overheard our hushed conversation."
                    c "I’m sorry if I’ve made you feel uncomfortable, but I just can’t lie to you."
                    scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_shy") with dissolve
                    na "I...{w} It’s just...{w} I need to think on all this, [p_name]."
                    c "Of course."
                    c "Take all the time you need, but don’t deny yourself anything on account of me or anyone else."
                    scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_sad") with dissolve
                    na "I won’t, I promise."
                    c "I’ll leave you to your studies."
                    na "Thank you."
                    scene ep010_library_na_books with dissolve
                    "Nadya dove into her books almost immediately, glad for the distraction."
                    "I could tell she wasn’t really reading, as she absentmindedly turned the pages of whatever tome lay before her."
                    "A little apprehensive, I took my leave of her and exited the library."
                "Concede" if True:
                    c "Maybe you’re right."
                    c "Those mushroom spores had us acting on base instinct, without minding any of the consequences."
                    c "And if you feel uncomfortable now, it can’t have been right."
                    c "What I do hope is that this doesn’t remain standing between us as something uncomfortable."
                    scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_doubt") with dissolve
                    na "I think we should forget what happened and move on."
                    c "Agreed."
                    scene ep010_library_na_books with dissolve
                    "Nadya smiled wistfully and made it clear she wanted to be left alone with her books."
                    "Despite the awkward conversation I took my leave and exited the library feeling relieved."
        "Accept apology" if True:
            c "Thank you for your honesty."
            c "We were all acting very much out of character that night, so I think your theory about the mushroom spores does have merit."
            c "I do hope this doesn’t remain standing between us as something uncomfortable."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_sad") with dissolve
            na "Not as far as I’m concerned."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_smile") with dissolve
            na "I’m really glad we could talk this over."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_sad") with dissolve
            na "I think we should forget what happened and move on."
            c "Agreed."
            scene ep010_library_na_books with dissolve
            "Despite the awkward conversation I left Nadya to her books and exited the library feeling relieved."
        "Apologize" if True:
            $ ep010_na_apology = True
            c "No, I’m the one who should be making the apologies."
            c "I don’t know what came over me back in that cave."
            c "What I do know is that I took advantage of the situation and I shouldn’t have."
            c "I’m sorry if I made you feel uncomfortable."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_smile") with dissolve
            na "Thank you, [p_name_short], I’m really glad we could talk this over."
            scene expression eye_blink("images/ep010/ep010_library_na_closeup_alt_doubt") with dissolve
            na "Now, I think we should forget what happened and move on."
            scene ep010_library_na_books with dissolve
            "Despite the awkward conversation I left Nadya to her books and exited the library feeling relieved."
    return

label ep010_rahia:
    $ woman_name = "Guard"
    $ woman_portrait = "side_woman"
    "I hadn’t seen the Acarhyn commander in a while, but decided that now is as good a time as any to call on her."
    "We needed an edge during the upcoming Hunt, Rahia and her warrior caste might be able to provide one."
    scene ep010_rahia_guards with dissolve
    "The guards at the door to her quarters looked at me with some measure of indifference."
    c "I came to see the commander."
    scene expression eye_blink("images/ep010/ep010_rahia_guards_closeup") with dissolve
    woman "Do you have an appointment?"
    c "Yes."
    "Of course I didn’t, but it seemed the better answer."
    scene expression eye_blink("images/ep010/ep010_rahia_guards_alt") with dissolve
    "One of the guards went inside Rahia’s quarters and came back not long after."
    woman "The commander will see you now."
    c "Excellent."
    scene ep010_rahia_enter with dissolve
    "The two women stepped aside and allowed me to enter the spacious room ahead."
    scene expression eye_blink("images/ep010/ep010_rahia") with dissolve
    rah "You’re certainly not on my list of petitioners today."
    c "Must have been a clerical error."
    scene expression eye_blink("images/ep010/ep010_rahia_closeup") with dissolve
    rah "Quite..."
    rah "You’ve come about the Hunt, I take it?"
    c "How did you guess?"
    scene expression eye_blink("images/ep010/ep010_rahia_closeup_smile") with dissolve
    rah "It’s all everyone talks about at the moment and you have something to gain."
    rah "So I take it you are participating?"
    c "I am."
    c "The trouble is, that all the other contestants will have a sponsor."
    scene expression eye_blink("images/ep010/ep010_rahia_closeup") with dissolve
    rah "And you don’t have one?"
    c "I’m looking at options."
    rah "What?"
    scene expression eye_blink("images/ep010/ep010_rahia_closeup_doubt") with dissolve
    rah "You’re not seriously entertaining an offer by Erylin, are you?"
    menu:
        "Truth [RahiaPath]" if True:
            $ ep010_rahia_truth = True
            if ep010_priest_alliance:
                c "As a matter of fact, I am."
                c "But I feel you deserve a chance to state your case."
                scene expression eye_blink("images/ep010/ep010_rahia_closeup_serious") with dissolve
                rah "She’s going to betray you in the end."
                c "I’d be shocked if she didn’t."
                rah "At least you appear to be careful about it."
                rah "But I’d like you to reconsider your alliance with Erylin."
            elif True:
                if ep010_erylin_alliance_options:
                    c "She made me an offer, but I haven't decided yet."
                elif True:
                    c "No, I’m not."
                    c "Erylin and I don’t particularly see eye to eye."
                rah "I’m pleased to hear that, actually."
                scene expression eye_blink("images/ep010/ep010_rahia_closeup_serious") with dissolve
                rah "There’s no love lost between the warrior and the priest caste, especially in recent years."
                rah "We’ve made some daring technological leaps during the last decades, but we could have done more if it weren’t for the priesthood."
                rah "Our advancement couldn’t have happened with a stronger priest caste, but they’re clawing their way back."
                c "Why are they hampering your efforts at progress?"
                rah "Because they want absolute control over it, it’s the base of their power."
                rah "The priest caste are masters in genetics, but they don’t share."
                c "And you do?"
                scene expression eye_blink("images/ep010/ep010_rahia_closeup") with dissolve
                rah "We deem any technological advancement discovered by one of the Acarhyn a benefit to our entire people, it makes us stronger."
        "Be vague" if True:
            c "I can’t reveal any of my cards, I’m sure you’ll understand."
            scene expression eye_blink("images/ep010/ep010_rahia_closeup_serious") with dissolve
            rah "Every bit the politician."
            c "You sound disappointed."
            rah "Political infighting is at the heart of the conflict between the warrior and the priest caste."
            rah "What we want is simple, to make Acarhyn society as strong as possible, with whatever means necessary."
            rah "The priest caste have always been looking to control the population, in order to guide the people along their interpretation of our scripture."
            rah "We’ve made some daring technological leaps during the last decades, but we could have done more if it weren’t for the priesthood."
            rah "Our advancement couldn’t have happened with a stronger priest caste, but they’re clawing their way back."
            rah "If you’ve entered into an alliance with Erylin, I ask you to reconsider."
    scene expression eye_blink("images/ep010/ep010_rahia_closeup") with dissolve
    rah "Your goals are clear."
    if game.is_special:
        rah "You want access to your sister and eventually get off our planet."
    elif True:
        rah "You want access to your friend and eventually get off our planet."
    rah "We can ensure that will happen after the Hunt."
    rah "Once you’re the Hero of the Acarhyn you’ll have the political clout to demand anything you want and you’ll have the support of the warrior cast to back you up."
    c "And you benefit from this arrangement how?"
    scene expression eye_blink("images/ep010/ep010_rahia_closeup_serious") with dissolve
    rah "Finding the Virgin Queen has bolstered the influence of the priest caste, and Erylin is clearly wielding it with relish."
    if game.is_special:
        rah "During the ceremony after the Hunt, we’ll appear together, the Brother to the Queen and commander of the warrior caste."
    elif True:
        rah "During the ceremony after the Hunt, we’ll appear together, the Hero of the Acarhyn and commander of the warrior caste."
    rah "We’ll pose as a united front against Erylin."
    if game.is_special:
        rah "Combined with the power your sister wields as Queen, we’d be able to put the priest caste back in their place."
    elif True:
        rah "Combined with the power your friend wields as Queen, we’d be able to put the priest caste back in their place."
    c "I thought you hated politics."
    rah "I’m not averse to using any weapon necessary to further our goals for the good of the Acarhyn."
    c "How can I be sure you’ll follow through on this deal?"
    scene expression eye_blink("images/ep010/ep010_rahia_closeup") with dissolve
    rah "You won’t."
    rah "But I swear on my honor as a warrior that my caste won’t betray our alliance."
    rah "This is the only real chance to get what you want and live to see the day."
    c "You don’t mince words, do you?"
    scene expression eye_blink("images/ep010/ep010_rahia_closeup_smile") with dissolve
    rah "I like clarity."
    scene expression eye_blink("images/ep010/ep010_rahia_closeup") with dissolve
    rah "Do you accept?"
    menu:
        "Accept [gr][[Warrior Alliance]" if True:
            $ ep010_priest_alliance = False
            $ ep010_no_alliance = False
            $ ep010_warrior_alliance = True
            $ ep010_warrior_alliance_agreed = True
            c "Yes, I do."
            scene expression eye_blink("images/ep010/ep010_rahia_closeup_smile") with dissolve
            rah "A wise choice."
            rah "In addition to what we discussed earlier, my warriors will covertly assist you during the Hunt."
            c "What about the other Hunters from your caste?"
            rah "They’ll still participate, but won’t have the advantages you’ve now gained."
            c "No cheating, I suppose..."
            scene expression eye_blink("images/ep010/ep010_rahia_closeup_serious") with dissolve
            rah "Good hunting, warrior!"
            c "Thanks, I guess."
        "[gr]Think about it" if True:
            $ ep010_priest_alliance = False
            $ ep010_no_alliance = False
            $ ep010_warrior_alliance = False
            $ ep010_rahia_alliance_options = True
            c "I can only promise I’ll think about it."
            scene expression eye_blink("images/ep010/ep010_rahia_closeup_serious") with dissolve
            rah "You should come to a decision soon, [p_name]."
            rah "And remember that Erylin is not to be trusted."
            c "Thank you for the warning."
        "Decline" if True:
            $ ep010_rahia_decline = True
            c "I’m sorry, but I’ve made my choice."
            scene expression eye_blink("images/ep010/ep010_rahia_closeup_serious") with dissolve
            rah "As is your right."
            rah "Good hunting, warrior."
            rah "You’ll need all the luck you can get."
            c "Thanks, I guess."
    scene ep010_rahia_alt with dissolve
    "I left Rahia and headed back to my own quarters."
    return

label ep010_erylin:
    play music [ "music/unnatural-situation.ogg" ] fadeout 4 fadein 1.0

    scene ep010_quarters_letter with dissolve
    "During the day, one of the Acarhyn priestesses delivered a handwritten note to my quarters."
    "The letter was the promised invitation from Erylin."
    "I was to meet her for a private dinner in her quarters."
    menu:
        "Tear up invitation" if True:
            $ ep010_invitation_destroy = True
            scene ep010_quarters_letter_destroy with dissolve
            if game.is_special:
                "I was pretty sure the dinner would be the overture to some unholy alliance with the woman who made my sister’s life in the Citadel so much harder."
            elif True:
                "I was pretty sure the dinner would be the overture to some unholy alliance with the woman who made Eva's life in the Citadel so much harder."
            "Selling out to Erylin didn’t sit right with me, so I tore up the letter and went about my business."
        "[gr]Go to the dinner" if True:
            "I didn’t have anything better to do that evening and an alliance with Erylin might give us an advantage during the upcoming Hunt."
            "So I went."
            scene ep010_erylin_chambers with dissolve
            "Erylin’s chambers were near the temple I was brought to earlier."
            "The Acarhyn at the door evidently had orders to let me pass, because they stepped aside as soon as I approached."
            scene ep010_erylin_chambers_alt with dissolve
            if ep008_commander_visit:
                "I walked into a large room, comparable in size to Rahia’s quarters."
            elif True:
                "I walked into a large room, luxuriously furnished."
            scene ep010_erylin_chambers_inside with dissolve
            "The room was lit unevenly by many candles and a fire in the hearth."
            if ep008_commander_visit:
                "No artificial lighting was in evidence, a curious contrast compared to Rahia’s apartment."
            elif True:
                "No artificial lighting was in evidence."
            er "[p_name], I’m so delighted you took me up on my invitation."
            scene ep010_erylin with dissolve:
                yalign 1.0
                ease 8 yalign 0.01
            $ renpy.pause()
            "Erylin had shed her ceremonial armor and was wearing something comfortable tonight."
            "Her provocative dress was surely one of her many deliberate assaults on my willpower tonight."
            scene expression eye_blink("images/ep010/ep010_erylin_closeup") with dissolve
            $ keo_name = "Keodele"
            er "My acolyte Keodele will serve us tonight."
            er "Please say hi to [p_name], Keo."
            scene ep010_acolyte_hide with dissolve
            "At first, I didn’t notice the slight girl standing behind Erylin."
            "She shuffled towards us, her eyes downcast."
            er "Come, dear, come."
            scene ep010_acolyte_erylin with dissolve
            "Her shyness only extended to me, because she took Erylin’s outstretched hand eagerly and embraced the head priestess."
            er "Keo is one of my dearest pupils."
            scene ep010_acolyte_erylin_closeup with dissolve
            keo "Hi [p_name], it’s an honor to meet you."
            c "Likewise."
            scene ep010_acolyte_erylin_closeup_alt with dissolve
            er "Good, with the introductions out of the way, let’s sit at the table and break bread together, shall we?"
            "I followed Erylin to the table and sat down in the chair she offered me."
            scene ep010_erylin_sit_keo with dissolve
            er "Keo, be a dear and serve us the main course."
            keo "Yes, mistress."
            scene expression eye_blink("images/ep010/ep010_erylin_sit") with dissolve
            er "I think we should start with a toast."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine") with dissolve
            "The woman was bent on making this a diplomatic showpiece and I had no intention to go against the grain...{w} for now."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt") with dissolve
            "So I let her pour two glasses of what I supposed was red wine."
            er "To fruitful new beginnings."
            c "To new beginnings."
            er "I’ve asked for some of our local delicacies, I do hope you’ll enjoy them."
            c "I’m sure I will."
            "Keodele brought us the first dish, some type of stew which smelled quite good."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
            er "How are you enjoying your stay so far?"
            c "It’s been quite pleasant, as far as imprisonment goes."
            er "Come now, you’re not a prisoner."
            c "So we’re free to leave whenever we please?"
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
            er "Of course, as soon as your ship is space-worthy again."
            c "I hear work has been suspended."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_serious") with dissolve
            er "There was some misunderstanding, I’m sure the work will be resumed in due time."
            "I had to admire the way Erylin could spew bullshit and smile radiantly at the same time."
            "There was no question the repairs of the Bastard would be a bargaining chip in whatever game Erylin was playing."
            c "I’m very glad to hear that."
            c "This stew is excellent, by the way."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
            er "It’s one of the staples of Acarhyn cuisine."
            c "I can imagine."
            er "More wine?"
            c "Yes, please."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_serious") with dissolve
            er "So, [p_name], I’m sure you’ve heard the announcement."
            er "Are you going to participate in the upcoming Hunt?"
            c "Yes, it seems like too good an opportunity to pass up on."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
            er "That’s exactly right."
            er "The Hunt is one of the most prestigious events in our culture."
            c "Won’t me being an outsider and a man be a problem?"
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
            er "Heavens no, the Hunt is open to all, even to our male population."
            er "In fact, I believe your presence will be welcomed and your status as an outsider conveniently ignored."
            er "A chance to demonstrate your bravery and mettle."
            c "Indeed."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
            er "Forgive me for being forward, but do you have a sponsor for the Hunt?"

            menu:
                "Yes" if ep010_warrior_alliance:
                    c "Yes, I have."
                    scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_doubt") with dissolve
                    er "Oh...{w} That’s surprising."
                    er "Who has been so generous to support an outsider like you?"
                    c "I thought the fact that I was an outsider would conveniently be ignored."
                    scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
                    er "Not by sponsors."
                    if ep010_warrior_alliance:
                        c "The warrior caste is supporting me."
                        scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_serious") with dissolve
                        er "Are they now."
                        er "Rahia has been quick to sweep you up."
                        er "Would you allow me to make a counter-offer?"
                        menu:
                            "[gr]Yes" if True:
                                c "Of course."
                                scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
                                er "In that case I’m going to be blunt with you."
                                call ep010_erylin_proposal from _call_ep010_erylin_proposal
                            "No" if True:
                                $ ep010_erylin_decline = True
                                c "I’m afraid I must decline, I’m committed."
                                scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_annoyed") with dissolve
                                er "As is your right."
                                er "I wish you good luck on the Hunt."
                                er "Another toast, to good luck on the Hunt!"
                                scene ep010_erylin_dinner with dissolve
                                "To me, all her well-wishing suddenly sounded a little sinister, but I decided to ignore it during the remainder of the dinner."
                                "Erylin was ever courteous, but I did notice a certain detachment in her after pledging my alliance to the warrior caste."
                                "The remaining courses were served in quick succession and our conversation never veered from superficial banter."
                                "All smiles, Erylin and her acolyte thanked me for the company and bid me farewell."
                    elif True:
                        c "My crew is sponsoring me."
                        scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_doubt") with dissolve
                        er "You’re going to rely solely on them?"
                        c "I have done so for a long time now."
                        scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
                        er "I understand."
                        er "The relationships forged among a spaceship crew are stronger than family, or so I’ve heard."
                        er "But this is Erigone, your crew knows next to nothing about the intricacies of our society."
                        c "I can see where you’re going."
                        scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_serious") with dissolve
                        er "In that case, allow me to be blunt and make a proposition."
                        call ep010_erylin_proposal from _call_ep010_erylin_proposal_1
                "[gr]Looking at options" if True:
                    $ ep010_erylin_alliance_options = True
                    c "I’m still looking at all the options on the table."
                    scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
                    er "Are you now?"
                    er "A wise decision, I’d say."
                    scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
                    er "Allow me to make a proposition that might convince you."
                    call ep010_erylin_proposal from _call_ep010_erylin_proposal_2
                "No" if True:
                    c "No."
                    scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
                    er "In that case, allow me to make a proposition."
                    call ep010_erylin_proposal from _call_ep010_erylin_proposal_3
    return

label ep010_erylin_proposal:
    er "It’s no secret my caste wields considerable power."
    er "The warrior caste might impress you by their sheer martial power, but ours is more subtle."
    er "I’m sure you want to hear what we can offer you concretely."
    c "That would clear things up, yes."
    scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
    er "Right."
    er "If you choose to align yourself with us, I can promise you unfettered access to the Queen."
    er "No need to make appointments or petition her in any way."
    c "That’s a start."
    c "But what do you get out of it?"
    scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
    er "Your chances to win the Hunt with our sponsorship are high."
    er "As a matter of fact, two of your fellow Hunters are Priestesses, they might be persuaded to step aside at the right moment."
    c "All to give me a chance at winning?"
    c "The question remains, what do you get out of it?"
    scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
    if game.is_special:
        er "The Brother of the Queen as my ally."
    elif True:
        er "The Hero of the Acarhyn as my ally."
    er "Don’t underestimate the power of symbolism in this regard."
    er "The Virgin Queen has the potential of changing Acarhyn society for generations to come."
    er "I intend to steer that change in the right direction, and I’m willing to wield any measure at my disposal."
    scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
    er "So, will you allow us to sponsor you?"

    menu:
        "[gr]Maybe" if ep010_erylin_alliance_options or ep010_warrior_alliance:
            $ ep010_warrior_alliance = False
            $ ep010_no_alliance = False
            $ ep010_priest_alliance = False
            c "I won’t deny you make a strong case, but as I said, all options are still on the table."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_serious") with dissolve
            er "You mean to drive a hard bargain."
            c "I’m sure you would do the same in my place."
            er "So forward."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
            er "I like you, [p_name]."
            er "And yes, I’d do the same in your place."
            if game.is_special:
                er "You know how much power you yield as Brother to the Queen."
            elif True:
                er "You know how much power you yield as Friend to the Queen."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup") with dissolve
            er "Just know that to realize your full potential, you should align with us."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
            er "You and I, we understand each other."
            c "I’ll toast to that."
            scene ep010_erylin_dinner with dissolve
            "The remainder of the dinner, Erylin betrayed little emotion other than what she’d already displayed, but I sensed she was looking for an angle."
            "We talked about various topics, ranging from our travels to life on Erigone."
            "When we’d reached the dessert course, the woman looked at me intently."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
            er "I had a lovely dessert prepared, but I’ve thought of something that might persuade you to consider our partnership in a new and more favorable light."
            c "I’m rather well-known for my sweet tooth."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile_alt") with dissolve
            er "I don’t doubt that."
            er "Regardless, I’d like to offer you something better than dessert."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_call") with dissolve
            er "Keo, come over here."
            "The request evidently startled the girl, who’d kept a low profile until then."
            scene ep010_erylin_dinner_keodyle with dissolve
            "She came to stand beside Erylin, waiting for her superior to speak again."
            er "I’m going to ask you a question, girl."
            er "Do you agree to answer full and truthfully, no matter what?"
            keo "Of course, mistress."
            er "Good."
            er "How many men have you invited to your bed?"
            scene ep010_erylin_dinner_keodyle_shock with vpunch
            "A look of sheer horror crossed the girl’s face, the question clearly scandalizing to her."
            keo "Why, none, mistress!"
            keo "Acolytes are not allowed to have relations of any kind."
            keo "You don’t doubt that I..?"
            er "Of course not, I have no reason to."
            scene expression eye_blink("images/ep010/ep010_erylin_dinner_keodyle_closeup") with dissolve
            "That put the acolyte at ease somewhat, until Erylin focused her attention on me again."
            call ep010_erylin_keo_sex_proposal from _call_ep010_erylin_keo_sex_proposal
        "Accept [gr][[Priest Alliance]" if not ep010_warrior_alliance:
            $ ep010_warrior_alliance = False
            $ ep010_no_alliance = False
            $ ep010_priest_alliance = True
            $ ep010_priest_alliance_agreed = True
            c "It would be an honor."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
            er "Excellent, most excellent!"
            er "This calls for another toast."
            er "To our partnership!"
            er "To the Hunt!"
            scene ep010_erylin_dinner with dissolve
            "The remainder of the dinner, Erylin betrayed little emotion other than what she’d already displayed, but I sensed she was more at ease."
            "We talked about various topics, ranging from our travels to life on Erigone."
            "When we’d reached the dessert course, the woman looked at me intently."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
            er "I had a lovely dessert prepared, but in light of recent developments it just doesn’t seem celebratory enough."
            c "I’m rather well-known for my sweet tooth."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile_alt") with dissolve
            er "I don’t doubt that."
            er "Regardless, I’d like to offer you something better than dessert."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_call") with dissolve
            er "Keo, come over here."
            "The request evidently startled the girl, who’d kept a low profile until then."
            scene ep010_erylin_dinner_keodyle with dissolve
            "She came to stand beside Erylin, waiting for her superior to speak again."
            er "As you might have gathered, we’re in a festive mood."
            er "I’d like you to join us, girl."
            keo "Of course, mistress."
            scene expression eye_blink("images/ep010/ep010_erylin_dinner_keodyle_closeup") with dissolve
            er "Good."
            call ep010_erylin_keo_sex_proposal from _call_ep010_erylin_keo_sex_proposal_1
        "Decline" if True:
            $ ep010_erylin_decline = True
            c "I’m afraid I must decline, I’m committed."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_annoyed") with dissolve
            er "As is your right."
            er "I wish you good luck on the Hunt."
            scene expression eye_blink("images/ep010/ep010_erylin_sit_wine_alt_closeup_smile") with dissolve
            er "Another toast, to good luck on the Hunt!"
            scene ep010_erylin_dinner with dissolve
            "To me, all her well-wishing suddenly sounded a little sinister, but I decided to ignore it during the remainder of the dinner."
            "Erylin was ever courteous, but I did notice a certain detachment in her after pledging my alliance to the warrior caste."
            "The remaining courses were served in quick succession and our conversation never veered from superficial banter."
            "All smiles, Erylin and her acolyte thanked me for the company and bid me farewell."
    return

label ep010_erylin_keo_sex_proposal:
    if game.is_special:
        er "So [p_name], would you like to be my daughter’s first?"
        scene expression eye_blink("images/ep010/ep010_erylin_dinner_keodyle_closeup_alt") with vpunch
        keo "Mother!"
        c "You mean...{w} She’s your daughter?"
        scene expression eye_blink("images/ep010/ep010_erylin_dinner_keodyle_closeup") with dissolve
        er "She is, you didn’t notice the family resemblance?"
        c "Now that you mention it..."
    elif True:
        er "So [p_name], would you like to be Keo’s first?"
        scene expression eye_blink("images/ep010/ep010_erylin_dinner_keodyle_closeup_alt") with vpunch
        keo "Mistress!"
        scene expression eye_blink("images/ep010/ep010_erylin_dinner_keodyle_closeup") with dissolve
    er "Or are you scandalized by my offering her virginity to you?"

    menu:
        "Decline" if True:
            c "I’m sorry, but I must decline."
            scene expression eye_blink("images/ep010/ep010_erylin_dinner_keodyle_closeup_annoyed") with dissolve
            er "..."
            er "Tivronberry soufflé it is then."
            scene ep010_erylin_dinner_alt with dissolve
            "The head priestess wasn’t as courteous as before, but never became outright hostile."
            "She’d already got what she wanted from me anyway."
            "All smiles, Erylin and her daughter thanked me for the company and bid me farewell."
        "[gr]Accept" if True:
            $ ep010_er_keo_sex = True
            c "Not at all."
            c "I was just hoping you’d join as well."
            scene expression eye_blink("images/ep010/ep010_erylin_dinner_keodyle_closeup_smile") with dissolve
            er "Cheeky."
            er "But I can’t deny that I’m intrigued."
            call ep010_erylin_sex from _call_ep010_erylin_sex

            scene expression eye_blink("images/ep010/ep010_erylin_naked_post_closeup") with dissolve
            er "I hope we didn’t make you wait long for that dessert?"
            c "I’m not sure there is any dessert that tops the feeling of popping a girl’s cherry."
            er "Quite."
            er "Now, say thank you to [p_name], Keodele."
            scene expression eye_blink("images/ep010/ep010_erylin_naked_post_closeup_alt") with dissolve
            keo "Thank you, [p_name]."
            er "Why don’t you be a dear and clean up the dishes."
            keo "Of course, mother."
            scene expression eye_blink("images/ep010/ep010_erylin_naked_post_closeup") with dissolve
            er "I’m afraid we must part ways here, [p_name]."
            er "Thank you for a lovely evening."
            c "Likewise."
            scene ep010_erylin_naked_post_alt with dissolve
            if game.is_special:
                "As Keodele busied herself with the dishes, her mother stretched herself out on the bed."
            elif True:
                "As Keodele busied herself with the dishes, Erylin stretched herself out on the bed."
            "I took my leave and ventured back into the Citadel, in search of my own quarters."
        "Have dessert [gr][[Insult Erylin]" if True:
            $ ep010_er_insult = True
            c "I’d rather have dessert, if you don’t mind."
            scene expression eye_blink("images/ep010/ep010_erylin_dinner_keodyle_closeup_annoyed") with dissolve
            er "..."
            er "Tivronberry soufflé it is then."
            scene ep010_erylin_dinner_alt with dissolve
            "The head priestess wasn’t as courteous as before, but never became outright hostile, despite my thinly veiled insult."
            "She’d already got what she wanted from me anyway."
            "All smiles, Erylin and her daughter thanked me for the company and bid me farewell."

    python:
        if game.is_special:
            codex_keodele = add_codex_entry(
                Codex,
                __("Characters"),
                __("Keodele"),
                [
                    __("An acolyte of the Acarhyn priest caste and daughter of Erylin. Her virginity is offered by her mother in exchange for an alliance with the priest caste.")
                ],
                "images/codex/Keodele.webp"
            )
        else:
            codex_keodele = add_codex_entry(
                Codex,
                __("Characters"),
                __("Keodele"),
                [
                    __("An acolyte of the Acarhyn priest caste. Her virginity is offered by Erylin in exchange for an alliance with the priest caste.")
                ],
                "images/codex/Keodele.webp"
            )
    return

label ep010_raene:
    play music [ "music/chasing-daylight.ogg" ] fadeout 4 fadein 1.0
    scene ep008_erigone_quarters with dissolve
    "I was still mulling things over in my quarters when there was a knock on my door."
    scene ep010_quarters_ra with dissolve
    ra "Hi, [p_name], I’m not disturbing you or anything?"
    c "Of course not."
    c "Did you hear about the Hunt?"
    scene expression eye_blink("images/ep010/ep010_quarters_ra_closeup") with dissolve
    ra "Yes, I did."
    ra "It’s part of the reason I stopped by."
    c "Oh?"
    ra "You’re required to ride some native animal during the Hunt, right?"
    c "Yes, something huge and ugly called a calgound."
    scene expression eye_blink("images/ep010/ep010_quarters_ra_closeup_serious") with dissolve
    ra "Do you have any experience on horseback?"
    c "I had lessons back on Tuolovi, but I wasn’t very good at it."
    "The big-breasted girl who taught us interested me far more to the point of distraction, but it seemed prudent to omit that detail."
    scene expression eye_blink("images/ep010/ep010_quarters_ra_closeup") with dissolve
    ra "I mentioned me horse-riding on Verdigris, but I also have some experience in riding larger animals."
    ra "I was thinking maybe we could ride together, just to get some practice."
    scene expression eye_blink("images/ep010/ep010_quarters_ra_closeup_doubt") with dissolve
    ra "Or maybe you think it’s a stupid idea?"
    c "No, I’d love for someone to have my back while I attempt to tame one of those beasts."
    scene expression eye_blink("images/ep010/ep010_quarters_ra_closeup") with dissolve
    ra "We could go now, if you want to?"
    c "Sure thing, if I wait any longer I’ll probably get cold feet."
    scene expression eye_blink("images/ep010/ep010_quarters_ra_closeup_smile") with dissolve
    ra "I’m sure it won’t be that bad."
    c "Yeah, maybe they’ll assign us two docile cubs."
    scene ep010_corridor_ra with dissolve
    "Raene and I made our way to the pens where the calgounds were held."
    scene ep010_pens with dissolve
    "Unfortunately, there were only adult animals for us to ride."
    scene ep010_pens_alt with dissolve
    "The Acarhyn beastmaster allowed us to pick two calgounds after we explained we were looking to train for the Hunt."
    scene expression eye_blink("images/ep010/ep010_pens_ra") with dissolve
    c "They all look wild and vicious to me."
    ra "They’re certainly impressive."
    scene ep010_pens_beasts with dissolve
    "We paused before two fine looking specimens."
    ra "Why don’t we try those two?"
    c "I’ll tell that woman to saddle them up."
    scene ep010_citadel_beasts with dissolve
    "The beastmaster didn’t comment on our choice of calgound and just ordered two of her minions to prepare the beasts for riding."
    scene ep010_citadel_beasts_alt with dissolve
    "We were led into an open spot in the jungle near the Citadel walls, where the Acarhyn left us with the beasts"
    c "Right, let’s get this show on the road."
    scene ep010_citadel_beasts_mount with dissolve
    "I was still trying to find the right angle to mount the beast, when I noticed Raene hopping on the back of her calgound."
    "She looked well at ease on the back of the huge beast."
    scene expression eye_blink("images/ep010/ep010_citadel_beasts_mount_ra") with dissolve
    ra "Don’t think too much about it, [p_name_short]!"
    c "You make it look easy."
    scene ep010_citadel_beasts_mount_alt with dissolve
    "Nevertheless, I decided to heed her advice."
    "The calgound snorted when I put one foot in the stirrups."
    "It snorted again when I swung my leg over its back, sat down in the saddle and took the reins."
    c "So far, so good."
    scene expression eye_blink("images/ep010/ep010_citadel_beasts_mount_ra") with dissolve
    ra "Let’s ride!"
    "Raene pushed her boots into the flanks of the calgound and off she went."
    scene ep010_beasts_run with dissolve
    "Some of the basics I apparently picked up during those horse-riding lessons, through no effort of my own, kicked in and I followed her lead."
    "The calgounds ran fast, and Raene had a headstart."
    scene ep010_beasts_run_alt with dissolve
    "She looked back to see if I was following and slowed down when she saw the distance between us."
    scene expression eye_blink("images/ep010/ep010_beasts_run_ca_closeup") with dissolve
    ra "Great isn’t it?!"
    c "They’re pretty fast."
    scene ep010_calgound_raene with dissolve
    "It was clear Raene was loving every minute of this, but I had trouble mustering as much enthusiasm."
    scene expression eye_blink("images/ep010/ep010_calgound_raene_closeup") with dissolve
    ra "Don’t you feel free?"
    scene ep010_calgound_jungle with dissolve
    "I must admit I felt a thrill seeing the jungle flash past me, the wind whistling through my hair."
    scene expression eye_blink("images/ep010/ep010_calgound_raene_closeup_smile") with dissolve
    "Raene looked at me, her eyes glowing with fervor and admiration."
    ra "You’re a natural, [p_name_short]!"
    c "Thanks, this is going better than I’d thought."
    c "I might even start to enjoy this."
    ra "Wanna see how fast these calgounds go?"
    c "I-"
    scene ep010_calgound_jungle_alt with dissolve
    ra "Race you to the clearing up ahead!"
    scene ep010_calgound_jungle_sprint with vpunch
    "Before I could reply, Raene had kicked her mount into a fierce sprint."
    "I made an effort to follow her, but she was almost halfway to the clearing already."
    scene ep010_calgound_jungle_sprint_alt with dissolve
    "While in mid-sprint, Raene turned around to gauge my pursuit."
    "She grinned at me and spurred her calgound even further."
    "What happened next was all a jumble."
    scene ep010_calgound_raene_fall with vpunch
    "The calgound roared, Raene screamed while her mount leapt over a fallen tree and didn’t quite make it."
    "The violence of the beast’s stumble combined with the speed of its sprint made Raene lose control."
    "I saw her thrown from the saddle, hitting the ground and rolling through the jungle soil."
    c "Raene!!!"
    scene ep010_calgound_raene_fall_alt with vpunch
    "Freed from its rider, Raene’s calgound continued its mad dash into the jungle foliage and disappeared from view."
    scene ep010_calgound_raene_fallen with dissolve
    "I managed to slow down and guide my calgound to where Raene lay motionless."
    "Mercifully, I managed a hasty descent from my mount, without getting tied up in one of the stirrups."
    "As soon as I hit the ground I sprinted towards Raene."
    c "Raene!"
    c "Raene, are you alright?!"
    scene ep010_calgound_raene_fallen_closeup with dissolve
    "When I knelt down beside her I could tell she was breathing."
    "Her eyes were closed, and I thought she’d lost consciousness until she mouthed a whisper."
    scene ep010_calgound_raene_fallen_closeup_alt with dissolve
    ra "My...{w} My armor...{w} It...{w} hurts."
    "From what I could tell, the restrictive body armor she always wore was dented in several places from the fall."
    "A couple of those deeper dents were evidently pressing against her ribcage, making it hard for her to breath."
    c "I’m going to remove that armor, Raene, please stay with me."
    "Raene managed a nod and I started working on peeling the armor off her."
    scene ep010_calgound_raene_fallen_undress with dissolve
    "After removing her breastplate, I managed to pry loose the twisted piece that was restricting her air intake."
    "When I had the entire thing removed she suddenly breathed much easier."
    "Her neck and shoulders were severely bruised."
    "I was about to feel if she’d broken anything when she opened her eyes."
    scene expression eye_blink("images/ep010/ep010_calgound_raene_fallen_undress_closeup") with dissolve
    ra "What...{w} What was I thinking?!"
    ra "S-so s-stupid!"
    c "Save your strength, Raene."
    c "Can you get up?"
    scene expression eye_blink("images/ep010/ep010_calgound_raene_fallen_undress_closeup_doubt") with dissolve
    ra "I think so."
    "I supported her as Raene attempted to get up."
    scene expression eye_blink("images/ep010/ep010_calgound_raene_fallen_undress_sit") with dissolve
    ra "Owwww!{w} My leg!"
    c "Do you mind if I take a look?"
    ra "Not at all."
    scene ep010_calgound_raene_fallen_pants with dissolve
    "In pain, Raene lay down again, where I helped her out of her pants to reveal her bruised and battered legs."
    scene expression eye_blink("images/ep010/ep010_calgound_raene_fallen_undress_sit_cry") with dissolve
    c "Where does it hurt?"
    ra "Right there."
    scene ep010_calgound_raene_fallen_pants_touch with dissolve
    "I touched the spot she indicated and softly pressed."
    "She winced, but didn't cry out immediately."
    "As far as I could tell, nothing was broken, but her legs did endure the worst of the fall."
    c "I don't think you've broken anything."
    scene expression eye_blink("images/ep010/ep010_calgound_raene_fallen_pants_sit") with dissolve
    ra "That's a relief."
    "Raene stared in the distance."
    scene expression eye_blink("images/ep010/ep010_calgound_raene_fallen_pants_sit_sad") with dissolve
    ra "I'm such a failure, [p_name]."
    ra "Here I am, telling you I had so much experience riding horses, and the first thing I do is fall of my animal, like some amateur."
    c "It was an accident, Raene, just bad luck."
    c "Thanks to you I actually tried riding a calgound."
    c "Otherwise I'd probably have held off even looking at those beasts until right before the start of the hunt."
    c "But above all, I just liked seeing you so happy."
    scene expression eye_blink("images/ep010/ep010_calgound_raene_fallen_pants_sit_smile") with dissolve
    "She didn’t have a response, but a slight smile crept across her face."
    c "Do you think you can ride with me on my calgound?"
    scene expression eye_blink("images/ep010/ep010_calgound_raene_fallen_pants_sit_doubt") with dissolve
    ra "I think so."
    c "Good, let’s get you up slowly and carefully then."
    scene ep010_calgound_raene_fallen_pants_help with dissolve
    "I moved closer towards her in order to put my arms around her waist."
    scene ep010_calgound_raene_fallen_pants_help_alt with dissolve
    "We were face to face now."
    "I could feel Raene holding her breath."
    menu:
        "Kiss her [RaenePath]" if True:
            $ ep010_ra_kiss = True
            scene ep010_calgound_raene_kiss with dissolve
            "Instead of helping her rise, my lips brushed hers."
            scene ep010_calgound_raene_kiss_alt with dissolve
            "We kissed."
            "The noises of the jungle seemed to subside while I gingerly took the girl in my arms."
            "When we disentangled, Raene looked at me in confusion."
            scene expression eye_blink("images/ep010/ep010_calgound_raene_kiss_closeup") with dissolve
            ra "We kissed..."
            "I could tell that she was berating herself already for stating the obvious, so I didn’t allow her to dwell on it."
            c "I've wanted to do that for quite some time."
            c "I really like you, Raene."
            c "You’re strong, brave and deserve all the happiness you can get."
            scene expression eye_blink("images/ep010/ep010_calgound_raene_kiss_closeup_smile") with dissolve
            "The confusion on Raene’s face was gradually replaced by the admiration I’d seen earlier."
            ra "Thank you, [p_name_short], you don’t know how happy that makes me hearing you say that."
            scene expression eye_blink("images/ep010/ep010_calgound_raene_kiss_closeup_doubt") with dissolve
            ra "I...{w} I think..."
            ra "No."
            scene expression eye_blink("images/ep010/ep010_calgound_raene_kiss_closeup_smile") with dissolve
            ra "I really like you too..."
            scene ep010_calgound_raene_kissing with dissolve
            "This time it was she who kissed me first."
            "I could feel the passion burning behind that kiss, and I believe we’d have given ourselves over to it if it weren’t for her injuries."
            "Raene reached for me, but winced in pain as she twisted her leg."
            scene ep010_calgound_raene_kissing_closeup with dissolve
            ra "Ouch!"
            c "We really need someone to have a look at that."
            c "Let me help you up."
            scene ep010_calgound_raene_help with dissolve
            "I put my arms around her middle and slowly helped her rise."
        "Help her up" if True:
            scene ep010_calgound_raene_help with dissolve
            "She exhaled as soon as I put my arms around her middle and slowly helped her rise."
    "Raene limped on one of her legs and was visibly in pain."
    scene ep010_calgound_raene_help_alt with dissolve
    c "Just lean on that stump over there and I’ll get the calgound ready."
    "Luckily, the beast chose to cooperate instead of being a stubborn bitch."
    scene ep010_calgound_raene_help_calgound with dissolve
    "I managed to get the calgound to get as low to the ground as possible, to let Raene climb on top with relative ease."
    "Once she was in the saddle, I followed."
    scene ep010_calgound_raene_help_calgound_alt with dissolve
    if ep010_ra_kiss:
        "Raene put her arms firmly around my middle as the calgound rose."
    elif True:
        "Raene put her arms around my middle as the calgound rose."
    scene ep010_calgound_raene_run with dissolve
    "I softly kicked the animal into an urgent jog."
    if ep010_ra_kiss:
        "As the beast began to accelerate, Raene grabbed hold of me even tighter and let her head rest against my back."
    elif True:
        "As the beast began to accelerate, Raene grabbed hold of me even tighter."
    scene ep010_calgound_raene_beastmaster with dissolve
    "The Beastmaster of the Citadel was already awaiting us at the entrance of the animal pens."
    "Raene’s calgound had found its way back to the Citadel and the Acarhyn were on high alert."
    scene ep010_calgound_raene_beastmaster_alt with dissolve
    "Raene was taken off my mount by several women and carried off to the medical ward of the Acarhyn stronghold."
    scene ep010_calgound_raene_beastmaster_closeup with dissolve
    "I promised Raene I’d visit her as soon as they were done treating her injuries."
    "The Beastmaster accepted my explanation of how we lost one of her animals, and there were no further repercussions."
    scene ep008_erigone_quarters with dissolve
    if ep010_ra_kiss:
        "A little tired and overwhelmed by the events in the jungle, I went back to my quarters."
    elif True:
        "A little tired, I went back to my quarters."
    return

label ep010_celine:
    play music "music/solace.ogg" fadeout 4 fadein 1.0
    "Céline had successfully avoided me for quite some time now."
    "I thought it was time to force a meeting with her."
    scene ep010_kit with dissolve
    c "Hey Kit, do you know where your sister is hanging around?"
    ki "Hey!"
    scene expression eye_blink("images/ep010/ep010_kit_closeup_doubt") with dissolve
    ki "I’m not sure you want to meet her right now, she’s been in a foul mood for several days now."
    c "Yeah, I know."
    scene expression eye_blink("images/ep010/ep010_kit_closeup_doubt_alt") with dissolve
    ki "Uh-oh, trouble in paradise?"
    c "Something like that."
    c "She’s been avoiding me."
    scene expression eye_blink("images/ep010/ep010_kit_closeup_serious") with dissolve
    ki "You haven’t been a dick to her, have you?"
    ki "I mean, not more of a dick than you usually are?"
    c "You know you’re so funny sometimes, it almost hurts physically?"
    scene expression eye_blink("images/ep010/ep010_kit_closeup_smile") with dissolve
    ki "It’s a very rare and treasured gift."
    c "Yeah..."
    c "Seriously though, I haven’t been a dick to her."
    c "It’s just a misunderstanding."
    scene expression eye_blink("images/ep010/ep010_kit_closeup") with dissolve
    ki "Right, well, she’s been hanging out on the Citadel’s ramparts often."
    ki "Apparently that’s a great place to sulk."
    c "Thanks, Kit."
    ki "You’re welcome."
    scene expression eye_blink("images/ep010/ep010_kit_closeup_serious") with dissolve
    ki "Now go and make up, before I have to play the angry brother and beat you senseless to defend her honor."
    c "I’d like to see you try."
    scene expression eye_blink("images/ep010/ep010_kit_closeup_smile") with dissolve
    ki "Is that a challenge?"
    c "Later, Kit."
    scene expression eye_blink("images/ep010/ep010_kit_closeup") with dissolve
    ki "Later man."
    scene ep010_celine_wide with dissolve
    "Céline wasn’t sulking on the ramparts, but I could see her standing on one of the Citadel’s watchtowers, illuminated by Erigone’s moon."
    "A little heavy-hearted, I climbed the steps to the top of the tower."
    scene ep010_celine with dissolve
    c "Céline?"
    ce "Oh, I knew it was you."
    c "Céline, can we talk?"
    c "I know you’ve been avoiding me since you came into my quarters."
    scene expression eye_blink("images/ep010/ep010_celine_closeup_alt") with dissolve
    ce "Yes."
    if not ep009_jade_sex_accept:
        c "What you saw..."
        c "Jade was just talking to me."
        ce "I know."
        ce "I just...{w} I saw you to together and then it hit me."
        c "What hit you?"
        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_serious") with dissolve
        ce "All this time, I’ve come to regard Jade as one of the crew, you know?"
        ce "But she isn’t just one of the crew..."
        ce "She’s your personal plaything."
        c "It’s not like that."
        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_doubt") with dissolve
        ce "Isn’t it?"
        ce "Didn’t she offer herself to you?"
        c "Yes...{w} But..."
        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_serious") with dissolve
        ce "But you didn’t take what she offered."
        menu:
            "Tell truth [CelinePath]" if True:
                $ ep010_ce_truth = True
                if ep002_jade_sex or ep004_jade_sex or ep008_j_creampie:
                    c "Exactly."
                elif True:
                    c "Exactly, and I never have while we were dating."
            "Lie" if ep002_jade_sex or ep004_jade_sex or ep008_j_creampie:
                c "Exactly, and I never have while we were dating."
        c "I don’t mean to sound callous, but you knew about Jade."
        c "She’s been part of my life ever since I was young."
        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt") with dissolve
        ce "I know...{w} I know."
        ce "It's just...{w} Seeing you like that with her, it affected me more than I’d realized."
        ce "The thought of you being together with her made me so jealous."
        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_smile") with dissolve
        ce "I love you, [p_name_short]."
        "She blurted out that last statement and had me at a loss for words for an instant."
        menu:
            "Love her too [CelinePath]" if True:
                $ ep010_ce_love = True
                c "I love you too, Céline."
                scene ep010_celine_kiss with dissolve
                "I stepped in closer to kiss her and she accepted me right away."
                scene expression eye_blink("images/ep010/ep010_celine_kiss_closeup") with dissolve
                "When the girl tore away, she looked at me with mock disapproval."
                ce "I made myself a promise I was going to yell at you and be extra mad."
                c "The silent treatment you gave me the past few days was punishment enough."
                scene expression eye_blink("images/ep010/ep010_celine_kiss_closeup_smile") with dissolve
                ce "See, I can be cruel!"

                menu:
                    "Be faithful [gr][[Monogamy]" if True:
                        $ ep010_ce_monogamy = True
                        c "I want to make you a promise."
                        scene expression eye_blink("images/ep010/ep010_celine_kiss_closeup_serious") with dissolve
                        c "You’ll be the only girl for me."
                        scene expression eye_blink("images/ep010/ep010_celine_kiss_closeup_doubt") with dissolve
                        ce "You’d do that for me?"
                        c "Yes."
                        scene ep010_celine_kiss_alt with dissolve
                        "She kissed me with such passion, so that all doubts about my newly promised celibacy fell away instantaneously."
                    "[gr]There’ll be others" if True:
                        c "I do want to be honest with you."
                        c "I love you and I want to be with you, but my love is not unconditional."
                        scene expression eye_blink("images/ep010/ep010_celine_kiss_closeup_serious") with dissolve
                        ce "Meaning?"
                        c "Meaning that I’ll love you with all my heart, but that there’s room for others."
                        c "It might sound contradictory, but monogamy would eventually destroy our relationship, through no fault of your own."
                        scene expression eye_blink("images/ep010/ep010_celine_kiss_closeup_sad") with dissolve
                        ce "So I am to share you with others?"
                        c "Yes."
                        "Céline didn’t back away in horror from me, but I could tell she was conflicted."
                        "I was about to launch a volley of arguments when a resigned smile crossed her face."
                        scene expression eye_blink("images/ep010/ep010_celine_kiss_closeup_smile") with dissolve
                        ce "I don’t care.{w} I just want you."
                        scene ep010_celine_kiss_alt with dissolve
                        "Whether her acceptance of the situation would last, I didn’t know, but for now things seemed blissful again for us."
                        "I knew I’d have to deal with her feelings of jealousy later on, but I felt confident I could guide us through any troubles coming our way."
            "End things \n[EndRelationship]" if True:
                $ celine_romance = False
                $ celine_romance_ended = True
                c "I really like you Céline, but maybe not in the way you imagined."
                c "I like being around you, I like the intimacy we have together, but that’s it."
                scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_angry") with dissolve
                ce "Right."
                "She looked as if she was about to push me from the tower, but instead she just stared at me."
                c "I’m sorry, Céline."
                ce "Leave me alone."
                scene ep010_celine with dissolve
                "I left her on the top of the tower as she stared out over the jungle."
                return
    elif True:
        c "What you saw..."
        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_angry_alt") with dissolve
        ce "I know what I saw!{w} You two were about to fuck."
        c "I can’t deny that...{w} But you knew about me and Jade, didn’t you?"
        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_doubt") with dissolve
        ce "Yes, but all this time..."
        ce "All this time, I’ve come to regard Jade as one of the crew, you know?"
        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_serious") with dissolve
        ce "But she isn’t just one of the crew..."
        ce "She’s your personal plaything."
        c "She’s been part of my life ever since I was young."
        ce "I know...{w} I know."
        ce "Is it just her, or are there others?"
        menu:
            "Truth [CelinePath]" if True:
                $ ep010_ce_truth = True
                c "I care too much about you to lie about all this."

                if ep002_thyia_sex or ep002_ro_orgy or ep004_lu_lick or ep004_lu_suck or ep004_hannah_sex or ep005_woman_sex or ep005_workshop_sex or ep005_twill_sex or ep005_taera_sex or ep006_doctor_anal or ep006_chrone_creampie or ep007_v_sex or ep008_commander_sex or ep009_priestess_bj or ep009_cae_fuck or ep009_na_breasts or aven_romance or lilly_romance:
                    c "Yes, there are others, or have been others."
                elif True:
                    c "Jade has been the only one."

                menu:
                    "Be faithful [gr][[Monogamy]" if True:
                        $ ep010_ce_monogamy = True
                        c "But I want to make you a promise."
                        c "You’ll be the only girl for me from here on out."
                        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_smile") with dissolve
                        ce "You’d do that for me?"
                        c "Yes."
                        scene ep010_celine_kiss_alt with dissolve
                        "She kissed me with such passion, so that all doubts about my newly promised celibacy fell away instantaneously."
                    "[gr]There’ll be others" if True:
                        $ ep010_ce_love = True
                        c "I love you and I want to be with you, but my love is not unconditional."
                        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_doubt") with dissolve
                        ce "You love me?"
                        c "Yes, I do."
                        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_serious") with dissolve
                        ce "But not singularly."
                        c "No."
                        c "It might sound contradictory, but monogamy would eventually destroy our relationship, through no fault of your own."
                        ce "So if I want to have a shot with you I am to share you with others?"
                        c "Yes."
                        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_doubt") with dissolve
                        "Céline didn’t back away in horror from me, but I could tell she was conflicted."
                        ce "This is not how I imagined things to go."
                        ce "The thought of you and Jade, of anyone else together with you, makes me so jealous."
                        ce "But if refusing you to see others means I lose you..."
                        ce "I love you too, [p_name_short], that’s what makes this all so hard."
                        "I was about to launch a volley of arguments when a resigned smile crossed her face."
                        scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_smile") with dissolve
                        ce "I thought I didn't want anything to do with you anymore, but the past few days I felt so empty without you."
                        ce "So I've decided that for now I'm not going to care and give us a try, even if that means that I have to share you with others."
                        ce "I just want you."
                        scene ep010_celine_kiss_alt with dissolve
                        "Whether her acceptance of the situation would last, I didn’t know, but for now things seemed blissful again for us."
                        "I knew I’d have to deal with her feelings of jealousy later on, but I felt confident I could guide us through any troubles coming our way."
            "Lie" if ep002_thyia_sex or ep002_ro_orgy or ep004_lu_lick or ep004_lu_suck or ep004_hannah_sex or ep005_woman_sex or ep005_workshop_sex or ep005_twill_sex or ep005_taera_sex or ep006_doctor_anal or ep006_chrone_creampie or ep007_v_sex or ep008_commander_sex or ep009_priestess_bj or ep009_cae_fuck or ep009_na_breasts or aven_romance or lilly_romance:
                $ ep010_ce_love = True
                c "It was just her."
                scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_doubt") with dissolve
                ce "Just her..."
                "She voiced her last sentence with enough skepticism to make me wince."
                c "I love you, Céline."
                scene ep010_celine_kiss_alt with dissolve
                "I stepped in closer to kiss her and she accepted me right away, her lingering doubts apparently forgotten."
                "When the girl tore away, she looked at me with mock disapproval."
                ce "I made myself a promise I was going to yell at you and be extra mad."
                c "The silent treatment you gave me the past few days was punishment enough."
                scene expression eye_blink("images/ep010/ep010_celine_kiss_closeup_smile") with dissolve
                ce "See, I can be cruel!"
            "End things \n[EndRelationship]" if True:
                $ celine_romance = False
                $ celine_romance_ended = True
                c "I really like you Céline, but maybe not in the way you imagined."
                c "I like being around you, I like the intimacy we have together, but that’s it."
                scene expression eye_blink("images/ep010/ep010_celine_closeup_alt_angry") with dissolve
                ce "Right."
                "She looked as if she was about to push me from the tower, but instead she just stared at me."
                c "I’m sorry, Céline."
                ce "Leave me alone."
                scene ep010_celine with dissolve
                "I left her on the top of the tower as she stared out over the jungle."
                return

    call ep010_celine_sex from _call_ep010_celine_sex
    return

label ep010_hunt:
    play music "music/parasite.ogg" fadeout 4 fadein 1.0
    "The morning of the Hunt, the sirens of the Citadel blared again."
    "All Hunters were to gather at the pens where the calgounds were held."
    scene ep010_hunt_pens with dissolve
    "Four of my fellow Hunters had already arrived."
    "I counted two in priestess garb, while the others were clearly warriors."
    if ep008_commander_sex:
        "One of them wielded dual shotguns, another held some sort of dual-bladed glaive and the girl I knew as Athryn just brought her giant sword."
    elif True:
        "One of them wielded dual shotguns, another held some sort of dual-bladed glaive and one warrior just brought her giant sword."
    "The fourth woman, a priestess, had a large weapon strapped to her back."
    "The heavy weapon looked like some kind rocket launcher."
    "The weapon certainly wasn’t among the hardware selection I was presented with..."
    "Bloody Erylin."
    scene ep010_hunt_pens_alt with dissolve
    "I took my place next to the women, waiting for the signal to begin the Hunt."
    "Several Acarhyn were watching the spectacle unfold at the edges of the beast pens perimeter."
    scene ep010_hunt_pens_crew with dissolve
    "I spotted Lilly, Aven, Nadya and Raene pretty quickly and I hurried over to them."
    c "Nice of you to come cheer me on."
    av "The others are monitoring all the exits, so Kit and I can slip away as soon as the Hunt begins."
    l "At first the plan was to hide in the jungle during early morning, but that didn’t seem like a great idea with the beast on the loose."
    na "[p_name], I know advice is probably useless, but don’t approach the creature until you’re sure you can take it out."
    na "Don’t take any chances."
    c "I won’t."
    ra "Good luck, [p_name]."
    ra "We’ll be waiting for you in the courtyard after all this is done."
    av "I think the head priestess is arriving."
    scene ep010_hunt_pens_erylin with dissolve
    "Just after I took my place among the Hunters, Erylin came galloping into the beast pens."
    er "Hunters!"
    scene expression eye_blink("images/ep010/ep010_hunt_pens_erylin_closeup") with dissolve
    er "You are gathered here today, because of your sacred duty to the Acarhyn."
    er "A beast threatens our great Citadel."
    er "However, today the animal will become Prey!"
    er "One of you will become a Hero of the Acarhyn."
    scene ep010_hunt_pens_erylin_alt with dissolve
    er "Let the Hunt begin!"
    scene ep010_hunt_pens_mount with dissolve
    "After Erylin uttered those last words, every Hunter mounted their calgound."
    "I managed to get onto my beast without embarrassing myself and followed the other Hunters who’d already reached the exit of the animal pens."
    scene ep010_hunt_pens_exit with dissolve
    "The Hunters fanned out and put as much distance between each other as possible."
    "That seemed like a wise decision, so I did the same."
    "Getting shot by a rocket launcher or a shotgun wasn’t part of the plan."
    scene ep010_hunt_pens_jungle with dissolve
    "Finding the beast was going to be difficult in the vast jungle, but luckily we’d received some intel on the possible whereabouts of the monster."
    "Riding the calgound certainly was a speedy way to cross the jungle."
    if ep010_raene_talk:
        "The excursion together with Raene certainly helped me navigate the terrain with more ease."
    scene ep010_hunt_pens_jungle_cliff with dissolve
    "The supposed location of the beast took me up a steep cliff."
    "That’s when I heard a blood-curdling scream."
    menu:
        "[gr]Investigate" if True:
            $ ep010_hunt_investigate = True
            "The scream had sounded quite close, so I decided to check out the situation."
            scene ep010_hunt_pens_jungle_cliff_alt with dissolve
            "It had definitely been a woman’s voice, so it was probably one of my fellow Hunters."
            "My suspicions were confirmed when I entered a grassy clearing and saw what had caused the call of distress."
            scene ep010_tentacles_alt with dissolve
            if ep008_commander_sex:
                "The Acarhyn named Athryn was tangled up in what looked like some sort of vines."
            elif True:
                "One of the Acarhyn warriors was tangled up in what looked like some sort of vines."
                "With a shock I came to realize she was the same one who'd stabbed Kit back on Lanan."
                "I hadn't recognized her in the line up of Hunters at the start."
                "Seeing her hanging helpless and entangled in all those plants did seem like a small measure of vindication."
            "What made the situation even weirder was the fact that the girl was completely naked."
            scene ep010_tentacles_alt_closeup with dissolve
            "The vines were wriggling and growing around her, holding her ever tighter."
            "I whirled and nearly shot the Acarhyn who’d crept up on me."
            scene ep010_tentacles_hunter with dissolve
            "She was the other Hunter belonging to the warrior caste."
            $ woman_name = "Hunter"
            woman "Asret Tangle...{w} She’s in big trouble."
            c "She’s going to be strangled, isn’t she?"
            scene expression eye_blink("images/ep010/ep010_tentacles_hunter_closeup") with dissolve
            woman "No, nothing as lethal as that."
            woman "In a moment she’s going to stop struggling, giving in to the Asret Tangle."
            woman "The plant will penetrate her and deposit its seed."
            scene ep010_tentacles_hunter_alt with dissolve
            woman "It’s harmless, but the breeding will leave her unresponsive for a long while."
            menu:
                "Rescue her [RahiaPath]" if True:
                    $ ep010_hunt_rescue = True
                    if ep008_commander_sex:
                        "Despite the fact that she'd maimed Kit I couldn't just leave her hanging there."
                    c "We have to do something, cut down the plant or something!"
                    scene expression eye_blink("images/ep010/ep010_tentacles_hunter_closeup_doubt") with dissolve
                    woman "If we leave her be, it’s one less competitor in the Hunt."
                    c "I don’t care."
                    scene expression eye_blink("images/ep010/ep010_tentacles_hunter_closeup_serious") with dissolve
                    if ep010_warrior_alliance:
                        woman "Alright, I’ll help you cut her down."
                        woman "Be careful for any vines that might spring up around her and blast them off as close to the ground as possible."
                    elif True:
                        woman "Do what you will."
                    scene ep010_tentacles with dissolve
                    "The vines were slithering all over the warrior’s naked body now."
                    "She had her eyes closed and whimpered."
                    scene ep010_tentacles_closeup with dissolve
                    "When one of the vines circled around one of her breasts, she let out a short cry, tinged with slowly awakening lust."
                    if ep010_warrior_alliance:
                        scene ep010_tentacles_blast with vpunch
                    elif True:
                        scene ep010_tentacles_blast_solo with vpunch
                    if ep010_warrior_alliance:
                        "Right at that moment we both aimed at the vines and shot several of them to smithereens."
                    elif True:
                        "Right at that moment I aimed at the vines and shot several of them to smithereens."
                    "The plant lost most of its grip on the girl and she nearly dropped to the ground."
                    if ep010_warrior_alliance:
                        scene ep010_tentacles_blast_alt with vpunch
                    elif True:
                        scene ep010_tentacles_blast_solo with vpunch
                    if ep008_commander_sex:
                        "Another series of well-placed shots and Athryn was free."
                    elif True:
                        "Another series of well-placed shots and the warrior was free."
                    scene ep010_tentacles_blast_post with dissolve
                    if ep010_warrior_alliance:
                        "She fell onto the grass and we rushed towards her."
                        "With some effort, we managed to pull her out of the grassy clearing."
                    elif True:
                        "She fell onto the grass and I rushed towards her."
                        "With some effort, I managed to pull her out of the grassy clearing."
                    scene ep010_tentacles_blast_post_calgound with dissolve
                    "That’s when I noticed her calgound."
                    if ep010_warrior_alliance:
                        "We managed to drape her across the saddle of the mount."
                        "My fellow Hunter gave the beast a slap on the back and it sprinted in the general direction of the Citadel."
                    elif True:
                        "I managed to drape her across the saddle of the mount."
                        "I slapped the beast on the back and it sprinted in the general direction of the Citadel."
                    scene ep010_tentacles_blast_post_calgound_run with dissolve
                    "I could only hope she’d make it back in one piece."
                    if ep010_warrior_alliance:
                        scene expression eye_blink("images/ep010/ep010_tentacles_blast_post_calgound_hunter") with dissolve
                        woman "She’ll be fine."
                        woman "See you around."
                        "And then she was gone."
                        if ep008_commander_sex:
                            "Luckily she’d been honorable enough not to start a fight with me after saving Athryn."
                        elif True:
                            "Luckily she’d been honorable enough not to start a fight with me after saving her fellow warrior."
                        "I found my mount again and got back on the trail."
                "Keep watching \n[gr][[Plant Sex, Rahia Path]" if True:
                    "Fascinated, I kept watching the girl as more of the vines covered her."
                    "I didn’t even notice the other warrior slipping away into the jungle."
                    scene ep010_tentacles with dissolve
                    if ep008_commander_sex:
                        "The vines were slithering all over Athryn’s naked body now."
                    elif True:
                        "The vines were slithering all over the warrior's naked body now."
                    "She had her eyes closed and whimpered."
                    scene ep010_tentacles_closeup with dissolve
                    "When one of the vines circled around one of her breasts, she let out a short cry, tinged with slowly awakening lust."
                    call ep010_tentacle_sex from _call_ep010_tentacle_sex

                    "Satisfied by their prey, the tentacles seemed to have fled to whatever place they normally hid."

                    menu:
                        "Leave her" if True:
                            $ ep010_athryn_leave = True
                            if ep008_commander_sex:
                                "I didn't feel any urge to help her, considering what she did to Kit."
                            elif True:
                                "Her semi-conscious state would probably last for a few hours, which meant one less Hunter to worry about."
                            "So I just left her lying there."
                        "Take her away [RahiaPath]" if True:
                            $ ep010_hunt_rescue = True
                            scene ep010_tentacles_post_cum with dissolve
                            if ep008_commander_sex:
                                "I cautiously approached Athryn."
                            elif True:
                                "I cautiously approached the warrior."
                            "When nothing shot out of the ground I crossed the final distance towards her."
                            "With some effort, I managed to pull her out of the grassy clearing."
                            scene ep010_tentacles_blast_post_calgound with dissolve
                            "That’s when I noticed her calgound."
                            "I managed to drape her across the saddle of the mount."
                            "I slapped the beast on the back and it sprinted in the general direction of the Citadel."
                            scene ep010_tentacles_blast_post_calgound_run with dissolve
                            "I could only hope she’d make it back in one piece."
                "Leave her" if True:
                    c "In that case I say we leave her."
                    scene expression eye_blink("images/ep010/ep010_tentacles_hunter_closeup_serious") with dissolve
                    woman "One less competitor in the Hunt."
                    c "Exactly."
                    scene ep010_tentacles with dissolve
                    "We left Athryn there, covered in vines."
                    "The last thing we heard was a short cry, tinged with slowly awakening lust, as the vines started circling around her breasts."
                    scene ep010_hunt_pens_jungle_cliff_run with dissolve
                    "The other warrior slipped away in the jungle at some point."
                    "I found my mount again and got back on the trail."

            python:
                if "codex_athryn" in locals():
                    codex_athryn = update_codex_entry(codex_athryn, None,
                        [
                            __("An Acarhyn warrior who was present at the attack on Lanan P-10. She stabbed Kit while he was trying to run after Eva as she was being dragged away."),
                            __("The warrior was later encountered in the Acarhyn Citadel as one of the commander's lovers."),
                            __("Athryn also partook in the Hunt and had an unfortunate encounter with a plant-based lifeform.")

                        ],
                    )
        "Head onwards" if True:

            "Considering the relative quiet preceding the scream, the incident was unlikely to be related to the presence of the beast."
            "Maybe one of the Hunters had fallen prey to something else."
            scene ep010_hunt_pens_jungle_cliff_run with dissolve
            "I decided to press on."

    "Following the track on the calgound became increasingly difficult."
    scene ep010_hunt_pens_jungle_cavern with dissolve
    "At last we arrived at the entrance of what looked like a cave or tunnel through the rocks."
    "The man-made opening was too small for the calgound, so I decided to head on without it."
    scene ep010_hunt_pens_jungle_tunnel with dissolve
    "It turned out to be a long tunnel through the mountain."
    "The rocky floor of the corridor was treacherously slick from the continuous dripping of moisture from the ceiling."
    play music "music/hunted.ogg" fadeout 4 fadein 1.0
    "I could barely see in the dark, but right when I started wishing I’d brought a torch, the light of the tunnel’s other end came seeping through."
    scene ep010_hunt_acarhyn_ambush with dissolve
    "Two figures stepped into view when I was about to quicken my step and exit the tunnel."
    scene ep010_hunt_acarhyn_ambush_alt with vpunch
    "Instinctively I ducked, and the shots fired by what turned out to be two women flew over my head."
    "They wore unadorned black clothing, but the distinctive design clearly identified them as belonging to the priest caste."
    "The women had me pinned and would surely kill me after they’d reloaded their weapons."
    with vpunch
    with vpunch
    "Just when I’d made the decision to do a suicidal dash past my attackers, several shots were fired."
    scene ep010_hunt_acarhyn_ambush_dead with dissolve
    "At first I thought those bullets were intended for me, but instead I saw both women slump to the ground."
    scene ep010_hunt_acarhyn_ambush_av_ki with dissolve
    "Moments later, Aven and Kit stepped into view, kicking away the guns my assailants had dropped to the ground."
    c "That was close."
    scene ep010_hunt_acarhyn_ambush_av_ki_closeup with dissolve
    av "We spotted those women a while back, looked like they were up to no good."
    ki "The monster is supposed to be at this side of the mountain."
    c "You’ve seen it?"
    scene expression eye_blink("images/ep010/ep010_hunt_acarhyn_ambush_ki_closeup") with dissolve
    ki "No, but judging from the noise, there’s something very big out there."
    ki "Now, I think we have to leave before we’re seen with you."
    c "Right, thanks for the assist, guys."
    ki "Anytime."
    scene expression eye_blink("images/ep010/ep010_hunt_acarhyn_ambush_av_closeup") with dissolve
    av "Take care, [p_name_short]."
    "We went in opposite directions and I made my descent to a stream fed by a waterfall below."
    scene ep010_hunt_stream with vpunch
    "The ground trembled and an ear-splitting roar resounded through the jungle."
    if ep008_na_expedition:
        "It was the same sound I’d heard when we were at the breeding grounds of the unfortunate Eetu."
    "I kept moving towards the sound, despite every instinct desperately telling me not to."
    scene ep010_hunt_acarhyn_tree_alt with dissolve
    "A body was strewn across a couple of rocks."
    "It was the Acarhyn carrying the rocket launcher, her body mangled into a bloody mess."
    scene ep010_hunt_stream_alt with vpunch
    "I didn’t have time to pause, because another deafening howl ripped through the wilderness."
    "The beast was close, very close."
    "I advanced further, weapon at the ready."
    scene ep010_beast_alt with dissolve
    "Despite being prepared for anything, the shock of seeing the beast for the first time nearly rattled me to the core."
    "I’m not sure I knew what to expect, but a giant angry bug wasn’t really on my list."
    scene ep010_beast with vpunch
    "The thing towered over everything, crushing entire swaths of jungle under its step."
    "Though my laser rifle had seemed impressive when I selected it, I was pretty sure it wouldn’t even make a dent in the bug’s carapace."
    "I needed something bigger."
    "Luckily, the beast hadn’t noticed me yet, despite me blundering almost squarely into its path."
    "The bug probably relied on its hearing, touch or smell rather than its vision."
    scene ep010_hunt_acarhyn_tree with dissolve
    "I slinked back towards the stream where the Acarhyn lay."
    "Prying the rocket launcher loose took some effort, but I finally had the thing free of the Acarhyn corpse without being detected by the blundering monster."
    if ep010_warrior_alliance:
        scene ep010_hunt_acarhyn_bridge_alt with dissolve
    elif True:
        scene ep010_hunt_acarhyn_bridge with dissolve
    woman "Stand back!"
    "Of course, one of my colleagues had to ruin the whole thing."
    "Standing on a makeshift bridge across the stream, an Acarhyn trained her weapons on me."
    "There was quite some distance between me and her, so I decided to risk running away."
    if ep010_priest_alliance:
        "Besides, she was carrying a melee weapon, or so I thought."
        scene ep010_hunt_acarhyn_bridge_attack with vpunch
        "Turns out, the glowing ends of the glaive weren’t just for show and several energy bolts came scorching past me."
    elif True:
        scene ep010_hunt_acarhyn_bridge_attack_alt with vpunch
        "She fired off several rounds in my direction, none of them hit."
    play music "music/pariah.ogg" fadeout 4 fadein 1.0
    scene ep010_hunt_launcher with dissolve
    "Splashing through the water, I hoisted the heavy weapon on my back."
    if ep010_priest_alliance:
        "The Acarhyn was now in pursuit, but seemed to realize the beast was near and didn’t fire off any bolts."
    elif True:
        "The Acarhyn was now in pursuit, but seemed to realize the beast was near and didn’t fire at me."
    scene ep010_hunt_launcher_beast with dissolve
    "I approached the beast, attempting to circle around it and lose the Acarhyn in the process."
    "My tactic seemed to pay off, until I was nearly at the back of the insectoid monster."
    if ep010_warrior_alliance:
        scene ep010_hunt_launcher_beast_priest_alt with dissolve
    elif True:
        scene ep010_hunt_launcher_beast_warrior_alt with dissolve
    "It suddenly stopped its rampage through the jungle and stood eerily still."
    "I saw its snout and antennae vibrate, clearly sniffing out any prey in the vicinity."
    if ep010_warrior_alliance:
        scene ep010_hunt_launcher_beast_priest with dissolve
    elif True:
        scene ep010_hunt_launcher_beast_warrior with dissolve
    "Right when I thought it had spotted me, the Acarhyn decided to become a hero and charged."
    "As I suspected, her light weaponry didn’t even scratch the beast’s carapace."
    "It did, however, make it extremely angry."
    "The Acarhyn darted around the bug, evading the creature’s snapping mandibles, probably slowly realizing she’d made a terrible mistake."
    "The rocket launcher had two charges left, so I had to make them count."
    if ep010_warrior_alliance:
        scene ep010_hunt_launcher_beast_priest_attack_alt with dissolve
        "The beast had cornered the hapless Acarhyn, who was frantically firing her energy bolts and finding she couldn’t harm the creature."
    elif True:
        scene ep010_hunt_launcher_beast_warrior_attack with dissolve
        "The beast had cornered the hapless Acarhyn, who was frantically firing her dual shotguns and finding she couldn’t harm the creature."
    scene ep010_hunt_launcher_beast_rocket with dissolve
    "I shot a rocket at point blank range and scored a hit."
    scene ep010_hunt_launcher_beast_rocket_hit with vpunch
    "The impact was followed by a terrible howl as the explosion tore away at the chitinous hide of the creature."
    "My attack left a smoldering hole, but the beast was still standing."
    "It shrieked and howled like a banshee."
    "The Acarhyn thought she’d had a clear shot now, but her attack was interrupted suddenly by the enraged creature."
    if ep010_warrior_alliance:
        scene ep010_hunt_launcher_beast_priest_dead with vpunch
    elif True:
        scene ep010_hunt_launcher_beast_warrior_dead with vpunch
    "She was swept up in the beasts terrible mandibles and flung against a nearby tree."
    "The crunch of broken bones was sickening, but I had no time to even parse what had happened, because the creature rushed towards me."
    scene ep010_hunt_launcher_beast_pounce with vpunch
    "The next rocket was already in the chamber and I was about to aim, when the monster slammed itself bodily onto the ground."
    "I managed to duck away and avoid the worst of the attack, but the shockwaves the creature sent through the jungle made it hard to stand up again."
    "The beast was already on its hind legs when I managed to stand up."
    "It raised its entire body for another terrible attack."
    scene ep010_hunt_launcher_beast_rocket_aim with dissolve
    "I decided not to wait this time and brought the rocket launcher upwards."
    "Aiming at its soft belly, I fired the last of my rockets."
    scene ep010_hunt_launcher_beast_rocket_alt with vpunch
    "It struck home, blowing a large hole in its abdomen."
    "Another gurgling howl, which shook me to the core."
    scene ep010_hunt_launcher_beast_death with vpunch
    "Fear gripped me, as the creature seemed to prepare to follow through on its initial attack."
    "The light died in its eyes before it could complete another slam."
    scene ep010_hunt_launcher_beast_death_alt with vpunch
    "Instead the monster’s body fell to the ground, sending shockwaves that were much less terrible than before."
    "I kept my ground and when the dust settled approached the creature."
    "It was well and truly dead."
    "Before the start of the Hunt, I thought I’d take the head of the creature with me as a token of my victory."
    "The sheer size of the thing made that quite impossible."
    "I settled for one of its eyes."
    if ep010_warrior_alliance:
        scene ep010_hunt_launcher_beast_eyes with dissolve
        "Using the glaive of the dead Acarhyn, I cut out the eyeball and let the corpse burn."
        scene ep010_hunt_launcher_beast_burn with dissolve
    elif True:
        scene ep010_hunt_launcher_beast_eyes_alt with dissolve
        "Using the knife of the dead Acarhyn, I cut out the eyeball and let the corpse burn."
        scene ep010_hunt_launcher_beast_burn_alt with dissolve
    "There was only one Hunter left, but I didn’t want her running into remains of the beast, retrieving a trophy and stealing my victory by arriving at the Citadel before me."
    if ep010_warrior_alliance:
        scene ep010_hunt_end with dissolve
    elif True:
        scene ep010_hunt_end_alt with dissolve
    "The journey back was one of the most shitty experiences ever."
    "I was exhausted, covered in beast slime and really wanted a proper meal."
    "After a few hours, I reached the outer perimeter of the Citadel."

    play music "music/sanctuary.ogg" fadeout 4 fadein 1.0

    if ep010_warrior_alliance:
        scene ep010_hunt_end_pens with dissolve
    elif True:
        scene ep010_hunt_end_pens_alt with dissolve
    "A crowd had already gathered in the beast pens and my friends started cheering as soon as I stepped across the pen’s threshold."
    if ep010_hunt_rescue:
        scene ep010_hunt_end_athryn with dissolve
        if ep008_commander_sex:
            "Athryn had made her way back to the Citadel and sat naked on the ground, still groggy from her experience in the jungle."
        elif True:
            "The Acarhyn girl had made her way back to the Citadel and sat naked on the ground, still groggy from her experience with the vines in the jungle."
    if ep010_warrior_alliance:
        scene ep010_hunt_end_wounded_warrior with dissolve
    elif True:
        scene ep010_hunt_end_wounded_priest with dissolve
    "The fourth Acarhyn had a chest wound that was being treated by several physicians."
    "I stumbled across the perimeter towards Erylin and retrieved the eyeball."
    "Holding the slimy organ in the air I proclaimed my victory loudly for every Acarhyn to hear."
    if ep010_warrior_alliance:
        scene ep010_hunt_end_eye with dissolve
    elif True:
        scene ep010_hunt_end_eye_alt with dissolve
    c "I hereby claim the Victory of the Hunt."
    scene ep010_hunt_end_erylin with dissolve
    er "Your claim has been acknowledged, Hunter."
    er "The authenticity of your Trophy will be verified."
    er "The Ceremony will commence in three hours."
    scene ep010_hunt_end_exit with dissolve
    "All Acarhyn now cheered and I was guided towards the Citadel with the promise of a bath and treatment for any wounds I had sustained during the Hunt."
    scene black with fade
    "After my bath I retired to my quarters to prepare for the ceremony."
    "Not long after I returned, there was knock on my door."
    scene ep010_na_li_av with dissolve
    "Nadya, Aven and Lilly were standing in the doorway."
    na "May we come in?"
    scene ep010_na_li_av_embrace with vpunch
    l "You did it!"
    "Lilly was ecstatic and her enthusiasm was infectious."
    if game.is_special or aven_romance:
        "Kissing her would make for a rather awkward situation, but I had trouble holding back."
    scene expression eye_blink("images/ep010/ep010_na_li_av_closeup_na") with dissolve
    na "Do you know what kind of creature you hunted?"
    c "I’m not sure, some kind of enormous bug."
    na "An insect?"
    c "Something like that."
    c "It didn’t like rockets though."
    scene expression eye_blink("images/ep010/ep010_na_li_av_closeup_av") with dissolve
    av "You shot it with a rocket launcher?"
    c "I did."
    c "Seemed the most effective weapon at the time."
    av "I was so scared after we cleared up that ambush for you, the monster seemed so close."
    c "It was, I’m glad you all got to safety before it decided to show its face."
    scene expression eye_blink("images/ep010/ep010_na_li_av_closeup_li") with dissolve
    l "What’s next?"
    c "A ceremony where they’ll crown me as Hero of the Acarhyn."
    if ep010_warrior_alliance:
        c "Rahia is very keen on appearing next to me on the podium."
    elif True:
        c "Erylin is very keen on appearing next to me on the podium."
    scene expression eye_blink("images/ep010/ep010_na_li_av_closeup_av") with dissolve
    av "We’ll cheer you on."
    c "Having my own cheerleader squad will surely make the experience more bearable."
    scene expression eye_blink("images/ep010/ep010_na_li_av_closeup_na") with dissolve
    na "We’ll let you get some rest."
    scene ep010_na_li_av_post with dissolve
    "After the women had left, I decided to get some sleep."
    scene black with fade
    "I awoke to the sound of bells, just half an hour before the ceremony."
    "The Acarhyn probably wouldn’t appreciate it if their newfangled Hero were to appear late, so I jumped out of bed and ventured towards the courtyard."
    return

label ep010_aven:
    "After meeting her during lunch hour in the dining hall of the Citadel, Aven asked me to meet her in her quarters."
    scene ep010_aven_door with dissolve
    "The door to her quarters was unlocked and I stepped inside after knocking."
    scene ep010_aven_balcony with dissolve
    c "That balcony sure is one of your favorite places here, isn’t it?"
    scene expression eye_blink("images/ep010/ep010_aven_balcony_closeup") with dissolve
    av "Well, it’s either this or that dreary courtyard."
    c "You could explore the jungle?"
    if ep008_na_expedition:
        av "After what happened to you and mother, not likely."
    elif True:
        av "After what happened, not likely."
    c "I submitted my application for the Hunt, so I’m going into the jungle either way."
    scene expression eye_blink("images/ep010/ep010_aven_balcony_closeup_serious") with dissolve
    av "Right, about that."
    av "Officially, the rules don’t permit helping the Hunters, right?"
    c "Yup, that’s what Caese told us."
    scene expression eye_blink("images/ep010/ep010_aven_balcony_closeup_smile") with dissolve
    av "But everybody does it anyway."
    c "As long as they don’t get caught."
    av "Good."
    av "Kit and I will have your back out there as soon as the Hunt starts."
    c "But you don’t have any weapons?"
    scene expression eye_blink("images/ep010/ep010_aven_balcony_closeup_serious") with dissolve
    if ep010_warrior_alliance:
        av "Your alliance with Rahia has some benefits, so the weapons are taken care of."
    elif ep010_priest_alliance:
        av "Your alliance with Erylin has some benefits, so the weapons are taken care of."
    elif True:
        av "Caese is willing to help us on that front, so any weapons should be taken care of."
    c "Just be careful."
    scene expression eye_blink("images/ep010/ep010_aven_balcony_closeup") with dissolve
    av "The same applies to you."
    if aven_romance:
        scene ep010_aven_kiss with dissolve
        "Suddenly Aven was in my arms and we were kissing."
        scene expression eye_blink("images/ep010/ep010_aven_kiss_closeup") with dissolve
        av "I don’t want to lose you."
        c "You won’t."
        c "In fact, you’ll be dating the Hero of the Acarhyn when this is all over."
        scene expression eye_blink("images/ep010/ep010_aven_kiss_closeup_smile") with dissolve
        av "I’m glad you still feel confident."
        c "It’s either that or complete and utter despair."
        av "Right, I’d go with confidence too."
        scene ep010_aven_kiss_alt with dissolve
        "We kissed again and gazed out over the jungle, our arms wrapped around each other."
    elif True:
        scene expression eye_blink("images/ep010/ep010_aven_balcony_closeup_smile") with dissolve
        av "Take care, [p_name_short]."
        c "You too, see you in the jungle."
    return

label ep010_lilly:
    scene ep010_lilly with dissolve
    "Lilly caught my eye as she was walking on the battlements of the Citadel."
    scene expression eye_blink("images/ep010/ep010_lilly_alt") with dissolve
    if game.is_special:
        c "Hey sis, wait up!"
    elif True:
        c "Hey Lilly, wait up!"
    scene expression eye_blink("images/ep010/ep010_lilly_closeup_smile") with dissolve
    "Lilly turned and smiled."
    if lilly_romance:
        c "I’d kiss you right here and now, but we seem to have an audience down below."
        l "I’ll go for something less exposed when taking an aimless stroll next time."
    elif True:
        c "Inspecting the defenses?"
        l "Yes, for lack of anything better to do."
    scene expression eye_blink("images/ep010/ep010_lilly_closeup") with dissolve
    l "Did you make any progress enlisting help with the Hunt?"
    if ep010_warrior_alliance or ep010_priest_alliance:
        if ep010_warrior_alliance:
            c "Yes, I’ve accepted Rahia’s invitation."
        elif True:
            c "Yes, I’ve accepted Erylin’s invitation."
        scene expression eye_blink("images/ep010/ep010_lilly_closeup_doubt") with dissolve
        l "You have?"
        l "I’m sure there’ll be trade-offs, but I think it’s for the best."
        l "You can’t go at this alone."
        if ep010_warrior_alliance:
            c "Working together with Erylin wasn't an option."
            c "I mean, even her hidden agenda has its own hidden agenda..."
        elif True:
            c "Working together with Rahia wasn’t an option."
            c "She kidnapped Eva and I just don't think she has the political acumen to get on top of things."
            c "On the other hand, even Erylin's hidden agenda has a hidden agenda."
        scene expression eye_blink("images/ep010/ep010_lilly_closeup") with dissolve
        l "I trust you’ve made the right decision."
        c "Thanks for the support."
    elif True:
        if (ep010_erylin_talk or ep010_rahia_talk) and (not ep010_rahia_alliance_options and not ep010_erylin_alliance_options):
            c "I’ve decided to go at it alone."
            c "I have no interest in getting caught up in Acarhyn power politics."
            c "I mean, even Erylin's hidden agenda has its own hidden agenda..."
            scene expression eye_blink("images/ep010/ep010_lilly_closeup_serious") with dissolve
            l "I can only imagine..."
            l "But forgoing any alliance is risky, you’d be all alone in the jungle."
            c "Pretty much, yes."
        elif True:
            c "I’m not sure yet."
            l "There are three options, right?"
            scene expression eye_blink("images/ep010/ep010_lilly_closeup_serious") with dissolve
            l "Going solo, allying with the warriors or throwing your lot in with that priestess."
            c "Yup, pretty much."
            l "Going at it alone is a risky decision."
        l "On the other hand, you won’t be indebted to either the warriors or the priesthood."
        c "Exactly, but it’s hard to gauge how difficult the Hunt is without any backup."
        l "I’d assume the worst."
        scene expression eye_blink("images/ep010/ep010_lilly_closeup") with dissolve
        l "Out of curiosity, which of factions seems most trustworthy to you?"
        c "I’m not sure, I mean they’re both scheming and vying for control of the Acarhyn."
        scene expression eye_blink("images/ep010/ep010_lilly_closeup_doubt") with dissolve
        l "But who’d be the most reliable choice in your opinion?"
        c "Rahia seems to be the most straightforward so far."
        c "Erylin is a political animal, through and through."
        scene expression eye_blink("images/ep010/ep010_lilly_closeup") with dissolve
        l "So much less straightforward?"
        c "Yes, very much so, her hidden agenda has its own hidden agenda."
        l "She might be more pragmatic though."
        c "I’m not sure."
        scene expression eye_blink("images/ep010/ep010_lilly_closeup_smile") with dissolve
        l "Go with what feels right, [p_name_short]."
        l "I trust you’ll make the right decision."
        c "Thanks for the support."
    if lilly_romance:
        scene expression eye_blink("images/ep010/ep010_lilly_closeup") with dissolve
        l "Of course."
        scene expression eye_blink("images/ep010/ep010_lilly_closeup_smile") with dissolve
        l "Though I have a bit of a hidden agenda too."
        c "Oh?"
        l "I’d really like to be kissed by a certain boy right now."
        "We’d arrived in the shadow of one of the sentry towers."
        "Though still somewhat exposed, the shadows would hopefully shield us from any unwanted onlookers."
        scene ep010_lilly_kiss with dissolve
        if game.is_special:
            "Pushing her gently against the stone wall, I met my sister’s parted lips."
        elif True:
            "Pushing her gently against the stone wall, I met my girlfriend’s parted lips."
        "A passionate kiss followed, our tongues eventually engaged in a fierce dance."
        scene expression eye_blink("images/ep010/ep010_lilly_kiss_closeup") with dissolve
        l "Be extra careful out there, [p_name_short]."
        c "I will, that’s a promise."
    elif True:
        l "Anytime."
        l "Be careful out there, [p_name_short]."
        c "I will, thanks Lilly."
    return

label ep010_vess:
    play music "music/extrapolation.ogg" fadeout 4 fadein 1.0

    scene ep010_vess_empty with dissolve
    "Feeling restless, I was about to head out and wander through the Citadel."
    "A knock on my door forced a change of plans."
    scene expression eye_blink("images/ep010/ep010_vess") with dissolve
    "As soon as I unlocked the door, Vess slipped inside."
    if ep007_v_sleep:
        "She was wearing the red night gown that still haunted my dreams from time to time."
    scene expression eye_blink("images/ep010/ep010_vess_alt") with dissolve
    ve "Sorry to barge in like this."
    c "Don’t worry, I couldn’t sleep."
    scene expression eye_blink("images/ep010/ep010_vess_alt_doubt") with dissolve
    ve "I...{w} Do you have a moment?"
    c "Of course, you shouldn’t have to ask."
    scene expression eye_blink("images/ep010/ep010_vess_alt_sad") with dissolve
    ve "Okay.{w} Right."
    "It clearly took the girl a while to gather her thoughts and I thought it best not to interrupt."
    scene expression eye_blink("images/ep010/ep010_vess_alt_serious") with dissolve
    ve "I’ve thought a lot about what you said back on top of that tower."
    "Vess bit her lip and fell silent again."
    "Her eyes downcast, it was very hard to read her emotions."
    "When she finally looked up to me, she seemed determined."
    ve "I want you."
    scene expression eye_blink("images/ep010/ep010_vess_alt_sad_alt") with dissolve
    ve "Even if it’s just for tonight."
    c "Why only for tonight?"
    ve "I don’t know."
    scene expression eye_blink("images/ep010/ep010_vess_alt_sad_smile") with dissolve
    ve "Please, no more questions, I just want to be with you."
    call ep010_vess_sex from _call_ep010_vess_sex

    $ vess_romance = True

    return

label ep010_ziv:
    play music "music/never-dying.ogg" fadeout 4 fadein 1.0
    "I’d been itching to speak to Ziv ever since we were brutally interrupted in the grove."
    "It took a while to get a response after I knocked on her door, but when it eventually came I nearly tumbled through the doorway."
    scene ep010_ziv with dissolve
    "Ziv was in another state of mind however."
    "Sitting on her bed, she was meditating with closed eyes."
    "She was also completely naked."
    "I paused to take a good look at her majestic presence."
    scene ep010_ziv_closeup with dissolve
    zi "Hey [p_name_short]."
    c "Hey."
    c "I can come back another time."
    scene expression eye_blink("images/ep010/ep010_ziv_closeup_alt") with dissolve
    zi "No need."
    zi "I was hoping you’d stop by."
    zi "I’m sure I’m not the only one who felt our union at the grove was cut too short."
    c "You can say that again."
    zi "Did you get away without incident?"
    if ep009_priestess_bj:
        c "More or less."
    elif True:
        c "I did."
    c "There were some priestesses looking for me."
    zi "Coming to ensnare you in their politics."
    c "Something like that, yes."
    scene expression eye_blink("images/ep010/ep010_ziv_closeup_alt_smile") with dissolve
    zi "However, we were about to kiss again."
    c "We were indeed."
    call ep010_ziv_sex from _call_ep010_ziv_sex
    return

label ep010_thyia:
    scene ep010_thyia with dissolve
    "On my way to the ceremony I came past the quarters assigned to Thyia."
    "The door was open and I could see her unpacking her bag."
    c "Hey you."
    scene expression eye_blink("images/ep010/ep010_thyia_closeup") with dissolve
    th "Hey [p_name_short]."
    th "Seems like I missed all the excitement."
    c "You sure did, though I believe you’re just in time for the ceremony."
    scene expression eye_blink("images/ep010/ep010_thyia_closeup_smile") with dissolve
    th "Wouldn’t miss that for the world."
    th "I’ll hurry to the courtyard as soon as I’m done unpacking."
    c "No rush, I think they’re still setting up the stage."
    c "You just arrived I take it?"
    scene expression eye_blink("images/ep010/ep010_thyia_closeup") with dissolve
    th "An hour ago."
    scene expression eye_blink("images/ep010/ep010_thyia_closeup_sad") with dissolve
    th "It felt a little awkward leaving the Bastard behind."
    c "I’m sure the ship won’t be dismantled overnight."
    c "It has become somewhat of a bargaining chip."
    scene expression eye_blink("images/ep010/ep010_thyia_closeup_serious") with dissolve
    th "That’s never a good thing."
    c "I’m pretty confident they’ll restart the repairs soon."
    scene expression eye_blink("images/ep010/ep010_thyia_closeup") with dissolve
    th "At least they’ve done beautiful work so far."
    c "Can’t wait to see it."
    th "Acarhyn engineering is truly a marvel."
    c "Which is weird, considering they just went through a technological renaissance."
    th "A lot can happen in barely a hundred years."
    c "That’s true."
    c "I’ll let you get settled and we’ll talk later, okay."
    scene expression eye_blink("images/ep010/ep010_thyia_closeup_smile") with dissolve
    th "Deal."
    return

label ep010_tentacle_sex:
    if _in_replay:
        $ ep008_commander_sex = True
    show ep010_tentacles_fuck with dissolve
    "One of the plant’s tentacles had now entered the girls pussy completely, while another penetrated her mouth."
    scene ep010_tentacles_fuck_closeup with dissolve
    if ep008_commander_sex:
        "Athryn moaned with heightened pleasure as the plant fucked her with some force."
    elif True:
        "The warrior moaned with heightened pleasure as the plant fucked her with some force."
    scene ep010_tentacles_fucking with dissolve
    "Another vine had slithered towards her from behind and crept up along her leg towards her ass."
    scene ep010_tentacles_fucking_closeup with dissolve
    "The girl’s eyes widened as the tentacle pushed itself inside her asshole."
    show ep010_tentacles_fuck_alt with dissolve
    "She was now being fucked in her mouth, pussy and ass simultaneously."
    scene ep010_tentacles_fuck_closeup_alt with dissolve
    "The tentacles must have released some kind of aphrodisiac, because her pussy was drenched in her juices."
    scene ep010_tentacles_fuck_orgasm with flash
    with flash
    "Suddenly some of the plants seed pods opened and a semen-like substance erupted from its mouth."
    if ep008_commander_sex:
        "Athryn was quickly covered in cum as the seed pods kept spewing it onto her body."
    elif True:
        "The girl was quickly covered in cum as the seed pods kept spewing it onto her body."
    scene ep010_tentacles_fuck_orgasm_closeup with vpunch
    "Her mouth was pumped full of semen, causing her cheeks to puff up."
    scene ep010_tentacles_fuck_orgasm_belly with dissolve
    "The tentacles inside her pussy and ass were evidently discharging their seed as well."
    scene ep010_tentacles_fuck_orgasm_belly_inflate with dissolve
    if ep008_commander_sex:
        "Athryn’s belly grew to incredible proportions."
    elif True:
        "The warrior’s belly grew to incredible proportions."
    scene ep010_tentacles_fuck_orgasm_belly_inflate_alt with dissolve
    "For a long moment, she seemed almost pregnant with cum."
    scene ep010_tentacles_fuck_orgasm_creampie with vpunch
    "When the tentacles were subtracted from her body, all of the semen inside her was released all at once."
    scene ep010_tentacles_fuck_orgasm_creampie_alt with dissolve
    "A flood of cum streamed out of her pussy and asshole, splashing onto the ground below her."
    scene ep010_tentacles_fuck_orgasm_closeup_alt with dissolve
    "The girl now looked like several men had ejaculated on her over the course of several hours and only then the tentacles seemed satisfied by her."
    "The plant lost most of its grip on the girl and she nearly dropped to the ground."
    scene ep010_tentacles_fuck_orgasm_post with dissolve
    "When the last tentacle left Athryn’s orifices, the girl fell onto the grass."
    "She was drenched in cum, but alive."
    scene ep010_tentacles_fuck_orgasm_post_closeup with dissolve
    "The look on her face was one of complete bliss."
    $ renpy.end_replay()
    return

label ep010_celine_sex:
    scene ep010_celine_kiss with dissolve
    "We kissed and held each other for a long time as we looked out over the jungle."
    "Céline started getting frisky after a while."
    "My cock stirred, when she started to undress herself."
    scene ep010_celine_naked_alt with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "The glance she cast me over her shoulder spoke volumes."
    scene ep010_celine_naked with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    ce "I want you to have me, right here and now."
    "I didn’t need any further encouragement and quickly shed my clothing as well."
    scene ep010_celine_naked_kiss_alt with dissolve
    "Céline was back in my arms in moments, and we kissed again."
    scene ep010_celine_naked_kiss with dissolve
    "The petite girl pressed herself wantonly against my chest as my eager hands traced the curve of her tight butt."
    "She gasped when I kneaded her firm breasts, the palm of my hand rough against her soft nipples."
    show ep010_celine_hj with dissolve
    "Her hand had found my erection and she was jerking me with determined strokes while our tongues performed an intricate dance."
    scene ep010_celine_hj_alt with dissolve
    "Céline milked my cock until the first droplets of precum oozed out of the tip."
    "She used the moisture to lubricate my cock and was about to intensify her manual attention, but I slipped from her grasp"
    scene ep010_celine_naked_kiss_belly_closeup with dissolve
    "I lowered myself to my knees, kissing her toned abdomen, wanting a taste of her pussy."
    scene ep010_celine_naked_kiss_belly with dissolve
    "My girl knew what I was up to and awaited the slow journey towards her slit with great expectation."
    scene ep010_celine_pussy_lick with dissolve
    "My tongue found the salt of her lips making Céline shiver as I licked her tight cunt."
    ce "Oh fuck!{w} Oh, right there!"
    scene ep010_celine_pussy_lick_closeup with dissolve
    "I found her swollen clit without fail and massaged it with powerful strokes causing the girl to tremble on her legs."
    "Céline stopped me, lust burning in her eyes."
    scene ep010_celine_penetrate_closeup with dissolve
    ce "I want your hard cock all the way inside me."
    c "Dirty girl!"
    scene ep010_celine_penetrate with dissolve
    "She smiled as I stood up and made her lean against the artillery."
    "I pulled up her leg and pressed the tip of my dick against her entrance."
    ce "I’m so wet for you right now."
    scene ep010_celine_penetrate_alt with dissolve
    "She surely was, because when I slid my cock across her pussy lips, it came back covered with her moisture."
    "Céline was extremely horny, her body twisting in anticipation, longing to get speared by my throbbing cock."
    "I teased her by pegging her cunt, never going further than a few quarter-inches, just to feel her tightness close around me."
    "It was a wonderful feeling that got Céline all worked up, causing her to beg in frustration."
    scene ep010_celine_penetrate_closeup with dissolve
    ce "Fuck me, [p_name], fuck me please!{w} Don’t hold back!"
    scene ep010_celine_fuck_closeup_alt with vpunch
    "I decided I’d tormented the girl long enough and let her take the entirety of my shaft."
    "Céline moaned and tightened her grip on the gun turret, her legs turning into to jelly for a brief moment."
    scene ep010_celine_fuck_closeup with dissolve
    ce "That’s it!{w} Oh that feels so good!"
    show ep010_celine_fuck_alt with dissolve
    "With her leg hoisted on my arm, I could plunge my cock balls-deep inside her vagina."
    "It made for an amazing experience, fucking her harder each time she asked for it."
    scene ep010_celine_fuck with dissolve
    "Céline was dripping wet by now and had to steady herself against the turret in order to take the onslaught of my thrusts."
    "Her breasts danced to the rhythm of our lovemaking."
    scene ep010_celine_fucking_ass_alt with dissolve
    "Holding Céline like that put a strain on us both, so I made her bend over against the turret."
    "Céline wiggled her ass seductively and I grabbed the girl by her sides."
    "I admired her small, but firm ass."

    menu:
        "Try anal [gr][[Anal]" if True:
            $ ep010_ce_anal = True
            scene ep010_celine_fucking_ass with dissolve
            "As I tried to reenter her, the tip of my cock came to rest against the folds of her anus."
            scene ep010_celine_fucking_closeup with dissolve
            c "Do you want to try?"
            ce "Try...{w} my ass?"
            ce "I’ve never done that before."
            scene ep010_celine_fucking_closeup_fear with dissolve
            "Céline looked a little afraid, but I also detected a glint of curiosity."
            c "We’ll take it slow."
            c "Do you trust me?"
            ce "I trust you, [p_name]."
            scene ep010_celine_fucking_ass_penetrate with dissolve
            "Céline’s body tensed up as I grabbed hold of her ass and pushed the tip of my cock against her asshole."
            c "Relax, I won’t hurt you."
            scene ep010_celine_fucking_ass_penetrate_closeup with dissolve
            ce "Are you sure?"
            c "Just tell me when it hurts and we’ll stop immediately."
            ce "Okay."
            "I’m not sure if that last comment made her feel more comfortable, but I decided to go on."
            scene ep010_celine_fucking_ass_penetrate with dissolve
            "Her anus parted under the pressure of my dick."
            scene ep010_celine_fucking_ass_penetrate_closeup_alt with dissolve
            ce "Oh fuck!{w} Fuck!"
            "Céline gritted her teeth and whimpered, but didn’t tell me to stop."
            "She held firm against the gun turret as I slowly slid my cock deeper inside her ass."
            scene ep010_celine_fucking_ass_penetrate_alt with dissolve
            "I now filled her to the rim of my cock’s head and slowly thrust in and out."
            ce "Fuck no!{w} That hurts.{w} Stop [p_name_short], stop!"
            scene ep010_celine_fucking_ass_penetrate_gape with dissolve
            "Very slowly, I inched out of her tight ass."
            scene ep010_celine_fucking_stand_closeup_sad with dissolve
            ce "I’m sorry, [p_name_short], but I don’t think I’m ready yet."
            c "Don’t apologize."
            c "I was too eager."
            ce "No, I really want this too."
            ce "Just let me practice a little, okay?"
            c "That sounds like something I’d like to see."
            scene ep010_celine_fucking_stand_closeup_smile with dissolve
            ce "I bet..."
            ce "Now I really want you inside me again."
        "Keep fucking her" if True:
            ce "Please [p_name], I want you inside me again."
            scene ep010_celine_fucking with dissolve
            "I entered her again and fucked her like she asked me to."
            "Her ass quivered with every thrust I made."
            scene ep010_celine_fucking_alt with dissolve
            ce "That’s it, that’s it!"
            "The girl’s tight pussy drove me right near the edge."
            "Suddenly I longed for Céline to see me fucking her."
            "I made her spin around and let her lean against the turret."
            scene ep010_celine_fucking_stand_closeup_smile with dissolve

    "Facing me, Céline offered her cunt."
    scene ep010_celine_fucking_stand with dissolve
    "I drove into her with force, as she dug her nails into my back."
    scene ep010_celine_fucking_stand_closeup_alt with dissolve
    ce "Fuck me hard, [p_name], I want to feel all of you."
    scene ep010_celine_fucking_stand_alt with dissolve
    "The girl leaned heavily against the turret and grabbed one of the supports."
    scene ep010_celine_fucking_wide with dissolve
    "She cried lustfully into the night, not caring if anybody heard us."
    "I fucked her hard, my cock slapping into her dripping wet cunt all the way to the root."
    scene ep010_celine_fucking_stand_closeup with dissolve
    "Her tight pussy had me ready in no time."
    menu:
        "Creampie \n[gr][[Celine Creampie]" if True:
            $ ep010_ce_creampie = True
            scene ep010_celine_fucking_stand_closeup_alt with dissolve
            ce "Cum inside me, [p_name_short]. I want all of your warm cum inside me!"
            scene ep010_celine_fucking_stand_alt with vpunch
            "Gripping her tightly, I unloaded inside her vagina."
            scene ep010_celine_fucking_creampie with flash
            with flash
            "My cock was still spurting cum when it slipped out of her wet slit, followed by an oozing of warm seed."
        "Body" if True:
            scene ep010_celine_fucking_stand_alt with vpunch
            "Gripping her tightly, I fucked her until the very moment I was ready to unload."
            scene ep010_celine_fucking_body with flash
            with flash
            "Slipping from her wet slit, my cock spurted cum all over her abdomen."
        "Facial" if True:
            scene ep010_celine_kneel with dissolve
            "I made Céline kneel quickly and she started licking my shaft."
            scene ep010_celine_kneel_alt with dissolve
            "Using her hand and tongue, she helped me achieve my orgasm."
            scene ep010_celine_kneel_facial with flash
            with flash
            "I rewarded her hard work by blasting her face with warm seed."
            "Céline swallowed the droplets that splashed into her mouth with relish."
    scene ep010_celine_post with dissolve
    "Still a little shaky on our legs, I took Céline in an embrace, and we exchanged a passionate kiss."
    ce "I love you, [p_name]."
    c "I love you too, Céline."
    if is_patreon() and renpy.has_label("extra_scene_19") and not _in_replay:
        "We just stood there for a long time, the nocturnal wind gently blowing, caressing our naked bodies."
        call extra_scene_19 from _call_extra_scene_19
    elif True:
        "We just stood there for a long time, until the gently blowing nocturnal wind became too cold on our naked bodies."
    $ renpy.end_replay()
    return

label ep010_erylin_sex:
    if _in_replay:
        $ er_name = "Erylin"
        $ keo_name = "Keodele"
        $ ep010_keodele_fucked = False
        $ ep010_erylin_fucked = False
    scene ep010_erylin_keodele_sex with dissolve
    er "Now, Keo, be a good girl and follow my instructions to the letter."
    if game.is_special:
        keo "Yes, mother."
    elif True:
        keo "Yes, mistress."
    er "Undress yourself."
    scene ep010_acolyte_naked_alt with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "Gingerly, the girl slipped out of her acolyte robes."
    "Her back was turned to me and she revealed her muscular yet nubile body to me."
    "I craved to touch her well-toned ass, but kept my distance to let the whole scene play out."
    er "Now turn around, show yourself to [p_name]."
    scene ep010_acolyte_naked with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "The girl did as she was told, though visibly uncomfortable."
    "I admired the muscles rippling through her body."
    "Keodele’s breasts looked firm, her nipples proudly erect."
    scene ep010_acolyte_naked_erylin with dissolve
    if game.is_special:
        "Erylin came to stand behind her daughter."
    elif True:
        "Erylin came to stand behind her acolyte."
    er "Now, [p_name], do you enjoy what you see."
    if game.is_special:
        c "She looks like a nice piece of ass, just like her mother."
    elif True:
        c "She looks like a nice piece of ass, just like her superior."
    er "Oh, we’re going to have so much fun."
    er "Why don’t you slip out of those clothes as well?"
    "I didn’t hesitate and stood naked before both women in seconds."
    scene ep010_acolyte_naked_erylin_alt with dissolve
    "Keodele’s eyes widened at the sight of my growing erection."
    er "Doesn’t that cock look nice and juicy, Keo?"
    scene ep010_acolyte_naked_keo_closeup with dissolve
    if game.is_special:
        keo "It’s so big, mother."
    elif True:
        keo "It’s so big, mistress."
    er "And you’re going to enjoy every inch of it."
    keo "But-"
    scene ep010_acolyte_naked_erylin_alt with dissolve
    er "On your knees."
    keo "I’ve never-"
    scene ep010_acolyte_kneel with dissolve
    "Erylin pushed the whimpering girl to her knees and made her face my throbbing cock which had grown to it’s full size already."
    er "You’re going to be a good girl and suck [p_name]’s cock for me."
    er "Is that understood?!"
    if game.is_special:
        keo "Yes, mother."
    elif True:
        keo "Yes, mistress."
    scene ep010_acolyte_kneel_closeup with dissolve
    if game.is_special:
        er "You have to forgive my daughter, she has lived a rather sheltered life."
    elif True:
        er "You have to forgive Keodele, she has lived a rather sheltered life."
    er "But it’s high time she learned how to pleasure a man."
    if game.is_special:
        "Still holding her daughter’s face, the high priestess pushed the girl towards my shaft."
    elif True:
        "Still holding the acolyte's face, the high priestess pushed the girl towards my shaft."
    scene ep010_acolyte_kneel_alt with dissolve
    "I held my dick before Keodele’s face and she looked at it fearfully."
    er "Open your mouth, dear."
    scene ep010_acolyte_suck with dissolve
    "As I rested my hands on the top of her head, Keodele obeyed and parted her lips."
    "Her breath was warm on the tip of my cock."
    scene ep010_acolyte_suck_alt with dissolve
    er "Just a little further."
    er "That’s it."
    scene ep010_acolyte_sucking with dissolve
    "The head of my dick was now inside the young woman’s mouth."
    if game.is_special:
        "She mumbled something that was ignored by her mother."
    elif True:
        "She mumbled something that was ignored by the head priestess."
    scene ep010_acolyte_sucking_wide with dissolve
    er "Now just suck on that cock, girl."
    show ep010_acolyte_sucking_wide_alt_closeup with dissolve
    "She retched a little as her mouth covered more of my dick."
    show ep010_acolyte_sucking_wide_alt with dissolve
    hide ep010_acolyte_sucking_wide_alt_closeup
    if game.is_special:
        "Erylin guided her daughter’s head slowly along my shaft."
    elif True:
        "Erylin guided her acolyte’s head slowly along my shaft."
    scene ep010_acolyte_sucking_alt with dissolve
    er "Be careful not to hurt [p_name] with your teeth."
    "The warning came just in time, because the girl’s teeth brushed over my sensitive flesh ever so slightly."
    "Keodele evidently had trouble swallowing my cock, as she gagged multiple times, but she kept soldiering on."
    "By now, her saliva clung to my cock in thick strands."
    scene ep010_acolyte_sucking_closeup with dissolve
    if game.is_special:
        "Erylin held her daughter firmly in place, allowing her to breathe at regular intervals."
    elif True:
        "Erylin held her pupil firmly in place, allowing her to breathe at regular intervals."
    er "I didn’t know my girl was such a good cocksucker."
    er "I’m impressed, Keo."
    "The corners of the girl’s mouth turned up into a smile at those words of encouragement."
    scene ep010_erylin_naked with dissolve
    if game.is_special:
        "Erylin released her grip on her daughter’s body and slipped out of her robes."
    elif True:
        "Erylin released her grip on the girl’s body and slipped out of her robes."
    if game.is_special:
        "Keodele sucked my cock on her own accord while I was treated to the sight of her mother getting naked onto the bed."
    elif True:
        "Keodele sucked my cock on her own accord while I was treated to the sight of Erylin getting naked onto the bed."
    scene ep010_erylin_naked_alt with dissolve
    er "Why don’t you both come join me?"

    scene ep010_erylin_naked_closeup with dissolve
    if is_patreon() and renpy.has_label("extra_scene_21") and not _in_replay:
        call extra_scene_21 from _call_extra_scene_21

    "Erylin sank back onto the pillows and spread her legs, parting her labia with her fingers to reveal her pussy."
    if game.is_special:
        er "Come here Keo, and lick your mother’s pussy."
    elif True:
        er "Come here Keo, and lick my pussy."
    show ep010_erylin_naked_lick_alt with dissolve
    "Keodele nestled herself between Erylin’s legs and started licking."
    show ep010_erylin_naked_lick_alt_closeup with dissolve
    hide ep010_erylin_naked_lick_alt
    "She did it with so much confidence I suspected she’d done this many times before."
    scene ep010_erylin_naked_lick with dissolve
    if game.is_special:
        er "How do you like my daughter so far, [p_name]?"
    elif True:
        er "How do you like my acolyte so far, [p_name]?"
    c "She's still got things to learn, but she can practice sucking cock on me any time."
    er "Good!"
    er "Oh, Keo...{w} Yes, right there, keep going darling."
    er "Mmmmm, long strokes, yes."
    scene ep010_erylin_naked_lick_closeup_alt with dissolve
    "Wearing a satisfied smile, Erylin turned her attention from Keodele to me again."
    if game.is_special:
        er "I bet you love the show, but can’t wait to take my daughter’s virginity."
    elif True:
        er "I bet you love the show, but can’t wait to take her virginity."
    if game.is_special:
        c "True, but I’d like to fuck the virgin’s mother long and hard as well."
    elif True:
        c "True, but I’d like to fuck the virgin's superior long and hard as well."
    scene ep010_erylin_naked_lick_closeup with dissolve
    "Erylin shuddered as Keo applied her tongue to her clitoris."
    er "Mmmmm, your choice, of course."
    menu ep010_erylin_fucking:
        "Fuck Keodele" if not ep010_keodele_fucked:
            $ ep010_keodele_fucked = True
            if not ep010_erylin_fucked:
                scene ep010_erylin_naked_whisper with dissolve
                "I leaned over to Keodele and whispered."
            elif True:
                scene ep010_erylin_naked_whisper_alt with dissolve
                "I managed to remove my head from under Erylin, leaned over to Keodele and whispered."
            c "I hope you’re ready for me."
            if not ep010_erylin_fucked:
                scene ep010_erylin_naked_whisper_shock with dissolve
            elif True:
                scene ep010_erylin_naked_whisper_shock_alt with dissolve
            if game.is_special:
                "The acolyte looked up in shock causing some dissatisfied noises from her mother, who’d lost the feeling of the girl’s tongue on her slit."
            elif True:
                "The acolyte looked up in shock causing some dissatisfied noises from Erylin, who’d lost the feeling of the girl’s tongue on her slit."
            keo "I...{w} I am."
            "Erylin realized what the girl meant and made room for me to lie down."
            er "Just get on top of him, Keo."
            scene ep010_erylin_naked_penetrate with dissolve
            if game.is_special:
                "The girl climbed on top of me while her mother grabbed my cock."
            elif True:
                "The girl climbed on top of me while the head priestess grabbed my cock."
            er "You’re going to feel so wonderful in seconds."
            "The priestess pushed my dick against the young acolyte’s pussy."
            "Keodele tensed up and let out a cry of distress."
            scene ep010_erylin_naked_penetrate_closeup with dissolve
            keo "It won’t fit! It’s too big."
            er "Don’t panic, of course it will fit."
            er "It might hurt a bit the first time, but you can take that hard cock of his, I’m sure of it."
            scene ep010_erylin_naked_penetrate_alt with dissolve
            "Not waiting for a response, Erylin kept pushing my dick inside Keodele’s virginal entrance."
            scene ep010_erylin_naked_penetrate_closeup with dissolve
            keo "It hurts!{w} He’s stretching me out too far."
            er "Nonsense, you’re doing fine."
            er "His cock is going all the way inside you."
            "I felt the girl’s tight pussy close around my dick."
            "She felt warm, wet and absolutely delightful."
            keo "He’s inside me!"
            if game.is_special:
                keo "Oh mother!{w} I feel so full!"
            elif True:
                keo "Oh mistress!{w} I feel so full!"
            scene ep010_erylin_naked_fuck_alt with dissolve
            "Keodele didn’t sound all that panicked anymore, her exclamations more surprised than anything else."
            er "Now, move up and down, girl."
            er "Let him fuck you."
            scene ep010_erylin_naked_fuck_closeup with dissolve
            if game.is_special:
                er "Fuck my daughter's virgin pussy, [p_name]."
                "The girl followed her mother’s instructions and I helped her by moving in unison with her in the opposite direction."
            elif True:
                er "Fuck that virgin pussy, [p_name]."
                "The girl followed her superior's instructions and I helped her by moving in unison with her in the opposite direction."
            scene ep010_erylin_naked_fuck with dissolve
            keo "It’s so big!"
            er "But you like it, don’t you?"
            if game.is_special:
                keo "I love it!{w} I love having him inside of me, mother!"
            elif True:
                keo "I love it!{w} I love having him inside of me, mistress!"
            er "Good girl."
            er "I want a taste of you."
            if game.is_special:
                "With some reluctance Keodele slipped off my body in order to give her mother free access to my cock."
                scene ep010_erylin_naked_suck_alt with dissolve
                "Blinded by Erylin's wet cunt in my face, I felt Keodele's fingers wrap around my cock, followed by her mother's lips enveloping the tip."
                "Erylin wiggled her lower body, smothering me with her pussy."
                er "Why don’t you finish what Keo started?"
                show ep010_erylin_naked_suck with dissolve
                "Erylin eagerly slobbered up her daughter's juices, while I started working on her slit."
            elif True:
                "With some reluctance Keodele slipped off my body in order to give Erylin free access to my cock."
                scene ep010_erylin_naked_suck_alt with dissolve
                "Blinded by Erylin's wet cunt in my face, I felt Keodele's fingers wrap around my cock, followed by the older woman's lips enveloping the tip."
                "Erylin wiggled her lower body, smothering me with her pussy."
                er "Why don’t you finish what Keo started?"
                show ep010_erylin_naked_suck with dissolve
                "Erylin eagerly slobbered up Keodele's juices, while I started working on her slit."
            scene ep010_erylin_naked_suck_closeup with dissolve
            "The head priestess moaned as I licked her cunt, paying extra attention to her swollen clit."
            scene ep010_erylin_naked_suck_closeup_alt with dissolve
            if game.is_special:
                keo "Does his thick cock feel good in your mouth, mother?"
            elif True:
                keo "Does his thick cock feel good in your mouth, mistress?"
            er "Mmmm, yes, yes it does!"
            keo "Am I allowed to fuck him again?"
            keo "I want it so badly."
            if game.is_special:
                "Erylin smirked at her daughter's plea and released my member from her mouth."
                scene ep010_erylin_naked_fucking_alt with dissolve
                "Keodele mounted me again, while her mother turned around, her pussy still pressed firmly on my face."
            elif True:
                "Erylin smirked at the acolyte's plea and released my member from her mouth."
                scene ep010_erylin_naked_fucking_alt with dissolve
                "Keodele mounted me again, while her mistress turned around, her pussy still pressed firmly on my face."
            show ep010_erylin_naked_fucking with dissolve
            "The smell of her wet pussy overwhelmed almost all of my senses."
            scene ep010_erylin_naked_fucking_closeup_er with dissolve
            if game.is_special:
                "As I licked the older woman’s cunt, her daughter rode my dick in a lustful trance."
            elif True:
                "As I licked the older woman’s cunt, the younger girl rode my dick in a lustful trance."
            "Caution thrown in the wind, Keodele took the entire length of my shaft inside her tight pussy."
            "She moaned with abandon as my balls slapped against her ass."
            scene ep010_erylin_naked_fucking_closeup_alt with dissolve
            "I’d worked Erylin up into a similar state of mind with my tongue."
            "Covering her clit with powerful strokes, I took the head priestess to her climax."
            scene ep010_erylin_naked_fucking_closeup_er_alt with dissolve
            "As she orgasmed, a gush of pussy juice flooded my mouth."
            "Smiling triumphantly, I drank with greediness, while Erylin convulsed and nearly collapsed on top of me."
            scene ep010_erylin_naked_fucking_closeup with dissolve
            if not ep010_erylin_fucked:
                $ ep010_erylin_fucked_last = True
                "Having prepared her, I really wanted to use Erylin’s pussy."
            jump ep010_erylin_fucking
        "Fuck Erylin" if not ep010_erylin_fucked:
            $ ep010_erylin_fucked = True
            "The head priestess always seemed so in control of everything and I longed to take some of that away."
            scene ep010_erylin_naked_swap_fuck with dissolve
            "I wanted to look Erylin in the eyes as I fucked her, so I pushed her onto her back on the bed."
            if game.is_special:
                "Her daughter was near her, stroking her mother’s breasts as I plunged my cock into her wet cunt."
            elif True:
                "Her pupil was near her, stroking her mistress’s breasts as I plunged my cock into her wet cunt."
            scene ep010_erylin_naked_swap_fuck_closeup with dissolve
            er "Ah yes!{w} Ram that cock inside me!"
            "Erylin clearly relished the feeling of my entire length disappearing inside her fuckhole."
            scene ep010_erylin_naked_swap_fuck_closeup_alt with dissolve
            if game.is_special:
                "Keodele looked at me in awe as I fucked her mother hard."
            elif True:
                "Keodele looked at me in awe as I fucked the head priestess hard."
            er "Keep playing with my breasts, dear."
            if game.is_special:
                er "Mommy is getting fucked so good."
            elif True:
                er "I'm getting fucked so good."
            show ep010_erylin_naked_swap_fuck_alt with dissolve
            if ep010_keodele_fucked:
                if game.is_special:
                    er "Did my daughter’s snatch feel as good?"
                elif True:
                    er "Did the girl’s snatch feel as good?"
            elif True:
                if game.is_special:
                    er "Do you think my daughter’s snatch feels just as good?"
                elif True:
                    er "Do you think the girl's snatch feels just as good?"
            "I only grunted, grabbed her leg and forced my cock even deeper in the woman’s slit."
            if game.is_special:
                c "Why don’t you sit on your mother’s face, Keodele?"
            elif True:
                c "Why don’t you sit on Erylin’s face, Keodele?"
            scene ep010_erylin_naked_swap_fucking with dissolve
            "The girl smiled and covered Erylin’s mouth with her dripping pussy."
            scene ep010_erylin_naked_swap_fucking_closeup_alt with dissolve
            "The head priestess moaned loudly, the sound muffled by Keodele’s cunt as it was being treated by bold tongue strokes."
            scene ep010_erylin_naked_swap_fucking_closeup with dissolve
            "The older woman’s breast danced up and down as I fucked her mercilessly."
            scene ep010_erylin_naked_swap_fucking_alt with dissolve
            if not ep010_keodele_fucked:
                "After Erylin prepared Keodele so well, I really wanted to use her pussy."
            jump ep010_erylin_fucking

    "The sight of both women nearing the point of complete pleasure rapidly sped up the approach of my own orgasm."

    menu:
        "Creampie Keodele" if True:
            $ ep010_keodele_creampie = True
            "I’d long decided Keodele would receive my seed."
            if ep010_erylin_fucked_last:
                scene ep010_erylin_naked_fucking_closeup with dissolve
                if game.is_special:
                    "So I pulled out of Erylin and motioned her daughter to sit on my cock again."
                elif True:
                    "So I pulled out of Erylin and motioned her pupil to sit on my cock again."
            elif True:
                "So I kept her in place and thrust my cock inside her with rapid strokes."
            "Keodele didn’t know what happened until my cum had already started flooding her vagina."
            with vpunch
            keo "Oh!{w} It suddenly feels so warm inside me."
            er "He’s cum inside you, Keo, you’re truly not a virgin anymore!"
            scene ep010_erylin_naked_fucking_creampie with flash
            with flash
            "I kept fucking her until I shot every last drop of cum inside of her."
            scene ep010_erylin_naked_creampie_lick_alt with dissolve
            "Erylin made the girl lie down and admired the mess I’d made of Keodele’s pussy."
            if game.is_special:
                "Smiling, she cleaned my seed from her daughter’s pussy with her tongue."
            elif True:
                "Smiling, she cleaned my seed from her pupil's pussy with her tongue."
        "Creampie Erylin" if True:
            $ ep010_erylin_creampie = True
            "I’d long decided Erylin would receive my seed."
            if ep010_erylin_fucked_last:
                "So I kept fucking Erylin with rapid strokes."
            elif True:
                scene ep010_erylin_naked_swap_fucking_alt with dissolve
                "So I pushed Keodele off my cock and pulled Erylin towards me."
            "Erylin knew what was coming and smiled."
            er "I want it all inside of me, don’t waste a drop."
            scene ep010_erylin_naked_swap_fucking_creampie with vpunch
            "In response, my cum flooded her vagina and I kept fucking her until I shot every last drop inside of her."
            with flash
            with flash
            "When I pulled out of her, Erylin remained on her back, cum oozing out of her pussy."
            er "Come here, Keo."
            scene ep010_erylin_naked_creampie_lick with dissolve
            "She made the girl rest between her legs."
            if game.is_special:
                er "Make mommy’s pussy clean again, Keo."
                "The girl did just that, she cleaned the seed from her mother’s pussy with her tongue."
            elif True:
                er "Make my pussy clean again, Keo."
                "The girl did just that, she cleaned the seed from the older woman’s pussy with her tongue."
        "Facial" if True:
            "I wanted to mark both women with my seed."
            scene ep010_erylin_naked_facial_alt with dissolve
            if ep010_erylin_fucked_last:
                "As I pulled out of Erylin, I made both women lie down in front of me."
            elif True:
                "As I pushed Keodele off my body, I made both women lie down in front of me."
            scene ep010_erylin_naked_facial with flash
            with flash
            "Grabbing my cock, I managed to spray both their faces with cum."
            "Keodele looked surprised at the volume of semen splashing on their faces and abdomen."
            er "Now you’re truly not a virgin anymore, Keo."
            scene ep010_erylin_naked_cum_lick with dissolve
            if game.is_special:
                er "Why don’t you clean mommy up?"
                "Keodele obliged and lapped up the cum from her mother's face and the rest of her body."
            elif True:
                er "Why don’t you clean me up?"
                "Keodele obliged and lapped up the cum from the older woman's face and the rest of her body."
        "Bodies" if True:
            "I wanted to mark both women with my seed."
            scene ep010_erylin_naked_bodies_alt with dissolve
            if ep010_erylin_fucked_last:
                "As I pulled out of Erylin, I made both women lie down in front of me."
            elif True:
                "As I pushed Keodele off my body, I made both women lie down in front of me."
            scene ep010_erylin_naked_bodies with flash
            with flash
            "Grabbing my cock, I managed to spray both their bodies with cum."
            "Keodele looked surprised at the volume of semen splashing on their abdomen."
            er "Now you’re truly not a virgin anymore, Keo."
            scene ep010_erylin_naked_cum_lick_alt with dissolve
            if game.is_special:
                er "Why don’t you clean mommy up?"
                "Keodele obliged and lapped up the cum from her mother's breasts and the rest of her body."
            elif True:
                er "Why don’t you clean me up?"
                "Keodele obliged and lapped up the cum from the older woman's breasts and the rest of her body."

    scene ep010_erylin_naked_post with dissolve
    "Afterwards the women both sat on the bed, looking completely fulfilled."
    $ renpy.end_replay()
    return

label ep010_vess_sex:
    if _in_replay:
        $ ve_name = "Vess"
    scene ep010_vess_naked with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "Vess silenced any further conversation by slipping out of her night gown."
    scene ep010_vess_naked_alt with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "It was the first time I could take a good look at her gorgeous naked body."
    "My probing gaze made Vess a little uncomfortable."
    ve "Do my looks please you?"
    c "You’re beautiful, Vess."
    ve "I’m not sure you realize how much I enjoyed our night on Almaghest?"
    scene ep010_vess_kneel with dissolve
    "The girl knelt before me and looked, wearing a sultry expression."
    c "I have an inclination."
    ve "Would you allow me to return the favor."
    c "I don’t think you even need to ask that question."
    scene ep010_vess_kneel_alt with dissolve
    ve "That’s a yes, then?"
    c "I didn’t know you could be such a tease."
    c "But yes, a resounding yes."
    ve "Good."
    scene ep010_vess_lick with dissolve
    "Vess lowered her head towards my cock and reached out hesitantly with her tongue."
    scene ep010_vess_lick_alt with dissolve
    "When her tongue connected with the head of my cock, it was as if a small dose of electricity coursed through my body."
    scene ep010_vess_lick_closeup with dissolve
    "Precum already started flowing from the tip."
    "Vess smiled shyly because of my reaction to her cautious probe."
    ve "Do you like that?"
    "I’m sure she knew the answer, but the innocent look she gave me made that moment all the better."
    c "Oh yes, please keep doing that."
    scene ep010_vess_suck_alt with dissolve
    "Vess smiled and bit her lip, got onto the bed and turned her attention to my erection again."
    scene ep010_vess_suck with dissolve
    "By the time she was softly licking the border of my glans, an abundance of precum and her saliva already covered my cock."
    scene ep010_vess_suck_closeup with dissolve
    "She gave the head of my cock a lot of attention, triggering a great many nerve responses and making the stimulation almost unbearable."
    show ep010_vess_sucking with dissolve
    "The girl got on all fours and took my dick in her mouth, relieving some of the immediate tension."
    show ep010_vess_sucking_closeup with dissolve
    hide ep010_vess_sucking
    "Her head bobbed up an down as she tried to take more and more of my girth inside of her."
    scene ep010_vess_sucking_alt with dissolve
    "I took a moment to look at Vess, her round ass in the air and full breasts dangling in front of me."

    if is_patreon() and renpy.has_label("extra_scene_20") and not _in_replay:
        call extra_scene_20 from _call_extra_scene_20
    elif True:
        c "I want you, Vess."
        scene ep010_vess_sucking_interrupt with dissolve
        "Her mouth released my cock and she looked up at me."
        ve "W-want me?"
    scene ep010_vess_pussy_kiss with dissolve
    "In response I moved closer to her and kissed her lips."
    scene ep010_vess_pussy_kiss_alt with dissolve
    "A little startled, she didn’t immediately return the kiss, but gave herself over eventually."
    scene ep010_vess_pussy with dissolve
    "When we broke loose, she took position in front of me, her shy expression slowly replaced by a subtle smile."
    scene ep010_vess_pussy_closeup with dissolve
    ve "Do you want to fuck me, [p_name]?"
    c "Yes."
    ve "Fuck my tight pussy?"
    scene ep010_vess_pussy_closeup_alt with dissolve
    "Her dirty talk was still a little hesitant and uneasy, but I loved it all the same."
    scene ep010_vess_pussy_penetrate with dissolve
    "I scooted over to her and pushed her legs backward as I let my cock rest next to her pussy."
    "The girl’s seductive smile had transformed into a look of worry as she lay there before me, legs splayed open."
    scene ep010_vess_pussy_penetrate_alt with dissolve
    ve "[p_name]?"
    c "Yes?"
    ve "Please, be gentle with me."
    "A wealth of information was hidden in that single statement and I knew she wasn’t playacting at that point."
    c "I won’t hurt you."
    ve "Promise?"
    c "Promise."
    show ep010_vess_penetrate_closeup_rub with dissolve
    "Rubbing my cock along her slit, I could tell she was already very wet."
    "Her arousal would help, but I hoped she’d be able to find a measure of tranquility."
    scene ep010_vess_pussy_penetrate_closeup_alt with dissolve
    "I parted her labia with my cock and slowly inserted the tip inside her."
    scene ep010_vess_pussy_penetrate_closeup with dissolve
    "Vess bit her lip and scrunched her face in pain, but she didn’t cry out."
    c "Are you alright?"
    ve "Y-yes."
    "It sounded almost as is she had to convince herself of that answer."
    scene ep010_vess_pussy_fuck with dissolve
    "She offered nothing more, so I kept going, very slowly."
    "Even though Vess was dripping wet, she was very tight."
    show ep010_vess_pussy_penetrate_closeup_anim with dissolve
    "I stopped at one quarter and ventured my first thrust."
    scene ep010_vess_pussy_fuck_alt with dissolve
    "A pained moan escaped the girl, which turned halfway into groan laced with pleasure."
    show ep010_vess_pussy_penetrating_closeup_alt with dissolve
    "The next thrust took her breath away and when I came back from her depths she exhaled in a lustful sigh."
    scene ep010_vess_pussy_fuck_closeup with dissolve
    ve "I want you to have me, [p_name_short]."
    ve "Fuck me, please."
    show ep010_vess_penetrate_closeup_alt with dissolve
    "Vess was now completely ready for me, but when I dared to push deeper inside of her, she let out a small cry."
    c "Does it hurt?"
    scene ep010_vess_pussy_fuck_closeup_alt with dissolve
    ve "A little..."
    "I could tell Vess had trouble giving up control, to live in the moment itself."
    scene ep010_vess_pussy_fucking with dissolve
    "So I lay down and made her get on top of me."
    c "Just take it slow, you decide how far we go."
    scene ep010_vess_pussy_fucking_alt with dissolve
    ve "But will it feel good for you too?"
    c "Don’t worry about me, I’ll be quite alright."
    scene ep010_vess_pussy_fucking_closeup_alt with dissolve
    "With growing confidence, Vess let her body slide down on my cock."
    show ep010_vess_fucking with dissolve
    ve "Oh...{w} Oh!{w} Oh yes!"
    "She’d taken my cock deeper inside her tight pussy than before and clearly loved every inch of it."
    c "Now ride me."
    show ep010_vess_pussy_fucking_closeup with dissolve
    "The girl’s cunt slid upwards, the sensation causing her eyes to roll back."
    ve "Oh fuck, this feels so good.{w} Your cock feels so good inside me."
    "She relished the feeling as most of my veined shaft slowly returned from her wet vagina."
    "The second penetration she took it a little faster, still savoring every moment."
    scene ep010_vess_pussy_fucking_closeup_face with dissolve
    ve "I love your cock so deep inside me, [p_name]."
    "Her cunt strengthened that claim as pussy juice flowed freely along the sides of my shaft."
    scene ep010_vess_cowgirl with dissolve
    "Vess gripped my hands and started moving her ass up and down, finally giving herself over."
    "I’d remained almost motionless while she initially mounted me, but now I joined her."
    scene ep010_vess_cowgirl_alt with dissolve
    "Thrusting my pelvis upwards when she came down on me I could reach new depths easily."
    "Vess moaned loudly every time I went in deep."
    scene ep010_vess_cowgirl_closeup with dissolve
    "The girl still felt incredibly tight, but my cock clearly didn’t hurt her anymore."
    scene ep010_vess_cowgirl_closeup_alt with dissolve
    ve "Keep fucking me like that, [p_name]. Oh, it feels so good!"
    "The girl rode me hard for quite some time, getting me ever closer to the release that had been building up for quite some time."
    c "Oh Vess!{w} Vess!"
    menu:
        "Creampie" if True:
            $ ep010_vess_creampie = True
            ve "Don’t pull out, [p_name_short], I want your cum inside me."
            with vpunch
            "I gripped her hand tightly and a volley of cum surged into her vagina."
            scene ep010_vess_creampie with flash
            with flash
            "Because of the slippery wet mess I’d made of her pussy, my cock eventually slipped out of her cunt."
            "Droplets of cum still formed at the tip as a long dribble of semen leaked out of her slit onto my balls."
        "Body" if True:
            "I gripped her hand tightly as my cock slipped from the wet mess I’d made of her pussy."
            scene ep010_vess_body with vpunch
            "Freed from her tight slit, I showered her belly with cum."
        "Facial" if True:
            "I wanted to paste her beautiful face, so I squirmed out from under the girl and presented my cock to Vess, glistening with her own juices."
            scene ep010_vess_facial with vpunch
            "With barely a few tugs of her hand, I sprayed everything on her face, covering a good portion in cum."
    scene ep010_vess_post with dissolve
    "Completely spent, we both sagged on the bed, where we lay on our stomachs holding hands."
    scene ep010_vess_post_closeup with dissolve
    ve "I...{w} I’m glad you were my first."

    menu:
        "Tell her you love her [VessPath]" if True:
            $ ep010_vess_love = True
            c "I love you, Vess."
            scene ep010_vess_post_closeup_smile with dissolve
            "The girl smiled wistfully and tightened her grip on my hand."
        "Remain silent" if True:
            scene ep010_vess_post_closeup_smile with dissolve
            "I smiled at her and Vess smiled back wistfully."
    scene ep010_vess_post with dissolve
    "We remained in the same position for a long while."
    scene black with fade
    "When we were about to fall asleep, she slowly rose, kissed me and slipped out of the room."
    $ renpy.end_replay()
    return

label ep010_ziv_sex:
    if _in_replay:
        $ ep004_lu_suck = False

    scene ep010_ziv_naked with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    zi "I’d really like to continue what we started."
    c "And what was that exactly?"
    scene ep010_ziv_naked_alt with dissolve
    "Ziv had draped herself seductively on the bed, proudly displaying herself in all her glory."
    zi "If you really need to ask, I’m not sure we should continue..."
    "I’d started getting hard again and I noticed Ziv was experiencing the same."
    "I hastily undressed."
    zi "Ah, so you do know what we started."
    scene ep010_ziv_naked_pussy with dissolve
    "Ziv just lay there on the bed, her legs spread, challenging me."
    menu:
        "Suck her cock" if True:
            $ ep010_ziv_cock_sucked = True
            scene ep010_ziv_naked_cock with dissolve
            if ep004_lu_suck:
                "Hers wasn’t the first cock I’d tasted, but her half-erect member stirred something in me."
            elif True:
                "I’d never given someone a blowjob before, but her half-erect cock stirred something in me."
            scene ep010_ziv_naked_cock_closeup with dissolve
            "I moved in between her legs, keeping Ziv in doubt as to my intentions."
            scene ep010_ziv_naked_cock_lick with dissolve
            "Carefully, I took hold of her shaft and began to stimulate her with teasing licks."
            "Ziv let out a groan and I felt her cock stiffen under my touch."
            "My tongue explored all the places I knew were sensitive, to considerable success."
            scene ep010_ziv_naked_cock_lick_alt with dissolve
            zi "Oh yes, keep going like that!"
            "Precum had already started oozing from her tip and I decided to have a taste."
            "Savoring the saline liquid, I came to the conclusion we were both ready for more."
            scene ep010_ziv_naked_cock_suck with dissolve
            "Grabbing her cock firmer, I enveloped the head with my mouth."
            "Ziv gripped my hand and angled her pelvis towards me, wanting desperately for me to take more of her shaft inside my mouth."
            "My tongue whirled over the tip of Ziv’s cock, as saliva started dripping towards her balls from the corners of my mouth."
            show ep010_ziv_naked_cock_suck_alt with dissolve
            zi "Oh [p_name_short]!{w} Oh [p_name]!"
            "The woman writhed on the bed, her cock still firmly planted inside my mouth."
            "Her salty taste became almost overpowering, as I kept her on the edge of her climax."
            scene ep010_ziv_naked_cock_suck_closeup with dissolve
            zi "Make me cum with your mouth, please!"
            zi "I’m cumming!{w} I’m c-c-cumming!"
            "Her words urged me in to a frenzy of sucking and licking."
            "Ziv started to tremble violently and her grip on my hand intensified."
            menu:
                "Swallow" if True:
                    $ ep010_ziv_swallow_received = True
                    with vpunch
                    "With a long moan, Ziv unloaded in my mouth."
                    scene ep010_ziv_naked_cock_suck_orgasm with flash
                    with flash
                    "Cum flooded my mouth and because there was so much of it, I couldn’t swallow it all."
                    "Some of her seed oozed down her shaft as small amounts still oozed from the tip of her cock."
                "Facial" if True:
                    $ ep010_ziv_facial_received = True
                    scene ep010_ziv_naked_cock_suck_facial with vpunch
                    "With a long moan, Ziv unloaded all over my face."
                    "Thick strings of cum splashed onto my face, eventually dribbling down my chin."
                "Body" if True:
                    scene ep010_ziv_naked_cock_suck_body with vpunch
                    "Just when I released her cock from my mouth, Ziv unloaded all over her abdomen with a long moan."
            "Lust still burned in her eyes when Ziv regarded me."
            scene ep010_ziv_kiss with dissolve
            "Our tongues met and began a furious dance."
            "In between kisses she managed to finish a short sentence."
            scene ep010_ziv_kiss_alt with dissolve
            zi "I want more."
        "Lick her pussy" if True:
            $ ep010_ziv_pussy_licked = True
            scene ep010_ziv_naked_pussy_closeup with dissolve
            "Her pussy looked so inviting, so I moved in between her legs, keeping Ziv in doubt as to my intentions."
            show ep010_ziv_naked_pussy_lick with dissolve
            "Carefully, my tongue touched her labia and she let out a long groan."
            "Her cock stiffened when I began licking her in earnest."
            scene ep010_ziv_naked_pussy_lick_closeup with dissolve
            "I explored all the sensitive places of her slit, savoring the saline taste of her pussy juice which had begun flowing."
            scene ep010_ziv_naked_pussy_lick_alt with dissolve
            zi "Oh yes, keep going like that!"
            "Ziv’s cock had swollen to its full size and it proudly obstructed my view of her."
            menu:
                "Just finger her" if True:
                    scene ep010_ziv_naked_pussy_finger with dissolve
                    "I was too busy pleasuring her cunt, adding two fingers inside her."
                    "The woman couldn’t contain herself and took hold of her cock."
                    scene ep010_ziv_naked_pussy_finger_closeup with dissolve
                    "She jerked as I fingered her, receiving twice the amount of pleasure."
                    "The feeling of controlling her so completely made me even bolder than before and I slowly worked her up into a frenzy."
                    show ep010_ziv_naked_pussy_finger_alt with dissolve
                    zi "W-whatever y-ou do, don’t you dare stop!"
                    "I sure wasn’t planning on stopping, so I kept penetrating her slit with my fingers and licking her clit."
                    "Ziv was jerking very fast and breathing shallowly."
                    show ep010_ziv_naked_pussy_finger_alt_closeup with dissolve
                    hide ep010_ziv_naked_pussy_finger_alt
                    zi "Don’t stop!"
                    scene ep010_ziv_naked_pussy_finger_orgasm with dissolve
                    zi "I’m cumming!"
                    scene ep010_ziv_naked_pussy_finger_alt_orgasm with vpunch
                    "Her pussy convulsed right at the same time as her cock pumped out a wealth of cum."
                    scene ep010_ziv_naked_pussy_finger_alt_orgasm_alt with flash
                    with flash
                    "Thick strands of cum coated her fingers as she jerked the last droplets of seed from her cock."
                    "I kept fingering her, until I involuntarily slipped out of her dripping wet cunt."
                "Jerk her cock" if True:
                    $ ep010_ziv_hj_given = True
                    scene ep010_ziv_naked_pussy_finger_jerk with dissolve
                    "I took her cock in my hand and started jerking her."
                    "Ziv now received twice the amount of pleasure."
                    "The feeling of controlling her so completely made me even bolder than before and I slowly worked her up into a frenzy."
                    scene ep010_ziv_naked_pussy_finger_jerk_alt with dissolve
                    zi "W-whatever y-ou do, don’t you dare stop!"
                    "I sure wasn’t planning on stopping, so I kept jerking her cock and penetrating her slit with my fingers."
                    "Ziv was breathing very shallowly and gripped my hand with clawed fingers."
                    zi "Don’t stop!"
                    scene ep010_ziv_naked_pussy_finger_orgasm with dissolve
                    zi "I’m cumming!"
                    scene ep010_ziv_naked_pussy_finger_jerk_orgasm with vpunch
                    "Her pussy convulsed right at the same time as her cock pumped out a wealth of cum."
                    scene ep010_ziv_naked_pussy_finger_jerk_orgasm_alt with flash
                    with flash
                    "Thick strands of cum coated my fingers as I jerked the last droplets of seed from her cock."
                    "I kept fingering her, until I involuntarily slipped out of her dripping wet cunt."
            "Lust still burned in her eyes when Ziv regarded me."
            scene ep010_ziv_kiss with dissolve
            "Our tongues met and began a furious dance."
            "In between kisses she managed to finish a short sentence."
            scene ep010_ziv_kiss_alt with dissolve
            zi "I want more."
        "Let her suck your cock" if True:
            "Ziv’s gaze fell onto my rock-hard dick."
            scene ep010_ziv_naked_sucking with dissolve
            "She pushed me back onto the bed and dove between my legs."
            "Taking hold of my shaft, the tip disappeared inside her warm mouth."
            show ep010_ziv_naked_sucking_alt with dissolve
            "Her tongue eagerly lapped up the thin film that already covered my cock."
            "It was hard not to focus on the purple-skinned alien working on my dick, but I managed to shift my gaze and admire her well-shaped buttocks and powerful cock hanging between her legs."
            show ep010_ziv_naked_sucking_closeup with dissolve
            hide ep010_ziv_naked_sucking_alt
            "Ziv was a natural at cock sucking, with her intimate knowledge of all the sensitive spots."
            "She had me on the verge of cumming in minutes and I had to crawl from her grasp in order to stop blasting her mouth full of cum."
            scene ep010_ziv_naked_sucking_closeup_alt with dissolve
            zi "Are you displeased?"
            c "Not at all."
            c "But I don’t want this to end now."
            "Lust still burned in her eyes when Ziv regarded me."
            scene ep010_ziv_kiss with dissolve
            "Our tongues met and began a furious dance."
            "In between kisses she managed to finish a short sentence."
            scene ep010_ziv_kiss_alt with dissolve
            zi "Me neither, I want more."

    "We embraced again and exchanged another long kiss."
    scene ep010_ziv_naked_penetrate with dissolve
    "My erection pressed against her firm buttocks and Ziv smiled at me when I pushed against her rear entrance accidentally."
    zi "Someone’s very eager..."
    c "Easy for you to say, I’d like to see you try spooning with a sexy alien!"
    scene ep010_ziv_naked_penetrate_alt with dissolve
    zi "I think I’m doing just that right now."
    c "You know what I meant..."
    scene ep010_ziv_naked_penetrate_closeup with dissolve
    "Ziv helped me guide my cock towards her pussy."
    "With some effort, I managed to enter her."
    scene ep010_ziv_naked_fuck with dissolve
    zi "Oh yes!{w} That feels so good!"
    zi "Fuck me, [p_name]!"
    scene ep010_ziv_naked_fuck_alt with dissolve
    "As I started thrusting inside her, I realized again that I was her first."
    show ep010_ziv_naked_fuck_alt_wide with dissolve
    "Despite her lack of bedroom experience, Ziv didn’t seem to suffer from the ailments that often accompany a girl’s first time."
    "That didn’t mean her pussy wasn’t tight."
    scene ep010_ziv_naked_fuck_closeup with dissolve
    "On the contrary, it almost seemed as if my cock and her slit were made for each other."
    scene ep010_ziv_naked_fuck_closeup_alt with dissolve
    "Ziv completely gave herself over to me, enjoying every inch of my veined shaft as it disappeared inside her."
    scene ep010_ziv_naked_doggy with dissolve
    "The strain of penetrating her sideways from behind became a little too much, so we shifted positions."
    "I made her kneel before me and pushed my cock back inside her while straddling her body."
    show ep010_ziv_naked_doggy_wide with dissolve
    "Fucking her like this allowed me to penetrate her even deeper and she moaned loudly when my shaft went in to the root."
    scene ep010_ziv_naked_doggy_alt with dissolve
    zi "Your cock feels so amazing inside me, [p_name]!"
    zi "Keep going like that, nice and deep."
    scene ep010_ziv_naked_doggy_closeup with dissolve
    "Her ass grinded against my abdomen as she luxuriated in the feeling of my cock deep inside her."
    "Her own cock swung up and down unattended as Ziv focused completely on fucking our brains out."
    scene ep010_ziv_naked_cowgirl with dissolve
    "Wanting to give her more control, I made her sit on her knees again and shifted underneath her."
    "Ziv mounted me and allowed me to delve deep inside her wet slit."
    scene ep010_ziv_naked_cowgirl_alt with dissolve
    "She trembled as my cock speared her pussy with long and hard thrusts."
    zi "Fuck!{w} Make me cum, [p_name_short]!{w} Make me cum!"
    "Ziv’s erection stood completely taut and precum leaked from the tip of her cock."
    scene ep010_ziv_naked_cowgirl_closeup with dissolve
    "I knew she was in the last stretches as she grabbed her cock with force and started jerking herself with small flicks of her wrists."
    scene ep010_ziv_naked_cowgirl_closeup_alt with dissolve
    zi "I’m...{w} I’m..."
    "She didn’t need to tell me she was about to cum."
    "I felt the same feeling."
    menu:
        "Creampie" if True:
            $ ep010_ziv_creampie = True
            with vpunch
            "One last thrust and I erupted inside her."
            scene ep010_ziv_naked_cowgirl_creampie with flash
            with flash
            "A torrent of cum flooded her vagina, and as she kept riding me, it began to stream all down my shaft."
            "Ziv sprayed a fountain of seed at the same time, most of it splashing on the bed and my legs."
            "When my erection waned and slipped out of her slit, a long string of semen dribbled out of her."
        "Body" if True:
            "One last thrust and I pulled out of her."
            scene ep010_ziv_naked_cowgirl_body with vpunch
            "Right at that moment, Ziv sprayed a fountain of seed, most of it splashing on the bed and my legs."
            scene ep010_ziv_naked_cowgirl_body_alt with flash
            with flash
            "I joined her by releasing a torrent of cum that covered her abdomen and the underside of her breasts."
    scene ep010_ziv_naked_cowgirl_post with dissolve
    "Ziv let out a breathless laugh as she collapsed beside me."
    "She took my hand and sighed."
    scene ep010_ziv_naked_cowgirl_post_closeup with dissolve
    zi "I think we just crashed through thirty levels of Rhenkoy companionship at once."
    c "Is that a good score?"
    scene ep010_ziv_naked_cowgirl_post_closeup_alt with dissolve
    zi "Several decades worth of courting, so I’d say yes."
    zi "This felt so good on so many levels."
    zi "Definitive proof that all those rules we made up for ourselves are completely unnecessary."
    c "I don’t know the half of it, but I agree all the same."
    zi "I bet you do..."
    c "Don’t tease me, I just had sex with the most wonderful woman in the universe."
    c "So allow me a little post-coital enthusiasm."
    scene ep010_ziv_naked_cowgirl_post_closeup_smile with dissolve
    "Ziv just smiled and we lay in silence for a long time, holding hands."
    $ renpy.end_replay()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
