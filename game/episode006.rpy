
image ep006_cell_l_kiss = Movie(play="movies/ep006/ep006_cell_l_kiss.webm", loop=False)
image ep006_sim_stand_buttocks = Movie(play="movies/ep006/ep006_sim_stand_buttocks.webm", loop=False)
image ep006_doctor_ass_fuck_alt = Movie(play="movies/ep006/ep006_doctor_ass_fuck_alt.webm")
image ep006_doctor_doggy_fucking_hair_pull = Movie(play="movies/ep006/ep006_doctor_doggy_fucking_hair.webm")
image ep006_doctor_doggy_fucking_hair_pull_closeup = Movie(play="movies/ep006/ep006_doctor_doggy_fucking_hair_closeup.webm")
image ep006_shower_av_fingering = Movie(play="movies/ep006/ep006_shower_av_finger_alt.webm")
image ep006_shower_av_fingering_closeup = Movie(play="movies/ep006/ep006_shower_av_finger_alt_closeup.webm")
image ep006_sim_dildo_ass_insert_full = Movie(play="movies/ep006/ep006_sim_dildo_ass_insert_full.webm")
image ep006_sim_dildo_ass_insert_full_alt = Movie(play="movies/ep006/ep006_sim_dildo_ass_insert_full_alt.webm")


