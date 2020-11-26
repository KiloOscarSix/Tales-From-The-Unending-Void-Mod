
image ep002_celine_fuck_alt_closeup = Movie(play="movies/ep002/ep002_celine_fuck_alt_closeup.webm")
image ep002_celine_fucking = Movie(play="movies/ep002/ep002_celine_fuck_alt.webm")
image ep002_jade_fuck_reverse_closeup = Movie(play="movies/ep002/ep002_jade_fuck_reverse.webm")

label ep002_conversations:

    if 'ep002_conversations_init' not in locals():
        $ ep002_conversations_init = True

        $ ep002_vess_reassure = False
        $ ep002_vess_talk = False
        $ ep002_kit_talk = False
        $ ep002_kit_weelchair_talk = False
        $ ep002_jade_talk = False
        $ ep002_lilly_talk = False
        $ ep002_celine_talk = False
        $ ep002_thim_talk = False
        $ ep002_nadya_talk = False
        $ ep002_aven_talk = False
        $ ep002_thyia_talk = False
        $ ep002_kit_dismissed = False
        $ ep002_lilly_respect = False
        $ ep002_thyia_apology = False
        $ ep002_thyia_angry = False
        $ ep002_celine_sex = False
        $ ep002_celine_creampie = False
        $ ep002_celine_love = False
        $ ep002_thim_admonish = False
        $ ep002_nadya_dismissed = False
        $ ep002_aven_settling = False
        $ ep002_aven_past = False
        $ ep002_jade_empathize = False
        $ ep002_jade_sex = False
        $ ep002_jade_creampie = False
        $ ep002_celine_fucked = False

    play music [ "music/space-harmony.ogg", "music/searching-the-cosmos.ogg" ] fadeout 4 fadein 1.0

    label ep002_conversation_choices:
        $ choices = [
                {
                    'name': 'Vess',
                    'action': 'ep002_vess_talk',
                    'visible': True if not ep002_vess_talk else False
                },
                {
                    'name': 'Kit',
                    'action': 'ep002_kit_talk',
                    'visible': True if not ep002_kit_weelchair_talk or (ep002_cargo_completed and not ep002_kit_talk) else False
                },
                {
                    'name': 'Lilly',
                    'action': 'ep002_lilly_talk',
                    'visible':  True if not ep002_lilly_talk and ((ep002_cargo and ep002_university_completed) or ep002_cargo_completed) else False
                },
                {
                    'name': 'Jade',
                    'action': 'ep002_jade_talk',
                    'visible':  True if not ep002_jade_talk else False
                },
                {
                    'name': 'Céline',
                    'action': 'ep002_celine_talk',
                    'visible':  True if not ep002_celine_talk else False
                },
                {
                    'name': 'Thim',
                    'action': 'ep002_thim_talk',
                    'visible':  True if not ep002_thim_talk  else False
                },
                {
                    'name': 'Nadya',
                    'action': 'ep002_nadya_talk',
                    'visible':  True if not ep002_nadya_talk and ep002_university_completed else False
                },
                {
                    'name': 'Aven',
                    'action': 'ep002_aven_talk',
                    'visible':  True if not ep002_aven_talk and ep002_university_completed else False
                },
                {
                    'name': 'Thyia',
                    'action': 'ep002_thyia_talk',
                    'visible':  True if not ep002_thyia_talk and ep002_university and ep002_cargo_completed else False
                }
            ]

        scene black with fade
        $ conversation_menu(choices)

        if ep002_celine_sex and not ep002_celine_fucked:
            call ep002_celine_sex from _call_ep002_celine_sex
            call ep002_dream from _call_ep002_dream
            ce "[p_name_short]?!"
            scene ep002_celine_fuck_post_scared with vpunch
            ce "[p_name_short]? Are you all right?"
            c "Sorry...{w} It’s...{w} It was just a bad dream."
            c "Let's go back to sleep."
        elif not ep002_jade_talk:
            "I was completely exhausted, so I went to bed as soon as I was back in my quarters again."
            call ep002_dream from _call_ep002_dream_1
            "The dream marked the beginning of a very restless night."
        scene black with fade
        return

    label ep002_vess_talk:
        $ ep002_vess_talk = True
        scene expression eye_blink("images/ep002/ep002_quarters_vess") with dissolve
        c "Hey, how are you settling in?"
        ve "Just fine, everybody is very nice to me."
        c "Thim isn't bothering you?"
        ve "Not at all."
        ve "He seems like a very private person."
        c "I think so, we don't see eye to eye, so I'm not an expert on things related to Thim."
        ve "He's not the only one who's a little buttoned up."
        scene expression eye_blink("images/ep002/ep002_quarters_vess_unsure") with dissolve
        ve "I mean, the others are friendly, but..."
        c "I'm sure that will change."
        c "You're new here and everybody has been through hell lately."
        menu:
            "You can confide in me [VessPath]":
                $ ep002_vess_reassure = True
                c "If you need someone to speak to, I'll be there for you."
                scene expression eye_blink("images/ep002/ep002_quarters_vess_smile") with dissolve
                ve "Thank you, that means a lot."
            "Say nothing":
                c "It's going to be fine."
                ve "Thanks, I guess that's reassuring."
        jump ep002_conversation_choices

    label ep002_kit_talk:
        scene expression eye_blink("images/ep002/ep002_quarters_kit") with dissolve

        menu ep002_kit_dialogue:
            "Talk about wheelchair" if not ep002_kit_weelchair_talk:
                $ ep002_kit_weelchair_talk = True
                ki "Can't wait to be useful again, sitting in this chair sure sucks."
                c "I'm sure your excellent physique will help you stand upright in no time."
                ki "Let's hope so, I hate being pushed around."
                ki "Or peeing in a jar, for that matter."
                c "You like to add those little details, don't you?"
                ki "I thought you'd enjoy them."
                c "Enormously..."
                jump ep002_kit_dialogue
            "Talk about Pit of Despair" if not ep002_kit_talk and ep002_cargo_completed:
                $ ep002_kit_talk = True
                scene expression eye_blink("images/ep002/ep002_quarters_kit_serious") with dissolve
                if ep002_pit_thim:
                    ki "You let Thim take the fall for that mess with the R'o?"
                    c "I had to make a decision."
                    ki "I know, but...{w} I don't know..."
                    c "Just say what you want to say Kit, we've known each other long enough."
                    ki "It seems a little cold, throwing him to the wolves like that."
                    ki "I know you two don't like each other..."
                    c "It wasn't personal."
                    ki "If you say so."
                    ki "I'm not sure if you're seeing it that way, but you're sort of becoming our captain."
                    ki "And a captain has certain responsibilities, if you know what I mean."

                    menu:
                        "Agree [KitPath]":
                            c "I get what you're saying..."
                            c "It's just, I never asked to be captain, let alone all those new responsibilities."
                            c "But I made a choice for all of us, so maybe I should accept those responsibilities."
                            c "Fuck. Now I feel bad for Thim."
                            scene expression eye_blink("images/ep002/ep002_quarters_kit_smile") with dissolve
                            ki "Don't worry, we all make mistakes."
                            ki "I'm sure that captainship is something you'll grow into."
                            ki "But we sure as shit aren't at the academy anymore."
                            c "You can say that again..."
                        "Disagree":
                            $ ep002_kit_dismissed = True
                            c "I never asked to be captain and maybe this is just my style of leadership."
                            ki "Okay, I guess we have a different take on it then."
                            c "Guess so."
                            c "No hard feelings?"
                            ki "Nah, you know I'll support you through and through!"
                else:
                    ki "That Pit of Despair, how horrible was it?"
                    c "Not a lot of despair, to be honest."
                    ki "No?"
                    c "A cave full of horny R'o women isn't reason for despair, in my book."
                    scene expression eye_blink("images/ep002/ep002_quarters_kit_smile") with dissolve
                    ki "Horny R'o women...{w} Attractive women?"
                    c "Very!"
                    ki "Did you..."

                    if ep002_ro_orgy:
                        c "You have to ask me that? I never fucked as many women in a single night in my entire life!"
                        scene expression eye_blink("images/ep002/ep002_quarters_kit_big_smile") with dissolve
                        ki "Fuck, now I'm really jealous. Couldn't we do another cargo run for the R'o?!"
                        if ep002_ro_help:
                            c "Hehe, I think we'd be out of luck."
                            c "I helped one of the women escape to warn another tribe."
                            c "So those caves might just be empty when we get there another time."
                            scene expression eye_blink("images/ep002/ep002_quarters_kit_serious") with dissolve
                            ki "Bummer."
                        else:
                            c "Hehe, we'll ask Thyia when we meet her again."
                            ki "Good, because I'm ready to sin, big time!"
                    else:
                        c "No, it didn't feel right"
                        scene expression eye_blink("images/ep002/ep002_quarters_kit_serious") with dissolve
                        ki "Wow, I admire that self-restraint."

                        if ep002_ro_help:
                            c "I just hope those caves will be empty very soon. I helped one of the women escape to get help."
                            scene expression eye_blink("images/ep002/ep002_quarters_kit_smile") with dissolve
                            ki "That’s really decent of you, hope it works out for them."

                jump ep002_kit_dialogue
        jump ep002_conversation_choices

    label ep002_lilly_talk:
        $ ep002_lilly_talk = True
        scene expression eye_blink("images/ep002/ep002_quarters_lilly") with dissolve
        if game.is_special:
            c "Hey little sis."
        else:
            c "Hey Lilly."
        l "Hey."
        c "About everything that happened..."
        scene expression eye_blink("images/ep002/ep002_quarters_lilly_sad") with dissolve
        l "Sorry [p_name_short], I already told you, I just can't, not now."
        l "Maybe we can talk later, but could you just leave me be."

        menu:
            "No":
                c "No, I really want to talk about it now."
                scene expression eye_blink("images/ep002/ep002_quarters_lilly_angry") with vpunch
                l "Fuck you, you always think about yourself."
                l "Just leave."
            "Of course [LillyPath]":
                $ ep002_lilly_respect = True
                c "Of course."
        jump ep002_conversation_choices

    label ep002_jade_talk:
        $ ep002_jade_talk = True
        scene expression eye_blink("images/ep002/ep002_quarters_jade") with dissolve
        j "So how's my captain doing?"
        c "I'm not a captain!"
        j "Are you sure, master?"
        j "You've seen the looks everyone gives you when it's time to set a course or plan some action, don't you?"
        c "Not really..."
        j "I have and I think all of them are looking at you as some kind of leader."
        j "Even Thim."
        c "Shit. I didn't ask for this."
        scene expression eye_blink("images/ep002/ep002_quarters_jade_smile") with dissolve
        j "There are many things we never ask for in life and they still happen."

        menu:
            "Sorry [JadeLovePath]":
                $ ep002_jade_empathize = True
                c "Shit, I didn't mean to be insensitive."
                j "Oh, you mean because of my past?"
                j "If I'd still dwelt on the cards I've been dealt in life, I'd be a very bitter Tw'ill indeed."
                j "So don't worry about that, master."
            "Agree [JadeSubPath]":
                c "I guess you're right..."
        scene expression eye_blink("images/ep002/ep002_quarters_jade_smile_sexy") with dissolve
        j "Maybe we should celebrate your new captainship?"
        j "I could get naked..."

        menu:
            "Have sex":
                $ ep002_jade_sex = True
                c "That's always a great idea."
                j "I know, right?"
                j "Especially when you do it too and then have a long...{w} hard...{w} fuck..."
                call ep002_jade_sex from _call_ep002_jade_sex
                if not celine_romance:
                    call ep002_dream from _call_ep002_dream_2
                    j "Master [p_name]?!"
                    scene ep002_jade_fuck_post_scared with vpunch
                    j "Are you all right?"
                    c "Sorry...{w} It’s...{w} It was just a bad dream."
                    j "Do you need anything?"
                    c "No, just go back to sleep, it's nothing to worry about."
            "Turn her down":
                c "Tempting, but I'm not really in a festive mood."
                scene ep002_quarters_jade with dissolve
                j "No problem master, I'll just go to sleep then."
        jump ep002_conversation_choices

    label ep002_celine_talk:
        $ ep002_celine_talk = True
        scene expression eye_blink("images/ep002/ep002_quarters_celine") with dissolve
        c "What do you think of the ship?"
        ce "She takes a little getting used to, but she flies!"
        c "That she does."
        c "Funny though, how everyone slowly seems to slide into a role here."
        ce "What do you mean?"
        c "Well, ever since you sat in that pilot's chair on the Enfield, everyone thinks you can fly any ship."
        ce "Yes, that's not entirely true though..."
        ce "I'm still figuring out the Bastard's systems."
        c "Seems to me you're doing a good job so far."
        scene expression eye_blink("images/ep002/ep002_quarters_celine_smile") with dissolve
        ce "We seem to be arriving at the right locations, but there's still a lot to learn."
        c "Let me know if you need anything."
        ce "I will!"

        if celine_romance:
            scene expression eye_blink("images/ep002/ep002_quarters_celine_sexy") with dissolve
            ce "Oh and [p_name_short]..."
            ce "You have private quarters, right?"
            c "More or less, Jade sleeps in my quarters too."
            scene expression eye_blink("images/ep002/ep002_quarters_celine") with dissolve
            ce "Oh..."

            menu:
                "Invite her [CelinePath]":
                    $ ep002_celine_sex = True
                    c "But she doesn't mind sleeping somewhere else."
                    scene expression eye_blink("images/ep002/ep002_quarters_celine_sexy") with dissolve
                    ce "Great!"
                    ce "I mean, good."
                    ce "Would you like me to spend the night with you?"
                    c "I'll leave my door open."
                    ce "That sounds like a fantastic idea..."
                "Don't invite her":
                    c "So getting together is a little difficult right now."
                    c "Maybe when we're planet-side again, or at a station."
                    ce "Okay...{w} Maybe..."
                    "In truth I was completely exhausted and didn't want to deal with her, so I went to bed as soon as she left."
                    call ep002_dream from _call_ep002_dream_3
                    scene ep002_quarters_camran_scared with vpunch
                    c "Eva..."
                    c "Fuck."
        jump ep002_conversation_choices

    label ep002_thim_talk:
        $ ep002_thim_talk = True

        if not ep002_pit_thim and (ep001_thim_talk or ep001_medbay_thim_talk):
            scene expression eye_blink("images/ep002/ep002_quarters_thim") with dissolve
            c "Are these quarters okay?"
            t "I guess so."
            c "You’re sharing this room with Vess, right?"
            t "Yes, she seems like a nice girl."
            t "Quiet."
            t "And don’t worry, I’ll give her privacy if she needs it."

            menu:
                "Wasn't worried [ThimPath]":
                    c "I wasn’t worried about that."
                    scene expression eye_blink("images/ep002/ep002_quarters_thim_smile") with dissolve
                    t "Oh..."
                    t "Did you need anything else?"
                    c "Nope, just checking in."
                    scene expression eye_blink("images/ep002/ep002_quarters_thim") with dissolve
                    t "Your slave hit me pretty good, by the way."
                    c "Jade is not my slave."
                    t "Attendant...{w} whatever."
                    c "Do you require more medical attention?"
                    t "No, I’m fine."
                    c "You know, I never saw your attendant."
                    scene expression eye_blink("images/ep002/ep002_quarters_thim_smile") with dissolve
                    t "Never had one."
                    c "You didn’t, I thought all the rich kids got one eventually?"
                    t "I made it clear to my parents I didn’t care for slaves."
                    c "That’s decent of you."
                    scene expression eye_blink("images/ep002/ep002_quarters_thim_unsure") with dissolve
                    t "Is it?"
                    t "Didn’t make any difference."
                    t "My older brother got her as his second attendant and treated her like shit."
                    c "That’s harsh."
                    scene expression eye_blink("images/ep002/ep002_quarters_thim") with dissolve
                    t "Yeah...{w} well..."
                "You'd better":
                    $ ep002_thim_admonish = True
                    c "You’d better..."
                    scene expression eye_blink("images/ep002/ep002_quarters_thim_angry") with dissolve
                    t "Fuck you, what do you take me for?"
                    c "Never mind."
        elif ep002_pit_thim:
            scene ep002_quarters_thim_angry with vpunch
            t "Don't you fucking dare enter these quarters."
            t "Go the fuck away."
        else:
            scene expression eye_blink("images/ep002/ep002_quarters_thim") with dissolve
            t "Why are you here?"
            c "Just checking in."
            t "Well, I’m fine."
            t "You can leave now."
            c "Suit yourself."
        jump ep002_conversation_choices

    label ep002_nadya_talk:
        $ ep002_nadya_talk = True
        scene expression eye_blink("images/ep002/ep002_quarters_nadya") with dissolve
        na "Hi [p_name]."
        c "Hi aunt Nadya, just checking to see if you're okay."
        na "It's an old ship, but not the worst vessel I've travelled on."
        c "Maybe we can improve some things on the Bastard as soon as we have the funds."
        na "That would be nice."
        c "I wanted you to know that I'm really glad you and Aven came with us."
        c "I really didn't expect that."
        scene expression eye_blink("images/ep002/ep002_quarters_nadya_smile") with dissolve
        na "What else could I do when you told me that terrible news about Eva?"
        if game.is_special:
            na "After all these years, my love for you and your sisters hasn't diminished."
        else:
            na "After all these years, my love for you and your friends hasn't diminished."
        if ep002_cargo_completed:
            na "I can't wait to speak to Lilly some more."
            c "I think she'd be happy to."
        else:
            na "I can't wait to see Lilly again."
            c "I think she'll be very happy to see you too."
        na "When we're together, we should talk some more about the past, relive a couple of those happy memories."
        menu:
            "I'd like that [NadyaPath]":
                c "I'd like that."
                na "Good!"
            "I'd rather not":
                $ ep002_nadya_dismissed = True
                c "The past is the past, I always say."
                scene expression eye_blink("images/ep002/ep002_quarters_nadya") with dissolve
                na "Oh...{w} I guess that's a valid point of view too..."
        jump ep002_conversation_choices


    label ep002_aven_talk:
        $ ep002_aven_talk = True
        scene expression eye_blink("images/ep002/ep002_quarters_aven") with dissolve

        menu ep002_aven_dialogue:
            "Settling in" if not ep002_aven_settling:
                $ ep002_aven_settling = True
                c "Are you okay here in these quarters?"
                av "I'll manage."
                av "I've slept under worse conditions."
                if game.is_special:
                    c "On those expeditions with aunt Nadya?"
                else:
                    c "On those expeditions with Nadya?"
                av "Yup."
                av "There's never enough funding from the University, so we mostly had to make ends meet."
                c "Ever been in dangerous situations?"
                scene expression eye_blink("images/ep002/ep002_quarters_aven_smile") with dissolve
                av "Plenty!"
                if game.is_special:
                    av "Mom has successfully contacted several hostile races and profiled them."
                else:
                    av "Nadya has successfully contacted several hostile races and profiled them."
                av "The initial contact is always a little scary, but so is staying among an alien race you know would eat you for breakfast normally."
                c "My guess is that in those cases your combat skills aren't any good."
                scene expression eye_blink("images/ep002/ep002_quarters_aven") with dissolve
                av "Hah, no."
                av "Bluffing, lying and sweet-talking are better tools when it comes to that."

                menu:
                    "Be nice":
                        c "I'm glad you came with us."
                        scene expression eye_blink("images/ep002/ep002_quarters_aven_smile") with dissolve
                        av "I'd never leave mom alone."
                    "Say nothing":
                        "I just looked at her, trying to determine if she was acting all tough or if she was being genuine."
                jump ep002_aven_dialogue
            "About the past [AvenPath]" if not ep002_aven_past:
                $ ep002_aven_past = True
                c "I don't remember much about our time together on Tuolovi."
                av "I remember some things."
                scene expression eye_blink("images/ep002/ep002_quarters_aven_smile") with dissolve
                av "We played a lot together."
                av "There was this one time where we'd hidden Lilly and Eva's favorite toys."
                av "They were absolutely furious, especially when we made them do a scavenger hunt in order for them to find their toys."
                c "Ha! I remember that."
                c "The fury on Lilly's face."
                scene expression eye_blink("images/ep002/ep002_quarters_aven_smile_alt") with dissolve
                av "Yeah, that made it all worth it."
                c "So we played together much?"
                av "We did, but I was close with Lilly and Eva too, just liked to mess with them from time to time."
                c "Do you know why it went all wrong?"
                scene expression eye_blink("images/ep002/ep002_quarters_aven") with dissolve
                if game.is_special:
                    av "No...{w} Mom never talks about it."
                else:
                    av "No...{w} Nadya never talks about it."
                av "I'm pretty sure it's something between her and your mom and dad."
                if game.is_special:
                    av "She obviously still loves you and your sisters."
                else:
                    av "She obviously still loves us."
                av "That look on her face, when she saw you first back on Ryūjin Prime, never seen her so happy."
                c "Yeah, I noticed."
                c "Glad she doesn't hate me."
                scene expression eye_blink("images/ep002/ep002_quarters_aven_smile") with dissolve
                av "Why would she?"
                if game.is_special:
                    av "You were always her favorite nephew."
                else:
                    av "You were always her favorite."
                scene expression eye_blink("images/ep002/ep002_quarters_aven") with dissolve
                if game.is_special:
                    av "If there's anybody she hates, it's her brother, or should I say uncle Agust..."
                else:
                    av "If there's anybody she hates, your father, or should I say uncle Agust..."
                c "It doesn't take a lot of effort to hate him."
                av "Well, mom was very close to him once, or so she told me."
                if game.is_special:
                    c "You don't get to choose your brothers and sisters."
                    av "True, but you can also just ignore them, that wasn't the case with Agust and mom."
                c "Maybe he changed for the worse over time."
                av "Could be."
                jump ep002_aven_dialogue
        jump ep002_conversation_choices

    label ep002_thyia_talk:
        $ ep002_thyia_talk = True
        scene expression eye_blink("images/ep002/ep002_quarters_thyia") with dissolve
        th "What is it?"
        c "You're still angry with me?"
        th "I sure as shit am."
        if game.is_special:
            th "You went to Ryūjin Prime for a family reunion?!"
            c "We need my aunt's knowledge if we are to save my sister Eva."
        else:
            th "You went to Ryūjin Prime to hook up with some old pals?!"
            c "We need Nadya's knowledge if we are to save Eva."
        c "So yes, I went to the university on Ryūjin Prime first."
        th "Are you always this selfish and untrustworthy?"

        menu:
            "Apologize [ThyiaPath]":
                $ ep002_thyia_apology = True
                c "If I'd known beforehand everything would turn into a world of shit for you, I'd have done that cargo run first."
                if game.is_special:
                    c "I just want my sister back so badly that everything else seems unimportant..."
                else:
                    c "I just want my friend back so badly that everything else seems unimportant..."
                c "I'm sorry for that."
                scene expression eye_blink("images/ep002/ep002_quarters_thyia_smile") with dissolve
                th "Thank you."
                if game.is_special:
                    th "And I get it about your sister, I'm sure you'll get her back."
                else:
                    th "And I get it about your friend, I'm sure you'll get her back."
                c "I wish I had your confidence."
            "Don't apologize":
                c "I did what I had to do, I'm not going to apologize for it."
                th "Of course you aren't."
                c "You're free to leave at any port we dock."
                th "I know..."
            "Get angry":
                $ ep002_thyia_angry = True
                c "I did what I had to do."
                if game.is_special:
                    c "I want my fucking sister back and I really don't need people like you judging me."
                else:
                    c "I want my fucking friend back and I really don't need people like you judging me."
                c "I'm trying the fucking best I can, all right?!"
                "Possibly shocked by my outburst, Thyia didn't say anything further and I left her in her quarters."
        jump ep002_conversation_choices

