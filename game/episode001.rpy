
image ep001_camran_barracks_jade_hj = Movie(play="movies/ep001/ep001_camran_barracks_jade_hj.webm")
image ep001_camran_barracks_jade_hj_closeup = Movie(play="movies/ep001/ep001_camran_barracks_jade_hj_closeup.webm")
image ep001_tents_celine_camran_fucking = Movie(play="movies/ep001/ep001_tents_celine_camran_fucking.webm")
image ep001_tents_celine_camran_fucking_alt = Movie(play="movies/ep001/ep001_tents_celine_camran_fucking_alt.webm")


label episode001:
    $ save_name = "Episode 1"

    $ celine_romance = False
    $ celine_rejected = False
    $ ep001_celine_talk = False
    $ ep001_eva_talk = False
    $ ep001_lilly_talk = False
    $ ep001_kit_talk = False
    $ ep001_thim_talk = False
    $ ep001_c_visit = False
    $ ep001_c_spy = False
    $ ep001_e_l_spy = False
    $ ep001_e_l_visit = False
    $ ep001_celine_creampie = False
    $ ep001_j_hj = False
    $ ep001_jade_scold = False
    $ ep001_medbay_thim_talk = False
    $ ep001_medbay_thim_ignored = False
    $ ep001_medbay_lilly_talk = False
    $ ep001_medbay_kit_visit = False
    $ ep001_vess_truth = False

    play music "music/theoryofmachines.ogg" fadein 1.0 fadeout 4

    scene black with fade
    centered "{=chapter_heading}EPISODE 1{/=chapter_heading}"

    scene ep001_floating with fade:
        yalign 0
    call location_screen (__("Unknown"), True) from _call_location_screen
    "Space is a vast, cold place..."
    "Space is a fucking lonely place..."
    scene ep001_floating:
        ease 4 yalign 1.0
    $ renpy.pause(4.5, hard=True)
    "Especially when you're floating around in a vac-suit with just one bottle of oxygen left."
    "Yeah, you're probably wondering how the fuck that happened."
    "You know what? I'll tell you."
    scene black with fade
    "It's not that I've got something better to do, besides using up all my remaining air."
    scene ep001_kepler with dissolve
    "It all started when I was having some fun on one of the moons of Kepler XIV..."
    scene black with fade
    "No wait. I should start properly."
    "At the beginning."

    scene expression eye_blink("images/ep001/ep001_mansion") with dissolve
    "My name is [p_name] Agust Valenmann de Lonval, or just [p_name_short] for those who know me a little better."
    "I come from a long line of galactic nobility. Not that it's worth a damn, but having a title always impresses the ladies."
    if game.is_special:
        "Until the tender age of sixteen I lived with my parents and my twin sisters in a mansion on Tuolovi, a small green planet orbiting Typhon - once poetically called HD 10180 b."
    else:
        "Until the tender age of sixteen I lived with my parents in a mansion on Tuolovi, a small green planet orbiting Typhon - once poetically called HD 10180 b."
    python:
        codex_tuolovi = add_codex_entry(
            Codex,
            __("Planets"),
            __("Tuolovi"),
            [
                __("Location: Orbitting Typhon, Hydrus constellation"),
                __("A small green planet orbiting Typhon - once poetically called HD 10180 b. Birthplace of [p_name]. His mother Yve still lives in the family mansion on the surface of Tuolovi.")
            ]
        )
    "The mansion was what you would call ‘grand’, a vision of what an 18th century European rococo palace should look like in the modern age."
    "Lots of synthetic marble, curly gilded ornaments and far too many rooms."
    "A mediocre architect’s wet dream."
    "Ours wasn’t the largest house on Tuolovi, much to my father’s ire, but that’s what you get for wanting to live on a world for people with boatloads of money."
    scene ep001_agust_office with dissolve
    "So, my father: Agust Algerone Arlington Valenmann de Lonval, wealthy bigwig of the trading and manufacturing company VLCo."
    python:
        if game.is_special:
            codex_agust = add_codex_entry(
                Codex,
                __("Characters"),
                __("Agust Valenmann de Lonval"),
                [

                    __("Agust Algerone Arlington Valenmann de Lonval, wealthy CEO of the trading and manufacturing company VLCo, father to [p_name], Lilly and Eva.")
                ],
                "images/codex/Agust.webp"
            )
        else:
            codex_agust = add_codex_entry(
                Codex,
                __("Characters"),
                __("Agust Valenmann de Lonval"),
                [

                    __("Agust Algerone Arlington Valenmann de Lonval, wealthy CEO of the trading and manufacturing company VLCo, father to [p_name].")
                ],
                "images/codex/Agust.webp"
            )

        codex_vlco = add_codex_entry(
            Codex,
            __("Organizations"),
            __("VLCo."),
            [
                __("Location: Tooles Folly (HD 154857 c), Ara Constellation"),
                __("An intergalactic trading and manufacturing company founded by the Valenmann family and operated by them for centuries. The company has a murky past and regularly engages in questionable activity, though most of it is sanctioned by the Terran government. Activities range from trading rare minerals, ship parts to slaves and grey-market biotics.")
            ]
        )
    "The company has been in the family for ages, a successful venture, passing from father to son."
    "The money really started flowing in when Agust fully took over from my granddad."
    "There are rumors about that money though..."
    "Let’s just say the incarnation of VLCo. under the guidance of A. A. A. Valenmann de Lonval likes to operate in the morally grey areas of intergalactic trade."
    "In his role as fruitful entrepreneur, my father married a pop singer when he was really young."
    "I guess everybody does stupid things during that time boys think more with their dicks than anything else..."
    scene expression eye_blink("images/ep001/ep001_yve") with dissolve
    "Anyway, that pop singer was my mother Yve."
    "She wasn't all that talented as an artist."
    "Not like Maria Callas, Ella Fitzgerald or even Britney Spears in her post-human period."
    "But mom had a small hit back in her heydays and her share of fans, most of whom shared her bed sooner or later."
    "I guess wealth also has it’s share of devotees, so my father never came home to an empty bed."
    "Yve was never in it after we were born, that’s for sure."
    python:
        if game.is_special:
            codex_yve = add_codex_entry(
                Codex,
                __("Characters"),
                __("Yve Valenmann de Lonval"),
                [
                    __("Yve Valenmann de Lonval, former pop-star who married Agust at a very young age. Mother of [p_name], Lilly and Eva. She spends her days living in the mansion on Tuolovi entertaining a host of extramarital lovers.")
                ],
            "images/codex/Yve.webp"
            )
        else:
            codex_yve = add_codex_entry(
                Codex,
                __("Characters"),
                __("Yve Valenmann de Lonval"),
                [
                    __("Yve Valenmann de Lonval, former pop-star who married Agust at a very young age. Mother of [p_name]. She spends her days living in the mansion on Tuolovi entertaining a host of extramarital lovers.")
                ],
            "images/codex/Yve.webp"
            )
    "Calling my mom and dad's marriage loveless is an understatement."
    if game.is_special:
        "But my sisters and I were the product of it, so I guess it wasn't all bad."
        "I was mom and dad’s first child and my twin sisters soon followed."
        "They’re twins, but Eva and Lilly couldn’t be more different."
    else:
        "But I was the product of it, so I guess it wasn't all bad."
        "I was mom and dad’s only child, but that’s not to say I was lonely or anything."
        "Our family made use of an extensive staff, some of whom had families of their own living on the grounds of the estate."
        "Eva, Lilly and Aven, the daughters of the cook, gardener and maid respectively, were the children I spent almost my entire childhood with."
        scene ep001_aven with dissolve
        "Aven was the eldest."
        "We were the best of friends, always together, doing stupid shit."
        "That was until our family friend, Nadya, left with her without any notice."
        "And suddenly, none of the adults talked about Nadya and Aven anymore."
        "After a a long period of grieving, Eva and Lilly started to fill that large gap Aven left after her sudden departure."
        python:
            codex_aven = add_codex_entry(
                Codex,
                __("Characters"),
                __("Aven"),
                [
                    __("Aven, childhood friend of [p_name]. Was taken away by Nadya.")

                ],
                "images/codex/Aven-Young.webp"
            )

    scene ep001_eva with dissolve
    "Eva is what you call a kind soul."
    "Not that she’s soft or anything, she can hold her own in a fight, but she’s so open and understanding."
    "I don’t think there’s anybody who didn’t like her back on Tuolovi."
    if game.is_special:
        "Eva and I were often mistaken for twins, because we were always playing together when we were younger."
    python:
        if game.is_special:
            codex_eva = add_codex_entry(
                Codex,
                __("Characters"),
                __("Eva"),
                [
                    __("Eva Valenmann de Lonval, sister of Lilly and [p_name].")
                ],
                "images/codex/Eva.webp"
            )
        else:
            codex_eva = add_codex_entry(
                Codex,
                __("Characters"),
                __("Eva"),
                [
                    __("Eva Arderne, childhood friend of [p_name].")
                ],
                "images/codex/Eva.webp"
            )
    scene ep001_lilly with dissolve
    "Now Lilly is a different story."
    "People often say that her fiery hair matches her volatile character and they’re right."
    "I would go even further and say she’s a bitch, or was a bitch..."
    "I don’t know."
    "Let’s just say Lilly and I have a complicated relationship."
    if game.is_special:
        "The fact that mother and father mostly doted on her, the youngest of us three, while ignoring us mostly, didn't help at all."
        "All the positive attention Lilly got from Agust and Yve didn’t change the fact that she, like me and Eva, was sent to the Terran Galactic Naval Academy in Alpha Centauri at the age of sixteen."
    else:
        "The fact that her father mostly doted on her didn’t help at all."
        "All the positive attention Lilly got from her father didn’t change the fact that she, like me and Eva, was sent to the Terran Galactic Naval Academy near Alpha Centauri at the age of sixteen."
    python:
        if game.is_special:
            codex_lilly = add_codex_entry(
                Codex,
                __("Characters"),
                __("Lilly"),
                [
                    __("Lilly Valenmann de Lonval, sister of Eva and [p_name].")
                ],
                "images/codex/Lilly.webp"
            )
        else:
            codex_lilly = add_codex_entry(
                Codex,
                __("Characters"),
                __("Lilly"),
                [
                    __("Lilly Elyot, childhood friend of [p_name].")
                ],
                "images/codex/Lilly.webp"
            )
    scene ep001_uniforms with dissolve
    "I was the first to go. Eva and Lilly followed a year later."
    "Due to some unfortunate circumstances, which might have involved insulting a senior officer, I was forced to repeat the first year."
    if game.is_special:
        "I actually didn’t mind, because I got to be with my sisters again."
    else:
        "I actually didn’t mind, because I got to be with my friends again."
    "We were still the youngest at the academy, as most students enroll at age eighteen."
    "But Agust and Yve made it very clear to us that they were very eager to see us gone as soon as legally possible."
    "I was told naval academy would teach me some much needed discipline, but I’m not sure what the excuse was in Eva and Lilly’s case."
    "At any rate, we all weren’t very happy at the academy."
    if game.is_special:
        "Eva originally dreamed of going to university to become a scientist and Lilly probably just wanted to stay on Tuolovi with Mummy and Daddy and annoy the living hell out of people."
    else:
        "Eva originally dreamed of going to university to become a scientist and Lilly probably just wanted to stay on Tuolovi with her daddy and annoy the living hell out of people."
    python:
        codex_tgn = add_codex_entry(
            Codex,
            __("Organizations"),
            __("Terran Galactic Navy"),
            [
                __("The Terran Galactic Navy (TGN) is the name for the intergalactic fleet that keeps the peace in the human territories, collectively called the Sovereignty. Special divisions of the TGN are also occupied with conquering of new worlds, though the expansion of the Sovereignty has stagnated in recent years.")
            ]
        )
    scene ep001_ypotrill with dissolve
    "After two years of training the Terran Galactic Navy traditionally sends its fresh recruits on a training expedition."
    "Think of it as summer camp, but with heavy weapons training."
    "We were flown by the Battle Cruiser TGN Ypotryll to a dreary moon in a system neighboring the academy to do some humanitarian field work."
    "That’s when everything turned to total and utter shit..."

    play music "music/grim-league.ogg" fadein 1.0 fadeout 4

    scene ep001_ypotrill_lanan with fade:
        yalign 0
    call location_screen (__("Lanan P-10, Beta Centauri, Orbit"), True) from _call_location_screen_1
    "It all started innocently enough."
    "As soon as the Ypotryll was in orbit of Lanan, commander Szuzume ordered all recruits to the shuttle bay where transport to the surface of the moon was already waiting for us."
    scene expression eye_blink("images/ep001/ep001_calista") with dissolve
    ca "Listen up everyone."
    ca "Today is your first real assignment."
    ca "You’ve trained for this and you are ready, or you better be."
    ca "You’ll be divided in groups and shuttled to Lanan P-10, where you will be given your assignments."
    ca "Contact with mission control is forbidden until completion of your assignment or in case of absolute emergencies."
    ca "Small injuries or homesickness do not, I repeat, do not count as valid reasons for reaching out to mission control."
    ca "If you want to cry for mommy or daddy, do it at night when everyone else is asleep."
    ca "Now, your names will be called and you will assemble at the relevant shuttle."
    ca "Good luck out there."
    scene ep001_calista_list with dissolve
    ca "Group Alpha: Baudrillard, Kristeva, Butler, Kofman..."
    "Commander Calista Szuzume didn’t like me from the start."
    "It was very clear that she didn’t like me as a naval cadet, nor as a friend to her son Kit and her daughter Céline."
    "I don’t know when and how I ended up on her shit list, but she made it clear that my name was up there in shiny golden letters on many occasions."
    "Commander Szuzume probably didn’t appreciate that I liked to play fast and loose with the rules at the academy from time to time."
    "Like shaking up the group roster for a training mission."
    python:
        codex_calista = add_codex_entry(
            Codex,
            __("Characters"),
            __("Calista Szuzume"),
            [
                __("Commander Calista Szuzume is the captain of the Battle Cruiser TGN Ypotryll and the mother of Céline and Kit. She has a particular dislike for [p_name].")
            ],
            "images/codex/Calista.webp"
        )
    if game.is_special:
        ca "Group Kappa: Valenmann de Lonval, E. Valenmann de Lonval, L. Valen..."
    else:
        ca "Group Kappa: Arderne, E. Elyot, L. Valen..."
    scene ep001_calista_angry with vpunch
    ca "What the?!"
    ca "...Valenmann de Lonval, C. Szuzume, K. Szuzume C. and Von Skandersfelt."
    ca "Get your asses to that shuttle. "
    ca "We’ll talk about this organizational fuckup later, whomever is responsible..."
    scene ep001_lilly_kit_hangar with dissolve
    ki "I think you managed to piss my mom off...{w} again."
    c "She didn’t seem very happy, but I really wanted to do this first assignment with you guys."
    l "What the fuck did you do, [p_name_short]?"
    c "I may have persuaded a certain someone with considerable computer skills to change the group assignments..."
    l "You moron!"
    l "There’ll be hell to pay once we get back, for you and her both!"
    l "The Commander made that much clear."
    ki "Let’s just board the shuttle, the others are already strapped in."
    ki "By the way, how did fucking Thim end up with us?"
    c "A coincidence or a touch of sadistic humor on account of my illustrious hacker..."
    scene ep001_ypotrill_transport with dissolve

    play music [ "music/red-mist.ogg", "music/floating-cities.ogg" ] fadeout 4 fadein 1.0

    "The shuttle brought us swiftly to the surface and left us in a clearing where we were supposed to set up our tents."
    scene ep001_tents with fade:
        yalign 0
    call location_screen (__("Basecamp Kappa, Lanan P-10"), True) from _call_location_screen_2

    label ep001_basecamp_conversation:
        scene ep001_tents with dissolve
        menu:
            "Talk to Céline" if not ep001_celine_talk:
                $ ep001_celine_talk = True
                scene expression eye_blink("images/ep001/ep001_tents_celine") with dissolve
                "So I’ve mentioned Céline already, the commander’s daughter and sister to Kit."
                "You could say we had a thing for each other, which is probably one of the reasons her mother hated my guts."
                python:
                    codex_celine = add_codex_entry(
                        Codex,
                        __("Characters"),
                        __("Céline Szuzume"),
                        [
                            __("Céline is the daughter of Calista Szuzume, sister of Kit and a potential love interest of [p_name].")
                        ],
                        "images/codex/Celine.webp"
                    )
                ce "Hey [p_name]."
                ce "I understood from Kit you got us all together on this mission?"
                menu:
                    "I did it for you [CélinePath]":
                        $ celine_romance = True
                        c "I wanted a nice holiday on a romantic moon, together with you."
                        scene expression eye_blink("images/ep001/ep001_tents_celine_happy") with dissolve
                        ce "Haha, you’ve looked around, haven’t you?"
                        ce "The weather here is terrible and I believe Lanan is listed in all the tourist guides as one of the places you should just never visit."
                        c "I agree, but I had to make ends meet."
                        ce "Noted. And I do appreciate the effort."
                        c "Enough to get a kiss?"
                        ce "Maybe...{w} Why don’t you find out later tonight?"
                        c "Isn’t Kit sleeping in the same tent with you?"
                        ce "Who cares, he sleeps like a log, have you ever heard him snore?"
                        c "I did."
                        c "He makes more noise than a Farixillic heavy jet engine."
                        c "Point taken. See you tonight!"
                        "So yeah, we there was definitely something going on with me and her."
                    "I wanted everyone together":
                        c "I just wanted to do this with my friends."
                        ce "That doesn’t explain Thim being here."
                        c "He sure wasn’t on my wish list."
                        ce "Maybe the local wildlife will devour him in his sleep."
                        c "Let’s pray for small miracles."
                jump ep001_basecamp_conversation
            "Talk to Eva" if not ep001_eva_talk:
                $ ep001_eva_talk = True
                scene expression eye_blink("images/ep001/ep001_tents_eva") with dissolve
                e "You’re enjoying yourself far too much, [p_name]."
                c "Is it that obvious?"
                e "The smirk on your face is a dead giveaway."
                c "What can I say, I really like it when I can make things go my own way by doling out a little booze here and there."
                e "You’re going to get into trouble, commander Szuzume made that much clear before we disembarked."
                c "I’m not really worried."
                c "Graduation is right around the corner, after that Szuzume won’t have any hold over us anymore."
                if game.is_special:
                    e "Not so fast, brother, we need to accomplish this mission first."
                else:
                    e "Not so fast, [p_name_short], we need to accomplish this mission first."
                e "And there’s always the possibility of us serving under the commander as ensigns after graduation."
                c "The horror..."
                scene expression eye_blink("images/ep001/ep001_tents_eva_happy") with dissolve
                e "Better stock up on some more booze, maybe you can bribe your way into an admiralty."
                c "Great idea!"
                jump ep001_basecamp_conversation
            "Talk to Lilly" if not ep001_lilly_talk:
                $ ep001_lilly_talk = True
                scene expression eye_blink("images/ep001/ep001_tents_lilly") with dissolve
                l "What now [p_name]?"
                l "You’ve got your way, as always and I have zero desire to talk to you."
                c "Just checking in. Have you read the mission brief already?"
                l "Yes, and you?"
                c "Not yet."
                l "You’re not fishing for a summary of the brief, are you?"
                c "Can’t a guy just have a friendly chat with a girl?"
                if game.is_special:
                    l "Yes, but you’re my brother and I know the shit you’re up to mostly."
                else:
                    l "Yes, but I know you [p_name_short] and I know the kind of shit you’re up to mostly."
                l "Read the mission brief for yourself and don’t bother me, I’ve got things to do."
                c "Okay then..."
                "I would have liked to say Lilly wasn’t always like that, but it seems she was always angry at something..."
                jump ep001_basecamp_conversation
            "Talk to Kit" if not ep001_kit_talk:
                $ ep001_kit_talk = True
                scene expression eye_blink("images/ep001/ep001_tents_kit") with dissolve
                ki "Hey man, ready for some fun?"
                c "Setting up a tent in this godforsaken place isn’t my idea of fun, Kit."
                ki "Well, maybe we’ll get lucky and get to shoot something."
                c "Boy, you’re really eager to massacre the locals..."
                scene expression eye_blink("images/ep001/ep001_tents_kit_smile") with dissolve
                ki "No, no, but maybe we can hunt some wildlife?"
                c "I don’t think there’s time for that."
                ki "Shame."
                ki "Maybe when we get some downtime after this we could go to that forest moon everybody’s talking about, shoot some deer?"
                c "Trudging through the mud with a hunting rifle for several days?"
                c "I think I’ll pass."
                c "I just want a nice beach and several bikini-clad girls, willing and eager to sit on my lap preferably."
                ki "Sounds fun too!"
                "Kit was the first friend I made at the academy and became one of my best friends."
                "He even fucked up his exams on purpose in our first year so that we could stay in the same class together."
                if game.is_special:
                    "A really stupid move, of course, but it all worked out in the end as we were joined by our sisters."
                else:
                    "A really stupid move, of course, but it all worked out in the end as we were joined by our friends."
                "Kit’s interests veered towards the more extreme sports, like mountaineering, paragliding and martial arts."
                "So much he was even considered for advanced training as a specialist, instead of the officer track we were all preparing for."
                "This unhealthy appetite for dangerous athletics meant I often had to accompany him to some uninhabitable planet where we tried not to get killed while hanging from a single rope against a crater wall."
                "Apart from the near-death experiences on barren worlds, we also had fun in the many bars and clubs on Alf Cen."
                "Man, the amount of pussy we had during our furlough could fill a small space station..."
                python:
                    codex_kit = add_codex_entry(
                        Codex,
                        __("Characters"),
                        __("Kit Szuzume"),
                        [
                            __("Kit is the son of Calista Szuzume, brother of Céline and one of [p_name]'s best friends. Partly due to his interest in the more extreme sports he was considered for advanced training at the TGN Academy.")
                        ],
                        "images/codex/Kit.webp"
                    )
                jump ep001_basecamp_conversation
            "Talk to Thim" if not ep001_thim_talk:
                $ ep001_thim_talk = True
                scene expression eye_blink("images/ep001/ep001_tents_thim") with dissolve
                "Thim..."
                "Thim with a fucking ‘h’..."
                "I think it’s fair to say we pretty much hated each other from the start."
                "Remember my family descended from a long line of nobility?"
                "Well, Thim is fucking worse."
                "Apparently he can trace his lineage to some European royal family dating back to the Middle Ages..."
                "Combine that fact with boundless arrogance and you’ve got Thim."
                python:
                    codex_thim = add_codex_entry(
                        Codex,
                        __("Characters"),
                        __("Thim von Skandersfelt"),
                        [
                            __("Thim is a fellow student at the TGN Academy. His family can trace its lineage all the way back to a Nordic royal family dating back to the Middle Ages.")
                        ],
                        "images/codex/Thim.webp"
                    )
                t "Fuck off."
                c "Hello to you too."
                c "Looks like we’ll have to share a tent together."
                t "I said: fuck off."
                "We had some really great conversations, Thim and I."
                "Truth is, he was popular in some circles and he sure wasn’t a bad student."
                if game.is_special:
                    "But for some reason he was always hovering around my sisters."
                else:
                    "But for some reason he was always hovering around my friends."
                "Especially Eva, and even Céline for a while, who all ignored him mostly."
                "I guess that made him extra bitter."
                jump ep001_basecamp_conversation

    scene ep001_tents_team with dissolve
    "After setting up the tents and preparing a campfire everyone gathered together."
    "I had to read the mission brief first, so I arrived a little later when everyone had gotten into an argument already about what to do next."
    t "We should head out now. Nip the problem in the bud right away."
    l "Are you crazy? It’s getting dark soon. The locals can wait."
    e "The problem seems urgent."
    ce "They’ve been coping with it for a few weeks already, so one night isn’t going to be a problem, surely."
    "We were tasked by mission control to investigate repeated attacks on cattle at a settlement a couple of miles from our campsite."
    "The attacks were likely caused by a pack of animal predators coming from the nearby mountain range preying on the livestock."
    "Nothing a few well-placed explosives or targeted rifle fire couldn’t handle."
    c "Lilly is right. We should catch some sleep first."
    c "We’re no good to the locals in the middle of the night."
    scene ep001_tents_team_thim with dissolve
    t "The attacks are happening at night!"
    t "You would have known if you even bothered to read the entire mission brief."
    c "I did read the entire brief."
    c "What do you want to do?"
    c "Shoot up the place in the middle of the night when the beasts arrive to hunt for some farm animals?!"
    c "What if some dimwit from the settlement gets curious and steps into the firing line to see if Daisy the Prize-winning cow isn’t too stressed out by the whole ordeal?"
    scene ep001_tents_team_kit with dissolve
    ki "I vote we go in the morning and look for any tracks instead."
    scene ep001_tents_team_eva with dissolve
    e "Sounds reasonable."
    c "Okay, let’s get some sleep then and show some serious heroics in the morning."
    scene ep001_tents_night with dissolve
    "I’ve already mentioned that the training expeditions were more like summer camp than actual heavy duty missions."
    "It’s what you get when you send out a group of teenagers all on their own, without direct oversight."
    "My guess is that night, all over Lanan P-10 a lot of recruits experienced some very happy moments with each other."
    if celine_romance:
        "Our camp was no exception, at least in my case..."

    label ep001_basecamp_night:
        scene ep001_tents_night with dissolve
        menu:
            "Go to Céline" if celine_romance and not ep001_c_visit:
                $ ep001_c_visit = True
                "I admit my heart was beating heavily in anticipation as I approached Kit and Céline’s tent."
                "I’m pretty sure Kit was okay with Céline and me being an item, but actually diddling his sister in his own tent is of course another matter..."
                "Kit’s rhythmic snoring bolstered my confidence when I slowly pulled the zipper of the tent upward."

                call ep001_celine_sex from _call_ep001_celine_sex

                c "I know."
                ce "We should do this another time."

                menu:
                    "Certainly":
                        c "That sounds like a great idea."
                        scene ep001_tents_celine_camran_fucking_post_closeup with dissolve
                        ce "Okay, when we’re back on the Ypotryll I’ll show you something."
                        c "I can’t wait to hear you moan out loud."
                        ce "I can scream too, be warned!"
                        "I kissed Céline goodnight and hurried back to my tent."
                        "Lucky for me, Thim was still asleep."
                    "Better not [EndRelationship]":
                        $ celine_romance = False
                        $ celine_rejected = True
                        c "This was a one-time only deal for me."
                        scene ep001_tents_celine_camran_fucking_post_angry with vpunch
                        ce "What?! You fucking bastard!"
                        ce "Leave!"
                        "Céline clearly didn’t subscribe to my one-night stand philosophy and things never really recovered between us."
                        "I hurried back to my tent."
                        "Lucky for me Thim was still asleep."
                jump ep001_basecamp_night
            "Visit Céline" if not celine_romance and not ep001_c_visit:
                $ ep001_c_visit = True
                $ ep001_c_spy = True
                scene ep001_tents_celine_kit_sleeping with dissolve
                "Céline was already fast asleep when I visited her, Kit snoring loudly next to her."
                "I thought Céline and I had a thing going on, but after that day her interest in me seemed to wane."
                "She was a beautiful girl though, a fact I was reminded of when I admired her lithe body in the artificial light of my lantern."
                jump ep001_basecamp_night
            "Visit Eva and Lilly" if not ep001_e_l_visit:
                $ ep001_e_l_visit = True
                $ ep001_e_l_spy = True
                scene ep001_tents_lilly_eva_sleeping with dissolve
                "In preparation for the busy day ahead, Lilly and Eva must have gone to bed early, as they were already sleeping when I came by their tent."
                if game.is_special:
                    "After being separated for over a year from my sisters I was struck by their beauty when they finally joined me at the academy."
                else:
                    "After being separated for over a year from my friends I was struck by their beauty when they finally joined me at the academy."
                "When I left, both girls were typical lanky teenagers, but the Eva and Lilly that greeted me on the first day of the new school year were powerful gorgeous young women."
                scene ep001_tents_lilly_eva_sleeping_closeup with dissolve
                if game.is_special:
                    "Sure, Mom and Dad got the best gene treatments for their fetuses, but the well-toned bodies of my sisters were only in part due to modern-day genetics."
                else:
                    "Sure, Mom and Dad got the best gene treatments, even for their servants, but the well-toned bodies of my friends were only in part due to modern-day genetics."
                scene ep001_tents_lilly_eva_sleeping_closeup_alt with dissolve
                if game.is_special:
                    "I could have admired the exquisite curves of Lilly’s ass or the perky magnificence of Eva’s breasts all night, but spying on family members in the middle of the night is still considered ‘not done’ in human society..."
                else:
                    "I could have admired the exquisite curves of Lilly’s ass or the perky magnificence of Eva’s breasts all night, but spying on people in the middle of the night is still considered ‘not done’ in human society..."
                jump ep001_basecamp_night
            "Go to sleep":
                scene black with fade
                "As soon as my body hit the bedroll I fell into a deep, dreamless sleep."

    scene ep001_tents_morning with dissolve
    "We awoke early in the morning and broke up the tents, expecting that we didn’t have to spend another night on Lanan."
    "After a quick breakfast of the provided rations, we headed out to the settlement."
    scene ep001_eva_celine_walking with dissolve
    e "According to the map it shouldn’t be far from here."
    ce "I didn’t notice those smoke plumes yesterday."
    scene ep001_lilly_kit_thim_walking with dissolve
    t "Those stupid peasants are probably burning stuff to keep warm..."
    l "There sure is a lot of smoke..."
    c "Those are big fires, I doubt it’s just a cooking fire."
    ki "Let’s leave our baggage here and get closer."
    scene ep001_settlement with dissolve
    c "What the..."
    e "Are those..."
    e "...people?!"
    scene ep001_settlement_thim_lilly with dissolve
    t "Burnt to a fucking crisp."
    c "Show some fucking respect, Thim."
    l "It’s a massacre."
    scene ep001_settlement_celine_kit with dissolve
    ki "We should investigate. See if there are any survivors."
    c "Not so fast. Let’s contact mission control first."
    c "Céline?"
    ce "Errr...{w} Yes? What?"
    c "You’re carrying the radio. Could you please contact mission control?"
    ce "Right. You’re right. Sorry."
    c "Don’t apologize, just focus. We’ll have time to grieve for these poor people later."
    scene ep001_settlement_celine_kit_radio with dissolve
    ce "N-nothing. There’s nothing but static?"
    ki "Do you have the right frequency?"
    ce "Yes! Something seems to be jamming all frequencies."
    c "Fuck, that means the people who caused this slaughter are still on the moon’s surface."
    ce "What should we do?!"
    c "This settlement might actually be a defensible position."
    c "We need to clear every building, and search for any remaining threats or survivors."
    c "Lilly, Eva, Thim, you clear the outer perimeter. Kit, Céline and I will investigate the buildings and keep trying that damn radio."
    scene ep001_settlement_celine_kit_walk with dissolve
    "Most buildings were already reduced to cinders or too dangerous to even enter because of all the fire. Two houses were more or less intact and empty."
    "It wasn’t until we searched the huts at the back of the settlement that we found our first sign of life."
    scene ep001_settlement_celine_kit_man with dissolve
    "The man hiding in the dirty hovel was clearly too shocked to say a word."
    "The relief was visible in his eyes, though, when he was guided from his former home, supported by Kit."
    scene ep001_settlement_girls with dissolve
    "In the next hut, we encountered a similar scene."
    "Two girls were hiding beneath a table, shivering with fear and unable to speak."
    "They clearly didn’t consider us to be a danger and came with us to the entrance of the settlement."
    scene ep001_settlement_people with dissolve
    ki "What now?"
    c "We wait for the others to return."
    c "Check if any of the survivors need any medical attention."

    play music "music/venom.ogg" fadein 1.0 fadeout 4

    scene ep001_settlement_people_shock with vpunch
    "Right at that moment we were shocked by the sounds of gunfire from the vicinity where I sent Lilly, Eva and Thim."
    ce "What the fuck is that?!"
    c "The other group is under fire. Hurry!"
    scene ep001_settlement_running with dissolve
    "We ran towards the commotion, ready to shoot at anything."
    scene ep001_warrior with dissolve
    "What we found, was a mixture of both horror and comedy."
    "Lilly was being threatened by a muscular woman dressed in outrageous armor, carrying a huge sword."
    "It was as if she had walked straight out of some bad fantasy movie."
    "But the threat was very real."
    "Another similarly clad woman stood close by Thim, who sat slumped against a tree, unconscious or dead."
    scene ep001_warrior_closeup with dissolve
    "Both women were looking at us, grinning, as if daring us to make a move."
    c "Hold your fire!"
    ce "[p_name]! Look!"
    scene ep001_warrior_eva with dissolve
    "That’s when I saw another warrior carrying Eva on her shoulder towards the jungle."
    c "Eva!"
    scene ep001_warrior_eva_kit_running with dissolve
    "Probably driven by instinct, Kit tried to do something heroic."
    "He rushed towards Eva..."
    scene ep001_warrior_eva_kit with vpunch
    "And found himself impaled on a sword."

    $ woman_name = "Warrior"
    scene ep001_warrior_closeup with dissolve
    woman "Don’t try anything stupid."
    "Her accent was thick, but I understood her well enough."
    c "Let her go!"
    woman "I’ll let this one go, if you behave."
    if game.is_special:
        "I stood helpless as the woman disappeared with my sister in the wilderness, my gaze alternating from Lilly to Kit bleeding on the ground."
    else:
        "I stood helpless as the woman disappeared with my friend in the wilderness, my gaze alternating from Lilly to Kit bleeding on the ground."
    scene ep001_warrior_closeup_alt with dissolve
    woman "I’ll take my leave now."
    "She slowly backed away, still grinning."
    "We all stood motionless until she disappeared."
    scene ep001_warrior_lilly_camran with dissolve
    c "Lilly! Are you okay?"
    l "J-just a little rattled."
    c "Don’t you feel that nasty cut near your neck?"
    l "What?"
    l "No..."
    l "[p_name_short], they took Eva!"
    c "I know, we’ll get her back."
    c "Hold on tight, I have to check on Kit first."
    scene ep001_warrior_kit_closeup with dissolve
    ce "Kit?!"
    ce "Why did you run towards her?!"
    c "How bad is it?"
    ce "She stabbed him through his guts, if he doesn’t get medical attention he’ll die!"
    ce "We need to get to a transport ship immediately!"
    c "But Eva! Goddamnit!!!"
    scene ep001_warrior_thim with dissolve
    t "She’s gone man. Nothing you can do about it."
    c "Look who’s decided to conveniently wake up! Shut the fuck up, Thim."
    scene ep001_warrior_kit_closeup with dissolve
    ki "It...{w} It feels so cold..."
    c "Fuck!"
    c "Céline, Thim, can you carry Lilly and get the villagers?"
    ce "No problem, [p_name_short]."
    t "Yes."
    c "Good, I’ll carry Kit."
    c "Try the radio again Céline, we might get lucky and get through to mission control."

    play music "music/echoes-of-time-v2.ogg" fadeout 4 fadein 1.0

    scene black with fade
    "Céline and Thim moved faster than I could, dragging Kit along, who was bleeding like crazy."
    "When I reached the settlement the man and the girls were still standing where we left them, too stunned to act on their own."
    scene ep001_settlement_people_radio with dissolve
    ce "The radio is working again!"
    ce "And mission control sent us coordinates."
    ce "They sounded pretty tense."
    c "Yes, this sure isn’t normal procedure for training missions."
    c "I bet nobody expected an all out surprise attack so close to human space."
    t "Who were those women?"
    c "Beats me."
    c "I’m pretty sure we’ll find out when we’re debriefed by the brass once we’re back on the ship."
    scene ep001_settlement_people_walking with dissolve
    "The coordinates we received were several miles away from our position."
    "The trek took several hours, because the wounded slowed us down."
    scene ep001_transport_evacuate with dissolve
    "When we arrived at the rendezvous point, several other groups of trainees had already checked in."
    "Many of them carried wounded, or even lifeless bodies with them."
    "The incursion of the warriors seemed to have happened simultaneously on the surface of the entire moon."
    "An officer motioned us to enter a transport ship and after what seemed like ages we were finally lifted off the surface of Lanan to the safety of the Ypotryll."
    python:
        codex_warrior_women = add_codex_entry(
            Codex,
            __("Species"),
            __("The Warrior Women"),
            [
                __("First encountered on Lanan P-10 during a full-scale attack on TGN personnel, abducting a great many of them. The women appear muscular and wear elaborate armor and seem to prefer fighting with relatively crude melee weapons.")
            ],
            "images/codex/WarriorWomen.webp"
        )

    play music "music/echoes-of-time.ogg" fadeout 4 fadein 1.0

    scene ep001_ypotrill_transport_alt with fade
    call location_screen (__("TGN Ypotryll"), True) from _call_location_screen_3
    "Everyone was silent during our return trip, except for the moans of the badly injured."
    "As soon as we landed in the belly of the Ypotryll and the doors of the transport opened, medical personnel streamed in."
    "They began to take care of the many wounded, concentrating on the most critical first."
    "I slipped out, making room so that they could accomplish their tasks."
    scene ep001_camran_barracks with dissolve
    "A little disoriented, I decided to retire to my bunk."
    "Before I could lie down properly and collect my thoughts I heard the door slide open."
    j "Master [p_name]? Are you okay?"
    scene ep001_camran_barracks_jade with dissolve:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "Ah, Jade."
    "Lovely Jade."
    scene expression eye_blink("images/ep001/ep001_jade") with dissolve
    "My personal attendant, since my sixteenth birthday when Dad bought her for me as a coming-of-age birthday present."
    python:
        codex_jade = add_codex_entry(
            Codex,
            __("Characters"),
            __("Jade"),
            [
                __("Short for Jade'anna N'ec L'ordann va T'olnec. [p_name]'s personal Twi'll attendant, given to him on his sixteenth birthday.")
            ],
            "images/codex/Jade.webp"
        )
    "She's a Twi'll."
    "Officially she's called Jade'anna N'ec L'ordann va T'olnec, but Jade is much shorter when I cry out her name during sex."
    "Tw'ills, females and males, are a valuable commodity in modern day society."
    "They're commonly held as sex slaves."
    "Despite the fact that the whole Tw'ill race is portrayed as a degenerate species by the Department of Interplanetary Exploration, people sure want to fuck them real bad."
    "Their intelligence, well-toned humanoid bodies and fantastic skills between the bedsheets really speak volumes against any claim of degeneracy, but who am I to judge..."
    scene ep001_twill with dissolve
    "The Twi'll were the first species mankind encountered, during the first intergalactic space explorations."
    "They’re a peaceful race, not accustomed to warfare, so naturally we laid waste to their planet, killed nearly eighty percent of their population and enslaved the rest."
    "I’m not sure if that Lucas-guy, who envisioned the Tw'ills hundreds of years before we encountered them, would appreciate what we did and that we named our newly enslaved species in honor of his little-known series of science-fiction movies."
    "His epic about a duck named Howard is more popular anyway."
    "There's really no accounting for taste..."
    "Most people treat their Tw'ill slaves like shit. I try not to be an asshole to Jade and show her some respect, that seems to have worked out for us so far."
    python:
        codex_twill = add_codex_entry(
            Codex,
            __("Species"),
            __("Twi'll"),
            [
                __("Tw’ill were the first alien species the human race encountered on their initial explorations outside the known galaxy. The intelligent, benign race of humanoids were promptly enslaved by the Terran invaders and their homeworld Luclite orbiting Xut Thanaili was destroyed. 80% of the populace were wiped out and the rest of them (male and female) are commonly held as sex slaves by wealthy Terran individuals."),
                __("The race was named Tw’ill due to their likeness of a certain species in a movie trilogy that has waned in popularity over the centuries.")
            ],
            "images/codex/Twill.webp"
        )
    scene ep001_camran_barracks_jade_sit with dissolve
    c "I’m fine. I think."
    c "Hell, I don’t know."
    c "I think she’s gone Jade..."
    j "Who is?"
    if game.is_special:
        c "My sister."
    else:
        c "Eva..."
    j "Mistress Eva?"
    if not game.is_special:
        c "Who else?"
    c "Yes, we were ambushed on Lanan and they took her."
    j "Where?"
    c "To their ships, I don’t know."
    j "I should’ve cancelled the whole mission while I was in their systems."
    c "Jade...{w} You’re good with computers, but you’re not that good."
    j "I know..."
    j "But surely the navy is going after them, to intercept those vessels."
    c "I don’t think they will, they were as surprised as we were."
    j "But she was still alive when you last saw her?"
    c "She was."
    j "Don’t lose hope then."
    c "I’m trying."
    j "Can I do something to make it easier?"

    menu:
        "Massage me [JadePath]":
            c "I’d like a massage, to alleviate the tension a little."
            j "Certainly."
            scene ep001_camran_barracks_jade_massage with dissolve
            "Jade received training as an attendant, but you could tell she had a skill as masseur which can’t be obtained by just learning."
            "It was almost as if she could attune herself to your body."
            scene ep001_camran_barracks_jade_massage_alt with dissolve
            j "Do you want me to go further?"

            menu:
                "Yes [JadePath]":
                    $ ep001_j_hj = True

                    scene ep001_camran_barracks_jade_massage_naked with dissolve
                    c "Yes, please."
                    call ep001_jade_hj from _call_ep001_jade_hj

                    menu:
                        "Tease her [JadeLovePath]":
                            c "You can be very arrogant, you know that?"
                            scene ep001_camran_barracks_jade_hj_post_smile with dissolve
                            j "I know where my strengths lie and the proof of it coats my chest in abundance."
                            c "Will you lie with me for a while?"
                            j "Of course!"
                            scene ep001_camran_barracks_jade_laying with dissolve
                            "I embraced Jade and just took in her smell, laying there for almost an hour."
                            "My bunkmates came and went, ignoring us mostly, some even had sex with their own attendants."
                            "I dozed off, waking up hours later, feeling the distinct hum of a starship at full throttle immediately."
                            "The Ypotryll was still in orbit of Lanan when I went to sleep, but now we were moving at a brisk speed."
                            c "Go clean yourself up, I have some things to take care of."
                            j "Thank you, master."
                            c "Thank you, Jade."
                        "Scold her [JadeSubPath]":
                            $ ep001_jade_scold = True
                            scene ep001_camran_barracks_jade_hj_post_fear with dissolve
                            c "Don’t take that tone with me, Jade. I’m not in the mood."
                            j "Of course, master. It won’t happen again."
                            "I fell into a deep slumber after Jade left, waking up hours later."
                            "Immediately I felt the distinct hum of a starship at full throttle."
                            "The Ypotryll was still in orbit of Lanan when I went to sleep, but now we were moving at a brisk speed."
                "Not now":
                    c "Just lie with me, I just want someone to hold close."
                    scene ep001_camran_barracks_jade_laying_alt with dissolve
                    "So we just lay there, my face buried in her soft, cool skin."
                    "She stroked my hair and I cried until I fell asleep."
                    "I woke up hours later, feeling the distinct hum of a starship at full throttle immediately."
                    "The Ypotryll was still in orbit of Lanan when I went to sleep, but now we were moving at a brisk speed."
                    c "I have to take care of some things, Jade."
                    j "I understand, thank you, master."
                    c "Thank you, Jade."
        "Just lie with me":
            c "Just lie with me, I just want someone to hold close."
            scene ep001_camran_barracks_jade_laying_alt with dissolve
            "So we just lay there, my face buried in her soft, cool skin."
            "She stroked my hair and I cried until I fell asleep."
            "I woke up hours later, feeling the distinct hum of a starship at full throttle immediately."
            "The Ypotryll was still in orbit of Lanan when I went to sleep, but now we were moving at a brisk speed."
            c "I have to take care of some things, Jade."
            j "I understand, thank you, master."
            c "Thank you, Jade."
        "No thank you":
            c "I’m not really in the mood."
            c "I’m going to rest for a while."
            j "I understand, you know where to find me."
            scene ep001_camran_barracks_laying with dissolve
            "I fell into a deep slumber after Jade left, waking up hours later."
            "Immediately I felt the distinct hum of a starship at full throttle."
            "The Ypotryll was still in orbit of Lanan when I went to sleep, but now we were moving at a brisk speed."

    "I decided to head to the sickbay and see how Lilly and Kit were doing. Kit’s wound was very bad, but if the medics got to him in time he might have made it."
    scene ep001_medbay with dissolve
    "The sickbay was packed to the brim with wounded recruits."
    "Commander Szuzume was coming out of one of the private medpods, probably the one where her son was lying."
    scene expression eye_blink("images/ep001/ep001_kit_calista") with dissolve
    c "Commander."
    ca "Valenmann."
    c "Is Kit going to make it, ma’am?"
    ca "The doctors say he will."
    ca "They had him in a medically induced coma, but now he’s sleeping."
    c "What happened on Lanan..."
    ca "Was a terrible tragedy."
    c "We are going back for the others, aren’t we, ma’am?"
    ca "I will not comment on the orders we received from Central Command."
    if game.is_special:
        c "But they have my sister, we have to do something!"
    else:
        c "But they have my friend Eva, we have to do something!"
    scene expression eye_blink("images/ep001/ep001_kit_calista_angry") with dissolve
    ca "Don’t take that tone with me, boy or I’ll have you thrown into the brig."
    ca "I haven’t forgotten that little stunt you pulled before flying out to Lanan."
    ca "I’ll deal with you later."
    "The recent events sure didn’t bring Commander Szuzume and me closer together..."
    "I decided to ignore her for the moment."

    label ep001_medbay:
        scene ep001_medbay with dissolve
        menu:
            "Visit Kit" if not ep001_medbay_kit_visit:
                $ ep001_medbay_kit_visit = True
                scene ep001_kit_medbay with dissolve
                "Kit was lying peacefully and Szuzume had said he would recover, but everything still looked so very frail."
                c "You stupid, stupid ass!"
                c "We’re going to shoot those deer or climb some stupid rock you’re always going on about."
                c "Just don’t die on me!"
                jump ep001_medbay
            "Talk to Thim [ThimPath]" if not ep001_medbay_thim_talk and not ep001_medbay_thim_ignored:
                $ ep001_medbay_thim_talk = True
                scene expression eye_blink("images/ep001/ep001_thim_medbay") with dissolve
                c "Hey Thim, how are you?"
                t "Like you care."
                c "I do, actually."
                t "Go fuck yourself, [p_name]."
                "Obviously pissed off at me, Thim just stared into the distance."
                jump ep001_medbay
            "Ignore Thim" if not ep001_medbay_thim_talk and not ep001_medbay_thim_ignored:
                $ ep001_medbay_thim_ignored = True
                "Talking to Thim was the last thing I wanted."
                "I couldn’t bear seeing that smug face."
                "So I ignored him."
                jump ep001_medbay
            "Talk to Lilly" if not ep001_medbay_lilly_talk:
                $ ep001_medbay_lilly_talk = True
                scene expression eye_blink("images/ep001/ep001_lilly_medbay") with dissolve
                c "How are you feeling?"
                l "Fine..."
                scene expression eye_blink("images/ep001/ep001_lilly_medbay_fear") with dissolve
                l "Eva! Where is she?!"
                c "They took her, Lilly..."
                l "Is she dead?"
                c "I don’t know."
                c "They left with her."
                scene expression eye_blink("images/ep001/ep001_lilly_medbay_sad") with dissolve
                l "That woman knocked me out."
                l "Eva tried to fight her, but there were too many."
                c "They stabbed Kit."
                c "What happened back there, Lilly?"
                scene expression eye_blink("images/ep001/ep001_lilly_medbay_smile") with dissolve
                l "We were checking the perimeter, like you ordered."
                scene expression eye_blink("images/ep001/ep001_lilly_medbay_sad") with dissolve
                l "And suddenly they came streaming out of the forest, screaming like demons."
                scene expression eye_blink("images/ep001/ep001_lilly_medbay_smile") with dissolve
                l "Demons with swords, straight from those movies about the Middle Ages."
                l "We tried to shoot them, but they were upon us in seconds."
                l "Thim was knocked back against a tree and someone hit me with the flat of a sword."
                l "That’s all I remember."
                c "We found you just after that happened."
                c "They took Eva and left."
                c "And we carried you back to the transports."
                c "I think this happened all over the moon, one large ambush."
                scene expression eye_blink("images/ep001/ep001_lilly_medbay_serious") with dissolve
                l "But why?"
                c "Beats me, but I intend to find out."
                c "We seem to be going somewhere as well."
                c "I sure as hell hope we’re pursuing those Medieval bitches."
                l "We’ll figure something out together."
                l "The doctors say I’ll be out of here in a day or two."
                l "Please don’t do anything stupid."
                "Of course I was planning on doing just that."
                c "I’ll try to stay out of trouble."
                jump ep001_medbay
            "Leave medbay" if (ep001_medbay_thim_talk or ep001_medbay_thim_ignored) and ep001_medbay_lilly_talk and ep001_medbay_kit_visit:
                $ ve_name = "Girl"
                "I felt a soft hand on my arm as I was about to leave the infirmary, it was one of the girls we rescued from the village."
                scene expression eye_blink("images/ep001/ep001_medbay_girl") with dissolve
                ve "You're [p_name], right?"
                ve "I wanted to thank you, for saving us."
                c "No problem, it was the least we could do."
                c "How are you feeling...{w} eh...{w} miss?"
                ve "I'm okay."
                c "And the others?"
                ve "We lost track of each other when we disembarked."
                c "They were your family?"
                c "I could go look for them?"
                ve "No, other people from my village."
                scene expression eye_blink("images/ep001/ep001_medbay_girl_sad") with dissolve
                ve "My family got taken by those women."
                c "Fuck, that’s harsh."
                if game.is_special:
                    c "They got my sister."
                else:
                    c "They got one of my best friends."
                scene expression eye_blink("images/ep001/ep001_medbay_girl_fear") with dissolve
                ve "What's going to happen to them, [p_name]?"
                c "I don't know..."
                ve "There'll be a rescue operation, won't there?"
                ve "They have to do something!"
                c "I'm going to find out."
                c "I'll let you know as soon as I know more."
                scene expression eye_blink("images/ep001/ep001_medbay_girl") with dissolve
                ve "Thank you."
                c "You're welcome...{w} miss..."
                $ ve_name = "Vess"
                ve "Vess, my name is Vess."
                c "You're welcome, Vess."
                python:
                    codex_vess = add_codex_entry(
                        Codex,
                        __("Characters"),
                        __("Vess"),
                        [
                            __("Vess is a girl [p_name] encountered during the botched operation on Lanan P-10, helping her escape on a transport to the TGN Ypotryll. Her family was taken when the Warrior Women invaded the moon.")
                        ],
                        "images/codex/Vess.webp"
                    )

    $ man_name = "Guard"
    scene black with fade
    "I decided to pay Commander Szuzume a visit on the bridge, perhaps in a fool-hearted attempt to play on her emotions and convince her to help the abductees."
    scene ep001_officer with dissolve
    man "State your business."
    c "I have a message for the Commander."
    man "You can deliver it to me."
    c "It’s for her ears only."
    man "Commander Szuzume has explicitly forbidden any interruptions while we travel back to the academy."
    c "We’re going back to the academy?! "
    c "But the attack on Lanan?"
    c "Why are we not pursuing the attackers?!"
    c "You have to let me in."
    man "You’re testing my patience, boy."
    man "We have our orders from high command, you will be briefed as soon as we reach the academy."
    "I could have punched that smug bastard in the face."
    "Every minute we travelled any hope of finding a trace of Eva dwindled."
    "Instead, I said nothing and just walked away."
    man "Hey, soldier?! Didn’t you have a message for the Commander?"
    scene ep001_mess_camran with dissolve
    "I sat in the mess hall, barely touching my food and listening to the conversations of the people gathered there."
    "I already knew the attacks happened everywhere on Lanan and came out of nowhere."
    "Several recruits lost a team member, a lot of them women, but a fair share of men were also abducted."
    "The atmosphere of resignation finally became too much for me and I retired to my bunk."
    scene ep001_camran_barracks_thinking with dissolve
    "I tried to get some sleep again, but instead I remained awake, a desperate plan forming in my head."

    scene ep001_medbay_alt with dissolve
    "I went back to the medbay immediately, expecting to find Lilly and a comatose Kit there."
    "Instead, Lilly and Céline were hovering around Kit’s bed."
    "Both Thim and the girl, Vess, were nowhere to be found, they were probably released from the medbay earlier."
    scene ep001_kit_celine_lilly_medbay with dissolve
    c "Kit?!"
    c "How did you?"
    ki "Superior genes."
    c "Somebody rammed a sword through you, I somehow doubt that your perfect genes would have any significant effect."
    ki "The doctor says I’ll make a speedy recovery, provided I rest enough."
    c "Great!"
    c "I hate to ask this, but can you walk?"
    scene ep001_kit_celine_lilly_medbay_worried with dissolve
    ki "Walk? Why?"
    l "He just said the doctors told him to rest enough."
    c "I know, but this is important."
    c "Are you able to walk, Lilly?"
    l "I think so."
    scene ep001_kit_celine_lilly_medbay_annoyed with dissolve
    l "What are you playing at, [p_name]?"
    c "Meet me at hangar deck 2 at midnight, I’ll tell you then."
    scene ep001_kit_celine_lilly_medbay_worried with dissolve
    ki "I’ll be there, man."
    ki "You’ll carry me, right, Céline?"
    ce "I’m sure we can find a wheelchair somewhere."
    ki "I hadn’t thought of that."
    ce "Of course you didn’t."
    ki "Cut me some slack, sis, I wonder how quick your mind works when they puncture you with a big ass sword."
    scene ep001_kit_celine_lilly_medbay_annoyed with dissolve
    c "Will you be there, Lilly?"
    l "This is crazy."
    c "Lilly?"
    l "Fine. I’ll be there."
    l "But just to hear you out."
    c "Fair enough."
    "I'm sure I left them a little confused and very worried..."
    "On the way back to my bunk I messaged Jade to come to the meeting point."
    scene ep001_camran_barracks_laying with dissolve
    "The hours until midnight slowly passed by."
    scene ep001_hallway with dissolve
    "As the crew of the ship retired for the night I headed out to the hangar deck."
    scene expression eye_blink("images/ep001/ep001_hallway_thim") with vpunch
    t "[p_name]?"
    t "What are you doing out here at night?"
    "Of course he had to be there..."
    c "I could say the same of you."
    t "Fair enough."
    t "I'll leave you alone then."
    c "Good."
    scene ep001_hallway with dissolve
    "After making sure Thim went his way, I sped to the hangar deck, only to be interrupted by another familiar face."
    scene expression eye_blink("images/ep001/ep001_hallway_vess") with vpunch
    ve "[p_name]?"
    c "Vess?"
    c "What are you doing here, late at night?"
    ve "I was looking for you."
    ve "Do you have any news?"
    ve "Is there going to be a rescue mission?"
    c "No, there isn't."
    c "We're going back to the academy and then there'll be a debriefing and that's that."
    scene ep001_hallway_vess_shock with dissolve
    ve "But all those people we lost?!"
    c "I know, Vess."
    scene expression eye_blink("images/ep001/ep001_hallway_vess_sad") with vpunch
    ve "It isn't fair!"

    menu:
        "Tell her about your plan [VessPath]":
            $ ep001_vess_truth = True
            "When she burst into tears like that, I just couldn't leave her there."
            "Some say that women are a man's greatest weakness, I was no exception in that regard."
            c "Listen, don't despair."
            scene expression eye_blink("images/ep001/ep001_hallway_vess_sad_alt") with dissolve
            c "High command might not give a shit about all those people, but I do."
            ve "You do?"
            scene expression eye_blink("images/ep001/ep001_hallway_vess_smile") with dissolve
            c "I'm going to try."
            c "Come with me, we're meeting some of my friends."
            if game.is_special:
                "Together with Vess, I headed to the hangar to find my friends and sister already there."
            else:
                "Together with Vess, I headed to the hangar to find my friends already there."
        "Don't tell her":
            c "I'm sorry, Vess, I wish there was more I could do."
            scene expression eye_blink("images/ep001/ep001_hallway_vess_sad_alt") with dissolve
            "Giving me one last wistful look, the girl turned and fled out of the hallway."
            if game.is_special:
                "I continued to the hangar bay to find my friends and sister already there."
            else:
                "I continued to the hangar bay to find my friends already there."
    if ep001_vess_truth:
        scene ep001_hangar_camran_vess with dissolve
        ki "Is that the girl from the village?"
        c "This is Vess, she lost her family during the assault on Lanan."
        ve "I want to help."
        scene ep001_hangar_jade_lilly_celine_kit with dissolve
        l "Help with what?"
    else:
        scene ep001_hangar_jade_lilly_celine_kit with dissolve
    l "Are you going to tell us what all this cloak and dagger is all about?"
    c "Yes. We've lost someone today."
    c "And high command apparently doesn't give a shit."
    c "We're going back to the academy and there's probably going to be a memorial service for the abductees who're presumed lost."
    c "I don't accept that."
    c "So I intend to get Eva back myself."
    scene ep001_hangar_lilly_celine with dissolve
    l "You what?"
    l "How?"
    c "I'm going to commandeer a ship from this very hangar deck."
    scene ep001_hangar_lilly with dissolve
    l "You've gone mad."
    c "Don't you want her back Lilly?"
    c "Do you accept the fact that we're moving away from Lanan without even knowing what has happened?"
    l "They'll debrief us as soon as we land."
    c "That's too fucking late."
    c "She could be dead by then."
    l "Maybe she already is..."
    c "Don't you dare say that."
    l "I'm..."
    l "I'm sorry, [p_name]."
    scene ep001_hangar_jade_lilly_celine_kit with dissolve
    c "So, are you with me?"
    scene ep001_hangar_kit_celine with dissolve
    ki "What are you asking us exactly, [p_name_short]?"
    c "I'm going to take command of a small ship and I'd like you to be my crew."
    c "I can't do this alone and I know you loved Eva just as much as I did."
    ki "You're asking us to desert from the navy to come with you on some mad rescue mission?"
    c "That sounds so..."
    c "Yes."
    ki "I'm in."
    ce "Kit!"
    ce "What are you doing?"
    c "That means a lot, Kit."
    scene ep001_hangar_celine with dissolve
    c "What about you, Céline?"
    ce "Shit, [p_name]."
    ce "You're asking a lot."
    if celine_romance:
        ce "But if you and Kit are going..."
    else:
        ce "But if Kit is going..."
    ce "Yes I'm in."
    if ep001_vess_truth:
        ve "I'm with you too."
    c "Great!"
    c "What about you Lilly?"
    scene ep001_hangar_lilly with dissolve
    l "I'm sorry [p_name_short], but you're crazy."
    l "This is exactly the juvenile, irresponsible plan I would expect from you."
    c "So you're out?"
    l "Of course I'm out and you should all be."
    l "This is going to end miserably for you all and..."

    play music "music/future-gladiator.ogg" fadein 1.0 fadeout 4
    scene ep001_hangar_thim_hidden with vpunch
    "At that moment I noticed a figure standing in the doorway, eavesdropping on our conversation."
    "When I sprinted towards the door the culprit revealed himself."
    scene ep001_hangar_thim with dissolve
    "Thim, with a fucking 'h'."
    t "You're so fucking dead, [p_name]."
    scene ep001_hangar_thim_running with vpunch
    t "SECURITY! DESERTERS IN THE HANGAR BAY!"
    scene ep001_hangar_thim_jade with dissolve
    $ renpy.pause(0.5)
    scene ep001_hangar_thim_jade_strike with vpunch
    "Before Thim could sprint to the nearest guard station, Jade was upon him clubbing him on the back of the head with a wrench."
    scene ep001_hangar_thim_jade_alt with dissolve
    j "That should shut him up."
    c "Wow."
    c "I thought..."
    j "You thought I was only good at fucking?"
    c "I was going to say that I thought you weren’t capable of violence, but still..."
    c "Is he breathing?"
    j "Yes."
    c "Good."
    c "Thanks to him we need to hurry."
    scene ep001_hangar_thim_carry with dissolve
    "I carried Thim's body back to the hangar where Kit and the girls were looking at me in shock."
    "Sirens began to blare, Thim's alerted cries must have reached the guards."
    c "Hurry! They'll be upon us any minute."
    c "Help me drag him to that corvette over there."
    ce "Is he alive?"
    c "Yes, unfortunately."
    scene ep001_hangar_thim_drag with dissolve
    "Together with Jade, I dragged Thim's body inside the nearest ship, while Céline pushed Kit in his wheel chair."
    c "Jade, try to override the docking clamps!"
    j "On it."
    "Jade hurried to the hangar bay controls to release the docking clamps and start sequence to open doors of the hangar bay."
    scene ep001_hangar_console with dissolve
    "Smashing the controls for good measure seemed like a good idea before I sprinted back to the ship's cockpit."
    scene ep001_cockpit_camran_celine with dissolve
    "Céline was already seated in the co-pilot's chair and I took the captain's chair."
    "We had some basic flight training, so the controls weren't that unfamiliar."
    ce "We're really going to do this, aren't we?"
    c "We can't go back now, not after what happened with Thim."
    ce "In that case: ready when you are, captain."
    scene ep001_hangar_security with dissolve
    "As I closed all the outer doors of the spaceship, several guards streamed into the hangar bay, guns at the ready."
    scene ep001_cockpit_kit_closeup with dissolve
    ki "We've got company."
    c "They won't stay long, the hangar bay doors are about to open."
    "The whole hangar lit up as a warning that a hard vacuum was about to open."
    "The security guards scrambled out of the hangar bay and the security doors closed shut."
    scene ep001_cockpit_celine with dissolve
    ce "Initiating launch sequence."
    scene ep001_cockpit_lilly_kit with dissolve
    l "Don't do it, [p_name_short]."
    l "Break it off."

    $ man_name = "Officer"
    "I ignored her as an unfamiliar voice sounded through the ship."
    man "This is ship security to the persons commandeering the TGN Enfield."
    man "You're in direct violation of the Terran Naval Code."
    man "Abort launch and power down your engines."
    man "Once we establish control of the hangar bay you're to come out of the ship with your hands in the air and kneel in front of the hull."
    c "Ignore them."
    scene ep001_cockpit_celine with dissolve
    ce "Five seconds to launch."
    man "Stop now and live."
    man "As soon as the illegally seized ship will come into firing range of the TGN Ypotryll you will be fired upon."
    man "This is not an idle threat."
    ce "All systems ready."
    c "Let's take this bucket for a ride."
    scene ep001_cockpit_camran_celine_alt with dissolve
    "Controlling a ship was a little different than in a simulator and we nearly hit a bulkhead, but using the board computer we managed to fly through the opened hangar doors."
    ce "We're going to make it!"
    scene ep001_cockpit_lilly with dissolve
    l "What are we doing?!"
    l "Take us back!"
    l "Please!"
    scene ep001_cockpit_camran_celine_alt with dissolve
    "As we left the Ypotryll behind us, a new, more familiar voice sounded through the ship's speakers."
    ca "Crew of the TGN Enfield, this is your commander speaking."
    ca "Power down your engines and return to the hangar deck."
    scene ep001_cockpit_camran_celine_surprise with dissolve
    ki "Shit, it's mom!"
    ca "If you do not comply we will be forced to shoot you down."
    ca "I repeat: power down your engines and turn the ship around."
    c "She won't shoot at us, will she?"
    ce "It's mom, we're talking about..."
    scene ep001_cockpit_lilly_kit with dissolve
    ki "She totally will."
    c "Fuck."
    scene ep001_cockpit_lilly_closeup with dissolve
    l "What did you think would happen, [p_name]?"
    l "That they wouldn't notice a ship leaving their sphere of influence?"
    c "If that fucking Thim had kept his mouth shut..."
    ce "Is there a way to talk to the Ypotryll?"
    c "I guess, they're talking to us, aren't they?"
    scene ep001_cockpit_celine_closeup with dissolve
    "Céline fiddled with the controls of the ship's radio and began to speak."
    ce "Mother?"
    ce "Mother, it's me. Céline."
    "There was a very long silence in which everybody seemed to hold their breath."
    scene ep001_bridge_calista with dissolve
    ca "Céline?"
    ca "What the fuck are you doing up there?"
    scene ep001_cockpit_celine_closeup with dissolve
    ce "I'm leaving, mom."
    ce "We're going to look for Eva and the others."
    ce "We can't leave them behind."
    scene ep001_bridge_calista with dissolve
    ca "Céline. I want you to think hard about what you're doing."
    ca "This is desertion."
    ca "Even I can't save you if you're tried by military court."
    ca "Céline?"
    ca "Is your brother with you?"
    ca "Don't tell me he is."
    scene ep001_cockpit_kit_closeup with dissolve
    ki "Yes, mom, I'm here."
    scene ep001_bridge_calista_surprise with dissolve
    ca "Not you as well?"
    ca "You didn't think up this misbegotten plan, did you?"
    scene ep001_cockpit_kit_closeup with dissolve
    ki "No, I didn't, but I believe we can make a difference."
    scene ep001_bridge_calista_surprise with dissolve
    ca "It's that fucking, good-for-nothing boy, isn't it."
    "It was rather clear to everyone the commander was talking about me."
    ca "You have two minutes to comply with my demands."
    scene ep001_cockpit_camran_celine_surprise with dissolve
    c "Fuck, she's really going to fire upon us?"
    c "Knowing that you're on board?"
    ce "I don't know..."
    ki "This is kind of a first for all of us, [p_name_short]."
    "That was the first moment I truly panicked."
    "Before, I rode on an adrenaline high and didn't really think about the consequences of my actions."
    "The harsh words of Commander Szuzume were a wake-up call."
    "Céline and Kit must have noticed the look of fear and doubt in my eyes."
    scene ep001_cockpit_lilly_kit with dissolve
    ki "I'm with you all the way, [p_name_short]."
    ce "We all knew what the consequences of desertion were when we signed up earlier."
    l "You're fucking crazy."
    c "So. No turning back?"
    scene ep001_cockpit_kit_closeup with dissolve
    ki "No."
    scene ep001_cockpit_camran_celine_alt with dissolve
    ce "No."
    scene ep001_cockpit_lilly with dissolve
    l "Yes."
    ca "Your two minutes are up."
    ca "Turn back at once."
    scene ep001_cockpit_camran_celine_alt with dissolve
    c "Let's fire those engines and see if we can outrun them."
    scene ep001_cockpit_lilly with dissolve
    l "The Ypotryll is massive, [p_name]."
    l "It has fucking rail guns, missiles..."
    l "This is suicide!"
    scene ep001_bridge_calista_resolve with dissolve
    ca "Turn back."
    ca "Céline. Kit. Please..."
    scene ep001_cockpit_celine_closeup with dissolve
    "That last statement brought tears to the eyes of Céline, but she wiped them away and concentrated on steering the Enfield."
    "The radio became eerily silent."
    "And then the combat scanner lit up and an angry siren sounded."
    c "What's happening?"
    scene ep001_cockpit_camran_celine_surprise with dissolve
    ce "She did it..."
    ce "She actually did it..."
    c "Are those?"
    ce "They've locked onto us..."
    ce "Three missiles approaching..."
    scene ep001_ypotrill_missiles with dissolve
    $ renpy.pause()

    jump episode002

    return

    label ep001_celine_sex:
        scene ep001_tents_celine_kit_sleep with dissolve
        c "Hey..."
        ce "Sssh, get over here. Quick!"
        "I carefully crawled next to her while Kit was still snoring away."
        "Céline closed the tent again and turned her attention to me."
        scene ep001_tents_celine_camran with dissolve
        "Both feeling we had little time to waste, Céline and I entangled in a passionate embrace, her mouth on mine."
        "She giggled softly as I bit her earlobe and dotted her neck and breasts with kisses."
        "Our caresses became more eager as the girl freed my erection."
        "I took her small, but firm breasts in my hands and brushed my lips against her nipples."
        scene ep001_tents_celine_camran_naked_alt with dissolve
        ce "Ooooh, [p_name]..."
        "We froze momentarily as Kit made a noise and seemed on the brink of awakening."
        scene ep001_tents_celine_camran_naked with dissolve
        if is_patreon() and renpy.has_label("extra_scene_01") and not _in_replay:
            "We let out a sigh of relief, when he turned his back on us."
            call extra_scene_01 from _call_extra_scene_01
            ce "We’re not done yet, are we?"
            "The girl had me erect in seconds and guided my penis towards her pussy."
        else:
            "Our sigh of relief, when he turned his back on us, transformed into soft moans as Céline guided my penis towards her pussy."
        scene ep001_tents_celine_camran_penetrate with dissolve
        "My dick pushed against Céline’s entrance, slick with her moisture. She gasped as I pressed the top of my shaft past her labia. I paused."
        "Céline grasped my arm to encourage me to go deeper."
        ce "I need you, [p_name]."
        show ep001_tents_celine_camran_fucking with dissolve
        "Her voice was barely a whisper and her moans just as soft when we started fucking."

        show ep001_tents_celine_camran_fucking_alt with dissolve
        "It was weird and exciting at the same time. The possibility of Kit waking up and catching us in the act actually enhanced our passionate lovemaking."

        scene ep001_tents_celine_camran_fucking_orgasm with flash
        with flash
        "I licked Céline’s hard nipples and fingered her, while my cock was still inside her. The stimulation of so many erogenous zones at once finally sent her over the edge."

        menu:
            "Cover her body":
                scene ep001_tents_celine_camran_fucking_belly with flash
                with flash
                "The girl shuddered and bit on my hand to suppress her orgastic moans, which in turn ushered my orgasm."
                scene ep001_tents_celine_camran_fucking_belly_alt with dissolve
                "I tried to muffle my delirious cry in the musk of her hair as I shot my seed onto her belly."
            "Creampie [gr]\[Celine Creampie\]":
                $ ep001_celine_creampie = True
                scene ep001_tents_celine_camran_fucking_creampie with flash
                with flash
                $ renpy.pause(0.8)
                scene ep001_tents_celine_camran_fucking_creampie_alt with dissolve
                "The girl shuddered and bit on my hand to suppress her orgastic moans, which in turn ushered my orgasm."
                "I tried to muffle my delirious cry in the musk of her hair as I shot my seed inside her."
        scene ep001_tents_celine_camran_fucking_post with dissolve
        ce "Hmmmm, I’d ask you to stay, but then we’d have too much explaining to do in the morning."
        $ renpy.end_replay()
        return

    label ep001_jade_hj:
        show ep001_camran_barracks_jade_hj with dissolve
        "Her soft hands touched my penis as she focused all of her attention on bringing me pleasure."
        "Jade’s handjobs, like every sex act with her, were a work of art."
        "She knew just how to apply the right amount of pressure, a little squeeze at just the perfect moment."
        show ep001_camran_barracks_jade_hj_closeup with dissolve
        "She was never just pumping you absentmindedly, but seemed to always know when you were about to explode, often stopping right at the height of your pleasure, slowing down and meticulously building that perfect orgasm."
        scene ep001_camran_barracks_jade_hj_orgasm with dissolve
        "I was very distracted by the events of the past day, but she had me spilling my seed after just a few minutes of complete nirvana."
        c "What would I do without you, Jade?"
        j "Probably doing the same by yourself, but poorly?"
        $ renpy.end_replay()
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