label episode006:
    $ save_name = "Episode 6"

    $ ep006_sim_ignore = False
    $ ep006_sim_ignore_twice = False
    $ ep006_lilly_shower_peek = False
    $ ep006_lilly_bed_offer = False
    $ ep006_lilly_bed_push = False
    $ ep006_lilly_family = False
    $ ep006_lilly_friends = False
    $ ep006_lilly_love = False
    $ ep006_lilly_comfort = False
    $ ep006_lilly_kiss = False
    $ ep006_aven_lilly_love = False
    $ ep006_aven_truth = False
    $ ep006_aven_compassion = False
    $ ep006_aven_feelings = False
    $ ep006_ra_comfort = False
    $ ep006_ra_berate = False
    $ ep006_ra_ignore = False
    $ ep006_inverview_result = 0
    $ ep006_l_attraction = False
    $ ep006_av_attraction = False
    $ ep006_na_attraction = False
    $ ep006_l_attraction_truth = False
    $ ep006_av_attraction_truth = False
    $ ep006_na_attraction_truth = False
    $ ep006_chrone_attraction = False
    $ ep006_guard_bluff = False
    $ ep006_guard_leave = False
    $ ep006_guard_shoot = False
    $ ep006_guard_confront = False
    $ ep006_doctor_anal = False
    $ ep006_chrone_creampie = False

    play music "music/theoldones.ogg" fadein 4 fadeout 1.0

    scene black with fade
    centered "{=chapter_heading}EPISODE 6{/=chapter_heading}"

    scene ep006_ship with dissolve
    call location_screen (__("Unknown"), True) from _call_location_screen_29

    $ woman_name = "Woman"
    $ woman_portrait = "side_bodyguard"

    scene expression eye_blink("images/ep006/ep006_bridge") with dissolve
    co "Where's the boy now?"
    woman "We've lost track of him after their ship left Verdant Station."
    woman "We're still waiting on further intel from our source."
    scene expression eye_blink("images/ep006/ep006_bridge_closeup") with dissolve
    co "There has been no contact?"
    woman "Not yet, milord."
    co "Has the data retrieved from Mr. Hreir's computer system been analyzed yet?"
    woman "We're still sifting through all of it, but our efforts are hampered by the various encryption schemes he used."
    co "You know how these kind of excuses vex me, woman!"
    scene expression eye_blink("images/ep006/ep006_bridge_alt") with dissolve
    woman "I do, milord."
    woman "I will strive to do better."
    co "I'm sure you will."
    if game.is_special:
        co "Because of his determination to find his sister, the boy is still our best source of information."
    elif True:
        co "Because of his determination to find his friend, the boy is still our best source of information."
    co "But if our informant among his crew has gone dark we need to find other ways to find the girl."
    woman "Yes, milord."
    scene expression eye_blink("images/ep006/ep006_bridge_alt_closeup") with dissolve
    co "Sadly, Hreir wasn't very forthcoming during his final confession, but maybe his records will show us where those warrior women took the boy's sister."
    co "Finding the words of the Prophecy was a great victory, but that was months ago and our progress has stalled since then."
    co "We need the girl, that much is clear from the text."
    scene expression eye_blink("images/ep006/ep006_bridge_alt_closeup_angry") with vpunch
    co "So get me results, or I'll be forced to take your last confession as well."
    scene expression eye_blink("images/ep006/ep006_bridge_alt_serious") with dissolve
    woman "Yes, milord."

    scene black with fade
    play music "music/the-chase.ogg" fadeout 4 fadein 1.0

    scene ep006_asteroids with dissolve
    call location_screen (__("Barranthis Asteroid Belt"), True) from _call_location_screen_30
    "Our euphoria regarding our escape didn't last very long as we had to focus on navigating the asteroid field we found ourselves in."
    "It wasn't as bad as the chaotic belt that surrounded Karan Hreir's asteroid base, but we had to be ready for any nasty surprises."
    scene expression eye_blink("images/ep006/ep006_asteroids_av") with dissolve
    av "What's that thing on the scanners?"
    ki "Larger asteroid?"
    av "It's moving too fast."
    ce "It's moving towards us!"
    scene ep006_asteroids_ce_c with dissolve
    c "Fuck, another ship?"
    c "Any chatter on comms?"
    ce "Nothing."
    scene ep006_asteroids_object with dissolve
    "The thing on our monitors moved at brisk speed, heading straight towards us."
    scene ep006_asteroids_ce_c with dissolve
    ce "They're going to crash into us if we keep this trajectory!"
    c "Evasive manoeuvres."
    "Céline attempted a series of movements that would have taken us outside the trajectory of the object coming towards us."
    scene ep006_asteroids_ce_c_alt with dissolve
    "Instead of responding, several of the Iron Bastard's warning lights began to blink."
    ce "The ship isn't allowing me to steer."
    c "Technical failure?"
    c "Thyia?!"
    scene expression eye_blink("images/ep006/ep006_asteroids_th") with dissolve
    th "All systems are online, it's not us."
    av "We're being jammed!"
    scene ep006_asteroids_ce_c_alarm with vpunch
    "All alarms started to go off on the bridge as the large object came into visual range."
    "Unable to do anything, we stared outside the window to see what was approaching us."
    scene ep006_asteroids_light with vpunch
    "Before the object became visible a searing white light washed over us."
    scene ep006_asteroids_white with hpunch
    "As soon as the light penetrated the bridge all sensory input was taken away."
    scene white with dissolve
    "Within seconds, I lost consciousness."

    play music "music/beautiful-oblivion.ogg" fadeout 4 fadein 1.0

    scene ep006_cell with dissolve
    "I awoke with a terrible headache lying on a mattress."
    "With some difficulty I managed to sit upright and take in my surroundings."
    scene ep006_cell_sit with dissolve
    "Apart from the simple bed I was lying on, the room was furnished with three crude blocks, probably to be used as benches or a table."
    "A portion of the room was shielded by a wall and behind it was a shower."
    "The room was evenly lit by glowing panels worked into the ceiling, emitting a cold light."
    scene ep006_cell_walk with dissolve
    "My bare feet touched the floor, which was surprisingly warm to the touch."
    "The door couldn't be opened despite my fruitless attempts."
    "A small window allowed me to view the area just beyond, a corridor, just as nondescript as my cell."
    "Only then did I notice that I was wearing a coverall, which fit my body perfectly."
    "The garment didn't have any identifying marks."
    scene ep006_cell_think with dissolve
    "I sat down on one of the blocks and tried to gather my thoughts."
    "I remembered a white light and my name, [p_name], but nothing else."
    "It was almost as if memories tried to bubble up in my mind, but something was holding them back, repressing them."
    scene ep006_cell_food with dissolve
    "The sound of the door opening just a fraction startled me and I watched a tray of food being slid inside my cell."
    "Just as sudden as it had opened, the door thudded closed."
    "Curious, I walked towards the tray to see what kind of awful grub they'd served me."
    "The food looked surprisingly appetizing and made me realize how hungry I was."
    scene ep006_cell_eat with dissolve
    "I brought the tray to my bench and proceeded to wolf down the meal I was served."
    "The food tasted as good as it looked."
    "After finishing the meal I tried to collect my thoughts again, but apart from the memory about the white light and knowing my name, nothing else came back."
    "The exercise evidently took its toll on me and I felt increasingly tired."
    scene ep006_cell_sleep with dissolve
    "I thought about trying out that shower, but retired to the bed instead."
    scene black with fade
    "The lights dimmed automatically as I hit the mattress and I fell asleep almost instantly."

    play music [ "music/satiate-only-percussion.ogg" ] fadeout 4 fadein 1.0

    "They came for me while I was sleeping."
    "Light flooded my eyes as I awoke from the sounds of footsteps."
    scene ep006_cell_guards with dissolve
    "Three guards were in my room, one at the door and two standing at my bed."
    c "What the?!"
    c "Where am I?"
    c "Who are you?"
    "The guards didn't speak."
    scene ep006_cell_guards_hold with dissolve
    "Instead, they reached for my arms and pulled me upright."
    "I struggled, but judging from their painful grip they were obviously much stronger than me."
    "I'd never seen aliens like this before, so I had no idea if they even understood me."
    scene ep006_cell_guards_corridor with dissolve
    "They dragged me out of the cell and into the corridor, the third guard leading the way."
    "We didn't encounter anyone else, but passed several similar doors, probably leading to cells like mine."
    "When we reached another section of the facility, the guard opened a door and they manhandled me into a spacious room."
    scene ep006_room with dissolve
    "A single chair formed the most characteristical feature of the decor and it reminded me of something found in an old-fashioned mental hospital."
    scene ep006_room_sit with dissolve
    "When they strapped me into the chair I became even more agitated than I already was and fought my restraints."
    scene ep006_room_dark with dissolve
    "The guards left the room and the lights went out."
    "I couldn't move my legs, arms or even my head."
    "Were they going to torture me?"
    call ep006_sim_01 from _call_ep006_sim_01

    scene ep006_room_dark with dissolve
    "The spotlights went out again and the women disappeared."
    scene ep006_room_light with dissolve
    "My stomach turned and the room suddenly bathed in the harsh light coming from the ceiling."
    "I was looking at a blank wall and heard the guards come in from behind me."
    scene ep006_cell_guards_corridor_return with dissolve
    "They took me back through the empty corridors to my cell and left me on my mattress."
    scene black with fade
    "Thoroughly confused I just remained there and fell asleep."
    scene ep006_cell_food_alt with dissolve
    "When I awoke, a tray of food was already waiting near the door."
    "I got up, retrieved the tray and sat on one of the benches again."
    scene ep006_cell_eat_alt with dissolve
    "As I wasn't as hungry as before, I ate slowly and thought of what happened in the chair."
    "The two women were so familiar and yet, when I tried to focus on retrieving any memory of them, my mind failed."
    "Everything was a haze, though what had happened in that room with the chair I could remember very vividly."
    scene ep006_cell_shower with dissolve
    "After finishing my meal, I decided to take a shower."
    "The water was warm and pleasant and I must have stayed under the stream for almost half an hour."
    "Feeling refreshed I sat on my bench again and wondered what I should do."

    play music "music/satiate.ogg" fadeout 4 fadein 1.0

    scene ep006_cell_guards_alt with dissolve
    "I didn't get the time to finish my thoughts, because the guards barged in again and took me out of my cell."
    scene ep006_cell_guards_corridor_alt with dissolve
    "We crossed the same corridor again and minutes later I was strapped tight into the chair again."
    scene ep006_room_dark with dissolve
    "The lights went out, then nausea returned and the spotlights once again illuminated two women."
    menu:
        "Ignore the women":
            $ ep006_sim_ignore = True
            scene black with fade
            "I closed my eyes, but that didn't seem to help, the scene still played out before my eyes somehow."
            "It was much of the same, but a little more extreme than before, the kneeling woman submitted to another round of debasement."
            scene ep006_room_light with dissolve
            "Throughout the ordeal I tried to think of other, more pleasant things and then it was suddenly over."
            scene ep006_cell_guards_corridor_alt_return with dissolve
            "The guards took me back to my cell and I longed to be alone again."
        "[gr]Look at them":
            call ep006_sim_02 from _call_ep006_sim_02
            scene ep006_cell_guards_corridor_alt_return with dissolve
            "The guards took me back and during the walk through the corridor I made plans to do something about that painful erection as soon as I was alone in my cell again."

    play music "music/beautiful-oblivion.ogg" fadeout 4 fadein 1.0

    scene ep006_cell_entrance with dissolve
    "That didn't happen though, because when they pushed me inside my cell I immediately heard the shower running."
    "For some reason they'd given me a cell mate."
    "Not wanting to startle whomever was inside the shower, I waited on one of the benches until the water stopped running."
    scene ep006_cell_l with dissolve
    "A young redheaded woman emerged from the shower, a towel wrapped around her body."
    scene ep006_cell_l_alt:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "She was as shocked to see me as I was."
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup") with dissolve
    l "Who are you?"
    c "Who're you?"
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup_serious") with dissolve
    l "I asked first."
    c "But this is my cell."
    l "Fine, I'm Lilly."
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup") with dissolve
    "Her name triggered something inside me, as if a thought tried to form itself, but never made it to the surface."
    c "I'm [p_name]."
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup_unsure") with dissolve
    "She looked at me strangely for several seconds as if she was struck by something too, but the moment passed and she sat on the bench opposite of me."
    c "So, who did you piss off to get stuck here with me?"
    l "I don't have a clue, to be honest."
    l "I can't remember much more than my name."
    c "Me too, I'm pretty sure something was done to us."
    c "There's this blank feeling in my mind, as if there's a blanket thrown over my memories, if you know what I mean."
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup") with dissolve
    l "I know exactly what you mean."
    c "Have they strapped you to that chair too?"
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup_fear") with dissolve
    l "What?!{w} A chair?{w} No."
    l "I awoke in a cell much like this one and they shoved food inside once in a while."
    l "Then the guards came and brought me here."
    l "What do they do to you in the chair?"
    c "They make you see disturbing shit."
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup") with dissolve
    l "In that case I'm glad they haven't taken me."
    c "I hope they won't now that you're my cell mate."
    c "I'm glad I have someone to talk to, even if the conversation will be limited, because we both can't remember anything about our lives."
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup_smile") with dissolve
    l "Haha, I'm sure we'll manage."
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup_alt") with dissolve
    "During the moment of silence that followed I tried to study Lilly without making her feel uncomfortable."
    "She looked so familiar and I felt feelings raging under the surface, unable to bloom fully inside my mind, because of the mysterious inhibitions our captors probably imposed on us."
    "Despite our short acquaintance and the limited conversation topics, she intrigued me more and more."
    "Why were we locked up together?"
    "Did we know each other before becoming prisoners?"
    scene expression eye_blink("images/ep006/ep006_cell_l_closeup") with dissolve
    l "Well, I'd better change into that coverall so generously provided to us."
    "She stood up and walked towards the shower."
    menu:
        "Look at her":
            scene ep006_cell_l_behind with dissolve
            "Inadvertently my eyes trailed her and I was shocked to realize I found her very attractive."
            "It was not some casual observation, but something deeper, as if a lone sensation managed to break through whatever barrier blocked my thoughts."
            "Maybe we'd been lovers before ending up here?"
        "Leave her to it":
            scene ep006_cell_l_think with dissolve
            "I racked my brain as to why we could have ended up in a cell together, but it was as if I just couldn't form any coherent mental picture on the matter."
    "Her words shocked me out of my thoughts."
    scene ep006_cell_l_behind_closeup with dissolve
    l "Promise you won't look!"
    "Lilly disappeared behind the shower wall."

    menu:
        "[gr]Have a look":
            $ ep006_lilly_shower_peek = True
            "The recent ordeal in the chair might have made me a little rash, but I simply wanted to have a look at her."
            "I got up, cautiously approached the shower and peeked around the corner."
            scene ep006_cell_l_naked:
                yalign 1.0
                ease 8 yalign 0.01
            $ renpy.pause()
            "Lilly was fully naked and took in the gorgeous curves of her hips and the shape of her luscious ass."
            "She picked up the coverall from a hook on the wall and dressed herself."
            "Before she noticed me I was already back at the bench, staring at something."
        "Remain seated":
            scene ep006_cell_sit_alt with dissolve
            "I stared into the distance as Lilly dressed herself behind the cover of the wall."
    scene ep006_cell_l_sit with dissolve
    "Lilly returned and sat across me again."
    scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup") with dissolve
    l "Do you have any idea what day it is?"
    c "Nope, couldn't tell you the time either."
    c "I think of the time they serve us those meals as being in the evening and I mostly went to bed after eating."
    l "Me too."
    l "Solitary confinement does weird things to you."
    c "Evidently."
    l "How are we going to address the sleeping situation?"
    c "Sleeping situation?"
    c "Oh, the single mattress."
    menu:
        "[gr]You can have it":
            $ ep006_lilly_bed_offer = True
            c "You can use the mattress."
            l "Where are you going to sleep?"
            l "Not on the floor, right?"
            c "That was the plan."
            scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup_smile") with dissolve
            l "Nonsense, we can share the mattress."
            l "Unless you snore, of course..."
        "Sleep together":
            c "I was thinking of sharing one half of the mattress."
            scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup_smile") with dissolve
            l "How very kind."
            l "Works for me, unless you snore..."
    c "I'm not sure..."
    scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup_smirk") with dissolve
    l "Maybe I'll beg for another cell to our kind jailers in the morning and then you'll have your answer."
    c "Deal."
    scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup") with dissolve
    l "I wonder if there are other prisoners like us."
    c "I haven't seen them yet, but when the guards took me to the room with the chair I saw other cells like this one."
    l "It's a large facility I guess."
    l "I'd still like to know if we are lab rats."
    c "We might be."
    c "Or we're two famous space pirates serving several life sentences together."
    scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup_smile") with dissolve
    l "In that case I hope our fellow pirates come to our rescue at some point and break us out."
    scene ep006_cell_l_sit_alt with dissolve
    "Surprisingly, we kept the conversation going without much effort, until two trays of food were slid through a crack in the door."
    scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup_smile") with dissolve
    l "Ready for our candlelit dinner?"
    c "Very much so."
    "We ate our dinner, trying to guess what kind of ingredients were used in the preparation of the weirdly shaped food."
    scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup_smirk") with dissolve
    l "We really have to ask for some wine, next time they serve us."
    c "Good idea."
    c "A proper dessert and some coffee afterwards would be nice too."
    scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup_smile") with dissolve
    l "Right, I'm sure they'll accommodate us."
    c "They can't deny two famous space buccaneers a little luxury."
    scene ep006_cell_l_yawn with dissolve
    "Pushing the finished meals aside, we talked some more until Lilly started to yawn."
    scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup") with dissolve
    l "I think I'm going to bed."
    c "Me too."
    c "Another busy day of staying indoors and eating a tray of food ahead of us, after all."
    scene expression eye_blink("images/ep006/ep006_cell_l_sit_closeup_smile") with dissolve
    l "Haha, right."
    scene expression eye_blink("images/ep006/ep006_cell_l_sleep") with dissolve
    "We both lay on the mattress and I pulled the covers over us."
    c "Good night, Lilly."
    scene expression eye_blink("images/ep006/ep006_cell_l_sleep_closeup") with dissolve
    l "Good night, [p_name]."
    l "Oh and [p_name]?"
    c "Yes?"
    l "I'm delighted to be sharing a cell with you."
    c "The pleasure is entirely mutual."
    scene ep006_cell_l_sleeping with dissolve
    "The lights dimmed and I listened to Lilly's breathing until she was fast asleep, I followed her just a few minutes later."
    scene black with fade

    if is_patreon() and renpy.has_label("extra_scene_12") and not ep006_sim_ignore:
        play music "music/ghost.ogg" fadein 4 fadeout 1.0

        "I didn’t sleep well."
        "It had nothing to do with the fact that Lilly was sleeping next to me, but rather the woman with the whip who stalked my dreams that night."

        call extra_scene_12 from _call_extra_scene_12

        scene black with fade
        "I was about to answer her when everything morphed into something entirely different."
        "Suddenly I was running through endless corridors, pursued by some unknown enemy."
        "My proud erection quickly shrivelled and I began to sweat from irrational fear instead."

        play music "music/beautiful-oblivion.ogg" fadeout 4 fadein 1.0

        "Later, I didn't remember much from those dreams, though the one with the woman stayed with me for quite some time after I woke up in the morning."

    "The ceiling lights brightened again and I awoke slowly."
    scene ep006_cell_l_awake with dissolve
    "Despite keeping to our half of the bed when falling asleep, Lilly hugged my body and had an arm draped across my chest."
    "She was still asleep, undisturbed by the bright lights."
    menu:
        "Push her away":
            $ ep006_lilly_bed_push = True
            "Not wanting to give her the wrong impression, I pushed Lilly away to her side of the bed."
            scene expression eye_blink("images/ep006/ep006_cell_l_awake_open") with dissolve
            "She opened her eyes and look at me in a state of drowsy shock."
            l "Oh!"
            l "Sorry!"
        "Pull her closer [LillyPath]":
            scene ep006_cell_l_awake_alt with dissolve
            "I dared to put an arm around her and pull her just a little closer."
            "Lilly made some light noises of satisfaction and eased her head against my chest."
            "The smell of her hair provoked another unexpected emotion, I wanted to protect her at all costs, this innocent redheaded girl."
            scene expression eye_blink("images/ep006/ep006_cell_l_awake_alt_open") with dissolve
            "At that moment, she opened her eyes and looked up at me drowsily."
            l "Oh..."
            l "I..."
    scene ep006_cell_l_awake_blush with dissolve
    "Visibly flustered, she wormed herself from the embrace and rolled to her side of the mattress."
    c "Good morning."
    "Lilly managed a mumbled greeting and her cheeks flushed."
    l "I'm going to take a shower, if you don't mind."
    c "Not at all."
    scene ep006_cell_l_shower_run with dissolve
    "A little amused, I watched her hurry towards the shower and heard the water running within moments."

    play music "music/satiate-only-strings.ogg" fadeout 4 fadein 1.0

    scene ep006_cell_l_guards with vpunch
    "The door opened and two guards lifted me from the bed before I could warn Lilly."
    "They dragged me once again to the room with the chair."
    scene ep006_room_dark with dissolve
    "Without a word they strapped me into the chair and fear coursed through my body again."
    "The blonde slave and her Mistress appeared again."
    menu:
        "[gr]Watch":
            call ep006_sim_03 from _call_ep006_sim_03
            scene ep006_cell_guards_corridor_return with dissolve
            "The guards took me away, apparently not noticing or purposely ignoring my raging erection bulging between my legs."
        "Think of other things":
            $ ep006_sim_ignore_twice = True
            scene black with fade
            "I zoned out as another humiliating display was acted out before my eyes."
            scene ep006_cell_guards_corridor_return with dissolve
            "The thought of coming back to Lilly in my cell kept me occupied until the guards came to take me away."

    "I still didn't know whether to tell Lilly about my experiences in the chair."
    "Because she wasn't subjected to any of it I didn't think it wise to alarm her about the blatant pornography I was subjected to."
    "Frankly, I didn't want to spoil my budding relationship with the girl with stories about sexual torture."
    scene ep006_cell_entrance_alt with dissolve
    "When the guards delivered me to my cell I thought Lilly was in the shower again."
    "Then I noticed there wasn't any water running."
    "The cell was completely empty."
    scene ep006_cell_sit_worry with dissolve
    "A little worried and dejected I sat on one of the benches."
    "Was Lilly moved to another cell again, or did they subject her to a session in the chair as well?"
    "I waited for what felt like several hours, but it could have easily been less than sixty minutes."

    play music "music/midsommar.ogg" fadeout 4 fadein 1.0

    scene ep006_cell_door_open with dissolve
    "The door opened."
    scene ep006_cell_door_open_l with dissolve
    "At first I thought they'd brought my food, but the door opened fully and Lilly was pushed in."
    "Her despairing expression made my heart sink."
    scene ep006_cell_door_open_l_closeup with dissolve
    c "Lilly?"
    c "What did they do to you?"
    "She approached me, but I had to cover the last few inches."
    scene ep006_cell_l_cry with dissolve
    "We faced each other and she looked up to me, with tears in her eyes."
    scene ep006_cell_l_crying with dissolve
    "She fell against my chest and started crying."
    "I took her into my arms and held her as she sobbed without restraint."
    scene ep006_cell_l_crying_closeup with dissolve
    l "I was so scared."
    c "Did they hurt you?"
    l "No, no, nothing like that!"
    scene ep006_cell_l_crying_alt with dissolve
    "Relieved, I held her tightly, as she slowly calmed down and regained control over her breathing."
    c "Do you want to sit down?"
    l "Yes, on the bed please."
    scene ep006_cell_l_crying_sit with dissolve
    "She put her head in my lap as soon as we sat down."
    "After a shuddering sigh, she remained silent."
    "We just sat there, Lilly staring in the distance, until I dared to break the silence."
    scene expression eye_blink("images/ep006/ep006_cell_l_crying_sit_closeup") with dissolve
    c "Do you want to talk about it?"
    l "Not really, but maybe I should."
    l "They put me in a chair for the first time."
    c "Fuck."
    c "I should have prepared you more for that experience."
    l "I'm not sure you could have."
    scene expression eye_blink("images/ep006/ep006_cell_l_crying_sit_closeup_fear") with dissolve
    l "At first I thought they were going to torture me, pull out my nails or something."
    l "Instead the lights went out and I almost puked."
    l "And then..."
    scene expression eye_blink("images/ep006/ep006_cell_l_crying_sit_closeup_fear_alt") with dissolve
    "She gripped my hand in fear as the memories about her time in the chair came back to her."
    l "They showed me things."
    l "Terrifying things."
    l "Things that looked so familiar, but I couldn't really place them, like something prohibited me."
    c "I know the feeling."
    scene expression eye_blink("images/ep006/ep006_cell_l_crying_sit_closeup_serious") with dissolve
    l "There's this house in a field."
    l "It's totally dark, save for the light coming through the windows."
    l "I walk towards the front door, light is coming from under the door and something is buzzing."
    l "I place my hand on the door handle and the buzzing gets louder, everything starts trembling."
    l "I feel a presence approaching, from the other side."
    l "And fear grips me, overwhelming, primal fear."
    scene expression eye_blink("images/ep006/ep006_cell_l_crying_sit_closeup_fear") with dissolve
    l "I screamed and I was still screaming when the lights suddenly blinked on."
    "Lilly told her story with fits and starts, but she managed to get to the end."
    "Her experience in the chair sounded very different from mine."
    "While my sessions played out some debased sexual fantasy, hers tapped into some form of existential dread."
    c "They're making you experience nightmares."
    c "I think we're both put in some kind of simulation, the nausea is an indicator."
    c "But for what purpose?"
    scene expression eye_blink("images/ep006/ep006_cell_l_crying_sit_closeup_doubt") with dissolve
    l "Some twisted scientific experiment, maybe?"
    c "Could be."
    c "I really hope they're not going to subject you again."
    l "I think they will."
    c "Fuck, I wish I could help you get through those nightmares."
    scene expression eye_blink("images/ep006/ep006_cell_l_crying_sit_closeup_smile") with dissolve
    l "Talking about it with you helps."
    l "There's nothing else you can do I'm afraid."
    l "But they're not showing you nightmares in the chair?"
    c "No, I was a little afraid to tell you."
    scene expression eye_blink("images/ep006/ep006_cell_l_crying_sit_closeup_doubt") with dissolve
    l "Why?"
    c "Because they're showing me some sort of twisted sex dream."
    c "Two women, one exerts control over the other."
    l "Damn, I get the nightmares and you get treated to wet dreams, I know what I'd prefer..."
    scene ep006_cell_l_laying with dissolve
    "We lay down on the bed, Lilly lying on my stomach, probably still feeling a little rattled about what happened to her."
    l "You said you know about those memories that feel prohibited?"
    c "Yes, I do."
    c "I know my own name, but nothing else."
    scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup") with dissolve
    l "But what about those suppressed memories, when did you experience those?"
    c "When I first saw you."
    l "Really?"
    c "You sound surprised?"
    l "Yes, because I had it too."
    scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_unsure") with dissolve
    l "Didn't you notice me gawking at you for several seconds?"
    c "I probably was too busy doing it myself."
    scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup") with dissolve
    l "Could you describe what happened when you first saw me?"
    c "I don't know exactly."
    c "Something pleasant welled up in my mind, but it didn't burst to the surface somehow."
    scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_unsure") with dissolve
    l "As if it was hidden under a thick blanket?"
    c "Exactly like that."
    l "So maybe we knew each other before?"
    c "The thought crossed my mind."
    scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup") with dissolve
    l "It makes sense."
    l "I had the exact same feeling when I first saw you."
    menu:
        "Maybe we're family":
            $ ep006_lilly_family = True
            c "Maybe we're family or something?"
            scene ep006_cell_l_laying_closeup_laugh with dissolve
            l "Yeah right, distant family in that case, because I'm much cuter than you!"
            c "Sure!"
        "Maybe we're friends":
            $ ep006_lilly_friends = True
            c "Maybe we're best friends or something?"
            scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_serious") with dissolve
            l "Could be, though it felt more complicated."
            c "Mortal enemies then?"
            scene ep006_cell_l_laying_closeup_laugh with dissolve
            l "Haha, maybe something in between."
        "Maybe we're in love [LillyPath]":
            $ ep006_lilly_love = True
            c "What did you feel exactly?"
            scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_unsure") with dissolve
            l "I don't know..."
            l "Something very strong and a kind of wild fluttering in my stomach."
            c "Like butterflies?"
            scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup") with dissolve
            l "Like butterflies..."
            scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_unsure") with dissolve
            l "You don't think..."
            c "It could be."
            l "Love?"
            c "You sound really unsure."
            scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_doubt") with dissolve
            l "It's just, why would we forget something like that?"
            c "I'm not sure, but I don't think we forgot it willingly."
            scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_serious") with dissolve
            l "Right."
            c "But to be very honest, I don't hate having you close to me."
            scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_shy") with dissolve
            l "Oh...{w} eh..."
            c "Are you blushing?"
            scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_angry") with dissolve
            l "Just lay off, [p_name]!"
    scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_doubt") with dissolve
    l "You've gotten me all confused!"
    c "Sorry."
    scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup") with dissolve
    l "Don't be."
    l "I just need to think about it, that's all."
    l "Why don't we try and get some sleep."
    c "Sounds like a good idea."
    scene expression eye_blink("images/ep006/ep006_cell_l_laying_closeup_smile") with dissolve
    l "Good night, [p_name]."
    c "Good night, Lilly."
    if ep006_lilly_love:
        scene ep006_cell_l_sleep_alt_embrace with dissolve
    else:
        scene expression eye_blink("images/ep006/ep006_cell_l_sleep_alt") with dissolve
    "The lights dimmed automatically and Lilly's breathing became very regular after just a few minutes."
    "I had more trouble falling asleep, mulling over what we just talked about."
    if ep006_lilly_love:
        "I was also acutely aware of the nearness of her body, feeling so comfortable against my own."
    else:
        "I was also acutely aware of the nearness of her body, our hands almost touching."
    scene black with fade
    "Once I concentrated on her measured breathing I managed to fall asleep as well."
    with vpunch
    "In pitch blackness I woke up to screams."
    scene ep006_cell_l_scream with vpunch
    "It was Lilly."
    "She was half-awake and sounded absolutely terrified."
    menu:
        "Comfort her [LillyPath]":
            $ ep006_lilly_comfort = True
            scene ep006_cell_l_scream_embrace with dissolve
            "As the ceiling light went on again, I reached for her and she gave herself over to my embrace, her last screams dying against my chest."
            scene ep006_cell_l_scream_embrace_alt with dissolve
            "Lilly sobbed and trembled, now fully awake, but still unable to speak."
            c "Don't be afraid, I'm here for you."
            c "There's nothing to be afraid of."
            "It took quite a while for the trembling to subside and her breathing to steady."
            scene expression eye_blink("images/ep006/ep006_cell_l_scream_embrace_closeup") with dissolve
            l "I saw it again, [p_name]."
            l "The house.{w} The buzzing..."
            l "I don't want to go to sleep again."
            scene expression eye_blink("images/ep006/ep006_cell_l_scream_embrace_closeup_fear") with dissolve
            l "I'm so afraid."
            "My words failing me, I stroked her hair and just held her."
            scene expression eye_blink("images/ep006/ep006_cell_l_scream_embrace_closeup_sad") with dissolve
            "Lilly looked up to me, her eyes reflecting a whole range of conflicting emotions."
            scene expression eye_blink("images/ep006/ep006_cell_l_scream_embrace_closeup_front") with dissolve
            menu:
                "Kiss her [LillyPath]":
                    $ ep006_lilly_kiss = True
                    show ep006_cell_l_kiss_still with dissolve
                    show ep006_cell_l_kiss with dissolve
                    "My lips reached for hers and we kissed."
                    "We were careful at first, as if afraid one of us would pull away."
                    "When none of that happened, any reluctance dissolved in an instant."
                    scene ep006_cell_l_kiss_alt with dissolve
                    "Drawing in the smell of her hair, feeling the firmness of her body against mine, I kissed her over and over."
                    "Her hands touched me all over my chest, pulling at me, as if wanting me ever closer."
                    "The desire to touch her, to meld together even, was overpowering, but at the same time another feeling struck me, for the first time, everything made perfect sense."
                    "Lilly was mine and I was hers."
                    scene ep006_cell_l_kiss_breast with dissolve
                    "She gasped when I cupped one of her breasts in my hand, but made no attempt to stop me."
                    "Almost regretting it, I parted my lips from hers and moved slowly downwards."
                    scene ep006_cell_l_kiss_neck with dissolve
                    "She arched her back to allow me to brush her soft skin with my lips."
                    "I could feel her heart beating heavily as my caresses took her breath away."
                "Keep holding her":
                    scene ep006_cell_l_lay_chest with dissolve
                    "I kept holding and lay down with her again, her head resting on my chest."
                    "Despite her fear, she couldn't fight the sleep and after a long time her eyelids became heavy again."
                    scene black with fade
                    "She fell asleep on my chest and I followed soon after."
        "Let her sleep":
            "I thought it was better not to disturb her, maybe scaring her even more."
            scene black with fade
            "The screaming subsided quickly and Lilly fell asleep with a whimper."

    play music [ "music/satiate-only-percussion.ogg" ] fadeout 4 fadein 1.0

    "Suddenly the lights went on."
    if ep006_lilly_kiss:
        scene ep006_cell_l_bed_shock with vpunch
        "We practically jumped up in shock, standing on both sides of the bed."
    else:
        scene ep006_cell_l_bed_shock_alt with vpunch
        "We were both awake in an instant."
    "Four guards came in and walked towards us."
    scene ep006_cell_l_guards_alt with vpunch
    l "Leave us alone!"
    c "Get your fucking hands off her."
    scene ep006_cell_l_c_guards with dissolve
    "The guards didn't understand us or clearly didn't care and grabbed us both."
    "We were hauled outside and I fully expected them to take me to the room with the chair again."
    scene ep006_cell_l_c_guards_corridor with dissolve
    "Instead the two guards holding me followed their colleagues who had Lilly and together we went into a different direction."
    l "Where are you taking us?"
    "The dread in Lilly's voice was palpable and a powerful hatred took root inside of me."
    "I wanted to lash out at the people who'd done those things to her, treating us like lab animals to be experimented upon."
    scene ep006_cell_l_c_guards_corridor_alt with dissolve
    "The guards must have sensed my growing tension, because they held me tighter and shoved me in front of them."
    scene ep006_new_cell with dissolve
    "We reached a door which opened automatically, giving way to another cell, much larger than ours."

    play music "music/hiraeth.ogg" fadeout 4 fadein 1.0

    scene ep006_new_cell_women with dissolve
    "Two women were sitting at a makeshift table together and looked very surprised to see us."
    "We were pushed in and the door closed quickly behind us."
    scene expression eye_blink("images/ep006/ep006_new_cell_av") with dissolve
    av "Great, roommates... now we have to share a bed."
    scene expression eye_blink("images/ep006/ep006_new_cell_na") with dissolve
    na "Be a little more polite, Aven."
    scene ep006_new_cell_av_na with dissolve
    av "You're not my mother, Nadya."
    na "Well, we don't know that for sure."
    na "My name is Nadya and this is Aven."
    scene ep006_new_cell_av_na_l with dissolve
    l "Pleased to meet you, I'm Lilly and this is [p_name]."
    scene expression eye_blink("images/ep006/ep006_new_cell_na") with dissolve
    "Like first meeting Lilly, I was struck by something I couldn’t quite place."
    "A clouded memory so vague I had no choice to just dismiss it."
    scene expression eye_blink("images/ep006/ep006_new_cell_av_curious") with dissolve
    "I was distracted by the girl named Aven anyway, who’d sauntered over and took a good look at us both."
    "She hid her surprise well when she looked at me, but for a split second a look of shock marred her face when she looked right into my eyes."
    scene expression eye_blink("images/ep006/ep006_new_cell_av_shock") with dissolve
    "I didn’t know whether it was recognition or some other realization, but it sure was weird."
    "The woman named Nadya looked at us for a long time before speaking again."
    scene expression eye_blink("images/ep006/ep006_new_cell_na") with dissolve
    na "I trust you don't know how you got here as well?"
    c "Yes, we were in a similar cell together for a while."
    c "Do they take you out for tests as well?"
    scene expression eye_blink("images/ep006/ep006_new_cell_av") with dissolve
    av "Tests?"
    scene expression eye_blink("images/ep006/ep006_new_cell_na") with dissolve
    na "Maybe they’re doing the same to them as they do to you?"
    av "I’ve told you before, as soon as they bring me into that room I lose consciousness."
    na "Right, so you’ve told me."
    na "Aven has been taken three times since we woke up here together."
    scene expression eye_blink("images/ep006/ep006_new_cell_av") with dissolve
    av "The only other time the door has opened is when they brought you in and when they shove food inside."
    "I somehow got the feeling the girl wasn’t telling everything, but as I wasn’t in a position to confront her I shelved the thought for later."
    l "So you've been here all this time?"
    av "Yes, Nadya and I woke up together in this room."
    av "Though we don't know how long it's been and why we are together."
    scene expression eye_blink("images/ep006/ep006_new_cell_na") with dissolve
    na "We'd just finished sleeping when you arrived."
    na "But what tests do they run on you, or are you unconscious just like Aven?"
    c "They make you see things, experience things."
    c "Scary stuff and some of it downright confusing."
    na "Seems like the tests are different from person to person."
    scene expression eye_blink("images/ep006/ep006_new_cell_av") with dissolve
    av "All in all, it doesn't sound like a very nice break from all the boredom of being cooped up in here."
    av "Anyway, I'd give you guys a guided tour of the place, but this is everything there is to see."
    av "Also, you probably already know, but be careful what you say in here, they're likely monitoring us."
    c "I'm quite sure of it."
    c "There are at least some automated systems in place which register our sleep and wake patterns."
    scene expression eye_blink("images/ep006/ep006_new_cell_na") with dissolve
    na "It's more than just that, I'm afraid."
    na "There was an incident..."
    na "We just woke up here and discussed our options."
    na "Apparently, Aven was a little too proactive, because they came into the cell and beat her down."
    c "They beat you, Aven?"
    scene expression eye_blink("images/ep006/ep006_new_cell_av_serious") with dissolve
    av "That's too big a word, they just subdued me very effectively..."
    av "I guess they didn't like my investigation of the ceiling and cell door."
    av "But it's pretty clear they know exactly what we're saying and doing in here."
    scene ep006_new_cell_women_alt with dissolve
    "We talked some more and made sleeping arrangements."
    "Lilly and I were allowed on one bed, while Nadya and Aven would share the other."

    if ep006_lilly_kiss:
        scene expression eye_blink("images/ep006/ep006_new_cell_women_l") with dissolve
        "Despite the joy of having new people to talk to, I longed to be alone with Lilly again."
        "I desired her touch, wanted to hold her, tell her how beautiful she looked, even in her prison bodysuit."
        scene expression eye_blink("images/ep006/ep006_new_cell_women_l_smile") with dissolve
        "Lilly must have felt the same way, because she stayed close to me."
        "At one point she touched my arm to get my attention, which had an electrifying effect on me."
        scene expression eye_blink("images/ep006/ep006_new_cell_women_av") with dissolve
        "That's when I noticed Aven looking at us."
        "I couldn't exactly place the look she wore on her face."
        "Was it envy, dismissal or just curiosity?"
        scene ep006_new_cell_women_av_na with dissolve
        "She quickly recovered and struck up a conversation with Nadya and the moment passed."
        "When we all ran out of stuff to talk about, we tried to pass the time in different ways."
        scene ep006_new_cell_women_idle with dissolve
        "Nadya just stared in the distance, while Aven pulled off a series of quick pushups."
        "Lilly seemed a little lost since we were transferred to the new cell, like she didn’t know how to behave around these two new women."
        scene expression eye_blink("images/ep006/ep006_new_cell_women_idle_l") with dissolve
        "She looked at me and I beckoned her."
        scene ep006_new_cell_l_sit with dissolve
        "After a moment’s hesitation she came and sat down next to me."
        scene expression eye_blink("images/ep006/ep006_new_cell_l_closeup") with dissolve
        "I pulled her closer and she allowed her head to rest on my shoulder."
        c "How are you feeling?"
        l "Fine, a little tired after last night."
        c "What do you think of the new roommates?"
        l "They seem nice..."
        c "But?"
        scene expression eye_blink("images/ep006/ep006_new_cell_l_closeup_doubt") with dissolve
        l "I don’t know... Do you think they look familiar?"
        c "Not exactly."
        c "I don’t think I remember their faces, but something is familiar about them."
        l "Exactly."
        c "Is that what’s bothering you?"
        scene expression eye_blink("images/ep006/ep006_new_cell_l_closeup_serious") with dissolve
        l "A little."
        l "I was just starting to get used to living alone with you in one cell, if you know what I mean."
        l "This changes the dynamic entirely and I’m not sure if I like it."
        c "Right, prying eyes and all that."
        l "Yes, that Aven doesn’t seem to miss much."
        l "Though we weren’t exactly alone in our previous cell either."
        c "Yeah, the surveillance isn’t surprising, but disturbing nonetheless."
        scene ep006_new_cell_l_closeup_alt with dissolve
        "Lilly sighed and pressed her body more firmly against mine."
        "I just enjoyed her nearness and watched Nadya lost in thought and Aven continue her exercising."
        "Four trays of food eventually arrived and we all sat down for dinner."
        scene ep006_new_cell_dinner with dissolve
        "To stave off the boredom we slowly ate our food and talked a lot about absolutely nothing, because we all couldn’t remember anything about our past lives."
        "Coming up with fresh conversation topics turned out to be very tiresome for all of us after a while and we decided to go to sleep not long after clearing the trays."
        scene ep006_new_cell_sleep with dissolve
        "Lilly and I took one of the beds as Nadya occupied the other one."
        "Aven said she wanted to take a shower first."
        scene ep006_new_cell_sleeping with dissolve
        "Both Lilly and Nadya slept when the first streams of water started running."
        "Only the shower area was now lit, the rest of the room was wrapped in semi-darkness."
        "Despite having Lilly lying comfortably next to me, I couldn’t sleep."
    else:
        scene ep006_new_cell_women_idle with dissolve
        "Lilly amused herself by staring at the walls, while Nadya was lost in thought and Aven continued her exercising."
        scene ep006_new_cell_dinner with dissolve
        "Four trays of food eventually arrived and we all sat down for dinner."
        "To stave off the boredom we slowly ate our food and talked a lot about absolutely nothing, because we all couldn’t remember anything about our past lives."
        "Coming up with fresh conversation topics turned out to be very tiresome for all of us after a while and we decided to go to sleep not long after clearing the trays."
        scene ep006_new_cell_sleep with dissolve
        "Lilly and I took one of the beds as Nadya occupied the other one."
        "Aven said she wanted to take a shower first."
        scene ep006_new_cell_sleeping with dissolve
        "Both Lilly and Nadya slept when the first streams of water started running."
        "Only the shower area was now lit, the rest of the room was wrapped in semi-darkness."
        "Maybe it was because of Lilly lying next to me, but I couldn’t sleep."

    scene ep006_new_cell_shower with dissolve
    "After a while I heard Aven turn off the water and I expected her to emerge from the shower after a couple of minutes, but she didn’t."
    "Above Lilly's heavy breathing I could eventually hear distinct sighs coming from the shower cubicle."
    "When the sighing turned into frequent moans, I had a pretty clear idea what was happening."
    menu:
        "[gr]Have a look":
            "I just had to sate my curiosity and slipped out of bed."
            call ep006_aven_shower from _call_ep006_aven_shower

            scene ep006_new_cell_shower_av with dissolve
            "I had just returned when Aven emerged from the shower."
            "She hid her shock well when she noticed me looking at her."
        "Remain in bed":
            "I understood the urge to relieve the tension all too well and decided to leave Aven be for the moment."
            scene ep006_new_cell_shower_av with dissolve
            "She must have brought herself to a very restrained climax quickly, because her return from the shower surprised me."
            "Aven hid her shock well when she noticed me looking at her."

    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_alt") with dissolve
    av "Can’t sleep?"
    "Not wanting to wake up Lilly, I slipped out of bed and shuffled towards Aven."
    c "Nope."
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup") with dissolve
    av "I’d offer you something to drink, but I already drank my entire water ration for the day."
    c "Some hard alcohol would be nice right about now, yeah..."
    av "I hear you."
    "The girl sighed and stared into the distance."
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_serious") with dissolve
    av "I don’t know how much longer I can take this."
    av "The empty conversations with Nadya and now with you guys, drawing a blank every time you try to think a little deeper about your own past."
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_angry") with dissolve
    av "I fucking hate it."
    c "I feel the same."
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup") with dissolve
    c "There’s this promise of something lying just beneath the surface, but you just can’t reach it."
    av "Right."
    c "I felt it strongly with Lilly and again with you and Nadya."
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_doubt") with dissolve
    av "Really?"
    av "What’s the deal with you and Lilly anyway?"

    menu:
        "We’re in love [AvenPath]":
            $ ep006_aven_lilly_love = True
            c "We’re in love."
            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup") with dissolve
            av "How do you know that?"
            c "Because we both felt something so strongly when we first met here."
        "I don’t know":
            c "It’s complicated."
            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup") with dissolve
            av "Isn’t it always?"
            c "We both had strong feelings we couldn’t place when we first saw each other."

    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_doubt") with dissolve
    av "You did?"
    c "You sound skeptical?"
    av "I do?"
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_sad") with dissolve
    av "Sorry."
    av "I didn’t mean to."
    c "I saw you looking at us earlier."
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_angry") with dissolve
    av "So, we’re in a cramped cell, where else was I supposed to look?"
    c "Look, I didn’t mean to put you on the defensive here..."
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_sad") with dissolve
    av "I know you didn’t."
    av "Fuck."
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_serious") with dissolve
    av "When you first got here you told us they were doing tests on you, right?"
    av "Making you experience things?"
    c "Yes, that’s right."
    av "I lied to Nadya."
    av "I’ve been fully conscious for every test they administered."
    c "Really, why would you lie?"
    av "The same reason why you’re so vague about it, I reckon."
    av "Because it’s invasive and confusing and...{w} Sexual..."
    c "You too?"
    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_sad") with dissolve
    av "Yes."
    av "So that means they’re making you see stuff too?"

    menu:
        "Truth [AvenPath]":
            $ ep006_aven_truth = True
            c "They do."
            c "It’s different for all of us I think, because Lilly is experiencing nightmares."
            c "I just see more or less the same scene played out between two women, some sort of sexual powerplay."
            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_shock") with dissolve
            av "Wow."
            av "Do you know those women?"
            c "I haven’t got a clue, because I can’t remember anything."
            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_serious") with dissolve
            av "Same here."
            av "With me they’re feeding me images of myself and a man."
            av "We’re both naked and I’m lying down and he’s kissing me all over."
            av "The scene plays out with some variations, but right at the moment where things start to get good everything stops."
            c "Bummer."
            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_smile") with dissolve
            av "Yeah."
            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_serious") with dissolve
            av "Thing is though, the guy in that simulation...{w} It’s you."
            av "So you might imagine why I looked like a ghost had just entered my cell a while back."
            c "Yeah..."

            menu:
                "Ask about her feelings [AvenPath]":
                    $ ep006_aven_compassion = True
                    c "Are you all right?"
                    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_doubt") with dissolve
                    av "Why wouldn’t I be?"
                    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_smile") with dissolve
                    av "I didn’t say it was unpleasant, did I?"
                    c "No, but meeting me like that, it must have been scary."
                    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_doubt") with dissolve
                    av "Scary?"
                    c "Hell, I don’t know."
                    c "You’re being fed these images to your brain and all of a sudden the subject is walking through that door."
                    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_serious") with dissolve
                    av "Scared is not what I felt."
                    c "What did you feel then?"
                    av "I don’t know...{w} Fuck..."
                    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_doubt") with dissolve
                    av "Happy, I guess?"
                    c "Happy?"
                    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_serious") with dissolve
                    av "Right, that really doesn’t cover it."
                    av "I had more or less the same feeling when I saw Nadya for the first time."
                    av "But with you it’s different, stronger, almost something electric."
                    av "I don’t know how else to explain it."
                    menu:
                        "Acknowledge the feeling [AvenPath]":
                            $ ep006_aven_feelings = True
                            c "I know what you mean."
                            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_doubt") with dissolve
                            av "You do?"
                            av "But you never saw me before right?"
                            c "Not that I can remember and not in any simulation either."
                            c "There was something though when I first saw you."
                            c "A spark."
                            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_smile") with dissolve
                            av "Something deep inside your stomach, something indefinable, but not unwelcome?"
                            c "Pretty much, yes."
                            av "So I either hated your guts before and they’re trying to re-educate me, or there was something else."
                            c "I really hope it’s the latter, to be honest."
                            scene ep006_new_cell_shower_av_laugh with dissolve
                            av "Haha, I bet you do."
                            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_doubt") with dissolve
                            av "But [p_name], if you felt a spark...{w} what does that say about Lilly?"
                            if ep006_lilly_kiss or ep006_lilly_love:
                                c "Fuck..."
                                c "It’s all too complicated."
                            else:
                                c "What about her?"
                                c "I already told you we aren’t together."
                            scene ep006_new_cell_av_sit with dissolve
                            "Aven nudged closer to me, until our knees almost touched."
                            "I could smell the shampoo she’d just used in the shower and felt the comfortable warmth she emanated."
                            scene expression eye_blink("images/ep006/ep006_new_cell_av_sit_closeup") with dissolve
                            av "Prison might not be the best place to start a relationship, I agree."
                            av "Maybe we should make a deal."
                            c "A deal?"
                            scene expression eye_blink("images/ep006/ep006_new_cell_av_sit_closeup_smile") with dissolve
                            av "When we get out of here, yes when, we’re going to have a serious talk about this."
                            av "Away from Nadya and Lilly and the fuckers who are listening in on us at the moment."
                            c "Deal."
                            scene expression eye_blink("images/ep006/ep006_new_cell_av_sit_closeup") with dissolve
                            av "I’m going to try and get some sleep now, I think."
                            scene expression eye_blink("images/ep006/ep006_new_cell_av_sit_closeup_smile") with dissolve
                            av "Oh and [p_name], I’m glad I met you today."
                            scene ep006_new_cell_av_sit_kiss with dissolve
                            "When Aven stood up she bowed towards my cheek and brushed it with her soft lips."
                            av "Sleep well."
                            scene ep006_new_cell_av_sleep with dissolve
                            "A little dumbfounded I watched her lie down next to Nadya and go to sleep."
                            "I followed not long after, but it took a long while before I actually fell asleep."
                        "Don’t talk about it":
                            c "I know."
                            c "It’s hard to put something like this into words."
                            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_sad") with dissolve
                            av "Yeah..."
                            av "Hey, if you don’t mind I’m going to get some sleep."
                            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_smile") with dissolve
                            av "Good night."
                            c "Sleep well."
                "Ignore her feelings":
                    c "So, that was awkward."
                    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_smile") with dissolve
                    av "You could say so."
                    c "I hope I didn’t give you too much of a scare."
                    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_serious") with dissolve
                    av "No, it’s okay."
                    c "Those fuckers, messing around in our heads like that!"
                    scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_sad") with dissolve
                    av "Yeah..."
                    av "Hey, if you don’t mind I’m going to get some sleep."
                    av "Good night."
                    c "Sleep well."
        "Lie":
            c "They do."
            c "But I think it’s different for all of us."
            c "Lilly is experiencing nightmares."
            c "Mine are just these weird fever dreams."
            scene expression eye_blink("images/ep006/ep006_new_cell_shower_av_closeup_serious") with dissolve
            av "Hmmm, weird."
            av "Why would it differ so much per person?"
            c "Probably part of some psychological evaluation or something."
            av "Must be."

    play music "music/satiate-only-percussion.ogg" fadeout 4 fadein 1.0

    scene ep006_new_cell_guards with dissolve
    "I was hoping for a quiet and lazy morning, but instead two guards walked in and manhandled me off the bed."
    "Lilly was awake instantly and started screaming."
    scene ep006_new_cell_guards_l with dissolve
    l "Get your fucking hands off him!"
    scene ep006_new_cell_guards_l_fight with dissolve
    "She hit one of the guards and her nails raked the cheek of the other one leaving bloody gashes."
    "The guards let go of me and turned their attention to Lilly."
    scene ep006_new_cell_guards_l_fight_alt with dissolve
    "The guard reached for his gun and stunned the raging girl into submission."
    "They proceeded to wrestle me towards the exit."
    "Nadya and Aven looked at me in fear and disbelief as I was dragged from the cell."
    scene ep006_new_cell_guards_women with dissolve
    c "Don't worry about me, take care of Lilly, please!"
    "Walking at a very brisk pace, the guards took me to a section of the facility I hadn't been before."
    scene ep006_office with dissolve
    "They guided me into what looked like an office."
    "That probably meant no simulated wet dreams for me today..."
    scene ep006_office_chair with dissolve
    "The guards forced me down into a chair and positioned themselves near the door."

    play music [ "music/dark-dreams.ogg", "music/facility.ogg" ] fadeout 4 fadein 1.0

    scene ep006_office_chair_woman with dissolve
    "A woman entered."
    "She had strikingly pale skin and eyes that were like a gateway to unknown depths."
    "The woman looked eerily familiar, but again my memory failed me."
    $ chrone_name = "Doctor"
    scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup") with dissolve
    chrone "Mr. Valenmann de Lonval."
    c "That's my name, I guess?"
    chrone "Right, I forgot about your...{w} condition."
    c "Bullshit."
    scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_smile") with dissolve
    chrone "Quite."
    scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup") with dissolve
    chrone "My name is Dr. Moora."
    $ chrone_name = "Dr. Moora"

    python:
        codex_chrone = add_codex_entry(
            Codex,
            __("Characters"),
            __("Dr. Moora"),
            [
                __("A doctor at the mysterious science facility where the crew was held after flying into an asteroid field as part of their escape from Barranthis.")
            ],
            "images/codex/Chrone.webp"
        )

    chrone "I'm going to ask you a few questions."
    c "Why would I answer them?"
    chrone "Because it's the right thing to do?"
    c "Bullshit."
    scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_smile") with dissolve
    chrone "That word again."
    chrone "We could also torture you."
    scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup") with dissolve
    chrone "Now. Question 1."
    chrone "Do you enjoy sex?"
    mod "You need 4 points to achieve the sex scene, however you also don't want to give too much infomation away, the choices in green are my suggestions."

    menu:
        "[gr]Evade":
            $ ep006_inverview_result += 1
            c "Who doesn't?"
        "Truth":
            $ ep006_inverview_result += 1
            c "Yes, I do."
        "Lie":
            c "My libido is incredibly low, so no."

    chrone "Have you ever experienced forbidden urges?"
    c "What the fuck is that supposed to mean?"
    scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_smile") with dissolve
    chrone "Let me rephrase."
    scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup") with dissolve
    chrone "Have you ever had sexual urges that defied the social norms of your society?"

    menu:
        "[gr]Yes":
            $ ep006_inverview_result += 1
            c "The place where I come from is pretty puritanical, so yes, I have."
        "No":
            c "No, I haven't."
            c "What kind of question is that?"

    chrone "Do you masturbate often?"
    c "Why is that important?"
    scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_serious") with dissolve
    chrone "Just answer the questions."

    menu:
        "[gr]Yes":
            $ ep006_inverview_result += 1
            c "Yes, often."
        "No":
            c "No, not a lot."

    scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup") with dissolve
    chrone "Are you sexually attracted to the redheaded girl you share a cell with?"

    menu:
        "Yes":
            $ ep006_inverview_result += 1
            $ ep006_l_attraction = True
            $ ep006_l_attraction_truth = True
            c "Yes, I am."
        "No":
            c "No, I'm not."
        "[gr]No (Lie)":
            $ ep006_l_attraction = True
            c "No, I'm not."

    chrone "Are you sexually attracted to the brunette girl known as Aven?"

    menu:
        "Yes":
            $ ep006_inverview_result += 1
            $ ep006_av_attraction = True
            $ ep006_av_attraction_truth = True
            c "Yes, I am."
        "No":
            c "No, I'm not."
        "[gr]No (Lie)":
            $ ep006_av_attraction = True
            c "No, I'm not."

    chrone "Are you sexually attracted to the older woman Nadya?"

    menu:
        "Yes":
            $ ep006_inverview_result += 1
            $ ep006_na_attraction = True
            $ ep006_na_attraction_truth = True
            c "Yes, I am."
        "No":
            c "No, I'm not."
        "[gr]No (Lie)":
            $ ep006_na_attraction = True
            c "No, I'm not."

    chrone "Are you sexually attracted to me?"

    menu:
        "[gr]Yes":
            $ ep006_inverview_result += 1
            $ ep006_chrone_attraction = True
            c "Yes, I am."
        "No":
            c "No, I'm not."

    chrone "Have the past few days heightened or lowered you sexual desires?"

    menu:
        "[gr]Heightened":
            $ ep006_inverview_result += 1
            c "They've increased."
            c "Do you know how frustrating it is to be locked up in a cell and be subjected to hardcore pornography once in a while while strapped to a chair?"
        "Lowered":
            c "Lowered."
            c "You have no idea how much that hardcore pornography you've subjected me to has desensitized me to anything erotic."
        "No change":
            c "I don't think there's been any change, to be honest."

    if ep006_chrone_attraction and ep006_inverview_result > 4:
        scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_smile") with dissolve
        chrone "If I were to offer you my body, would you take advantage?"
        c "Wait a minute, are we still talking hypotheticals here?"
        scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_serious") with dissolve
        chrone "Please answer the question."

        menu:
            "[gr]Yes":
                c "Yes, I would."
                chrone "How would you fuck me?"
                c "I'd tear that skimpy uniform you're wearing from your body and force you to bend over."
                c "Grabbing you by the hair, I'd ram my cock inside you."
                c "Then I'd hate-fuck you until you begged for me to cum."
                scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_smile") with dissolve
                c "Does that satisfy your curiosity?"
                chrone "A little."
                scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_serious") with dissolve
                chrone "It's all talk though..."
                c "Send away your guards and find out how much of it is true."
                scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_smile") with dissolve
                chrone "I'm afraid that won't happen, as it would be far to easy for you to overpower me and use me as a hostage."
                scene expression eye_blink("images/ep006/ep006_office_chair_woman_stand") with dissolve
                chrone "Follow me to the examination table."
                "Expecting a physical exam, I followed her hesitantly."
                "She nodded at the guards and they shifted positions, their backs turned to us."
                scene ep006_office_room with dissolve

                call ep006_doctor_sex from _call_ep006_doctor_sex

                scene ep006_office_pen_woman with dissolve
                chrone "Thank you for answering my questions so thoroughly."
                chrone "We’ll move the conversation back to my desk so we can wrap things up."
                "Before I fucked her brains out, I’d been eyeing a pen on the doctor’s desk."
                scene ep006_office_pen with dissolve
                "I couldn’t really make a move during the interview, but I really wanted to palm that thing somehow and now was as good a time as any."
                "We needed an edge and something small like a pen could be smuggled, sharpened and maybe used as a weapon."
                "Yeah, I didn’t have a fucking clue, but what else was I supposed to do?"
                scene ep006_office_pen_woman_dressed with dissolve
                "She let me walk in front of her, busying herself with the buttons of her dress."
                "When I reached the desk I quickly covered the pen with the palm of my hand and stuck it between the waistband of my jumpsuit."
                "The guards never strip-searched us, so I was pretty confident I could smuggle the thing into our cell."
                c "Are we done here, doc?"
                chrone "Yes, we are."
                "She called the guards who either hadn’t noticed the vigorous fucking that had gone on in the office or simply didn’t give a shit."
                scene black with fade
                "Like I hoped, they took me back to the cell without any further inspection."
            "No":
                c "No, I wouldn't."
                chrone "You harbor a grudge against me?"
                c "Of course I fucking do, you’re the reason why I’m locked up here in the first place."
                scene ep006_office_pen_alt with dissolve
                "While the doctor was droning on with her useless questions I’d eyed a pen on her desk."
                "Her attention was fully on me, so I couldn’t really make a move, but I really wanted to palm that thing somehow."
                "We needed an edge and something small like a pen could be smuggled, sharpened and maybe used as a weapon."
                "Yeah, I didn’t have a fucking clue, but what else was I supposed to do?"
                scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_smile") with dissolve
                chrone "We’re done with the interview."
                c "Finally."
                chrone "You may stand up."
                scene ep006_office_pen_alt_fall with dissolve
                "I did so and pretended to buckle forward, steadying myself on the edges of the desk."
                "I heard the guards behind me tense and draw their weapons."
                c "You really need to invest in more comfortable furniture."
                scene expression eye_blink("images/ep006/ep006_office_pen_alt_woman") with dissolve
                "As she looked me in the eyes sneeringly, I quickly covered the pen with my hand and stuck it between the waistband of my jumpsuit."
                "The guards never strip-searched us, so I was pretty confident I could smuggle the thing into our cell."
                scene black with fade
                "Like I hoped, they took me back to the cell without any further inspection."
    else:
        scene ep006_office_pen_alt with dissolve
        "While the doctor was droning on with her useless questions I’d eyed a pen on her desk."
        "Her attention was fully on me, so I couldn’t really make a move, but I really wanted to palm that thing somehow."
        "We needed an edge and something small like a pen could be smuggled, sharpened and maybe used as a weapon."
        "Yeah, I didn’t have a fucking clue, but what else was I supposed to do?"
        scene expression eye_blink("images/ep006/ep006_office_chair_woman_closeup_smile") with dissolve
        chrone "We’re done with the interview."
        c "Finally."
        chrone "You may stand up."
        scene ep006_office_pen_alt_fall with dissolve
        "I did so and pretended to buckle forward, steadying myself on the edges of the desk."
        "I heard the guards behind me tense and draw their weapons."
        c "You really need to invest in more comfortable furniture."
        scene expression eye_blink("images/ep006/ep006_office_pen_alt_woman") with dissolve
        "As she looked me in the eyes sneeringly, I quickly covered the pen with my hand and stuck it between the waistband of my jumpsuit."
        "The guards never strip-searched us, so I was pretty confident I could smuggle the thing into our cell."
        scene black with fade
        "Like I hoped, they took me back to the cell without any further inspection."

    play music "music/hiraeth.ogg" fadeout 4 fadein 1.0

    scene ep006_new_cell_return with dissolve
    "When they dumped me back into the cell all three women rushed towards me."
    l "Are you okay, [p_name]?"
    av "Did they hurt you?"
    na "Let him sit down girls and get his bearings."
    if ep006_lilly_kiss:
        scene ep006_new_cell_return_embrace_l with dissolve
        "Instead of following Nadya’s advice, I embraced Lilly and whispered something in her ear."
        c "We’re breaking out, wait for my signal."
        "Lilly looked into my eyes and nodded."
        scene ep006_new_cell_return_embrace_av with dissolve
        "I turned towards Aven and embraced her too."
        c "Take this, we’re breaking out, wait for Lilly and me to start making some noise."
    else:
        scene ep006_new_cell_return_embrace_av with dissolve
        "Instead of following Nadya’s advice, I embraced Aven and whispered something in her ear."
        c "Take this, we’re breaking out, wait for Lilly and me to start making some noise."
        "Aven took the offered pen and hid slipped it into her sleeve."
        scene ep006_new_cell_return_embrace_l with dissolve
        "I turned towards Lilly and embraced her too."
        c "We’re breaking out, wait for my signal."
    scene ep006_new_cell_return_embrace_na with dissolve
    "I embraced Nadya too for good measure, though she was a little hesitant to return the gesture."
    c "We’re breaking out, wait for us to make a move."
    "Nadya didn’t give any hint she understood me, but didn’t break my cover either."
    scene ep006_new_cell_return_idle_alt with dissolve
    "We fell into our routine and waited for the right moment."

    play music [ "music/bitter-fight.ogg", "music/in-pursuit.ogg" ] fadeout 4 fadein 1.0

    scene ep006_new_cell_return_food with dissolve
    "Eventually, the food arrived."
    scene ep006_new_cell_return_food_throw with vpunch
    "I walked towards the trays of food and picked one up and threw it against the wall."
    scene ep006_new_cell_return_food_throw_l with dissolve
    l "What the fuck are you doing?!"
    "Before she could approach me I threw another tray against the wall."
    scene ep006_new_cell_return_food_throw_l_alt with dissolve
    "Lilly shrieked and rushed towards me as I was about to throw the third tray against the wall."
    l "No!{w} That's our food, you lunatic!"
    "She pulled at my arm and made a whole lot of noise."
    scene ep006_new_cell_return_food_throw_l_alt_closeup with dissolve
    "When my eyes met hers a mischievous smile briefly crept across her face."
    "During all the commotion, Aven had positioned herself beside the door."
    scene ep006_new_cell_return_guards with dissolve
    "That's when the guards arrived to break up the fight."
    scene ep006_new_cell_return_guards_hit with vpunch
    "As they tried to grab me I swung the tray I'd picked up and struck one of the guards right across his face."
    scene ep006_new_cell_return_guards_alt with vpunch
    "Meanwhile, Aven took one of the other guards in a chokehold and held the pen I stole inches above one of the poor fellow's arteries."
    scene ep006_new_cell_return_guards_stun with vpunch
    "Lilly pulled the gun from the unfortunate guard's holster and stunned him with his own weapon."
    scene ep006_new_cell_return_guards_hit_alt with vpunch
    "That left one guard, who was about to assault Lilly when Nadya ran up behind him and thrashed him on the head with one of the dinner trays I had thrown against the wall."
    scene ep006_new_cell_return_guards_after with dissolve
    "More guards would surely arrive now, so we worked quickly and retrieved all the weapons the guards carried."
    "One of them also carried a set of keys which we took."
    "The door was still open, so we ran out in the corridor, leaving the unconscious guards behind."
    "Though there were no alarms audible, we knew it was a matter of time before more guards would arrive."
    "We had to think fast."
    scene ep006_escape_corridor with dissolve
    "The way to the doctor's office still fresh in my memory, I took the lead."
    scene ep006_escape_office with vpunch
    "With our weapons drawn we slammed open the door and moved inside."
    "The doctor nearly fell from her chair in shock and was quickly overpowered by Aven."
    scene ep006_escape_office_c with dissolve
    c "Are we being watched here?"
    chrone "I..."
    c "Answer the question."
    chrone "No, the surveillance is limited to the cells."
    c "Back when we were here and you were asking me all kinds of impertinent questions, the guards seemed to obey you."
    c "You're their superior, aren't you?"
    scene expression eye_blink("images/ep006/ep006_escape_office_c_serious") with dissolve
    chrone "I am."
    c "In that case, tell them to stand down immediately."
    chrone "I don't know if I can, the whole base is on full alert."
    c "Try anyway."
    c "And if you try anything stupid, Aven will fry your brain with that shiny gun she's holding."
    scene ep006_escape_office_c_broadcast with dissolve
    "The doctor moved to the comm console and pressed one of the speaker buttons."
    chrone "Guards in Sector Gamma, stand down at once."
    chrone "Prisoner escape drill has been completed."
    chrone "Stand down at once."
    scene expression eye_blink("images/ep006/ep006_escape_office_c_serious") with dissolve
    chrone "There, I did it."
    c "We'll have to take that risk."
    c "Now you’re going to tell us where we are."
    chrone "At a research facility."
    scene ep006_escape_office_c_hit with vpunch
    "Before I could say anything, Aven cracked the butt of the pistol against the woman’s head."
    av "Tell us something we don’t know."
    c "You heard the lady."
    c "Which research station?"
    scene expression eye_blink("images/ep006/ep006_escape_office_c_alt") with dissolve
    chrone "Höfel MDCL, built on an asteroid deep inside the Heveliun Belt."

    python:
        codex_chrone = update_codex_entry(codex_chrone, None,
            [
                __("A doctor at the Höfel MDCL science facility where the crew was held after flying into an asteroid field as part of their escape from Barranthis.")
            ]
        )

        codex_hofel = add_codex_entry(
            Codex,
            __("Planets"),
            __("Höfel MDCL"),
            [
                __("Location: Heveliun Belt"),
                __("A science facility operated by ConVitæ where the crew was held after flying into an asteroid field as part of their escape from Barranthis.")
            ]
        )

    c "Who runs this place?"
    chrone "A large company, they do research into immersive simulations."
    c "So we’re all lab rats?"
    scene expression eye_blink("images/ep006/ep006_escape_office_c_doubt") with dissolve
    chrone "I wouldn’t call it that..."
    scene ep006_escape_office_c_hit_alt with vpunch
    "That statement earned her another hit from Aven with the pistol."
    c "How did we all get here?"
    scene expression eye_blink("images/ep006/ep006_escape_office_c_alt") with dissolve
    chrone "You all arrived together on a ship."
    c "Us four?"
    chrone "No, there were others with you."
    c "So we were a crew."
    c "Where are they now?"
    scene expression eye_blink("images/ep006/ep006_escape_office_c_serious") with dissolve
    chrone "Elsewhere on this floor, I can show you where."
    c "What did you do to our memories?"
    chrone "They’re temporarily suppressed, the effect will wear off when the chemicals leave your body."
    c "Chemicals?{w} You drugged us?"
    chrone "We administer a solution via the meals we provide in order to have the most clear response to the simulations."
    c "So you take us prisoner, pry into our brains, drugs us, subject us to mind games..."
    c "Aven, what would be the effect of that blaster at point blank range on the doctor’s skull?"
    av "I think the only way to describe that would be ‘messy’."
    c "Goodbye, doctor."
    scene expression eye_blink("images/ep006/ep006_escape_office_c_alt") with vpunch
    chrone "No!{w} Wait!{w} I can get you out of here!"
    chrone "Please don’t kill me!"
    "I signalled Aven to give the doctor a chance to explain herself."
    scene expression eye_blink("images/ep006/ep006_escape_office_c_serious") with dissolve
    chrone "Your ship is still stationed in the company docks."
    chrone "I can show you where your friends are and help you reach your ship."
    c "Keep talking."
    chrone "There’s a locker room two doors down from here where you’ll find lab coats and armor."
    chrone "If you wear those the station’s personnel will not suspect you."
    c "All of the guards were aliens, doesn’t that raise any alarms?"
    chrone "Only on this floor, on the others it’s more mixed."
    chrone "Your friends are in cell block Z-X17 and storage bay G-N135."
    c "A storage bay?"
    chrone "Yes, some of you didn’t respond well enough to our research."
    c "So you put them in cold storage?"
    scene expression eye_blink("images/ep006/ep006_escape_office_c_doubt") with dissolve
    chrone "In a sense."
    chrone "They should be up and running in no time."
    c "Gee, that’s a relief, doc!"
    scene expression eye_blink("images/ep006/ep006_escape_office_c_serious") with dissolve
    chrone "You’ll need this card to override the locks on the doors."
    c "Good, anything else we should know?"
    chrone "Yes, the station has weaponry to deal with escapees, so you’ll need a clearance code in order to leave on your ship."
    c "How do we get one?"
    chrone "The docking bay office should have a console where you can generate a code."
    c "So that’s all?"
    scene expression eye_blink("images/ep006/ep006_escape_office_c_alt") with dissolve
    chrone "Yes, that’s all I know."
    c "Alright then."
    c "Aven, please stun the good doctor into unconsciousness."
    scene ep006_escape_office_c_shoot with vpunch
    "After setting the gun to stun, Aven blasted the doctor far too many times than necessary."
    "The woman fell from the chair and Nadya took her pulse and checked her eyes."
    scene ep006_escape_office_na with dissolve
    na "She’s unconscious."
    c "Good. You and Lilly stow her in that closet, while Aven and I go get the clothing from the locker room."
    scene ep006_escape_lockers with dissolve
    "We found the lockers soon enough and rummaged through them in search for clothing that would fit us."
    "After some searching we found two lab coats, a couple of shoes and two sets of armor that fit us nicely."
    "Aven and I hurried back to the doctor’s office and were nearly blasted by Lilly when we entered."
    scene expression eye_blink("images/ep006/ep006_escape_office_l") with vpunch
    l "Fuck!"
    l "Shouldn’t we have practiced a secret knock or something?"
    l "I nearly stunned you both!"
    c "Right, glad you didn’t."
    c "We brought two lab coats and shoes, better put them on."
    scene ep006_escape_office_dress with dissolve
    "Both women dressed and we headed out into the corridor towards the cell block where part of our crew was supposedly held."
    scene ep006_escape_corridor_alt with dissolve
    "We passed rows and rows of doors as we made our way through the complex."
    l "Do you think all these cells are occupied?"
    c "I sincerely hope not, there are so many doors..."
    "Block Z-X17 wasn’t too far away and we opened the door with the keycard the doctor so generously provided us with."
    scene ep006_escape_cell with dissolve
    "When we opened the door the cell’s occupants, two humans and a green-skinned woman looked at us in fear, soon mixed with bewilderedness."
    c "We’re not actual guards, we’ve come to get you out of here."
    ce "Thank heavens!"
    scene expression eye_blink("images/ep006/ep006_escape_cell_j") with vpunch
    j "But we need to find Vess, they just took her away."
    c "Where to?"
    j "To some sort of simulation room and not for the first time either."
    j "I think she said it was sixteen doors down from here."
    c "Let’s go get her then."
    c "I’m [p_name], this is Lilly, Nadya and Aven."
    c "We’ve all suffered memory loss, which will fade over time."
    c "We came here together on a ship as its crew."
    c "Wait here while Aven and me go find Vess."
    scene ep006_escape_corridor_run with dissolve
    "They did as they were told and we sprinted towards the room indicated by the green-skinned girl."
    "Two guards were in front of the door."
    c "Open that door at once."
    scene ep006_escape_corridor_guard with dissolve
    "The guard mumbled something in a language I didn’t understand, probably challenging my authority or something."
    scene ep006_escape_corridor_guard_hit with vpunch
    "That’s when he was hit square in the chest by Aven’s blaster."
    "I took care of the other guard who didn’t even have time to draw his weapon."
    c "You move the bodies, I’m getting the girl out of that chair."
    scene ep006_escape_corridor_guard_drag with dissolve
    "Aven started dragging the unconscious guards inside the simulation room after I opened the door."
    scene ep006_escape_sim with dissolve
    "The room was completely dark, save for a chair illuminated by a vivid simulation playing out in front of it."
    scene ep006_escape_sim_v with dissolve
    "A blonde girl was seated in the chair."
    "Tears were streaming down her cheeks as she was forced to look at the realistic imagery."
    scene ep006_escape_sim_v_alt with dissolve
    "A man and a woman were hunched over a crib, playing with a newborn child."
    scene ep006_escape_sim_v_alt_closeup with dissolve
    "They laughed and the baby crowed with pleasure as it tried to grab the finger dangling in front of her face."
    scene expression eye_blink("images/ep006/ep006_escape_sim_v_closeup") with dissolve
    "The happy scene was marred by the sadness radiating from the blonde girl in the chair."
    "She cried and fought against her restraints and mumbled two words over and over again."
    ve "Mom!"
    ve "Dad!"
    scene expression eye_blink("images/ep006/ep006_escape_sim_v_closeup_cry") with dissolve
    "I couldn’t find a way to turn off the simulation, so I approached the chair carefully."
    c "Vess, can you hear me?"
    ve "Who’s there?"
    ve "Grandfather?"
    c "No, I’m [p_name]."
    c "I’m going to release you from this chair and take you out of here."
    scene ep006_escape_sim_v_support with dissolve
    "She didn’t reply, but I couldn’t waste more time on talking and started undoing the straps that bound her to the chair."
    scene ep006_escape_sim_v_support_alt with dissolve
    "Still crying, I helped her stand and supported her while we walked towards the door, the simulation still playing in the background."
    c "Are you alright?"
    ve "I think so."
    c "Did you recognize those people in the simulation?"
    ve "I think they were my parents, but I can’t remember them."
    c "There’s a lot of that going on around here..."
    c "Let’s go find the others."
    scene ep006_escape_v_corridor with dissolve
    "Aven joined us and we ran back to the cell where the others waited."
    scene ep006_escape_cell_v with dissolve
    c "Our next stop is a storage bay where the rest of our crew is being held."
    c "Just follow us."
    scene ep006_escape_storage with dissolve
    "The storage units were not far from our location."
    "Thankfully the keycard worked on the entrance door as well."
    scene ep006_escape_storage_pods with dissolve
    "Storage bay G-N135 wasn’t that large and held five suspension pods, one of them empty."
    "We hit the release button on the four occupied pods and they cycled through their revivification cycles quickly."
    scene expression eye_blink("images/ep006/ep006_escape_storage_pods_z") with dissolve
    "A woman with purple skin was the first to come staggering out of the pod."
    zi "Am I glad to see you all."
    l "You know who we are?"
    zi "Errr....{w} You don’t?"
    c "We’ve been given drugs that repress our memories."
    zi "Right, that must be confusing."
    zi "Until you can remember me, I’m Ziv, one of your crew mates."
    zi "Those other pods likely hold Raene, Thyia and Thim."
    scene ep006_escape_storage_pods_th with dissolve
    "Ziv was interrupted by a black woman vomiting bile on the floor as she crawled from her storage pod."
    scene expression eye_blink("images/ep006/ep006_escape_storage_pods_th_closeup") with dissolve
    th "I fucking hate induced cryo sleep."
    th "Oh...{w} Hi all."
    zi "Are you alright, Thyia?"
    th "I feel fine, other than the nausea."
    th "Why are you staring at me all glassy-eyed?"
    zi "Most of the crew have lost their memory."
    th "Fuck.{w} Temporarily I hope?"
    zi "It seems so."
    scene ep006_escape_storage_pods_thim with dissolve
    "The two remaining persons woke up and started heaving while steadying themselves against one of the sides of the pod."
    t "Wh-where the fuck am I?"
    c "We’re on a research station."
    c "You four were kept on ice, while we were used as lab animals."
    scene expression eye_blink("images/ep006/ep006_escape_storage_pods_ra") with dissolve
    ra "Lab animals?"
    ra "What did they do to you?"
    scene expression eye_blink("images/ep006/ep006_escape_storage_pods_av") with dissolve
    av "They put us through various simulations."
    av "Probably to measure our responses to them."
    scene expression eye_blink("images/ep006/ep006_escape_storage_pods_th_closeup") with dissolve
    th "They just plucked us out of space and did clandestine experiments on us?"
    c "Well, we don’t have time to appreciate what assholes these people are."
    c "Our ship is on one of the higher levels of this facility."
    c "As we appear to have our crew all together, I think it’s time to get the hell out of here."
    scene ep006_escape_corridor_group with dissolve
    "The order to stand down the doctor gave earlier must have worked, because we didn’t encounter any guards on alert as we ran back towards the locker room."

    play music [ "music/emergent.ogg", "music/hiding-your-reality.ogg" ] fadein 4 fadeout 1.0

    scene ep006_escape_lockers_z_thim with dissolve
    "Thim and Ziv found two suits of armor that fit them."
    scene ep006_escape_lockers_v_th with dissolve
    "The others were all trying on lab coats when I noticed Raene was missing."
    scene ep006_escape_lockers_ra with dissolve
    "While the others busied themselves, I walked into the showers and found Raene there looking distraught."
    menu:
        "Comfort her [RaenePath]":
            $ ep006_ra_comfort = True
            scene expression eye_blink("images/ep006/ep006_escape_lockers_ra_closeup") with dissolve
            c "What's the matter?"
            ra "Nothing, I'll be fine in a moment."
            c "You can tell me."

            if (ep004_ra_confront_angry + ep004_ra_doubt + ep004_ra_angry + ep005_ra_intimidate) < 1 or ( (ep004_ra_confront_angry + ep004_ra_doubt + ep004_ra_angry + ep005_ra_intimidate) < 2 and ep005_ra_accept):
                ra "It's silly, really."
                c "Try me."
                ra "I...{w} Just look at me, [p_name_short]!"
                "That's when I noticed she was wearing the same clothes as I was."

                menu:
                    "Berate her":
                        $ ep006_ra_berate = True
                        c "So they assumed you were a boy?"
                        c "In case you haven't noticed, we're trying to get out of here..."
                        c "So stop making a fuss and get a grip."
                        scene expression eye_blink("images/ep006/ep006_escape_lockers_ra_closeup_sad") with dissolve
                        ra "I know."
                        ra "I said it was silly."
                        ra "I'll be fine in a moment."
                        ra "It won't happen again."
                        c "Good, I'll see you in a minute."
                    "Be understanding [RaenePath]":
                        c "Oh...{w} fuck...{w} they assumed you were..."
                        scene expression eye_blink("images/ep006/ep006_escape_lockers_ra_closeup_sad") with dissolve
                        ra "Yes, they did."
                        ra "And I hate that it affects me so much, especially considering our circumstances."
                        ra "But it was just too much all at once."
                        ra "As as I said, I'll be fine in a moment."
                        c "Right, take whatever time you need."
                        c "But promise me we'll talk further once we're safe?"
                        scene expression eye_blink("images/ep006/ep006_escape_lockers_ra_closeup_smile") with dissolve
                        ra "I promise."
                        ra "Thank you, [p_name_short]."
                        c "Don't worry about it."
            else:
                scene expression eye_blink("images/ep006/ep006_escape_lockers_ra_closeup_sad") with dissolve
                ra "Just leave me here for a minute, I'll be fine."
                c "Suit yourself."
        "Ignore her":
            $ ep006_ra_ignore = True
            "I didn't want to disturb her private moment and left to join the others before she noticed me."

    scene ep006_escape_lockers_group with dissolve
    "Raene joined us and picked a suit of armor and soon we had a battalion of doctors and a couple of guards."
    c "I think we’re ready to board that elevator."
    scene ep006_escape_elevator with dissolve
    "Luckily the elevator wasn’t guarded and was large enough to carry us all."
    "A helpful schematic told us which floor we needed to punch in."
    "The facility turned out to be very large and we were on one of the lower floors."
    scene ep006_escape_elevator_ride with dissolve
    "We were almost overwhelmed by vertigo, because the elevator moved very fast towards its destination."
    with vpunch
    "Just before the doors slid open, a memory from my youth welled up all of a sudden."
    "And then it began crashing in all at once."
    with vpunch
    "The events on Lanan, deserting, life at the Academy, life on Tuolovi, stealing the larvae on Sagueliath."
    "The flood of memories was an assault on all the senses and I retched."
    scene ep006_escape_elevator_ride_l with dissolve
    "Bleary-eyed I looked up and saw Lilly bent over in much the same state as I was."

    if ep006_lilly_kiss:
        if game.is_special:
            "Then the realization hit me, the girl I’d loved for the past few days was my own sister."
        else:
            "Then the realization hit me, the girl I’d loved for the past few days was my childhood friend."
        "She wouldn’t meet my eyes, but I’d gathered she went through much the same horrifying process as I was."
        if game.is_special:
            "How wrong we’d been about each other, mistaking our sibling bond for true love."
        else:
            "How wrong we’d been about each other, mistaking our bond of friendship for true love."
    else:
        if game.is_special:
            if ep006_lilly_friends:
                "Then the realization hit me, how wrong we’d been about each other, being brother and sister instead of just friends."
            else:
                "Then the realization hit me, how right we’d been about each other, being brother and sister."
        else:
            if ep006_lilly_family:
                "Then the realization hit me, how wrong we’d been about each other, being friends instead of brother and sister."
            else:
                "Then the realization hit me, how right we’d been about each other, being childhood friends."
    if ep006_aven_compassion:
        scene ep006_escape_elevator_ride_av with dissolve
        "Aven had to steady herself against the wall and looked at me intently through tear-filled eyes."
        "Was she ashamed of herself, of the feelings she confessed to me when we were just strangers in a cell together?"
    "The sound of a station broadcast disturbed my thoughts and put me back in the here and now."
    "When I felt my legs could carry me again I motioned the others to follow me."
    scene ep006_escape_plaza with dissolve
    "We walked unsteadily through a long corridor to find a large plaza."
    "That’s when another realization hit me square in the face."
    "A huge wall dominated the plaza, covered in huge lettering announcing the name of company in charge of this research station."
    scene ep006_escape_plaza_alt with dissolve
    "The doctor had already mentioned the name ConVitæ before, but I was too drugged to make any kind of mental connection."
    "With the haze of the drugs cleared, I remembered the name ConVitæ well enough."
    if ep003_verdant_con_vitae_accepted:
        "I very much regretted signing that ConVitæ paperwork back on Verdant Station."
        "In retrospect, everything just screamed ‘evil corporation’ and they’d sure honored that reputation."
    elif ep003_verdant_con_vitae_declined:
        "I was glad I didn’t sign any of the paperwork on Verdant Station."
        "I had a feeling those fuckers weren’t to be trusted."
        "Everything just screamed ‘evil corporation’ and they’d sure honored that reputation."
    else:
        "I already knew back on Verdant Station that those fuckers weren’t to be trusted."
        "Everything just screamed ‘evil corporation’ and they’d sure honored that reputation."
    "This was probably one of the facilities where they tested out new simulated experiences and did fuck knows what else."

    python:
        if ep003_verdant_con_vitae_accepted:
            codex_convitae = add_codex_entry(
                Codex,
                __("Organizations"),
                __("ConVitæ"),
                [
                    __("A research company primarily interested in creating immersive sims. The company had a small office on Verdant Station where [p_name] was part of a voluntary experiment involving simulation research."),
                    __("The company also maintained the Höfel MDCL research base where the crew of the Iron Bastard was held against their will and experimented upon."),
                ]
            )
        elif ep003_verdant_con_vitae_declined:
            codex_convitae = add_codex_entry(
                Codex,
                __("Organizations"),
                __("ConVitæ"),
                [
                    __("A research company primarily interested in creating immersive sims. The company had a small office on Verdant Station where [p_name] was declined to be part of a voluntary experiment involving simulation research."),
                    __("The company also maintained the Höfel MDCL research base where the crew of the Iron Bastard was held against their will and experimented upon."),
                ]
            )
        else:
            codex_convitae = add_codex_entry(
                Codex,
                __("Organizations"),
                __("ConVitæ"),
                [
                    __("A research company primarily interested in creating immersive sims. The company had a small office on Verdant Station."),
                    __("The company also maintained the Höfel MDCL research base where the crew of the Iron Bastard was held against their will and experimented upon."),
                ]
            )
    scene ep006_escape_plaza_group with dissolve
    c "We must keep moving."
    c "There's another elevator on this floor that will take us to the docks."
    c "We might encounter more people on this level, so try to act natural."
    scene ep006_escape_plaza_walk with dissolve
    "We entered the plaza and tried to blend in."
    "Jade, Céline and Nadya feigned an animated conversation about some made-up scientific topic, while the others looked determined and cut a confident path across the square."
    scene ep006_escape_plaza_walk_alt with dissolve
    "Nobody paid any attention to us as we neared the elevator."
    "At least, that's what we thought."
    $ man_name = "Guard"
    $ man_portrait = "side_man"
    scene expression eye_blink("images/ep006/ep006_escape_plaza_guard") with vpunch
    man "You there."
    man "We need you on Sublevel 11-XXXVIII."

    menu:
        "Bluff":
            $ ep006_guard_bluff = True
            c "We have orders to escort these scientists to the docks, on the double."
            scene expression eye_blink("images/ep006/ep006_escape_plaza_guard_doubt") with dissolve
            man "The docks?"
            man "Why would they need to go there?"
            c "They're assigned to some special project, I think."
            man "First I've heard about it."
            man "What kind of project?"
            c "Beats me, they never tell you anything do they?"
            scene expression eye_blink("images/ep006/ep006_escape_plaza_guard") with vpunch
            man "Right, bunch of stuck-up cunts."
            c "Exactly."
            man "On your way then."
        "Intimidate":
            c "I'm tasked with escorting these scientists to the docking bay."
            man "And I'm ordering you to come with me."
            c "No."
            man "Who's your superior?"
            c "None of your fucking business."
            scene expression eye_blink("images/ep006/ep006_escape_plaza_guard_angry") with dissolve
            man "I ought to report you!"
            c "You really don't."
            c "Now fuck off and let me do my job."
            "The guard stared long and hard at me, but turned on his heel eventually."
            scene expression eye_blink("images/ep006/ep006_escape_plaza_av") with dissolve
            av "Fuck, I really thought he was going to punch you in the face or something."
            c "That would have been rude..."

    scene ep006_escape_plaza_guard_walk with dissolve
    c "Let's go inside that elevator before more of his friends start to get ideas and order us around."
    "We entered the large elevator and the doors started to close agonizingly slow."
    scene ep006_escape_docks with dissolve
    "The elevator ride itself was very fast and we were greeted by the smell of engine fuel, oil and metal as soon as the doors opened."
    "The Bastard was docked here together with several other ships."
    scene ep006_escape_docks_bastard with dissolve
    "Our vessel didn't look that much worse for wear, at least not more than it usually did."
    c "We need that identification code, it's on a computer here somewhere."
    scene expression eye_blink("images/ep006/ep006_escape_docks_j") with dissolve
    j "I guess I might be able to help with that."
    j "Unless there are a lot of guards..."
    scene expression eye_blink("images/ep006/ep006_escape_docks_av") with dissolve
    av "We'll handle those."
    c "Right."
    c "Jade, Aven and me will try and find that docking computer."
    c "Everyone else, take up position near the Bastard and try to gain access."
    scene ep006_escape_docks_command with dissolve
    "A central command post looked out over all the docking bays and that would be our best bet to gain access to the computer system."
    "Trying to look confident we marched towards the entrance door and barged in."
    scene ep006_escape_docks_interior with dissolve
    "I was ready to bark orders to the any surprised guards, but there weren't any, the control post was completely empty."
    scene expression eye_blink("images/ep006/ep006_escape_docks_interior_av") with dissolve
    av "Shouldn't someone be monitoring stuff?"
    c "Maybe they're on a lunch break?"
    av "Yeah...{w} I don't like this."
    "We pulled our guns and cased the area."
    scene expression eye_blink("images/ep006/ep006_escape_docks_interior_j") with dissolve
    j "There's a computer console over there."
    c "You might as well take advantage of the situation and start working."
    j "Right away."
    scene expression eye_blink("images/ep006/ep006_escape_docks_interior_av") with dissolve
    av "Why isn't anyone here?"
    "Right at that moment I heard a distinct yelp coming from a backroom."
    c "Over here!"
    scene expression eye_blink("images/ep006/ep006_escape_docks_interior_door") with dissolve
    "We carefully approached the door leading to a maintenance room."
    "There were sounds coming from behind it."
    av "Either someone is in pain or they're having a good time."
    "I opened the door slightly and saw two guards hunched over the screen of a handheld device."
    scene ep006_escape_docks_guards with dissolve
    man "Fuck!{w} Is that thing really going in there?!"
    man "No, she didn't!"
    man "All the way?{w} Damn!"
    menu:
        "Close the door":
            $ ep006_guard_shoot = True
            scene expression eye_blink("images/ep006/ep006_escape_docks_interior_door") with dissolve
            "I closed the door softly and left the guards to whatever nasty pornography they were admiring."
            c "Let's leave them to it and hurry the fuck up."
            scene expression eye_blink("images/ep006/ep006_escape_docks_console_j") with dissolve
            "Jade was still hovered over the console when we got back."
            j "Just a couple of minutes."
            c "I hope the boys will be occupied long enough back there."
            j "Boys?"
            c "Never mind, just focus on getting us those access codes."
            scene ep006_escape_docks_console with dissolve
            "Jade's fingers danced frantically over the keyboard and she sighed in frustration multiple times."
            "The system evidently resisted her attempts to gain entry and I started to fear we'd get caught."
            scene expression eye_blink("images/ep006/ep006_escape_docks_console_j") with dissolve
            j "Nearly got it!"
            "We heard the closet door slide open and the two guards emerged."
            c "Fuck."
            scene ep006_escape_docks_guard with dissolve
            man "What are you doing here?!"

            menu:
                "Bluff":
                    c "We're to relieve you."
                    scene expression eye_blink("images/ep006/ep006_escape_docks_guard_doubt") with dissolve
                    man "Nonsense, that's only supposed to happen in an hour."
                    c "Plans have changed, command tried to contact you, but got no response."
                    c "You probably had a good reason for leaving your post, didn't you?"
                    man "I'm going to call command and sort this mess out."
                    c "Fuck."
                    scene ep006_escape_docks_guard_shot with vpunch
                    "I shot him in the face before the guard could bring his communicator to his mouth."
                    scene ep006_escape_docks_guard_shot_alt with vpunch
                    "Aven took care of the other guard who dropped with a shocked look on his face."
                    "Just as the men both hit the floor Jade exclaimed her success."
                "Shoot them":
                    scene ep006_escape_docks_guard_shot with vpunch
                    "Before the guard could say anything else I shot him in the face."
                    scene ep006_escape_docks_guard_shot_alt with vpunch
                    "The other guard attempted to bring his communicator to his mouth, but was caught by a blast from Aven's gun."
                    "Just as the men both hit the floor Jade exclaimed her success."
            scene expression eye_blink("images/ep006/ep006_escape_docks_console_j_happy") with dissolve
            j "I've got it!"
            j "I've got the codes and we're cleared for launch."
            scene ep006_escape_docks_console_guards with dissolve
            "Only then she seemed to notice the shooting that had just happened and her face contorted in disgust."
            av "Fuck, what a mess."
            c "Let's leave here quickly, hopefully the others are already on the Bastard."
        "Confront the guards [JadePath]":
            $ ep006_guard_confront = True
            "Much to Aven's shock I kicked the door in."
            scene ep006_escape_docks_guards_shock with vpunch
            c "What the fuck do you think you're doing here?"
            "The guards were startled beyond belief and stared at us with mouths agape."
            "One of them still held the tablet showing a woman stuffing her butthole with an incredibly large dildo."
            scene expression eye_blink("images/ep006/ep006_escape_docks_guards_shock_closeup") with dissolve
            man "Sir...{w} we..."
            c "You both abandoned your posts to lock yourself up in a closet and look at porn?!"
            c "I should shoot you on sight."
            man "Please...{w} sir..."
            c "Shut the fuck up."
            c "Report to your commander immediately and make sure to tell him everything."
            c "Make sure to tell him everything, because I intend to verify your story once my guard shift here is done."
            scene ep006_escape_docks_guards_shock with dissolve
            man "But sir, we weren't supposed to be relieved until the next hour."
            c "Do I look like I care?"
            c "Get the fuck out of here at once!"
            scene ep006_escape_docks_console_guards_leave with dissolve
            "The guards were too flustered to really think about the whole situation and hurried out in shame."
            "They didn't even notice Jade working on the console on their way out."
            scene expression eye_blink("images/ep006/ep006_escape_docks_console_guards_av") with dissolve
            av "Damn, you really made them shit their britches, [p_name_short]."
            scene expression eye_blink("images/ep006/ep006_escape_docks_console_j") with dissolve
            j "What was that about?"
            c "Just some guys slacking off at work."
            c "I put them in their place."
            j "You sure did."
            j "Just a couple of minutes and we should have those access codes."
            scene ep006_escape_docks_console with dissolve
            "Jade's fingers danced frantically over the keyboard and she sighed in frustration multiple times."
            "The system evidently resisted her attempts to gain entry and I started to fear we'd get caught."
            j "Nearly got it!"
            "I just hoped the guards we dismissed didn't get any second thoughts and mess things up for us."
            "Luckily, nobody disturbed us."
            scene expression eye_blink("images/ep006/ep006_escape_docks_console_j_happy") with dissolve
            j "I've got it!"
            j "I've got the codes and we're cleared for launch."
            c "Great work!"
            c "Let's leave here quickly, hopefully the others are already on the Bastard."

    scene ep006_escape_docks_bastard_approach with dissolve
    "We hurried down towards the Iron Bastard."
    "Nobody opposed us and the few maintenance droids stalking the premises didn't even register us."
    "There was nobody in the vicinity of the Bastard and the entrance hatch was open."
    c "Everyone's already inside, let's get the fuck out of here."
    "The hatch closed immediately after we climbed aboard the ship."
    "We rushed towards the bridge to find Céline and the others already strapped in."
    scene ep006_escape_bridge with dissolve
    ce "Ready for take-off."
    "The Iron Bastard hummed as Céline started the engines and the docking bay doors opened."
    "No alarms interrupted us and we sped outside the docking bay in seconds."
    scene ep006_escape_bridge_alt with dissolve
    "The ship prompted us for an identification code which Jade recited to Céline."
    "After punching in the code we had to wait for a number of agonizing seconds until the screen turned green in approval."
    "Full thrust, we flew back into the asteroid field and left the station behind."
    c "Set a course for Almagest."
    scene expression eye_blink("images/ep006/ep006_escape_bridge_ce_doubt") with dissolve
    ce "Uh, [p_name_short]...{w} about that..."
    c "What's the matter?"
    ce "I had a look at the ship's records to find the date we were captured."
    c "And?"
    scene expression eye_blink("images/ep006/ep006_escape_bridge_ce") with dissolve
    ce "That was almost six months ago."
    with vpunch
    c "Six months?"
    c "That can't be true."
    ce "I double-checked it."
    scene ep006_escape_bridge_chair with dissolve
    "The thought of losing almost half a year sent me reeling and I had to support myself by grabbing hold of a chair."
    c "We'll find a way to deal with this."
    c "Plot a course to Almagest, we'll get that information one way or another."
    scene expression eye_blink("images/ep006/ep006_escape_bridge_kit") with dissolve
    ki "We could turn back Barranthis, maybe ask that Vitriv for help again?"
    scene expression eye_blink("images/ep006/ep006_escape_bridge_th") with dissolve
    th "I'm not sure we're going to find him that easily."
    th "Also, you can bet on Doarn giving us a warm welcome, we've made a powerful enemy there."
    c "I don't want to waste more time, we'll think of something once we reach Almagest."
    scene ep006_escape_asteroids with dissolve
    "Once Céline fed the Bastard the coordinates to the Psi1-Draconis system and we were in for a long journey through several jumpgates."
    "Now was as good a time as any to settle a few things with some of my crew mates."

    call ep006_conversations from _call_ep006_conversations

    jump episode007
    return