label ep002_celine_sex:
    $ ep002_celine_fucked = True
    scene ep002_door with dissolve
    "I waited for Céline, a little nervous and watching the door all the while."
    scene expression eye_blink("images/ep002/ep002_celine_door") with dissolve
    "Finally she came, clad in just her underwear."
    ce "Hey."
    c "Hey."
    scene ep002_celine_door_kiss with dissolve
    "We didn't need much words and just kissed instead, with growing intensity."
    "Her hands were everywhere, mine were also all over her body."
    scene ep002_celine_naked with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "At last we were naked and I took in the beauty of her body, from her small breasts to her beautifully shaped thighs and that perfect butt."
    "Céline just smiled and eyed my growing cock."
    scene ep002_celine_lap with dissolve
    "As she sat on my lap, her pussy grinding on my leg, she grabbed my dick and began to jerk me off."
    "I buried my face in her breasts and licked them with lustful intensity."
    scene ep002_celine_penetrate with dissolve
    "Kissing her neck and earlobe, her grip on my cock slackened and she just sighed with pleasure, a sound so erotic I nearly painted her belly with my seed."
    "Carefully, I lifted her body and lowered her on my cock."
    "I'd felt her wetness on my leg already, but was still amazed with the ease I was able to penetrate her, aided by her moisture."
    scene ep002_celine_fuck with dissolve
    "She embraced me tightly and whispered hoarsely in my ear."
    ce "Fuck me, [p_name_short]!"
    "Holding her slender waist, I guided Céline up and down my cock."
    "She'd buried her face in my neck and moaned softly in my ear."
    scene ep002_celine_fuck_alt with dissolve
    "The smell of her sweat and sex fueled my desire for her even more and she helped me reach new heights of pleasure by moving her hips on the pulse of our fucking."
    show ep002_celine_fucking with dissolve
    "As she shifted her weight I nearly went through the roof, having found new reserves of bliss inside her pussy."
    ce "Oh [p_name_short], [p_name_short], yes!"
    show ep002_celine_fuck_alt_closeup with dissolve
    "Every thrust brought me closer to climax, until it was there as sudden as it ever was."

    menu:
        "Creampie [gr]\[Celine Creampie\]":
            $ ep002_celine_creampie = True
            scene ep002_celine_fuck_creampie with vpunch
            "Céline's body had just slammed down and my cock was deep inside her as my seed flooded her vagina."
            scene ep002_celine_fuck_creampie_alt with flash
            with flash
            "She embraced me tightly as the last drops of cum entered her body, showering my face and neck with kisses."
        "Body":
            "With a lot of effort I was able to pull out of her."
            scene ep002_celine_fuck_body with flash
            with flash
            "My cock showered her butt with cum as she embraced me tightly, covering my face and neck with kisses."
    ce "I love you [p_name_short]!"

    $ renpy.end_replay()
    scene expression eye_blink("images/ep002/ep002_celine_fuck_post") with dissolve

    menu:
        "Love you too [CelinePath]":
            $ ep002_celine_love = True
            c "I love you too, Céline!"
            "Incapable of saying anything else, I pulled her on the bed and hugged her firmly."
        "Stay silent":
            "Incapable of answering I pulled her on the bed and hugged her firmly."
    "We fell asleep not long afterwards."
    scene black with fade
    return

