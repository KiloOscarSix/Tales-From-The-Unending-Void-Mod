
image ep004_ha_quarters_breasts_alt = Movie(play="movies/ep004/ep004_ha_quarters_breasts_alt.webm")
image ep004_ha_quarters_doggy_up_side = Movie(play="movies/ep004/ep004_ha_quarters_doggy_up_side.webm")
image ep004_ha_quarters_doggy_up = Movie(play="movies/ep004/ep004_ha_quarters_doggy_up.webm")
image ep004_ha_quarters_fuck_side = Movie(play="movies/ep004/ep004_ha_quarters_fuck_side.webm")
image ep004_ha_quarters_fuck = Movie(play="movies/ep004/ep004_ha_quarters_fuck.webm")
image ep004_lu_jerk = Movie(play="movies/ep004/ep004_lu_jerk.webm")
image ep004_lu_ca_fuck_jerk_alt = Movie(play="movies/ep004/ep004_lu_ca_fuck_jerk_alt.webm")
image ep004_lu_ca_penetrate_face = Movie(play="movies/ep004/ep004_lu_ca_penetrate_face.webm")
image ep004_lu_ca_penetrate_side = Movie(play="movies/ep004/ep004_lu_ca_penetrate_side.webm")
image ep004_lu_ca_penetrate_alt = Movie(play="movies/ep004/ep004_lu_ca_penetrate.webm")
image ep004_quarters_jade_behind_penetrate_ass_fuck = Movie(play="movies/ep004/ep004_quarters_jade_behind_penetrate_ass_fuck.webm")
image ep004_quarters_jade_behind_penetrate_ass_cowgirl_alt = Movie(play="movies/ep004/ep004_quarters_jade_behind_penetrate_ass_cowgirl_alt.webm")
image ep004_quarters_jade_cock_mouth = Movie(play="movies/ep004/ep004_quarters_jade_cock_mouth.webm")
image ep004_quarters_jade_cowgirl = Movie(play="movies/ep004/ep004_quarters_jade_cowgirl.webm")


