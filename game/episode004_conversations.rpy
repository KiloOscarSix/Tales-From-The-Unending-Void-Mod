label ep004_conversations:

    if 'ep004_conversations_init' not in locals():
        $ ep004_conversations_init = True

        $ ep004_lilly_talk = False
        $ ep004_lilly_raene_talk = False
        $ ep004_lilly_vess_talk = False
        $ ep004_kit_talk = False
        $ ep004_nadya_talk = False
        $ ep004_n_tuolovi = False
        $ ep004_n_sovereignty = False
        $ ep004_n_university = False
        $ ep004_aven_talk = False
        $ ep004_aven_encounter = False
        $ ep004_aven_dismiss = False
        $ ep004_aven_kepler_talk = False
        $ ep004_celine_talk = False
        $ ep004_thyia_talk = False
        $ ep004_th_l_drinks = False
        $ ep004_eva_talk = False
        $ ep004_jade_talk = False
        $ ep004_ziv_talk = False
        $ ep004_ziv_rhenkoy = False
        $ ep004_ziv_luzane = False
        $ ep004_ziv_skarak = False
        $ ep004_ziv_force = False
        $ ep004_ziv_impolite = False
        $ ep004_ziv_no_romance = False
        $ ep004_ziv_ra_talk = False
        $ ep004_raene_talk = False
        $ ep004_ziv_ra_injection = False
        $ ep004_ra_confront = False
        $ ep004_ra_confront_angry = False
        $ ep004_ra_kind = False
        $ ep004_ra_doubt = False
        $ ep004_ra_angry = False
        $ ep004_jade_dom = False
        $ ep004_jade_sex = False
        $ ep004_jade_dismissed = False
        $ ep004_jade_sex_hard = False
        $ ep004_jade_sex_soft = False
        $ ep004_jade_apologize = False

    play music [ "music/searching-the-cosmos.ogg", "music/the-restoration.ogg", "music/space-harmony.ogg" ] fadeout 4 fadein 1.0

    label ep004_conversation_choices:
        $ choices = [
                {
                    'name': 'Lilly',
                    'action': 'ep004_lilly_talk',
                    'visible': True if not ep004_lilly_talk and ep004_skarak else False
                },
                {
                    'name': 'Kit',
                    'action': 'ep004_kit_talk',
                    'visible': True if not ep004_kit_talk and ep004_aven_talk and ep004_nadya_talk else False
                },
                {
                    'name': 'Nadya',
                    'action': 'ep004_nadya_talk',
                    'visible': True if not ep004_nadya_talk else False
                },
                {
                    'name': 'Aven',
                    'action': 'ep004_aven_talk',
                    'visible': True if not ep004_aven_talk and ep004_skarak else False
                },
                {
                    'name': 'Céline',
                    'action': 'ep004_celine_talk',
                    'visible': True if not ep004_celine_talk and celine_romance else False
                },
                {
                    'name': 'Thyia',
                    'action': 'ep004_thyia_talk',
                    'visible': True if not ep004_thyia_talk and ep004_lilly_talk else False
                },
                {
                    'name': 'Eva',
                    'action': 'ep004_eva_talk',
                    'visible': True if not ep004_eva_talk and ep004_skarak else False
                },
                {
                    'name': 'Jade',
                    'action': 'ep004_jade_talk',
                    'visible': True if not ep004_jade_talk and ep004_eva_talk and ep004_skarak else False
                },
                {
                    'name': 'Raene',
                    'action': 'ep004_raene_talk',
                    'visible': True if not ep004_raene_talk and ep004_skarak else False
                },
                {
                    'name': 'Ziv',
                    'action': 'ep004_ziv_talk',
                    'visible': True if not ep004_ziv_talk and not ep004_ziv_derisive and ep004_raene_talk and ep004_skarak else False
                }
            ]

        scene black with fade
        $ conversation_menu(choices)
        scene black with fade
        return

        label ep004_lilly_talk:
            $ ep004_lilly_talk = True

            scene expression eye_blink("images/ep004/ep004_quarters_lilly") with dissolve
            if game.is_special:
                c "Hey sis."
            else:
                c "Hey Lilly."

            if ep003_lilly_dismiss and (ep003_l_admonish or not ep002_lilly_understanding):
                l "Hey."
                l "Could you please leave me to eat on my own?"
                c "Sure."
            else:
                c "Enjoying the wondrous food from our kitchen?"
                scene expression eye_blink("images/ep004/ep004_quarters_lilly_unsure") with dissolve
                l "It’s certainly wondrous, but not sure if it’s tasty though..."
                c "Still, it beats Kit’s cooking, that’s for sure."
                scene expression eye_blink("images/ep004/ep004_quarters_lilly_smile") with dissolve
                l "Haha, remember that stew he made for us back at the Academy?"
                c "Really, that was a stew?"
                l "Maybe one of the new crew members is an excellent cook?"
                c "We should ask."
                c "What do you think of them, by the way, the new ones?"

                menu ep004_lilly_choices:
                    "About Raene" if not ep004_lilly_raene_talk:
                        $ ep004_lilly_raene_talk = True
                        c "I think I saw you talking to Raene earlier."
                        scene expression eye_blink("images/ep004/ep004_quarters_lilly_unsure") with dissolve
                        l "That girl is very strange."
                        c "Really?"
                        c "She’s very silent and shy, but strange?"
                        l "I tried to talk to her over lunch, but every conversation just stops after a couple of words."
                        c "I’m sure it’s just nerves or something."
                        c "What else could it be?"
                        l "I don’t know."
                        scene expression eye_blink("images/ep004/ep004_quarters_lilly_serious") with dissolve
                        l "She came here on her own volition, right?"
                        l "Ziv isn’t some slaver who’s using us to transport her wares?"
                        c "No, she isn’t."
                        c "Another woman brought Raene back on Verdigris and Raene went with Ziv willingly."
                        c "I think she’s escaping from her father."
                        scene expression eye_blink("images/ep004/ep004_quarters_lilly_smile") with dissolve
                        l "Well, maybe she’ll come around."
                        c "She just might, but I’ll make a note to talk to her, get to know her a little."
                        jump ep004_lilly_choices
                    "About Vess" if not ep004_lilly_vess_talk:
                        $ ep004_lilly_vess_talk = True
                        c "How are you getting on with Vess?"
                        scene expression eye_blink("images/ep004/ep004_quarters_lilly_smile") with dissolve
                        l "All right, I think."
                        l "She keeps to herself."
                        scene expression eye_blink("images/ep004/ep004_quarters_lilly_serious") with dissolve
                        l "I think she talks with Thim the most, but that’s just because they’re bunkmates."
                        l "I guess the situation on Lanan hit her hard."
                        c "Yeah, I think so too, she doesn’t really want to talk about it."
                        l "I’m sure in time she will."
                        scene expression eye_blink("images/ep004/ep004_quarters_lilly_smile") with dissolve
                        l "We do seem to collect the shy ones."
                        c "That we do!"
                        jump ep004_lilly_choices

            jump ep004_conversation_choices

        label ep004_kit_talk:
            $ ep004_kit_talk = True

            scene expression eye_blink("images/ep004/ep004_quarters_kit") with dissolve
            ki "Céline just pushed me inside a utility closet."
            c "I’m sure she had a very good reason."
            ki "I might have whined a little too much about this and that."
            scene expression eye_blink("images/ep004/ep004_quarters_kit_sad") with dissolve
            ki "But abusing a poor wheelchair-bound man like that!"
            c "Truly, my heart is overflowing with heartfelt compassion for you."
            scene expression eye_blink("images/ep004/ep004_quarters_kit_smile") with dissolve
            ki "Thanks man, glad to have a friend like you in this harsh universe of ours."
            c "Your hardships aside, how are you holding up?"
            scene expression eye_blink("images/ep004/ep004_quarters_kit") with dissolve
            ki "Pretty good actually, Cé thinks I’ll be able to walk on my own again real soon."
            c "The ship’s autodoc tell her that?"
            ki "Yes, it’s not the most advanced system in existence, but it does the job."
            c "Like almost everything around here."
            c "So you’ll be up and about running through the halls again?"
            ki "Looks like."
            c "When that happens, we should celebrate."
            ki "Great idea."
            if not ep004_aven_kepler_talk and (ep002_nadya_dismissed and ep004_nadya_talk):
                scene expression eye_blink("images/ep004/ep004_quarters_kit_smile") with dissolve
                ki "There’s this one place I always wanted to go."
                c "The Monument to Earth on Draugr?"
                ki "Pfah, who cares."
                ki "No, there’s a certain moon orbiting Kepler XIV."
                c "Yes..."
                scene expression eye_blink("images/ep004/ep004_quarters_kit_smile_alt") with dissolve
                ki "I’ve only heard about it, but it’s supposed to be awesome."
                c "You’re not talking about the local wildlife?"
                ki "In a sense..."
                ki "The women are said to be exquisite."
                ki "It’s a place where everyone comes to relax and just give in to any urge you might have."
                c "Any?"
                ki "Within reason, though there aren’t many rules..."
                ki "The Sovereignty doesn’t look to closely at what happens on Kepler."
                c "Yes, the Sovereignty..."
                c "I’ve been to Kepler XIV when I was little and it’s right at the edge of Sovereignty space."
                ki "It is."
                scene expression eye_blink("images/ep004/ep004_quarters_kit_unsure") with dissolve
                ki "That’s a problem, isn’t it?"
                c "Not necessarily, but we’ll have to be careful."
                scene expression eye_blink("images/ep004/ep004_quarters_kit_smile_alt") with dissolve
                ki "Careful, so we’re going?"
                c "That’s the plan."
                ki "But it might be dangerous."
                c "I’m sure Thyia knows something to mask the ship’s ownership records."
                c "And if we keep a relatively low profile, I’m sure we’ll be fine."
                ki "Sounds like a plan."
                c "Just hop out of that wheelchair and we’ll be off."
                ki "Working on it!"
            jump ep004_conversation_choices


        label ep004_nadya_talk:
            $ ep004_nadya_talk = True
            scene expression eye_blink("images/ep004/ep004_quarters_n") with dissolve
            c "How are you holding up?"
            na "I’m fine, I guess."
            scene expression eye_blink("images/ep004/ep004_quarters_n_sad") with dissolve
            na "Karan was far from an easy man to get along with, but I’d still call him a friend."
            na "To see him murdered so viciously..."
            na "Who’d do such a thing?"
            c "I don’t know."
            c "But his line of research got him into trouble once or twice, right?"
            scene expression eye_blink("images/ep004/ep004_quarters_n_serious") with dissolve
            na "Yes, people threatened his life on several occasions."
            na "Especially when he started probing in unsanctioned research programs."
            na "There are more of those programs than anyone dares to admit..."
            na "The research that comes out of those places is mind-boggling sometimes."
            c "I guess that’s the benefit of setting aside any kind of morals or ethical oversight."
            scene expression eye_blink("images/ep004/ep004_quarters_n_angry") with dissolve
            na "Yes, I have absolutely no illusions about those kinds of places."
            scene expression eye_blink("images/ep004/ep004_quarters_n_sad") with dissolve
            na "There’s so much ugliness in the galaxy..."
            c "I hope I’ll be able to visit the beautiful places with you too."
            scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
            na "That’s sweet of you to say and I hope so too."

            if not ep002_nadya_dismissed:
                scene expression eye_blink("images/ep004/ep004_quarters_n") with dissolve
                na "Aven told me you handled the situation on Sagueliath well."
                c "Really, she told me I took a big risk shooting at the ceiling like that."
                na "You probably did, but fighting a boverine calls for extreme measures."
                c "I’ve noticed, tough bastards."
                na "Especially when they’re hungry."
                c "Such a surprise, considering they’re such cute animals when they’re young."
                scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
                na "Agreed, very cuddly."
                na "All in all a little different from exploring the local wildlife on Tuolovi."
                c "You could say that again, there were a lot less near-death experiences involved, if I remember correctly."
                scene expression eye_blink("images/ep004/ep004_quarters_n_unsure") with dissolve
                na "Very true, though you came close once or twice."
                c "Really?"
                na "Yes, don’t you remember?"
                na "It wasn’t on Tuolovi, but during one of those holidays on Kepler XIV."
                c "The beach resort?"
                scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
                na "Yes, right at the edge of Sovereignty space."
                if ep004_aven_kepler_talk:
                    c "Funny you should mention it, Aven and I just had a conversation about the place."
                    c "We made that raft together, didn’t we?"
                else:
                    c "I think I remember."
                    c "Aven and I made a raft together, didn’t we?"
                na "Yes, you did."
                na "It had a sail and everything."
                na "So you decided to take it out on the open sea."
                na "Everything went fine as long as you didn’t go past the buoys."
                c "Of course we had to try and do just that..."
                scene expression eye_blink("images/ep004/ep004_quarters_n_serious") with dissolve
                na "Exactly..."
                na "I think there was something up with Eva or Lilly and I had to take them back to the pavilion in a hurry."
                na "When I returned you’d already gone past the buoys and the current was pulling at that raft like crazy."
                c "I believe the exact moment Aven and I began to panic."
                na "And rightly so, because the raft started to fall apart."
                na "In the end a rescue team had to pull you from the wreckage."
                na "I was worried sick, you were both excellent swimmers, but you could have drowned in that current."
                c "But apart from shipwrecking and giving you a heart attack those holidays were fun."
                scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
                na "They were."
                na "One of the rare times Agust allowed us to use the family ship for transport as well."
                c "Mom and dad came too, right?"
                na "They did."
                c "I have almost no memory of them being there."
                scene expression eye_blink("images/ep004/ep004_quarters_n_serious") with dissolve
                na "That’s because they partied all night and slept during the day."
                c "Right, sounds like them."
                na "Being in charge of all of you was hard work, but it was so nice having you all together."
                na "And Kepler was a truly beautiful place."
                c "Supposedly one of the best climates in Sovereignty space."
                c "Did you ever go back there?"
                scene expression eye_blink("images/ep004/ep004_quarters_n_unsure") with dissolve
                na "Alone?"
                na "No, there wasn’t much for me to do there."
                c "Getting a tan and showing off your bikini body to everyone?"
                scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
                na "Hah, yeah right."
                if ep004_aven_kepler_talk:
                    c "I already told Aven we should go back."
                else:
                    c "We should go back."
                scene expression eye_blink("images/ep004/ep004_quarters_n_unsure") with dissolve
                na "To Kepler?"
                c "Yes!"
                c "For old time’s sake."
                scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
                na "That sounds lovely, but you do realize Kepler is still in Sovereignty space?"
                na "And last thing I heard is that you were wanted by the Sovereignty, so going right to their doorstep doesn’t sound like the best of ideas."
                c "We’ll think of something."
                c "I’m sure Thyia knows something to mask the ship’s ownership records."
                c "And we’ll be very careful."
                scene expression eye_blink("images/ep004/ep004_quarters_n_serious") with dissolve
                na "It’s too dangerous, [p_name_short]."
                na "Think about it for one moment."
                na "Don’t risk everything just to go on some nostalgia trip."
                c "Where’s the fun in living risk-free?"
                c "We won’t rush into things, I promise, but I’ll get us on Kepler safe and sound, that’s a promise."
                na "I won’t be sorry if you don’t keep that promise."
                if ep004_aven_kepler_talk:
                    c "Sunny beaches, good food..."
                else:
                    c "Lying on a beach in the warm sun, sipping cocktails..."
                scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
                na "That does sound lovely."
                c "See!"
                scene expression eye_blink("images/ep004/ep004_quarters_n_serious") with dissolve
                na "[p_name_short]..."
                na "Just be careful, okay?"
                c "I will."

            menu ep004_nadya_choices:
                "About university" if not ep004_n_university:
                    $ ep004_n_university = True
                    c "I never asked, but is the university okay with you not being there?"
                    na "Of course they are."
                    na "You didn’t think I’d leave without notifying them?"
                    c "Don’t you have classes to teach?"
                    scene expression eye_blink("images/ep004/ep004_quarters_n") with dissolve
                    na "I’ve been working on my research for several years, delegated teaching to some of my assistants."
                    na "The university doesn’t seem to mind."
                    jump ep004_nadya_choices
                "Life after Tuolovi" if not ep004_n_tuolovi:
                    $ ep004_n_tuolovi = True
                    c "How did you end up at the university anyway?"
                    na "Well, after I left Tuolovi I started contacting some scientists I knew from back in the day."
                    if game.is_special:
                        na "I had quite the career before becoming a mother and kept an eye on the developments in my field of research."
                    else:
                        na "I had quite the career before coming to Tuolovi and kept an eye on the developments in my field of research."
                    c "Still, you were out of the game for quite a while, weren’t you?"
                    scene expression eye_blink("images/ep004/ep004_quarters_n_serious") with dissolve
                    na "Yes, that’s true."
                    na "Without my contacts I wouldn’t have been able to get even a minor position on Ryūjin Prime."
                    na "So I started playing catch-up and taking on risky field research jobs, Aven eventually accompanying me."
                    na "That high-risk research paid off after a while, with the university taking notice and eventually promoting me ever higher up the food chain."
                    c "So you’re in a relatively comfortable position right now?"
                    scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
                    na "Yes, you could say that, especially considering where I came from "
                    na "Apart from the university budget, some commercial sponsors have taken an interest in some of my research over the years."
                    na "So I’ve operated relatively independent the past few years."
                    c "I’m glad you landed on your feet like that."
                    jump ep004_nadya_choices
                "Life outside Sovereignty" if not ep004_n_sovereignty:
                    $ ep004_n_sovereignty = True
                    c "How were you able to leave the Sovereignty?"
                    scene expression eye_blink("images/ep004/ep004_quarters_n_serious") with dissolve
                    na "Leaving isn’t hard, getting back in is."
                    na "There’s no law forbidding you to leave, but the government has run some very effective propaganda campaigns over the years and people just don’t bother."
                    c "I was a little surprised, non-Sovereignty space is a lot different than in those government videos."
                    na "Of course it is."
                    scene expression eye_blink("images/ep004/ep004_quarters_n") with dissolve
                    na "Take Ryūjin Prime for example, it’s one of the most well-respected places in the universe."
                    na "There’s no university inside Sovereignty space that can compare itself to the one on Ryūjin."
                    na "The fact that the Sovereignty doesn’t allow any contact with alien scientists is a major factor of course."
                    na "But I won’t lie, I had to adjust my world-view when I travelled outside the borders of the Sovereignty."
                    scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
                    na "I was paired with a Vbrecl xenobiologist for the first few years at the university, I certainly wasn’t prepared for that..."
                    c "A Vbrecl?"
                    na "Yes, if there’s a species with a culture unlike ours it’s the Vbrecl."
                    scene expression eye_blink("images/ep004/ep004_quarters_n") with dissolve
                    na "They also prefer to communicate telepathically, which is extremely invasive if you’re not used to it."
                    na "The scientist I had to work with was a prime specimen of the Vbrecl, socially awkward, but extremely brilliant."
                    na "We fought a lot in the beginning, but came to respect one another after working so close together."
                    na "So, prepare yourself for some weird stuff along the way, but the galaxy is filled with very decent people."
                    c "Now I’m curious about those Vbrecl."
                    scene expression eye_blink("images/ep004/ep004_quarters_n_smile") with dissolve
                    na "I’ll be sure to introduce you to my colleague if we get the chance."
                    jump ep004_nadya_choices

            jump ep004_conversation_choices

        label ep004_aven_talk:
            if not ep004_aven_encounter:
                $ ep004_aven_encounter = True
                scene expression eye_blink("images/ep004/ep004_quarters_av_cleavage") with vpunch
                c "I...{w} Oh..."
                av "[p_name]?"
                scene expression eye_blink("images/ep004/ep004_quarters_av_cleavage_alt") with dissolve
                c "Shit...{w} I..."
                scene expression eye_blink("images/ep004/ep004_quarters_av_cleavage") with dissolve
                av "You're staring."
                av "Never seen cleavage up close?"
                c "I have...{w} I mean...{w} I'll leave."
                av "Guess you didn't do the communal shower thing at the Academy?"
                c "No, we didn't."
                scene expression eye_blink("images/ep004/ep004_quarters_av_cleavage_smile") with dissolve
                av "Well, I saw some things back on Skarak, so showing you a bit of skin isn't going to harm anybody."
                av "Did you need something?"
                c "Just wanted to talk."
                av "I was about to hit the showers, maybe we can talk afterwards?"
                c "That sounds good."
                scene expression eye_blink("images/ep004/ep004_quarters_av_cleavage_smile_alt") with dissolve
                av "I can't believe I made you blush!"
                menu:
                    "It’s human nature [AvenPath]":
                        if game.is_special:
                            c "Well, bumping into half-naked cousins has that effect on me."
                        else:
                            c "Well, bumping into half-naked girls has that effect on me."
                        av "See you later!"
                    "Don’t do it again":
                        $ ep004_aven_dismiss = True
                        c "Just make sure it never happens again."
                        scene expression eye_blink("images/ep004/ep004_quarters_av_cleavage_angry") with vpunch
                        av "Well, okay, maybe next time you can just knock?"

                jump ep004_conversation_choices
            else:
                $ ep004_aven_talk = True
                if ep004_aven_dismiss:
                    scene expression eye_blink("images/ep004/ep004_quarters_av_serious") with dissolve
                    av "Have you recovered from before?"
                    c "Of course..."
                    av "Was there something urgent you'd like to discuss?"
                    c "Not really."
                    if ep003_aven_lilly_deride:
                        av "Maybe you should get the fuck out of here then."
                    else:
                        av "In that case I'd like to be left alone."
                    c "Suit yourself."
                else:
                    $ ep004_aven_kepler_talk = True
                    scene expression eye_blink("images/ep004/ep004_quarters_av_smile") with dissolve
                    av "Have you recovered from before?"
                    c "Of course...{w} Enjoyed the shower?"
                    av "I certainly did."
                    av "That was pretty close on Sagueliath and again on Skarak."
                    c "You could say that again."
                    av "But you handled yourself pretty well."
                    c "You sound surprised?"
                    scene expression eye_blink("images/ep004/ep004_quarters_av_smile_alt") with dissolve
                    av "Well, you used to trip over your own feet as a young boy."
                    c "Lies!"
                    av "Wasn’t the first time we nearly died together."
                    if not ep002_nadya_dismissed and ep004_nadya_talk:
                        c "Funnily enough, Nadya brought up Kepler when I spoke to her."
                        c "Remember?{w} The raft..."
                    else:
                        av "Remember Kepler?"
                        c "Vividly."
                        c "The raft..."
                    scene expression eye_blink("images/ep004/ep004_quarters_av_serious") with dissolve
                    av "Yes, that fucking raft."
                    av "We were so proud of ourselves, having built that thing together."
                    c "It floated pretty well, if I remember correctly."
                    av "It did, just not on the open sea where the currents tore the thing apart."
                    c "The coast guard rescued us, didn’t they?"
                    av "Yes, they picked us up from the wreckage."
                    if game.is_special:
                        av "Mom was beside herself with worry, she saw the whole thing happen while keeping an eye on Lilly and Eva."
                    else:
                        av "Nadya was beside herself with worry, she saw the whole thing happen while keeping an eye on Lilly and Eva."
                    c "Apart from the drowning I really loved those holidays on Kepler."
                    scene expression eye_blink("images/ep004/ep004_quarters_av_smile") with dissolve
                    c "We went a couple of times, didn’t we?"
                    av "Yes, whenever your mom and dad wanted to drown themselves in expensive liquor."
                    if not ep002_nadya_dismissed and ep004_nadya_talk:
                        c "Nadya mentioned that too, I almost forgot."
                    else:
                        c "They were there too, I almost forgot."
                    scene expression eye_blink("images/ep004/ep004_quarters_av_smile") with dissolve
                    av "You’re forgiven, considering how little they were interested in us..."
                    if not ep002_nadya_dismissed and ep004_nadya_talk:
                        c "Yeah..."
                    else:
                        c "Sounds like them all right."
                    scene expression eye_blink("images/ep004/ep004_quarters_av_smile_alt") with dissolve
                    if game.is_special:
                        av "I think mom loved it just as much as we did, despite all the responsibility of minding the children falling to her."
                    else:
                        av "I think Nadya loved it just as much as we did, despite all the responsibility of minding the children falling to her."
                    if not ep002_nadya_dismissed and ep004_nadya_talk:
                        c "Yes, she told me as much."
                        c "You never went back there, after you left Tuolovi, right?"
                    else:
                        c "Did you ever go back there, you know, after you left?"
                    scene expression eye_blink("images/ep004/ep004_quarters_av_serious") with dissolve
                    av "No, never."
                    if game.is_special:
                        av "Kepler is very expensive and mom had a lot on her mind after leaving Tuolovi."
                    else:
                        av "Kepler is very expensive and Nadya had a lot on her mind after leaving Tuolovi."
                    if not ep002_nadya_dismissed and ep004_nadya_talk:
                        c "I already promised Nadya to go back there some time."
                    else:
                        c "We should go back there one time."
                    c "Make some money and spend it all on a nostalgic holiday to Kepler."
                    scene expression eye_blink("images/ep004/ep004_quarters_av_smile") with dissolve
                    av "Fat chance it’s going to happen."
                    av "Kepler is right at the edge of Sovereignty space and last I checked you were on the run from them."
                    if not ep002_nadya_dismissed and ep004_nadya_talk:
                        if game.is_special:
                            c "You're just as big a spoilsport as your mom."
                        else:
                            c "You're just as big a spoilsport as Nadya."
                    c "We’ll think of something."
                    c "I’m sure Thyia knows something to mask the ship’s ownership records."
                    c "And we’ll be very careful."
                    scene expression eye_blink("images/ep004/ep004_quarters_av_serious") with dissolve
                    av "You’re serious, aren’t you?"
                    c "Increasingly so."
                    if not ep002_nadya_dismissed and ep004_nadya_talk:
                        c "Sunny beaches, good food, lots of parties..."
                    else:
                        c "Lying on a beach in the warm sun, sipping cocktails..."
                    scene expression eye_blink("images/ep004/ep004_quarters_av_smile") with dissolve
                    av "Getting caught by the police, spending years in a jail cell until you get executed for desertion..."
                    c "Minor details...{w} You’ve got to admit the first parts sounds good, no?"
                    scene expression eye_blink("images/ep004/ep004_quarters_av_smile_alt") with dissolve
                    av "All right, I’ll give you that."
                    c "See!"
                    c "That’s settled then."
                    av "[p_name_short]..."
                    if not ep002_nadya_dismissed and ep004_nadya_talk:
                        c "Sunny beaches, good food, parties!"
                    else:
                        c "Beaches, sun, cocktails!"
            jump ep004_conversation_choices

        label ep004_celine_talk:
            $ ep004_celine_talk = True
            scene expression eye_blink("images/ep004/ep004_quarters_ce") with dissolve
            c "Hey, are you alone?"
            ce "I am, but I don't know for how long."
            ce "Kit just learned that Ziv scaled some famous rock formation and is beyond excited."
            c "He's going to pester her for hours, isn't he?"
            scene expression eye_blink("images/ep004/ep004_quarters_ce_smile") with dissolve
            ce "He's been gone for a while now..."
            c "In that case I'm going to steal a kiss."
            scene ep004_quarters_ce_kiss with dissolve
            "I took her head in my hands and kissed her lips, a gesture she eagerly returned."
            "The feeling of her small yet firm breasts beneath the thin layer of her top aroused something in me."
            scene expression eye_blink("images/ep004/ep004_quarters_ce_kiss_closeup") with dissolve
            ce "We can't, [p_name_short], what if he comes in?"
            c "He's still in that chair, isn't he..."
            scene expression eye_blink("images/ep004/ep004_quarters_ce_kiss_closeup_shock") with dissolve
            ce "[p_name_short]!"
            c "This complete lack of privacy is one of the main downsides of living on this ship."
            scene expression eye_blink("images/ep004/ep004_quarters_ce_kiss_closeup") with dissolve
            ce "At least you have your own quarters."
            c "True, but the sound still carries through these thin walls..."
            scene expression eye_blink("images/ep004/ep004_quarters_ce_kiss_closeup_unsure") with dissolve
            ce "Maybe we should tell Kit about us?"
            c "Maybe..."
            c "It's just that I want this secret to be between us for a little while longer."
            c "We never had the chance to do something romantic together, with all the shit that's been going on."
            ce "What did you have in mind?"
            c "Candle-light dinner, for starters."
            c "A stroll through a park, walking hand in hand."
            c "Sitting at the river-bank and watching the sun go down together."
            scene expression eye_blink("images/ep004/ep004_quarters_ce_kiss_closeup_smile") with dissolve
            ce "That sounds so nice."
            c "You know what, once we reach Barranthis, I'll take you out somewhere."
            c "Just the two of us."
            ce "I think I'd like that."
            if is_patreon() and renpy.has_label("extra_scene_06"):
                call extra_scene_06 from _call_extra_scene_06

                if renpy.has_label("extra_scene_07") and not _in_replay:
                    call extra_scene_07 from _call_extra_scene_07
                    "We kissed one last time and then I slipped out before her brother returned for the second time."
            else:
                scene ep004_quarters_ce_kiss with dissolve
                "I kissed her in response and we cuddled for a short while until I slipped out before her brother returned."

            jump ep004_conversation_choices

        label ep004_thyia_talk:
            $ ep004_thyia_talk = True
            scene ep004_quarters_l_th with dissolve
            c "Is that a bottle of liquor?"
            th "Maybe..."
            l "Thyia bought a bottle of whisky on Verdant Station."
            th "Want some?"
            th "It’s pretty good stuff."
            menu:
                "Drink with them [ThyiaPath] [LillyPath]":
                    $ ep004_th_l_drinks = True
                    c "Why not."
                    scene expression eye_blink("images/ep004/ep004_quarters_th") with dissolve
                    th "Lilly told me a bit about your family."
                    th "Didn’t know your mother was behind that hit song from years ago."
                    c "A team of producers was behind that minor hit."
                    c "And I think it was mostly popular because of the VR-clip where she wore next to nothing."
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup_smile") with dissolve
                    l "Right!{w} That tiny piece of cloth was downright embarrassing."
                    c "Opinions differ on the matter, I believe..."
                    scene expression eye_blink("images/ep004/ep004_quarters_th") with dissolve
                    th "You never wanted to follow in your mother’s footsteps, Lilly?"
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup_unsure") with dissolve
                    if game.is_special:
                        l "Dancing in a monokini?"
                        l "Not really..."
                        scene expression eye_blink("images/ep004/ep004_quarters_th") with dissolve
                        th "Becoming a pop star, I meant."
                    else:
                        l "Becoming a gardener?"
                        l "Not really..."
                        scene expression eye_blink("images/ep004/ep004_quarters_th") with dissolve
                        th "Right, but something else maybe?"
                    scene ep004_quarters_l_th_glasses with dissolve
                    l "I never got the chance really, they picked the Naval Academy for me and that was that."
                    if game.is_special:
                        c "Mom and dad weren’t big on the whole upbringing thing."
                    else:
                        c "Both our parents weren’t big on the whole upbringing thing."
                    scene expression eye_blink("images/ep004/ep004_quarters_th_serious") with dissolve
                    th "Dreadful business, raising children."
                    c "They certainly thought so."
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup") with dissolve
                    l "Come on, [p_name_short], it wasn’t all bad!"
                    if game.is_special:
                        c "That’s because daddy liked you, Lilly."
                    else:
                        c "That’s because your daddy liked you, Lilly."
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup_angry") with dissolve
                    l "Don’t give me that."
                    if game.is_special:
                        l "If you behaved from time to time..."
                    else:
                        l "If you behaved from time to time I'm sure your dad would like you too..."
                    c "I might have gotten a pat on the head more often. "
                    c "Still would have ended up at the Naval Academy though."
                    scene ep004_quarters_l_th_glasses with dissolve
                    th "How did you manage in such a place?"
                    l "What do you mean?"
                    th "The hierarchy must be oppressing."
                    th "All that “yes sir”, “no sir”."
                    l "You get used to that pretty quickly."
                    th "I’m not sure I would."
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup") with dissolve
                    l "Now that you mention it, [p_name_short] also had a lot of trouble with the whole chain-of-command thing."
                    c "I think it makes everything unnecessarily complicated."
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup_smile") with dissolve
                    l "Keep telling yourself that..."
                    scene ep004_quarters_l_th_glasses with dissolve
                    l "You were born outside the Sovereignty, right Thyia?"
                    th "I was."
                    scene expression eye_blink("images/ep004/ep004_quarters_th_serious") with dissolve
                    th "My parents were pretty much the same as yours when it came to raising me."
                    c "Meaning they were never there?"
                    th "Exactly."
                    th "Though for very different reasons."
                    th "Dad left us even before my mother had me."
                    th "And my mother loved alcohol a little too much."
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup") with dissolve
                    l "Are you still in contact with her?"
                    scene expression eye_blink("images/ep004/ep004_quarters_th_serious") with dissolve
                    th "No."
                    th "I left as soon as I was able."
                    th "Never spoke to her again."
                    l "So you went to Vulpes Velox?"
                    scene expression eye_blink("images/ep004/ep004_quarters_th_smile") with dissolve
                    th "Haha, no, I was twelve when I left my mother."
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup_unsure") with dissolve
                    l "Oh...{w} But..."
                    scene expression eye_blink("images/ep004/ep004_quarters_th_serious") with dissolve
                    th "I lived on the streets for a while."
                    th "Joined a gang, because you won’t live long on your own out there without some form of protection."
                    th "I wasn’t cut out for a life of petty crime though, luckily my knack for fixing things is what ultimately saved me."
                    th "I started repairing stuff for other members of the crew."
                    scene expression eye_blink("images/ep004/ep004_quarters_th_serious_alt") with dissolve
                    th "Eventually I didn’t have to go on raids anymore because they became too reliant on me fixing their gear after some fight with local law enforcement."
                    th "I saved any credit I received and once I had enough, bought a ticket on the next transport out of that hell hole."
                    th "Wandered for a good while and started working as an independent contractor."
                    th "The workshop on Vulpes Velox was a recent thing actually, wasn’t there for longer than two years."
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup_unsure") with dissolve
                    l "And we disturbed all of that."
                    scene expression eye_blink("images/ep004/ep004_quarters_th_serious") with dissolve
                    th "Nah, Glixken did that."
                    th "Besides, I’m not one to stay in one place for too long."
                    th "This setup here on the Bastard suits me fine, actually."
                    scene ep004_quarters_l_th_bottle with dissolve
                    th "I’m talking too much, who’s up for another drink?"
                    l "Me!"
                    c "I’m good, thanks."
                    c "Going to leave you ladies alone for a while."
                    l "No problem, more booze for us!"
                    scene expression eye_blink("images/ep004/ep004_quarters_l_closeup_unsure") with dissolve
                    l "Oh-"
                    l "I-{w} I didn’t mean it like that, Thyia."
                    scene expression eye_blink("images/ep004/ep004_quarters_th_smile") with dissolve
                    th "What?"
                    l "Maybe I shouldn’t have said that, you know, with your mother and all..."
                    scene ep004_quarters_l_th_bottle with dissolve
                    th "Don’t worry about that!"
                    l "Thanks, in that case, hit me up!"
                "No thanks":
                    c "No thanks, you enjoy."
                    th "Suit yourself."

            jump ep004_conversation_choices

        label ep004_eva_talk:
            $ ep004_eva_talk = True

            play music "music/cobalt.ogg" fadeout 4 fadein 1.0

            scene expression eye_blink("images/ep004/ep004_quarters_cam") with dissolve
            "Fears of dreaming about Eva again kept me awake."
            "I heard the sounds of the crew die down around me, until I was alone with the hum of the ship."
            "After the fourth desperate hour of sleeplessness, I decided to check out the VR room."
            scene ep004_quarters_cam_corridor with dissolve
            "With every step towards the remote part of the ship where the room was located, the guilty feeling of what I was about to do increased."
            if game.is_special:
                "I just longed to see Eva again, but I knew Lilly would tear me a new one for loading a virtual copy of our sister in a simulation."
            else:
                "I just longed to see Eva again, but I knew Lilly would tear me a new one for loading a virtual copy of our best friend in a simulation."
            "Not that the practice was uncommon, but it was usually reserved for people to meet their deceased loved ones."
            "Interacting with a virtual person was said to be very lifelike, as the memories up until the point when their brain was scanned were fully accessible to the digital version."
            "Creating a virtual copy was a process requiring an inordinate amount of paperwork and consent of all the parties involved."
            "I had neither."
            "Ignoring the pangs of guilt, I entered the VR room."
            scene ep004_quarters_cam_sim_room with dissolve
            "Jade didn’t lie when she said the interface was old tech, but it still worked and was ready for me to use."
            "Like at ConVitæ, the shift between reality and the virtual was a nauseating experience."
            scene ep004_simulation with pixellate
            e "[p_name]?"
            scene ep004_simulation_eva with pixellate
            pause
            scene ep004_simulation_eva_dressed with pixellate
            c "Eva?"
            scene ep004_simulation_eva_active with dissolve
            e "[p_name_short], is that really you?"
            scene ep004_simulation_eva_active_hug with dissolve
            "I just hugged her and she let me, though I could sense her bewilderment while doing so."
            scene expression eye_blink("images/ep004/ep004_simulation_eva_active_closeup") with dissolve
            e "Why is it so empty here?"
            e "Where are we?"
            e "Are we far from our house?"
            "The virtual copy of Eva clearly didn’t experience the events on Lanan, maybe not even her stint at the academy."
            "So I decided not to confuse matters any further by attempting to explain everything."
            c "No, not far."
            "Using the virtual console, I called up the schematics of the family mansion on Tuolovi."
            "Once it was loaded, I took Eva’s hand."
            c "Come, let’s go home."
            scene expression eye_blink("images/ep004/ep004_simulation_eva_active_walk") with dissolve
            e "How have you been, [p_name_short]?"
            e "It feels like ages since I last talked to you."
            e "How’s the academy, is it exciting?"
            c "It’s a little lonely, so I’m glad to be back."
            e "You have to tell me all about it when we get home!"
            scene ep004_simulation_eva_estate with dissolve
            "We trudged through the virtual emptiness for a while, until we passed the gates of our estate."
            "Eva didn’t seem perturbed by the weird transition between the flat nothingness and the vibrancy of the estate’s grounds."
            "Instead, she held my hand firmly in hers and chatted about what had happened on Tuolovi during my first semester at the academy."
            "Of course, I heard it all before, but I was just so happy to hear Eva’s voice again."
            scene expression eye_blink("images/ep004/ep004_simulation_eva_estate_closeup") with dissolve
            e "So, have you made any friends already?"
            c "A couple."
            e "I can’t wait for us to join you!"
            scene expression eye_blink("images/ep004/ep004_simulation_eva_estate_closeup_serious") with dissolve
            e "Lilly has a hard time picturing herself away from Tuolovi, but I’m done with the place."
            c "Really, I thought you weren’t overjoyed with the prospect of studying at the Academy"
            e "I’m not, but it beats staying here."
            c "No argument there."
            scene expression eye_blink("images/ep004/ep004_simulation_eva_estate_interior") with dissolve
            e "[p_name_short], the house seems so empty."
            e "It wasn’t empty when I left it."
            e "Where’s everyone?"
            c "I’m sure there’s an explanation for that."
            c "I’ll go find someone."
            c "Why don’t you sit down here."
            scene expression eye_blink("images/ep004/ep004_simulation_eva_estate_interior_sit") with dissolve
            e "Okay, but don’t be too long."
            c "I won’t!"
            "I couldn’t bear explaining everything to her and ended the simulation as soon as I closed the door on her."
            scene ep004_quarters_cam_sim_room with pixellate
            "Not sure whether all this had been a good idea, I walked back to my quarters and fell down on my bunk."
            scene ep004_quarters_cam_sleep with dissolve
            "I fully expected to lie awake for the rest of the cycle, but instead a dreamless sleep overtook me in minutes."

            play music [ "music/searching-the-cosmos.ogg", "music/the-restoration.ogg", "music/space-harmony.ogg" ] fadeout 4 fadein 1.0

            jump ep004_conversation_choices

        label ep004_raene_talk:
            if not ep004_ziv_ra_injection:
                $ ep004_ziv_ra_injection = True
                scene ep004_quarters_zi_ra with dissolve
                "The door of Ziv and Raene’s quarters was slightly open and I could see both women sitting next to each other."
                "Ziv appeared to be injecting Raene with something."

                menu:
                    "[gr]Confront them":
                        $ ep004_ra_confront = True
                        c "What are you two doing?"
                        scene ep004_quarters_zi_ra_shock with vpunch
                        c "Are you taking drugs?"
                        scene ep004_quarters_zi_ra_angry with vpunch
                        zi "What do you take us for?!"
                        c "I don’t know, Ziv, you tell me."
                        zi "Raene needs medicine, that’s all you need to know."

                        menu:
                            "Get angry":
                                $ ep004_ra_confront_angry = True
                                c "Is that so?"
                                c "You’re a guest on my ship, so I’d like to know if you’re sticking needles into people for some reason."
                                c "I mean, is Raene contagious?"
                                c "Is she fucking dangerous?!"
                                scene ep004_quarters_zi_ra_sad with dissolve
                                ra "[p_name], please..."
                                zi "Raene needs regular injections."
                                zi "That’s all you need to know, as I’ve already made perfectly clear to you."
                                zi "Now go away."
                            "Accept [RaenePath]":
                                c "I didn’t know that."
                                c "If she needs any medical attention, just let me know."
                                scene ep004_quarters_zi_ra_smile with dissolve
                                ra "Thank you, [p_name]."
                    "Leave them be":
                        "I decided not to get involved in what was clearly a private matter between Ziv and Raene."
            else:
                $ ep004_raene_talk = True
                scene expression eye_blink("images/ep004/ep004_quarters_ra") with dissolve
                c "Hey, do you have everything you need?"
                ra "I think so...{w} Yes."
                c "Good."
                menu:
                    "Say something nice [RaenePath]":
                        $ ep004_ra_kind = True
                        c "Glad to have you aboard."
                    "Leave":
                        c "I’ll be on the bridge if you need me."
                scene expression eye_blink("images/ep004/ep004_quarters_ra_unsure") with dissolve
                ra "Ah...{w} [p_name]?"
                c "Yes?"
                if ep004_ra_confront:
                    scene expression eye_blink("images/ep004/ep004_quarters_ra_sad") with dissolve
                    ra "I’m sorry you had to see that earlier."
                    ra "The injections, I mean."
                    c "Ziv isn’t forcing them on you, is she?"
                    ra "Oh no, not at all!"
                    scene expression eye_blink("images/ep004/ep004_quarters_ra_shock") with dissolve
                    ra "You don’t think Ziv is...{w} I’m not her captive, or anything."
                    ra "I’d hate for you to think ill of her."
                    menu:
                        "Acknowledge [RaenePath]":
                            c "Don’t worry, I don’t."
                        "Doubt":
                            $ ep004_ra_doubt = True
                            c "I don’t know, Raene, just making sure."
                    scene expression eye_blink("images/ep004/ep004_quarters_ra") with dissolve
                    ra "Ziv and her people have been nothing but helpful."
                    c "I understand they’re helping you run from your father?"
                    scene expression eye_blink("images/ep004/ep004_quarters_ra_sad") with dissolve
                    ra "Yes..."
                    c "Does he want to hurt you?"
                    ra "No...{w} Not exactly."
                    c "It's something political then?"
                    ra "No..."
                    menu:
                        "Get angry":
                            $ ep004_ra_angry = True
                            c "Do you need to be so vague?!"
                            c "Why do you keep acting like you've got something to hide?!"
                            scene expression eye_blink("images/ep004/ep004_quarters_ra_sad_alt") with dissolve
                            ra "I'm sorry...{w} I..."
                            ra "I just can't."
                            scene expression eye_blink("images/ep004/ep004_quarters_ra_ziv_angry") with vpunch
                            zi "What's this, I heard you yelling?"
                            zi "Why were you yelling at her?!"
                            c "I don't-"
                            c "I'll just leave."
                            zi "You do that."
                        "Be understanding [RaenePath]":
                            c "Well, you're a guest here now, so if there's anything you need, just ask."
                            scene expression eye_blink("images/ep004/ep004_quarters_ra_smile") with dissolve
                            ra "I will, thank you [p_name]."
                else:
                    ra "Thank you for taking us in."
                    c "It’s not trouble."
                    c "I understand Ziv and her people are helping you run from your father?"
                    scene expression eye_blink("images/ep004/ep004_quarters_ra_sad") with dissolve
                    ra "Yes..."
                    c "Does he want to hurt you?"
                    ra "No...{w} Not exactly."
                    c "It's something political then?"
                    ra "No..."
                    menu:
                        "Get angry":
                            $ ep004_ra_angry = True
                            c "Do you need to be so vague?!"
                            c "Why do you keep acting like you've got something to hide?!"
                            scene expression eye_blink("images/ep004/ep004_quarters_ra_sad_alt") with dissolve
                            ra "I'm sorry...{w} I..."
                            ra "I just can't."
                            scene expression eye_blink("images/ep004/ep004_quarters_ra_ziv_angry") with vpunch
                            zi "What's this, I heard you yelling?"
                            zi "Why were you yelling at her?!"
                            c "I don't-"
                            c "I'll just leave."
                            zi "You do that."
                        "Be understanding [RaenePath]":
                            c "Well, you're a guest here now, so if there's anything you need, just ask."
                            scene expression eye_blink("images/ep004/ep004_quarters_ra_smile") with dissolve
                            ra "I will, thank you [p_name]."
            jump ep004_conversation_choices

        label ep004_ziv_talk:
            $ ep004_ziv_talk = True

            if ep004_ra_confront and not ep004_ziv_ra_talk:
                $ ep004_ziv_ra_talk = True
                scene expression eye_blink("images/ep004/ep004_quarters_ziv_serious") with dissolve
                zi "About before, with Raene..."
                c "Yes?"
                if ep004_ra_confront_angry:
                    zi "I get why you’re angry about it, but Raene will be able to tell you more as soon as she’s ready."
                else:
                    zi "Raene will be able to tell you more as soon as she’s ready."
                zi "If that’s not enough we’ll leave at the next station and be out of your hair."
                c "Fair enough, I guess."

            scene expression eye_blink("images/ep004/ep004_quarters_ziv") with dissolve

            menu ep004_ziv_choices:
                "About the Rhenkoy" if not ep004_ziv_rhenkoy and not ep004_ra_confront_angry:
                    $ ep004_ziv_rhenkoy = True
                    c "You told me before you're no longer part of a Cohort?"
                    zi "That's correct."
                    c "But you're not an outcast, right?"
                    zi "No, I have official dispensation from the council."
                    zi "I may return to a Cohort at any time, if I choose to."
                    c "And you're choosing not to now, obviously."
                    zi "Obviously."
                    c "Is it because of Raene?"
                    scene expression eye_blink("images/ep004/ep004_quarters_ziv_serious") with dissolve
                    zi "Yes, she's part of the reason."
                    zi "Some members of the Rhenkoy do humanitarian work and are allowed to live without a Cohort."
                    c "So, saving Raene was part of a humanitarian mission?"
                    zi "Yes."
                    c "But why, because her father is a religious nut?"
                    zi "Partly, she asked us to rescue her, she didn't feel safe."
                    c "Didn't feel safe, in what way?"
                    scene expression eye_blink("images/ep004/ep004_quarters_ziv_doubt") with dissolve
                    zi "Look, I've already said too much, you'd have to ask her."

                    menu:
                        "Press the issue":
                            $ ep004_ziv_force = True
                            if ep004_raene_talk:
                                c "I already did, but she doesn't want to tell."
                            c "What are you two hiding, exactly?"
                            if ep004_ra_confront:
                                c "You were injecting her with something."
                            else:
                                c "I saw you injecting her with something earlier."
                            scene expression eye_blink("images/ep004/ep004_quarters_ziv_serious") with dissolve
                            zi "Raene needs regular shots, she’s no danger to you or any of the crew."
                            zi "And that’s all I’m going to say on the matter."
                        "Relent [ZivPath]":
                            c "I understand, maybe I'll ask her."
                            scene expression eye_blink("images/ep004/ep004_quarters_ziv") with dissolve
                    jump ep004_ziv_choices
                "About Skarak" if not ep004_ziv_skarak:
                    $ ep004_ziv_skarak = True
                    c "So Ziv, about what happened on the planet, with Luzane..."
                    scene expression eye_blink("images/ep004/ep004_quarters_ziv_doubt") with dissolve
                    if ep004_lu_lick or ep004_lu_suck:
                        zi "You didn't have much of a choice, did you?"
                    else:
                        zi "Nothing happened, right?"
                    c "That's not what I mean."
                    zi "What do you mean?"

                    menu:
                        "Ask about Rhenkoy genitals [ZivPath]":
                            c "It's just that Luzane turned to be a bit of a surprise."
                            c "Having both down below is a little uncommon, if you know what I mean."
                            scene expression eye_blink("images/ep004/ep004_quarters_ziv_smile") with dissolve
                            zi "Ah, but it isn't among the Rhenkoy."
                            if ep004_ziv_derisive:
                                zi "You didn't know?"
                                c "Evidently not."
                            scene expression eye_blink("images/ep004/ep004_quarters_ziv_serious") with dissolve
                            zi "There's no distinction between female and male in our society."
                            zi "We just use the term female to describe ourselves when dealing with other alien species."
                            c "I understand."
                            c "Just wanted to clear that up."
                            if not ep004_lu_lick and not ep004_lu_suck:
                                zi "Does it bother you?"
                                zi "I know it's a problem for some..."

                                menu:
                                    "Yes [EndRelationship]":
                                        $ ep004_ziv_no_romance = True
                                        c "It's a little too outlandish to wrap my head around, to be honest."
                                        c "But that doesn't mean I can't be civil about it."
                                        scene expression eye_blink("images/ep004/ep004_quarters_ziv_doubt") with dissolve
                                        zi "I'm not sure what you mean by that, but as long as you don't mean to kick me off this ship I can live with that."
                                        c "Good."
                                    "No":
                                        c "No, why would it be a problem?"
                                        scene expression eye_blink("images/ep004/ep004_quarters_ziv_smile") with dissolve
                                        zi "Just making sure and I'm very glad to hear it isn't an issue."
                        "Ask if she has a cock":
                            $ ep004_ziv_impolite = True
                            $ ep004_ziv_no_romance = True
                            c "Considering Luzane and you are the same species, do you have a cock as well?"
                            scene expression eye_blink("images/ep004/ep004_quarters_ziv_angry") with vpunch
                            zi "What kind of question is that?!"
                            zi "Get out this instant!"
                            c "It was just a question!"
                            jump ep004_conversation_choices
                        "Forget it":
                            c "Nah, forget I said anything."
                            zi "Okay..."
                    jump ep004_ziv_choices
                "About Luzane" if not ep004_lu_truth and not ep004_ziv_luzane and ep004_ziv_skarak and not ep004_ziv_no_romance:
                    $ ep004_ziv_luzane = True
                    c "So you and Luzane..."
                    zi "What about her?"
                    c "She told me you were jealous of her and Tavort."
                    scene expression eye_blink("images/ep004/ep004_quarters_ziv_doubt") with dissolve
                    zi "Did she now..."
                    c "And that you were lovers."
                    zi "Well, she was quite frank just before killing you, wasn't she?"
                    scene expression eye_blink("images/ep004/ep004_quarters_ziv_serious") with dissolve
                    zi "All right."
                    zi "Yes, I was in love with her and I thought she was too."
                    zi "At least, she gave enough hints that she liked me."
                    zi "A relationship with a Premier is a big thing in our society, but that wasn't the reason why I pursued her."
                    scene expression eye_blink("images/ep004/ep004_quarters_ziv_sad") with dissolve
                    zi "I just loved her."
                    zi "You know, that foolish young love?"
                    zi "She was older than me, a mother figure maybe, but also such a sensual person."
                    zi "We courted each other for a while, but we were never lovers."
                    scene expression eye_blink("images/ep004/ep004_quarters_ziv_serious") with dissolve
                    zi "Maybe we could have been, but then Tavort came along and swept her up."
                    c "That came as a surprise then?"
                    scene expression eye_blink("images/ep004/ep004_quarters_ziv_annoyed") with dissolve
                    zi "It sure did."
                    zi "Especially if you know what the Tubloshi look like."
                    zi "Of course you'll see them once we rendezvous with their ship, but a Rhenkoy and a Tubloshi aren't a match you see every day."
                    zi "In fact, most of the Tubloshi view other species as something you can hunt or conquer with violence."
                    c "So the union Kyl Tavort and Luzane was an oddity?"
                    zi "It sure was, someone with the characteristics of Luzane is normally shunned by the Tubloshi, reviled even."
                    c "I guess love really does conquer all, to use a tired phrase."
                    scene expression eye_blink("images/ep004/ep004_quarters_ziv_smile") with dissolve
                    zi "Yes, you might be right."
                    jump ep004_ziv_choices

            jump ep004_conversation_choices

        label ep004_jade_talk:
            $ ep004_jade_talk = True
            scene ep004_quarters_empty with dissolve
            "I messaged Jade to come to my quarters."
            scene expression eye_blink("images/ep004/ep004_quarters_jade") with dissolve
            j "You rang, master?"

            menu:
                "Put her in her place [JadeSubPath]":
                    $ ep004_jade_sex_hard = True
                    $ ep004_jade_dom = True
                    $ ep004_jade_sex = True
                    c "Cut the bullshit Jade."
                    scene expression eye_blink("images/ep004/ep004_quarters_jade_fear") with dissolve
                    c "Sit down."
                    c "No, on your knees."
                    scene expression eye_blink("images/ep004/ep004_quarters_jade_fear_kneel") with dissolve
                    j "Yes, master."
                    j "Was everything in order with the simulation, master?"
                    c "Yes, everything worked fine."
                    c "You're going to help me relax now."
                    j "That's what I'm for, master."
                    c "Undress."
                    call ep004_jade_sex_hard from _call_ep004_jade_sex_hard
                "Laugh [JadeLovePath]":
                    c "You actually enjoy coming up with these greetings, don't you Jade?"
                    scene expression eye_blink("images/ep004/ep004_quarters_jade_smile") with dissolve
                    j "I do my best."
                    c "Come sit with me."
                    scene expression eye_blink("images/ep004/ep004_quarters_jade_sit") with dissolve
                    j "Was everything in order with the simulation?"
                    c "Yes, everything worked fine."
                    c "But it was strange seeing her..."
                    j "I can imagine."
                    c "I don't want to be alone right now, Jade."
                    j "Of course, I understand."
                    scene ep004_quarters_jade_sit_lean with dissolve
                    "Jade inched closer to me and I could feel her warmth enveloping me."
                    "We sat in silence for a while, until I felt her lips brush against my skin."
                    j "I know just the thing to make you feel better."

                    menu:
                        "Go on [JadePath]":
                            $ ep004_jade_sex = True
                            c "Very intriguing."
                            j "I can make this even more intriguing."
                            call ep004_jade_sex_soft from _call_ep004_jade_sex_soft
                        "Just lie with me":
                            c "Frankly, I just want to fall asleep together."
                            j "Of course, we'll just lie down."
                            scene ep004_quarters_jade_lying with dissolve
                            "And so we did."
                            "Eventually I fell into a dreamless sleep."
                        "Not now":
                            $ ep004_jade_dismissed = True
                            c "Frankly, I just want to fall asleep."
                            c "This was a mistake, Jade."
                            scene expression eye_blink("images/ep004/ep004_quarters_jade") with dissolve
                            j "I understand, I'll leave you alone."
                            j "Sleep well, master."
            jump ep004_conversation_choices

