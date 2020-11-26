label ep003_conversations:

    if 'ep003_conversations_init' not in locals():
        $ ep003_conversations_init = True

        $ ep003_vess_talk = False
        $ ep003_vess_understanding = False
        $ ep003_vess_hug = False
        $ ep003_lilly_talk = False
        $ ep003_lilly_kind = False
        $ ep003_lilly_nadya_talk = False
        $ ep003_lilly_talk_mission = False
        $ ep003_lilly_dismiss = False
        $ ep003_jade_talk = False
        $ ep003_jade_curt = False
        $ ep003_aven_talk = False
        $ ep003_aven_lilly_deride = False
        $ ep003_celine_talk = False
        $ ep003_celine_message = False
        $ ep003_thyia_talk = False
        $ ep003_thyia_coy = False

    play music [ "music/the-restoration.ogg", "music/space-harmony.ogg", "music/searching-the-cosmos.ogg" ] fadeout 4 fadein 1.0

    label ep003_conversation_choices:
        $ choices = [
                {
                    'name': 'Vess',
                    'action': 'ep003_vess_talk',
                    'visible': True if not ep003_vess_talk else False
                },
                {
                    'name': 'Lilly',
                    'action': 'ep003_lilly_talk',
                    'visible':  True if not ep003_lilly_talk or (ep003_aven_talk and not ep003_lilly_talk_mission) else False
                },
                {
                    'name': 'Jade',
                    'action': 'ep003_jade_talk',
                    'visible':  True if not ep003_jade_talk else False
                },
                {
                    'name': 'Aven',
                    'action': 'ep003_aven_talk',
                    'visible':  True if not ep003_aven_talk else False
                },
                {
                    'name': 'Kit',
                    'action': 'ep003_celine_talk',
                    'visible':  True if not ep003_celine_talk else False
                },
                {
                    'name': 'Thyia',
                    'action': 'ep003_thyia_talk',
                    'visible':  True if not ep003_thyia_talk else False
                }
            ]

        scene black with fade
        $ conversation_menu(choices)
        scene black with fade
        return

        label ep003_vess_talk:
            $ ep003_vess_talk = True
            scene expression eye_blink("images/ep003/ep003_quarters_vess") with dissolve
            ve "I thought we were done for back in the asteroid field."
            c "Yeah, we cut it close."
            if ep003_verdant_visit_first:
                ve "We’re heading to a space station now?"
                c "Yes, for some repairs, maybe hit a bar as well and get a decent meal."
                scene expression eye_blink("images/ep003/ep003_quarters_vess_doubt") with dissolve
                ve "That sounds nice, but will it be as crowded as Ryūjin Prime?"
                c "Probably not, but space stations are a lot more cramped, so you might have the same feeling as on Ryūjin."
                if ep002_vess_reassure:
                    c "I’ll be there for you."
                else:
                    c "You could stay on the ship if you want."
            else:
                ve "We're heading to a planet now?"
                c "Yes, we need to get that specimen for Hreir."
                scene expression eye_blink("images/ep003/ep003_quarters_vess_doubt") with dissolve
                ve "Will that be dangerous?"
                c "Probably not, Sagueliath doesn't really sound like a hospitable planet."
                ve "I guess I'll be okay if I stay with the ship..."
                if ep002_vess_reassure:
                    c "I’ll make sure nothing happens to you."
                else:
                    c "Just stay on the ship and wait until we come back."

            menu:
                "Be understanding [VessPath]":
                    $ ep003_vess_understanding = True
                    c "To be honest, I feel bad for dragging you along across all those worlds."
                    c "Must be hard, coming from that quiet rural life and being thrust into all this."
                    scene expression eye_blink("images/ep003/ep003_quarters_vess_smile") with dissolve
                    ve "Don’t worry, it’s for a good cause."
                    ve "It’s quite exciting so far and I think I’m even starting to like it."
                    c "Well, I’m sure there’s more to come, so you better brace yourself."
                    scene expression eye_blink("images/ep003/ep003_quarters_vess_laugh") with dissolve
                    ve "Haha, I will."
                    scene expression eye_blink("images/ep003/ep003_quarters_vess_smile") with dissolve
                    ve "Hey [p_name]?"
                    c "You can call me [p_name_short] if you want, everyone does it."
                    ve "Okay, [p_name_short], what’s it like growing up in the more crowded part of the Sovereignty?"
                    c "I spent most of my youth on Tuolovi, not exactly a bustling metropolis."
                    ve "You grew up on a farm too?"
                    c "No, but there are farms on my parents’ estate though."
                    scene expression eye_blink("images/ep003/ep003_quarters_vess_doubt") with dissolve
                    ve "An estate?"
                    ve "So your parents are rich?"
                    c "I’m sure they see it otherwise, but yeah, they have money."
                    c "I think that’s the second-most important thing in their lives, besides influence."
                    ve "I’m sure your parents love you."
                    c "If they do, they sure as shit know how to hide it well."
                    scene expression eye_blink("images/ep003/ep003_quarters_vess_serious") with dissolve
                    ve "Oh..."
                    c "Yeah."
                    c "Growing up on Tuolovi was nice, but part of me is very glad we eventually got sent away to the academy."
                    c "But enough about me, what was it like on Lanan?"
                    ve "Nothing much to tell really."
                    ve "I mean, you’ve seen the place."
                    c "Some would call it quaint."
                    ve "Right."
                    ve "It was mostly muddy and dreary to be honest."
                    c "And your folks?"
                    scene expression eye_blink("images/ep003/ep003_quarters_vess_sad") with dissolve
                    ve "My...{w} I..."
                    ve "Sorry, [p_name_short], it’s still hard for me to talk about."
                    c "It’s okay if you don’t want to."
                    ve "I know...{w} It’s just..."
                    ve "Whenever I think about them I see them taken away by those women."
                    ve "I was so scared."

                    menu:
                        "Hold her [VessPath]":
                            $ ep003_vess_hug = True
                            scene ep003_quarters_vess_hug with dissolve
                            "Vess started crying and I just held her while she sobbed."
                            "Once she’d calmed, the girl said a teary goodbye, wanting to rest for a while."
                        "Leave her":
                            c "Sorry, I shouldn’t have asked."
                            scene expression eye_blink("images/ep003/ep003_quarters_vess_sad_alt") with dissolve
                            ve "It’s okay."
                            "Despite her lip trembling, Vess maintained her composure, but told me she wanted to rest for a while."
                "Leave her":
                    c "Well, gotta run."
                    scene expression eye_blink("images/ep003/ep003_quarters_vess_serious") with dissolve
                    ve "See you later."
            jump ep003_conversation_choices

        label ep003_lilly_talk:
            scene expression eye_blink("images/ep003/ep003_quarters_lilly") with dissolve

            l "Hey [p_name_short]."
            c "Hi, you seem to be in a good mood."
            l "I am."

            menu ep003_lilly_dialogue:
                "About Nadya and Aven" if not ep003_lilly_nadya_talk:
                    $ ep003_lilly_nadya_talk = True
                    if game.is_special:
                        l "Asking Aunt Nadya to come with us turned out to be a good idea."
                    else:
                        l "Asking Nadya to come with us turned out to be a good idea."
                    c "You really think so?"
                    scene expression eye_blink("images/ep003/ep003_quarters_lilly_smile") with dissolve
                    l "Yes, you were right, she can help us."
                    l "And it’s nice to have family aboard."
                    l "Aven and me already talked for hours on end, we had so much to catch up on."
                    if game.is_special:
                        c "And Aunt Nadya doesn’t seem to hate us at all."
                    else:
                        c "And Nadya doesn’t seem to hate us at all."
                    l "No, on the contrary."
                    l "A little weird though that she never contacted or visited us after leaving."
                    scene expression eye_blink("images/ep003/ep003_quarters_lilly_serious") with dissolve
                    if game.is_special:
                        l "But whenever I mention mom or dad she gets that look in her eyes."
                        l "Something really bad happened between them, I’m sure of it."
                        c "Yeah, I think you’re right."
                        c "Maybe she’ll tell us, eventually."
                        l "Maybe."
                    else:
                        l "But whenever I mention the past she gets that look in her eyes."
                        l "Something really bad happened, I’m sure of it."
                        c "You might be right."
                        c "Maybe she’ll tell you, eventually."
                    l "Maybe."
                    scene expression eye_blink("images/ep003/ep003_quarters_lilly_smile") with dissolve
                    l "But for now I’m just glad she’s with us."
                    jump ep003_lilly_dialogue
                "About her" if not ep003_lilly_talk:
                    $ ep003_lilly_talk = True
                    c "How are you holding up?"
                    l "Better."
                    scene expression eye_blink("images/ep003/ep003_quarters_lilly_sad") with dissolve
                    l "Though there are times where I feel completely empty."
                    c "Because of Eva?"
                    l "Yes."
                    l "I lie awake sometimes, just thinking back about what happened on Lanan."
                    l "Maybe I could have done something different..."
                    scene expression eye_blink("images/ep003/ep003_quarters_lilly_angry") with dissolve
                    l "I could have tried to fight that sword wielding bitch!"
                    c "That would have been suicide, look what happened to Kit."
                    scene expression eye_blink("images/ep003/ep003_quarters_lilly_sad") with dissolve
                    l "I know, I just feel so helpless."
                    l "We’re going to get her back, aren’t we?"
                    c "That’s the plan."
                    c "Are you still angry with me?"
                    scene expression eye_blink("images/ep003/ep003_quarters_lilly_serious") with dissolve
                    l "No, I don’t think I am..."
                    c "You think..."
                    l "It’s difficult, you know."
                    l "You’ve always tried very hard not to play by the rules."
                    l "Acting before thinking..."
                    l "And I’m just not like that."
                    l "Choosing to desert like that, it closed off a whole lot of options."
                    c "What options?"
                    scene expression eye_blink("images/ep003/ep003_quarters_lilly_doubt") with dissolve
                    l "Letting the Sovereignty deal with it, for example."
                    c "The Sovereignty doesn’t give a shit about a few recruits, their actions made that pretty clear."
                    l "I guess you’re right."
                    l "Maybe you see these things clearer than I do, or maybe I’m just too careful..."

                    menu:
                        "Acknowledge":
                            c "Maybe you are."
                            scene expression eye_blink("images/ep003/ep003_quarters_lilly_serious") with dissolve
                            l "I just don’t want to lose you too."
                        "Reassure her [LillyPath]":
                            $ ep003_lilly_kind = True
                            c "Diving headfirst into things isn’t always the best approach."
                            c "So please, tell me your doubts when I’m about to do something stupid and rash again."
                            scene expression eye_blink("images/ep003/ep003_quarters_lilly_smile") with dissolve
                            l "I will, I don’t want to lose you too."

                    jump ep003_lilly_dialogue
                "About the mission" if not ep003_lilly_talk_mission and ep003_lilly_talk and ep003_lilly_nadya_talk and ep003_aven_talk:
                    $ ep003_lilly_talk_mission = True
                    c "Aven told me you wanted to come hunting on Sagueliath."
                    l "Yes, I want to come with."
                    scene expression eye_blink("images/ep003/ep003_quarters_lilly_serious") with dissolve
                    l "Why do you ask?"

                    menu:
                        "No reason [LillyPath]":
                            c "No reason, just glad to have you along."
                            scene expression eye_blink("images/ep003/ep003_quarters_lilly_smile") with dissolve
                            l "Might as well see the sights while we’re at it."
                            c "I know what you mean."
                            scene expression eye_blink("images/ep003/ep003_quarters_lilly_doubt") with dissolve
                            l "I thought you were going to sleep, by the way."
                            c "I was, but I couldn’t sleep."
                            scene expression eye_blink("images/ep003/ep003_quarters_lilly_serious") with dissolve
                            l "I have trouble falling asleep too, the noises of the ships are still so new to me."
                            c "I hope the Bastard grows on you."
                            l "Very apt name that, she’s really ugly."
                            c "I’m sure insulting the ship you’re on is considered bad luck."
                            l "Luckily we’re not superstitious."
                            c "If you say so..."
                            l "Anyway, I’m going to try and rest, if the ship doesn’t kill me out of spite in the meantime."
                            c "I’ll monitor your life signals from the bridge."
                            scene expression eye_blink("images/ep003/ep003_quarters_lilly_laugh") with dissolve
                            l "Haha, you do that."
                            c "Night, Lilly."
                            l "Good night, [p_name_short]."
                        "Not a good idea":
                            $ ep003_lilly_dismiss = True
                            c "I don’t think it’s a good idea."
                            scene expression eye_blink("images/ep003/ep003_quarters_lilly_angry") with dissolve
                            l "I still don’t understand why you think you’re in charge."
                            l "I’m going, whether you like it or not."
                            c "Well, I don’t."
                            scene expression eye_blink("images/ep003/ep003_quarters_lilly_angry_alt") with vpunch
                            l "I’m sure this whole Captain [p_name_short] shtick is one big power trip for you, but you can just go fuck yourself for all I care!"

                    jump ep003_lilly_dialogue

            jump ep003_conversation_choices

        label ep003_jade_talk:
            $ ep003_jade_talk = True
            scene expression eye_blink("images/ep003/ep003_quarters_jade") with dissolve
            j "Is there something you need, master?"
            c "Yes, maybe..."
            c "Have you made an inventory of the ship’s systems?"
            j "Yes, as soon as we took off from Vulpes Velox."
            c "Good, so do you know if this ship has a VR interface?"
            j "It’s an old bucket, but one of its previous owners did have one installed, yes."
            j "It’s in a separate room in the lower crew quarters."
            c "Thyia didn’t mention it during our tour."
            j "Probably didn’t think it was that important."
            j "It’s an outdated interface, nothing like what’s currently on the market."
            c "But it works."
            j "Yes, it does."
            scene expression eye_blink("images/ep003/ep003_quarters_jade_doubt") with dissolve
            j "Why the sudden interest in virtual reality, master?"
            j "I thought you always preferred physical interaction when it comes to pleasure?"
            c "Those VR interfaces weren’t just intended for porn simulations, you know that?"
            j "Of course master, but that’s what 90%% of those simulators are used for nowadays."
            c "Right..."
            c "Do you have Eva’s digital profile on hand?"
            j "Mistress Eva..."
            j "Yes, I have her profile."
            c "Could you load it so that it’s accessible via the interface?"
            j "Yes, I can."
            j "I’m assuming nobody needs to know about this?"

            menu:
                "Be curt":
                    $ ep003_jade_curt = True
                    c "Correct."
                    c "I need to talk to her."
                    scene expression eye_blink("images/ep003/ep003_quarters_jade_serious") with dissolve
                    j "Understood, master."
                "Be gentle":
                    c "I think it’s better that way."
                    c "I just want to talk to her...{w} to see her again."
                    scene expression eye_blink("images/ep003/ep003_quarters_jade_smile") with dissolve
                    j "I understand."

            j "You do realize it won’t be the same as it is in real life."
            if ep003_jade_curt:
                c "You don’t need to concern yourself with that."
            else:
                c "Yes, I’m aware, but it’s better than nothing."
            j "I’ll set it up for you."
            if ep003_jade_curt:
                c "Good."
            else:
                c "Thank you."
            jump ep003_conversation_choices

        label ep003_aven_talk:
            $ ep003_aven_talk = True
            scene expression eye_blink("images/ep003/ep003_quarters_aven") with dissolve
            av "[p_name_short]."
            c "Hey Aven."
            c "What did you make of Hreir?"
            scene expression eye_blink("images/ep003/ep003_quarters_aven_smile") with dissolve
            av "He’s not the craziest person mother has dealt with."
            av "But he ranks fairly high."
            c "He seemed quite paranoid."
            av "Yeah, he did."
            av "Guess that comes with the job."
            av "His specialization is genetics, but he has an unhealthy interest in clandestine research programs."
            av "Sometimes people just don’t want you poking around in their business."
            c "Would that army of robots protect him?"
            av "Not sure, but if it makes him feel better."
            scene expression eye_blink("images/ep003/ep003_quarters_aven") with dissolve
            if game.is_special:
                av "Mom is staying on the ship once we touch down on Sagueliath."
            else:
                av "Nadya is staying on the ship once we touch down on Sagueliath."
            c "She’s not coming with us?"
            av "I told her not to."
            av "We’ve done these things often enough together, so I know what to do."
            c "So just you and me then?"
            av "Lilly wants to come too."
            c "Lilly?"
            av "Yes."
            av "I told her about the work I’ve done and I guess that got her excited."
            scene expression eye_blink("images/ep003/ep003_quarters_aven_doubt") with dissolve
            av "Why, do you have a problem with it?"

            menu:
                "Yes":
                    $ ep003_aven_lilly_deride = True
                    c "Yes, I’m afraid she’ll slow us down."
                    scene expression eye_blink("images/ep003/ep003_quarters_aven_doubt_alt") with dissolve
                    av "Wow...{w} Errr...{w} Really?"
                    av "You all have the same training, [p_name_short]...{w} I don’t see the problem here."
                "No [LillyPath] [AvenPath]":
                    c "No, of course not."
                    scene expression eye_blink("images/ep003/ep003_quarters_aven_smile") with dissolve
                    c "It’s just that I didn’t think she’d venture into the wild again after what happened on Lanan..."
                    av "Ah, right."
            av "I’m going to get some sleep now, if you don’t mind."
            c "Not at all."
            jump ep003_conversation_choices