label episode004:
    $ save_name = "Episode 4"

    $ ep004_ziv_bargain = False
    $ ep004_na_hug = False
    $ ep004_n_ask = False
    $ ep004_ziv_derisive = False
    $ ep004_skarak = False
    $ ep004_lu_truth = False
    $ ep004_lu_lick = False
    $ ep004_lu_suck = False
    $ ep004_tu_polite = False
    $ ep004_tu_contest = False
    $ ep004_hannah_sex = False
    $ ep004_ha_creampie = False

    play music [ "music/unnatural-situation.ogg" ] fadeout 4 fadein 1.0

    scene black with fade
    centered "{=chapter_heading}EPISODE 4{/=chapter_heading}"

    scene ep004_calista_apartment_walking with dissolve
    call location_screen ("Proxima Centauri Orbital IV", True) from _call_location_screen_21

    $ bl_name = "Woman"

    scene ep004_calista_apartment_closeup with dissolve
    bl "Calista Szuzume, you truly look like shit."
    ca "Fuck off."
    bl "Are you even allowed to have this much liquor in your apartment?"
    scene ep004_calista_apartment with vpunch
    ca "Leave!"
    bl "No, I won’t."
    scene expression eye_blink("images/ep004/ep004_calista_apartment_bl") with dissolve
    bl "I was sent here, we have business to discuss."
    bl "Didn’t know you were in such a state, though."
    scene ep004_calista_apartment_ca_sad with dissolve
    ca "Yeah, well, having to kill your own children apparently does that to you."
    bl "Attempting to kill would be a more precise way of putting it."
    bl "You made a mess of things, Commander Szuzume."
    scene ep004_calista_apartment_ca with dissolve
    ca "We were completely blindsided by the attack on Lanan, even the top brass were surprised."
    scene expression eye_blink("images/ep004/ep004_calista_apartment_bl") with dissolve
    bl "That’s the official story, certainly."
    scene ep004_calista_apartment_ca with dissolve
    ca "What?"
    ca "Do you know something?"
    scene expression eye_blink("images/ep004/ep004_calista_apartment_bl_serious") with dissolve
    bl "No, just some vague musings, baseless insinuations."
    bl "Also, not why I am here."
    scene ep004_calista_apartment_ca_angry with dissolve
    ca "Why are you here, other than to annoy the fuck out of me?"
    bl "I’m sure you understand that the higher-ups needed a scapegoat and that you were the perfect candidate."
    scene ep004_calista_apartment_ca_serious with dissolve
    ca "Yes."
    bl "They haven’t discarded you completely however and are offering you a chance to make it right."
    ca "So why are they sending a Bloodhound to be the messenger?"

    $ bl_name = "Bloodhound"
    scene expression eye_blink("images/ep004/ep004_calista_apartment_bl_smile") with dissolve
    bl "You figured me out already?"
    ca "To be honest, it wasn’t hard..."
    bl "I wasn’t trying to hide the fact, we’re allowed to operate in the open if we want to."
    scene ep004_calista_apartment_ca_laugh with dissolve
    ca "When you have to run petty errands?"
    scene expression eye_blink("images/ep004/ep004_calista_apartment_bl_smile") with dissolve
    bl "Have I told you before that the drink unleashes the worst in you?"
    bl "I’m to find the deserters you failed to terminate."
    scene ep004_calista_apartment_ca_serious with dissolve
    ca "To finish the job?"
    bl "To bring them in, preferably."
    ca "Again I ask you, why are you here?"
    scene expression eye_blink("images/ep004/ep004_calista_apartment_bl_smile") with dissolve
    bl "You’re going to answer all of my questions."
    scene ep004_calista_apartment_ca_serious with dissolve
    ca "And if I don’t?"
    scene expression eye_blink("images/ep004/ep004_calista_apartment_bl_smile_alt") with dissolve
    bl "In that case you can waste away in this nice apartment until they decide to arrest you on some bullshit charges and lock you away for a long time."
    bl "On the other hand, if you help me, you might see Céline and Kit again."
    bl "Maybe they’ll get reduced sentences..."
    bl "We already know from your report that the main instigator of the desertion is that boy, [p_name]."
    scene ep004_calista_apartment_ca_serious_alt with dissolve
    ca "Just read their personnel files, everything is in there."
    bl "I already have, but you also know that a file on someone doesn’t tell the whole story."
    scene ep004_calista_apartment_ca_bl_sit with dissolve
    bl "Why don’t we have a chat?"
    ca "Fine."
    ca "Where do I start?"
    bl "By pouring me a drink."
    scene black with fade

    play music [ "music/simplex.ogg" ] fadeout 4 fadein 1.0

    python:
        codex_bloodhound = add_codex_entry(
            Codex,
            "Characters",
            "Bloodhound",
            [
                "An operative from an elite force in the Sovereignty military who comes to visit Calista Szuzume to find out more about [p_name] and his band of deserters in order to hunt them."
            ],
            "images/codex/Bloodhound.webp"
        )

    scene ep004_bastard_ship with dissolve
    call location_screen ("Near Verdant Station", True) from _call_location_screen_22

    scene ep003_bastard_av_th_alt with dissolve
    c "Well, let’s see what we can do in five minutes."
    c "First we’re going to open up that shuttle."
    scene ep004_bastard_av with dissolve
    av "The button for the hatch isn’t responding."
    c "The whole thing was disabled by His Eternal Holy Whatever, so likely all the electronics are fried."
    c "Other suggestions besides pushing the button?"
    av "Shooting?"
    scene ep004_bastard_th with dissolve
    th "Not advisable against an armored shuttle inside a cargo hold..."
    th "Let me try something."
    scene ep004_bastard_th_shuttle with dissolve
    "Thyia pried open the button console and started ripping wires loose."
    scene ep004_bastard_speaker with dissolve
    man "Four minutes."
    "When she found the ones she needed, Thyia held them together causing a spark."
    "Slowly, the door hissed open."
    scene expression eye_blink("images/ep004/ep004_bastard_zi") with dissolve
    zi "Hi, [p_name]."
    c "Ziv?"
    zi "None other."
    scene ep004_bastard_speaker with dissolve
    man "Three minutes."
    scene expression eye_blink("images/ep004/ep004_bastard_zi_serious") with dissolve
    c "Why did that ship with the long-ass name disable your shuttle, Ziv?"
    c "What do they want with you?"
    zi "They don’t want me, they want Raene."
    c "She’s a princess after all?"
    zi "No, she isn’t."
    c "Hierophant Sacleus, also known as His Holiness, isn’t the equivalent of a king, or an emperor, or whatever?"
    scene expression eye_blink("images/ep004/ep004_bastard_zi_unsure") with dissolve
    zi "Well, if you put it that way..."
    c "I fucking hate debating semantics."
    av "We’re on a clock too."

    menu:
        "Bargain with Ziv [gr]\[Ziv Bargain\] \[Recommended\]":
            $ ep004_ziv_bargain = True
            c "Tell me one good reason not to hand you over."
            scene expression eye_blink("images/ep004/ep004_bastard_zi_serious") with dissolve
            c "You fucking lied to me, Ziv."
            zi "I had my reasons."
            c "I’m sure you did."
            c "But despite the guy on the other end of the line sounding like a massive dick, I’m not hearing any arguments why we should save you."
            scene expression eye_blink("images/ep004/ep004_bastard_zi_unsure") with dissolve
            zi "Doing it out of the kindness of your heart is out of the question, I reckon?"
            c "Yes."
            c "Completely."
            scene expression eye_blink("images/ep004/ep004_bastard_zi_serious") with dissolve
            zi "I have some money."
            c "That’s a start, how much?"
            zi "5000."
            c "Okay..."
            c "What else?"
            scene expression eye_blink("images/ep004/ep004_bastard_zi_serious_alt") with dissolve
            zi "A location."
            c "A location..."
            scene ep004_bastard_speaker with dissolve
            man "Two minutes."
            scene expression eye_blink("images/ep004/ep004_bastard_zi_serious_alt") with dissolve
            zi "Have you ever heard of the Tubloshi?"
            c "A little."
            c "Lumbering, power-hungry space grunts, right?"
            scene expression eye_blink("images/ep004/ep004_bastard_zi_serious") with dissolve
            zi "Yes, a noble race of interstellar warriors."
            zi "Honor is everything to them."
            zi "Their last great hero, Kyl Tavort, died during what’s known as the Fifth Glorious Campaign."
            scene expression eye_blink("images/ep004/ep004_bastard_zi_serious_alt") with dissolve
            c "Some messy interplanetary genocide, I take it?"
            zi "The Tubloshi attempted to retrieve the bodies of their fallen warriors after the battle, but Tavort’s body was never found."
            zi "But I know where his body is kept."
            c "And that’s worth a lot of money to the Tubloshi?"
            zi "Not being able to apply the last funeral rites to one of their greatest heroes in recent history is something that’s been a thorn in the side of the Tubloshi for years now."
            zi "It has tarnished their account of the Fifth Glorious Campaign."
            c "So if we were to set everything right by retrieving the body for them, they would be very grateful?"
            python:
                codex_tubloshi = add_codex_entry(
                    Codex,
                    "Characters",
                    "Tubloshi",
                    [
                        "A warrior race known for taking pride in their honor and hero worship. The Tubloshi mounted several military campaigns of which the Fifth Glorious Campaign was the last."
                    ]
                )
            scene expression eye_blink("images/ep004/ep004_bastard_zi_serious") with dissolve
            zi "Exactly."
            scene ep004_bastard_speaker with dissolve
            man "One minute."
            scene expression eye_blink("images/ep004/ep004_bastard_zi_serious") with dissolve
            c "Can you contact the Tubloshi and negotiate a contract with them?"
            zi "I can."
            c "Good."
            c "Now, let’s tell the annoying man in the big ship something that makes him go away."
            c "What do we do to blow him off?"
        "Take them in":
            c "I’m sure you and Raene have good reasons to run from His Holiness."
            c "And the guy on the other end of the line kinda sounds like a massive dick."
            scene expression eye_blink("images/ep004/ep004_bastard_zi_smile") with dissolve
            c "So what do we do to blow them off?"

    play music "music/hiding-your-reality.ogg" fadein 1.0 fadeout 4

    scene expression eye_blink("images/ep004/ep004_bastard_th_unsure") with dissolve
    th "We could send them the empty shuttle."
    c "Would that buy us enough time?"
    th "It would if I rigged the shuttle with an EMP grenade."
    c "Nice, that would take out a lot of their electronics."
    c "How fast can you set it up?"
    scene expression eye_blink("images/ep004/ep004_bastard_th_smile") with dissolve
    th "Couple of minutes."
    c "Okay, I’ll stall him."
    scene ep004_bastard_c_comms with dissolve
    c "Captain of the “His Eternal Holy Light”, please standby, we are ready to transfer the shuttle to you."
    man "Acknowledged."
    scene ep004_bastard_th_av_shuttle with dissolve
    "I decided to see if I could stretch the moment as long as possible, to give Thyia time to complete rigging the shuttle."
    scene ep004_bastard_av_ra_shuttle with dissolve
    "Aven helped Ziv pull Raene out of the shuttle."
    "Unfortunately, the captain of the other ship was rather impatient."
    scene ep004_bastard_speaker with dissolve
    man "Iron Bastard, why haven’t you released the shuttle yet?"
    scene ep004_bastard_c_comms with dissolve
    c "Our cargo bay door is malfunctioning, we’re running diagnostics."
    scene ep004_bastard_speaker with dissolve
    man "Need I remind you that you’re not in the position to play games with us..."
    scene ep004_bastard_th_shuttle_closeup with dissolve
    c "Almost done, Thyia?"
    th "Just a minute."
    scene ep004_bastard_c_comms with dissolve
    c "No need to worry “His Eternal Holy Light”, my mechanic is on the job."
    "They didn’t respond to that and for several seconds the fear of being hit by one of their missiles in retaliation was palpable."
    scene ep004_bastard_th_shuttle_smile with dissolve
    th "Done!"
    "We hastily evacuated the cargo bay and I told Céline to initiate the release of the shuttle."
    scene ep004_bastard_c_comms with dissolve
    c "“His Eternal Holy Light”, opening cargo bay door and transferring shuttle now."
    man "Acknowledged."
    scene ep004_bastard_shuttle_ship with dissolve
    "For several minutes we watched the empty shuttle float towards the larger ship."
    "One of its cargo bay doors opened and the vessel was towed inside the belly of “His Eternal Holy Light That Graces Our Paltry Existence A Thousandfold”."
    scene expression eye_blink("images/ep004/ep004_bastard_ce") with dissolve
    c "Ready to make a run for it?"
    ce "Yup."
    scene ep004_bastard_ship with dissolve
    man "Captain of the Iron Bastard, I hereby confirm that the..."
    with vpunch
    with hpunch
    "The rest of his words ended in static."
    "No explosion was visible on the outside of the ship, but Thyia’s grenade must have gone off as planned."
    scene expression eye_blink("images/ep004/ep004_bastard_ce") with dissolve
    c "Now would be a good time."
    scene ep004_bastard_ship_escape with dissolve
    "Céline kicked the engine into overdrive and we sped away from the cruiser."
    scene black with fade
    "No threats came over the comms and we were out of their range and on our way to a jump gate in just a few minutes."

    if not ep004_ziv_bargain:
        scene expression eye_blink("images/ep004/ep004_bastard_ziv") with dissolve
        zi "Thank you, I speak for Raene to, when I say that this means a lot."
        zi "Hierophant Sacleus is a man not to be trifled with."
        c "He’s Raene’s father?"
        scene expression eye_blink("images/ep004/ep004_bastard_ziv_serious") with dissolve
        zi "Yes."
        c "And you’ve kidnapped his daughter?"
        zi "No, Raene came of her own volition."
        zi "The Hierophant doesn’t respect her wishes and getting her back on the estate on Verdigris has become an obsession of sorts."
        python:
            codex_sacleus = update_codex_entry(codex_sacleus, None,
                [
                    "Hierophant Sacleus is the highest ranking member of an unknown religious order on Verdigris V and father of Raene. He's also the owner of the vessel “His Eternal Holy Light That Graces Our Paltry Existence A Thousandfold”."
                ]
            )
        c "I asked you directly if she wasn’t a princess."
        c "She technically isn’t, but you know what I meant by that."
        scene expression eye_blink("images/ep004/ep004_bastard_ziv_worry") with dissolve
        zi "I did."
        zi "Look, I was desperate."
        zi "My people were able to hide Raene for quite some time among the populace of Verdigris."
        zi "But arranging transport took such a long time and the Hierophant had launched an aggressive campaign to get Raene back."
        zi "When you responded to my notice I couldn’t believe my luck."
        scene expression eye_blink("images/ep004/ep004_bastard_ziv_serious") with dissolve
        c "So you lied to me."
        scene expression eye_blink("images/ep004/ep004_bastard_ziv_doubt") with dissolve
        zi "Would you have taken the job if I’d told you the truth?"
        c "Maybe...{w} I don’t know."
        scene expression eye_blink("images/ep004/ep004_bastard_ziv_serious") with dissolve
        zi "In any case, for what it’s worth, sorry I lied to you."
        zi "We’ll hop off on the next station and be out of your hair."
        zi "If you run into the Hierophant’s men again, you can say you were held at gunpoint or something..."
        c "They’d buy that?"
        scene expression eye_blink("images/ep004/ep004_bastard_ziv_doubt") with dissolve
        zi "They probably don’t even care."
        zi "I’ve heard that most of the Hierophant’s men are quite sick and tired of their master’s single-minded quest for his daughter."
        zi "That doesn’t mean they’ll stop pursuing us, but they probably won’t care about the people we’ve had contact with."
        c "That sounds vaguely reassuring, but I guess the chances we run into them are pretty slim."
        scene expression eye_blink("images/ep004/ep004_bastard_ziv") with dissolve
        zi "I’d say so."
        zi "They’ll take some time to recover from that pulse grenade Thyia set up for them."
        c "That worked out quite well."
        c "We’re off to a very small asteroid base next and there’s no clear plan yet what we’re to do after."
        c "There are still some empty quarters on the aft of the ship, so make yourselves at home there."
        zi "We will."
        zi "Thank you."
    else:
        scene expression eye_blink("images/ep004/ep004_bastard_ziv_serious") with dissolve
        zi "Your plan seems to have worked, they’ll take some time to recover from that pulse grenade Thyia set up for them."
        c "That’s the idea."
        c "Listen, we’re off to a very small asteroid base next and there’s no clear plan yet what we’re to do after."
        c "Once we’ve finished our business at the asteroid base, we’ll might go find Kyl Tavort’s last resting place."
        zi "That works for me."
        c "Good."
        c "In the mean time, you can and Raene take one of the empty quarters on the aft of the ship."
        zi "Thanks."

    play music "music/ephemera.ogg" fadein 1.0 fadeout 4

    scene ep004_asteroid_base with dissolve
    call location_screen ("Hreir Asteroid Base, Approach", True) from _call_location_screen_23

    "Using the navigational data we received from Hreir, the Iron Bastard cut it’s way through the asteroid field."
    "It wasn’t until we docked that something began to feel off."
    scene ep004_asteroid_av_na with dissolve
    c "No security bots to greet us..."
    av "Wait here, I’m going to get us some protection from the ship."
    na "You know how Karan is about firearms on his base, Aven."
    av "We’ll worry about that later."
    scene ep004_asteroid_av_na_guns with dissolve
    "Aven returned with two pistols and we made our way into the base."
    "All automatic doors opened without fail, but we all couldn’t shrug that uncomfortable feeling, perhaps caused by the eerie quiet of the base."
    scene ep004_asteroid_bots with dissolve
    "When we encountered the smoldering remnants of two of the security bots, we knew for sure something terrible had happened."
    na "Karan?"
    scene ep004_asteroid_ka with dissolve
    av "Fuck."
    av "He’s gone, Nadya."
    scene ep004_asteroid_ka_table with dissolve
    "Karan had died a violent death, tied down on his own examination table."
    "The two remaining bots lay slumped against the wall, black holes of some kind of energy weapon piercing their armor."
    scene expression eye_blink("images/ep004/ep004_asteroid_na") with dissolve
    na "Who could do such a thing?"
    c "Maybe one of those companies he pissed off by prying into their affairs?"
    na "Could be."
    scene expression eye_blink("images/ep004/ep004_asteroid_av") with dissolve
    av "I’ll go find something to cover him with."
    scene expression eye_blink("images/ep004/ep004_asteroid_na") with dissolve
    na "I can’t believe it, he was always so careful..."
    c "He was never attacked before?"
    scene expression eye_blink("images/ep004/ep004_asteroid_na_unsure") with dissolve
    na "Not that I know of."
    na "Threats, yes, lots of them."
    scene expression eye_blink("images/ep004/ep004_asteroid_na") with dissolve
    na "Such a bright mind..."

    menu:
        "[gr]Hug her":
            $ ep004_na_hug = True
            scene ep004_asteroid_hug with dissolve
            "I took Nadya in my arms and I held her in silence, until Aven returned with a sheet she found somewhere"
        "Wait for Aven":
            "We waited in silence, until Aven returned with a sheet she found somewhere."

    scene ep004_asteroid_av_na_c with dissolve
    "Nadya covered him up while Aven and I looked around in the lab."
    scene ep004_asteroid_av_bot with dissolve
    av "These look like awfully precise shots."
    av "Two in the torso, one in the head."
    av "Wait a minute..."
    av "Where’s the third body?"
    c "There are two lying here, those are the only ones."
    scene ep004_asteroid_av_head with dissolve
    av "There’s another head here on the table."
    c "So?"
    c "Maybe Hreir was working on it?"
    av "Maybe, but the memory core might still be intact."
    av "Might tell us something."
    c "I’m sure Thyia and Jade can find that out for us."
    scene expression eye_blink("images/ep004/ep004_asteroid_na") with dissolve
    na "We should give Karan a proper burial first."
    na "Could you help me move him to an airlock?"
    na "I think he’d like the asteroid field as his final resting place."
    scene ep004_asteroid_body with dissolve
    "Hreir weighed next to nothing, so getting him to the nearest airlock didn’t pose much of a problem."
    "Nadya asked us to leave her alone for a moment, so she could speak a few words in private."
    scene ep004_asteroid_body_space with dissolve
    "When the alarm of the air lock sounded we knew that Nadya gave him the final honors."
    scene black with fade
    "Back at the ship Jade and Thyia went on to work on the bot’s head, to see if any information could be pried from it."
    scene ep004_ship_th_ja with dissolve
    "I had Céline check the station’s records as well, to see if any ships had docked in the time we were away."
    "The logs showed nothing, so someone had carefully covered their tracks."

    call ep004_conversations from _call_ep004_conversations

    play music "music/ephemera.ogg" fadein 1.0 fadeout 4

    "A couple of hours passed until an excited Jade sent me a message to come find her in the engine room."
    scene ep004_ship_th_ja_happy with dissolve
    j "We did it!"
    j "Thyia had a hard time getting it out of the skull, as it was already damaged, but we managed to retrieve some information from the data core."
    th "It’s not much..."
    scene ep004_ship_bot with dissolve
    "The bot’s eyes began to glow and we heard Karan’s voice."
    ka "Nadya."
    $ man_name = "Bot"
    man "I hope this message gets to you, because they’re finally coming for me."
    man "I don’t know who it is, but they’re nearly through the security doors."
    man "Maybe it has something to do with you, or maybe it’s just my time."
    man "It doesn’t matter now."
    man "The warrior women you’re searching for are the Acarhyn, product of an illicit genetics experiment."
    man "The location of their home planet is unknown, but Ranimo Cetruvar probably knows."
    man "Nadya, you’ve been a loyal friend, I-"
    man "*Static*"
    python:
        codex_warrior_women = update_codex_entry(codex_warrior_women, "Acarhyn",
            [
                "First encountered on Lanan P-10 and identified by Karan Hreir just before his unfortunate demise. The Acarhyn launched a full-scale attack on TGN personnel on Lanan P-10, abducting a great many of them.",
                "The women appear muscular and wear elaborate armor and seem to prefer fighting with relatively crude melee weapons."
            ]
        )

    scene expression eye_blink("images/ep004/ep004_ship_n_sad") with dissolve
    c "Acarhyn..."
    c "Are you okay, aunt Nadya?"
    scene expression eye_blink("images/ep004/ep004_ship_n") with dissolve
    na "Yes, yes I am."
    na "It’s just...{w} He sounded so frightened."
    scene expression eye_blink("images/ep004/ep004_ship_n_sad") with dissolve
    "We were all silent for a moment, until Aven spoke up."
    scene ep004_ship_av with dissolve
    if game.is_special:
        av "Have you ever heard of those Acarhyn, mother?"
    else:
        av "Have you ever heard of those Acarhyn, Nadya?"
    scene ep004_ship_n with dissolve
    na "No, I haven’t."
    c "And Ranimo Cetruvar?"
    scene ep004_ship_av with dissolve
    av "A fellow scientist maybe?"
    scene ep004_ship_n with dissolve
    na "Could be, but I’ve never heard of the name."
    scene expression eye_blink("images/ep004/ep004_ship_th") with dissolve
    th "I have."
    th "Guy’s infamous."
    th "I’m amazed you all don’t know him."
    th "Cetruvar was the Sovereignty Minister of Information for years."
    scene ep004_ship_av with dissolve
    av "Right, isn’t he the one who got away?"
    th "Exactly."
    c "I haven’t got a clue what you’re talking about."
    scene expression eye_blink("images/ep004/ep004_ship_th") with dissolve
    th "Ranimo Cetruvar served as Minister of Information for years and became one of the most powerful men in the Sovereignty."
    th "After a couple attempts on his life, I think he finally decided he had enough and disappeared all of a sudden, taking a lot of state secrets with him."
    th "Years later he resurfaced, living like a flamboyant king in a fucking castle on a moon far outside Sovereignty space."
    python:
        codex_cetruvar = add_codex_entry(
            Codex,
            "Characters",
            "Ranimo Cetruvar",
            [
                "Former Minister of Information in the Sovereignty turned information broker living like a king on a heavily fortified moon. Cetruvar should have more information on the possible location of the Acarhyn home planet."
            ]
        )

    c "Ballsy, why doesn’t the Sovereignty just blow him and his moon up?"
    scene expression eye_blink("images/ep004/ep004_ship_th_smile") with dissolve
    th "There’s no telling what dirt Cetruvar has on the rich and powerful."
    th "He acts like an information broker now, so I guess he’s useful to many."
    scene expression eye_blink("images/ep004/ep004_ship_th_unsure") with dissolve
    th "You never heard of him?"
    c "Not a word."
    th "Guess the Sovereignty quickly swept that scandal under the rug..."
    th "Still, he's famous all over the galaxy because of his parties, one of the few things the elite get excited about."
    c "Is he our only option?"
    c "Surely we can think of something else than some slimy ex-Sovereignty cunt, who likes to throw cocktail parties and suck up to the rich?"
    scene expression eye_blink("images/ep004/ep004_ship_n_doubt") with dissolve
    na "I could ask around to see if anybody knows something about a species called Acarhyn."
    th "Me too, but is all this something we’d like everybody to know?"
    scene ep004_ship_av with dissolve
    av "Good point."
    av "For all we know we expose them to the clean-up crew who killed Hreir."

    menu:
        "[gr]Ask around":
            $ ep004_n_ask = True
            c "We have to take that risk."
            c "Nadya, could you ask around, discretely?"
            scene ep004_ship_n_doubt with dissolve
            na "I’ll do my best."
            c "Good, let’s meet here again after your contacts have responded."
            scene ep004_asteroid_exit with dissolve
            "We made our way out of the asteroid belt and waited for Nadya to contact her colleagues."
            scene black with fade
            "After several hours Nadya returned from her quarters, wearing a worried look on her face."
            scene ep004_cockpit_n with dissolve
            na "Nothing, as I feared."
            c "Fuck."
            na "There’s nothing in the official records about them."
            scene ep004_cockpit_av with dissolve
            av "So that means Cetruvar is our only option."
            c "Seems like it."
            c "Let’s go find the fucker."
            scene expression eye_blink("images/ep004/ep004_cockpit_th") with dissolve
            c "Do you have the location of that moon he’s living on, Thyia?"
            th "Yes, it’s called Almagest in the Psi1 Draconis system."
            c "Cé, please set course for Almagest."
            scene expression eye_blink("images/ep004/ep004_cockpit_th_unsure") with dissolve
            th "And then what?"
            th "You can’t just waltz in there and demand to speak to Cetruvar."
            th "I mean, you probably won’t be shot on sight, but there’s no way you’d even be able enter orbit."
            th "He doesn’t like unannounced guests."
            c "Maybe he’ll just have to adjust this once, or do you have another idea?"
            scene ep004_cockpit_av with dissolve
            av "Didn't you say he was famous for his parties, Thyia?"
            scene expression eye_blink("images/ep004/ep004_cockpit_th") with dissolve
            th "Exactly, they occur frequently enough for us to attend one from what I’ve heard."
            c "Could you get us in?"
            th "Maybe, I’d need to contact a few people."
            c "Good, do so."
            scene expression eye_blink("images/ep004/ep004_cockpit_th_unsure") with dissolve
            th "But [p_name]..."
            c "Yes?"
            c "This is going to be about money, isn’t it?"
            th "Yes and lots of it."
            th "There’s bribes to consider, payment for the invitation, information on Cetruvar’s castle, not to mention pretty party dresses for all of us."
            c "Pretty dresses?"
            c "I’m happy with a tuxedo, thank you very much."
            scene expression eye_blink("images/ep004/ep004_cockpit_th") with dissolve
            if ep004_ziv_bargain:
                c "I'll ask Ziv to establish contact with the Tubloshi and share the location of the body with Céline so we can get there as soon as possible."
            else:
                c "I guess we’ll be doing cargo runs for the rest of our lives..."
            c "Could you draw up an estimation of the costs, Thyia?"
            th "On it."
        "Go after Cetruvar":
            c "Agreed, it’s too dangerous to involve others."
            c "Let’s go find Cetruvar."
            c "Do you have the location of that moon he’s living on, Thyia?"
            scene expression eye_blink("images/ep004/ep004_ship_th") with dissolve
            th "Yes, it’s called Almagest in the Psi1 Draconis system."
            c "Cé, please set course for Almagest."
            scene expression eye_blink("images/ep004/ep004_ship_th_unsure") with dissolve
            th "And then what?"
            th "You can’t just waltz in there and demand to speak to Cetruvar."
            th "I mean, you probably won’t be shot on sight, but there’s no way you’d even be able enter orbit."
            th "He doesn’t like unannounced guests."
            c "Maybe he’ll just have to adjust this once, or do you have another idea?"
            scene ep004_ship_av with dissolve
            av "Those parties he throws seem like a good way in."
            scene expression eye_blink("images/ep004/ep004_ship_th") with dissolve
            th "Exactly, they occur frequent enough from what I’ve heard."
            c "Could you get us in?"
            th "Maybe, I’d need to contact a few people."
            c "Good, do so."
            scene expression eye_blink("images/ep004/ep004_ship_th_unsure") with dissolve
            th "But [p_name]..."
            c "Yes?"
            c "This is going to be about money, isn’t it?"
            th "Yes and lots of it."
            th "There’s bribes to consider, payment for the invitation, information on Cetruvar’s castle, not to mention pretty party dresses for all of us."
            c "Pretty dresses?"
            c "I’m happy with a tuxedo, thank you very much."
            scene expression eye_blink("images/ep004/ep004_ship_th_smile") with dissolve
            th "So money."
            if ep004_ziv_bargain:
                c "Luckily the Tubloshi might owe us a costly favor in the near future."
            else:
                c "I guess we’ll be doing cargo runs for the rest of our lives..."
            c "Could you draw up an estimation of the costs, Thyia?"
            th "On it."

            scene expression eye_blink("images/ep004/ep004_ship_ziv") with dissolve
            if ep004_ziv_bargain:
                c "Ziv, now would be a good time to establish contact with the Tubloshi."
                c "Could you provide Céline with the location where the body is supposed to be?"
                zi "I can, I’ll let you know when it’s set up."
            else:
                "Everyone left, but Ziv lingered by the door."
                c "Is there something on your mind Ziv?"
                zi "Yes, I might be able to help out."
                c "In what way?"
                zi "Solving the money problem."
                c "Keep talking."
                scene expression eye_blink("images/ep004/ep004_ship_ziv_unsure") with dissolve
                zi "Only if you agree to something."
                c "Haggling, Ziv, really?"
                zi "Just looking out for me and Raene."
                c "I guess that’s fair."
                c "So, what are you asking?"
                scene expression eye_blink("images/ep004/ep004_ship_ziv_serious") with dissolve
                zi "If the lead I tell you pans out, I’d like us to stay here on the ship for the foreseeable future."
                c "Deal."
                scene expression eye_blink("images/ep004/ep004_ship_ziv_smile") with dissolve
                zi "Good."
                zi "Have you ever heard of the Tubloshi?"
                c "A little."
                c "Lumbering, power-hungry space grunts, right?"
                zi "Yes, a noble race of interstellar warriors."
                zi "Honor is everything to them."
                zi "Their last great hero, Kyl Tavort, died during what’s known as the Fifth Glorious Campaign."
                c "Some messy interplanetary genocide, I take it?"
                scene expression eye_blink("images/ep004/ep004_ship_ziv_serious") with dissolve
                zi "The Tubloshi attempted to retrieve the bodies of their fallen warriors after the battle, but Tavort’s body was never found."
                zi "But I know where his body is kept."
                c "And that’s worth a lot of money to the Tubloshi?"
                scene expression eye_blink("images/ep004/ep004_ship_ziv") with dissolve
                zi "Not being able to apply the last funeral rites to one of their greatest heroes in recent history is something that’s been a thorn in the side of the Tubloshi for years now."
                zi "It has tarnished their account of the Fifth Glorious Campaign."
                c "So if we were to set everything right, by retrieving the body for them, they would be very grateful?"
                scene expression eye_blink("images/ep004/ep004_ship_ziv_smile") with dissolve
                zi "Exactly."
                c "Can you contact the Tubloshi and negotiate a contract with them?"
                zi "I can."
                c "Good, do so."
                c "Could you provide Céline with the location where the body is supposed to be?"
                zi "No problem."
                c "It looks like we’re going to need all the money we can get, from what Thyia said..."
                zi "I’ll let you know when I’ve made contact."
                scene black with fade

                python:
                    codex_tubloshi = add_codex_entry(
                        Codex,
                        "Characters",
                        "Tubloshi",
                        [
                            "A warrior race known for taking pride in their honor and hero worship. The Tubloshi mounted several military campaigns of which the Fifth Glorious Campaign was the last."
                        ]
                    )

    scene ep004_mess_ziv with dissolve
    if not ep004_ziv_bargain and ep004_n_ask:
        "I was busy talking details with Thyia about getting our party invitations from Cetruvar when Ziv walked in."
        zi "I heard you had some money troubles?"
        c "That's right."
        zi "I might have a solution."
        c "Keep talking."
        scene ep004_mess_ziv_unsure with dissolve
        zi "Only if you agree to something."
        c "Haggling, Ziv, really?"
        zi "Just looking out for me and Raene."
        c "I guess that’s fair."
        c "So, what are you asking?"
        scene ep004_mess_ziv_serious with dissolve
        zi "If the lead I tell you pans out, I’d like us to stay here on the ship for the foreseeable future."
        c "Deal."
        scene ep004_mess_ziv_smile with dissolve
        zi "Good."
        zi "Have you ever heard of the Tubloshi?"
        c "A little."
        c "Lumbering, power-hungry space grunts, right?"
        zi "Yes, a noble race of interstellar warriors."
        zi "Honor is everything to them."
        zi "Their last great hero, Kyl Tavort, died during what’s known as the Fifth Glorious Campaign."
        c "Some messy interplanetary genocide, I take it?"
        scene ep004_mess_ziv_serious with dissolve
        zi "The Tubloshi attempted to retrieve the bodies of their fallen warriors after the battle, but Tavort’s body was never found."
        zi "But I know where his body is kept."
        c "And that’s worth a lot of money to the Tubloshi?"
        scene ep004_mess_ziv with dissolve
        zi "Not being able to apply the last funeral rites to one of their greatest heroes in recent history is something that’s been a thorn in the side of the Tubloshi for years now."
        zi "It has tarnished their account of the Fifth Glorious Campaign."
        c "So if we were to set everything right, by retrieving the body for them, they would be very grateful?"
        scene ep004_mess_ziv_smile with dissolve
        zi "Exactly."
        c "Can you contact the Tubloshi and negotiate a contract with them?"
        zi "I've already done that."
        c "That's great!"
        zi "We are to meet them with the body at a specified location."
        zi "They didn’t sound excited, but the Tubloshi never betray much emotion."
        c "Could you provide Céline with the location where the body is supposed to be?"
        zi "No problem."
        c "It looks like we’re going to need all the money we can get..."
        c "Did you already come to a price with the Tubloshi?"
        zi "Yes, 100.000 credits upon successful delivery."
        c "Wow...{w} They really like that guy Tavort, don’t they?"
        zi "Mostly they don’t like leaving their heroes behind on the battlefield."
        c "Question is, will that be enough, Thyia?"
        scene ep004_mess_ziv_th with dissolve
        th "Yes, I think this will pay for much if not all of the costs of reaching Cetruvar."
        c "Good, let’s get going then."

        python:
            codex_tubloshi = add_codex_entry(
                    Codex,
                    "Characters",
                    "Tubloshi",
                    [
                        "A warrior race known for taking pride in their honor and hero worship. The Tubloshi mounted several military campaigns of which the Fifth Glorious Campaign was the last."
                    ]
                )
    else:
        zi "I spoke to them."
        zi "We are to meet them with the body at a specified location."
        zi "They didn’t sound excited, but the Tubloshi never betray much emotion."
        c "Did you come to a price?"
        zi "Yes, 100.000 credits upon successful delivery."
        c "Wow...{w} They really like that guy Tavort, don’t they?"
        zi "Mostly they don’t like leaving their heroes behind on the battlefield."
        c "Question is, will that be enough, Thyia?"
        scene ep004_mess_ziv_th with dissolve
        th "Yes, I think this will pay for much if not all of the costs of reaching Cetruvar."
        c "Good, let’s get going then."

    scene black with fade
    call ep004_skarak from _call_ep004_skarak

    call ep004_conversations from _call_ep004_conversations_1

    call ep004_tubloshi from _call_ep004_tubloshi

    play music "music/horizons.ogg" fadeout 4 fadein 1.0

    scene ep004_bastard_th_ce with dissolve
    if ep004_hannah_sex:
        "Back on the Bastard, nobody seemed surprised by my late arrival, so Ziv must have given them some excuse for which I was grateful."

    "We undocked from the Tubloshi ship moments later and were on our way again to the planet where Thyia's contact would help us get into the home of Ranimo Cetruvar."
    c "Where are we headed exactly?"
    scene expression eye_blink("images/ep004/ep004_bastard_th_ce_closeup") with dissolve
    th "Barranthis."
    c "A sunny paradise full of delightful people willing to help us?"
    th "Sadly, no."
    scene expression eye_blink("images/ep004/ep004_bastard_th_ce_closeup_smile") with dissolve
    th "It's a seedy shithole, from what I've heard."
    c "You've never been there?"
    th "No, but Vitriv lives there."
    c "I assume he's the one who's going to help us out?"
    th "That's the plan."
    th "He's well-connected and he should be able to get us the credentials we need to impress Cetruvar."

    scene ep004_barranthis with dissolve
    call location_screen ("Barranthis, Approach", True) from _call_location_screen_24

    "Only after haggling a fair amount were we able to land our ship in one of the many commercial docks of Barranthular, the largest city on the planet."
    scene ep004_barranthis_docks with dissolve
    "Thyia bribed one of the port officials to waive even more docking and admittance fees, which was apparently how the system worked here."
    "The rest of the crew agreed to stay aboard the ship, so Thyia and I could hit the streets to find her friend Vitriv."
    scene ep004_barranthis_city with dissolve
    "Her description of Barranthis being a seedy shithole was actually quite generous, if Barranthular was anything to go on."
    "The place stank of the trash piles heaping up along the streets, mixed with pollution from the busy air traffic above our heads."
    "Barranthular was as crowded as it was noisy and I couldn't think of any reason why someone would want to live here voluntarily."
    scene expression eye_blink("images/ep004/ep004_barranthis_city_closeup") with dissolve
    c "This guy, Vitriv, he actually likes living here?"
    th "I don't know, but this place has some of the best gambling dens in the galaxy."
    c "Right, that's a persuasive argument for some."
    th "It sure is for Vitriv."
    c "Do you have his address?"
    th "I do, it's not far from here."
    scene ep004_barranthis_city_apartment with dissolve
    "The neighborhood didn't get any better until we finally arrived at a gigantic apartment building."
    c "Cozy."
    th "I'm sure the views upstairs are lovely..."

    play music "music/reign-supreme.ogg" fadeout 4 fadein 1.0

    scene black with fade
    "We took the elevator up to the tenth floor, the smell of piss and moldy carpet invading our senses."
    scene ep004_barranthis_city_apartment_corridor with dissolve
    "Passing a long row of doors, we looked for Vitriv's room number."
    "Most of the apartments seemed to be occupied, judging from the noises coming from behind the front doors."
    "Vitriv's apartment was at the very end of the hall, the entrance decorated by several leaky bags of trash."
    scene expression eye_blink("images/ep004/ep004_barranthis_apartment") with dissolve
    "Thyia pressed the buzzer next to the door and we waited for several moments until pressing it again."
    c "Maybe he's not home?"
    scene ep004_barranthis_apartment_door with dissolve
    "Thyia seemed unconvinced and rapped her fist against the door."
    scene ep004_barranthis_apartment_door_open with vpunch
    "It creaked open."
    c "Uh-oh..."
    th "Fuck."
    scene expression eye_blink("images/ep004/ep004_barranthis_apartment_interior") with dissolve
    th "The place is completely trashed."
    c "Any sign of Vitriv?"
    th "I'm not sure, it's a real mess."
    th "Maybe we should get the hell out of here?"
    c "No, he's supposed to be our ticket to Cetruvar, let's see if we can find any leads inside."
    scene ep004_barranthis_apartment_interior_search with dissolve
    "The apartment looked like someone ransacked it, furniture was overturned and some of it broken."
    "The entire contents of the kitchen was dumped in pieces on the floor."
    "Other than that, the place was empty, no sign of Vitriv."
    "Thyia searched the small bedroom, but found nothing of note."
    scene expression eye_blink("images/ep004/ep004_barranthis_apartment_interior_th_closeup") with dissolve
    c "Place is as good as empty."
    th "Seems like it."
    c "Vitriv is a gambler right, Thyia?"
    th "Yes, he is."
    c "So we might have better luck hitting a couple of big casinos and asking about him?"
    scene expression eye_blink("images/ep004/ep004_barranthis_apartment_interior_th_closeup_fear") with dissolve
    "Right at that moment I saw Thyia's eyes go wide as she looked past me."
    th "[p_name], look out!"
    with vpunch
    "It was quite clear we were no longer alone in the apartment."
    scene ep004_barranthis_apartment_interior_shot with vpunch
    "Seconds later, the sound of a gunshot rung in my ears."

    call credits from _call_credits
    return

    label ep004_skarak:
        $ ep004_skarak = True

        play music "music/signal-to-noise.ogg" fadein 1.0 fadeout 4

        call location_screen ("Unknown, En Route to Skarak", False) from _call_location_screen_25
        "Ziv’s coordinates took us through several jump gates and star systems before we reached the planet where Tavort’s body was supposed to be."
        "When were nearly in orbit of the planet, I asked Ziv to join me on the bridge."
        scene expression eye_blink("images/ep004/ep004_cockpit_ziv") with dissolve
        c "Is this going to be another inhospitable rock?"
        zi "No, this a lush and green planet."
        c "You’ve been here before?"
        zi "I have."
        c "Wait, were you the one who brought the body here?"
        zi "Hardly, but I knew Tavort’s lover..."
        zi "She’s the one who brought him here after the battle."

        menu:
            "Derisive":
                $ ep004_ziv_derisive = True
                c "So now you’re betraying your friend’s trust by letting us grave-rob Tavort’s tomb?"
                scene expression eye_blink("images/ep004/ep004_cockpit_ziv_angry") with dissolve
                zi "She wasn’t my friend."
                "Céline broke the silence between Ziv and me by announcing we were arriving."
                scene expression eye_blink("images/ep004/ep004_cockpit_ce") with dissolve
                ce "Prepare for landing in two minutes."
            "[gr]Curious":
                c "Is she okay with us disturbing his corpse?"
                scene expression eye_blink("images/ep004/ep004_cockpit_ziv_angry") with dissolve
                zi "Frankly, I don’t care."
                zi "Luzane was my Premier and I hated her guts."
                zi "The only reason I know of Tavort is because we came here frequently and she had us gather resources while she visited him in the mountains."
                zi "One day, curiosity go the better of me and I just followed her to see what she was up to."
                zi "I found her praying at a grave."
                scene expression eye_blink("images/ep004/ep004_cockpit_ziv_angry_alt") with dissolve
                zi "Her fling with Tavort was public knowledge, but nobody knew what happened to him at the end of the Fifth Glorious Campaign."
                zi "Turns out he secretly abandoned his squad, to stay with Luzane, thinking of deserting..."
                zi "His transport shuttle got hit by a stray blast of a laser cannon and that’s the last she saw of him."
                c "So, the glorious hero of the Tubloshi..."
                scene expression eye_blink("images/ep004/ep004_cockpit_ziv_smile") with dissolve
                zi "Thought primarily with his dick in his twilight years, yes."
                c "I guess that’s something we can’t tell the Tubloshi?"
                zi "Not if you want to collect that reward."
                c "What happened to Luzane?"
                scene expression eye_blink("images/ep004/ep004_cockpit_ziv_serious") with dissolve
                zi "After word came out of her relationship with Tavort she was reprimanded and demoted."
                zi "Her position in my Stratum was untenable after that."
                zi "She’d been a terrible Premier, even her Secondaries loathed her."
                zi "So after she was physically assaulted multiple times, she just vanished."
                scene expression eye_blink("images/ep004/ep004_cockpit_ziv_smile") with dissolve
                zi "No one missed her, I can tell you that much."
                c "So basically we’re going to collect a guy who followed his dick around and had an accident, instead of saving a glorious hero?"
                zi "That’s pretty much the scenario, yes."
                c "Well, I’m not judging, as long as the Tubloshi are happy with his remains..."
                scene expression eye_blink("images/ep004/ep004_cockpit_ziv_serious") with dissolve
                zi "I’m sure they will be."
                zi "Tavort is mainly remembered for his deeds in the early years of the Fifth Glorious Campaign, before he met Luzane."
                c "How did they meet?"
                zi "Our Cohort, led by Luzane, was staying at a planet that was just conquered by the Tubloshi."
                zi "Or liberated is a better term, it was a very nasty place."
                scene expression eye_blink("images/ep004/ep004_cockpit_ziv") with dissolve
                c "Cohort?"
                c "I’m sorry, you were talking about Premiers and Secondaries before and it just struck me that I don’t even know what species you belong to."
                zi "I’m a Rhenkoy."
                c "Never heard of."
                zi "A Cohort is a group of Rhenkoy living together, headed by a Premier."
                scene expression eye_blink("images/ep004/ep004_cockpit_ziv_serious") with dissolve
                zi "All the Cohorts combined form the Rhenkoy, led by our Council of Nkoy."
                c "So a caste-based system?"
                zi "In a way, yes, strongly hierarchical."
                c "But you’re not part of a Cohort?"
                zi "No, I’m not at the moment."
                zi "I have special dispensation."
                scene expression eye_blink("images/ep004/ep004_cockpit_ce") with dissolve
                ce "Prepare for landing in two minutes."

                python:
                    codex_luzane = add_codex_entry(
                        Codex,
                        "Characters",
                        "Luzane",
                        [
                            "Ziv's former squad leader (Premier) and former lover of the Tubloshi hero Kyl Tavort."
                        ]
                    )

                "My conversation with Ziv was cut short when the Bastard broke atmosphere."

        scene ep004_skarak with dissolve
        call location_screen ("Skarak, Surface", True) from _call_location_screen_26
        "We touched down in a clearing and made a decision who was to go and find Tavort's tomb."
        "Lilly didn't have the stomach to go on an expedition so soon after our adventure with the Boverin, but Aven didn't have a problem with it."
        "We stocked up on supplies and weapons and went out into the wilderness."
        scene ep004_skarak_trek with dissolve
        c "This seems like a fertile planet, how come nobody lives here?"
        c "At least, I didn't see any cities or settlements in the Bastard's computer."
        scene expression eye_blink("images/ep004/ep004_skarak_trek_ziv") with dissolve
        zi "This is a designated conservation world of the Katorr, they use this planet and others to repopulate the wildlife they decimated on their own home planet."
        c "You could have told we just landed in a nature reserve..."
        c "How long before the Katorrian come and take us in?"
        zi "Katorran..."
        c "Who gives a fuck?"
        scene expression eye_blink("images/ep004/ep004_skarak_trek_ziv_smile") with dissolve
        c "How long before the Katorran find out we're violating the serenity of one of their nature reserves?"
        zi "Don't worry, these reserves aren't heavily policed and we'll be out of here within a day."
        c "If you say so..."
        scene ep004_skarak_trek_alt with dissolve
        "We walked for several hours, Ziv leading the way for most of the trek."
        "Upon reaching a small spring, Aven suddenly stopped."

        play music [ "music/satiate.ogg", "music/satiate-only-percussion.ogg" ] fadeout 4 fadein 1.0

        scene expression eye_blink("images/ep004/ep004_skarak_trek_av_shock") with vpunch
        av "Don’t move!"
        c "What?"
        av "Booby trap."
        c "I thought you said this planet was uninhabited, Ziv?"
        scene ep004_skarak_trek_doubt with dissolve
        zi "It is...{w} It should be..."
        zi "Maybe it’s an old trap?"
        scene expression eye_blink("images/ep004/ep004_skarak_trek_av") with dissolve
        av "Maybe..."
        c "Can you disable it?"
        av "Probably."
        scene ep004_skarak_trek_av_trap with dissolve
        "I didn’t see the trap in the high grass until Aven prodded it with a stick."
        "It was a crude device, often used by hunters, which would have been quite painful had anyone stepped on it."
        scene ep004_skarak_trek_av_trap_alt with vpunch
        "She prodded the trigger mechanism and the trap clamped shut, after which she allowed us to proceed."
        av "I think it goes without saying that we have to be extra careful from now on."
        av "Stay behind me."
        scene ep004_skarak_trek_single with dissolve
        "Our continued pace was much slower and Aven had to disable three more devices similar to the one we already encountered."
        zi "Nearly there."
        c "Good, be extra careful, whomever planted those booby traps might have created more surprises."
        c "You’re frowning, Ziv, what’s the matter."
        scene expression eye_blink("images/ep004/ep004_skarak_trek_single_ziv") with dissolve
        zi "This is supposed to be the spot..."
        c "I don’t like the sound of that."
        zi "No, I’m sure."
        zi "This is the location of his grave where I saw her praying."
        scene expression eye_blink("images/ep004/ep004_skarak_trek_single_av") with dissolve
        av "Well, there's no visible grave now."
        av "Maybe the marker was destroyed?"
        c "Probably by the same person who doesn’t like any visitors."
        c "Should we try to dig?"
        zi "But-"
        scene ep004_skarak_grenade with vpunch
        "A metallic thud cut Ziv short, as an object the size of a rock was thrown amongst us."
        scene ep004_skarak_grenade_active with vpunch
        av "GRENADE!"
        scene ep004_skarak_grenade_cloud with dissolve
        "Before we could jump away the device detonated with an audible click and we were all covered in a cloud of gas."
        scene ep004_skarak_grenade_cloud_person with dissolve
        "As we collapsed on the ground coughing, a figure wearing a gas mask stepped through the fumes."

        scene black with fade
        $ lu_name = "Woman"
        scene ep004_skarak_woman_closeup with dissolve
        lu "...yes my love, we will, soon."
        lu "There were intruders, I dealt with them."
        lu "Actually, they might prove useful..."
        "A woman cooing at a skeleton wasn’t exactly the sight I’d imagined after being gassed."
        scene ep004_skarak_woman with dissolve
        "Yet there she was, mumbling in front of an altar."
        "In any case, we’d found Tavort, but we were now tied up with ropes, which complicated matters considerably."
        scene ep004_skarak_av_zi with dissolve
        c "Aven?"
        c "Ziv?"
        scene expression eye_blink("images/ep004/ep004_skarak_woman_alt") with dissolve
        lu "Ah, you’re awake."
        lu "No, don’t pretend you’re still unconscious, I heard you whisper."
        c "Well, you got me."
        c "I’d like to be untied now please."
        scene expression eye_blink("images/ep004/ep004_skarak_woman_alt_smile") with dissolve
        lu "Sorry, but that’s not going to happen."
        c "You look an awful lot like Ziv..."
        c "Fuck, you’re Luzane, aren’t you?"

        $ lu_name = "Luzane"

        python:
            codex_luzane = update_codex_entry(codex_luzane, None,
                [
                    "Ziv's former squad leader (Premier) and former lover of the Tubloshi hero Kyl Tavort. Luzane lived on Skarak near the resting place of Kyl Tavort."
                ],
                "images/codex/Luzane.webp"
            )

        scene expression eye_blink("images/ep004/ep004_skarak_woman_alt_surprise") with dissolve
        lu "Yes, did Ziv tell you about me?"
        c "Yes."
        c "Only nice things, obviously."
        scene expression eye_blink("images/ep004/ep004_skarak_woman_alt_serious") with dissolve
        lu "You lie so easily, human."
        lu "Did Ziv come for me?"
        lu "Get revenge at last?"

        menu:
            "[gr]Truth":
                $ ep004_lu_truth = True
                c "No."
                scene expression eye_blink("images/ep004/ep004_skarak_woman_alt_surprise") with dissolve
                lu "Then why are you here?"
                c "We came for Tavort."
                lu "Did you now."
                lu "Ziv couldn’t let it all rest, could she?"
                c "I guess not."
            "Lie":
                c "Yes."
                scene expression eye_blink("images/ep004/ep004_skarak_woman_alt_smile") with dissolve
                lu "I knew she couldn’t let me go."
                scene expression eye_blink("images/ep004/ep004_skarak_woman_alt_angry") with dissolve
                lu "Jealous bitch."
                c "Jealous?"
                scene expression eye_blink("images/ep004/ep004_skarak_woman_alt_smile") with dissolve
                lu "Ah, so she didn’t tell you everything?"
                lu "Ziv and I...{w} We had feelings for each other."
                lu "But that was all a whim, something I realized when I experienced true love."
                c "For Tavort?"
                scene expression eye_blink("images/ep004/ep004_skarak_woman_alt_serious") with dissolve
                lu "Yes, for him."
                lu "Ziv couldn’t stand the idea of us together, so she was all too happy when my fortunes reversed."
                lu "I suspect she even had a hand in it."
        scene ep004_skarak_lu_zi with dissolve
        zi "Luzane?"
        lu "Ah, you’re awake."
        lu "I didn't think I'd ever see you again."
        scene expression eye_blink("images/ep004/ep004_skarak_zi_closeup") with dissolve
        zi "Nor did I."
        scene ep004_skarak_lu_zi with dissolve
        lu "So you came to defile my lover's grave?"
        zi "Your words."
        scene expression eye_blink("images/ep004/ep004_skarak_zi_closeup") with dissolve
        zi "I just came to give him a proper burial."
        lu "And what gives you the right to do that?"
        lu "Tavort's mine."
        scene expression eye_blink("images/ep004/ep004_skarak_zi_closeup_grim") with dissolve
        zi "Tavort's dead."
        scene expression eye_blink("images/ep004/ep004_skarak_lu_closeup") with dissolve
        lu "Then why does his spirit talk to me, Ziv?"
        lu "No, my love still lingers here, longing to be alive again."
        c "Just on the off-chance, but do the Tubloshi really reincarnate or something, Ziv?"
        scene expression eye_blink("images/ep004/ep004_skarak_zi_closeup_grim") with dissolve
        zi "No, they don't."
        c "Right."
        scene expression eye_blink("images/ep004/ep004_skarak_lu_closeup") with dissolve
        lu "Come on Ziv, you know as much about the treatises of Nkoy Kyldjar on the spirit world as I do."
        zi "Yes, I know that they're ravings by a mad heretic and that they deserve to be forgotten."
        lu "You'll take a different tone with me once I complete the ritual."
        lu "All in all, your arrival wasn't untimely, maybe an omen of things to come."
        scene ep004_skarak_lu_zi with dissolve
        c "Ritual?"
        lu "Yes, one of you will do nicely as a vessel to usher in Tavort's spirit into the land of the living again."
        scene expression eye_blink("images/ep004/ep004_skarak_zi_closeup_fear") with dissolve
        zi "Luzane, you can't seriously be thinking of performing those rites described by Kyldjar."
        c "What rites?"
        lu "It's the only way."
        zi "You've gone mad, Luzane."
        lu "Just watch, Ziv, I'll prove you wrong."
        lu "The boy looks like a prime candidate for the ritual."
        c "Wait, what?!"
        scene expression eye_blink("images/ep004/ep004_skarak_lu_closeup_angry") with dissolve
        lu "Silence! I need to prepare."
        scene ep004_skarak_ritual with dissolve
        "Her back turned towards us, Luzane began to lay out crystals among the stone altar and the surrounding surfaces."
        c "Ziv, what ritual is she talking about?"
        scene expression eye_blink("images/ep004/ep004_skarak_ritual_zi") with dissolve
        zi "Superstitious nonsense from an old book written by a disgraced former council member."
        zi "It describes the existence of the so-called spirit world and methods on how to communicate with its inhabitants."
        zi "Kyldjar also talks about manipulating the spirits by bonding with them through performing rituals."
        c "Fascinating, but what's going to happen to me?"
        scene expression eye_blink("images/ep004/ep004_skarak_ritual_zi_serious") with dissolve
        zi "You're going to have sex with her and at your climax she'll cut your throat."
        zi "She'll intone the prescribed incantations as you bleed out and that will bring Tavort back, supposedly."
        c "I must say I kinda lost you after the climax..."
        c "Fuck."
        zi "I suggest you hold out as long as possible."
        c "Gee, thanks for that nugget of advice..."
        c "If only Aven were awake!"
        scene expression eye_blink("images/ep004/ep004_skarak_ritual_av") with dissolve
        av "I am."
        av "Also, I've nearly cut through my wrist rope."
        c "Why didn't you say anything?"
        av "Didn't want to alert Luzane."
        c "What are we going to do?"
        av "Go through with the ritual and stall her long enough for us to free ourselves."
        av "Can you manage that?"
        c "I'll think of something, but hurry!"
        av "We will."
        scene ep004_skarak_ritual_lu with dissolve
        lu "Ah, the girl is awake as well."
        lu "You'll all be present to witness the return of Tavort."
        lu "My preparations are complete."
        lu "I'm going to untie your legs now, boy."
        c "Call me [p_name]."
        lu "All right."
        lu "If you try to run, [p_name], I'll cut you down and then I'll do the same to your friends."
        lu "If you just follow my lead from here on out, they'll live, you have my word on that."
        scene ep004_skarak_ritual_lu_ropes with dissolve
        "She didn’t wait for my reply, dragged me to the ritual circle and proceeded to cut the rope binding my hands."
        "With several surprisingly quick motions she was able to remove my body armor"
        scene ep004_skarak_ritual_naked with vpunch
        c "Wah?"
        lu "Yes, you’ll do nicely."
        lu "I’m sure Ziv already told you when you were whispering behind my back, but we’re going to have sex, you and I."
        lu "Our climax will bring Tavort back into this world."
        c "You really are crazy, aren’t you?"
        scene expression eye_blink("images/ep004/ep004_skarak_ritual_naked_angry") with dissolve
        lu "Shut up."
        scene ep004_skarak_ritual_undress with dissolve:
            yalign 1.0
            ease 8 yalign 0.01
        $ renpy.pause()
        "The woman started to undress herself, revealing her large breasts and athletic physique."
        "My cock began to stir and I thought to myself that the ritual wasn’t all together that bad, expect for the violent death at the end."
        scene ep004_skarak_ritual_undress_alt with vpunch:
            yalign 0.01
        "But then her dress dropped to the ground."
        scene ep004_skarak_ritual_undress_alt:
            yalign 0.01
            ease 8 yalign 0.8
        $ renpy.pause()
        c "What?!{w} You have a...?"
        c "You have both?!"
        scene expression eye_blink("images/ep004/ep004_skarak_ritual_undress_alt_smile") with dissolve
        lu "Yes."
        lu "And you’re going to make me ready."

        menu:
            "Lick pussy":
                $ ep004_lu_lick = True
                call ep004_lu_lick from _call_ep004_lu_lick
            "Suck cock":
                $ ep004_lu_suck = True
                call ep004_lu_suck from _call_ep004_lu_suck
            "Pretend to go along [red]\[Ends Sex Scene\]":
                scene ep004_skarak_ritual_fist with vpunch
                "Luzane attempted to push her rock-hard erection against my face, but instead she got my fist in her groin."
                "She nearly collapsed and staggered backward, crying out in pain."
                c "Now would be a great time to help me, girls!"
                scene ep004_skarak_ritual_rock with vpunch
                "Ziv jumped up and grabbed a rock before lunging at Luzane and hitting her square in the head."
                "The woman toppled over and fell unconscious to the ground."

        scene expression eye_blink("images/ep004/ep004_skarak_ritual_av_sit") with dissolve
        av "Are you all right [p_name_short]?"
        if ep004_lu_lick or ep004_lu_suck:
            "Yes, I think so, she's a bit heavy though..."
            scene ep004_skarak_ritual_drag with dissolve
            "Ziv and Aven dragged the woman off me and untied my legs."
        else:
            "Yes, I think so..."
            scene ep004_skarak_ritual_drag with dissolve
            "Ziv and Aven dragged the woman away and untied my legs."
        "Neither of them mentioned the uneasy spectacle they just witnessed and let me dress without saying anything."
        scene expression eye_blink("images/ep004/ep004_skarak_skeleton") with dissolve
        "Aven made sure the madwoman was tied up firmly while Ziv and I inspected the remains of Kyl Tavort."
        c "Well, it's a skeleton, how do we make sure it's actually Tavort?"
        zi "The skeleton has the bone structure of a Tubloshi and the fact that Luzane was guarding it should be proof enough."
        zi "The Tubloshi will probably do a quick genetic scan to verify the remains with the ones on file in their database."
        c "Let's pack up those bones then."
        scene ep004_skarak_container with dissolve
        "Ziv and I retrieved the large collapsable container we dumped back in the fields and we began to work on moving the bones of Kyl Tavort to it. "
        "We tried to be as careful as possible to preserve the remains for the Tubloshi and luckily the skeleton of Tavort was in rather good shape, all things considering."
        "Aven kept watch over the unconscious Luzane, holding her gun which she found amongst the woman's possessions."

        play music "music/signal-to-noise.ogg" fadein 1.0 fadeout 4

        "After we filled the container we retrieved the rest of our things and prepared for the journey back to the Bastard."
        scene expression eye_blink("images/ep004/ep004_skarak_container_av") with dissolve
        av "What are we going to do with that woman?"
        c "I don't know, leave her here?"
        scene expression eye_blink("images/ep004/ep004_skarak_container_av_unsure") with dissolve
        av "Bound?"
        c "I don't want her pursuing us."
        c "Could you loosen the ropes so she can free herself with some effort?"
        scene expression eye_blink("images/ep004/ep004_skarak_container_av") with dissolve
        av "That's possible, yes."
        c "Do it, unless you object, Ziv?"
        scene expression eye_blink("images/ep004/ep004_skarak_container_zi") with dissolve
        zi "No, why would I?"
        zi "Despite everything, I don't hold a grudge against her."
        zi "And she's fallen so low already, living here like a savage, that's punishment enough, I think."
        scene ep004_skarak_trek_back with dissolve
        "So we left Luzane's unconscious naked body at Tavort's burial site and began the hike back to the ship."
        "Because we backtracked the same route the boobytraps didn't bother us and we kept good pace."
        scene ep004_skarak_bastard with dissolve
        "Lilly and Thyia were already on the lookout outside the ship when we arrived."
        l "That took quite some time, are you all okay?"
        scene expression eye_blink("images/ep004/ep004_skarak_bastard_av") with dissolve
        av "We met some resistance along the way."
        th "I thought the planet was uninhabited?"
        c "Nearly uninhabited might be a better description..."
        c "Tavort had company, seems his former lover didn't want to part with him."
        scene ep004_skarak_bastard with dissolve
        l "How did you convince her to give up the remains?"
        c "Subterfuge and a big rock to the side of the head did the trick."
        th "You killed her?"
        zi "No, she's still alive."
        th "Let's get out of here then."
        c "Splendid idea."
        scene black with fade
        return

    label ep004_lu_lick:
        if _in_replay:
            $ lu_name = "Luzane"

        scene ep004_lu_pussy with dissolve
        "Luzane pushed her rock-hard erection against my face, but I managed to evade and planted my lips firmly on her lower lips."
        "The earthy smell of her cock and dripping-wet pussy was oddly arousing and I found myself probing her cunt with my tongue, eager to taste her."
        show ep004_lu_jerk with dissolve
        "With firm strokes I licked her swollen lips and clitoris, while she jerked herself off."
        "When I used my fingers to enhance the stimulation of her clitoris, Luzane let go of her cock and succumbed to my touch."
        scene ep004_lu_jerk_alt with dissolve
        "She grabbed my hair with raking fingers and moaned into the night."
        lu "Fuck yes, [p_name], keep going like that!"
        "At first I thought she was too consumed by lust and had forgotten all about the ritual, but after a bout of intense licking nearly sent her twitching into orgasm she pulled me from her pussy."

        call ep004_lu_fuck from _call_ep004_lu_fuck

        $ renpy.end_replay()
        return

    label ep004_lu_suck:
        if _in_replay:
            $ lu_name = "Luzane"

        scene ep004_lu_cock with dissolve
        "Luzane pushed her rock-hard erection against my face and forced my lips apart."
        lu "Suck."
        scene ep004_lu_cock_alt with dissolve
        "The earthy smell of her cock and dripping-wet pussy was oddly arousing and I found myself accepting her throbbing member."
        "I’d never sucked a cock before, but I knew what I liked myself."
        "With deep strokes I sucked in her veined shaft, my tongue whirling over the head of her dick."
        "I reached at the base of her cock, where the testicles would normally be, to find her pussy."
        scene ep004_lu_cock_finger with dissolve
        "Luzane’s swollen lips were wet to the touch, a sure sign she enjoyed the stimulation of her cock."
        "She grabbed my hair with raking fingers and moaned into the night."
        lu "Fuck yes, [p_name], keep going like that!"
        "At first I thought she was too consumed by lust and had forgotten all about the ritual, but after a bout of intense sucking nearly sent her twitching into orgasm she pulled me from her cock."

        call ep004_lu_fuck from _call_ep004_lu_fuck_1

        $ renpy.end_replay()
        return

    label ep004_lu_fuck:
        scene ep004_lu_ca_jerk with dissolve
        lu "Not yet, boy."
        lu "I need your seed."
        "With a few flicks she had my cock at battle-strength, though it was a little annoying she didn't take the time to pleasure me as I did her."
        scene ep004_lu_ca_penetrate with dissolve
        "She lowered herself on top of me, guiding my cock inside her pussy with her hand."
        show ep004_lu_ca_penetrate_alt with dissolve
        "Luzane sighed when I was fully inside her and began to ride me, slow at first, but growing more intense with each thrust."
        show ep004_lu_ca_penetrate_side with dissolve
        "I saw precum leaking from the tip of her dick, as it bounced up and down on the rhythm of our coupling."
        scene ep004_lu_ca_fuck with dissolve
        "The fact that both Aven and Ziv were looking at us fucking, was something I didn't care about anymore, all I wanted was to fill Luzane with cum."
        scene ep004_lu_ca_fuck_alt with dissolve
        "My fingers felt the woman's rolling muscles of her powerful legs as she rode me harder and harder."
        scene ep004_lu_ca_fuck_jerk with dissolve
        "As her moans became hoarser, I grabbed hold of her veined shaft and began to jerk her cock."
        "Luzane's penis was covered in precum and responded instantly to my touch by releasing more from her slit."
        show ep004_lu_ca_fuck_jerk_alt with dissolve
        "I couldn't hold out much longer and brought Luzane right at the edge of her climax in seconds, her cock still firmly in my fist."
        show ep004_lu_ca_penetrate_face with dissolve
        "With my penis deep inside her, I felt the woman on top of me twitch."
        scene ep004_lu_ca_fuck_jerk_closeup with dissolve
        "She slammed her body down for the last time as I tugged desperately at her shaft."
        scene ep004_lu_ca_fuck_orgasm with vpunch
        "Luzane roared as her cock sprayed cum everywhere and I exploded inside her pussy."
        "The madwoman began to rock back and forth as her orgasm coursed through her body."
        scene ep004_lu_ca_fuck_orgasm_knife with vpunch
        "My dick was still pumping cum in her vagina when a knife flashed in Luzane's hands."
        "She brought her arms down to plunge the knife point-first in my chest."
        scene ep004_skarak_ritual_rock_alt with vpunch
        "Luzane’s confusion over my relieved expression saved me from a violent death, as did the blow to the head with a rock courtesy of Ziv, who'd sneaked up behind her back."
        "The woman collapsed on my chest, where she lay unconscious, cum still leaking from her cunt and cock."
        return

    label ep004_tubloshi:
        play music "music/tears-in-rain.ogg" fadein 1.0 fadeout 4

        call location_screen ("Unknown, En-route to Tubloshi rendezvous point", False) from _call_location_screen_27
        "The Bastard took off with some haste after Céline punched in the coordinates that would take us to the location of the Tubloshi."
        scene ep004_tubloshi with dissolve
        "A large warship appeared on our scanners when Céline disengaged the SL-Drive."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ce") with dissolve
        ce "The Tubloshi are already hailing us, [p_name_short]."
        c "Guess they're excited their hero is coming back to them."
        ce "They're submitting docking instructions."
        c "All right, Ziv, let's get a move on."
        scene ep004_tubloshi_docking with dissolve
        "While Céline initiated the docking procedure we retrieved the container with Tavort's remains and headed to the exit hatch."
        "After the Iron Bastard was swallowed inside the belly of the Tubloshi warship, our designated landing pad pressurized and we stepped outside."
        scene ep004_tubloshi_ship with dissolve
        "The Tubloshi delegation awaited us inside the entrance corridor."
        "Two enormous warriors carrying large weapons flanked a lithe human woman in a distinctive green bodysuit."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_zi") with dissolve
        zi "That's probably their translator."
        c "They don't speak our language?"
        zi "They either don't, or they won't."
        scene ep004_tubloshi_ship_closeup with dissolve
        "Our conversation was cut short by a series of grunts and growls from one of the giants facing us."
        "About midway, the translator cut in."

        $ ha_name = "Translator"

        ha "Greetings, Ziv of the Rhenkoi and [p_name] of the Humans."

        menu:
            "[gr]Be polite":
                $ ep004_tu_polite = True
                c "Greetings, noble warriors of the Tubloshi, we have brought home the hero Kyl Tavort."
            "Be brash":
                c "Shall we cut to the chase?"
                c "Tavort's body in exchange for the sum we agreed upon."

        ha "We are grateful for returning one of our most valiant, [p_name] of the Humans."
        ha "After verifying the genetic fingerprint of Kyl Tavort's remains we will pay him the proper respect he's been denied for so long."
        scene ep004_tubloshi_ship_walk with dissolve
        ha "Please follow us."
        "The woman and the warriors led us through several corridors to a section that contained the ship's lab."
        scene ep004_tubloshi_ship_door with dissolve
        ha "We ask you to remain outside until the test have been completed."

        menu:
            "Contest":
                $ ep004_tu_contest = True
                c "Wait a minute, who's to say you won't whisk away the remains and put us out of an airlock?"
                "It took the woman a while to translate what I just said and a long silence followed."
                scene ep004_tubloshi_ship_door_angry with dissolve
                "Both warriors stared at me in what could have been rage or disbelief."
                "As soon as one of them spoke I knew it was rage, for he roared and bellowed at me at the top of his lungs."
                scene ep004_tubloshi_ship_door_angry_alt with vpunch
                ha "You dare to question our honor?!"
                ha "We have killed lesser men for an insult like that, [p_name] of the Humans!"
                scene ep004_tubloshi_ship_door_zi with dissolve
                zi "Forgive us, please, [p_name] spoke out of ignorance."
                zi "Be assured that we do not question the honor of the Tubloshi, a trait famously associated with your species across the entire galaxy."
                "Now it was my turn to look enraged as Ziv undermined me in front of those warriors."
                scene expression eye_blink("images/ep004/ep004_tubloshi_ship_door_ha") with dissolve
                "They seemed to accept her apology and took the remains inside the laboratory."
                ha "Wait here."
            "[gr]Accept":
                c "Of course."
                scene expression eye_blink("images/ep004/ep004_tubloshi_ship_door_ha") with dissolve
                "The Tubloshi took the remains inside the laboratory and the door shut behind them, leaving us with the translator."

        ha "This will probably take a while."
        ha "Why don't you follow me to the mess."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_mess") with dissolve
        "We trailed behind the woman through another set of corridors and arrived at a large room filled with tables and benches."
        ha "They'll come find us after they're done examining the bones."
        ha "Can I get you anything to drink?"
        zi "No, thank you."
        c "I'm good, thanks, miss..."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_mess_shock") with dissolve
        ha "Oh, that’s right, I never properly introduced myself."
        ha "I'm Hannah."

        $ ha_name = "Hannah"

        c "Pleased to meet you, Hannah."
        c "A fellow human, no less?"
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_mess_smile") with dissolve
        ha "Yes, I am."
        c "Just making sure, but you're here out of your own free wil?"
        ha "Haha, of course."
        ha "You haven't figured out the Tubloshi for the honorable people they are?"
        c "I guess so, are they really so zealously righteous?"
        ha "From what I've seen of them, yes."
        c "What on earth made you decide to become a translator for them?"
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_mess_smile_alt") with dissolve
        ha "I responded to a job offer a couple of years back."
        ha "The Tubloshi are well-known for their unwillingness to speak other languages and they pay well."
        c "But for that paycheck you just need to stay cooped up in a warship at the ass-end of the galaxy for most of the time."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_mess_smile") with dissolve
        ha "It's not so bad."
        ha "I have my own quarters here and we make regular trips to space stations and planets."
        ha "It helps that Kyl Zaghav is often sent on diplomatic trips."
        c "Kyl Zaghav?"
        ha "He's the commander of this vessel, maybe you'll meet him."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_mess_zi") with dissolve
        zi "He's quite well-known in some circles."
        c "So you've heard of him?"
        zi "Yes, I have."
        zi "I'm glad we're dealing with him."
        c "How so?"
        zi "He's used to interacting with other species, regular Tubloshi aren't."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_mess_smile_alt") with dissolve
        ha "I can confirm."
        ha "I've met some of the other warship crews and they're just not used to dealing with other people than their own."
        ha "Makes for some very awkward conversations, I can tell you..."
        zi "Lots of talk about battle, I gather?"
        ha "Yes and dying honorably, of course."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_mess_unsure") with dissolve
        ha "When one of them tried to strike up a conversation about the ways of killing enemy combatants with just a clipped fingernail I decided to keep to myself."
        scene ep004_tubloshi_ship_mess_tubloshi with dissolve
        "The door slid open and the two Tubloshi entered the room."
        "They were followed by another who wore an armor suit that was slightly different."
        "The new Tubloshi began to speak immediately, assuming Hannah would translate."
        scene ep004_tubloshi_ship_mess_ha_tu with dissolve
        ha "I am pleased to meet you, [p_name] and Ziv, my name is Kyl Zaghav."
        c "Likewise."
        ha "The bones have been confirmed as those of our hero Kyl Tavort."
        ha "We will grant him the proper burial rights and a place of honor in the annals of the Fifth Glorious Campaign."
        ha "By retrieving his remains, you have done our people a great service."
        ha "Will you join us for a toast to commemorate Kyl Tavort's passing?"
        scene ep004_tubloshi_ship_mess_bottle with vpunch
        "One of the Tubloshi slammed a bottle together with several glasses on the table."
        "Kyl Zaghav didn't wait for our answer and filled six glasses to the brim."
        scene ep004_tubloshi_ship_drink_tu with dissolve
        ha "To Kyl Tavort, for his deeds were glorious and his demeanor honorable."
        zi "To Kyl Tavort."
        c "To Kyl Tavort."
        scene ep004_tubloshi_ship_drink with dissolve
        "The Tubloshi downed the glass in one go, as did Hannah and Ziv, so I did the same."
        "My throat was instantly overwhelmed by a burning sensation that crept towards my stomach."
        "It took a lot of restraint not to collapse into a fit of coughing, though the Tubloshi seemed to notice my discomfort and grinned."
        "The six glasses were filled again, the Tubloshi all downed them again, but Hannah and Ziv only sipped from the liquid this time."
        "I followed their example and tried to start a conversation with the Tubloshi ambassador via Hannah."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_drink_tu_alt") with dissolve
        c "What will the ceremony for Kyl Tavort entail exactly?"
        ha "The priests will sing the praises of Kyl Tavort's actions for several days, while they sculpt his likeness into stone."
        ha "On the day of the ceremony, an account of the Fifth Glorious Campaign will be told, with special emphasis on Kyl Tavort's part in this heroic event."
        ha "His bones will then be buried at the base of the sculpture created by the priests as they sing his song for one last time."
        "I was very happy we weren't invited to the funeral, as it sounded utterly dull."
        "The Tubloshi seemed happy with the polite words we had to offer on the burial and proceeded to drink even more of the hard liquor."
        scene ep004_tubloshi_ship_drink_alt with dissolve
        "Pretty soon they were visibly drunk and talking amongst each other."
        "Hannah didn't translate, but the language of a drunk is pretty universal."
        "They seemed to have forgotten about us and were too caught up in their tall tales, probably boasting about some heroic battle somewhere."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_drink_zi") with dissolve
        zi "I'd like to retire to the Iron Bastard, I think."
        ha "Of course."
        "Hannah interrupted the boisterous conversation of the Tubloshi and spoke a few words with Kyl Zaghav."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_drink_tu_alt") with dissolve
        ha "Kyl Zaghav thanks you for your services from the bottom of his heart."
        ha "You are true friends of the Tubloshi."
        ha "The payment has also been authorized, so you should have received it already."
        "I looked at Ziv and she nodded, she'd probably checked the transaction during our talk with the Tubloshi."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_drink_ha") with dissolve
        ha "Let me walk you to your ship."
        "The Tubloshi saluted us briefly before returning to their drinking and Hannah guided us back to the access corridor."
        scene expression eye_blink("images/ep004/ep004_tubloshi_ship_corridor") with dissolve
        ha "It was nice meeting you both."

        if ep004_tu_polite and not ep004_tu_contest:
            ha "Especially you, [p_name], it's been such a long while since I encountered a fellow human."
            ha "Will you be leaving immediately, or..?"
            c "That was the plan, unless there's something else?"
            scene expression eye_blink("images/ep004/ep004_tubloshi_ship_corridor_unsure") with dissolve
            ha "No, not really."
            ha "It's just...{w} I wanted to talk a little more, but that wasn't really possible with the Tubloshi present."
            c "I see."
            scene expression eye_blink("images/ep004/ep004_tubloshi_ship_corridor") with dissolve
            ha "Would you like to have a drink in my quarters?"
            ha "To catch up on things, maybe?"

            menu:
                "[gr]Accept":
                    c "Only if you have better liquor than whatever the Tubloshi like to drink."
                    scene expression eye_blink("images/ep004/ep004_tubloshi_ship_corridor_smile") with dissolve
                    ha "I promise."
                    c "Good."
                    scene expression eye_blink("images/ep004/ep004_tubloshi_ship_corridor_zi") with dissolve
                    c "Go on ahead, Ziv, I'll catch up later."
                    zi "Right."
                    zi "See you later."
                    zi "Goodbye, Hannah."

                    call ep004_hannah from _call_ep004_hannah
                "Decline":
                    c "I'm sorry, but we must really be on our way."
                    scene expression eye_blink("images/ep004/ep004_tubloshi_ship_corridor_unsure") with dissolve
                    ha "Oh...{w} of course...{w} I understand."
                    scene expression eye_blink("images/ep004/ep004_tubloshi_ship_corridor_smile") with dissolve
                    ha "Safe travels!"
                    c "You too, Hannah, goodbye."
                    scene expression eye_blink("images/ep004/ep004_tubloshi_ship_corridor_zi") with dissolve
                    zi "Goodbye."
        else:
            zi "Goodbye, Hannah."
            c "Goodbye."
            scene expression eye_blink("images/ep004/ep004_tubloshi_ship_corridor_smile") with dissolve
            ha "Safe travels."

        python:
            codex_hannah = add_codex_entry(
                Codex,
                "Characters",
                "Hannah",
                [
                    "Hannah is a translator in the employ of the Tubloshi and acted as a guide on their warship when [p_name] and Ziv brought the body of the warrior Kyl Tavort back home."
                ],
                "images/codex/Hannah.webp"
            )

        scene black with fade
        return

    label ep004_hannah:
        if _in_replay:
            $ ha_name = "Hannah"

        $ ep004_hannah_sex = True
        scene ep004_tubloshi_ship_ha_walk with dissolve
        "I followed the woman to the crew quarters of the ship."
        scene expression eye_blink("images/ep004/ep004_ha_quarters") with dissolve
        ha "Well, here we are."
        c "Cosy, considering we're on a warship."
        ha "I did my best."
        ha "Drink?"
        c "Yes please."
        scene ep004_ha_quarters_alt with dissolve
        c "Let's make a toast then."
        c "Not to Kyl Tavort again, surely?"
        scene expression eye_blink("images/ep004/ep004_ha_quarters_drink") with dissolve
        ha "Nah, to chance encounters?"
        c "I'll drink to that."
        c "So Hannah, do you invite all of your guests to your private quarters?"
        scene expression eye_blink("images/ep004/ep004_ha_quarters_drink_smile") with dissolve
        ha "Haha, no."
        ha "Just the interesting ones."
        c "Right, I'm glad I qualify."
        ha "To be honest, it's the first time I asked someone..."
        ha "It's just, you reminded me of someone."
        c "Happy memory, I hope?"
        ha "Yes, a sweet boy named Cenc, from very long ago."
        scene expression eye_blink("images/ep004/ep004_ha_quarters_drinking") with dissolve
        "We were silent for a while, the tension between us tangible."
        scene expression eye_blink("images/ep004/ep004_ha_quarters_drinking_closeup") with dissolve
        "I set my glass on the ground and met her eyes."
        "She looked at me with a fire in her eyes, a gaze tinged with melancholy and desire."
        c "Kyl Zaghav doesn't object to me being here?"
        scene expression eye_blink("images/ep004/ep004_ha_quarters_drinking_closeup_unsure") with dissolve
        ha "Why would he?"
        c "Oh, I thought you and he..."
        scene expression eye_blink("images/ep004/ep004_ha_quarters_drinking_closeup_laugh") with vpunch
        ha "Hahahaha!"
        c "That's funny, because...?"
        scene expression eye_blink("images/ep004/ep004_ha_quarters_drinking_closeup_smile") with dissolve
        ha "Most if not all Tubloshi are homosexuals."
        c "Really?"
        ha "Really."
        c "But how do they reproduce?"
        ha "I could tell you all about that, or...{w} you could...{w} kiss...{w} me..."
        call ep004_hannah_sex from _call_ep004_hannah_sex

        scene black with fade
        return

    label ep004_hannah_sex:
        scene ep004_ha_quarters_kissing with dissolve
        "The sexual preferences of the Tubloshi forgotten in an instant, we embraced on the couch and kissed."
        "As our passion become more heated, we rose from the couch, still kissing and nearly toppling over the drinks on the floor before moving to the bed."
        scene ep004_ha_quarters_kissing_bed with dissolve:
            yalign 1.0
            ease 8 yalign 0.01
        $ renpy.pause()
        "My hands trailed the soft fabric of her tight bodysuit in search for a zipper."
        scene ep004_ha_quarters_kissing_undress with dissolve
        "When my fingers found purchase I slowly exposed her breasts, while dotting the freckled skin of her sternum with kisses."
        "Her fingers tousled my hair, directing me to her gorgeously shaped breasts and the nipples that stood proudly erect."
        ha "Make love to me, [p_name]!"
        scene ep004_ha_quarters_breasts with dissolve
        "I took one of her hard nipples in my mouth and circled her aureolas with my tongue."
        "Hannah began to sigh heavily and slowly rubbed her thighs against each other as I kneaded her full breasts."
        show ep004_ha_quarters_breasts_alt with dissolve
        "While she trashed and turned, I slipped a hand between her legs."
        "She welcomed me by opening her legs and twisting her lower body towards my eager fingers."
        "Her pussy was warm and wet to the touch."
        scene ep004_ha_quarters_finger with dissolve
        "Hannah gasped as my fingertips brushed her moist lips, making their way towards her clit."
        "I looked up from suckling her nipples and met her pleading eyes."
        "Slowly lowering my head towards her cunt, my fingers began their work in earnest."
        scene ep004_ha_quarters_finger_alt with dissolve
        "Massaging the area around her clitoris I brought the red-haired woman gradually into a trance-like state of pleasure."
        scene ep004_ha_quarters_finger_mouth with dissolve
        "She breathed heavily and moaned pleadingly when I paused to take my fingers off her clit to wet them in her own juices."
        "Wanting to taste her, I let my tongue take over from my fingers."
        "She tasted of salt and I gorged myself on her earthly smell."
        scene ep004_ha_quarters_licking with dissolve
        "Suddenly I felt her hands on my head, pushing me down and I knew I had her close to a climax."
        "Using my tongue and my fingers, I treated her pussy to an intense volley of attention."
        "Hannah clasped her hand over her mouth and let out a muffled squeal."
        scene ep004_ha_quarters_orgasm with vpunch
        "She climaxed right in my face, her juice dripping on my tongue."
        "The last remnants of her orgasm left her body after several minutes, but at that point she already had my hard cock in her hands."
        scene ep004_ha_quarters_suck with dissolve
        "Licking and sucking the tip, she made me ready to enter her."
        scene ep004_ha_quarters_suck_alt with dissolve
        "Her warm mouth enveloped my throbbing shaft as generous streams of saliva dripped from the corners of her mouth."
        "Hannah's pussy glistened wet in the artificial light of the cabin."
        "There was absolutely no mistake she was entirely ready for me."
        scene ep004_ha_quarters_penetrate with dissolve
        "So I pushed the head of my dick against her tight opening and pushed slowly."
        "Murmuring encouraging words, she dug her fingers into my back and urged me to go deeper inside her."
        show ep004_ha_quarters_fuck with dissolve
        "Hannah moaned my name in my ear and our bodies collided at an ever increasing rhythm."
        show ep004_ha_quarters_fuck_side with dissolve
        "I lusted over her perfect body, the gorgeous curve of her waist and the delicious swell of her breasts."
        "My cock slipped from her cunt after fucking her hard for several minutes."
        scene ep004_ha_quarters_doggy with dissolve
        "Biting her lip, Hannah flipped around and offered me the sight of her perfect ass."
        "I grabbed her by the hips and slid inside her cunt from behind."
        scene ep004_ha_quarters_doggy_alt with dissolve
        "The flesh of her round ass bounced as I fucked her, holding her firmly at the waist."
        "She rested her head on the bed and drooled a little on the sheets, still moaning my name as my cock thrust deep inside her."
        show ep004_ha_quarters_doggy_up with dissolve
        "I grabbed her arms and folded them across her back, pulling her body upward."
        show ep004_ha_quarters_doggy_up_side with dissolve
        "Her ass was pressed flat against my pelvis as I fucked her with renewed intensity."
        scene ep004_ha_quarters_doggy_up_alt with dissolve
        "Hannah was completely out of breath and could only manage ragged outcries as my hard cock hit home inside of her."
        "I kissed her neck and kept her close to me as I felt my orgasm building."

        menu:
            "Creampie":
                $ ep004_ha_creampie = True
                scene ep004_ha_quarters_doggy_up_alt with vpunch
                "Roaring, I slammed my entire length inside her one last time, my balls hitting her pussy with a slap."
                "Deep inside her a torrent of thick cum was released as she collapsed on the bed."
                scene ep004_ha_quarters_doggy_creampie with flash
                with flash
                "When my cock finally slipped from her cunt, a stream of cum oozed from her gaping pussy."
            "Facial":
                "Roaring, I let go of her arms and flipped her over on her back."
                scene ep004_ha_quarters_facial with dissolve
                "I sprayed her face with thick streaks of cum as she brought her head towards my cock."
            "Body":
                "Roaring, I let go of her arms and whipped my cock outside of her pussy."
                scene ep004_ha_quarters_body with dissolve
                "I sprayed her back with a thick stream of cum as she collapsed on the bed."

        scene ep004_ha_quarters_post with dissolve
        "Hannah smiled and sighed in complete satisfaction."
        "I took the woman in my arms and lay with her on the bed for a long time, kissing the freckled skin of her shoulders and stroking her fiery red hair."
        scene expression eye_blink("images/ep004/ep004_ha_quarters_post_closeup") with dissolve
        ha "There's no way I can convince you to stay, is there?"
        c "What you and I just did was pretty convincing, actually..."
        c "But I have people waiting on me, I'm afraid."
        ha "I know, but a girl can dream, right?"
        ha "I'm really glad I met you, [p_name], even if it was just for one night."
        c "Me too, Hannah."
        scene ep004_ha_quarters_post_alt with dissolve
        "We kissed and cuddled for a while longer, until it was high time to get dressed and find the others on the Iron Bastard."
        "Hannah and I said our farewells, expressing hope that we'd meet again and knowing full-well how slim that chance actually was."
        $ renpy.end_replay()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