label ep006_sim_01:
    if _in_replay:
        $ yve_name = "Woman"
        $ woman_portrait = "side_yve"

    $ woman2_name = "Woman"
    $ woman2_portrait = "side_calista"

    scene ep006_sim_chair with dissolve
    "Suddenly I was overwhelmed by a familiar nausea."
    scene ep006_sim with pixellate
    "The darkness in front of me was pierced by several spotlights and I saw two figures, unmistakably female."
    scene ep006_sim_closeup with dissolve
    "One of the women was completely naked and kneeling, her shapely ass turned towards me."
    scene ep006_sim_closeup_boots with dissolve
    "The other woman was scantly clad and walking circles around the naked woman, carrying a whip."
    scene ep006_sim_closeup_face with dissolve
    "When her face was illuminated by one of the spotlights a wave of emotion coursed through me."
    "I felt I should recognize the woman because of the ferociousness of my feelings, a burning hatred, but my mind drew a blank."
    scene ep006_sim_closeup_whip with dissolve
    "The woman let the whip touch the skin of the other woman's back."
    "I heard her whimper."
    "The other woman spoke, she had a commanding voice that brooked no contradiction."
    scene expression eye_blink("images/ep006/ep006_sim_closeup_ca") with dissolve
    woman2 "Do you deny you're a slut?"
    "The woman on the floor replied in a whisper as she shirked away from the tip of the whip."
    "Her long blonde hair fell as a waterfall on the floor."
    woman2 "I can't hear you, slut."
    woman2 "Speak up!"
    $ yve_name = "Woman"
    scene expression eye_blink("images/ep006/ep006_sim_closeup_yve") with dissolve
    yve "I'm not a slut!"
    "With a flick of her wrist the woman attacked with her whip."
    "I saw her buttocks clench as the coarse leather lashed viciously against the helpless slave."
    scene expression eye_blink("images/ep006/ep006_sim_closeup_ca") with dissolve
    woman2 "You will address me as Mistress!"
    $ yve_name = "Slave"
    $ woman2_name = "Mistress"
    scene expression eye_blink("images/ep006/ep006_sim_closeup_yve") with dissolve
    yve "I'm not a slut, Mistress."
    scene expression eye_blink("images/ep006/ep006_sim_closeup_ca_smile") with dissolve
    woman2 "But you are."
    woman2 "You've slept with so many men."
    woman2 "Or should I say boys?"
    woman2 "You like those eighteen and nineteen-year olds, don't you, because they still have the stamina to fuck you all night?"
    woman2 "Admit it!"
    "The Mistress lashed her slave several times before she could answer."
    woman2 "Stand up, slut."
    "The blonde slave just whimpered which earned her two slaps on the bare soles of her feet."
    scene ep006_sim_stand with dissolve
    "She yelped and struggled to get up."
    "Her long hair covered most of her well-sculpted back and stopped just above her ass."
    scene expression eye_blink("images/ep006/ep006_sim_stand_alt") with dissolve
    woman2 "Face me, whore."
    "The slave finally turned around, the harsh light hitting her face."
    scene ep006_sim_stand_front with vpunch
    "I was struck with another torrent of emotions, a little more ambivalent than what I felt for the Mistress."
    "A weird kind of affection and familiarity, mixed with the same hatred I felt for the other woman."
    "Strangely, both women also aroused me."
    "My erection was straining against the coverall I was wearing."
    scene ep006_sim_stand_front_alt with dissolve
    woman2 "You love to be fucked by teenage cocks, don't you?"
    woman2 "Say it."
    scene ep006_sim_stand_front_alt_fear with dissolve
    yve "No, mistress."
    show ep006_sim_stand_buttocks with dissolve
    pause 8.9
    show ep006_sim_stand_buttocks_whipped with dissolve
    "The Mistress savagely whipped her slave's buttocks and I saw the blonde woman clench her teeth to deal with the pain."
    woman2 "You love to get fucked."
    woman2 "Say it."
    scene ep006_sim_stand_front_nipples with dissolve
    "The woman now faced her captive and she stroked the woman's hard nipples with the tip of the whip."
    woman2 "Say it."
    scene expression eye_blink("images/ep006/ep006_sim_stand_front_closeup_yve") with dissolve
    yve "I love to get fucked."
    "A vicious slap and the blonde woman's large breasts were marked with the whip's red mark."
    woman2 "Louder!"
    yve "I love to get fucked!"
    woman2 "Because you're a slut."
    yve "Because I'm a slut!"
    woman2 "Good girl."
    scene ep006_sim_stand_whip_legs with dissolve
    "The whip was now between the trembling slave's legs and the Mistress slowly stroked her inner thighs."
    "She swished the instrument upwards and lightly touched the slave's cunt."
    woman2 "Again."
    scene expression eye_blink("images/ep006/ep006_sim_stand_front_closeup_yve_alt") with dissolve
    yve "I love to get fucked, because I'm a slut!"
    woman2 "Good, very good."
    woman2 "You're learning to be a good pet."
    woman2 "But you have a lot to atone for, so on your knees again."
    $ renpy.end_replay()
    return

