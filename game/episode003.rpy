
image ep003_club_girl_fucking_alt_closeup = Movie(play="movies/ep003/ep003_club_girl_fucking_alt_closeup.webm")
image ep003_club_girl_fucking_alt = Movie(play="movies/ep003/ep003_club_girl_fucking_alt.webm")
image ep003_club_girl_fucking_throat_closeup = Movie(play="movies/ep003/ep003_club_girl_fucking_throat_closeup.webm")
image ep003_sim_farm_be_fuck_doggy = Movie(play="movies/ep003/ep003_sim_farm_be_fuck_doggy.webm")
image ep003_sim_farm_le_lick_closeup = Movie(play="movies/ep003/ep003_sim_farm_le_lick_closeup.webm")
image ep003_sim_farm_le_lick = Movie(play="movies/ep003/ep003_sim_farm_le_lick.webm")
image ep003_sim_farm_le_penetrate_closeup_pleasure = Movie(play="movies/ep003/ep003_sim_farm_le_penetrate_closeup_pleasure.webm")
image ep003_sim_farm_le_penetrate_closeup_pleasure_alt = Movie(play="movies/ep003/ep003_sim_farm_le_penetrate_closeup_pleasure_alt.webm")
image ep003_sim_farm_le_fuck_doggy = Movie(play="movies/ep003/ep003_sim_farm_le_fuck_doggy.webm")
image ep003_sim_farm_be_lick_closeup = Movie(play="movies/ep003/ep003_sim_farm_be_lick_closeup.webm")
image ep003_sim_farm_be_lick = Movie(play="movies/ep003/ep003_sim_farm_be_lick.webm")
image ep003_sim_farm_be_penetrate_closeup_pleasure = Movie(play="movies/ep003/ep003_sim_farm_be_penetrate_closeup_pleasure.webm")
image ep003_sim_farm_be_penetrate_closeup_pleasure_alt = Movie(play="movies/ep003/ep003_sim_farm_be_penetrate_closeup_pleasure_alt.webm")