label ep002_jade_sex:
    scene ep002_jade_topless with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "She undid her top, revealing her supple breasts and using her poise to great effect by accentuating the curves of her body."
    "I'm not sure how it works, but her body language always did a number on me."
    "For some reason, it made Jade an even more sensual being than she already was."
    scene ep002_jade_undress with dissolve
    "My Tw'ill girl proceeded to undress me, her cool fingers caressing my skin wherever she uncovered it."
    "I shivered."
    scene ep002_jade_naked with dissolve
    "Grinning she slipped out of her remaining clothes and sat on top of me, her powerful thighs straddling my body."
    "I felt her pussy on my bare skin as she rubbed herself, longing for pleasure."
    "My erection was growing fast and finally pushed against her buttocks."
    scene ep002_jade_penetrate with dissolve
    "Satisfied, she took my member and slid it inside her pussy."
    "The sigh of pleasure and delighted expression on her face were absolutely genuine and I loved her for it."
    scene ep002_jade_fuck with dissolve
    "I had one hand on her ass and another greedily reaching for one of her breasts as she started to bounce on my cock."
    "Jade's pussy always felt tight, as if I'd entered her for the first time and took her maidenhood."
    j "Gods, master, your cock feels so good!"
    scene ep002_jade_fuck_alt with dissolve
    "My girl massaged the nipple of one of her breasts, while I took care of the other one."
    "All the while her pussy was slapping down on my hard dick, probing her very depths."
    scene ep002_jade_fuck_closeup with dissolve
    j "Do you like my ass, master?"
    j "Do you want to see more of it?"
    scene ep002_jade_fuck_reverse with dissolve
    "Not waiting for my answer, she pulled my cock out and reversed her position."
    "Her firm ass was glorious, especially when it danced on the cadence of our motions."
    show ep002_jade_fuck_reverse_closeup with dissolve
    "The reversed position also had the benefit of stimulating my cock in entirely new ways."
    scene ep002_jade_fuck_reverse_alt with dissolve
    "Jade felt it too and started to finger herself, while I reached around and cupped her breasts."
    "I couldn't hold out any longer, her pussy was too good."

    menu:
        "Creampie [gr]\[Jade Creampie\]":
            $ ep002_jade_creampie = True
            scene ep002_jade_fuck_creampie with vpunch
            "Deep inside of her I unloaded, my seed splashing against the entrance of her womb."
            scene ep002_jade_fuck_creampie_alt with flash
            with flash
            "Jade quivered with pleasure as she slid from my cock to lay next to me, cum leaking out of her on the bed."
        "Body":
            "As I felt the release of my seed approaching, I lifted Jade from my cock and threw her on the bed."
            scene ep002_jade_fuck_body with flash
            with flash
            "She spread her legs and allowed me to splatter her body with thick splashes of cum."
        "Facial":
            "As I felt the release of my seed approaching I lifted Jade from my cock and pulled her head close to my cock."
            scene ep002_jade_fuck_facial with vpunch
            "She took the hint and started sucking the cum from my dick."
            scene ep002_jade_fuck_facial_alt with flash
            with flash
            "Quivering, I unloaded thick splashes of seed on her grinning face."

    if is_patreon() and renpy.has_label("extra_scene_02"):
        call extra_scene_02 from _call_extra_scene_02

    $ renpy.end_replay()

    scene ep002_jade_fuck_post with dissolve
    if celine_romance:
        "I pulled her close and together we happily lay next to each other until Jade slipped out of our embrace to go to her own quarters."
    else:
        "I pulled her close and together we happily fell asleep."
    scene black with fade
    return

label ep002_dream:
    scene black with fade
    e "[p_name]?"
    scene ep002_e_dream_01 with vpunch
    e "Are you there [p_name]?"
    scene ep002_e_dream_02 with dissolve
    c "Eva?"
    scene ep002_e_dream_03 with vpunch
    c "Eva?!"
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