label ep006_sim_02:
    if _in_replay:
        $ yve_name = "Woman"
        $ woman_portrait = "side_yve"
        $ woman2_name = "Mistress"
        $ woman2_portrait = "side_calista"

    scene ep006_sim_standing with pixellate
    woman2 "Are you ready to be punished again, slut?"
    yve "No, mistress, I'm not."
    woman2 "Sure you are."
    woman2 "You've trained your holes so well, letting all those boys use you like a common whore."
    scene ep006_sim_standing_alt with dissolve
    yve "Yes, mistress."
    woman2 "Tell me, did you like all that seed running from your gash onto your thighs?"
    woman2 "Did you relish swallowing the cum from all those hard cocks you took so eagerly in your mouth?"
    scene ep006_sim_standing_alt_closeup with dissolve
    yve "I did, mistress."
    woman2 "Of course you did."
    woman2 "There won't be any cock for you now though."
    scene ep006_sim_dildo with dissolve
    woman2 "Just this."
    yve "Mistress, please, it's too big!"
    woman2 "Nonsense."
    woman2 "Kneel."
    woman2 "Ass in the air."
    scene ep006_sim_kneel_ass with dissolve
    "The blonde slave obliged, giving me a perfect view of her buttocks."
    scene ep006_sim_kneel_ass_slap with vpunch
    "The Mistress slapped them lightly with the flat of her hand."
    woman2 "Such a sturdy ass."
    woman2 "Did you like it when you got fucked from behind?"
    yve "No, mistress, I didn't."
    woman2 "Don't lie, you loved a big fat cock inside your asshole, didn't you?"
    scene ep006_sim_kneel_ass_slap_alt with vpunch
    "She slapped the woman's ass hard leaving a red impression of her hand."
    scene ep006_sim_kneel_hand with dissolve
    "The girl yelped in pain as the Mistress roughly shoved her hand across her cunt."
    woman2 "You can try all you want, but your body is not going to lie."
    scene ep006_sim_dildo_ass with dissolve
    "The slave whimpered as she eyed the large toy the Mistress held in her fist."
    "The domineering woman spat between the kneeling slave's butt cheeks and spread the saliva with her finger around the asshole."
    "Tenderly, she stroked the blonde woman's anus, making it open very slightly."
    scene ep006_sim_dildo_ass_finger with dissolve
    woman2 "See, you're opening up to me already."
    yve "No, I'm not, Mistress, mercy! Please!"
    "My hard cock pressed violently against the taut fabric of my coverall."
    "If my arms weren't restrained to the chair I would've masturbated at the sight of those two depraved women."
    "The only thing I could do now was look."
    scene ep006_sim_dildo_ass_push with dissolve
    "The Mistress had pressed the dildo against the folds of the slave's butthole."
    "The blonde woman had balled her hands to fists and waited for the toy to enter her rectum."
    scene ep006_sim_dildo_ass_insert with dissolve
    "Little by little the Mistress slid the toy inside the other woman's asshole."
    woman2 "Look at that."
    woman2 "Look at that big thing sliding so easily inside your hole."
    woman2 "Too big you said!"
    woman2 "A lying whore, that's what you are."
    show ep006_sim_dildo_ass_insert_full with dissolve
    "The toy was now fully inside of her and the slave gritted her teeth as the cold dildo probed her asshole."
    woman2 "Do you like that thing inside your ass, slut?"
    yve "No, mistress."
    woman2 "Don't lie."
    scene ep006_sim_dildo_ass_closeup with dissolve
    yve "It's so big, mistress."
    woman2 "Answer me!"
    woman2 "Do you like that thing stuffed inside of you?"
    scene ep006_sim_dildo_ass_closeup_smile with dissolve
    yve "Yes, I do, mistress."
    woman2 "Do you want to get fucked in your ass?"
    show ep006_sim_dildo_ass_insert_full_still with dissolve
    yve "Yes, mistress."
    show ep006_sim_dildo_ass_insert_full_alt with dissolve
    "The Mistress grinned and she began to move the dildo up and down inside the slave's anal cavity."
    "Sighs and moans could be heard from the blonde woman as her asshole was fucked by the ribbed toy."
    scene ep006_sim_dildo_ass_fuck with dissolve
    woman2 "You want to cum, don't you?"
    yve "Yes!"
    woman2 "Yes, what?!"
    scene ep006_sim_dildo_ass_fuck_shock with vpunch
    "The Mistress suddenly rammed the full length of the dildo inside the other woman's asshole."
    yve "Ahh!{w} Yes, mistress."
    "Satisfied by the answer, the Mistress continued fucking the slave's ass with the dildo."
    scene ep006_sim_dildo_ass_fuck_alt with dissolve
    woman2 "Tell me you love getting fucked like this."
    yve "I love it, mistress!"
    yve "I love it!"
    woman2 "Good girl."
    woman2 "You're allowed to cum."
    scene ep006_sim_dildo_ass_orgasm with dissolve
    "Using her fingers, it took just a few flicks of the blonde woman's clit and she convulsed violently."
    "The strength of her orgasm nearly made the dominant woman lose grip on the dildo, but she managed to keep fucking the slave's ass while she climaxed wildly."
    scene ep006_sim_dildo_ass_collapse with dissolve
    "Completely spent, the blonde woman collapsed to the floor, the dildo still sticking out of her ass."
    $ renpy.end_replay()
    scene ep006_room_light with pixellate
    "That's when the lights blinked out and moments later I was alone in my chair again, my boner still raging between my legs."
    return