label ep003_celine_talk:
    $ ep003_celine_talk = True
    scene ep003_quarters_celine_kit with dissolve
    c "Oh, sorry, I hope I’m not interrupting."
    if celine_rejected or not celine_romance:
        scene ep003_quarters_celine with dissolve
        ce "A little."
    scene ep003_quarters_kit with dissolve
    ki "Not at all, we were just talking about our homicidal parent."
    scene expression eye_blink("images/ep003/ep003_quarters_celine_sad") with dissolve
    ce "Don’t fucking joke about that..."
    c "Right, Calista..."
    ce "I was just saying to Kit that I haven’t really been able to process what happened at that moment."
    ce "Partly because we haven’t had time to catch our breath, really, but on the other hand..."
    scene expression eye_blink("images/ep003/ep003_quarters_kit_serious") with dissolve
    ki "She fucking pushed the button..."
    ki "She was ready to blow us up."
    ki "Or actually, she very nearly did."
    ki "Being the children of a commanding officer never did us any favors, but I didn’t expect her to be that ruthless."
    ki "Coldhearted bitch."
    scene expression eye_blink("images/ep003/ep003_quarters_celine_sad") with dissolve
    ce "Come on Kit, maybe she-"
    scene expression eye_blink("images/ep003/ep003_quarters_kit_angry") with vpunch
    ki "She tried to fucking murder us, Cé!"
    ki "I know what you’re going to say and I don’t fucking care if she was conflicted when she gave the kill order."
    scene expression eye_blink("images/ep003/ep003_quarters_celine_sad") with dissolve
    ce "She’s still our mother."
    ki "Unfortunately..."
    scene expression eye_blink("images/ep003/ep003_quarters_celine_unsure") with dissolve
    ce "Do you think it would be possible to get a message out to her?"
    ki "Why would you want to do that?"
    ce "I really want her to know we’re okay."
    scene expression eye_blink("images/ep003/ep003_quarters_kit_serious") with dissolve
    ki "I honestly don’t know why you’d bother."
    ki "At any rate, she’s as good as dead to me, so I don’t care if she knows."
    scene expression eye_blink("images/ep003/ep003_quarters_celine_unsure") with dissolve
    ce "Do you think it would be possible, [p_name_short]?"

    menu:
        "[gr]Too dangerous":
            c "It’s too dangerous."
            c "They might trace that message back to us, we can’t take that risk."
            scene expression eye_blink("images/ep003/ep003_quarters_celine_sad") with dissolve
            ce "I understand."
        "Maybe":
            $ ep003_celine_message = True
            c "Maybe, but we should be very careful."
            c "We can’t have them tracing that message back to us."
            scene expression eye_blink("images/ep003/ep003_quarters_celine_smile") with dissolve
            ce "Of course."
            ce "I’ll ask Thyia or Jade if they know of a way."
            c "Good idea."
    jump ep003_conversation_choices