label episode003:
    $ save_name = "Episode 3"

    $ ep003_bastard_damage = 0
    $ ep003_verdant_visit = False
    $ ep003_verdant_con_vitae = False
    $ ep003_verdant_ziv = False
    $ ep003_verdant_thyia_celine = False
    $ ep003_ziv_mission = False
    $ ep003_ziv_mission_accepted = False
    $ ep003_ziv_mission_completed = False
    $ ep003_sagueliath_visit_first = False
    $ ep003_verdant_visit_first = False
    $ ep003_sagueliath_visit = False
    $ ep003_bar_first_visit = False
    $ ep003_bar_thyia_talk = False
    $ ep003_bar_kit_talk = False
    $ ep003_kit_conversation = False
    $ ep003_kit_personal = False
    $ ep003_kit_bar = False
    $ ep003_bar_lilly_talk = False
    $ ep003_bar_vess_talk = False
    $ ep003_thim_insult = False
    $ ep003_l_admonish = False
    $ ep003_verdant_party = False
    $ ep003_verdant_party_dance = False
    $ ep003_verdant_convitae_contract = False
    $ ep003_verdant_con_vitae_accepted = False
    $ ep003_verdant_con_vitae_declined = False
    $ ep003_sim_farm_talk = False
    $ ep003_sim_farm_force = False
    $ ep003_sim_farm_dismiss = False
    $ ep003_sim_farm_sex_threesome_soft = False
    $ ep003_sim_farm_sex_solo_le = False
    $ ep003_sim_farm_sex_deal = False
    $ ep003_sim_farm_threat = False
    $ ep003_sim_farm_sex_le = False
    $ ep003_sim_farm_sex_be = False
    $ ep003_le_sex_last = False
    $ ep003_be_sex_last = False
    $ ep003_shuttle_refusal = False
    $ ka_name = "Man"
    if game.is_special:
        $ ep003_sim_farm_menu_label = "daughter"
    else:
        $ ep003_sim_farm_menu_label = "maid"

    scene black with fade
    centered "{=chapter_heading}EPISODE 3{/=chapter_heading}"

    scene ep002_iron_bastard_cockpit_asteroids with dissolve
    call location_screen (__("Hreir Asteroid Base, Approach"), True) from _call_location_screen_18

    "For some time, we floated just outside the asteroid field, our armor pelted by small debris coming from the field."

    scene expression eye_blink("images/ep003/ep003_cockpit_celine") with dissolve
    c "Can we fly through it manually?"
    ce "An experienced pilot could..."
    ce "Maybe..."
    c "So we have a chance?"
    scene expression eye_blink("images/ep003/ep003_cockpit_celine_doubt") with dissolve
    ce "[p_name_short], you know I’m far from an experienced pilot."
    ce "I’m still figuring out what half of the damned console does."
    ce "Maybe if the flight computer assists with some of the more difficult maneuvers..."
    ce "And I could use your help as a co-pilot too."
    c "Of course."
    scene expression eye_blink("images/ep003/ep003_cockpit_kit") with dissolve
    ki "Would shooting at those asteroids accomplish anything?"
    ce "The smaller ones, probably."
    ce "If you hit one of the larger rocks the resulting debris might still hit our ship and cause a lot of damage."
    c "That might be worth the risk."
    c "Let's do it."
    "We strapped in and Céline asked everyone else on the ship to do the same."
    scene ep003_asteroid_flight with vpunch
    "As soon as we increased our forward thrust and crossed the threshold of the field, the ship was hit by larger debris, sending shockwaves throughout the hull."
    scene ep003_cockpit_celine_kit with dissolve
    "Céline gripped the steering control firmly, while her brother monitored the field through the ship's combat sensors."
    "The journey appeared to go smoothly, until possible collision alerts suddenly started clogging the flight interface."

    scene ep003_asteroid_flight_01 with dissolve
    "A debris field loomed before us, several large rocks were hurtling towards us."

    menu:
        "Evade":
            $ ep003_bastard_damage += 1
            "On my command, Céline tried to bank the ship to avoid most of the heavy debris that was about to hit us."
            scene ep003_asteroid_flight_01_evade with vpunch
            "We were too slow and several large rocks pelted our hull."
            with vpunch
            "It almost sounded as if we were being shot upon by a very large automatic rifle."
        "Full thrust":
            $ ep003_bastard_damage += 2
            "On my command, Céline increased thrust in order to ram through the debris field ahead of us."
            scene ep003_asteroid_flight_01_thrust with vpunch
            "Several large rocks buried itself into the hull."
            with vpunch
            "Terrible sounds of tearing metal screamed throughout the ship."
        "[gr]Shoot":
            "On my command, Kit started shooting at the debris field in front of us."
            scene ep003_asteroid_flight_01_fire with vpunch
            "Several large rocks shattered before we reached them and we were showered in a rain of dust and small pebbles."

    scene ep003_asteroid_flight_02 with dissolve
    "Once we were through the field a passage between asteroids opened up."
    "The corridor was small and the asteroids spun ever so slightly."
    menu:
        "Evade":
            $ ep003_bastard_damage += 1
            "Céline steered the ship carefully through the narrow passage, trying to avoid the spinning rocks"
            scene ep003_asteroid_flight_02_evade with vpunch
            "We moved too slow and several of the asteroids grazed the hull, causing deep lacerations in our outer shields."
        "[gr]Full thrust":
            "Forgoing any carefulness, Céline kicked the engine in high gear and we punched through the corridor."
            scene ep003_asteroid_flight_02_thrust with vpunch
            "A terrible screeching resonated throughout the ship, but we escaped the corridor relatively unscathed."
        "Shoot":
            $ ep003_bastard_damage += 2
            "As Céline increased thrust, her brother shot at the asteroids."
            "Instead of shattering them, the rocks became adrift and started spinning at a much greater speed."
            scene ep003_asteroid_flight_02_fire with vpunch
            "As we flew through the passage, the ship was crushed between two boulders."
            with vpunch
            "The violence resulted in the electronics to fail temporarily and Céline reported diminished thrust on the starboard side."

    scene ep003_asteroid_flight_03 with dissolve
    "Escaping the corridor, Céline screamed as a big boulder hurtled towards us."

    menu:
        "[gr]Evade":
            "Céline yanked at her fly stick to make a hard bank port side, narrowly evading the large asteroid."
            scene ep003_asteroid_flight_03_evade with vpunch
            "The move took everyone by surprise, but nobody got hurt and the ship escaped mostly unharmed."
        "Full thrust":
            $ ep003_bastard_damage += 2
            "Taking the rock head on didn't seem like the best idea afterwords, but it had the effect of careening it off course."
            scene ep003_asteroid_flight_03_thrust with vpunch
            "Unfortunately, the crash caused one of the thrusters to fail completely."
            with vpunch
            "A portion of the hull caved in and causing depressurization of the surrounding area."
            "Luckily the automatic blast door closed and nobody was present in that section of the ship at the time..."
        "Shoot":
            $ ep003_bastard_damage += 2
            "Kit tried to blast the boulder out of our orbit, but it had absolutely no effect."
            scene ep003_asteroid_flight_03_fire with vpunch
            "The asteroid crashed head-on into our hull, rupturing several exterior pipes and cabling."
            with vpunch
            "A blackout of the lower crew quarters occurred not long after, until emergency power was restored by Thyia."

    "After an excruciating couple of minutes, several risky maneuvers and some lucky shots fired from the ship's cannon, the collision threats slowly cleared from the monitors."
    scene ep003_cockpit_celine_kit_smile with dissolve
    ce "I think we did it!"
    ki "That was too fucking close."

    if ep003_bastard_damage > 2:
        scene expression eye_blink("images/ep003/ep003_cockpit_celine_post_worry") with dissolve
        ce "Hull integrity 32%%"
        c "That was quite a battering..."
        c "Are we still able to fly?"
        ce "Barely, we really need to get this fixed at the next port."
        ce "And I sure hope we don't have to exit the way we came in, because that's a death sentence."
    else:
        scene expression eye_blink("images/ep003/ep003_cockpit_celine_post_smile") with dissolve
        ce "Hull integrity 87%%."
        c "Nothing we can't fix when we dock at a larger port."
        ce "Seems like it, unless we need to exit the way we came in..."

    play music "music/ephemera.ogg" fadein 1.0 fadeout 4

    "While I brought the crew up to speed via the internal comms, Céline brought us close to the asteroid base."
    scene ep003_asteroid_base with dissolve
    "Pulsing lights at the entrance of a docking bay indicated we were cleared to enter the base."
    "Comm chatter is something everyone expects at even the smallest space port, from port regulation listings to excited commercial advertisements."
    "Other than the signal lights everything was eerily quiet at Karan Hreir's supposed home."
    scene ep003_asteroid_base_dock with dissolve
    "After completing the automatic docking procedure and making sure there was a breathable atmosphere, I went out with Nadya and Aven to find Hreir."
    "Or, barring Hreir, any form of life..."
    scene ep003_asteroid_base_bots with dissolve
    "As we approached the far end of the docking bay, a set of large doors opened, revealing two security bots."
    "Blocking the way, they pointed their rifles at us and we were subjected to a weapons scan."
    $ man_name = "Bot"
    man "Please follow."
    scene ep003_asteroid_base_bots_escort with dissolve
    "The bots led us through a system of corridors, deep into the heart of the base."
    "We passed several closed doors, a lot of empty rooms and an occasional patrol of sentry bots, much like our armed escort."
    "The base seemed utterly devoid of sentient life."
    scene expression eye_blink("images/ep003/ep003_asteroid_base_bots_escort_aven") with dissolve
    av "You're sure Karan is still alive, mother?"
    scene expression eye_blink("images/ep003/ep003_asteroid_base_bots_escort_nadya") with dissolve
    na "I haven't received any information that told me otherwise."
    c "Not very reassuring..."
    scene expression eye_blink("images/ep003/ep003_asteroid_base_bots_escort_aven") with dissolve
    av "I wish we brought guns."
    av "And lots of them."
    scene expression eye_blink("images/ep003/ep003_asteroid_base_bots_escort_nadya") with dissolve
    na "The sentries would have ripped us to shreds already."
    na "The fact that Karan allowed an armed ship in the vicinity of his base is proof enough that he didn't deem us a threat."
    c "The base is well-armed then?"
    scene expression eye_blink("images/ep003/ep003_asteroid_base_bots_escort_aven") with dissolve
    av "I counted several rail gun turrets on the surface of the base."
    av "And there are probably several other defense measures I wasn't able to spot."
    av "So pretty well-defended, I'd say."
    scene ep003_asteroid_base_bots_doors with dissolve
    "At what must have been the heart of the base, the bots stopped us."
    man "Wait here."
    "The guards took their position, flanking a large metal door."
    c "Will Mr. Hreir see us now?"
    "The bots remained mute, frozen in their defensive position."
    "After several minutes, something clicked and the door started sliding sideways."
    scene ep003_hreir_lab with dissolve
    "The room beyond was dimly lit and occupied by two more sentry bots, guarding a solitary man at a computer console."
    ka "Enter."
    scene ep003_hreir_lab_closeup with dissolve
    "Large containers containing alien creatures suspended in clear liquid, dominated the room."
    "It didn't take a genius to realize we had entered the laboratory of Karan Hreir."

    python:
        codex_karan_hreir = add_codex_entry(
            Codex,
            __("Characters"),
            __("Karan Hreir"),
            [
                __("Scientist specializing in genetics and living a solitary live inside a well-protected asteroid base. Knows more about the warrior women that abducted Eva.")
            ],
            "images/codex/Karan.webp"
        )

    $ ka_name = "Karan"
    na "Karan, old friend, how nice of you to see us."
    scene expression eye_blink("images/ep003/ep003_hreir_lab_h") with dissolve
    ka "Nadya, what brings you here?"
    na "We were hoping that you could help us with a very difficult problem."
    ka "I might."

    menu:
        "Plead with Karan":
            if game.is_special:
                c "My sister, Nadya's niece, has been captured by a band of warriors."
            else:
                c "My friend has been captured by a band of warriors."
            c "They appeared out of nowhere, ambushing us on Lanan P-10."
            c "We're desperate to get her back."
            c "Can you help us?"
            scene expression eye_blink("images/ep003/ep003_hreir_lab_h_smile") with dissolve
            ka "Family."
            ka "I see."
        "Remain objective":
            c "We're looking for information on a band of warriors."
            scene expression eye_blink("images/ep003/ep003_hreir_lab_h_frown") with dissolve
            ka "Could you be less vague?"

    scene expression eye_blink("images/ep003/ep003_hreir_lab_h") with dissolve
    ka "Could you describe those warriors to me, as I suspect they weren't regular mercenaries?"
    c "They were all women, possibly humans."
    c "Very tall, muscular, commanding."
    c "I guess you could even call them beautiful, if you're into sharp-featured bodybuilders."
    scene expression eye_blink("images/ep003/ep003_hreir_lab_h_frown") with dissolve
    c "The most peculiar thing about them was the clothing they wore and the weapons they carried."
    c "Large swords, ancient-looking armor."
    ka "Peculiar indeed."
    ka "What makes you think I have any information about a species like this?"
    ka "My area of expertise is genetic manipulation, you know this, Nadya."
    scene ep003_hreir_lab_h_n with dissolve
    na "I do, Karan, but something about [p_name]'s story made me think of those manipulation programs from the early days of the Sovereignty."
    ka "You think they're spliced humans?"
    na "Possibly."
    ka "Intriguing."
    c "Will you help us?"
    scene ep003_hreir_lab_h_n_alt with dissolve
    ka "Possibly."
    ka "What do you offer in return?"
    c "I-"
    scene ep003_hreir_lab_h_n with dissolve
    na "Come on, Karan, just say what you want from us."
    ka "Always to the point, Nadya."
    ka "Very well."
    scene ep003_hreir_lab_h_n_alt with dissolve
    ka "If you want my help I'd like you to find me a healthy specimen of boverine."
    c "We are to transport some unknown alien creature aboard our ship?"
    c "We're not equipped for that."
    ka "Don't worry, I just need a larvae."
    ka "I'll provide you with a storage container for safe transport."
    if game.is_special:
        c "Aunt?"
    else:
        c "Nadya?"
    scene ep003_hreir_lab_n_closeup with dissolve
    na "I don't see that we have another choice."
    c "Fine, let's do it."
    scene expression eye_blink("images/ep003/ep003_hreir_lab_h_closeup") with dissolve
    ka "Good, I'll provide you with the likely location of the specimen and a storage canister."
    ka "Be advised though, hunting boverine is dangerous."
    ka "I'll provide you all with some basic information about the creature."

    python:
        codex_boverin = add_codex_entry(
            Codex,
            __("Species"),
            __("Boverine"),
            [
                __("Boverine are native to the planet Sagueliath and extremely dangerous predators. The crew was tasked with retrieving an larvae of a boverin for Karan Hreir.")
            ]
        )

    scene ep003_hreir_lab_h_n with dissolve
    na "You drive a hard bargain, Karan."
    ka "I'm sorry, but there's not a lot that excites me these days."
    ka "Examining a boverin would be a very diverting experiment though."
    scene ep003_hreir_lab_n_closeup with dissolve
    na "I'm sure..."
    na "I think we know enough, [p_name], let's find that boverin."
    c "Just make sure you have the information about those warrior-women ready when we return, Hreir."
    scene expression eye_blink("images/ep003/ep003_hreir_lab_h_closeup") with dissolve
    ka "I will."
    scene black with fade
    "We returned to the ship where Nadya filled me in on the species that Hreir wanted captured."
    scene expression eye_blink("images/ep003/ep003_cockpit_n") with dissolve
    na "Don’t think for a moment that hunting the creature Hreir wants is in any way easy."
    na "He didn’t lie when he said it was dangerous."
    c "Have you ever seen one?"
    na "Just pictures."
    scene expression eye_blink("images/ep003/ep003_cockpit_n_alt") with dissolve
    na "But I’ve read about them, they’re a popular research subject and also feature a lot in the folklore of certain alien species."
    c "The info Hreir sent us tells me they’re aggressive predators, living only on Sagueliath."
    na "They are indeed ferocious hunters, even more so when it’s their mating season."
    c "Great, let’s just hope they’re not in the mood for love when we’re about to steal one of their kids..."
    scene ep003_cockpit_ce with dissolve
    ce "Leaving the asteroid field should be a little easier than entering."
    c "Oh?"
    ce "Hreir sent us navigational charts for the field, the ship’s autopilot should take us through smoothly."
    c "Good, but I’m sure Kit will be sad he doesn’t get to shoot any more rocks."
    scene ep003_cockpit_ce_smile with dissolve
    ce "He’ll live."
    "I received a comm signal from Thyia so I left Céline to steer the ship from the asteroid field and headed to the engine room."
    scene expression eye_blink("images/ep003/ep003_engine_th") with dissolve
    th "Hey."
    c "You buzzed me?"

    if ep003_bastard_damage > 2:
        th "Yeah, how soon can we get into a port?"
        c "Is it that bad?"
        scene expression eye_blink("images/ep003/ep003_engine_th_serious") with dissolve
        th "Yes it is."
        th "I understand we’re going on a trip again?"
        c "We are."
        th "Well, in that case we need to stop at a port first."
        c "Could you find us a port with good mechanics?"
        th "Of course, I’ll get right on it."
        c "Thanks."
        "Thyia found us a port and Céline immediately set course to a place called Verdant Station."
        call ep003_sleep from _call_ep003_sleep

        call ep003_verdant from _call_ep003_verdant
    else:
        th "Yeah, I thought you wanted to assess the damage."
        c "We avoided most of it."
        scene expression eye_blink("images/ep003/ep003_engine_th_smile") with dissolve
        th "Luckily we did."
        th "We do have to get that damage fixed at some point."
        c "Understood."
        th "I’ll get Céline some coordinates for space ports with good workshops."
        c "That would be great."
        th "Thanks."

        menu:
            "Go to station":
                $ ep003_verdant_visit_first = True
                "I asked Céline to set a course for the station Thyia located for us."
                call ep003_sleep from _call_ep003_sleep_1

                call ep003_verdant from _call_ep003_verdant_1
            "Go to Sagueliath":
                $ ep003_sagueliath_visit_first = True
                "I asked Céline to set a course for the planet where the boverine were supposed to live."
                call ep003_sleep from _call_ep003_sleep_2

                call ep003_sagueliath from _call_ep003_sagueliath
    return

    label ep003_sleep:
        scene ep003_camran_sleep with dissolve
        "The journey would take several hours, so I retired to my quarters to get some sleep."
        call ep003_dream from _call_ep003_dream

        scene expression eye_blink("images/ep003/ep003_camran_awake") with dissolve
        "That’s when the dreams really took a turn for the worse..."
        "Unable to sleep anymore, I decided to pester some of my crew mates until we arrived at our destination."
        call ep003_conversations from _call_ep003_conversations
        return

    label ep003_verdant:
        $ ep003_verdant_visit = True

        play music [ "music/horizons.ogg", "music/floating-cities.ogg", "music/a-new-year.ogg" ] fadeout 4 fadein 1.0

        scene ep003_verdant_approach with dissolve
        call location_screen (__("Verdant Station, Approach"), True) from _call_location_screen_19
        "Verdant Station turned out to be a rather busy port, so we had to wait for several hours until a docking bay was available for our ship."

        python:
            codex_verdant_station = add_codex_entry(
                Codex,
                __("Places"),
                __("Verdant Station"),
                [
                    __("A medium-sized commercial spaceport where the crew of the Iron Bastard touched down to repair the ship."),
                    __("Several intergalactic companies have an office on the station, including ConVitæ."),
                ]
            )

        "Once we docked, I asked Céline and Thyia to arrange the necessary repairs."
        "The others were free to explore and soon flocked to one of the many bars on the station."

        label ep003_verdant_choices:
            scene ep003_verdant_docks_empty with dissolve

            menu:
                "Visit Thyia and Céline" if not ep003_verdant_thyia_celine:
                    $ ep003_verdant_thyia_celine = True
                    scene ep003_verdant_docks_bastard with dissolve
                    "When I checked up on the Bastard, Thyia and Céline were doing a visual inspection of the hull."
                    c "Back already?"
                    c "Have you found someone willing to do the repairs?"
                    scene expression eye_blink("images/ep003/ep003_verdant_docks_bastard_ce") with dissolve
                    ce "We have, seems like a reliable sort."
                    th "It’s not going to be cheap though."
                    scene expression eye_blink("images/ep003/ep003_verdant_docks_bastard_th") with dissolve
                    if ep003_bastard_damage > 2:
                        c "That was to be expected."
                        th "Yup."
                        c "Fuck."
                        th "Yup."
                    else:
                        c "I thought we sustained minimal damage."
                        th "We did, but the damage is to a few critical parts of our hull."
                        c "So critical means costly?"
                        th "Generally yes."
                    th "We need to arrange for food and supplies too."
                    scene expression eye_blink("images/ep003/ep003_verdant_docks_bastard_ce") with dissolve
                    ce "I’m sure we can manage that, can’t we?"
                    c "The money Nadya brought in certainly helped, but we’re burning through it fast."
                    c "I guess we need to go look for work."
                    th "There are jobs posted on a board on the station’s internal network."
                    scene ep003_verdant_docks_bastard_th_terminal with dissolve
                    th "Here, have a look."
                    "The list of jobs wasn’t very long and several of the requests involved hauling supplies that would never fit in our cargo bay."
                    "In the end, two jobs seemed like viable options."
                    "The first, was pretty straightforward and involved collecting someone from a nearby planet in the system."
                    "The advert listed someone named Ziv as the official contact."
                    "The other one, from a company called ConVitæ was a lot more vague, but the pay was exceptionally good."
                    "I know the name of the company practically threw the ‘Hey we’re an evil corporation’ in your face, but we needed the money."
                    scene ep003_verdant_docks_bastard with dissolve
                    th "I think we’re pretty much done here, so we’re going to the bar where the others are."
                    ce "Come join us if you want."
                    jump ep003_verdant_choices
                "Visit bar" if ((ep003_bar_thyia_talk + ep003_bar_kit_talk + ep003_bar_lilly_talk + ep003_bar_vess_talk) < 4) and not ((ep003_bar_kit_talk + ep003_bar_lilly_talk + ep003_bar_vess_talk) >= 3 and ep003_ziv_mission_completed):
                    play music [ "music/eigengrau.ogg", "music/the-water-and-the-well.ogg" ] fadeout 4 fadein 1.0

                    call ep003_verdant_bar from _call_ep003_verdant_bar

                    jump ep003_verdant_choices
                "Go to party" if ep003_kit_bar and not ep003_verdant_party:
                    call ep003_verdant_party from _call_ep003_verdant_party

                    play music [ "music/horizons.ogg", "music/floating-cities.ogg", "music/a-new-year.ogg" ] fadeout 4 fadein 1.0

                    jump ep003_verdant_choices
                "Visit ConVitæ" if ep003_verdant_thyia_celine and not ep003_verdant_con_vitae:
                    $ ep003_verdant_con_vitae = True
                    scene black with fade
                    "Using a map of the station I headed out to the address of the company from the advert."
                    call ep003_verdant_con_vitae from _call_ep003_verdant_con_vitae

                    jump ep003_verdant_choices
                "Contact Ziv" if ep003_verdant_thyia_celine and not ep003_verdant_ziv and not ep003_ziv_mission_completed:
                    $ ep003_verdant_ziv = True
                    scene black with fade
                    "I messaged the person from the job posting and arranged a meeting at the docks a little while later."
                    "Ziv responded almost immediately after I sent the message and we agreed to meet at the docks, near our ship."
                    scene expression eye_blink("images/ep003/ep003_verdant_docks") with dissolve
                    zi "Are you the captain of the Iron Bastard?"
                    c "I am."
                    zi "Good, I need someone collected from Verdigris V."
                    c "So I’ve gathered from your job posting."
                    zi "We are to touch down on the surface at a specific location and retrieve someone."
                    c "We?"
                    zi "I’m going with you."
                    c "Right."
                    zi "And you’re not to speak about this to anyone."
                    "The simple retrieval mission suddenly sounded a lot less simple..."
                    c "We’re not abducting someone, are we?"
                    zi "No, she wants to leave the planet out of her own free will."
                    c "But someone doesn’t want her to?"
                    zi "Look, do you want the job or not?"
                    c "I want to read up on Verdigris V first, to make sure we’re not kidnapping a local princess or something."
                    zi "She’s not a princess."
                    c "If you say so."
                    c "Still, I want to check up on what we’re heading into."
                    zi "Fine, but don’t take too long."
                    c "I’ll message you as soon as I’ve made up my mind."
                    scene ep003_verdant_docks_empty with dissolve
                    "After the woman left I went back into the Bastard and used the ship’s computer."
                    "Verdigris V turned out to be a peaceful world, one might even call it pastoral."
                    "It was one of the planets the humans colonized after the Third Migration and they dominated the population."
                    "I couldn’t find anything out of the ordinary about the place."
                    "No obstinate princesses wanting to flee the palace, no rebellions, no wars even for the past three hundred years."

                    python:
                        codex_ziv = add_codex_entry(
                            Codex,
                            __("Characters"),
                            __("Ziv"),
                            [
                                __("A woman on Verdant Station who contacted the crew about a taxi mission to Verdigris V.")
                            ],
                            "images/codex/Ziv.webp"
                        )

                    menu:
                        "Message Ziv":
                            $ ep003_ziv_mission = True
                            "I messaged Ziv and arranged for her to come aboard to make the trip to Verdigris V."
                            scene black with fade

                            call ep003_verdigris from _call_ep003_verdigris
                        "Don't message Ziv":
                            "Playing taxi sure was a lot of work and getting the money from ConVitæ sure seemed a lot easier."

                    jump ep003_verdant_choices

        scene ep003_verdant_docks_bots with dissolve
        if ep003_verdant_con_vitae_accepted:
            "Thyia and Céline went out to get the last supplies we needed and to do a last check of the ship's repairs."
            "Returning after several hours, Thyia and Céline brought everything for our next journey."
        else:
            "The ship was left to the care of a team of mechanics as Thyia and Céline went out to get the supplies for our next journey."
            "After several hours the repairs were completed and the Bastard was deemed space-worthy again."
        "As soon as Céline and I took our places on the bridge, we requested to leave the station."
        scene ep003_verdant_departure with dissolve
        if ep003_sagueliath_visit:
            "Permission was granted almost instantly and we took off to Hreir’s asteroid base."
            call ep003_shuttle from _call_ep003_shuttle
        else:
            "Permission was granted almost instantly and we took off to Sagueliath."
            call ep003_sagueliath from _call_ep003_sagueliath_1
        return

    label ep003_sagueliath:
        $ ep003_sagueliath_visit = True

        play music "music/bent-and-broken.ogg" fadein 1.0 fadeout 4

        scene ep003_sagueliath_approach with dissolve
        "Sagueliath turned out to be a small, but densely forested planet and we had difficulties finding a good landing spot."
        scene ep003_sagueliath_landed with dissolve
        "The Bastard eventually touched down on a rocky plateau overlooking the many trees of Sagueliath."
        "We had some trouble establishing a team to go on the hunt, as the perfect candidate for such activities was still bound to a wheelchair."
        "Aven volunteered, with Lilly completing the team."
        "Despite the fact that guns would be largely useless against the boverine and their thick skins, we took a few firearms from the Bastard’s armory, just in case."
        "Nadya agreed to stay in radio contact if we needed any information on the boverine."
        scene ep003_sagueliath_av_l with dissolve
        "After making the descent from the plateau, large trees towered all around and I became aware of the eery quiet."
        c "Shouldn’t there be more sounds of wildlife?"
        scene expression eye_blink("images/ep003/ep003_sagueliath_av") with dissolve
        av "Landing spacecraft is generally noisy business, so my guess is we scared away a lot of the critters."
        av "I’m sure they’ll be back."
        scene expression eye_blink("images/ep003/ep003_sagueliath_l") with dissolve
        l "Do we know where to look for the beasts?"
        scene expression eye_blink("images/ep003/ep003_sagueliath_av") with dissolve
        if game.is_special:
            av "Mom gave me a pretty clear explanation about boverine habitats, we should look for caves."
        else:
            av "Nadya gave me a pretty clear explanation about boverine habitats, we should look for caves."
        av "She also gave me a set of some very specific tracks to look out for."
        "That’s what we set out to do."
        scene ep003_sagueliath_av_l_alt with dissolve
        "As we ventured deeper, the forest gradually came to life, the sounds returning after leaving the landing area of the Bastard."
        "We also got our first glimpses of the local wildlife, but they were more afraid of us than we of them."
        "Aven motioned us to a halt when we reached a clearing."
        scene expression eye_blink("images/ep003/ep003_sagueliath_alt_l") with dissolve
        l "What’s that?"
        scene ep003_sagueliath_alt_av with dissolve
        av "A dead animal, I think."
        l "I’m amazed you can tell, it’s been practically ripped to shreds."
        av "I think we have our first clue."
        scene expression eye_blink("images/ep003/ep003_sagueliath_alt_l_fear") with dissolve
        l "A boverin did this?"
        scene ep003_sagueliath_alt_av with dissolve
        av "I’m pretty sure."
        c "Can you tell where it went?"
        av "Maybe."
        av "It’s hard to tell really, the whole scene is a complete mess."
        c "You don’t say..."
        scene ep003_sagueliath_alt_av_smile with dissolve
        av "Wise-ass."
        scene ep003_sagueliath_search with dissolve
        "We surveyed the area, Aven looking for clues, while Lilly and me were mostly just taking in the details of the carnage caused by the beast."
        scene ep003_sagueliath_search_l with dissolve
        l "Is that a..."
        c "Yes, I think it is..."
        l "I think it is."
        c "Damn..."
        c "And that..."
        l "U-huh..."
        scene ep003_sagueliath_search_av with dissolve
        av "Are you kids done pointing at all those entrails?"
        av "I think I know where the creature went."
        c "Do those monsters always create these full-scale horror set-pieces?"
        av "No, but a boverin who just had young does."
        av "Lots of mouths to feed, so the local wildlife suffers terrible losses during those times."
        scene ep003_sagueliath_search_l_unsure with dissolve
        l "And it drags all of its kills back to its young?"
        av "No, it devours them first and feeds the young boverin from its crop."
        l "Like a bird?"
        scene ep003_sagueliath_search_av with dissolve
        av "Yup."
        av "Though don’t expect it to look like a bird, because that would be an insult to any bird."
        c "Wouldn’t want that, of course."
        av "We should get going before the trail gets cold."
        scene ep003_sagueliath_av_alt with dissolve
        "Obediently, we followed Aven to a rock wall a kilometer from the slaughter."
        av "There must be a cave here somewhere."
        l "How do you know that?"
        av "Because these monsters live in caves."
        c "Great, no light, close corners, hormonal boverin waiting inside..."
        c "Remind me why didn’t we just torture the information out of Hreir?"
        scene expression eye_blink("images/ep003/ep003_sagueliath_l_shock") with dissolve
        l "[p_name_short]!"
        c "Kidding!"
        c "Mostly..."
        scene ep003_sagueliath_av_pointing with dissolve
        av "There!"
        av "Follow me."
        scene ep003_sagueliath_cave with dissolve
        "Trailing behind Aven and carrying our flashlights, we entered the cave."
        if not ep002_pit_thim:
            "I was pretty sure the things inside were much less pleasurable than what had awaited me in the cave on Nyiruan."
        av "Try not to make any loud noises."
        av "A boverin always sleeps deeply for some time after eating, so we should be careful not to wake it."
        scene ep003_sagueliath_cave_av with dissolve
        av "When we reach the creature, we should sneak up on it and steal one of the larvae."
        l "Larvae?"
        av "Young boverine are blind, deaf, legless creatures."
        av "They only have a mouth in which the mother deposits food."
        c "Vomits up food, you mean?"
        scene expression eye_blink("images/ep003/ep003_sagueliath_cave_l") with dissolve
        l "[p_name_short], I really could do without that mental image."
        c "Sorry!"
        scene ep003_sagueliath_cave_av with dissolve
        av "So we put a larvae in the canister Hreir gave us and get the hell out of here."
        c "You make it sound far too simple."
        "Taking the lead again, Aven led us further into the cave."
        scene ep003_sagueliath_cave_alt with dissolve
        "The dank smell of the cave got progressively worse until it became an overpowering stench of rot and decay."
        av "We’re close."
        c "No shit."
        scene ep003_sagueliath_cave_chasm with dissolve
        "As I was preparing another useless remark, Aven suddenly stopped dead in her tracks and shone her flashlight on the ground before her."
        av "Be very careful here."
        l "Fuck, that’s deep."
        av "It is."
        av "Don’t rush across."
        scene ep003_sagueliath_cave_boverin with dissolve
        "After two turns, we arrived at a very large chamber and in it rested a creature I had never seen before."
        "Actually, I would have been very happy to have never seen it at all."
        "The boverin was a true monstrosity, fearsome to behold even when resting."
        "Aven pointed out several larvae slithering at the claws of their mother."
        scene expression eye_blink("images/ep003/ep003_sagueliath_cave_boverin_av") with dissolve
        av "[p_name_short] and I will sneak towards the larvae, you stay here Lilly and watch the boverin for any sudden moves."
        av "I’ll try to catch one of those larvae while you hold the canister ready."
        av "Just be sure not to make any noises, the larvae might be almost senseless, but they can still detect tremors and alert their mother."
        av "Then we should be able to sneak back the way we came."
        av "Understood?"
        c "Yeah."
        l "Yup."
        scene ep003_sagueliath_cave_boverin_approach with dissolve
        "Carefully, Aven and I made our way to the sleeping monster and the writhing larvae at its feet."
        "When we came closer the predatory physique of the boverin became even more apparent."
        "Every feature of its sinewy body exhumed a kind of bold aggressiveness and made me glad it was still sleeping safe and sound."
        scene ep003_sagueliath_cave_boverin_closeup with dissolve
        "I held the canister at the ready, while Aven tried to scoop up one of the larvae."
        "She had to make multiple attempts, as she didn’t want to touch any of the other young boverine."
        "At last she managed to take hold of one of the slimy creatures and tried to deposit into the receptacle I was holding."
        scene ep003_sagueliath_cave_boverin_worm with dissolve
        "The larvae wriggled in her hands and opened its fanged beak to bite Aven, or so I assumed."

        play music "music/pursuit.ogg" fadein 1.0 fadeout 4

        scene ep003_sagueliath_cave_boverin_worm_alt with vpunch
        "Instead, the creature let out an ear-splitting scream."
        "Aven nearly dropped the thing, but together we managed to get the screaming worm inside the container where it continued to let out muffled noises."
        scene ep003_sagueliath_cave_boverin_eye with vpunch
        "Its siblings had joined the chorus and Sleeping Beauty was waking up."
        av "Fuck."
        c "Fuck."
        scene ep003_sagueliath_cave_boverin_run with dissolve
        "With the need for stealth eliminated, we broke into a sprint, as the boverin rose to its feet behind us."
        c "Run, Lilly!"
        c "We’re right behind you!"
        scene ep003_sagueliath_cave_boverin_run_alt with dissolve
        "We frantically scrambled back towards the exit, Lilly in front of us."
        "The sounds of the alarmed larvae gradually faded away, to be replaced by a hair-raising roar that echoed throughout the whole cave."
        av "It’s coming after us."
        "My witty retort was lost in Lilly’s surprised scream."
        scene ep003_sagueliath_cave_run_l_closeup with vpunch
        l "HELP!"
        "Arriving at the chasm we crossed so cautiously just before, it wasn’t instantly clear where Lilly’s distressed calls were coming from."
        scene ep003_sagueliath_cave_run_l with vpunch
        "Only when Aven shone her flashlight at the edges of the rift did we see her barely hanging on the edge."
        c "I’ll help her, you go across."
        "After passing her the canister containing the very unhappy larvae, Aven made a hurried pass to the other side, jumping the remaining distance."
        scene ep003_sagueliath_cave_run_l_c with dissolve
        c "Hold on, Lilly."
        l "[p_name_short]!"
        l "I slipped!"
        c "Can you grab my hand?"
        l "I don’t know, I can’t hold out much longer!"
        scene ep003_sagueliath_cave_run_hand with dissolve
        c "Grab it on three."
        "Another roar and the scratching of nails on stone, signified the boverin was close by."
        c "Two!"
        c "Three!"
        "The creature was extremely close, its scrambling movements clearly audible and interpuncted by enraged screams."
        "Lilly let one hand go of the ledge and latched onto my hand and the lower part of my arm."
        scene ep003_sagueliath_cave_run_l_c_ledge with vpunch
        "I pulled her upwards with all the strength I had and we nearly tumbled on top of each other."
        c "Run!"
        "Hurriedly, we crossed the chasm, wary of the slippery stone."
        scene ep003_sagueliath_cave_run_boverin with dissolve
        "When we were about halfway, the boverin entered the cavern and roared triumphantly at us."
        "Lilly nearly slipped again, but I held her upright and we made it across the crevasse as the Boverin set foot on the ledge."
        "The sharp claws of the beast allowed it to cross at much greater speed than us and within seconds the monster was halfway."
        l "We can’t outrun it!"
        scene ep003_sagueliath_cave_run_boverin_shot with vpunch
        "Lilly was right and in a split second I pointed my gun towards the stalactite-covered ceiling."
        "Dust and pebbles showered on the boverin which distracted it for a moment."
        l "What are you doing, [p_name_short]?"
        "After shooting multiple rounds into the ceiling nothing seemed to happen, until a smaller stalactite fell downward."
        "The boverin’s hide deflected most of the rock, merely annoying the animal."
        scene ep003_sagueliath_cave_run_boverin_shot_alt with dissolve
        "I kept shooting, despite Lilly’s attempts to pull me away towards the exit."
        "The beast remained at the center of the ledge and all of the muscles in its hind legs suddenly tensed."
        l "It’s going to jump!"
        scene ep003_sagueliath_cave_run_boverin_closeup with dissolve
        "It almost seemed as if the animal was laughing at us for pelting it with rocks, its face contorted in a rictus grin."
        "A larger stalactite fell down and grazed the beast’s hide, blood leaking from the wound into the void below."
        "Still, the distraction didn’t prove large enough and the boverin resumed its jump towards us."
        scene ep003_sagueliath_cave_run_boverin_jump with dissolve
        "As it set off and lifted itself into the air, I fired several shots into the ceiling and a gigantic pointy rock fell down."
        "The stalactie landed squarely on the beasts back and slammed it down towards the ledge."
        scene ep003_sagueliath_cave_run_boverin_fall with vpunch
        "Mowing frantically with its front claws the boverin tried to hold onto the ledge, its nails creating deep grooves in the stone."
        "Failing to achieve any grip, the boverin fell backwards into the chasm, bawling with impotent rage."

        play music "music/bent-and-broken.ogg" fadein 1.0 fadeout 4

        scene expression eye_blink("images/ep003/ep003_sagueliath_cave_run_l_surprise") with dissolve
        l "You killed it!"

        if ep002_lilly_comfort and ep002_lilly_understanding and not ep003_lilly_dismiss:
            scene ep003_sagueliath_cave_run_l_hug with dissolve
            "A very relieved Lilly wrapped her arms around me and hugged me fiercely, laughing nervously."
        l "You fucking killed it!"
        scene ep003_sagueliath_cave_run_l_av with dissolve
        av "Are you guys all right?"
        l "[p_name_short] killed the boverin."
        av "Damn, how?"
        av "By shooting at it?"
        c "The ceiling, mostly."
        scene ep003_sagueliath_cave_run_av with dissolve
        av "You’re a very lucky guy, [p_name_short]."
        av "A stunt like that could have brought the entire ceiling down on you."
        c "I think that would still be preferable to being ripped to shreds by a boverin."
        av "I see your point."
        c "Is the canister still intact?"
        av "It is."
        c "Good, let’s get it to the Bastard."
        l "Very good idea."
        scene black with fade
        "Despite disposing of the boverin, we still made haste, not wanting to attract another specimen looking for fresh game."
        scene ep003_sagueliath_landed with dissolve
        "Nadya was already waiting for us after receiving our message reporting our success over the radio."
        scene expression eye_blink("images/ep003/ep003_sagueliath_na") with dissolve
        na "I’m so glad you’re all safe."
        av "As are we."
        scene ep003_sagueliath_l_smile with dissolve
        l "It was really close..."

        menu:
            "Admonish her":
                $ ep003_l_admonish = True
                if ep003_lilly_dismiss:
                    c "I told you before, you shouldn’t have come."
                else:
                    c "You shouldn’t have come."
                c "You could have died out there!"
                scene ep003_sagueliath_l_angry with dissolve
                l "Don’t you think I’m aware of that?!"
                l "You don’t need to rub it in or anything."
                na "Please, stop it you two."
                na "Let’s just be grateful all ended well."
            "Be supportive [LillyPath]":
                c "It sure was."
                c "They don’t teach you that at the academy."
                l "You skipped Ledge Hanging 101?"
                c "Probably."

        scene expression eye_blink("images/ep003/ep003_sagueliath_na_alt") with dissolve
        na "The sample you took looks like a fine specimen, so I’m sure Karan will be pleased."
        av "It has stopped screaming, which is a plus."
        c "So, I think we can head back immediately and show Hreir that slime worm we got for him."
        na "Yes, I’m sure he wants it as fresh as possible."
        c "I’m sure he does."
        scene black with fade

        if not ep003_verdant_visit:
            "There were the repairs we still had to take care of, so Thyia found us a space station nearby where we made a pit stop."
            call ep003_verdant from _call_ep003_verdant_2
        else:
            "After some preliminary checks, we took off to the stars, on our way to Karan Hreir."
            "On our return trip from Sagueliath, we skirted the territory of Verdant Station."
            call ep003_shuttle from _call_ep003_shuttle_1

        return

    label ep003_verdant_bar:
        if not ep003_bar_first_visit:
            $ ep003_bar_first_visit = True
            "Getting a drink sounded like a great idea at that time, so I went to look for my crew."
            if ep003_ziv_mission_completed:
                scene ep003_verdant_bar_no_ziv with dissolve
            else:
                scene ep003_verdant_bar with dissolve
            "The music of the bar was inescapable, but didn’t drown out conversations completely."
            "Other than that it wasn’t what you’d call an upscale place, the scantly clad squirming alien near the entrance being a first hint."
            "Still, everyone seemed to have found a place at one of the many tables."

        label ep003_verdant_bar_conversations:
            if ep003_ziv_mission_completed:
                scene ep003_verdant_bar_no_ziv with dissolve
            else:
                scene ep003_verdant_bar with dissolve

            menu:
                "Talk to Thyia" if ep003_verdant_thyia_celine and not ep003_bar_thyia_talk and not ep003_ziv_mission:
                    $ ep003_bar_thyia_talk = True
                    scene ep003_verdant_bar_thyia with dissolve
                    th "[p_name_short], this is Ziv. "
                    th "Ziv, this is [p_name_short]."
                    scene ep003_verdant_bar_thyia_ziv with dissolve
                    if ep003_verdant_ziv:
                        c "Hi, we’ve met already."
                        scene ep003_verdant_bar_thyia_ziv_doubt with dissolve
                        th "You did?"
                        zi "Yes and you agreed to message me back, which you didn’t."
                        c "Look, I’m just not interested."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_thyia_closeup") with dissolve
                        th "You found an alternate source of income?"
                        if ep003_verdant_con_vitae_accepted:
                            c "I did, already got paid."
                            th "How much?"
                        elif ep003_verdant_con_vitae and not ep003_verdant_con_vitae_accepted:
                            c "Nope."
                            th "So?"
                        else:
                            c "I might."
                            th "How much does that pay?"

                        if ep003_verdant_con_vitae_accepted or not ep003_verdant_con_vitae:
                            $ ep003_ziv_mission = True
                            $ ep003_ziv_mission_accepted = True

                            c "Ten thousand credits."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_thyia_closeup_concern") with dissolve
                            th "That’s not enough."
                            c "What?!"
                            th "The head mechanic just messaged me and the repairs are more extensive than originally budgetted."
                            if ep003_verdant_con_vitae_accepted:
                                c "Well fuck."
                                th "Yup, I managed to haggle a discount, but still..."
                            else:
                                c "When did you plan on telling me?"
                                th "The message came in minutes ago."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_thyia_closeup_smile") with dissolve
                            th "But it looks like we need another source of income."
                            c "Looks like..."
                            c "What do the others think?"
                            th "About a taxi job?"
                            th "Everyone is fine with it."
                            c "Well Ziv, I guess you have a deal."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_ziv_closeup") with dissolve
                            zi "Your enthusiasm is heartwarming."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_thyia_closeup_annoyed") with dissolve
                            if not ep002_thyia_acceptance:
                                th "You do have a big problem with new people joining your crew, haven’t you [p_name]?"
                                c "I don’t, but this just feels wrong."
                            else:
                                th "Why do you have such a problem with this?"
                                c "I don’t know, just a feeling."
                            th "It’s just a transport job."
                            th "Seriously, there aren’t any other jobs available that do not involve hauling freight our ship is not equipped for, or where the journey doesn’t take several years."
                            th "We can't afford not to take this job."
                            c "If you say so."
                    else:
                        c "Hi."
                        c "You’re the one from the advert, aren’t you?"
                        zi "I am."

                        if ep003_verdant_con_vitae_accepted:
                            c "I’m afraid we can’t do the job."
                            scene ep003_verdant_bar_thyia_ziv_doubt with dissolve
                            th "You found an alternate source of income?"
                            c "I have, it should cover our expenses."
                            th "Well, the head mechanic just messaged me and the repairs are more extensive than originally budgetted."
                            th "So I hope you earned a lot with that one job."
                            c "Well fuck."
                            th "Yup, I managed to haggle a discount, but still..."
                            c "How much more?"
                            th "3000."
                            c "Fuck."
                            c "Well Ziv, looks like I’m listening."
                        else:
                            c "What’s the job exactly?"
                            th "Simple transport job."

                        scene expression eye_blink("images/ep003/ep003_verdant_bar_ziv_closeup") with dissolve
                        zi "I need someone collected from Verdigris V."
                        zi "We are to touch down on the surface at a specific location and retrieve someone."
                        c "We?"
                        zi "I’m going with you."
                        c "Right."
                        scene ep003_verdant_bar_ziv_closeup_alt with dissolve
                        zi "And you’re not to speak about this to anyone."
                        "The simple retrieval mission suddenly sounded a lot less simple..."
                        c "We’re not abducting someone, are we?"
                        zi "No, she wants to leave the planet out of her own free will."
                        c "But someone doesn’t want her to?"
                        zi "Look, do you want the job or not?"
                        c "We’re not kidnapping a local princess?"
                        zi "She’s not a princess."

                        menu:
                            "[gr]Accept":
                                $ ep003_ziv_mission = True
                                $ ep003_ziv_mission_accepted = True
                                c "All right, you have a deal Ziv."
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_ziv_closeup_smile") with dissolve
                                zi "Good, I’ll make sure I’m on your ship as soon as you depart."
                            "Decline":
                                $ ep003_ziv_mission_accepted = True
                                c "No sorry, can’t do it."
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_thyia_closeup_annoyed") with dissolve
                                if not ep002_thyia_acceptance:
                                    th "You do have a big problem with new people joining your crew, haven’t you [p_name]?"
                                    c "I don’t, but this just feels wrong."
                                else:
                                    th "Why do you have such a problem with this?"
                                    c "I don’t know, just a feeling."
                                th "Seriously, there aren’t any other jobs available that do not involve hauling freight our ship is not equipped for, or where the journey doesn’t take several years."
                                th "We can't afford not to take this job."
                                c "What do the others think?"
                                th "They’re all fine with it."
                                c "Fuck it then."
                                zi "Well Ziv, I guess you have a deal."
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_ziv_closeup_smile") with dissolve
                                zi "Your enthusiasm is heartwarming."

                        python:
                            codex_ziv = add_codex_entry(
                                Codex,
                                __("Characters"),
                                __("Ziv"),
                                [
                                    __("A woman on Verdant Station who contacted the crew about a taxi mission to Verdigris V.")
                                ],
                                "images/codex/Ziv.webp"
                            )
                    jump ep003_verdant_bar_conversations
                "Talk to Kit" if not ep003_bar_kit_talk:
                    $ ep003_bar_kit_talk = True

                    scene expression eye_blink("images/ep003/ep003_verdant_bar_kit") with dissolve

                    menu ep003_kit_conversation:
                        "About Kit" if not ep003_kit_personal:
                            $ ep003_kit_personal = True
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit") with dissolve
                            c "Nobody wants to drink with a cripple?"
                            ki "I was waiting on you, of course."
                            ki "And nobody wanted to sit close to the pole dancer, which is a damn shame, because she’s an artist."
                            c "Ever the art lover."
                            c "Well, I don’t have any problems with exotic dancing."
                            c "So, how are you holding up?"
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_smile") with dissolve
                            ki "Never a dull moment, it seems."
                            ki "Didn’t know space was so exciting outside the Sovereignty."
                            c "Me neither."
                            ki "The few stories didn’t do reality any justice."
                            c "What do you think of the new crew members?"
                            ki "Thyia is fun, Vess I don’t know..."
                            c "Oh, how so?"
                            ki "I don’t know, she seems so cagey."
                            ki "But that might just be her lack of confidence."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_smile_alt") with dissolve
                            ki "I still prefer her over Thim though."
                            c "Me too."
                            ki "You know anything more about her?"
                            c "Not much."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_serious") with dissolve
                            ki "I think she's the daughter of some local bigwig back on Lanan or something."
                            c "Why do you think that?"
                            ki "It’s just the way she talks."
                            c "So it’s just because she has a bit of an accent?"
                            ki "Yes and the fact that she wore much nicer clothes than those two other villagers."
                            c "I’ll admit you have a point there."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_smile") with dissolve
                            ki "See, all my theories are always airtight."
                            c "Yeah..."
                            c "Well, maybe I’ll ask Vess once she opens up a bit more."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_smile_alt") with dissolve
                            ki "Maybe she turns out to be the Queen of Lanan, in that case I’d marry her if I were you."
                            c "I’m pretty sure Lanan falls under the jurisdiction of some faceless bureaucrat somewhere back on the Proxima Centauri Orbital."
                            ki "A boy can still dream."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_sad") with dissolve
                            ki "You’re never any fun, you know that?"
                            c "Still you’ve put up with me all these years."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_smile_alt") with dissolve
                            ki "True, it’s an ongoing challenge."
                            jump ep003_kit_conversation
                        "About the bar" if not ep003_kit_bar:
                            $ ep003_kit_bar = True
                            c "Didn’t I see you talking to a girl earlier by the way?"
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_smile_alt") with dissolve
                            ki "Yes!"
                            ki "The whole wheelchair thing is finally paying off."
                            c "How so?"
                            ki "Well, as you said, a very pretty girl approached me and handed me a leaflet."
                            c "Some random girl smiled at you and dumped a flyer on you?"
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_sad") with dissolve
                            ki "It always sounds much less glamorous if you tell the story."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_serious") with dissolve
                            ki "Not sure why she handed it to me though, it’s a flyer for some party and I can’t dance for quite some time."
                            ki "You should go though, it looks like fun."
                            c "I’ll think about it."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_smile_alt") with dissolve
                            ki "Maybe you could ask Thim to come with you, I’m sure he’ll love it."
                            c "I could also wheel you into an airlock and throw away the key."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_sad") with dissolve
                            ki "Low blow!"
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_smile_alt") with dissolve
                            jump ep003_kit_conversation

                    scene expression eye_blink("images/ep003/ep003_verdant_bar_kit_smile") with dissolve
                    "We made fun of each other until Kit became very distracted by what was happening at the pole, so I left him gawking at the dancer."
                    jump ep003_verdant_bar_conversations
                "Talk to Lilly and Céline" if not ep003_bar_lilly_talk:
                    $ ep003_bar_lilly_talk = True

                    scene ep003_verdant_bar_lilly_celine with dissolve
                    c "Interesting choice of venue, didn’t know you were into seedy bars."
                    l "They’re all like that on the station."
                    ce "We’ve checked."
                    scene expression eye_blink("images/ep003/ep003_verdant_bar_celine") with dissolve
                    ce "Well, at least Kit seems to be having a good time."
                    c "Yeah, he’s a great devotee of the noble art of dancing at the pole."
                    l "Yeah sure..."
                    ce "Did you find already find some means to pay for the repairs?"
                    if ep003_ziv_mission or ep003_verdant_con_vitae_accepted:
                        c "I did."
                        if ep003_ziv_mission and not ep003_ziv_mission_completed:
                            c "Looks like we’ll get a temporary extra crew member though."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_lilly") with dissolve
                            l "Thyia told us something about her."
                            l "Seems like an easy job."
                            c "Everyone keeps telling me that..."
                        else:
                            c "The taxi job should cover everything."
                            ce "Great!"

                        if ep003_verdant_con_vitae_accepted:
                            c "Also did some work for a company called ConVitæ."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_lilly_doubt") with dissolve
                            l "What exactly?"
                            c "Participated in a simulation."
                            l "And sold one of your kidneys?"
                            c "I have no suspicious scarring as far as I know."
                            l "I’m sure ConVitæ is perfectly legit, but we all heard the rumors of what’s going on outside of the Sovereignty."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_celine") with dissolve
                            ce "I’m starting to wonder how much of that is just propaganda."
                            c "Exactly."
                            scene expression eye_blink("images/ep003/ep003_verdant_bar_lilly_concern") with dissolve
                            l "What happened back on Vulpes Velox could have come straight out of the vids back home."
                            l "But, despite everything we’ve been through, non-Sovereignty space isn’t the lawless cesspool they make it out to be."
                            if not ep003_lilly_dismiss:
                                l "Still..."
                                l "Just be careful."
                                c "I will."
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_lilly_smile") with dissolve
                    else:
                        c "I’m still working on it."

                    jump ep003_verdant_bar_conversations
                "Talk to Vess and Thim" if not ep003_bar_vess_talk:
                    $ ep003_bar_vess_talk = True

                    scene ep003_verdant_bar_vess_thim with dissolve
                    "Thim and Vess were sitting at a table together and seemed to be having an animated conversation."
                    ve "Hey [p_name]."

                    if ep001_medbay_thim_ignored and ep002_pit_thim:
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_angry") with dissolve
                        t "..."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_vess") with dissolve
                        c "Am I mistaken or did you just exchange more than three words with Thim?"
                        ve "Yes, he’s been telling me about the Academy you all went to."
                        c "Well that’s more than I have managed so far."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_angry") with dissolve
                        t "..."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_vess") with dissolve
                        c "He’s got that hostile stare down to a T. though."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_angry") with dissolve
                        t "Vess and I were having a conversation."
                        c "It speaks!"
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_angry_alt") with dissolve
                        c "And so you were."
                        ve "Don’t be like that, boys."

                        menu:
                            "Leave them [ThimPath]":
                                c "All right, I’ll leave you two alone."
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_vess_smile") with dissolve
                                ve "See you later."
                            "Insult Thim":
                                $ ep003_thim_insult = True
                                c "Well, before I go, might I suggest asking Thim about his pedigree?"
                                c "The story about how his grandmother was also his grandfather’s sister are truly legendary."
                                c "Or was she his daughter, I keep forgetting?"
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_furious") with vpunch
                                t "Fuck you, you miserable cunt!"
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_vess_shock") with dissolve
                                ve "Please!"
                                ve "Stop it!"
                                c "I have no intention of starting a bar fight, but at least I got more than three words out of Thim."
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_furious") with dissolve
                                "Quite happy with myself, I left the two to their drinks."
                    else:
                        t "Hi."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_vess") with dissolve
                        c "Am I mistaken or did you just exchange more than three words with Thim?"
                        ve "Yes, he’s been telling me about the Academy you all went to."
                        c "Well that’s more than I have managed so far."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_thim") with dissolve
                        t "Go fuck yourself, [p_name_short]."
                        c "See, very short and to the point."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_smile") with dissolve
                        t "More than three words though."
                        c "Yes, I’ll give you that."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_vess_doubt") with dissolve
                        ve "Is it true that you once stole a commander's car?"
                        c "I returned it!"
                        c "Eventually..."
                        c "Borrowing is the term you’re looking for."
                        c "It’s just that those stupid enforcers didn’t allow me to actually return the vehicle when they pulled me over."
                        c "Just didn’t want to listen."
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_vess_laugh") with dissolve
                        ve "Haha, I’m sure they didn’t."
                        c "Thim has been telling you all this?"
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_thim") with dissolve
                        t "Just filling her in on a bit of history of her crew mates."
                        c "By listing off all of my juvenile transgressions?"
                        scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_smile") with dissolve
                        t "You have to admit, there are a lot of those..."

                        menu:
                            "Leave them [ThimPath]":
                                c "Right..."
                                c "Well Vess, if you ever want the true version of anything he tells you, you know where to find me."
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_vess_smile") with dissolve
                                ve "I sure do!"
                            "Insult Thim":
                                $ ep003_thim_insult = True
                                c "Right..."
                                c "If you ever want to hear something about Thim’s wondrous pedigree, just let me know."
                                c "The story about how his grandmother was also his grandfather’s sister are truly legendary."
                                c "Or was she his daughter, I keep forgetting?"
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_furious") with vpunch
                                t "Fuck you, you miserable cunt!"
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_vess_shock") with dissolve
                                ve "Please!"
                                ve "Stop it!"
                                c "I have no intention of starting a bar fight, but at least I got more than three words out of Thim."
                                scene expression eye_blink("images/ep003/ep003_verdant_bar_thim_furious") with dissolve
                                "Quite happy with myself, I left the two to their drinks."

                    jump ep003_verdant_bar_conversations

            if ep003_ziv_mission_accepted and not ep003_ziv_mission_completed:
                call ep003_verdigris from _call_ep003_verdigris_1
        return

    label ep003_verdigris:
        $ ep003_ziv_mission_completed = True

        scene expression eye_blink("images/ep003/ep003_bastard_zi") with dissolve
        zi "Is this thing actually space-worthy?"
        c "Yes, of course, why do you ask?"
        zi "I heard Thyia and you talking about sustaining damage."
        c "We did, but that doesn’t prevent us from visiting Verdigris."
        c "Thyia and the head mechanic here have assured me there’s no immediate problem."
        "I actually had no idea if the Bastard would hold up if we were attacked again, but we really needed Ziv’s money."
        zi "If you say so..."
        c "Provide Céline with the coordinates and she’ll take us there."
        c "Just a taxi job, right?"
        scene expression eye_blink("images/ep003/ep003_bastard_zi_smile") with dissolve
        zi "Right."
        scene ep003_verdant_departure with dissolve
        "Mercifully, the ship took off and left Verdant’s docking bay without any issues."
        "The trip to Verdigris wasn’t very long and took us a couple of hours."

        play music "music/mirage.ogg" fadeout 4 fadein 1.0

        scene ep003_verdigris_approach with dissolve
        call location_screen (__("Verdigris V, Approach"), True) from _call_location_screen_20

        "After entering the atmosphere Céline flew us to a small spaceport near one of the cities of Verdigris."
        scene expression eye_blink("images/ep003/ep003_bastard_zi_hatch") with dissolve
        c "Is she waiting for us at the terminal?"
        zi "No, I have yet to receive her location."
        zi "We should head out."
        c "All right, I’ll get Aven and Thyia to come with us."
        scene expression eye_blink("images/ep003/ep003_bastard_zi_hatch_serious") with dissolve
        zi "I’m sorry, but they can’t come with."
        c "Why not?"
        zi "The contact who’s bringing her only knows me and might get jumpy when there’s a group of people waiting."
        c "Just message your contact and explain..."
        zi "I’m afraid that’s not possible."
        c "Great."
        c "I thought this was a simple taxi job."
        c "What’s with all the cloak and dagger?"
        zi "It’s necessary."
        zi "After we collect her things will be more simple."
        c "My confidence is increasing by the minute..."
        c "Lead the way."
        scene expression eye_blink("images/ep003/ep003_port_zi") with dissolve
        zi "I’ve just received word, they’re close."
        c "Good."
        c "Are we to meet them?"
        zi "They’re coming to us."
        c "Even better."
        c "This might just turn out to be the simple taxi job you promised."
        scene ep003_port_people with dissolve
        "After a few minutes, two figures emerged from between a couple of buildings lining the landing pad."
        "Their pacing was hurried, as if they were pursued by something or someone."
        "As they came closer, I noticed that one of them was of the same species as Ziv, whereas the other one looked decidedly human."
        scene ep003_port_wo_ra with dissolve
        $ woman_name = "Woman"
        image side woman_portrait = "gui/side-images/side_woman.webp"
        woman "This is the transport you arranged, Ziv?"
        zi "It is."
        zi "This is [p_name], the captain of the vessel."
        scene ep003_port_wo_ra_smile with dissolve
        woman "Thank you for helping us, [p_name]."
        c "Don’t mention it."
        zi "He’s getting paid quite a lot."
        scene ep003_port_wo_ra_serious with dissolve
        woman "Oh."
        woman "Right."
        woman "Do you have the necessary supplies?"
        zi "I have."
        woman "Good."
        woman "Raene, please meet Ziv, she’ll help from now on."
        ra "Thank you."
        "The girl’s voice was barely a whisper and after an embrace, the woman left her standing with us."
        scene ep003_port_zi_ra with dissolve
        zi "Please come with me Raene, we have a lot to talk about on the journey to Verdant Station."
        scene black with fade
        "The Iron Bastard took off as soon as we’d boarded, heading back to Verdant."

        play music [ "music/floating-cities.ogg", "music/horizons.ogg", "music/a-new-year.ogg" ] fadeout 4 fadein 1.0

        scene ep003_bastard_door with dissolve
        "Ziv and the girl were locked up most of the time during the return voyage to Verdant Station, so I never had a chance to speak to the both of them."
        scene ep003_verdant_docks_zi_ra with dissolve
        "As soon as we docked, Ziv transferred the funds to my account."
        zi "Thank you for your assistance."
        c "You’re welcome."
        c "Simple taxi job, after all."
        zi "Indeed."
        scene ep003_verdant_docks_zi_ra_departure with dissolve
        "The odd couple left and that was the last we saw of them."
        scene black with fade
        "Or so I thought..."

        python:
            codex_ziv = update_codex_entry(codex_ziv, None,
                [
                    __("A woman on Verdant Station who contacted the crew about a taxi mission to Verdigris V, where you collected Raene, her ward.")
                ]
            )

            codex_raene = add_codex_entry(
                Codex,
                __("Characters"),
                __("Raene"),
                [
                    __("A shy girl from Verdigris V. You helped Ziv get her off the planet to Verdant Station.")
                ],
                "images/codex/Raene.webp"
            )

        return

    label ep003_verdant_con_vitae:
        $ woman_name = "Receptionist"
        image side woman_portrait = "gui/side-images/side_secretary.webp"

        scene ep003_verdant_corridor with dissolve
        "The offices turned out to be located in a perfectly nondescript corridor, its presence only denoted by an equally nondescript sign bearing the company’s logo."
        scene expression eye_blink("images/ep003/ep003_verdant_convitae") with dissolve
        woman "Can I help you, sir?"
        c "I’m here about the advert."
        woman "You’d like to participate in our test program?"
        c "That depends on what the program is."
        c "I’m not participating in any medical experiments or anything."
        woman "Don’t worry sir, this is not a medical examination."
        woman "If you sign up, you’ll be entering a test simulation."
        woman "Your responses in the simulation will be recorded and evaluated as part of a larger research effort on the impact of simulated realities."
        c "So you’re not going to take any tissue samples?"
        scene expression eye_blink("images/ep003/ep003_verdant_convitae_smile") with dissolve
        woman "No, the Verdant branch of ConVitæ is working exclusively on simulations."
        woman "It’s all in the contract."
        woman "I have a copy for you if you’d like to be sure of our intentions."

        menu ep003_verdant_con_vitae_choices:
            "Ask for the contract" if not ep003_verdant_convitae_contract and not ep003_verdant_con_vitae_accepted and not ep003_verdant_con_vitae_declined:
                $ ep003_verdant_convitae_contract = True
                c "I’d like that."
                scene expression eye_blink("images/ep003/ep003_verdant_convitae_contract") with dissolve
                "As I expected, the contract was a thick bundle of mind-numbingly boring legalese."
                "Supposedly, most of the text only made sense to a lawyer, but the important parts seemed to check out."
                "The participant would be subjected to a test in one of ConVitæ’s simulators and the responses in the simulation would be recorded."
                "The contract didn’t stipulate any requirements regarding the age of the test subject, but would be required to pass a simple health scan."
                "The results of the scan would be destroyed after completion of the simulated test."
                "The last paragraphs of the contract dealt with a waiver of any risks voluntarily incurred by the participant."
                "It seemed a straightforward contract, just like the secretary had told me."
                jump ep003_verdant_con_vitae_choices
            "Sign the contract" if not ep003_verdant_con_vitae_accepted or ep003_verdant_con_vitae_declined:
                $ ep003_verdant_con_vitae_accepted = True
                scene expression eye_blink("images/ep003/ep003_verdant_convitae") with dissolve
                c "I’m ready to participate, so I’d like to sign the contract."
                scene expression eye_blink("images/ep003/ep003_verdant_convitae_smile") with dissolve
                woman "Excellent, just sign your name in all the indicated places."
                scene ep003_verdant_convitae_walk with dissolve
                "Signing took a while and after filing the paperwork the secretary took me to another room."
                woman "Please wait here, I will be with you shortly."
                scene ep003_verdant_convitae_room with dissolve
                "Most of these simulation rooms look the same, white walls and nothing else to bump into, this one was no different."
                "A few minutes after I left the receptionist, she reappeared"
                scene expression eye_blink("images/ep003/ep003_verdant_convitae_scan_pre") with dissolve
                woman "Are you ready?"
                c "I think so."
                woman "Good."
                scene expression eye_blink("images/ep003/ep003_verdant_convitae_scan") with dissolve
                "She gave me a full inspection with her medical scanner and promptly left the room, satisfied with the results."
                scene ep003_verdant_convitae_room with dissolve

                call ep003_verdant_convitae_sim from _call_ep003_verdant_convitae_sim

                play music [ "music/horizons.ogg", "music/floating-cities.ogg", "music/a-new-year.ogg" ] fadeout 4 fadein 1.0

                scene ep003_verdant_convitae_room with dissolve
                "I found myself alone in the white room again."
                scene expression eye_blink("images/ep003/ep003_verdant_convitae_room_door") with dissolve
                "The door to the reception area opened automatically and the receptionist beckoned me in."
                scene expression eye_blink("images/ep003/ep003_verdant_convitae_post") with dissolve
                c "That’s it?"
                woman "Yes."
                c "Did you monitor the whole thing?"
                woman "I’m not at liberty to tell, sir."
                c "I understand."
                c "Have a good day."
                scene expression eye_blink("images/ep003/ep003_verdant_convitae_post_unsure") with dissolve
                woman "You too, sir."

            "Don't sign the contract" if not ep003_verdant_con_vitae_declined or ep003_verdant_con_vitae_accepted:
                $ ep003_verdant_con_vitae_declined = True
                scene expression eye_blink("images/ep003/ep003_verdant_convitae") with dissolve
                c "Sorry, but I can’t participate."
                woman "No problem at all, sir."
                woman "Have a good day."
                c "Yeah, you too."
                "Feeling I had just dodged a bullet, I left the ConVitæ’s offices."

        scene black with fade
        return

    label ep003_verdant_convitae_sim:
        $ be_name = "Girl"
        $ le_name = "Woman"

        play music "music/fantasy-ambience.ogg" fadeout 4 fadein 1.0

        scene ep003_sim_farm with pixellate
        "The shift between reality and the virtual is always a little disorientating, this time even more so because I was suddenly standing on a moss floor wearing unfamiliar clothes."
        "I was standing in a forest, a blue sky over my head and birds chirped happily all around me."
        "While some part of me wanted to explore the wilderness instead of taking the obvious path, I decided to play along with the rules of the simulation."
        scene ep003_sim_farm_closeup with dissolve
        "A small farm completed the pastoral scene and it was pretty obvious what my destination was."
        "Walking in Medieval finery along a muddy road isn’t the most comfortable experience and it took me a while to reach the front door."
        scene ep003_sim_farm_door with dissolve
        "The sound of my knocks against the wood of the door echoed throughout the valley."
        "After some commotion inside, the door creaked open to reveal a girl."
        scene expression eye_blink("images/ep003/ep003_sim_farm_girl") with dissolve
        be "Yes?"
        be "Oh..."
        if game.is_special:
            be "Mom!"
        else:
            be "Mistress!"
        be "The tax collector is here!"
        if game.is_special:
            "An edge of panic was noticeable when the girl called out for her mother, who appeared not long after."
        else:
            "An edge of panic was noticeable when the girl called out for her mistress, who appeared not long after."
        scene ep003_sim_farm_woman with dissolve
        le "Please sir, we’ve done all we can."
        le "The harvest was poor this year, we’ll be able to pay in the coming season."
        le "Please let the Duke have mercy on us!"
        "Just my luck to be thrust into a poor man’s fantasy of what life in the Middle Ages must have been like."

        menu:
            "Talk to the woman":
                $ ep003_sim_farm_talk = True
                c "Might I come in?"
                le "Of course, milord."
                "The woman stepped aside and I was allowed to enter the small building."
                scene ep003_sim_farm_interior with dissolve
                "The farmers were obviously dead poor, so I wondered what kind of massive dickhead the Duke I supposedly worked for was."
                c "Tax collection is the same time every year, you cannot be surprised by this."
                scene ep003_sim_farm_interior_le with dissolve
                le "We’re not, good sir, it’s just that the rains destroyed all of our crops and our last pig died just last week."

                menu:
                    "Offer to pay her taxes":
                        c "Life isn’t fair."
                        le "It surely isn’t, milord."
                        c "I’ll pay your taxes."
                        scene ep003_sim_farm_interior_le_surprise with dissolve
                        le "You-"
                        le "What?"
                        le "Milord, that’s too much!"
                        le "We’d be indebted to you and-"
                        c "Consider it a gift."
                        le "A gift?"
                        le "Did you hear that Berit?"
                        $ be_name = "Berit"
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_be_smile") with dissolve
                        if game.is_special:
                            be "I surely did, mother."
                        else:
                            be "I surely did, mistress."
                        be "You’re too kind, sir!"
                        c "I’ll cross your name off the list and make sure nobody comes to bother you."
                        c "But be sure to have the money next year, you might not be so lucky."
                        scene ep003_sim_farm_interior_le_smile with dissolve
                        le "Of course, sir, of course we will."
                        le "You’ll be forever in our prayers."
                        c "Thanks, I guess."
                        c "Goodbye."
                        scene ep003_sim_farm_leaving with dissolve
                        "I left both women and headed back out, quite eager to explore that dark forest in the opposite direction."
                        "Right when I passed the fence surrounding the farm the farmer’s wife called out to me."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_leaving_le") with dissolve
                        le "Milord!"
                        le "Please, turn back!"
                        c "What’s the matter?"
                        scene expression eye_blink("images/ep003/ep003_sim_farm_leaving_le_closeup") with dissolve
                        if game.is_special:
                            le "My daughter and I...{w} We talked..."
                        else:
                            le "My servant and I...{w} We talked..."
                        le "We thought you must be tired from your journey."
                        le "Why don’t you rest for a while?"

                        menu:
                            "Accept [ThreesomeSoft]":
                                $ ep003_sim_farm_sex_threesome_soft = True
                                "I had a feeling I was going to be treated to some wholesome and very special rural hospitality, so I accepted the woman’s invitation."
                                "When I entered the farm again, my suspicions were confirmed."

                                call ep003_sim_farm_sex_threesome_soft from _call_ep003_sim_farm_sex_threesome_soft
                            "[red]Decline":
                                "I did my best impression of a noble knight and declined her offer."
                                scene expression eye_blink("images/ep003/ep003_sim_farm_leaving_le_closeup") with dissolve
                                c "I’m sorry, good woman, but I must venture forth."
                                le "I understand, sir, bless you."
                                scene expression eye_blink("images/ep003/ep003_sim_farm_leaving_le_wave") with dissolve
                                "After crossing the fence again the simulation suddenly ended."
                    "Come to a deal [ThreesomeSoft]":
                        $ ep003_sim_farm_sex_deal = True
                        c "I’m not an unreasonable man, so if there’s anything you can think of to pay me with?"
                        c "I might be able to give you a few months respite, if we can reach an agreement."
                        c "I’m going to have a hard time selling it to the Duke, but I’m willing do that for you."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_worry") with dissolve
                        le "There’s nothing left but this house and our health."
                        c "Well, the house is worthless..."
                        if game.is_special:
                            c "But you and your daughter look very healthy indeed."
                        else:
                            c "But you and your maid look very healthy indeed."
                        le "Thank you, sir."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_shock") with dissolve
                        le "Oh!"
                        le "You don’t mean?!"
                        c "Yes, I think you know what I mean."
                        le "You want to...{w} bed me, milord?"
                        if game.is_special:
                            c "Not just you, your daughter as well."
                        else:
                            c "Not just you, your servant as well."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_shock_alt") with dissolve
                        le "Sir!"
                        le "You cannot ask this of us!"
                        c "I think I just did."
                        le "We’re honest farmers."
                        c "The alternative is paying what you owe the Duke."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_worry") with dissolve
                        c "It’s up to you, but time is running out."
                        if game.is_special:
                            "The distraught woman looked from me to her daughter, who had been present for the entire conversation."
                        else:
                            "The distraught woman looked from me to her maid, who had been present for the entire conversation."
                        scene ep003_sim_farm_interior_le_be_worry with dissolve
                        "I decided to put some pressure on her by standing up and walking towards the door."
                        be "Milord, please wait."
                        le "Berit?!"
                        $ be_name = "Berit"
                        le "What are you doing?"
                        scene ep003_sim_farm_leaving_be_naked_alt with dissolve:
                            yalign 1.0
                            ease 8 yalign 0.01
                        $ renpy.pause()
                        "When I turned to face the women again, the youngest girl was already undressing herself."
                        if game.is_special:
                            c "It seems your daughter is eager to begin."
                        else:
                            c "It seems your maidservant is eager to begin."
                        le "Berit, you don’t have to do this."
                        if game.is_special:
                            be "What’s the alternative, mother?"
                            "The daughter stood fully naked before me, the other woman still wracked by indecision."
                        else:
                            be "What’s the alternative, mistress?"
                            "The young servant stood fully naked before me, the other woman still wracked by indecision."
                        "When she finally started to unlace her clothing my heart skipped a beat."
                        scene ep003_sim_farm_leaving_le_be_naked with dissolve
                        "The prospect of having power over those two women aroused me, even if it was in a simulation."
                        "I knew all the pleasures, up to my own orgasm, would only exist in my mind, carefully orchestrated by whatever current was hooked up to my neural pathways."
                        if game.is_special:
                            "I just didn’t care, the desire to fuck the farmer’s wife and her daughter became too overwhelming."
                        else:
                            "I just didn’t care, the desire to fuck the farmer’s wife and her servant became too overwhelming."

                        call ep003_sim_farm_sex_threesome_soft from _call_ep003_sim_farm_sex_threesome_soft_1
                    "Threaten her":
                        "I did my best to look interested in the simple interior of the wooden hovel."
                        c "This seems like a cosy house."
                        le "It is, sir, we’re truly blessed."
                        c "What a shame then, if I were to set fire to the place if you fail to pay up what you owe the Duke."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_worry") with dissolve
                        le "Milord, please!"
                        c "I think you leave me no choice."
                        le "This is the first time we’re not able to pay the tax."
                        le "The Duke has always been kind to us."
                        c "Well, I’m not the Duke."
                        c "Pay now, or I’m lighting a torch and burn this hole to the ground."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_shock_alt") with dissolve
                        le "Sir!"

                        menu:
                            "[red]Fuck them":
                                scene ep003_sim_farm_interior_le_hold with dissolve
                                if game.is_special:
                                    c "Or you and your daughter could undress before me and let me have my way with you both."
                                else:
                                    c "Or you and your maid could undress before me and let me have my way with you both."
                                le "Milord?!"
                                call ep003_sim_farm_knockout from _call_ep003_sim_farm_knockout
                            "Fuck her":
                                call ep003_sim_farm_sex_proposal_le from _call_ep003_sim_farm_sex_proposal_le
                            "[red]Fuck her [ep003_sim_farm_menu_label]":
                                if game.is_special:
                                    c "Or your daughter could undress before me and you could let me have my way with her."
                                else:
                                    c "Or your maid could undress before me and you could let me have my way with her."
                                scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_shock") with dissolve
                                le "Milord?!"
                                call ep003_sim_farm_knockout from _call_ep003_sim_farm_knockout_1
                            "[red]Turn away":
                                call ep003_sim_farm_turn_away from _call_ep003_sim_farm_turn_away
            "Force entry":
                $ ep003_sim_farm_force = True
                "Wanting to be done with it I pushed the woman aside and entered her home."
                scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_shock") with dissolve
                le "Sir, please!"

                menu:
                    "Talk to her":
                        c "I’m not an unreasonable man, so if there’s anything you can think of to pay me with."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_worry") with dissolve
                        le "We have nothing, good sir, the rains destroyed all of our crops and our last pig died just last week."
                        c "I might be able to give you a few months respite, if we can reach an agreement."
                        c "I’m going to have a hard time selling it to the Duke, but I’m willing do that for you."
                        le "There’s nothing left but this house and our health."
                        c "Well, the house is worthless..."
                    "Threaten her":
                        $ ep003_sim_farm_threat = True
                        c "You’ll pay, one way or the other."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_worry") with dissolve
                        le "We have nothing, kind sir, the harvest-"
                        c "I can always put you to the sword."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_shock") with dissolve
                        le "What?!"
                        le "No, please sir!"
                        le "This is the first time we’re not able to pay the tax."
                        le "The Duke has always been kind to us."
                        c "Well, I’m not the Duke."
                        c "Pay now, or be killed."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_shock_alt") with dissolve
                        le "Please, there must be some other way!"
                        le "Sir!"

                menu:
                    "Fuck them [ThreesomeHard]":
                        scene ep003_sim_farm_interior_le_hold with dissolve
                        if game.is_special:
                            c "You and your daughter could undress before me and let me have my way with you both."
                        else:
                            c "You and your maid could undress before me and let me have my way with you both."
                        le "Milord?!"
                        c "You heard me."
                        c "Spread your legs for me just this once and you don’t have to fear the Duke’s tax man for a whole year."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_be_angry") with dissolve
                        be "You perverted brute!"
                        le "Berit!"
                        $ be_name = "Berit"
                        if game.is_special:
                            be "But mother, this outrageous."
                        else:
                            be "But mistress, this outrageous."
                        be "What are you doing?!"
                        scene ep003_sim_farm_leaving_le_naked with dissolve:
                            yalign 1.0
                            ease 8 yalign 0.01
                        $ renpy.pause()
                        "When the farmer’s wife started to unlace her clothing my heart skipped a beat."
                        "The prospect of having power over those two women aroused me, even if it was in a simulation."
                        "I knew all the pleasures, up to my own orgasm, would only exist in my mind, carefully orchestrated by whatever current was hooked up to my neural pathways."
                        if game.is_special:
                            "I just didn’t care, the desire to fuck the woman and her daughter became too overwhelming."
                        else:
                            "I just didn’t care, the desire to fuck the woman and her maid became too overwhelming."
                        le "Just follow my lead, dear, I’ll make sure it won’t hurt."
                        be "You can’t be serious!"
                        le "Do as you’re told girl."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_be_fear") with dissolve
                        if game.is_special:
                            "Staring daggers at me, Berit disrobed and stood naked next to her mother."
                        else:
                            "Staring daggers at me, Berit disrobed and stood naked next to her mistress."
                        call ep003_sim_farm_sex_threesome_hard from _call_ep003_sim_farm_sex_threesome_hard
                    "Fuck her":
                        call ep003_sim_farm_sex_proposal_le from _call_ep003_sim_farm_sex_proposal_le_1
                    "Fuck her [ep003_sim_farm_menu_label]":
                        if game.is_special:
                            c "Or your daughter could undress before me and you could let me have my way with her."
                        else:
                            c "Or your maid could undress before me and you could let me have my way with her."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_shock") with dissolve
                        le "Milord?!"
                        c "You heard me."
                        c "Let her spread her legs for me just this once and you don’t have to fear the Duke’s tax man for a whole year."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_alt") with dissolve
                        le "Sir! What you’re asking..."
                        le "There must be another way."
                        le "We’re just simple fa-"
                        c "Yes, just simple farmers, I know and I don’t care."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_fear") with dissolve
                        if game.is_special:
                            le "But my daughter, take me, at least!"
                        else:
                            le "But my servant, take me, at least!"
                        c "No."
                        "I stared the woman down hard, the panic clearly visible on her face."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_doubt") with dissolve
                        if game.is_special:
                            "When her eyes shifted towards her daughter, I knew I’d won."
                        else:
                            "When her eyes shifted towards her maid, I knew I’d won."
                        "The prospect of having power the woman aroused me, even if it was in a simulation."
                        "I knew all the pleasures, up to my own orgasm, would only exist in my mind, carefully orchestrated by whatever current was hooked up to my neural pathways."
                        "I just didn’t care, the desire to fuck the young girl became too overwhelming."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_be_fear") with dissolve
                        if game.is_special:
                            be "Mother?"
                        else:
                            be "Mistress?"
                        le "Berit..."
                        $ be_name = "Berit"
                        if game.is_special:
                            be "Mother?!"
                        else:
                            be "Mistress?!"
                        le "Berit, I need to go outside for a while, please obey milord in everything he wishes."
                        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_be_shock") with dissolve
                        if game.is_special:
                            be "You can’t do this mother!"
                        else:
                            be "You can’t do this mistress!"
                        le "Please don’t hurt her."
                        if game.is_special:
                            "Ignoring her daughter’s pleas, the farmer’s wife went outside, leaving me alone with the girl."
                        else:
                            "Ignoring her maid's pleas, the farmer’s wife went outside, leaving me alone with the girl."
                        call ep003_sim_farm_sex_be_hard from _call_ep003_sim_farm_sex_be_hard
                    "[red]Turn away":
                        call ep003_sim_farm_turn_away from _call_ep003_sim_farm_turn_away_1
            "[red]Turn away":
                call ep003_sim_farm_turn_away from _call_ep003_sim_farm_turn_away_2
        return

    label ep003_sim_farm_sex_proposal_le:
        $ ep003_sim_farm_sex_solo_le = True
        c "Or you could undress before me and let me have my way with you."
        le "Milord?!"
        c "Final offer."
        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_fear") with dissolve
        le "We’re just simple fa-"
        c "Yes, just simple farmers, I know."
        "I stared the woman down hard, the panic clearly visible on her face."
        if game.is_special:
            "When her eyes shifted towards her daughter, I knew I’d won."
        else:
            "When her eyes shifted towards her maid, I knew I’d won."
        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_le_doubt") with dissolve
        le "Berit, please leave us for a while."
        $ be_name = "Berit"
        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_be_shock") with dissolve
        if game.is_special:
            be "Mother!"
        else:
            be "Mistress!"
        be "No!"
        le "Just go."
        "Ultimately, the girl did as she was asked."
        scene expression eye_blink("images/ep003/ep003_sim_farm_interior_be_angry") with dissolve
        "When she passed me, it almost seemed as if she wanted to spit before my feet, but she just walked on and slammed the door shut."
        scene ep003_sim_farm_leaving_le_naked with dissolve:
            yalign 1.0
            ease 8 yalign 0.01
        $ renpy.pause()
        if game.is_special:
            "As her mother started to unlace her clothing my heart skipped a beat."
        else:
            "As her mistress started to unlace her clothing my heart skipped a beat."
        "The prospect of having power over the farmer’s wife aroused me, even if it was in a simulation."
        "I knew all the pleasures, up to my own orgasm, would only exist in my mind, carefully orchestrated by whatever current was hooked up to my neural pathways."
        "I just didn’t care, the desire to fuck the woman became too overwhelming."
        call ep003_sim_farm_sex_le_hard from _call_ep003_sim_farm_sex_le_hard
        return

    label ep003_sim_farm_turn_away:
        $ ep003_sim_farm_dismiss = True
        c "Sure thing, have a nice day."
        "Thoroughly fed up with the whole simulation, I turned around and walked away, leaving the woman dumbfounded in the doorway."
        scene ep003_sim_farm_leaving with dissolve
        "At the moment where I reached the fence surrounding the farm the simulation suddenly ended."
        return

    label ep003_sim_farm_knockout:
        scene ep003_sim_farm_interior_be_pan with dissolve
        "Right when I was putting up one my best arrogant noble smirks I was hit on the head violently with a heavy metal object."
        scene ep003_sim_farm_interior_le_be_pan with dissolve
        if game.is_special:
            "The last thing I saw were the two women hovering over me, the daughter holding a cast iron pan."
        else:
            "The last thing I saw were the two women hovering over me, the maid holding a cast iron pan."
        scene black with pixellate
        "My attempt to talk to them was drowned out by the sensation of the cookware hitting my head multiple times."
        "All went black and the simulation ended."
        return

    label ep003_sim_farm_sex_threesome_soft:
        if _in_replay:
            $ le_name = "Leda"
            $ be_name = "Berit"
            $ ep003_sim_farm_sex_le = False
            $ ep003_sim_farm_sex_be = False
            $ ep003_le_sex_last = False
            $ ep003_be_sex_last = False

        scene ep003_sim_farm_leaving_be_naked with dissolve:
            yalign 1.0
            ease 8 yalign 0.01
        $ renpy.pause()

        if game.is_special:
            le "Forgive us for being forward, but my daughter and I would like to thank you properly."
        else:
            le "Forgive us for being forward, but my maid and I would like to thank you properly."
        "While the woman closed the door, I lusted over Berit’s supple young body."
        scene ep003_sim_farm_le_smile with dissolve
        c "Tell me your name."
        le "Leda, milord."
        $ le_name = "Leda"
        c "No need for that, call me [p_name]."
        if game.is_special:
            c "You and your daughter are very beautiful, Leda."
        else:
            c "You and your maid are very beautiful, Leda."
        le "Thank you, mi...{w} [p_name], I hope we please you."
        c "You do indeed."
        scene ep003_sim_farm_le_be_kiss with dissolve
        if game.is_special:
            "Berit came up to me and kissed me on the mouth as her mother undressed."
        else:
            "Berit came up to me and kissed me on the mouth as her mistress undressed."
        "The girl undid my belt and helped me get out of the many layers of clothing I was wearing."
        scene expression eye_blink("images/ep003/ep003_sim_farm_be_shy") with dissolve
        be "You’re to be my first, [p_name]."
        c "Have you ever sucked a cock, Berit?"
        be "No, no I haven’t."
        if game.is_special:
            c "Maybe your mother can teach you a thing or two."
        else:
            c "Maybe your mistress can teach you a thing or two."
        scene ep003_sim_farm_le_be_kneel with dissolve
        "The women got on their knees and Leda wrapped her hand around my cock as she brought my member to her mouth."
        "The feeling was so very real, I could sense the roughness of her callused hands brushing my own skin."
        "The warm sensation of her mouth enveloping my dick felt just right, even more so when her tongue softly tickled the tip."
        c "That’s it, Leda."
        scene ep003_sim_farm_le_suck with dissolve
        "I could tell the woman wasn’t that experienced in giving head, as she retched and gagged to take my length inside her mouth."
        "Berit looked at her intently, one hand trailing down her belly towards her pussy."
        show ep003_sim_farm_le_lick_closeup with dissolve
        if game.is_special:
            "The young girl fingered herself as her mother started sucking me in earnest."
        else:
            "The young girl fingered herself as her mistress started sucking me in earnest."
        scene ep003_sim_farm_le_suck_alt with dissolve
        c "You like what you see, Berit?"
        be "Hmmm, yes, [p_name]."
        if game.is_special:
            c "In that case, don’t be greedy Leda, let your daughter have a turn."
        else:
            c "In that case, don’t be greedy Leda, let your servant have a turn."
        scene ep003_sim_farm_be_jerk with dissolve
        "Leda offered the younger girl my cock which she began to jerk softly, her other hand still pressed against her wet slit."
        "After a few hesitant licks, I pushed the tip against her lips."
        c "Take it into your mouth."
        scene ep003_sim_farm_be_mouth with dissolve
        "She looked up at me again with a smile and did as I asked."
        c "That’s it, now suck."
        show ep003_sim_farm_be_lick with dissolve
        "The inexperience showed as Berit sucked my cock, her teeth brushing painfully against my shaft as my member disappeared halfway into her mouth."
        "But the girl proved to be a quick learner and as she picked up on the signals of my body she gradually used her small mouth to perfection."
        "I could have blasted my load down her throat, but I wanted to use the girls in other ways as well."
        c "Let’s go to your bed."
        c "There’s more for you to do than sucking cock."
        scene ep003_sim_farm_bed with dissolve
        "The mattress turned out to be a hemp sack of filled with straw, but I’d have fucked the women on the dirt floor if need be."
        "It was just a matter of deciding who had the honor to go first."
        menu ep003_sim_farm_sex_soft:
            "Fuck Leda" if not ep003_sim_farm_sex_le:
                $ ep003_sim_farm_sex_le = True
                if not ep003_sim_farm_sex_be:
                    "I didn’t hesitate and pushed the older woman’s legs apart."
                else:
                    $ ep003_le_sex_last = True
                    if game.is_special:
                        "Berit was a little annoyed by the fact that I turned my attention to her mother."
                    else:
                        "Berit was a little annoyed by the fact that I turned my attention to her employer."
                scene ep003_sim_farm_le_penetrate with dissolve
                "Leda cried out when I entered her thoroughly wet pussy, her body surely responded to sucking my cock earlier."
                scene ep003_sim_farm_le_fuck with dissolve
                "The bed creaked as I fucked the woman hard, her moans filling the small living room."
                scene ep003_sim_farm_le_breasts with dissolve
                "I grabbed at her large breasts, luxuriating in the feeling as my hands kneaded its luscious flesh."
                show ep003_sim_farm_le_penetrate_closeup_pleasure_alt with dissolve
                le "Oh [p_name]!"
                c "Do you enjoy getting fucked, Leda?"
                show ep003_sim_farm_le_penetrate_closeup_pleasure with dissolve
                le "I do! Oh, I do!"
                scene ep003_sim_farm_le_fuck_alt with dissolve
                if game.is_special:
                    "Berit was eagerly clinging to me, grinding her ass against my body as I kept fucking her mother."
                else:
                    "Berit was eagerly clinging to me, grinding her ass against my body as I kept fucking her mistress."
                jump ep003_sim_farm_sex_soft
            "Fuck Berit" if not ep003_sim_farm_sex_be:
                $ ep003_sim_farm_sex_be = True
                scene ep003_sim_farm_be_foreplay with dissolve
                if not ep003_sim_farm_sex_le:
                    "I didn’t hesitate and pushed the young girl’s legs apart."
                else:
                    $ ep003_be_sex_last = True
                    if game.is_special:
                        "Leda looked a little worried when I turned my attention to her daughter."
                    else:
                        "Leda looked a little worried when I turned my attention to her maid."
                le "Please, be gentle with her."
                be "Fuck me [p_name], don’t hold back."
                "Aroused by the mixed messages I received from both of them, I hungrily pulled Berit towards my cock."
                scene ep003_sim_farm_be_penetrate with dissolve
                "With the head I parted her lower lips and pushed against her entrance."
                be "Is it going to hurt?"
                c "Maybe a little..."
                "I started pushing and the young girl bit her lower lip."
                scene ep003_sim_farm_be_penetrate_closeup with dissolve
                be "It’s too big!"
                "Berit’s cry of fear turned into a surprised gasp as soon as I was fully inside her wet pussy."
                scene ep003_sim_farm_be_penetrate_closeup_smile with dissolve
                be "Oh!"
                "The bed creaked as I fucked the young girl hard, her moans filling the small living room, a virgin no longer."
                scene ep003_sim_farm_be_fuck with dissolve
                "I grabbed at her small breasts, squeezing them greedily and twisting her nipples."
                be "Sir, oh sir!"
                show ep003_sim_farm_be_penetrate_closeup_pleasure_alt with dissolve
                c "Do you enjoy getting fucked, Berit?"
                le "Oh, don’t ask her that, sir!"
                show ep003_sim_farm_be_penetrate_closeup_pleasure with dissolve
                be "Yes, yes I do! Ooooh!"
                c "Why don’t you kiss me then?"
                scene ep003_sim_farm_be_fuck_kiss with dissolve
                "Berit hesitated but her eager mouth was soon enough pressed against mine and we engaged in some very intimate french kissing."
                c "You enjoy being my little slut."
                be "I enjoy being your little slut, sir!"
                c "Good girl, now turn over."
                show ep003_sim_farm_be_fuck_doggy with dissolve
                "The girl got up on all fours and I pulled her ass towards me."
                "Then I began to fuck her harder than ever before, her ass cheeks bouncing violently."
                "Any mention of pain forgotten, Berit seemed fully entranced by the act of fucking."
                "I took hold of her shoulders and applied pressure, attacking her cunt with short aggressive thrusts."
                be "Oh god!"
                scene ep003_sim_farm_be_fuck_doggy_alt with dissolve
                "My balls slapped against her cunt as it buried itself to the root inside her slit, coming back wetter with every probe."
                "The girl’s moans turned ever hoarser as the fucking grew more intense."
                "I knew I was close...{w} So close..."
                jump ep003_sim_farm_sex_soft
        menu:
            "Creampie Berit":
                if ep003_le_sex_last:
                    if game.is_special:
                        "I wanted to give the farmer’s daughter something to remember me by, so I pulled out of Leda and re-entered Berit."
                    else:
                        "I wanted to give the maidservant something to remember me by, so I pulled out of Leda and re-entered Berit."
                else:
                    "I wanted Berit so badly I just kept on fucking her until erupted inside of her."
                scene ep003_sim_farm_be_fuck_shock with dissolve
                be "No!"
                be "He came inside me!"
                if game.is_special:
                    "Her mother looked at me aghast as Berit stopped her protests and came to savor the warm feeling of my seed spilling inside her cunt."
                else:
                    "Leda looked at me aghast as Berit stopped her protests and came to savor the warm feeling of my seed spilling inside her cunt."
                scene ep003_sim_farm_be_fuck_creampie with flash
                with flash
                "I came inside her so deep that when I pulled out it took a while for some cum to spill out of her."
            "Creampie Leda":
                if ep003_be_sex_last:
                    "I wanted to give the farmer’s wive something to remember me by, so I pulled out of Berit and re-entered Leda. "
                else:
                    "I wanted to give Leda something to remember me by, so I kept fucking her hard."
                scene ep003_sim_farm_le_fuck_doggy_alt with dissolve
                c "Oh Leda!"
                scene ep003_sim_farm_le_fuck_shock with dissolve
                le "[p_name]!"
                "Her final cry was edged with surprise as I spilled my seed inside her cunt."
                le "What did you do?!"
                scene ep003_sim_farm_le_fuck_creampie with flash
                with flash
                "I came inside her so deep that when I pulled out it took a while for some cum to spill out of her."
            "Body":
                scene ep003_sim_farm_be_le_fuck_bodies with flash
                with flash
                if ep003_le_sex_last:
                    if game.is_special:
                        "At the last moment, I pulled out of Leda and my cock spurted warm cum all over the bodies of mother and daughter."
                    else:
                        "At the last moment, I pulled out of Leda and my cock spurted warm cum all over the bodies of the woman and her maid."
                else:
                    if game.is_special:
                        "At the last moment, I pulled out of Berit and my cock spurted warm cum all over the bodies of mother and daughter."
                    else:
                        "At the last moment, I pulled out of Berit and my cock spurted warm cum all over the bodies of the woman and her maid."
            "Facial":
                scene ep003_sim_farm_be_le_fuck_facial with flash
                with flash
                if ep003_le_sex_last:
                    "At the last moment, I pulled out of her and brought Leda’s towards my cock, Berit joining her quickly."
                    "Leda was about to say something when my cock spurted warm cum all over her face and in her open mouth."
                    "Berit took a hit of warm cum square in the face too."
                else:
                    "At the last moment, I pulled out of her and brought Berit’s towards my cock, Leda joining her quickly."
                    "Berit was about to say something when my cock spurted warm cum all over her face and in her open mouth."
                    "Leda took a hit of warm cum square in the face too."
        scene ep003_sim_farm_be_le_fuck_post with dissolve
        c "Consider your debt paid."
        le "Thank you, [p_name]."
        be "That was something truly special."
        be "I won’t forget you."
        scene ep003_sim_farm_leaving_alt with dissolve
        "Leaving the naked women behind, I walked through the door."
        scene black with pixellate
        "All went black and the simulation ended."
        $ renpy.end_replay()
        return

    label ep003_sim_farm_sex_threesome_hard:
        if _in_replay:
            $ le_name = "Leda"
            $ be_name = "Berit"
            $ ep003_sim_farm_sex_le = False
            $ ep003_sim_farm_sex_be = False
            $ ep003_le_sex_last = False
            $ ep003_be_sex_last = False

        c "Tell me your name."
        le "Leda, milord."
        $ le_name = "Leda"
        if game.is_special:
            c "You and your daughter are very beautiful, Leda."
        else:
            c "You and your servant are very beautiful, Leda."
        scene expression eye_blink("images/ep003/ep003_sim_farm_le_fear") with dissolve
        le "Thank you, milord."
        c "Leda, come here and kiss me."
        c "Undress, Berit."
        scene ep003_sim_farm_le_be_kiss_alt with dissolve
        if game.is_special:
            "Leda obliged and came up to me and kissed me on the mouth as her daughter slowly undressed."
        else:
            "Leda obliged and came up to me and kissed me on the mouth as her maid slowly undressed."
        "The woman undid my belt and helped me get out of the many layers of clothing I was wearing."
        scene ep003_sim_farm_be_naked with dissolve:
            yalign 1.0
            ease 8 yalign 0.01
        $ renpy.pause()
        "When Berit finally stood naked before us, my eyes slowly lingered trailed her young body, so full of nubile grace."
        if game.is_special:
            c "Just as beautiful as her mother."
        else:
            c "Just as beautiful as your mistress."
        c "Have you ever sucked a cock, Berit?"
        be "No, I haven’t."
        if game.is_special:
            c "Maybe your mother can teach you a thing or two."
        else:
            c "Maybe your mistress can teach you a thing or two."
        c "On your knees."
        scene expression eye_blink("images/ep003/ep003_sim_farm_le_fear") with dissolve
        le "Please sir, let me do it."
        if game.is_special:
            le "Spare my Berit the disgrace."
        else:
            le "Spare Berit the disgrace."
        c "On your knees and start sucking."
        scene ep003_sim_farm_le_be_kneel with dissolve
        "The women got on their knees and Leda wrapped her hand around my cock as she brought my member to her mouth."
        "The feeling was so very real, I could sense the roughness of her callused hands brushing my own skin."
        scene ep003_sim_farm_le_suck with dissolve
        "The warm sensation of her mouth enveloping my dick felt just right, even more so when her tongue softly tickled the tip."
        c "That’s it, Leda."
        c "Finger yourself, Berit, give me something nice to look at."
        show ep003_sim_farm_le_lick with dissolve
        "I could tell the older woman wasn’t that experienced in giving head, as she retched and gagged to take my length inside her mouth."
        "Berit looked at her intently, one hand reluctantly trailing down her belly towards her pussy."
        scene ep003_sim_farm_le_suck_alt with dissolve
        if game.is_special:
            "The young girl fingered herself as her mother started sucking me in earnest."
        else:
            "The young girl fingered herself as her employer started sucking me in earnest."
        c "You like what you see, Berit?"
        be "No!"
        if game.is_special:
            c "Don’t be jealous, Leda, let your daughter have a turn."
        else:
            c "Don’t be jealous, Leda, let your maid have a turn."
        scene ep003_sim_farm_be_jerk with dissolve
        "Leda offered the younger girl my cock which she began to jerk softly, her other hand still obediently pressed against her wet slit."
        "After a few hesitant licks, I pushed the tip against her lips."
        c "Take it into your mouth."
        scene ep003_sim_farm_be_mouth with dissolve
        "She looked up at me defiantly, but did as I asked."
        c "That’s it, now suck."
        show ep003_sim_farm_be_lick with dissolve
        "The inexperience showed as Berit sucked my cock, her teeth brushing painfully against my shaft as my member disappeared halfway into her mouth."
        "But the girl proved to be a quick learner and as she picked up on the signals of my body she gradually used her small mouth to perfection."
        "I could have blasted my load down her throat, but I wanted to use the girls in other ways as well."
        c "Let’s go to your bed."
        c "There’s more for you to do than sucking cock."
        scene ep003_sim_farm_bed with dissolve
        "The mattress turned out to be a hemp sack of filled with straw, but I’d have fucked the women on the dirt floor if need be."
        scene expression eye_blink("images/ep003/ep003_sim_farm_bed_plead_le") with dissolve
        le "Please sir, I have one request."
        c "A request?"
        le "Please spill your seed outside of us..."
        c "What, you don’t want the honor of giving birth to a bastard?"
        "I didn’t wait for an answer and focused on the matter at hand, deciding who had the honor to go first."
        menu ep003_sim_farm_sex:
            "Fuck Leda" if not ep003_sim_farm_sex_le:
                $ ep003_sim_farm_sex_le = True
                if not ep003_sim_farm_sex_be:
                    "I didn’t hesitate and pushed the older woman’s legs apart."
                else:
                    $ ep003_le_sex_last = True
                    if game.is_special:
                        "Berit looked a little relieved by the fact that I turned my attention to her mother."
                    else:
                        "Berit looked a little relieved by the fact that I turned my attention to her mistress."
                scene ep003_sim_farm_le_penetrate with dissolve
                "Leda cried out when I entered her thoroughly wet pussy, her body surely responded to sucking my cock earlier."
                scene ep003_sim_farm_le_fuck with dissolve
                "The bed creaked as I fucked the woman hard, her moans filling the small living room."
                scene ep003_sim_farm_le_breasts with dissolve
                "I grabbed at her large breasts, luxuriating in the feeling as my hands kneaded its luscious flesh."
                show ep003_sim_farm_le_penetrate_closeup_pleasure with dissolve
                c "Do you enjoy getting fucked, Leda?"
                le "Oh, don’t ask me that, sir!"
                show ep003_sim_farm_le_penetrate_closeup_pleasure_alt with dissolve
                c "You enjoy playing my whore."
                scene ep003_sim_farm_le_fuck_alt with dissolve
                le "No sir, no I don’t!"
                c "Say it!"
                le "I enjoying being your whore, sir!"
                jump ep003_sim_farm_sex
            "Fuck Berit" if not ep003_sim_farm_sex_be:
                $ ep003_sim_farm_sex_be = True
                scene ep003_sim_farm_be_foreplay with dissolve
                if not ep003_sim_farm_sex_le:
                    "I didn’t hesitate and pushed the young girl’s legs apart."
                else:
                    $ ep003_be_sex_last = True
                    if game.is_special:
                        "Leda looked worried when I turned my attention to her daughter."
                    else:
                        "Leda looked worried when I turned my attention to her maid."
                le "Please, be gentle with her."
                be "I’ve never done it with a man before."
                "Aroused by the women’s statements, I hungrily pulled Berit towards my cock."
                scene ep003_sim_farm_be_penetrate with dissolve
                "With the head I parted her lower lips and pushed against her entrance."
                scene ep003_sim_farm_be_penetrate_closeup with dissolve
                be "It hurts!"
                c "Nonsense, you’re already so very wet, Berit."
                scene ep003_sim_farm_be_penetrate with dissolve
                "I started pushing and the young girl looked at me in fear."
                scene ep003_sim_farm_be_penetrate_closeup with dissolve
                be "You’re too big sir!"
                show ep003_sim_farm_be_penetrate_closeup_pleasure with dissolve
                "Berit’s cry of fear turned into a surprised gasp as soon as I was fully inside her wet pussy."
                be "Oh!"
                show ep003_sim_farm_be_penetrate_closeup_pleasure_alt with dissolve
                "The bed creaked as I fucked the young girl hard, her moans filling the small living room, a virgin no longer."
                scene ep003_sim_farm_be_fuck with dissolve
                "I grabbed at her small breasts, squeezing them greedily and twisting her nipples."
                c "Do you enjoy being my little slut?"
                be "Sir, please!"
                c "Say it!"
                be "I enjoying being your little slut, sir!"
                c "Good girl, now turn over."
                show ep003_sim_farm_be_fuck_doggy with dissolve
                "The girl got up on all fours and I pulled her ass towards me."
                "Then I began to fuck her harder than ever before, her ass cheeks bouncing violently."
                "Any mention of pain forgotten, Berit seemed fully entranced by the act of fucking."
                "I took hold of her shoulders and applied pressure, attacking her cunt with short aggressive thrusts."
                be "Oh god!"
                scene ep003_sim_farm_be_fuck_doggy_alt with dissolve
                "My balls slapped against her cunt as it buried itself to the root inside her slit, coming back wetter with every probe."
                "The girl’s moans turned ever hoarser as the fucking grew more intense."
                "I knew I was close...{w} So close..."
                jump ep003_sim_farm_sex
        menu:
            "Creampie Berit":
                if ep003_le_sex_last:
                    if game.is_special:
                        "I wanted to give the farmer’s daughter something to remember me by, so I pulled out of Leda and re-entered Berit."
                    else:
                        "I wanted to give the maidservant something to remember me by, so I pulled out of Leda and re-entered Berit. "
                else:
                    "I wanted Berit so badly I just kept on fucking her until erupted inside of her."
                scene ep003_sim_farm_be_fuck_shock with dissolve
                be "No!"
                be "He came inside me!"
                if game.is_special:
                    "Her mother looked at me aghast as my seed spilled inside her daughter’s cunt."
                else:
                    "Leda looked at me aghast as my seed spilled inside her maid’s cunt."
                le "You told us..."
                c "I did no such thing."
                scene ep003_sim_farm_be_fuck_creampie with flash
                with flash
                "I came inside her so deep that when I pulled out it took a while for some cum to spill out of her."
            "Creampie Leda":
                if ep003_be_sex_last:
                    "I wanted to give the farmer’s wive something to remember me by, so I pulled out of Berit and re-entered Leda. "
                else:
                    "I wanted to give Leda something to remember me by, so I kept fucking her hard."
                scene ep003_sim_farm_le_fuck_doggy_alt with dissolve
                c "Oh Leda!"
                le "Sir!"
                c "Oh Leda, yes!"
                scene ep003_sim_farm_le_fuck_shock with dissolve
                le "Please sir, pull out!"
                "I ignored the pleadings of the farmer’s wife, her pushing hands and erupted inside of her."
                le "No!"
                scene ep003_sim_farm_le_fuck_creampie with flash
                with flash
                "She stopped her protests as all of my seed spilled inside her cunt."
                "I came inside her so deep that when I pulled out it took a while for some cum to spill out of her."
            "Body":
                scene ep003_sim_farm_be_le_fuck_bodies with flash
                with flash
                if ep003_le_sex_last:
                    if game.is_special:
                        "At the last moment, I pulled out of Leda and my cock spurted warm cum all over the bodies of mother and daughter."
                    else:
                        "At the last moment, I pulled out of Leda and my cock spurted warm cum all over the bodies of the woman and her maid."
                else:
                    if game.is_special:
                        "At the last moment, I pulled out of Berit and my cock spurted warm cum all over the bodies of mother and daughter."
                    else:
                        "At the last moment, I pulled out of Berit and my cock spurted warm cum all over the bodies of the woman and her maid."
            "Facial":
                scene ep003_sim_farm_be_le_fuck_facial with flash
                with flash
                if ep003_le_sex_last:
                    "At the last moment, I pulled out of her and brought Leda’s towards my cock, Berit joining her quickly."
                    "Leda was about to say something when my cock spurted warm cum all over her face and in her open mouth."
                    "Berit took a hit of warm cum square in the face too."
                else:
                    "At the last moment, I pulled out of her and brought Berit’s towards my cock, Leda joining her quickly."
                    "Berit was about to say something when my cock spurted warm cum all over her face and in her open mouth."
                    "Leda took a hit of warm cum square in the face too."
        scene ep003_sim_farm_be_le_fuck_post with dissolve
        c "Consider your debt paid."
        scene ep003_sim_farm_leaving_alt with dissolve
        "Leaving the naked women behind, I walked through the door."
        scene black with pixellate
        "All went black and the simulation ended."
        $ renpy.end_replay()
        return

    label ep003_sim_farm_sex_le_hard:
        if _in_replay:
            $ le_name = "Leda"

        scene expression eye_blink("images/ep003/ep003_sim_farm_le_fear") with dissolve
        c "Tell me your name."
        le "Leda, milord."
        c "On your knees and suck my cock."
        le "Yes, milord."
        "I undid my belt and got out of the many layers of clothing I was wearing."
        scene ep003_sim_farm_le_kneel with dissolve
        "Leda sank to her knees and looked up at me."
        c "Good, now pleasure me with your mouth."
        le "Yes, milord."
        scene ep003_sim_farm_le_jerk with dissolve
        "Her hands wrapped around my cock as she brought my member to her mouth."
        "The feeling was so very real, I could sense the roughness of her callused hands brushing my own skin."
        scene ep003_sim_farm_le_suck_solo with dissolve
        "The warm sensation of her mouth enveloping my dick felt just right, even more so when her tongue softly tickled the tip."
        show ep003_sim_farm_le_lick with dissolve
        c "That’s it, Leda."
        show ep003_sim_farm_le_lick_closeup with dissolve
        "I could tell the woman wasn’t that experienced in giving head, as she retched and gagged to take my length inside her mouth."
        c "Let’s go to your bed."
        c "There’s more for you to do than sucking cock."
        "The mattress turned out to be a hemp sack of filled with straw, but I’d have fucked the woman on the dirt floor if need be."
        scene expression eye_blink("images/ep003/ep003_sim_farm_bed_plead_le") with dissolve
        le "Please sir, I have one request."
        c "A request?"
        le "Please spill your seed outside of me..."
        scene ep003_sim_farm_le_penetrate with dissolve
        "I didn’t wait for an answer and pushed her legs apart."
        "Leda cried out when I entered her thoroughly wet pussy, her body surely responded to sucking my cock earlier."
        scene ep003_sim_farm_le_fuck with dissolve
        "The bed creaked as I fucked the woman hard, her moans filling the small living room."
        scene ep003_sim_farm_le_breasts with dissolve
        "I grabbed at her large breasts, luxuriating in the feeling as my hands kneaded its luscious flesh."
        show ep003_sim_farm_le_penetrate_closeup_pleasure_alt with dissolve
        le "Sir, oh sir!"
        show ep003_sim_farm_le_penetrate_closeup_pleasure with dissolve
        c "Do you enjoy getting fucked, Leda?"
        scene ep003_sim_farm_le_fuck_shame with dissolve
        le "Oh, don’t ask me that, sir!"
        c "You enjoy playing my whore."
        le "No sir, no I don’t!"
        c "Say it!"
        le "I enjoying being your whore, sir!"
        c "Good girl, now turn over."
        show ep003_sim_farm_le_fuck_doggy with dissolve
        "The farmer’s wife got up on all fours and I pulled her ass towards me."
        "Then I began to fuck her harder than ever before, her breasts bouncing as violently as her ass cheeks."
        "I took hold of her shoulders and applied pressure, attacking her cunt with short aggressive thrusts."
        le "Oh god!"
        scene ep003_sim_farm_le_fuck_doggy_alt with dissolve
        "My balls slapped against her cunt as it buried itself to the root inside her slit, coming back wetter with every probe."
        "The woman’s moans turned ever hoarser as the fucking grew more intense."
        "I knew I was close...{w} So close..."
        c "Oh Leda!"
        le "Sir!"
        c "Oh Leda, yes!"
        le "Please sir, pull out!"
        menu:
            "Creampie":
                "I ignored the pleadings of the farmer’s wife, her pushing hands and erupted inside of her."
                scene ep003_sim_farm_le_fuck_shock with dissolve
                le "No!"
                "She stopped her protests as all of my seed spilled inside her cunt."
                scene ep003_sim_farm_le_fuck_creampie with flash
                with flash
                "I came inside her so deep that when I pulled out it took a while for some cum to spill out of her."
            "Body":
                scene ep003_sim_farm_le_fuck_body with flash
                with flash
                "At the last moment, I pulled out of her and my cock spurted warm cum all over her body."
            "Facial":
                scene ep003_sim_farm_le_fuck_facial with flash
                with flash
                "At the last moment, I pulled out of her and brought her head towards my cock."
                "She was about to say something when my cock spurted warm cum all over her face and in her open mouth."
        scene expression eye_blink("images/ep003/ep003_sim_farm_le_fuck_post") with dissolve
        c "Consider your debt paid."
        le "Thank you, milord."
        c "Leaving the naked woman behind, I walked through the door."
        scene black with pixellate
        "All went black and the simulation ended."
        $ renpy.end_replay()
        return

    label ep003_sim_farm_sex_be_hard:
        if _in_replay:
            $ be_name = "Berit"

        scene expression eye_blink("images/ep003/ep003_sim_farm_be_fear") with dissolve
        be "Please have mercy, milord!"
        c "Have you ever sucked a cock, Berit?"
        be "No, milord, I’ve never been with a man!"
        be "You’ll find me lacking, I’m sure of it."
        c "On the contrary, you’ve just made this all the more enticing."
        c "Undress."
        scene ep003_sim_farm_be_naked with dissolve:
            yalign 1.0
            ease 8 yalign 0.01
        $ renpy.pause()
        "The girl stopped protesting as she unlaced her clothing."
        c "A beautiful girl like you has never been with a man?"
        be "No, milord."
        be "Not until I’m properly married."
        c "Well, I’m afraid that’s not going to happen."
        c "On your knees."
        scene ep003_sim_farm_be_kneel with dissolve
        "Her lip trembled, but she obliged nonetheless and looked up to me as I disrobed."
        c "You’re going to pleasure me with your mouth."
        be "But how..."
        c "Just open your mouth and use that tongue to make my cock wet."
        show ep003_sim_farm_be_lick with dissolve
        "After a few hesitant licks, I pushed the tip against her lips."
        c "Take it into your mouth."
        show ep003_sim_farm_be_lick_closeup with dissolve
        "She looked up at me again and did as I asked."
        c "That’s it, now suck."
        "The inexperience showed as Berit sucked my cock, her teeth brushing painfully against my shaft, combined with the retching and gagging as my member disappeared halfway into her mouth."
        scene ep003_sim_farm_be_suck_alt with dissolve
        "But the girl proved to be a quick learner and as she picked up on the signals of my body she gradually used her small mouth to perfection."
        "I could have blasted my load down her throat, but I wanted to use Berit in other ways as well."
        c "Let’s go to your bed."
        c "There’s more for you to do than sucking cock."
        scene ep003_sim_farm_bed with dissolve
        "The mattress turned out to be a hemp sack of filled with straw, but I’d have fucked the girl on the dirt floor if need be."
        scene expression eye_blink("images/ep003/ep003_sim_farm_bed_plead_be") with dissolve
        be "Please sir, don’t take my maidenhood!"
        c "I’d think it would be an honor to be fucked by a nobleman."
        be "Only if we marry..."
        c "Well, I’m not going to do that."
        c "Lie down."
        scene ep003_sim_farm_bed_be with dissolve
        "Berit obliged, but it looked as if she wanted to voice more objections."
        "I didn’t want to give her the chance and pushed her legs apart, pulling her bodily towards my cock."
        scene ep003_sim_farm_be_penetrate with dissolve
        "With the head I parted her lower lips and pushed against her entrance."
        be "It hurts!"
        c "Nonsense Berit, you’re so wet..."
        be "You’re too big, sir, please!"
        show ep003_sim_farm_be_penetrate_closeup_pleasure with dissolve
        "Berit cried out when I entered her thoroughly wet pussy, her body surely responded to sucking my cock earlier."
        show ep003_sim_farm_be_penetrate_closeup_pleasure_alt with dissolve
        "Her whimpering turned into a surprised gasp as soon as I was fully inside her."
        be "Oh!"
        scene ep003_sim_farm_be_fuck with dissolve
        "The bed creaked as I fucked the young girl hard, her moans filling the small living room, a virgin no longer."
        "I grabbed at her small breasts, squeezing them greedily and twisting her nipples."
        be "Sir, oh sir!"
        c "Do you enjoy getting fucked, Berit?"
        scene ep003_sim_farm_be_penetrate_closeup_shame with dissolve
        be "Oh, don’t ask me that, sir!"
        scene ep003_sim_farm_be_fuck_alt with dissolve
        c "You enjoy being my little slut."
        be "No sir, no I don’t!"
        c "Say it!"
        scene ep003_sim_farm_be_penetrate_closeup_shame with dissolve
        be "I enjoy being your little slut, sir!"
        c "Good girl, now turn over."
        show ep003_sim_farm_be_fuck_doggy with dissolve
        "The girl got up on all fours and I pulled her ass towards me."
        "Then I began to fuck her harder than ever before, her ass cheeks bouncing violently."
        "Any mention of pain forgotten, Berit seemed fully entranced by the act of fucking."
        scene ep003_sim_farm_be_fuck_doggy_alt with dissolve
        "I took hold of her shoulders and applied pressure, attacking her cunt with short aggressive thrusts."
        be "Oh god!"
        "My balls slapped against her cunt as it buried itself to the root inside her slit, coming back wetter with every probe."
        "The girl’s moans turned ever hoarser as the fucking grew more intense."
        "I knew I was close...{w} So close..."
        c "Oh Berit!"
        c "Oh Berit, yes!"
        menu:
            "Creampie":
                "I wanted Berit so badly I just kept on fucking her until erupted inside of her."
                scene ep003_sim_farm_be_fuck_shock with dissolve
                be "No!"
                be "Not inside me!"
                "She stopped her protests as all of my seed spilled inside her cunt."
                scene ep003_sim_farm_be_fuck_creampie with flash
                with flash
                "I came inside her so deep that when I pulled out it took a while for some cum to spill out of her."
            "Body":
                scene ep003_sim_farm_be_fuck_body with flash
                with flash
                "At the last moment, I pulled out of her and my cock spurted warm cum all over her body."
            "Facial":
                scene ep003_sim_farm_be_fuck_facial with flash
                with flash
                "At the last moment, I pulled out of her and brought her head towards my cock."
                "She was about to say something when my cock spurted warm cum all over her face and in her open mouth."

        scene expression eye_blink("images/ep003/ep003_sim_farm_be_fuck_post") with dissolve
        c "Consider your debt paid."
        "Leaving the naked girl behind, I walked through the door."
        scene black with pixellate
        "All went black and the simulation ended."
        $ renpy.end_replay()
        return

    label ep003_verdant_party:
        $ ep003_verdant_party = True
        scene black with fade
        "I was sorely tempted to go to that party described on the flyer Kit gave me."
        "Whenever we had some free time back at the Academy, Kit and I crashed any party we could find."
        scene ep003_verdant_corridor_alt with dissolve
        "Feeling nostalgic and in a desperate need to take my mind off things, I wandered towards the location indicated on the leaflet."
        "Apparently they had a very lax door policy, because the bouncer let me in straight away."

        play music [ "music/the-water-and-the-well.ogg", "music/eigengrau.ogg" ] fadeout 4 fadein 1.0

        scene ep003_club with dissolve
        "The music inside was overwhelming, the pounding beat overpowering everything."
        scene ep003_club_alt with dissolve
        "I was swallowed in a writhing sea of bodies, my dancing fueled by the strong alcohol they served."
        scene expression eye_blink("images/ep003/ep003_club_girl") with dissolve
        "When the music reached a fevered pitch, a girl caught my eye."
        "She was dancing close-by and tried to get my attention."
        menu:
            "[gr]Dance with her":
                $ ep003_verdant_party_dance = True
                scene ep003_club_girl_dance with dissolve
                "Inching closer we both engaged in a sensual dance, her body pressed hard against mine."
                scene ep003_club_girl_dance_closeup with dissolve
                "My arms firmly around her middle, she grinded her ass against my crotch."
                "I could smell her perfume, mixed with sweat."
                scene ep003_club_girl_dance_kiss with dissolve
                "When she turned her head to meet mine we kissed passionately."
                scene expression eye_blink("images/ep003/ep003_club_girl_dance_laugh") with dissolve
                "Laughing, she took my hand and pulled me through the crowd."
                "She led me through a corridor of alcoves, her gloved fingers entangled with mine."
                scene ep003_club_girl_dance_sex with dissolve
                "I got glimpses of people hidden in the shadow, some were just drinking, others were stark-naked and engaged in the wildest sex imaginable."

                if is_patreon() and renpy.has_label("extra_scene_04") and not _in_replay:
                    call extra_scene_04 from _call_extra_scene_04
                    "Part of me wanted to admire them a little longer, but the girl I was with tugged at my arm."
                    "She lead me past several alcoves, some empty, some filled with people socializing."

                if is_patreon() and renpy.has_label("extra_scene_05") and not _in_replay:
                    "Something in the corner of my eye made me stop."
                    call extra_scene_05 from _call_extra_scene_05
                    "I felt a tug at my arm and the girl I was with pulled me further along, past other booths, in search for one of our own."

                "We arrived at some sort of lounge area where the music wasn’t as loud and found a corner where nobody would disturb us."
                scene ep003_club_girl_skirt with dissolve
                "Still silent, the girl pressed herself against me and guided my hand beneath her skirt."
                scene ep003_club_girl_pussy with dissolve
                "She wasn’t wearing any underwear and my fingers touched her bare pussy."
                scene ep003_club_girl_pussy_pleasure with dissolve
                "As I began to rub her clit, the girl let go of my hand and gasped in my ear, her eager moans lost in the violence of the music."
                "When I pulled back my hand from the wetness between her legs, she began to frantically unbutton my pants."
                scene ep003_club_girl_cock with dissolve
                "Despite the drink, my cock was ready for her and she took it greedily into her hand."
                scene ep003_club_girl_fuck with dissolve
                "Seizing the initiative, I turned her back towards the wall and lifted her on my cock."
                "Her eyes were burning with lust as my penis slid into her soft, wet mound."
                scene ep003_club_girl_fuck_closeup with dissolve
                "We began to move in unison, her arms clasped tightly around my neck."
                "It was only then that I noticed the hardware in place of her arms, the sparse lighting of the club had largely obscured her synthetic limbs."
                scene ep003_club_girl_fuck_breasts with dissolve
                "I didn’t have much time to think about it, because she ripped off her bra to allow me to bury my face in the supple flesh of her young, natural breasts."
                scene ep003_club_girl_fuck_alt with dissolve
                "Her body slammed down on my cock, as I penetrated her deeply."
                scene ep003_club_girl_fuck_alt_closeup with dissolve
                "She whispered in my ear, the sound mostly lost in the violence of the music in the main hall."
                "Losing our balance, we careened into the wall and I lowered her to the ground."
                scene ep003_club_girl_naked with dissolve:
                    yalign 1.0
                    ease 8 yalign 0.01
                $ renpy.pause()
                "She let her skirt drop and offered me a view of her tight ass."
                "I took the invitation and entered her pussy from behind, holding her tightly as my cock slipped past her wet lips."
                scene ep003_club_girl_fucking with dissolve
                "Our love-making took a violent turn as I fucked her with measured strokes, digging my fingers into her breasts and pinching her nipples."
                show ep003_club_girl_fucking_alt with dissolve
                "As the music fell silent for just an instant, I heard her gasps as my dick rammed itself deep inside her ribbed tunnel."
                show ep003_club_girl_fucking_alt_closeup with dissolve
                "Pressing myself against her body, her ass flattened against my abdomen, I wrapped my arms around her and grabbed her slender throat."
                scene ep003_club_girl_fucking_throat with dissolve
                "Controlling her breath, I pinned her with my cock, attacking her cunt with short violent thrusts."
                show ep003_club_girl_fucking_throat_closeup with dissolve
                "Her eyes rolled backward with intense pleasure, her whole body tensing up as I dominated her."
                scene ep003_club_girl_fucking_alt with dissolve
                "When I released my grip on her throat, every muscle in her body relaxed and she let herself be fucked without any restraint."
                menu:
                    "Creampie":
                        $ ep003_girl_creampie = True
                        scene ep003_club_girl_fucking_cum with vpunch
                        "My orgasm was sudden and powerful, as I creamed the inside of her pussy."
                        scene ep003_club_girl_creampie with flash
                        with flash
                        "As she leaned against the wall, breathing heavily, cum started pulsing out of her slit, leaking down her thigh."
                    "Body":
                        scene ep003_club_girl_body with flash
                        with flash
                        "My orgasm was sudden and powerful, as I pulled out and sprayed cum all over her back."
                    "Swallow":
                        "My orgasm was sudden and powerful, but I only allowed it to flow when she was on her knees, facing me."
                        scene ep003_club_girl_swallow with flash
                        with flash
                        "She received a warm load right inside her mouth, cum dripping from the corners of her mouth as she swallowed."
                scene ep003_club_girl_post with dissolve
                "The girl smiled at me and blew me a kiss."
                scene ep003_club_girl_post_empty with dissolve
                "She was gone before I knew it, slipping back into the partying crowd."
                scene black with fade
                "My urges thoroughly satisfied, I didn’t linger much longer at the party and went back to the ship."
            "Don't dance with her":
                scene ep003_club_solo with dissolve
                "I really wanted to get pissed that night, so I ignored her and downed several glasses of whatever they were pouring instead."
                scene black with fade
                "The drink slowly taking over my senses, I didn’t linger much longer at the party and went back to the ship."
        $ renpy.end_replay()
        return

    label ep003_shuttle:
        play music [ "music/simplex.ogg" ] fadeout 4 fadein 1.0

        scene expression eye_blink("images/ep003/ep003_bastard_ce") with dissolve
        ce "[p_name]?"
        ce "There’s something on our sensors."
        c "Debris?"
        ce "No, too close to the station."
        ce "It’s a light shuttle."
        ce "The drive is inert."
        c "Weird."
        ce "I’m going to bring it aboard."

        menu:
            "All right [CelinePath]":
                c "Good idea."
                c "But what if it’s a trap, or something?"
                scene expression eye_blink("images/ep003/ep003_bastard_ce_serious") with dissolve
                ce "That shuttle doesn’t have any weapons, as far as I can tell."
                c "We’ll be prepared."
                scene ep003_bastard_shuttle with dissolve
                "Céline began hauling the shuttle into our cargo bay."
            "Don’t":
                $ ep003_shuttle_refusal = True
                c "Just leave it alone."
                scene expression eye_blink("images/ep003/ep003_bastard_ce_angry") with dissolve
                ce "But someone could be alive in there!"
                ce "That shuttle doesn’t have any weapons, as far as I can tell."
                ce "I’m bringing it in."
                c "What part of “just leave it alone” don’t you understand?"
                ce "There’s clearly something wrong with that shuttle, [p_name_short]."
                ce "There might be people in there who need our help."
                scene ep003_bastard_shuttle with dissolve
                "Despite my protests, Céline began hauling the shuttle into our cargo bay."

        scene ep003_bastard_av_th with dissolve
        "Together with Aven and Thyia I went down to the bay, well-armed."
        "Just when we were about to pry open the shuttle, Céline’s voice sounded over the coms."
        scene expression eye_blink("images/ep003/ep003_bastard_ce_coms") with dissolve
        ce "We’re being hailed by a ship."
        ce "It’s a large cruiser."
        c "Sovereignty?"
        ce "The ship is called “His Eternal Holy Light That Graces Our Paltry Existence A Thousandfold”."
        c "Wow, that doesn’t sound pompous at all."
        c "Put them on speaker if you will."
        scene ep003_bastard_av_th_alt with dissolve
        "A short sound signified that Céline had done what I asked and before I could speak a gravelly voice sounded through the cargo bay."
        $ man_name = "Man"
        man "Unidentified vessel, by the order of His Holiness, Hierophant Sacleus, you will release that shuttle to us immediately."
        man "You have five minutes to comply, otherwise we’ll be forced to disable the drive of your ship like we did with the shuttle you illegally obtained."
        python:
            codex_sacleus = add_codex_entry(
                Codex,
                __("Characters"),
                __("Sacleus"),
                [
                    __("Hierophant Sacleus is the highest ranking member of an unknown religious order and owner of the vessel “His Eternal Holy Light That Graces Our Paltry Existence A Thousandfold”.")
                ]
            )

        c "This is Captain Valenmann de Lonval of the Iron Bastard."
        c "We came across a shuttle and wanted to provide aid."
        c "What claim do you have on the shuttle and what do you want with it?"
        man "You have five minutes to comply."
        ce "They’re targeting us."
        c "I just love that sense of deja-vu..."

        jump episode004
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