label ep006_sim_03:
    if _in_replay:
        $ yve_name = "Woman"
        $ woman_portrait = "side_yve"
        $ woman2_name = "Mistress"
        $ woman2_portrait = "side_calista"

    scene ep006_sim_spread with pixellate
    "The slave lay helpless on the floor, her arms and legs spread wide, while her captor circled her."
    "The whip flashed multiple times and left marks on the blonde woman's breasts and her inner thighs."
    woman2 "You're going to satisfy me with that whore mouth of yours again."
    scene ep006_sim_spread_closeup with dissolve
    yve "Yes, mistress."
    scene ep006_sim_spread_face with dissolve
    "Without giving her slave time to adjust, the Mistress squatted on the woman's face."
    woman2 "Lick!"
    woman2 "That's right!"
    woman2 "Faster!"
    scene ep006_sim_spread_face_lick with dissolve
    "I heard the blonde woman slobber and suck eagerly at her mistress' cunt."
    scene ep006_sim_spread_face_lick_breasts with dissolve
    "The squatting woman rocked back and forth while amusing herself by playing with the breasts of her prisoner."
    "I saw the blonde woman's cunt starting to glisten in the spotlight, as she became more and more aroused."
    woman2 "Deeper!"
    woman2 "Make me cum with that slutty mouth of yours."
    scene ep006_sim_spread_face_lick_alt with dissolve
    "The Mistress pressed her wet gash even more forceful on her slave's mouth."
    scene ep006_sim_spread_face_lick_breasts_alt with dissolve
    "She kneaded the blonde woman's large breasts, leaving aggressive marks in the luscious flesh."
    "The wet sounds of the woman's tongue lapping at the Mistress' cunt were muffled now, but the slave's fervor didn't seem diminished."
    woman2 "Yes!{w} Yes!{w} Oh yes!"
    scene ep006_sim_spread_face_lick_squirt with vpunch
    "The Mistress began to shudder and a torrent of ejaculate squirted out of her mound, drenching the slave's body."
    scene ep006_sim_spread_face_lick_squirt_alt with dissolve
    "Her face was flooded with pussy juice and she drank eagerly while her mistress moaned loudly."
    "Only when the blonde slave had cleaned the other woman's dripping slit was she allowed to sit up and breathe freely."
    scene ep006_sim_post with dissolve
    woman2 "Good work, little whore."
    $ renpy.end_replay()
    scene ep006_room_light with pixellate
    "The women suddenly disappeared and I was alone in the chair again."
    return

