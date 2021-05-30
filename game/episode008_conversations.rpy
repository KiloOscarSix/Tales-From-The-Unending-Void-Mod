label ep008_conversations:

    if 'ep008_conversations_init' not in locals():
        $ ep008_conversations_init = True

        $ ep008_aven_talk = False
        $ ep008_kit_talk = False
        $ ep008_eva_talk = False
        $ ep007_eva_apology = False
        $ ep008_l_deny = False
        $ ep008_l_kiss = False
        $ ep008_simulation_alter = False
        $ ep008_simulation_pursue = False
        $ ep008_simulation_exit = False
        $ ep008_simulation_abandon = False
        $ ep008_simulation_clear = False
        $ ep008_eva_love = False

    play music [ "music/the-restoration.ogg", "music/space-harmony.ogg", "music/searching-the-cosmos.ogg" ] fadeout 4 fadein 1.0

    label ep008_conversation_choices:
        $ choices = [
                {
                    'name': 'Aven',
                    'action': 'ep008_aven_talk',
                    'visible': True if not ep008_aven_talk and aven_romance else False
                },
                {
                    'name': 'Eva',
                    'action': 'ep008_eva_talk',
                    'visible': True if not ep008_eva_talk else False
                },
                {
                    'name': 'Kit',
                    'action': 'ep008_kit_talk',
                    'visible': True if not ep008_kit_talk else False
                },
            ]

        scene black with fade
        $ conversation_menu(choices)
        scene black with fade
        return

        label ep008_aven_talk:
            $ ep008_aven_talk = True
            scene ep008_corridor_empty with dissolve
            "Aven occupied my thoughts almost completely and I found myself wandering towards her quarters."
            scene expression eye_blink("images/ep008/ep008_av_corridor_alt") with dissolve
            "I encountered her in one of the corridors."
            scene expression eye_blink("images/ep008/ep008_av_corridor") with dissolve
            "Her eyes lit up and she smiled warmly."
            if ep007_j_injured:
                av "I was just on my way to the med bay to see Jade."
            elif True:
                av "I was just on my way to the engine room to see Jade."
            "An awkward silence followed."
            scene expression eye_blink("images/ep008/ep008_av_corridor_closeup") with dissolve
            "Aven, normally so confident, suddenly seemed so hesitant and unsure of herself."
            scene ep008_av_corridor_kiss with dissolve
            "So we stood there for several seconds, smiling at each other like bumbling lovesick teenagers, until I held her close and kissed her."
            scene ep008_av_corridor_kiss_alt with dissolve
            "She returned my kiss eagerly and all uncertainty evaporated."
            "A door opened and footsteps could be heard startling us from our embrace."
            scene ep008_av_corridor_l with dissolve
            "When Lilly turned the corner, Aven and I were already at an appropriate distance from each other."
            "I glanced at Aven, whose cheeks were flushed and tried to act normally."
            scene expression eye_blink("images/ep008/ep008_av_corridor_l_closeup") with dissolve
            l "What are you two conspiring here in the hallway?"
            c "We're planning a mutiny."
            "Aven's laugh sounded a little strained, but my comment had distracted Lilly enough to stop her from asking any more hard questions."
            scene expression eye_blink("images/ep008/ep008_av_corridor_l_closeup_alt") with dissolve
            l "Last time I checked you were already acting like the captain of the ship around here, [p_name_short]."
            c "Right, I didn't really think through all those details, to be honest."
            l "Well, in any case, if you're serious maybe you should admit yourself to the brig."
            c "Noted, or walk myself out of an airlock."
            scene expression eye_blink("images/ep008/ep008_av_corridor_closeup_alt") with dissolve
            av "That seems rather drastic."
            if ep007_j_injured:
                av "Anyway, Jade needed me in the med bay."
            elif True:
                av "Anyway, Jade needed me in the engine room."
            scene expression eye_blink("images/ep008/ep008_av_corridor_l_closeup_alt") with dissolve
            "Aven left me alone with Lilly."
            if game.is_special:
                "My sister cast me one more questioning smile, but walked away when I didn't venture anything further."
            elif True:
                "My friend cast me one more questioning smile, but walked away when I didn't venture anything further."
            jump ep008_conversation_choices

        label ep008_kit_talk:
            $ ep008_kit_talk = True
            scene expression eye_blink("images/ep008/ep008_ki") with dissolve
            ki "I didn’t get a chance to tell you, but that little rock climbing excursion on Almagest was totally awesome."
            c "I knew you’d like it."
            scene expression eye_blink("images/ep008/ep008_ki_smile") with dissolve
            ki "It was the first time in months I get to do something exciting."
            c "You say that, but I thought you handled that wheelchair with a lot of panache."
            scene expression eye_blink("images/ep008/ep008_ki_laugh") with dissolve
            ki "Fuck you."
            scene expression eye_blink("images/ep008/ep008_ki") with dissolve
            ki "I'm glad that I could dump that thing in the cargo bay."
            c "So you've completely healed?"
            scene expression eye_blink("images/ep008/ep008_ki_smile") with dissolve
            ki "I have, all thanks to my great physique."
            c "And six months of involuntary revalidation."
            scene expression eye_blink("images/ep008/ep008_ki") with dissolve
            ki "That too."
            c "How did you cope with living inside that cell?"
            scene expression eye_blink("images/ep008/ep008_ki_smile") with dissolve
            ki "Well you know, lots of masturbating and waiting for the food to arrive."
            ki "Living with three women really helped as well."
            c "You didn't?!"
            scene expression eye_blink("images/ep008/ep008_ki_serious") with dissolve
            ki "No, of course I didn't!"
            ki "Imagine hitting on my sister, that would have been very awkward."
            if not ep005_celine_romance_secret:
                c "Yeah...."
                scene expression eye_blink("images/ep008/ep008_ki_doubt") with dissolve
                ki "Why are you so worried all of a sudden?"
                c "Just curious."
                scene expression eye_blink("images/ep008/ep008_ki_serious") with dissolve
                ki "I know you and Céline have a thing, [p_name_short]."
                ki "She told me a while ago."
                c "Oh."
                ki "Yeah, though she didn’t really need to tell me."
                ki "I knew about your super top secret romance, which has been plainly visible for everyone with a set of working eyes."
                c "Oh."
                scene expression eye_blink("images/ep008/ep008_ki_serious") with dissolve
                ki "But I’m happy for you both."
                ki "And Céline has been chasing you for a long time, so I’m glad to see she finally got her claws in you."
                c "You make it all sound so romantic."
                scene expression eye_blink("images/ep008/ep008_ki_smile") with dissolve
                ki "People say I have a gift for that."
                c "I’m sure they do."
            elif True:
                c "Yeah...."
                "But Vess and Jade?"
                scene expression eye_blink("images/ep008/ep008_ki_doubt") with dissolve
                ki "Why are you so worried all of a sudden?"
                c "Just curious."
            scene expression eye_blink("images/ep008/ep008_ki_serious") with dissolve
            ki "Nothing happened on that research station."
            ki "Céline and I bonded from day one, like we knew we were related, you know?"
            ki "Vess kept to herself, like she does here on the ship as well."
            scene expression eye_blink("images/ep008/ep008_ki_doubt") with dissolve
            ki "But there was something strange about her, like she recognized us all."
            ki "I mean Céline, Jade and me clearly suffered from amnesia, but Vess..."
            c "Could just be what she saw in that simulation."
            c "She was pretty distraught."
            scene expression eye_blink("images/ep008/ep008_ki_serious") with dissolve
            ki "Could be."
            ki "Jade acted weirdly too, but it was kinda funny looking back at it."
            c "How so?"
            scene expression eye_blink("images/ep008/ep008_ki") with dissolve
            ki "She was like really haughty, acting like she was a queen or something."
            c "Well, she comes from a royal bloodline, you know."
            ki "So you've told me."
            scene expression eye_blink("images/ep008/ep008_ki_smile") with dissolve
            ki "Anyway, it seems that deep down somewhere, she's still very much that Twi'll princess."
            ki "It took a while to convince her we were not her servants."
            c "I didn't notice anything when we were in the middle of escaping."
            ki "I think she was probably too busy saving her own skin instead of fussing over which one of us would bring her highness her food tray."
            c "I'll be sure to bow, next time I see her."
            scene expression eye_blink("images/ep008/ep008_ki_serious") with dissolve
            ki "Good, just don't mention that I told you, because I think she was pretty embarrassed when we got our memories back."
            c "Weren't we all?"
            ki "Right."
            scene expression eye_blink("images/ep008/ep008_ki") with dissolve
            ki "Listen, I'm going to get some food before we all die horribly in that irradiated hell dimension."
            c "Sounds like a plan, enjoy your last supper."
            jump ep008_conversation_choices

        label ep008_eva_talk:
            $ ep008_eva_talk = True
            scene ep008_quarters with dissolve
            "I dreaded going back into the simulation."
            "Adding Lilly's profile might not have been the best idea."
            "My supposed abandonment of Eva had sparked such an increase in hostility from her."
            if game.is_special:
                "I was pretty sure she'd put my other sister against me too, making matters even worse."
            elif True:
                "I was pretty sure she'd put my friend against me too, making matters even worse."
            "I wracked my brain to find a way to get to Eva and explain the situation to her, but I was sure I wouldn't get far with Lilly in the way."
            "I could purge Lilly's profile from the system, but that would no doubt have a devastating effect on Eva."
            if game.is_special:
                "First her brother leaving her and now her sister?"
            elif True:
                "First me leaving her and now one of her best friends?"
            "Deleting Lilly was out of the question, so I'd have to resort to more subtle tactics."
            scene ep008_simulation_corridor with dissolve
            "The simulation software featured an impressive array of configuration tools."
            "Apart from the more obvious things, like controlling the weather and scenery, it was also possible to alter parameters on a more detailed level."
            "Each character profile in the simulation could be tweaked in certain ways, allowing characters to express different personalities."
            "It was tempting to alter Lilly's profile to make her less hostile towards me."
            "Doing this did have its dangers, simulation companies generally always warn people not to mess with the profiles of their simulated loved ones, as the results can be very unpredictable."
            "However, I felt I had zero chance of reaching Eva with Lilly standing in my way."
            scene ep008_simulation_room with dissolve
            "Just before entering the simulation again, I opened up Lilly's profile and had a look at the long list of attributes that made up her personality."
            "When I reached the \"Disposition\" heading of the list, I paused."
            "Should I risk it?"
            menu:
                "[gr]Risk it" if True:
                    $ ep008_simulation_alter = True
                    "Maybe Jade would be better at this, but I didn't feel like explaining it to her."
                    "Resigned, I quickly made a few changes and committed the altered profile to the system's memory."
                "Don't tamper" if True:
                    "Tampering with something as delicate as a psychological profile didn’t sit right with me."
                    "I’d have to face whatever was waiting for me in the simulation without cheating."
            "Taking a deep breath, I entered the simulation again."

            play music "music/cobalt.ogg" fadeout 4 fadein 1.0

            scene ep008_simulation_stairs with pixellate
            "I was back in the mansion again, the stairs looming before me."
            "As nobody came to greet me, I climbed them, lost in thought."
            if not ep008_simulation_alter:
                $ ep008_simulation_exit = True
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_l_alt") with dissolve
                l "[p_name_short]?!"
                "I expected to see her furious again and I was right, she looked absolutely livid."
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_l_alt_closeup") with dissolve
                l "Why the fuck are you back?!"
                l "Didn’t we tell you to leave us alone?"
                l "I don’t want to see you ever again."
                l "The same goes for Eva."
                scene ep008_simulation_stairs_l_alt_e with dissolve
                if game.is_special:
                    "Eva appeared in the hallway, next to her sister."
                elif True:
                    "Eva appeared in the hallway, next to her friend."
                c "Eva, I just want to talk to you."
                c "Explain..."
                e "Don’t bother, [p_name]."
                e "Please go."
                scene ep008_simulation_room with pixellate
                "Frustrated, I pulled out of the simulation immediately."
                "The animosity displayed by both Eva and Lilly just hurt too much."
                "I just didn’t see any way how to fix this."
            elif True:
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_l") with dissolve
                l "[p_name_short]?!"
                "The sharpness of Lilly’s voice startled me."
                "I expected to see her furious again, instead she rushed up to me."
                scene ep008_simulation_stairs_l_hug with dissolve
                "And hugged me without restraint."
                l "You’re back!"
                "She clung to me and forced my arm around her."
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_l_hug_closeup") with dissolve
                l "I was thinking we could take a walk together."
                l "Just us."
                c "Isn’t Eva around?"
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_l_hug_closeup_doubt") with dissolve
                l "Probably, but who cares?"
                c "I was hoping to talk to her."
                c "Is she alright?"
                l "She’s fine."
                c "Is she still upset with me?"
                l "She was, for a time, but I convinced her it wasn’t your fault."
                c "You did?"
                l "Yeah, is that so surprising?"
                "The change in behavior weirded me out a little, but was to be expected after messing with her profile's parameters."
                c "She was really upset."
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_l_hug_closeup_serious") with dissolve
                l "And now she isn't, why are we still talking about this?"
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_e") with dissolve
                e "[p_name_short]?"
                e "You're back!"
                c "I am."
                c "I came to find you earlier, but-"
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_e_sad") with dissolve
                e "I know."
                e "You went away for all those months without saying goodbye, I just couldn't deal with it."
                c "I was wondering if you'd be willing to spend some time together."
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_e_smile") with dissolve
                e "Of course I would."
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_l_closeup") with dissolve
                l "Uh, hello?!"
                l "You just promised we were going for a walk together, just you and me."
                c "No, I didn't."
                c "Eva, will you join us?"
                scene expression eye_blink("images/ep008/ep008_simulation_stairs_e_smile") with dissolve
                e "Gladly."
                scene ep008_simulation_walk with dissolve
                "Lilly glared out of the corner of her eye, but much of her scorn was surprisingly directed at Eva."
                "We set out towards the garden, Lilly trailing after us in a foul mood."
                menu:
                    "[gr]Apologize to Eva" if True:
                        $ ep007_eva_apology = True
                        scene expression eye_blink("images/ep008/ep008_simulation_walk_e") with dissolve
                        c "Listen, Eva, I shouldn't have left you like that."
                        c "My sudden disappearance must have been awful for you."
                        c "I had no control over the situation, no means of getting a message to you, but I'm sorry nonetheless."
                        scene expression eye_blink("images/ep008/ep008_simulation_walk_e_smile") with dissolve
                        e "Thank you, [p_name_short]."
                        scene expression eye_blink("images/ep008/ep008_simulation_walk_e_serious") with dissolve
                        e "I was worried sick, but Lilly got me through."
                        e "I heard you when you finally came to visit."
                        e "I was angry with you then, returning like nothing had happened."
                        e "When I had finally mustered the courage to confront you, Lilly had already taken matters into her own hands."
                        e "So I'm sorry I just let her send you away, I really don't want you out of my life."
                        c "Me neither."
                    "Wait for her to speak" if True:
                        scene expression eye_blink("images/ep008/ep008_simulation_walk_e_serious") with dissolve
                        e "You came back..."
                        c "You sound a little surprised."
                        e "Can you blame me?"
                        c "I guess I can't."
                        c "Just know that I had no control over my absence all those months."
                        c "I couldn't even get a message out to you."
                        e "Did you try?"
                        c "You have to realize it was very complicated, but I did everything in my power to get back to you as soon as possible."
                        e "After several months..."
                        c "After several months."
                        c "I wanted to explain to you before, but-"
                        scene expression eye_blink("images/ep008/ep008_simulation_walk_e_sad") with dissolve
                        e "But I didn't want to see you."
                        c "So Lilly told me in no uncertain terms."
                        e "I'm not proud of that moment, to be honest."
                        scene expression eye_blink("images/ep008/ep008_simulation_walk_e_serious") with dissolve
                        e "I was angry with you then, returning like nothing had happened."
                        e "When I had finally mustered the courage to confront you, Lilly had already taken matters into her own hands."
                        e "She's been really there for me these past few months."
                        c "I'm glad to hear that."
                scene expression eye_blink("images/ep008/ep008_simulation_walk_l") with dissolve
                l "What are you two talking about?"
                "Lilly clearly got over her dampened spirits and possessively took my other arm."
                l "Every time I walk out here, I'm amazed by all the shit we own."
                scene expression eye_blink("images/ep008/ep008_simulation_walk_e_smile") with dissolve
                e "I think there are places on the estate I have never even explored."
                if game.is_special:
                    c "Dad does have that reputation as a grandiose landed gentleman to uphold."
                    l "He sure does seem less interested nowadays, than he did when we were younger."
                elif True:
                    c "My dad does have that reputation as a grandiose landed gentleman to uphold."
                scene expression eye_blink("images/ep008/ep008_simulation_clearing_e") with dissolve
                e "Guys?!"
                e "Isn't this the perfect spot for a picnic?"
                l "It sure is, just a shame we didn't bring anything."
                e "No matter, I'll go back and raid the kitchens."
                c "Want me to come with you?"
                scene expression eye_blink("images/ep008/ep008_simulation_clearing_e_smile") with dissolve
                e "No, I'll be back in no time."
                "I really wanted to go after her, but Lilly pulled me down to the ground while Eva left the clearing."
                scene ep008_clearing with dissolve
                l "Good, now I've got you all to myself."
                if game.is_special:
                    "My sister sat really close to me, her shoulder touching mine."
                elif True:
                    "My friend sat really close to me, her shoulder touching mine."
                "The whole scene evoked memories of the moments I shared with the real Lilly back in our cell on the research station."
                "In this case, it made me a little uncomfortable, partly because the change in behavior was so abrupt and of my doing."
                "I sat with her, silently cursing my decision to alter virtual Lilly's psychological profile."
                "We sat there for several long minutes, looking out over the grasslands."
                scene expression eye_blink("images/ep008/ep008_clearing_closeup") with dissolve
                l "Why are you so distracted?"
                c "Distracted, I-"
                l "Don't deny it."
                c "I was just thinking about some things."
                l "'Thinking about some things', could you be any more vague?!"
                scene expression eye_blink("images/ep008/ep008_clearing_closeup_angry") with dissolve
                l "You're thinking of her, aren't you?"
                l "You'd rather have gone with Eva."
                scene expression eye_blink("images/ep008/ep008_clearing_closeup_angry_alt") with dissolve
                l "Making a fucking picnic basket!"
                menu:
                    "[gr]Confirm" if True:
                        c "Yes, I would have."
                        scene expression eye_blink("images/ep008/ep008_clearing_closeup_angry_cry") with vpunch
                        l "It just isn't fair!"
                    "Deny" if True:
                        $ ep008_l_deny = True
                        c "No, I-"
                        scene expression eye_blink("images/ep008/ep008_clearing_closeup_angry_cry") with vpunch
                        l "Don't lie to me!"
                "By then, tears rimmed her eyes, fighting to replace her unleashed rage."
                l "Why do you want to be with her and not me?!"
                c "It isn't like th-"
                scene expression eye_blink("images/ep008/ep008_clearing_closeup_cry") with dissolve
                l "Don't you love me?"
                scene ep008_clearing_embrace with dissolve
                "While I was struggling to come up with a response, she advanced on me and pushed herself against me."
                "We were in quite an awkward position."
                l "I love you, [p_name_short]."
                l "I always have."
                l "I love you."
                "Her last statement was almost a plea."
                "Lilly looked up at me, meeting my eyes."
                scene ep008_clearing_embrace_kiss with vpunch
                "Her mouth sought mine and she suddenly kissed me."
                menu:
                    "[gr]Kiss her back" if True:
                        $ ep008_l_kiss = True
                        if ep006_lilly_kiss:
                            "The feelings that were awakened after the kiss I'd shared with Lilly on the research station burst into my mind again."
                        elif True:
                            "My feelings for Lilly were undeniable and burst into my mind with overwhelming intensity."
                        scene ep008_clearing_embrace_kiss_alt with dissolve
                        "I kissed her back without reservations."
                    "Push her away" if True:
                        "Feeling the wrongness of what we were about to do, I tried to push Lilly back."
                        "She held onto me with such strength, I was afraid I'd harm her if I pushed her away more violently."
                        "Lilly ignored my struggles and covered my lips with kisses, despite never finding reciprocation."
                scene expression eye_blink("images/ep008/ep008_clearing_alt") with dissolve
                "Just at that moment, Eva arrived on the scene, carrying a picnic basket."
                scene expression eye_blink("images/ep008/ep008_clearing_alt_shock") with vpunch
                "Aghast, she dropped the basket and backed away."
                scene ep008_clearing_alt_run with dissolve
                "When Lilly and I became aware of her, she'd already ran back towards the mansion, evidently distraught."
                c "Eva?!"
                scene expression eye_blink("images/ep008/ep008_clearing_alt_run_l") with dissolve
                l "Let her run."
                l "Just stay with me."
                "Lilly took my arm in a painful grip, but I wrenched free."

                menu:
                    "[gr]Run after her" if True:
                        $ ep008_simulation_pursue = True
                        scene ep008_clearing_alt_run_alt with dissolve
                        "I bolted before Lilly could respond and ran in the direction Eva had gone."
                        "She had a good head start, so when I reached the outskirts of the forest she'd already entered the mansion."
                        "As I entered the building I heard one of the doors upstairs slam shut."
                        scene ep008_simulation_stairs_alt with dissolve
                        "Hastily I ran up the stairs and paused before Eva's bedroom door."

                        call ep008_simulation_room from _call_ep008_simulation_room
                    "Pull out of the simulation" if True:

                        $ ep008_simulation_exit = True
                        scene ep008_simulation_room with pixellate
                        "Disgusted at what just happened, I pulled out of the simulation."
                        "My changes to Lilly's psych profile had clearly fucked things up majorly."
                        "The thought of reverting the profile to its prior state crossed my mind, but then it hit me that I had no way of knowing what the consequences of that would be."
                        "Considering what just happened, how would Lilly react when she was her old self?"
                        "The damage to Eva's trust was another thing I didn't know how to fix."

            if ep008_simulation_exit:
                menu:
                    "Clear the simulation [red]\[Ends all simulation scenes\]" if True:
                        $ ep008_simulation_clear = True
                        "Right then and there, I made a difficult decision, this couldn't continue."
                        scene ep008_simulation_room_alt with dissolve
                        "Digging into the simulation's settings I found the controls to erase everything."
                        if game.is_special:
                            "Initiating all this had brought me nothing but stress and the simulated versions of my sisters weren't happy either."
                        elif True:
                            "Initiating all this had brought me nothing but stress and the simulated versions of my friends weren't happy either."
                        "Steeling myself, I hit the delete button and watched the simulation initiate a full system wipe."
                        "It took a while for it to complete, but then the system was blank again."
                        scene ep008_quarters_sleep with dissolve
                        "I didn't know what to feel when I left the simulation room and when I got back to my quarters a numb sleep soon overtook me."
                    "Abandon the simulation" if True:
                        $ ep008_simulation_abandon = True
                        "Right then and there, I made a difficult decision."
                        "The simulation had an option to wipe the entire system."
                        "Although Eva and Lilly were digital copies in that simulation, I couldn't bear wiping out their existence."
                        "Neither could I go back into the viper's nest the simulation had become."
                        "So I took the coward's way out and put the system on standby."
                        scene ep008_quarters_sleep with dissolve
                        "I didn't know what to feel when I left the simulation room and when I got back to my quarters a numb sleep soon overtook me."
                    "Go back in" if ep008_simulation_alter and not ep008_simulation_pursue:
                        "A pang of regret, suddenly coursed through me."
                        "The whole mess in the simulation was of my own creation, so I needed to take action and resolve it."
                        "Resolved, I went back into the simulation in search of Eva."
                        scene ep008_clearing_empty with pixellate
                        "Again, I found myself in the clearing, but Lilly was nowhere in sight."
                        "With lead-filled shoes I made my way out of the forest and back to the mansion."
                        "Eva was nowhere to be found on the ground floor of the house."
                        scene ep008_simulation_stairs with dissolve
                        "I walked up the stairs and paused before Eva's bedroom door."

                        call ep008_simulation_room from _call_ep008_simulation_room_1

            play music [ "music/searching-the-cosmos.ogg", "music/the-restoration.ogg", "music/space-harmony.ogg" ] fadeout 4 fadein 1.0

            jump ep008_conversation_choices

