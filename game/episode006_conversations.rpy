label ep006_conversations:

    if 'ep006_conversations_init' not in locals():
        $ ep006_conversations_init = True

        $ ep006_lilly_talk = False
        $ ep006_nadya_talk = False
        $ ep006_aven_talk = False
        $ ep006_raene_talk = False
        $ ep006_eva_talk = False
        $ ep006_aven_understand = False
        $ ep006_raene_accept = False
        $ ep006_ra_ziv_talk = False
        $ ep006_ra_research_talk = False
        $ ep006_ra_mother_talk = False
        $ ep006_ra_father_talk = False
        $ ep006_ra_comfort = False
        $ ep006_ra_dismissive = False
        $ ep006_ra_demand = False

    play music [ "music/thunderbird.ogg", "music/the-restoration.ogg", "music/space-harmony.ogg", "music/searching-the-cosmos.ogg" ] fadeout 4 fadein 1.0

    label ep006_conversation_choices:
        $ choices = [
                {
                    'name': 'Lilly',
                    'action': 'ep006_lilly_talk',
                    'visible': True if not ep006_lilly_talk else False
                },
                {
                    'name': 'Aven',
                    'action': 'ep006_aven_talk',
                    'visible': True if not ep006_aven_talk and ep006_lilly_talk and (ep006_aven_feelings or ep006_lilly_kiss) else False
                },
                {
                    'name': 'Raene',
                    'action': 'ep006_raene_talk',
                    'visible': True if not ep006_raene_talk else False
                },
                {
                    'name': 'Eva',
                    'action': 'ep006_eva_talk',
                    'visible': True if not ep006_eva_talk else False
                }
            ]

        scene black with fade
        $ conversation_menu(choices)
        scene black with fade
        return

        label ep006_lilly_talk:
            $ ep006_lilly_talk = True

            scene ep006_l_door with dissolve
            "Lilly had retired to her quarters almost immediately after we set course for Almagest."

            if ep006_lilly_kiss:
                "I never got the chance to talk to her after we regained our memories and I longed to be near her again."
                "I knocked on her door and after a while she opened the door just slightly."
                scene expression eye_blink("images/ep006/ep006_l_door_open") with dissolve
                l "Oh, it's you."
                "Not quite the welcome I was hoping for..."
                c "Are you okay?"
                l "Yes, I just fell asleep back there."
                c "I can imagine, probably the after-effects of the drugs they gave us."
                l "Probably."
                c "Do you mind if I come in?"
                scene expression eye_blink("images/ep006/ep006_l_door_open_sad") with dissolve
                l "I'm really tired, [p_name_short]."
                c "I know, but we really should talk about what happened back in that cell."
                l "What happened back in that cell?"
                c "You know...{w} us..."
                c "Don't you remember?"
                scene expression eye_blink("images/ep006/ep006_l_door_open_serious") with dissolve
                l "No, I don't."
                c "But..."
                l "I really want to go to sleep now."
                scene ep006_l_door with dissolve
                "Before I could get another word in edgewise she'd already closed the door."
            else:
                "After being together with her for so long, I just wanted to know if she was okay."
                "I knocked on her door and after a while she opened the door."
                scene expression eye_blink("images/ep006/ep006_l_door_open") with dissolve
                l "Oh, hey [p_name_short]."
                l "I just fell asleep back there."
                c "Probably an after-effect of the drugs they gave us."
                c "Are you alright?"
                scene expression eye_blink("images/ep006/ep006_l_door_open_serious") with dissolve
                l "I think so."
                if ep006_lilly_comfort:
                    l "No dreams, so far."
                c "I'm glad to hear that."
                c "You know where to find me, should that change."
                l "I do, thanks [p_name_short]."
            jump ep006_conversation_choices

        label ep006_aven_talk:
            $ ep006_aven_talk = True
            if ep006_aven_feelings and ep006_lilly_kiss:
                scene expression eye_blink("images/ep006/ep006_av") with dissolve
                c "Hey, how are you holding up?"
                av "Just barely."
                av "What a mess."
                c "Yeah, this is not how I pictured things."
                scene expression eye_blink("images/ep006/ep006_av_sad") with dissolve
                av "Me neither, I just can't deal with all this at the moment, to be honest."
                av "We made a promise to have a talk after our escape and we really should..."
                av "Just not now, [p_name_short], I hope you understand."

                menu:
                    "I don't":
                        c "No, I don't."
                        c "We have to resolve this mess, right now."
                        scene expression eye_blink("images/ep006/ep006_av_angry") with dissolve
                        av "No, we don't."
                        av "Let's wait until we've both processed all of this, unless we might say something one of us is going to regret later."
                        scene expression eye_blink("images/ep006/ep006_av_sad") with dissolve
                        av "I'm sorry, [p_name_short]."
                        c "Can you at least answer me this though, do you remember anything from while we were on the station?"
                        c "Before we regained our memories, I mean."
                        av "Yes, I can, vividly."
                        scene expression eye_blink("images/ep006/ep006_av_doubt") with dissolve
                        av "Why are you bringing this up?"
                        c "Lilly says she doesn't remember anything."
                        av "Maybe it works differently for everyone?"
                        c "Maybe."
                        scene expression eye_blink("images/ep006/ep006_av") with dissolve
                        av "Or maybe she just doesn't want to talk about it."
                        c "That sounds familiar..."
                        scene expression eye_blink("images/ep006/ep006_av_angry") with dissolve
                        av "Don't be so damn salty."
                    "I do [AvenPath]":
                        $ ep006_aven_understand = True
                        c "I think I do."
                        scene expression eye_blink("images/ep006/ep006_av_sad") with dissolve
                        av "Let's wait until we've both processed this entire mind fuck and see where we stand, okay?"
                        c "Agreed."
                        c "One thing that's been bothering me, can you remember anything from while we were on the station?"
                        c "Before we regained our memories, I mean."
                        av "Yes, I can, vividly."
                        scene expression eye_blink("images/ep006/ep006_av_doubt") with dissolve
                        av "Why are you bringing this up?"
                        c "Lilly says she doesn't remember anything."
                        av "Maybe it works differently for everyone?"
                        c "Maybe."
                        scene expression eye_blink("images/ep006/ep006_av") with dissolve
                        av "Or maybe she just doesn't want to talk about it."
                        c "That thought has crossed my mind."
                        av "I'm sure she'll come around eventually."
                        av "You do have a lot to talk about though and I think you really should once you're both ready."
                        scene expression eye_blink("images/ep006/ep006_av_sad") with dissolve
                        av "This whole trip has been one big mindfuck."
                        c "You can say that again."
                        av "I'm here if you need me."
                        c "Thanks, I'll keep that in mind."
                        scene expression eye_blink("images/ep006/ep006_av_smile") with dissolve
                        av "Good night, [p_name_short]."
                        c "Good night, Aven."
            elif ep006_aven_feelings:
                scene expression eye_blink("images/ep006/ep006_av") with dissolve
                c "Hey, how are you holding up?"
                av "Just barely."
                av "What a mess."
                c "Yeah, this is not how I pictured things."
                scene expression eye_blink("images/ep006/ep006_av_sad") with dissolve
                av "Me neither, I just can't deal with all this at the moment, to be honest."
                av "We made a promise to have a talk after our escape and we really should..."
                av "Just not now, [p_name_short], I hope you understand."

                menu:
                    "I don't":
                        c "No, I don't."
                        c "We have to resolve this mess, right now."
                        scene expression eye_blink("images/ep006/ep006_av_angry") with dissolve
                        av "No, we don't."
                        av "Let's wait until we've both processed all of this, unless we might say something one of us is going to regret later."
                        scene expression eye_blink("images/ep006/ep006_av_sad") with dissolve
                        av "I'm sorry, [p_name_short]."
                    "I do [AvenPath]":
                        $ ep006_aven_understand = True
                        c "I think I do."
                        scene expression eye_blink("images/ep006/ep006_av_sad") with dissolve
                        av "Let's wait until we've both processed this entire mind fuck and see where we stand, okay?"
                        c "Agreed."
                        scene expression eye_blink("images/ep006/ep006_av_smile") with dissolve
                        av "Good night, [p_name_short]."
                        c "Good night, Aven."
            elif ep006_lilly_kiss:
                scene expression eye_blink("images/ep006/ep006_av") with dissolve
                c "Hey, how are you holding up?"
                av "I'm fine, thanks for asking."
                c "I'm just wondering, can you remember anything from while we were on the station?"
                c "Before we regained our memories, I mean."
                av "Yes, I can, vividly."
                scene expression eye_blink("images/ep006/ep006_av_doubt") with dissolve
                av "Why are you bringing this up?"
                c "Lilly says she doesn't remember anything."
                av "Maybe it works differently for everyone?"
                c "Maybe."
                av "Or maybe she just doesn't want to talk about it."
                c "That thought has crossed my mind."
                scene expression eye_blink("images/ep006/ep006_av") with dissolve
                av "I'm sure she'll come around eventually."
                av "You do have a lot to talk about though and I think you really should once you're both ready."
                scene expression eye_blink("images/ep006/ep006_av_sad") with dissolve
                av "This whole trip has been one big mindfuck."
                c "You can say that again."
                scene expression eye_blink("images/ep006/ep006_av") with dissolve
                av "I'm here if you need me."
                c "Thanks, I'll keep that in mind."
            jump ep006_conversation_choices

        label ep006_raene_talk:
            $ ep006_raene_talk = True
            scene expression eye_blink("images/ep006/ep006_ra") with dissolve
            c "I was wondering if we could talk."
            ra "If it's about what happened back on the research station, don't worry, I'm fine now."
            c "I'm sure you are, but I still like to know what happened to you back there."
            scene expression eye_blink("images/ep006/ep006_ra_doubt") with dissolve
            ra "Why?"
            menu:
                "Placate [RaenePath]":
                    c "Because I'd hate for you to feel so distraught."
                    c "Something on the station triggered some heavy emotions in you and I don't want you to think you have to go through all that on your own."

                    if (ep004_ra_confront_angry + ep004_ra_doubt + ep004_ra_angry + ep005_ra_intimidate + ep006_ra_berate + ep006_ra_ignore) < 1:
                        scene expression eye_blink("images/ep006/ep006_ra") with dissolve
                        ra "You've said so before and I believe you."
                        ra "I...{w} I don't know where to begin, really."
                        c "Why not at the beginning?"
                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                        ra "That might be best."
                        ra "I carry my mother's name, she was called Rae."
                        scene expression eye_blink("images/ep006/ep006_ra_smile") with dissolve
                        ra "It's a name I wear with pride."
                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                        ra "On our world women are mostly regarded as a necessary evil, because of their ability to bear children."
                        ra "Other than that they live their lives in seclusion and don't participate in daily life."
                        ra "They serve at the pleasure of the men who rule Verdigris, my father at the head of it all. "
                        ra "I had a different name when I was born, one that my father still uses when he addresses me."
                        ra "He was so happy my mother bore him a son, because an heir would secure our bloodline."
                        scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                        ra "I've been a disappointment to him ever since I could barely speak."
                        ra "I've never been the son he wanted, needed even, deep down I've always been Raene."

                        menu:
                            "Be accepting [RaenePath]":
                                $ ep006_raene_accept = True
                                c "I'm really glad you decided to tell me."
                                c "A lot of things are starting to click now."
                                scene expression eye_blink("images/ep006/ep006_ra") with dissolve
                                c "Like your behavior in the locker room back on the research station, having to wear those men's clothes."
                                ra "I know it seems so futile considering what we were up against back there."
                                scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                                ra "But it all came flooding in all of a sudden."

                                menu ep006_ra_conversation:
                                    "Relationship with Ziv" if not ep006_ra_ziv_talk:
                                        $ ep006_ra_ziv_talk = True
                                        c "Your relationship with Ziv is no coincidence, I presume?"
                                        scene expression eye_blink("images/ep006/ep006_ra") with dissolve
                                        ra "No, I managed to reach out to her people while a delegation visited Verdigris."
                                        ra "The non-binary nature of the Rhenkoy is well-known throughout the galaxy."
                                        c "So I've heard."
                                        c "Considering what I've heard about your planet those meetings with the Rhenkoy delegation must have been rather chilly?"
                                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                                        ra "I'm sure of it, but The Mysteries were more or less forced to deal with them as a courtesy to other political factions."
                                        ra "Nothing ever came of the meeting, of course."
                                        c "The Mysteries?"
                                        scene expression eye_blink("images/ep006/ep006_ra") with dissolve
                                        ra "Yes, the ruling council of wise men on my planet, my father is their leader."
                                        c "Right."
                                        c "So Ziv's people managed to take you away and hide you?"
                                        ra "They did for a while, before you and Ziv picked us up."
                                        ra "During the time in hiding on Verdigris they prepared me for the process of transitioning."
                                        ra "Ziv was the one who finally administered the first treatment on the Bastard."
                                        if ep004_ra_confront:
                                            ra "But you kinda knew that already."
                                        jump ep006_ra_conversation
                                    "About the research station" if not ep006_ra_research_talk:
                                        $ ep006_ra_research_talk = True
                                        c "You were pretty rattled back on the station."
                                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                                        ra "I was."
                                        scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                                        ra "It's stupid really."
                                        c "You keep saying that and I don't think it's stupid at all."
                                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                                        ra "It's just that I woke from that storage pod and we were in such a hurry that I only realized later that they dressed me the same as you."
                                        scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                                        ra "Of course, they probably just looked at what's between my legs, but at that moment everything just rushed into me."
                                        ra "I just realized I still have a long way to go."
                                        c "You've come far already."
                                        c "Leaving your home under those circumstances, beginning the treatment with Ziv..."
                                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                                        ra "I know."
                                        ra "It's just that there are going to be more moments like these and I hope I'm prepared for them."
                                        menu:
                                            "Comfort her [RaenePath]":
                                                $ ep006_ra_comfort = True
                                                c "I'm sure there will, but never doubt yourself because of how others treat or perceive you."
                                                c "And know that I'll be here for you if it ever wears you down."
                                                scene expression eye_blink("images/ep006/ep006_ra_smile_alt") with dissolve
                                                ra "Thank you, [p_name_short], that means a lot."
                                            "Reassure her":
                                                c "There might be, but I'm sure you can handle it."
                                                c "Making your choice was a courageous thing to do, it shows true character."
                                                scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                                                ra "I guess."
                                        jump ep006_ra_conversation
                                    "Her mother" if not ep006_ra_mother_talk:
                                        $ ep006_ra_mother_talk = True
                                        c "You mentioned Rae, your mother, did she know about your attempt to escape Verdigris?"
                                        scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                                        ra "No...{w} That is...{w} I should have told you..."
                                        ra "My mother passed away when I was barely five years old."
                                        c "Oh...{w} I'm so sorry to hear that."
                                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                                        ra "I have some memories of her and a picture I cherish."
                                        ra "She wasn't a constant presence in my early life, because women are only allowed to provide the necessary care for a child, the rest is the duty of the men."
                                        ra "At least, that's the case for sons, daughters are whisked away in whatever compound the mothers are held."
                                        c "That sounds awful, to be honest."
                                        ra "It is."
                                        scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                                        ra "At the age of five I would have lost my mother anyway, because the upbringing is left solely to the fathers at that age."
                                        ra "My mother fell ill weeks after my fourth birthday and died not long after."
                                        scene expression eye_blink("images/ep006/ep006_ra") with dissolve
                                        ra "My father, or rather the staff he hired, cared for me ever since."
                                        c "I don't know what to say..."
                                        c "What an awful childhood."
                                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                                        ra "It wasn't all bad, but I wouldn't call it happy."
                                        c "No, not at all."
                                        jump ep006_ra_conversation
                                    "Her father" if not ep006_ra_father_talk:
                                        $ ep006_ra_father_talk = True
                                        c "You told me your father still considers you his son?"
                                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                                        ra "He does."
                                        scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                                        ra "He probably thinks he can still change me...{w} Cure me..."
                                        c "Right."
                                        c "Do you think he wants to do that out of the misguided love of a parent, or is there more at play?"
                                        scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                                        ra "Partly, I think."
                                        ra "My father is a very guarded person, he doesn't show his feelings at all, so it's hard to know what he wants for me."
                                        scene expression eye_blink("images/ep006/ep006_ra") with dissolve
                                        ra "The title of Hierophant is not hereditary, but it has been in my family for several generations."
                                        ra "He probably thought of me as his successor once, before I became a growing embarrassment."
                                        ra "Now I'm not so sure if he's looking to save me, or control the damage I might do to his reputation."
                                        c "Either way sounds misguided."
                                        scene expression eye_blink("images/ep006/ep006_ra_smile") with dissolve
                                        ra "It does, doesn't it?"
                                        jump ep006_ra_conversation

                                scene expression eye_blink("images/ep006/ep006_ra") with dissolve
                                c "I'm glad you confided in me, Raene."
                                ra "It felt good to talk to you, to be honest."
                                scene expression eye_blink("images/ep006/ep006_ra_smile_alt") with dissolve
                                ra "Thank you, [p_name]."
                                c "Sleep well, Raene."
                                ra "You too, [p_name_short]."
                            "Be dismissive":
                                $ ep006_ra_dismissive = True
                                c "I suspected as much."
                                c "Well, so you know, I don't mind."
                                scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                                ra "I'm glad to hear that."
                                c "Ziv is treating you, I suppose?"
                                ra "She is."
                                c "Good, I hope you feel welcomed here and will continue to do so."
                                scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                                ra "Er...{w} I am and I hope so too."
                                c "Sleep well."
                                ra "You too."
                    else:
                        scene expression eye_blink("images/ep006/ep006_ra_sad") with dissolve
                        ra "Thank you, [p_name]."
                        ra "But I'm fine now, I really am."
                        c "If you say so, just know that you can talk to me any time."
                "Demand":
                    $ ep006_ra_demand = True
                    c "Because, as the commander of this vessel, I have a right to know."
                    scene expression eye_blink("images/ep006/ep006_ra_serious") with dissolve
                    ra "I can assure you that nothing is the matter now."
                    ra "Really, it won't happen again."
                    c "If you say so..."
            jump ep006_conversation_choices

        label ep006_eva_talk:
            $ ep006_eva_talk = True

            scene ep006_bastard_sim with dissolve
            "Ever since we boarded the Bastard my mind wandered towards Eva."
            "I dreaded going back into the simulation, especially considering we'd been away for almost six months."
            "Just before leaving Barranthis I had loaded Lilly's profile into the system, but I couldn't find a quiet moment to actually enter simulation."
            scene ep006_bastard_sim_garden with pixellate
            "I found myself in the garden, on the small bridge where she'd said goodbye last time."
            "With a heavy sense of foreboding I approached the house."
            scene ep006_bastard_sim_veranda with dissolve
            "I saw no sign of her, nor Lilly on the veranda, so I went into the house."
            scene ep006_bastard_sim_interior with dissolve
            c "Eva?"
            c "Lilly?"
            c "I'm back."
            "The downstairs rooms were all quiet."
            "The fire in the hearth had gone out quite some time ago."
            scene ep006_bastard_sim_stairs with dissolve
            "I went upstairs to Eva and Lilly's bedrooms."
            scene ep006_bastard_sim_upstairs with dissolve
            c "Are you there?"
            c "I'm sorry it took me so long to get back, but I can explain."
            c "Eva?"
            scene expression eye_blink("images/ep006/ep006_bastard_sim_upstairs_l") with vpunch
            "At that moment the door to Eva's room slammed open and a fuming Lilly barged into the hallway."
            l "Will you shut the fuck up already?!"
            l "Isn't it clear she doesn't want to see you."
            l "She's been asking for you every day, thinking that something happened to you."
            scene expression eye_blink("images/ep006/ep006_bastard_sim_upstairs_l_alt") with dissolve
            l "You told her you'd meet her at the house, instead you're gone for months."
            l "How could you leave her like that?"
            "Seeing Lilly so hostile like this rattled me severely."
            "I'd come to know her so differently after being so close together on the ConVitae research station."
            c "I...{w} I can explain."
            scene expression eye_blink("images/ep006/ep006_bastard_sim_upstairs_l") with dissolve
            l "Of course you can."
            l "We're just not interested."
            l "Leave us alone, [p_name_short], you've done enough harm already."
            scene ep006_bastard_sim_upstairs with vpunch
            "She slammed the door in my face and left me standing there in the hallway."
            scene ep006_bastard_sim with pixellate
            "I immediately pulled out of the simulation and rushed back to my room, wondering desperately how the fuck I could fix this."
            jump ep006_conversation_choices
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