label ep006_aven_shower:
    if _in_replay:
        $ av_name = "Aven"

    scene ep006_shower_av with dissolve
    "Aven was resting against one of the walls of the shower, her legs spread."
    "She had her eyes closed and rocked back and forth while her fingers massaged her slit."
    "Her moans were louder now and she whispered softly."
    scene ep006_shower_av_breasts with dissolve
    "She massaged one of her firm breasts, twisting her hard nipples between thumb and finger."
    scene ep006_shower_av_closeup with dissolve
    av "Mmmm, oh yes, touch me there...{w} oh!"
    "It almost seemed as if she was imagining someone else touching her intimately."
    scene ep006_shower_av_finger with dissolve
    "Two fingers were now lingering in the vicinity of her clitoris."
    scene ep006_shower_av_finger_alt with dissolve
    "When she applied pressure, Aven gasped, her eyes still closed and her hand still massaging her breast."
    av "Right there...{w} mmmmm!"
    show ep006_shower_av_fingering with dissolve
    "The girl was now bringing herself ever closer to her inevitable climax."
    show ep006_shower_av_fingering_closeup with dissolve
    "Her breathing became labored as the juices from her pussy mixed with the water of the shower still pearling her skin."
    av "Yes! Touch me right there!"
    av "Right there!"
    scene ep006_shower_av_finger_closeup with vpunch
    av "Oh [p_name]!"
    scene ep006_shower_av_finger_wide with dissolve
    "The mention of my name sent an electric shock through my body."
    "All the while she'd been thinking of me..."
    "She'd been acting strange ever since Lilly and I entered the cell, but was that enough to explain this behavior?"
    scene ep006_shower_av_finger_orgasm with dissolve
    "Aven let out a very restrained moan as her body shuddered against the wall."
    "She climaxed with my name on her lips."
    scene ep006_shower_av_finger_orgasm_alt with dissolve
    "As she sat there, her hand still between her legs, I decided it was safer to slip back into my bed."
    $ renpy.end_replay()
    return