label ep003_thyia_talk:
    $ ep003_thyia_talk = True
    scene ep003_quarters_th_tools with dissolve
    c "Does the engine need this much maintenance?"
    th "No, but it doesn’t hurt either."
    th "Just making sure everything runs smoothly."
    scene expression eye_blink("images/ep003/ep003_quarters_th_tools_smile") with dissolve
    th "The Bastard is an old beast, but with a little care she can keep running forever."
    menu:
        "Propose a break [ThyiaPath]":
            c "Why don’t you take a break?"
            scene expression eye_blink("images/ep003/ep003_quarters_th_tools_doubt") with dissolve
            th "I like tinkering, why would I need a break?"
            menu:
                "Be blunt":
                    c "So I can slam you against the bulkhead and fuck you hard, just like on Vulpes."
                    scene expression eye_blink("images/ep003/ep003_quarters_th_tools_angry") with dissolve
                    th "Wow, what a romantic proposal..."
                    th "No thanks."
                    th "And don’t bother asking in the future."
                "Be coy [ThyiaPath]":
                    $ ep003_thyia_coy = True
                    c "I have a feeling that maybe we left a couple of things unexplored back on Vulpes."
                    scene expression eye_blink("images/ep003/ep003_quarters_th_tools_serious") with dissolve
                    th "Right."
                    th "Perhaps I should have been clearer, but that was strictly a one-time deal."
                    c "Oh."
                    th "It’s much cleaner that way."
                    th "Both parties have a good time, feel all relaxed and there are no messy feelings afterwards."
                    c "Right..."
                    scene expression eye_blink("images/ep003/ep003_quarters_th_tools_sad") with dissolve
                    th "Fuck, I’m sorry to disappoint."
                    th "It’s just...{w} I’m not built for long-term relationships, believe me."
                    c "If you say so."
                    scene expression eye_blink("images/ep003/ep003_quarters_th_tools_unease") with dissolve
                    th "..."
                    scene expression eye_blink("images/ep003/ep003_quarters_th_tools_serious") with dissolve
                    th "So, there was this one part of the engine I’d really like to inspect, if you don’t mind."
                    c "Of course, I’ll leave you to it."
        "Leave her to work":
            c "I won’t keep you from tinkering."
            c "Especially if it will benefit us all."
            th "Thanks!"
    jump ep003_conversation_choices

label ep003_dream:
    $ woman_name = "Warrior"
    scene black with fade
    e "[p_name]?"
    scene ep002_e_dream_01 with vpunch
    e "Are you there [p_name]?"
    scene ep002_e_dream_02 with dissolve
    c "Eva?"
    scene ep003_e_dream_01 with dissolve
    c "Eva?!"
    c "I thought you were gone?"
    e "I’m not, [p_name_short]."
    e "I’m right here."
    scene ep003_e_dream_02 with dissolve
    e "Come with me, I want to show you something."
    c "Wh-"
    scene ep003_e_dream_03 with dissolve
    e "Look, over there!"
    e "Just a little further."
    c "Eva! Look out!"
    scene ep003_e_dream_04 with vpunch
    image side woman_portrait = "gui/side-images/side_warrior_woman.webp"
    woman "Don’t try anything stupid."
    c "Eva!"
    c "No!"
    scene ep003_e_dream_05 with dissolve
    woman "I’ll take my leave now."
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