label ep004_jade_sex_hard:
    if not _in_replay:
        $ ep004_jade_sex_hard = True
    scene ep004_quarters_jade_naked with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "Her top and skirt quickly fell to the ground and the Tw'ill stood meekly before me, waiting on my command."
    c "Go lie on the bed, head towards me."
    scene expression eye_blink("images/ep004/ep004_quarters_jade_naked_closeup") with dissolve
    j "Yes, master."
    j "Am I to be fucked?"
    c "Don't ask questions, just do as your told."
    c "Lie on the bed."
    "Jade did as she was told while I removed my shorts."
    scene ep004_quarters_jade_cock with dissolve
    "I slapped my cock against her cheek and janked her by her tails towards my crotch."
    c "Open your mouth."
    j "Yes, master."
    show ep004_quarters_jade_cock_mouth with dissolve
    "Jade struggled as my hard cock entered her mouth and I pushed the veined shaft further and further."
    scene ep004_quarters_jade_cock_mouth_alt with dissolve
    "Her eyes began to tear and she had trouble controlling her breathing."
    "Just wanting to use her, I began to fuck her throat."
    scene ep004_quarters_jade_mouth_fuck with dissolve
    "She retched and gagged as I shoved my penis up and down, her throat bulging as my balls hit her lips."
    "During the short moments I allowed her to breathe she spat out thick strings of saliva."
    scene ep004_quarters_jade_breasts with dissolve
    "I rubbed her breasts and face with some of the drool, before pushing my cock inside her mouth again."
    "This was the first time I ever treated Jade like this and she was just as surprised by my behavior as I was."
    scene ep004_quarters_jade_behind with dissolve
    "Just when she had adjusted to the throat-fucking I pulled out and turned her on her stomach."
    c "Would you like to be fucked now, Jade?"
    j "I'd love that, master."
    scene ep004_quarters_jade_behind_slap with vpunch
    "In response, I slapped her ass hard, making her clench her teeth in pain."
    c "You have such a firm ass, Jade."
    j "Thank you, master."
    with vpunch
    "I slapped her again across the buttocks and she let out a small moan."
    c "Do you like being slapped, Jade?"
    j "I do, master."
    scene ep004_quarters_jade_behind_penetrate with dissolve
    c "I grabbed her ass and pulled her towards me."
    "Her pussy glistened wet as I pushed the head of my dick against her lips."
    "She was ready for me, waiting for me to fuck her hard."
    scene ep004_quarters_jade_behind_penetrate_ass with dissolve
    "Instead of entering her, I pushed her down and poked my tip against the delicate folds of her anus."
    scene ep004_quarters_jade_behind_penetrate_ass_shock with dissolve
    j "Master?"
    "One hand pressed against her lower back, I pressed my cock against her rear opening."
    scene ep004_quarters_jade_behind_penetrate_ass_alt with dissolve
    "She whimpered as I pushed the head into her asshole."
    "Jade and I had tried anal before, mostly using fingers and toys."
    "One attempt ended in mutual discomfort, as Jade couldn’t adjust to my girth."
    "I didn’t care about any of that at that moment and kept forcing my cock inside her tight asshole."
    c "Can you take everything inside of you, Jade?"
    scene ep004_quarters_jade_behind_penetrate_ass_fear with dissolve
    j "I...{w} I...{w} Y-yes, m-master..."
    "It turned out she really could as I stuffed the last few inches of my dick inside."
    c "How do you feel, Jade?"
    scene ep004_quarters_jade_behind_penetrate_ass_pain with dissolve
    j "So f-full, master."
    c "Do you want me to fuck your ass?"
    c "Make you my little anal slut?"
    j "If you want, master."
    show ep004_quarters_jade_behind_penetrate_ass_fuck with dissolve
    "I realized I really wanted to and began to thrust back and forth."
    "Jade groaned in discomfort and held on to the bed tightly."
    "As I fucked her butt she apparently began to feel accustomed to the feeling and I felt her relax."
    scene ep004_quarters_jade_behind_penetrate_ass_fuck_alt with dissolve
    "Her asshole was still very tight, but I no longer felt restricted in my movements, so I picked up the pace."
    "With ever increasing speed I assaulted her ass, fucking her like an animal."
    "Her groans turned into moans and yelps as my cock speared her anal cavity."
    c "Do you want me to go on, Jade?"
    j "Yes, yes master!"
    scene ep004_quarters_jade_behind_penetrate_ass_cowgirl with dissolve
    "As I didn’t want to do all the work, I grabbed Jade by the waist and hauled her on top of me as I lay down on the bed."
    "She was now squatting on top of me, my throbbing shaft still rooted inside her rectum."
    c "Show me what an anal slut you really are, Jade."
    j "Yes, master."
    show ep004_quarters_jade_behind_penetrate_ass_cowgirl_alt with dissolve
    "Jade obediently moved her ass up and down on my cock."
    "Holding her waist I complemented her movements by thrusting my hips upward, penetrating her ass even more deeply."
    "My balls slapped against her wet cunt as I fucked her asshole like it was her pussy."

    menu:
        "Anal creampie":
            with vpunch
            "Roaring, I slammed my cock balls-deep inside her ass and erupted at the same time."
            with vpunch
            "Holding her firmly down, I pumped semen inside her ass until I had spent every drop."
            scene ep004_quarters_jade_behind_creampie with flash
            with flash
            "I allowed her to collapse on top of me, warm sticky cum dripping from her asshole."
        "Swallow":
            "Roaring, I withdrew my cock and pulled her head towards me."
            scene ep004_quarters_jade_behind_swallow with flash
            with flash
            "She gasped and I thrust my veined shaft inside her open mouth, coating her throat with warm sticky cum."
            "After swallowing my load, I allowed her to collapse on top of me."
        "Facial":
            "Roaring, I withdrew my cock and pulled her head towards me."
            scene ep004_quarters_jade_behind_facial with dissolve
            "She gasped and I directed my veined shaft at her face, promptly coating her with warm sticky cum."
            "After plastering my face with semen, I allowed her to collapse on top of me."
    scene ep004_quarters_jade_behind_post with dissolve
    j "Did I satisfy you, master?"
    c "Yes, Jade, you did."
    $ renpy.end_replay()
    j "I certainly didn’t expect you to be so bold, master."
    menu:
        "Apologize [JadeLovePath]":
            $ ep004_jade_apologize = True
            c "Sorry, I didn’t know what came over me."
            scene expression eye_blink("images/ep004/ep004_quarters_jade_behind_post_smile") with dissolve
            j "That’s okay."
            j "I must admit that it hurt in the beginning, but later..."
            j "You had such power over me."
            j "It was so different from what we ever did before."
            j "But I liked it."
            j "I liked it a lot."
            c "Be careful what you wish for, Jade."
            j "Hah, I know, but next time I’ll be prepared."
            c "Will you now?"
            scene expression eye_blink("images/ep004/ep004_quarters_jade_behind_post_alt") with dissolve
            "I slapped her teasingly across the buttocks and we fell asleep after that brief exchange."
        "Don’t apologize [JadeSubPath]":
            c "You’re my slave, Jade, I can do whatever I want with you."
            scene expression eye_blink("images/ep004/ep004_quarters_jade_behind_post_serious") with dissolve
            j "So I am, master."
            j "Will you be using me again like this?"
            c "Maybe, if I feel like it."
            j "I’ll be ready for you, master."
            c "I’m counting on it."
            c "Now go."
            j "Yes, master."
    return