label ep008_simulation_room:
    scene ep008_simulation_door with dissolve
    c "Eva?"
    c "Can I come in?"
    "She didn't respond."
    menu:
        "[gr]Enter her room" if True:
            scene ep008_simulation_door_open with dissolve
            "Resolved, I pushed open the door."
            scene ep008_simulation_bed with dissolve
            "Eva was lying on her bed, facing the wall and crying silently."
            scene ep008_simulation_bed_sit with dissolve
            "She didn't react to my presence, even when I sat down next to her on the bed."
            c "Eva, I just want to talk."
            c "What you just saw in the forest...{w} I didn't want that."
            c "Lilly has been acting weird around me and she just threw herself at me."
            scene ep008_simulation_bed_shoulder with dissolve
            "I dared to touch her shoulder."
            "Eva flinched at first, but didn't pull away."
            "Instead she turned to face me."
            "I expected to find shocked revulsion, but instead she only looked at me in anguish."
            scene expression eye_blink("images/ep008/ep008_simulation_bed_e") with dissolve
            e "Why her?!"
            "That wasn't really the question I was expecting."
            if game.is_special:
                c "I love Lilly like a sister, nothing more."
            elif True:
                c "I love Lilly like a friend, nothing more."
            c "What she did today shocked me just as much as you."
            "Eva looked at me, her lip trembling."
            e "So you think it's wrong, what she did?"
            c "Yes."
            "I answered before I could think about the hidden meaning of Eva's questions and cursed myself for it immediately."
            scene expression eye_blink("images/ep008/ep008_simulation_bed_e_cry") with dissolve
            "Eva started to cry again."
            c "Eva, please, tell me what's the matter?"
            e "No, no, I can't."
            e "You'd think I'm just as terrible as Lilly."
            c "No, I won't."
            e "Of course you will."
            scene expression eye_blink("images/ep008/ep008_simulation_bed_e_cry_serious") with dissolve
            e "Any sane person would."
            c "Try me."
            scene ep008_simulation_bed_window with dissolve
            "Eva shuddered and averted her gaze from me, looking out of the window for a long time."
            "She drew a ragged breath and calmed down a little."
            "When she looked at me again she seemed more determined."
            scene expression eye_blink("images/ep008/ep008_simulation_bed_e_serious") with dissolve
            e "You've been away a lot."
            c "I'd like to apologize for that."
            e "No, it isn't a reproach, just stating a fact."
            e "You've been away for longer periods of time before."
            e "But it has never affected me like it did recently."
            scene expression eye_blink("images/ep008/ep008_simulation_bed_e_sad") with dissolve
            e "I've missed you, [p_name_short]."
            e "I thought of you every day while you were gone."
            c "I never intended to be callous about your feelings."
            c "I know how you care for me, Eva."
            scene expression eye_blink("images/ep008/ep008_simulation_bed_e_serious") with dissolve
            e "No, you don't...{w} not really."
            e "I have come to realize that I have feelings for you, [p_name_short]."
            if game.is_special:
                e "Something way beyond what a normal person should feel for her brother..."
            elif True:
                e "Something way beyond what a normal person should feel for a childhood friend..."
            scene expression eye_blink("images/ep008/ep008_simulation_bed_e_fear") with dissolve
            e "I love you, [p_name]."
            e "When I look at you, my heart skips."
            e "I know it's wrong and it disgusts me at the same time."
            scene expression eye_blink("images/ep008/ep008_simulation_bed_e_sad") with dissolve
            e "I shouldn't feel this way..."
            menu:
                "[gr]Tell her you love her" if True:
                    $ ep008_eva_love = True
                    "Eva's words triggered something inside me."
                    "What she described, I felt too."
                    if game.is_special:
                        "We'd always been close, shared a familiarity I'd taken for granted as a sibling bond."
                    elif True:
                        "We'd always been close, shared a familiarity I'd taken for granted as a bond of friendship."
                    "She made me realize that bond went deeper."
                    "I needed her, loved her...{w} desired her."
                    c "Don't let others dictate what you should feel."
                    c "I love you too, Eva."
                    e "But?"
                    scene expression eye_blink("images/ep008/ep008_simulation_bed_e_fear") with dissolve
                    e "Like that?"
                    scene ep008_simulation_bed_kiss with dissolve
                    "By way of an answer, I edged closer to her and kissed Eva on her lips."
                    scene ep008_simulation_bed_kiss_alt with dissolve
                    "She responded to my kiss immediately by parting her lips."
                    "Our tongues met."
                    scene expression eye_blink("images/ep008/ep008_simulation_bed_kiss_alt_closeup") with dissolve
                    "She was out of breath when we separated, so I spoke before she could ask me anything more."
                    c "Yes, like that."
                    scene ep008_simulation_bed_kissing with dissolve
                    "Overjoyed, Eva kissed me again and we tumbled on the bed."

                    play music "music/night-terrors.ogg" fadeout 4 fadein 1.0

                    scene ep008_simulation_bed_l with vpunch
                    "At that moment, the door was thrown open."
                    "Lilly was standing in the doorway, gaping in a mixture of horror and rage."
                    scene expression eye_blink("images/ep008/ep008_simulation_bed_l_closeup") with dissolve
                    l "You fucking piece of shit!"
                    l "YOU FUCKING PIECE OF SHIT!"
                    "Lilly kept repeating the same sentence over and over."
                    scene ep008_simulation_bed_l_e with dissolve
                    "Eva stared at her in fear and I noticed I'd unconsciously shielded her with my body."
                    scene ep008_simulation_bed_l_glitch with dissolve
                    "Suddenly, Lilly stopped speaking and turned her head towards the floor."
                    "I thought the simulation had somehow deactivated her avatar, but I was wrong."
                    scene ep008_simulation_bed_l_glitch_alt with vpunch
                    "Lilly's head jerked upwards, mouth agape and murder in her eyes."
                    "An inhuman wail escaped her, slowly transforming into an ungodly screeching that seemed to assault all of my senses."
                    scene ep008_simulation_bed_l_glitch_e with dissolve
                    "Behind me, Eva was muttering the same string of words over and over again."
                    "The sense of familiar safety I'd always felt in the simulation was completely gone, replaced by a horrific cacophony of rage emanating from Lilly."
                    scene ep008_simulation_bed_l_glitch_e_alt with dissolve
                    "Frantically, I tried to pull out of it, but the system wouldn't let me."
                    "As the sound reached a crescendo I thought my brain would turn to mush."
                    scene ep008_simulation_bed_l_glitch_crash with vpunch
                    "Suddenly all of the scenery dropped away."
                    "Lilly and Eva were still there for a moment, until they disintegrated suddenly."
                    scene ep008_simulation_bed_l_glitch_empty with vpunch
                    "The noise was gone and I was alone in total darkness."
                    "After taking a few shuddering breaths I attempted to pull of out the simulation again."
                    scene ep008_simulation_room_exit with pixellate
                    "This time I succeeded."
                    "I didn't know what had just happened, but I was pretty sure the simulation had malfunctioned in a big way."
                    "Running a full diagnostics report would have to wait until I'd mustered the courage again to deal with the craziness that had become the simulation."
                    scene ep008_quarters_sleep with dissolve
                    "I staggered back to my quarters and fell into a numb sleep for several hours."
                "Put an end to this" if True:
                    c "I understand why this is hard for you."
                    if game.is_special:
                        c "And I love you too, but only as a brother."
                        c "As you say, anything else is not natural."
                    elif True:
                        c "And I love you too, but only as a friend."
                    c "I'm sorry Eva, but you have to put all this out of your head."
                    scene expression eye_blink("images/ep008/ep008_simulation_bed_e_sad") with dissolve
                    e "I know, I'm sorry, [p_name_short]."
                    e "I won't bring it up again."
                    e "I don't want things to be awkward between us."
                    c "I'm not sure that will be possible, but I'm willing to try."
                    e "Me too."
                    scene ep008_simulation_bed_window with dissolve
                    "I left Eva then, looking wistfully out of the window."
                    scene ep008_simulation_room with pixellate
                    "As soon as I was standing in the small simulation room again, I put the system on standby."
                    "I wasn't sure if I ever wanted to come back to this strange place the simulation had become."
                    scene ep008_quarters_sleep with dissolve
                    "I walked back to my quarters and fell into a numb sleep for several hours."
        "Leave the simulation" if True:
            $ ep008_simulation_exit = True
            scene ep008_simulation_room with pixellate
            "Despondent, I pulled out of the simulation immediately."
            "I didn't know how to fix things anymore."
            "The damage to Eva's trust seemed irreparable and the changes I'd made to Lilly's personality clearly fucked things up even more."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