label ep006_doctor_sex:
    if _in_replay:
        $ ep006_doctor_anal = False
        $ chrone_name = "Dr. Moora"

    "When I looked at the doctor, she was unbuttoning her dress."
    scene ep006_doctor_naked:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "My cock already stirred when the dress fell to her ankles."
    chrone "Time to show me if you can deliver on those promises."
    scene ep006_doctor_naked_alt with dissolve
    "Eyeing her naked body, I quickly undressed myself."
    "I could see a glint of approval when I revealed my hardened cock to her."
    "With two steps I crossed the distance between her and me."
    scene ep006_doctor_doggy with dissolve
    "I seized her arms and spun her around, forcing her to lean on the examination chair."
    scene ep006_doctor_doggy_closeup with dissolve
    "She gasped when I shoved her legs apart and felt between them with my fingers."
    c "You're wet, doctor."
    scene ep006_doctor_doggy_alt with dissolve
    "The woman only gasped, because she felt the tip of my dick against her moist lips."
    scene ep006_doctor_doggy_fuck with vpunch
    "Holding her flanks, I parted her lower lips with the tip of my cock and speared her pussy in one swift motion."
    "She clenched her teeth as my balls slapped against her soft flesh."
    c "How does that feel, doctor?"
    scene ep006_doctor_doggy_fucking with dissolve
    "I didn't wait for her answer, but started fucking her hard."
    "The woman had to steady herself against the creaking chair, her hands buried deeply in the leather cushions."
    scene ep006_doctor_doggy_fucking_alt with dissolve
    "Because of the violence of my thrusts, her moans came out haltingly, as if she were stuttering."
    "The guards still had their backs turned towards us and remained silent."
    "The only thing that could be heard where the doctor's moans and the sounds of my cock plunging wetly into her depths."
    scene ep006_doctor_doggy_fucking_hair with dissolve
    "I grabbed her braids and pulled her towards me, her back straining to arch towards me."
    scene ep006_doctor_doggy_fucking_hair_alt with dissolve
    "Holding her upper body in a strangled embrace, I buried my cock to the root inside her cunt."
    show ep006_doctor_doggy_fucking_hair_pull_closeup with dissolve
    "The doctor's panting and moans were tinged with a raw edge of pain, but she allowed me keep fucking her mercilessly."
    c "Do you like that pain, doc?"
    show ep006_doctor_doggy_fucking_hair_pull with dissolve
    chrone "I...{w} I...{w} I fucking love it!"
    chrone "Keep fucking me with that hard dick!"
    scene ep006_doctor_doggy_fucking_hair_closeup with dissolve
    "I had no intention of doing otherwise, but right at that moment my cock slipped from her wet gash."
    chrone "Put it back in, quickly!"

    menu:
        "Blowjob" if is_patreon() and renpy.has_label("extra_scene_11"):
            call extra_scene_11 from _call_extra_scene_11
        "Anal":
            $ ep006_doctor_anal = True
            "I was about to stuff her pussy again, when I got a better idea."
            scene ep006_doctor_ass with dissolve
            "Forcing her lower body down, I pushed against the folds of her anus."
            scene ep006_doctor_ass_closeup with dissolve
            chrone "Wrong entrance!"
            "The doctor tried to guide my cock inside her pussy again, but I slapped her hand away."
            scene ep006_doctor_ass_penetrate with vpunch
            "Grabbing her arms together, I stuffed my throbbing cock inside her asshole."
            "The woman yelped in pain as the first inches slid inside her and she tried speak."
            "Whatever she wanted to say got lost as my entire length disappeared into her rectum."
            "Instead she tried to back away and let my cock slip from her ass."
            "I wouldn't let her."
            scene ep006_doctor_ass_fuck with dissolve
            "So I held her down and started to thrust."
            "The first few attempts I encountered too much friction, but by the fourth trust she relaxed her asshole and I slid in and out with ease."
            scene ep006_doctor_ass_fuck_closeup with dissolve
            chrone "Fuck!{w} You're so big."
            chrone "You're burning me up!"
            show ep006_doctor_ass_fuck_alt with dissolve
            "Her ass was still tight as hell, but I could fuck her as deeply as before, no doubt helped by her pussy juice coating my dick."
            scene ep006_doctor_ass_cowgirl with dissolve
            "Getting a little tired of remaining in the same position, I shoved her on top of me while I sat down on the chair."
            scene ep006_doctor_ass_cowgirl_alt with dissolve
            "She was forced to ride me cowgirl, my cock still firmly rooted inside her ass."
            "Her firm butt hit on my stomach time and time again, until my cock began to twitch."

            menu:
                "Anal creampie":
                    with vpunch
                    "Without warning I was about to cum, I held her fast and thrust my cock deep inside her ass and warm cum started to flow in thick waves."
                    scene ep006_doctor_ass_cowgirl_creampie with flash
                    with flash
                    "When my cock slipped from her asshole, a stream of cum dripped down on the chair."
                    "The doctor rested for a while on the chair, playing with the cum oozing from her butthole."
                "Body":
                    scene ep006_doctor_ass_cowgirl_body with flash
                    with flash
                    "Without warning I was about to cum, I pushed her off me and sprayed her butt and lower back with wave after wave of warm cum."
                    "The doctor rested for a while on the chair, playing with the cum splashed on her body."
        "Vaginal":

            scene ep006_doctor_prone with dissolve
            "I pushed her flat on her stomach on the chair and re-entered her."
            "Using the full weight of my body, I pinned her down and fucked her with short, aggressive strokes."
            scene ep006_doctor_prone_alt with dissolve
            "The force of my thrusts drove her into the leather cushions of the chair and muffled any cries she let out."
            "She was incredibly wet and I drove my cock deeper and deeper inside of her."
            "The doctor struggled under me and tried to get upright."
            scene ep006_doctor_upright with dissolve
            "When I let her, she moaned loudly, almost out of breath."
            scene ep006_doctor_upright_closeup with dissolve
            chrone "Fuck me!{w} Fuck me harder!"
            scene ep006_doctor_upright_breasts with dissolve
            "I pulled the woman on her side to get better access to her large breasts."
            "Still driving myself mercilessly inside her wet cunt, I began kneading her breasts."
            scene ep006_doctor_upright_alt with dissolve
            "Her closed eyes blinked open when I pinched and twisted her nipples."
            chrone "Oh!{w} What are you doing?"
            scene ep006_doctor_upright_slap with vpunch
            "I looked her in the eye and slapped her breasts."
            "She tried to look away, but I grabbed hold of her chin and continued to torment her nipple with my other hand."
            c "I told you this was going to be a hate-fuck."
            scene ep006_doctor_upright_slap_closeup with dissolve
            chrone "I don't care, just don't stop!"
            "That was a request I could honor and I kept drilling her cunt as it leaked pussy juice all over her thighs."
            scene ep006_doctor_upright_wide with dissolve
            "At long last, I knew I was about to cum."
            menu:
                "Creampie [gr]\[Dr. Moora Creampie\]":
                    $ ep006_chrone_creampie = True
                    with vpunch
                    "Without warning I was about to cum, I held her fast and thrust my cock deep inside her vagina and warm cum started to flow in thick waves."
                    scene ep006_doctor_upright_creampie with flash
                    with flash
                    "When my cock slipped from her wet slit, a stream of cum dripped down on the chair."
                    scene ep006_office_pen_woman with dissolve
                    "The doctor rested for a while on the chair, playing with the cum oozing from her cunt."
                "Body":
                    scene ep006_doctor_upright_body with flash
                    with flash
                    "Without warning I was about to cum, I pulled out of her and coated her back with wave after wave of warm cum."
                    scene ep006_office_pen_woman with dissolve
                    "The doctor rested for a while on the chair, playing with the cum splashed on her body."
    $ renpy.end_replay()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