label ep004_jade_sex_soft:
    if not _in_replay:
        $ ep004_jade_sex_soft = True

    scene ep004_quarters_jade_naked with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "With one swift motion Jade unlaced her skirt and top and let them fall to the floor."
    "She stood naked before me, ready for anything."
    scene ep004_quarters_jade_cock_grab with dissolve
    "I laid back and she crept on top of me, grabbing my cock in her soft hands."
    "Jade had me erect in seconds, jerking my cock in her tight fist."
    scene ep004_quarters_jade_cock_grab_alt with dissolve
    "Touching the exposed head with the tips of her fingers she nearly made me cum."
    scene ep004_quarters_jade_cock_grab_lick with dissolve
    "Instead she waited and lapped up the precum that flowed freely."
    j "Do you want to fuck me, master?"
    c "Yes, I do Jade!"
    scene ep004_quarters_jade_cowgirl_penetrate with dissolve
    "The girl squatted on top of me and guided my veined shaft inside her cunt."
    "She looked at me in delight as the entire length disappeared inside her wet slit."
    j "Mmmm, [p_name]!"
    show ep004_quarters_jade_cowgirl with dissolve
    "Holding her by the waist I urged her to pleasure me and she began to rock back and forth."
    "Her tight pussy stimulated my cock perfectly as she fucked me with ever increasing speed."
    scene ep004_quarters_jade_cowgirl_alt with dissolve
    "Jade’s body slammed down on me as she rode me cowgirl, my balls hitting her ass."
    "When my cock slipped from her wet gash, she bit her lip and turned around, offering me a view of her ass."
    scene ep004_quarters_jade_reverse_cowgirl with dissolve
    "The girl lowered herself on top of my dick again, slipping it past her swollen lower lips."
    "The juices from her cunt streamed down my throbbing shaft as she bounced her body up and down."
    scene ep004_quarters_jade_reverse_cowgirl_alt with dissolve
    "I couldn’t resist playing with her ass and ran a finger between her ass cheeks."
    j "Mmmm!"
    "Emboldened by her moans I pushed my finger against the delicate folds of her anus."
    scene ep004_quarters_jade_anal_finger with dissolve
    "Jade started fingering her pussy while I slipped a digit inside her anus."
    scene ep004_quarters_jade_anal_finger_alt with dissolve
    "The girl was fingered front and back now and seemed to enjoy the sensation thoroughly."
    c "Do you want me to go further, Jade?"
    j "Yes!{w} Yes please!"
    "Lifting Jade off my cock I allowed her to get on all fours."
    scene ep004_quarters_jade_behind_penetrate with dissolve
    "One hand pressed against her lower back, I pressed my cock against her opening."
    "Jade and I had tried anal before, mostly using fingers and toys."
    "One attempt ended in mutual discomfort, as Jade couldn’t adjust to my girth."
    "This time seemed to be different for both of us."
    scene ep004_quarters_jade_behind_penetrate_ass_alt with dissolve
    "Jade seemed to be completely relaxed and my dick was slick with her juices so the tip slid easily inside her rectum."
    "She bit her lip as I pushed the entirety of my veined shaft slowly into her asshole."
    scene ep004_quarters_jade_behind_penetrate_ass_smile with dissolve
    j "I f-feel s-so f-full, [p_name_short]!"
    c "Do you want me to fuck your ass?"
    j "Yes!"
    j "Fuck my ass, please!"
    show ep004_quarters_jade_behind_penetrate_ass_fuck with dissolve
    "Jade moaned and held on to the bed tightly as I began to thrust back and forth."
    "As I fucked her butt she relaxed and gave in to the sensation of her ass being filled with a thick cock."
    scene ep004_quarters_jade_behind_penetrate_ass_fuck_alt with dissolve
    "Her asshole was still very tight, but I no longer felt restricted in my movements, so I picked up the pace."
    "With ever increasing speed I fucked her ass and her soft moans turned into groans of true pleasure."
    scene ep004_quarters_jade_behind_penetrate_ass_cowgirl with dissolve
    "Trying for another position, I grabbed Jade by the waist and hauled her on top of me as I lay down on the bed."
    "She was now squatting on top of me, my throbbing shaft still rooted inside her rectum."
    show ep004_quarters_jade_behind_penetrate_ass_cowgirl_alt with dissolve
    "Deliriously, Jade moved her ass up and down on my cock."
    "Holding her waist I complemented her movements by thrusting my hips upward, penetrating her ass even more deeply."
    "My balls slapped against her wet cunt as I fucked her asshole like it was her pussy."

    menu:
        "Anal creampie":
            with vpunch
            "Roaring, I slammed my cock balls-deep inside her ass and erupted at the same time."
            with vpunch
            "Holding her firmly down, I pumped semen inside her ass until I had spent every drop."
            scene ep004_quarters_jade_behind_creampie with flash
            with flash
            "She collapsed on top of me, warm sticky cum dripping from her asshole."
        "Swallow":
            "Roaring, I withdrew my cock and pulled her head towards me."
            scene ep004_quarters_jade_behind_swallow with flash
            with flash
            "She gasped and I thrust my veined shaft inside her open mouth, coating her throat with warm sticky cum."
            "After swallowing my load with a broad smile and collapsed on top of me."
        "Facial":
            "Roaring, I withdrew my cock and pulled her head towards me."
            scene ep004_quarters_jade_behind_facial with dissolve
            "She gasped and I directed my veined shaft at her face, promptly coating her with warm sticky cum."
            "After plastering my face with semen, she collapsed on top of me with a broad smile."
    scene ep004_quarters_jade_behind_post with dissolve
    j "That was something else."
    c "It sure was."
    scene expression eye_blink("images/ep004/ep004_quarters_jade_behind_post_smile") with dissolve
    j "I didn’t know it could be so...{w} You know...{w} So intense."
    scene expression eye_blink("images/ep004/ep004_quarters_jade_behind_post_alt") with dissolve
    "Jade kissed me and we fell asleep after that brief exchange."
    $ renpy.end_replay()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
