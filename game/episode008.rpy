
image ep008_av_sex_closeup = Movie(play="movies/ep008/ep008_av_sex_closeup.webm")
image ep008_av_sex_side_alt = Movie(play="movies/ep008/ep008_av_sex_side_alt.webm")
image ep008_av_sex_side = Movie(play="movies/ep008/ep008_av_sex_side.webm")
image ep008_av_sex = Movie(play="movies/ep008/ep008_av_sex.webm")
image ep008_commander_group_doggy_alt = Movie(play="movies/ep008/ep008_commander_group_doggy_alt.webm")
image ep008_commander_group_doggy = Movie(play="movies/ep008/ep008_commander_group_doggy.webm")
image ep008_commander_group_lick_alt = Movie(play="movies/ep008/ep008_commander_group_lick_alt.webm")
image ep008_commander_group_lick = Movie(play="movies/ep008/ep008_commander_group_lick.webm")
image ep008_commander_group_sex_alt = Movie(play="movies/ep008/ep008_commander_group_sex_alt.webm")
image ep008_commander_group_sex_closeup = Movie(play="movies/ep008/ep008_commander_group_sex_closeup.webm")
image ep008_commander_group_sex = Movie(play="movies/ep008/ep008_commander_group_sex.webm")
image ep008_commander_lick_alt = Movie(play="movies/ep008/ep008_commander_lick_alt.webm")
image ep008_commander_lick = Movie(play="movies/ep008/ep008_commander_lick.webm")
image ep008_commander_sex = Movie(play="movies/ep008/ep008_commander_sex.webm")
image ep008_jade_sex_alt = Movie(play="movies/ep008/ep008_jade_sex_alt.webm")
image ep008_jade_sex = Movie(play="movies/ep008/ep008_jade_sex.webm")
image ep008_jade_suck_alt = Movie(play="movies/ep008/ep008_jade_suck_alt.webm")
image ep008_jade_suck = Movie(play="movies/ep008/ep008_jade_suck.webm")


label episode008:
    $ save_name = "Episode 8"

    $ thim_doctor = False
    $ ep008_footage_evening = False
    $ ep008_footage_night = False
    $ ep008_l_talk = False
    $ ep008_warrior_yell = False
    $ ep008_av_erigone_talk = False
    $ ep008_av_creampie = False
    $ ep008_j_talk = False
    $ ep008_j_concern = False
    $ ep008_j_creampie = False
    $ ep008_j_baths = False
    $ ep008_na_talk = False
    $ ep008_ce_talk = False
    $ ep008_ki_erigone_talk = False
    $ ep008_kit_truth = False
    $ ep008_ziv_talk = False
    $ ep008_raene_talk = False
    $ ep008_raene_baths = False
    $ ep008_raene_baths_visit = False
    $ ep008_ziv_dislike = False
    $ ep008_ziv_like = False
    $ ep008_ziv_neutral = False
    $ ep008_ziv_accept = False
    $ ep008_raene_dislike = False
    $ ep008_na_expedition = False
    $ ep008_na_rebuke = False
    $ ep008_commander_talk = False
    $ ep008_commander_visit = False
    $ e008_rahia_decline_polite = False
    $ e008_rahia_decline_rude = False
    $ ep008_commander_sex = False
    $ ep008_anus_lick = False
    $ ep008_athryn_fucked = False
    $ ep008_athryn_choke = False
    $ ep008_frisa_fucked = False
    $ ep008_rahia_creampie = False
    $ ep008_athryn_creampie = False
    $ ep008_frisa_creampie = False
    $ ep008_athryn_fucked_last = False
    $ ep008_frisa_fucked_last = False
    $ ep008_frisa_anal = False

    centered "{=chapter_heading}EPISODE 8{/=chapter_heading}"

    if aven_romance:
        scene ep008_awake_aven with dissolve
        "Céline’s voice stirred me."
        if game.is_special:
            "I nearly jumped from the bed fearing she’d caught me with my naked cousin lying in my arms."
        elif True:
            "I nearly jumped from the bed fearing she’d caught me with a naked girl lying in my arms."
        "Of course Céline was still on the bridge speaking via the ship’s comms."
        if celine_romance:
            "At the same time it hit me that I would have some explaining to do about my romantic entanglements to both Aven and Céline."
            "But I didn’t want to ruin the night Aven and I had just shared."
        ce "[p_name] to bridge."
        scene expression eye_blink("images/ep008/ep008_awake_aven_closeup") with dissolve
        "I was about to rise when Aven lifted her head."
        av "Mmmm, stay?"
        c "I need to get to the bridge, it’s probably something important."
        av "I know..."
        av "Go then, I’ll slip out a little later."
    elif True:
        scene ep008_awake with dissolve
        ce "[p_name] to bridge."
        "Céline’s voice stirred me."
        "I was with her before she could repeat her message over the comms."

    play music "music/red.ogg" fadein 4 fadeout 1.0

    scene ep008_bridge with dissolve
    c "Have we arrived?"
    scene expression eye_blink("images/ep008/ep008_bridge_ce") with dissolve
    ce "Nearly there."
    c "You just wanted me here in case we get toasted by all that radiation?"
    ce "Something like that."
    scene ep008_bridge_alt_sit with dissolve
    "Céline disengaged the S-K drive and stared at the monitors in front of her intently."
    c "Are we dead?"
    scene expression eye_blink("images/ep008/ep008_bridge_ce_doubt") with dissolve
    ce "No, but we’re where we should be."
    ce "Our scanners are picking up an anomaly."
    c "The microquasar?"
    ce "I don’t think so."
    ce "It’s something though, but I need more readings."
    ce "I’ll let you know once I’ve found out more."
    c "Right, catch you later."
    scene ep008_bridge_alt with dissolve
    "When I left the bridge Jade contacted me."
    if not ep007_j_injured:
        scene ep008_engine_j with dissolve
        "She was at the workbench in the engine room."
        c "Is Thyia not with you?"
        scene expression eye_blink("images/ep008/ep008_engine_j_closeup") with dissolve
        j "No, she’s spending time with Lilly I believe."
        c "What did you need me for?"
    elif True:
        scene ep008_medbay with dissolve
        "She was still in the infirmary, convalescing from her foot wound."
        if (ep005_thim_joke or ep005_thim_press) and (ep001_medbay_thim_ignored + ep002_pit_thim + ep003_thim_insult) <= 2:
            $ thim_doctor = True
            c "How’s the patient, doctor?"
            scene expression eye_blink("images/ep008/ep008_medbay_th") with dissolve
            t "Stubborn and willful."
            t "She wanted to get out of bed and walk to the bridge."
            t "At which point I had to remind her of the bullet wound in her foot."
            if ep005_jade_punish and ep004_jade_dom and not ep004_jade_apologize:
                j "Is that you, master?"
            elif True:
                j "Thim, you really need to learn about doctor-patient confidentiality."
            c "I’ll go check up on the patient."
            c "I hear you’re not exactly a model patient?"
            scene expression eye_blink("images/ep008/ep008_medbay_j") with dissolve
            j "I guess I haven’t been, but lying here doing nothing is just terrible."
            j "But I found a project to work on."
        elif True:
            scene expression eye_blink("images/ep008/ep008_medbay_j") with dissolve
            c "How are you holding up?"
            j "I’m feeling fine."
            j "I’ll be up and running in no time."
            c "Be sure to take enough rest."
            c "You messaged me?"

    j "I’ve been messing around with Cetruvar’s tablet, looking at some of the encrypted files."
    c "And?{w} Have you found more on the Acarhyn?"
    j "Sadly, no, nothing more on them."
    j "But I’ve found something else, security footage."
    c "Oh?"
    j "Apparently Cetruvar had some of the feeds forwarded to his tablet, probably convenient."
    j "One of them was of the cell they stashed that woman in, the one that apparently killed herself?"
    j "She mostly sits there for the duration of the video and does some exercises, but I found two interesting things."
    if not ep007_j_injured:
        scene expression eye_blink("images/ep008/ep008_engine_j_closeup_serious") with dissolve
    elif True:
        scene expression eye_blink("images/ep008/ep008_medbay_j_serious") with dissolve
    j "Shall I show them to you?"
    c "Of course."
    j "There’s one snippet just before evening falls and one where the video feed has been cut out, so there’s only audio."

    $ woman_name = "Prisoner"
    $ woman_portrait = "side_bodyguard"

    menu ep008_footage:
        "Watch evening snippet" if not ep008_footage_evening:
            $ ep008_footage_evening = True
            if not ep007_j_injured:
                scene ep008_woman_cell with dissolve
            elif True:
                scene ep008_woman_cell_medbay with dissolve
            "Jade showed me a video of the woman pacing around her cell."
            c "So she’s pacing?"
            c "Wait, is she muttering something?"
            j "She is."
            c "Can you enhance the audio?"
            j "I tried, it’s not perfect, but you can get the gist."
            j "It sounds like a bunch of nonsense to me, a prayer or something."
            j "She keeps repeating it too."
            if not ep007_j_injured:
                scene ep008_woman_cell_closeup with dissolve
            elif True:
                scene ep008_woman_cell_closeup_medbay with dissolve
            woman "In the dying light of triple suns..."
            woman "I hum a binary tune..."
            woman "My ears shatter as the great bear roars..."
            woman "And my feet touch dust and bone..."
            woman "As I walk across a field of ancient hubris and conceit..."
            woman "In the abyss of birds..."
            woman "When the augur strikes the anvil of ingress..."
            if not ep007_j_injured:
                scene ep008_woman_cell_closeup_alt with dissolve
            elif True:
                scene ep008_woman_cell_closeup_alt_medbay with dissolve
            woman "Hippolyta births the singularity..."
            woman "While chaos rides a metal warhorse..."
            woman "My desiccated mouth tastes of ashes..."
            woman "My aberrative mind shatters..."
            if not ep007_j_injured:
                scene ep008_woman_cell_closeup_alt with dissolve
            elif True:
                scene ep008_woman_cell_closeup_medbay with dissolve
            woman "As I abscind and coalesce..."
            woman "In the throes of supreme vicissitude..."
            woman "I awaken, forever torn..."
            woman "Between Tartarus and Cucaniensis."
            c "Well, it sure is weird."
            c "Does it sound like something religious to you?"
            if not ep007_j_injured:
                scene expression eye_blink("images/ep008/ep008_engine_j_closeup_serious") with dissolve
            elif True:
                scene expression eye_blink("images/ep008/ep008_medbay_j_serious") with dissolve
            j "I’m not sure, my knowledge of human religions is a little hazy, to be honest."
            c "Show this to Nadya and Aven, but to no-one else."
            j "Right, I will."
            jump ep008_footage
        "Watch night snippet" if not ep008_footage_night:
            $ ep008_footage_night = True
            if not ep007_j_injured:
                scene ep008_tablet_static with dissolve
            elif True:
                scene ep008_woman_cell_night_medbay with dissolve
            "The woman stared out over the ocean until night had fallen."
            "When she sat on her bed there was a sound of a door opening."
            "At that moment the video feed was cut, only voices could be heard."
            if not ep007_j_injured:
                scene ep008_woman_cell_night with dissolve
            elif True:
                scene ep008_tablet_medbay_static with dissolve
            woman "You’ve come."
            "The other person in the room either didn’t speak or their speech was inaudible."
            woman "For my failure I’m supposed to end my life, there’s no escape."
            woman "I’ve accepted this."
            woman "Tell our master it has been an honor to serve."
            "Again the sound of a door, followed by a resigned sigh from the woman."
            "Then the unmistakable sound of steel piercing flesh, heavy grunting."
            "A body dropping to the floor, followed by soft gurgling."
            c "Someone slipped her a weapon."
            c "One of the guards?"
            if not ep007_j_injured:
                scene expression eye_blink("images/ep008/ep008_engine_j_closeup_serious") with dissolve
            elif True:
                scene expression eye_blink("images/ep008/ep008_medbay_j_serious") with dissolve
            j "I’m not sure."
            j "As far as I can discern the other person in the room doesn’t speak to the prisoner."
            j "But I think she’s handed a knife before the other person leaves. "
            j "The video of the feed never comes back."
            c "Disturbing."
            jump ep008_footage
    c "I don’t think anyone else needs to see that night footage at the moment, but Aven or Nadya could provide some insight on the prayer."
    if not ep007_j_injured:
        c "Céline is analyzing the system we want to breach."
        c "It doesn’t seem to be an instant-death kind of deal."
        scene expression eye_blink("images/ep008/ep008_engine_j_closeup") with dissolve
        j "I’ll join her shortly, see if I can help her."
        c "Sounds good."
    elif True:
        c "Get well soon, Jade."
        scene expression eye_blink("images/ep008/ep008_medbay_j") with dissolve
        if ep005_jade_punish and ep004_jade_dom and not ep004_jade_apologize:
            j "I will master."
        elif True:
            j "Thanks."

    call ep008_conversations from _call_ep008_conversations

    play music "music/red.ogg" fadein 4 fadeout 1.0

    scene ep008_bridge_alt with dissolve
    "Eventually, Céline pinged me and asked if I would rejoin her on the bridge."
    c "Do you know what's inside that nebula?"
    scene expression eye_blink("images/ep008/ep008_bridge_alt_ce") with dissolve
    ce "Yes, I'm pretty sure it's a single planet orbiting a yellow dwarf."
    ce "Many of the readings just don't make sense."
    ce "A cursory look would make you believe it truly is the irradiated mess it appears to be."
    ce "But there's a pattern to the distortions."
    c "Like someone or something is actively manipulating the readings?"
    ce "That seems likely."
    ce "I sent out a probe and it came back clean."
    ce "There's no radiation in that nebula, or at least not a lethal amount."
    ce "So I started cross-referencing all of the data I had and I'm pretty sure there's a small planet in the center of that gas cloud."
    c "Good."
    c "I'll call the others."
    c "Time to see that planet for ourselves."
    scene ep008_bridge_crew with dissolve
    "Aven, Kit and Nadya joined us on the bridge and Céline brought them up to speed."
    "Nadya wanted to check the readouts from the probe multiple times before she signed off on entering the nebula."
    "Her findings, which corresponded with Céline's, seemed to put Aven's mind at ease."
    c "Céline, would you please be so kind as to fly us swiftly into the Horrific Nebula of Certain Death?"
    scene expression eye_blink("images/ep008/ep008_bridge_crew_ce") with dissolve
    ce "Aye, aye, sir!"
    scene expression eye_blink("images/ep008/ep008_bridge_crew_na") with dissolve
    na "Let's abstain from the gallows humor before we actually reach our destination."
    c "That does kind of defeat the purpose, doesn't it?"
    scene ep008_bridge_crew_alt with dissolve
    "Despite the reassuring test results about the true nature of the gas cloud, I was more than apprehensive."
    "The readings of the ship's instruments became increasingly erratic as we neared our point of entry into the nebula."
    "Several warnings told us we were subjected to extremely high doses of lethal radiation at that moment."
    "After the tenth death spike registered by our systems failed to kill us I became more confident of our gamble."
    "We were now completely inside the nebula, honing in on the location of the only planet in the system."
    "All of a sudden, all the death warnings were gone from the ship's console and we cleared the nebula."
    scene expression eye_blink("images/ep008/ep008_bridge_crew_ce") with dissolve
    ce "There it is."
    c "Thank fuck it's not a failed star leaking into a black hole."
    ce "Just a boring little star and a boring little planet."
    scene expression eye_blink("images/ep008/ep008_bridge_crew_av") with dissolve
    av "I wouldn't be so sure about that, looks can be deceiving."
    c "Only one way to find out."
    "We approached the planet at brisk speed."
    "As far as we could tell there was currently no one roaming local space, nor orbiting the planet."
    av "It sure is very quiet."
    c "You expected a welcome party?"
    av "I really didn't know what to expect."
    c "Well, maybe our welcome party is still planetside."
    c "Let's break orbit."
    "On my mark we began our descent."
    scene ep008_erigone_descent with dissolve
    "As soon as we cleared the cloud deck of the planet we were able to see an immense forest stretching for miles."
    "The Bastard's scanners were already collecting data."
    scene expression eye_blink("images/ep008/ep008_bridge_crew_na") with dissolve
    na "According to our readings, this planet seems to be inhabited."
    c "Anything to the contrary would be a big disappointment up to this point."
    scene expression eye_blink("images/ep008/ep008_bridge_crew_ce") with dissolve
    ce "There are several mountain ranges in the vicinity."
    ce "Also, some large unidentified structures."
    c "It might be worth getting a close look at those."
    "Our ship sped across the outstretched jungle until the very large anomalies were in visual range."
    scene expression eye_blink("images/ep008/ep008_bridge_crew_av_doubt") with dissolve
    av "Those are the engines from a capital ship, aren't they?"
    c "Yes..."
    av "And that's the hull from a command carrier."
    c "Maybe..."
    av "Is this some sort of ship graveyard?"
    scene ep008_erigone_descent_alarm with vpunch
    "The ship's siren shocked us into alertness."
    ce "Missiles approaching!"
    c "From where?"
    ce "Not sure, the mountains, maybe?"
    ce "Fuck!"
    scene ep008_erigone_descent_missiles with dissolve
    "Céline jerked the ship around in an attempt to evade the sudden onslaught of missiles."
    "The Bastard lurched and bucked, pulling through the first wave of projectiles relatively unscathed."
    "However, immediately after we cleared the initial assault, another volley followed."
    "Céline desperately tried to dodge the attack again, but failed."
    scene ep008_erigone_descent_missiles_hit with vpunch
    "The ship groaned and shuddered and explosions could be heard as several missiles hit the hull."
    "A chorus of alarms now drowned out much of the other sounds."
    "The ship tilted suddenly, despite Céline's efforts to keep her steady."
    scene ep008_crash with dissolve
    "With a sickening speed the ship lurched towards the green canopy of the jungle beneath us."
    "Multiple fires were being reported on the ship's monitors."
    scene ep008_erigone_descent_alarm with dissolve
    ce "We've lost control over the starboard thrusters."
    c "Then get us on the ground in one piece."
    "I'm sure we all shared the panic palpable in Céline's voice."
    "There was nothing else we could do but brace ourselves for the inevitable."
    "Trying to make due with whatever control she had over the ship, Céline tried to decelerate and prepare for a crash landing."
    scene ep008_erigone_bridge_glass with vpunch
    "Glass broke when we hit the highest trees in the jungle and thick branches lashed at the ships hull."
    "The whole Bastard was shaking massively and groaning as if she was torn asunder."
    scene ep008_erigone_bridge_dark with vpunch
    "Everything was dark all of a sudden as we plunged deeper into the jungle and the ship's electronics gave out."
    "Combined with our speed, the ship was strong enough to plow through several trees and clear a path."
    scene ep008_crashed with vpunch
    "Moments after we dropped out of the sky, we hit the ground with a terrible crash."
    "The nose of our ship burrowed itself into the wet soil of the wilderness."
    "After several miles we finally came to an abrupt standstill."
    "The ear-splitting noise gradually subsided, replaced by the sounds of groaning metal and fires roaring to life."
    scene ep008_erigone_bridge_post with dissolve
    "I forced myself out of the captain's chair and staggered around on the bridge."
    "Amazingly, everyone seemed to be conscious and unharmed."
    c "We need to get out of here."
    c "I'll get the others."
    scene ep008_erigone_corridor with dissolve
    "I made my way to the ship's quarters and encountered most of the crew on my way."
    "Our involuntary landing had torn deep gashes into the hull, even exposing one of the corridors to the outside air."
    scene ep008_erigone_corridor_opening with dissolve
    "I paused, sensing something."
    "It was as if the ground thrummed."
    scene ep008_crashed_mechs with vpunch
    "Trees shook and fell to the ground as a very large mech stomped into view."
    "A large searchlight shone over the ruined Bastard."
    "I ducked away too late and several large guns were trained at me."
    "The dull thumps on the ground could still be felt and I knew there were more mechs approaching."
    "I stared at the mech's cockpit, waiting to be gunned down or for something else to happen."
    scene ep008_crashed_mechs_alt with dissolve
    "Luckily, the person in the mech chose the latter option as a voice crackled through a loudspeaker."
    $ woman_name = "Mech"
    $ woman_portrait = "side_woman"
    woman "Surrender yourself and be spared."
    "With our ship in ruins and facing a bunch of colossal mechs, I didn't really know whether they expected us to do something else than surrendering."
    "But it was nice of them to offer us the illusion of choice."
    "Regardless, I don't think any member of the crew begrudged me when I shouted my reply at the mechanical beast in front of me."
    c "We surrender."
    scene ep008_crashed_mechs_wide with dissolve
    "Several mechs had now come into view, towering over the crash site."
    scene expression eye_blink("images/ep008/ep008_crashed_mechs_closeup") with dissolve
    "In reply to my words, the cockpit hatch of the mech opened to reveal a woman."
    "Her garb looked instantly familiar and I knew we had found the Acarhyn."
    scene expression eye_blink("images/ep008/ep008_crashed_mechs_closeup_alt") with dissolve
    woman "Bring out all of the crew. "
    woman "A salvage team will arrive shortly to treat any wounded and escort you back to the Citadel."
    scene ep008_crashed_women with dissolve
    "A group of warrior women arrived in a ground car after a few minutes."
    "By then, the crew of the Bastard had abandoned ship and was waiting to be taken in."
    "The darkness and smoke made it difficult to assess the damage to the ship, but I knew it was extensive."
    "That aerial assault and subsequent crash landing might very well have been the Bastard's death sentence."
    "We didn't have much time to dwell on it, because the women herded us into the armored ground car and we were swept away from the crash site."
    scene ep008_crashed_women_alt with dissolve
    "My only encounter with the Acarhyn had been on Lanan, so I only knew them as sword-wielding warriors wearing antiquated armor."
    "The level of technology on display here, including the mechs and anti-aircraft weapons, didn't mesh with my earlier estimation of their technical sophistication."
    scene ep008_crashed_car with dissolve
    "The journey by ground car took us nearly an hour."
    "There were no windows in the car, so we had no idea where they were taking us."
    scene ep008_transport_interior with dissolve
    "Nobody spoke, as we were still too numb from the crash we'd just endured."
    "The two Acarhyn watching us likely also factored into that decision."
    "My ears popped and I had some trouble breathing for some time, a tell-tale sign we were gaining altitude."
    "We were very probably driving in some mountainous area."
    "Abruptly we stopped."
    "Both Acarhyn motioned us to leave the ground car and to follow them."
    scene ep008_erigone_citadel with dissolve
    "I squinted at the sunlight and took in the scenery surrounding me."
    "We were indeed on some mountain range, in front of something that looked like a very large medieval castle."
    "I was half-expecting some knight on horseback to come trotting through the gate, but somehow the very modern looking gun turrets on top of the towers spoiled that notion."
    scene ep008_erigone_citadel_alt with dissolve
    "We were forced to march single-file down a flight of stone stairs beneath the castle."

    play music "music/computations-in-a-snowstorm-alt-mix.ogg" fadein 4 fadeout 1.0

    "The medieval castle also appeared to have a medieval dungeon."
    scene ep008_erigone_citadel_dungeon with dissolve
    "Again, the rustic look was marred by a wealth of cameras and electronic security measures."
    "We passed several cells until the Acarhyn told us to stand against the wall."
    scene ep008_erigone_cell with dissolve
    "The women were swiftly separated from the men and Kit, Thim and I were then pushed inside a jail cell."
    "The door closed with a heavy thud and locked itself automatically."
    scene ep008_erigone_cell_man with dissolve
    "My eyes were still adjusting to the sparse light when an unfamiliar voice startled us."
    $ man_name = "Prisoner"
    $ man_portrait = "side_prisoner"
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup") with dissolve
    man "New blood?"
    c "I guess you could say that."
    "A man was sitting against the wall."
    "He wasn't wearing much, just a simple dirty smock."
    c "You've been here a while, I take it?"
    man "I have."
    t "Do they treat you well?"
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup_smile") with dissolve
    man "Why, are you afraid they might hurt you?"
    t "We just don't know what they intend to do with us."
    man "Well, I reckon there'll be an auction at some point..."
    ki "An auction?"
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup") with dissolve
    man "Yes, though it's been a while."
    man "The new queen doesn't like it apparently."
    c "She doesn't like what exactly?"
    man "The slave auctions, of course."
    man "Tell me boys, do you like to fuck?"
    man "Because that's what you'll do, a lot, once you're sold to one of the Acarhyn."
    c "We'll be sold as sex slaves?"
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup_serious") with dissolve
    man "That's the gist of it, yes."
    man "You're lucky if you can get one of them pregnant, because you'll have a few months of free time."
    t "They need human males to breed with them..."
    man "Well, as far as I know the Acarhyn are some human offshoot, created in a lab."
    man "And they only conceive daughters, so you see the problem."
    man "So, once in a while they raid some human settlement somewhere and take prisoners."
    man "Back here, the kidnapped females become servants and the males become a valuable trading commodity."
    c "I feel valued already..."
    ki "Is there a way out?"
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup_smile") with dissolve
    man "Hah, you'd be better off just accepting your fate."
    man "I mean, you get clothed, fed, a roof over your head and you get to fuck a hard-bodied supermodel warrior once in a while."
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup") with dissolve
    man "Or you could do the stupid thing and try to run, like I did."
    man "And now I'm here, getting sold again to another Acarhyn."
    t "You tried to escape?"
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup_serious") with dissolve
    man "Twice."
    man "Last time I got caught with the ship that would take me away from this planet in sight."
    man "Luckily, the Acarhyn don't punish the men that try to escape."
    man "They seem to value willful men, so I reckon I'll fetch an even higher price on the market this time."
    man "So it's back to fucking some highly placed Acarhyn all day."
    man "It starts to lose its initial appeal after a while, but it beats sitting around in this cell, that's for sure."
    ki "Where are you from?"
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup_doubt") with dissolve
    man "Does it matter?"
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup") with dissolve
    man "Some small backwater system in the Satrapian Cluster."
    c "Do you know any people who were taken here from Lanan P-10?"
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup_doubt") with dissolve
    man "That name sounds familiar."
    man "I know they took back a large group of people months ago."
    c "I'm looking for someone, a girl who was taken."
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup_smile") with dissolve
    man "Good luck with that."
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup") with dissolve
    man "She's probably working as a servant somewhere in an Acarhyn household, sweeping floors and cooking dinner."
    scene expression eye_blink("images/ep008/ep008_erigone_cell_man_closeup_smile") with dissolve
    man "And as you're all going to spend the rest of your lives playing breeding bulls to your Acarhyn overlords, there's zero chance you'll find her."
    scene ep008_erigone_cell_man_alt with dissolve
    "I didn't have the stomach for any more downbeat talk from our fellow prisoner, so I sat down in a corner and stared into the distance."
    "Thim and Kit grilled the man further on their supposed new life as Acarhyn property."
    scene ep008_erigone_cell_door with dissolve
    "I must have fallen asleep, because the noise of the cell door opening startled me awake."
    "Kit and Thim were still asleep, as was our cellmate."
    "A familiar face entered the cell, the woman from Lanan."
    scene expression eye_blink("images/ep008/ep008_erigone_cell_door_woman") with dissolve
    $ warrior_name = "Commander"
    rah "You.{w} Come with me."
    menu:
        "Yell at her" if True:
            $ ep008_warrior_yell = True
            "The only thing that kept me from attacking her was that gigantic sword she was carrying."
            "The terror and impotent rage I felt back on Lanan all came flooding back in."
            c "You miserable bitch, what did you do to my friends?!"
            scene expression eye_blink("images/ep008/ep008_erigone_cell_door_woman_unsure") with dissolve
            rah "They’re in a similar cell as you are and unharmed."
            scene expression eye_blink("images/ep008/ep008_erigone_cell_door_woman_serious") with dissolve
            rah "Please contain yourself, or I’ll be forced to restrain you."
            rah "Now, come with me."
            "Grudgingly, I followed the woman out the jail cell."
        "[gr]Remain silent" if True:
            "I didn't feel like I had much of a choice, considering I didn't carry one of those gigantic swords around."
            "The terror and impotent rage I felt back on Lanan all came flooding back in and I felt powerless once more."

    scene ep008_erigone_corridor_acarhyn with dissolve
    "The woman and two other Acarhyn escorted me up a flight of stairs."
    "Sunlight touched the roughly hewn stone of the ground floor corridors, making it feel decidedly less oppressive than the dungeon we just left behind."
    scene ep008_erigone_throne with dissolve
    "After crossing several iron gates, I was brought before a large throne inside a large room, lit by crystal pedestals."
    rah "Kneel."
    "I was too bewildered to immediately comply with her command, so the two women pushed me to the floor."
    scene ep008_erigone_throne_alt with dissolve
    "Their commander took up position beside the throne."
    "And then nothing happened for a long time."
    "The stone floor was rather uncomfortable and the two armed women looming behind me didn't help much either."
    "I was studying the floating glowing crystals on the pedestals when I heard footsteps."
    "Several women entered."
    scene expression eye_blink("images/ep008/ep008_erigone_throne_alt_closeup") with dissolve
    rah "Behold, Her Highness, The Virgin Queen."
    scene ep008_erigone_throne_queen with dissolve
    "A girl, dressed in an elaborate gown with a large bejeweled collar strode towards the throne."
    scene ep008_erigone_throne_queen_alt with dissolve
    "As soon as I recognized her I wanted to jump up and embrace her, but one of the women firmly pinned me down."
    scene expression eye_blink("images/ep008/ep008_erigone_throne_alt_closeup_angry") with dissolve
    rah "Do not dare to disrespect the Virgin Queen!"
    c "Eva!"
    scene ep008_erigone_throne_queen_sit with dissolve
    "My exclamation earned me several angry glares, but Eva just looked at me impassively as she sat down on the throne."
    scene expression eye_blink("images/ep008/ep008_erigone_throne_queen_sit_closeup") with dissolve
    e "We have recently learned of your arrival and subsequent imprisonment."
    "Eva's voice was edged with an authority I'd never heard from her before."
    e "It pleases us to offer you our hospitality until the day when your vessel has been repaired and is fit for travel again."
    e "We hope this gesture of goodwill will allay any ill feelings towards your initial treatment which was based on an oversight for which the people responsible express their heartfelt remorse."
    if game.is_special:
        "Any hope of talking to my sister was dashed by her standing up from the throne and leaving the room abruptly."
    elif True:
        "Any hope of talking to Eva was dashed by her standing up from the throne and leaving the room abruptly."
    scene expression eye_blink("images/ep008/ep008_erigone_throne_alt_closeup") with dissolve
    rah "Her Majesty has spoken."
    rah "Stand up and follow me."

    python:
        if game.is_special:
            codex_eva = update_codex_entry(codex_eva, None,
                [
                    __("Eva Valenmann de Lonval, sister of Lilly and [p_name]. Kidnapped on a training mission on Lanan P-10 by a group of warrior women called the Acarhyn."),
                    __("Eva now apparently rules over the Acarhyn as their Virgin Queen.")
                ]
            )
        else:
            codex_eva = update_codex_entry(codex_eva, None,
                [
                    __("Eva Arderne, childhood friend of [p_name]. Kidnapped on a training mission on Lanan P-10 by a group of warrior women called the Acarhyn."),
                    __("Eva now apparently rules over the Acarhyn as their Virgin Queen.")
                ]
            )

    scene ep008_erigone_corridor_acarhyn_alt with dissolve
    "Without an escort this time, the Acarhyn took me through a series of corridors and halted in front of a door."
    scene expression eye_blink("images/ep008/ep008_erigone_corridor_acarhyn_closeup") with dissolve
    rah "These will be your quarters for the duration of your stay here in the Citadel."
    rah "Meals will be served in the main hall."
    rah "You're allowed the use of our communal baths and any expenses you make will be compensated by the Crown."
    rah "Your friends will be assigned similar quarters shortly."
    rah "Any possessions from your ship will be transferred to you in due time."
    c "Thanks, I guess?"
    c "What about our ship?"
    rah "The Queen has decreed your vessel to be repaired at the Aegisthus Shipyards."
    rah "The damage to the ship is extensive, but she seems to be salvageable, according to our engineers."
    c "When will I see her again?"
    scene expression eye_blink("images/ep008/ep008_erigone_corridor_acarhyn_closeup_doubt") with dissolve
    rah "Who?"
    c "Eva."
    scene expression eye_blink("images/ep008/ep008_erigone_corridor_acarhyn_closeup") with dissolve
    rah "You may petition for an audience with the Virgin Queen."
    rah "I'll let you get settled here."
    scene ep008_erigone_corridor_acarhyn_leaving with dissolve
    "Ignoring any attempts at me to continue the conversation, the woman left me in front of the door."
    "The door responded to my touch and revealed a sparsely furnished bedroom."
    scene ep008_erigone_quarters with dissolve
    "I tried the bed and it sure felt better than the cold stone floor I'd spent the night on."
    "I closed my eyes and slept for an hour."

    play music [ "music/tears-in-rain.ogg", "music/the-spaces-between.ogg", "music/beautiful-oblivion.ogg" ] fadeout 4 fadein 1.0

    "After I woke up, I decided to find my friends who should have been assigned quarters by now."

    menu ep008_citadel_conversations:
        "Visit Lilly" if not ep008_l_talk:
            $ ep008_l_talk = True
            call ep008_lilly_talk from _call_ep008_lilly_talk
            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations
        "Visit Aven" if not ep008_av_erigone_talk:
            $ ep008_av_erigone_talk = True
            call ep008_aven_erigone_talk from _call_ep008_aven_erigone_talk
            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations
        "Visit Nadya" if not ep008_na_talk and ep008_ki_erigone_talk:
            $ ep008_na_talk = True
            call ep008_nadya_talk from _call_ep008_nadya_talk

            if not ep008_commander_talk:
                $ ep008_commander_talk = True
                call ep008_commander from _call_ep008_commander

            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations
        "Visit Céline" if not ep008_ce_talk:
            $ ep008_ce_talk = True
            call ep008_celine_talk from _call_ep008_celine_talk
            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations
        "Visit Kit" if not ep008_ki_erigone_talk:
            $ ep008_ki_erigone_talk = True
            call ep008_kit_erigone_talk from _call_ep008_kit_erigone_talk

            if not ep008_commander_talk and not ep008_kit_truth:
                $ ep008_commander_talk = True
                call ep008_commander from _call_ep008_commander_1

            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations
        "Visit Jade" if not ep008_j_talk:
            $ ep008_j_talk = True
            call ep008_jade_talk from _call_ep008_jade_talk
            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations
        "Visit Ziv" if not ep008_ziv_talk:
            $ ep008_ziv_talk = True
            call ep008_ziv_talk from _call_ep008_ziv_talk
            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations
        "Visit Raene [gr]\[Do before Kit\]" if not ep008_raene_talk and ep006_raene_accept:
            $ ep008_raene_talk = True
            call ep008_raene_talk from _call_ep008_raene_talk

            if not ep008_commander_talk:
                $ ep008_commander_talk = True
                call ep008_commander from _call_ep008_commander_2

            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations
        "Visit Raene" if not ep008_raene_baths_visit and ep008_raene_baths and ep008_j_talk:
            $ ep008_raene_baths_visit = True
            call ep008_raene_baths from _call_ep008_raene_baths
            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations
        "Visit Jade" if ep008_j_talk and ep008_raene_talk and not ep008_j_baths and not ep008_raene_baths:
            $ ep008_j_baths = True
            call ep008_j_baths from _call_ep008_j_baths
            scene ep008_erigone_quarters with dissolve
            jump ep008_citadel_conversations

    scene ep008_hallway_night with dissolve
    "Night had fallen and the halls were mostly empty."
    "I decided to find my quarters and sleep for a couple of hours."
    scene ep008_quarters_night with dissolve
    "When I was about to undress and go to sleep someone knocked on my door."
    scene expression eye_blink("images/ep008/ep008_quarters_night_woman") with dissolve
    "One of the guards wearing a light colored suit of armor stood in the hallway."
    $ woman_name = "Guard"
    woman "The Queen would like to see you in her chambers."
    woman "Follow me."
    "My heart suddenly hammered in my chest."
    if game.is_special:
        "I was about to see my sister again."
    elif True:
        "I was about to see my friend again."
    "Speak to her again, without restrictions."
    scene ep008_hallway_night_woman with dissolve
    "Enheartened, I walked behind the guard who led me to the Queen’s Chambers."
    scene black with fade
    jump episode009
    return

label ep008_lilly_talk:
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_l") with dissolve
    if (ep008_av_erigone_talk + ep008_na_talk + ep008_j_talk + ep008_ki_erigone_talk + ep008_ce_talk + ep008_ziv_talk + ep008_raene_talk) > 5:
        l "What took you so long?"
    l "Is it true?!{w} Did you meet her?"
    c "Yes, I met her."
    l "Well, how did she seem?"
    l "Have they treated her well?"
    c "Hard to say, but as far a I could tell, they haven't done anything bad to her."
    c "The opposite probably, because they revere her as a queen."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_l_doubt") with dissolve
    l "A queen...{w} Eva?"
    c "Yes, it appears she's the Virgin Queen mentioned in the data we retrieved from Cetruvar."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_l") with dissolve
    l "But what did she tell you?"
    l "Was she happy to see you?"
    c "She apologized and offered us shelter."
    c "Other than that I'm not sure she recognized me."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_l_fear") with dissolve
    l "Of course she did, she must have!"
    l "Why else would she pull us out of that dungeon?"
    c "That's true, and she was playing the role of queen, of course."
    c "I'm really hoping we get a private moment with her."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_l_serious") with dissolve
    l "Do you know how we can reach her?"
    c "A formal petition..."
    c "Maybe we should wait until she contacts us somehow."
    l "Maybe, but just petition anyway."
    c "Of course."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_l_smile") with dissolve
    l "Oh [p_name_short], I'm so happy that she's still alive and unharmed!"
    c "Me too."
    l "I never thought we'd find her."
    l "I'm sorry I doubted you."
    return

label ep008_nadya_talk:
    $ cae_name = "Acarhyn"
    scene ep008_na with dissolve
    if game.is_special:
        "Aunt Nadya was sitting at a table talking avidly with one of the Acarhyn."
    elif True:
        "Nadya was sitting at a table talking avidly with one of the Acarhyn."
    scene expression eye_blink("images/ep008/ep008_ca_closeup") with dissolve
    na "I'd be happy to join you."
    cae "That would be such an honor, we'll let you know as soon as an expedition will be mounted."
    scene ep008_ca_alt with dissolve
    "The woman nodded at me as she stood up and left the dining hall."
    scene expression eye_blink("images/ep008/ep008_na_closeup") with dissolve
    c "Making friends?"
    na "It's just amazing."
    scene expression eye_blink("images/ep008/ep008_na_closeup_smile") with dissolve
    na "Caese told me about this rare species of bird native to the jungle."
    na "They're going to mount an expedition especially for me."
    c "How did you convince them to do that?"
    scene expression eye_blink("images/ep008/ep008_na_closeup") with dissolve
    na "Oh no, it's not like that."
    na "Caese actually knows some of my work on the subject."
    c "Ah, you have a fan?"
    scene expression eye_blink("images/ep008/ep008_na_closeup_doubt") with dissolve
    na "Well...{w} She just shares my fascination."
    c "It seemed like a little more than that, awestruck might be a better word."
    scene expression eye_blink("images/ep008/ep008_na_closeup_smile") with dissolve
    na "Okay, okay, she might have been a little impressed by my work."

    $ cae_name = "Caese"
    
    python:
        codex_caese = add_codex_entry(
            Codex,
            __("Characters"),
            __("Caese"),
            [
                __("A young Acarhyn scientist, infatuated with Nadya.")
            ],
            "images/codex/Caese.webp"
        )

    scene expression eye_blink("images/ep008/ep008_na_closeup") with dissolve
    na "But enough about that, you have seen Eva, haven't you?"
    scene expression eye_blink("images/ep008/ep008_na_closeup_doubt") with dissolve
    na "Is she all right?"
    c "She seems to be."
    c "Eva is the queen of the Acarhyn, it seems."
    scene expression eye_blink("images/ep008/ep008_na_closeup_serious") with dissolve
    na "Yes, she seems to be quite revered by the Acarhyn."
    na "Caese talked about her with great respect."
    c "I really want to talk to her personally, to learn about what has happened since she was taken on Lanan."
    na "I'm sure we'll get to talk to her in private at some point."
    na "But it might require some patience on our part, I'm sure Eva is held back by all the decorum."
    c "I think so, yes."
    scene expression eye_blink("images/ep008/ep008_na_closeup_smile_alt") with dissolve
    na "I can't wait to see her either."
    na "It's been such a long time."
    na "Reuniting with both you and Lilly has been such a boon and now the same seems to be in reach for Eva."
    c "Well, if we get to speak to her again and not as the Virgin Queen..."
    scene expression eye_blink("images/ep008/ep008_na_closeup_serious") with dissolve
    na "I know, but let's be hopeful."
    na "We've started this long journey together and we may be here for a while, but I'm confident everything will be made right again."
    c "I hope so too."
    c "At least a long stay here on Erigone gives you the opportunity to go bird-hunting."
    scene expression eye_blink("images/ep008/ep008_na_closeup_doubt") with dissolve
    na "Oh sorry, I didn't come across as selfish, did I?"
    na "It's just that this is such an opportunity and we have a lot of spare time all of a sudden and..."
    menu:
        "Don't worry [NadyaPath]" if True:
            if game.is_special:
                c "Don't worry about it, Aunt Nadya."
            elif True:
                c "Don't worry about it, Nadya."
            c "Those birds must be something really special."
            scene expression eye_blink("images/ep008/ep008_na_closeup_shy") with dissolve
            na "I'm sure you think me very silly once you lay eyes on them."
            c "Do they look that unassuming?"
            scene expression eye_blink("images/ep008/ep008_na_closeup_smile") with dissolve
            na "Well, yes, but their physiology [p_name], it's so amazing!"
            c "I really love it when you get carried away like that."
            scene expression eye_blink("images/ep008/ep008_na_closeup_shy") with dissolve
            na "Oh...{w} uh..."
            c "No really, your enthusiasm is infectious."
            scene expression eye_blink("images/ep008/ep008_na_closeup_smile_alt") with dissolve
            na "Thank you."
            na "Would you like to come on the expedition?"
            menu:
                "Accept [NadyaPath]" if True:
                    $ ep008_na_expedition = True
                    c "Of course, I'd be happy to."
                    na "Great, I'll let you know as soon as Caese contacts me."
                "Decline" if True:
                    c "I can't, I'm afraid."
                    scene expression eye_blink("images/ep008/ep008_na_closeup") with dissolve
                    na "No worries, it's going to be a lot of traipsing through the jungle anyway."
                    c "I thought as much."
                    c "Well, I hope you find those birds at some point anyway."
                    na "Yes, me too, here's to hoping Caese contacts me soon."
        "Rebuke her" if True:
            $ ep008_na_rebuke = True
            c "You seem to get easily carried away by stuff like this."
            c "I must admit that it disappoints me a little."
            scene expression eye_blink("images/ep008/ep008_na_closeup_sad") with dissolve
            na "I'm sorry, [p_name_short], I really don't want you to think I'm insensitive."
            na "I'm so glad we'll finally be able to meet her and that she seems healthy and unharmed, really I am."
            c "Thank you."
            c "Well, I hope you find those birds at some point."
            na "I do too."

    return

label ep008_aven_erigone_talk:
    scene ep008_av_bed with dissolve
    if ep008_l_talk:
        "Aven's quarters were notably more spacious than mine, something I'd noticed when visiting Lilly earlier."
    elif True:
        "Aven's quarters were notably more spacious than mine."
    c "How come you have a balcony?"
    scene expression eye_blink("images/ep008/ep008_av_bed_closeup") with dissolve
    av "You don't?"
    c "I've been assigned a bed and a chest to put my stuff in, that's it."
    av "Might have something to do with me being a woman."
    c "And being a part of the new royal family."
    scene expression eye_blink("images/ep008/ep008_av_bed_closeup_doubt") with dissolve
    av "So it's true, Eva is their leader?"
    c "The Virgin Queen, yes."
    av "You spoke to her?"
    c "She mostly spoke at me and I cried out her name once, quite dramatically, and then the audience was over."
    c "I'm hoping to get a second chance and speak to her privately."
    scene expression eye_blink("images/ep008/ep008_av_bed_closeup") with dissolve
    av "I hope you do."
    av "In the meantime, the sleeping arrangements don't seem too bad."
    c "They're also repairing our ship in one of their shipyards."
    scene expression eye_blink("images/ep008/ep008_av_bed_closeup_smile") with dissolve
    av "Really?{w} That's good news."
    av "So I guess we'll have to be patient."
    c "I guess so."
    if aven_romance:
        scene expression eye_blink("images/ep008/ep008_av_bed_closeup_smile_alt") with dissolve
        av "Why don't you join me on the balcony?"
        av "There's booze."
        c "Wait, you have booze as well?"
        c "What an outrage!"
        av "Yup, a fully stocked liquor cabinet."
        av "And the jungle air sure is lovely tonight."
        scene ep008_av_balcony with dissolve
        "Aven was right about the air out on the balcony, but I enjoyed it even more because she was so close to me."
        "The rustling of leaves mingled with the occasional rallying cries of unknown jungle-dwelling animals."
        "Because the Citadel was high upon the mountain, a vast expanse of stars could be seen above the canopy."
        scene expression eye_blink("images/ep008/ep008_av_bed_closeup_shy") with dissolve
        av "So...{w} The question is, will you return to your tiny bedroom tonight?"
        c "You know you're making it very hard for me to go back."
        av "Am I?"
        av "It's because of the booze, isn't it?"
        c "Mostly, yes."
        c "Though the fact that you're wearing nothing but that hot lingerie plays a small part as well."
        scene expression eye_blink("images/ep008/ep008_av_bed_closeup_smile_sexy") with dissolve
        av "Does it now?"
        c "Uh-huh."
        av "So you'd be very unhappy when I lose the bra and panties?"
        c "I can't say that I would, funnily enough."
        av "Oh?{w} You know, maybe we should go inside."
        c "Maybe we should."
        scene expression eye_blink("images/ep008/ep008_av_balcony_topless") with dissolve
        "While we were walking through the glass doors, Aven was already unfastening the clasp of her bra."
        scene expression eye_blink("images/ep008/ep008_av_balcony_topless_alt") with dissolve
        "She cast me a smouldering look as the garment fell to the floor."
        "The sexual energy almost crackled and I somehow knew that tonight we weren't going to hold back."
        scene ep008_av_balcony_embrace with dissolve
        "With one step I swept her up in an embrace."
        av "Make love to me, [p_name]."
        call ep008_av_sex from _call_ep008_av_sex
    return

label ep008_celine_talk:
    scene ep008_ce_courtyard with dissolve
    "Céline was looking out over the Citadel courtyard and enjoying the warm sun."
    "She smiled as I approached and motioned me to sit down next to her."
    scene expression eye_blink("images/ep008/ep008_ce") with dissolve
    ce "How’s Eva?"
    ce "Is she still the same?"
    c "It’s really hard to say."
    c "She played the queen when I met her."
    c "I’m not sure if it was feigned for the benefit of the Acarhyn surrounding her, or if she’s really, you know, their queen."
    scene expression eye_blink("images/ep008/ep008_ce_doubt") with dissolve
    ce "This is all so weird."
    c "No argument there."
    ce "I really hope we get to meet the real Eva again."
    c "So do I."
    c "I feel I just need to see her for one private moment."
    c "I’m sure the old Eva is right there beneath the surface."
    scene expression eye_blink("images/ep008/ep008_ce") with dissolve
    ce "I really hope you’re right."
    c "How are you holding up?"
    scene expression eye_blink("images/ep008/ep008_ce_serious") with dissolve
    ce "My head is still spinning from that crash landing."
    c "I’m very glad we’re still in one piece."
    c "Although the same can’t be said of the Bastard."
    ce "No, unfortunately not."
    scene expression eye_blink("images/ep008/ep008_ce_smile") with dissolve
    ce "Though there’s at least one benefit of being friends with the queen of these parts."
    c "Yeah, the repairs to the ship should already be underway."
    ce "Thyia has already been pestering their engineers."
    c "Good, I hope they can get her space-worthy again."
    scene expression eye_blink("images/ep008/ep008_ce") with dissolve
    ce "The Acarhyn seem to be quite capable mechanics, so I’m not worried."
    ce "Maybe they’ll improve some parts of the ship."
    c "We’re not on a budget, so I’ll tell Thyia to install a jacuzzi on the bridge."
    scene expression eye_blink("images/ep008/ep008_ce_smile") with dissolve
    ce "Cozy, yet so impractical."
    c "One can dream."
    scene expression eye_blink("images/ep008/ep008_ce_serious") with dissolve
    ce "Still, it’s fucked up we’re now relying on the people who got us into this mess in the first place."
    c "I get what you’re saying, though I feel we have little choice."
    ce "We don’t, but it’s still grating."
    ce "I know Kit is secretly having a hard time dealing with being surrounded by the women who nearly killed him."
    if ep008_ki_erigone_talk:
        c "I know, we talked about it."
        scene expression eye_blink("images/ep008/ep008_ce") with dissolve
        ce "Was that the reason for the midnight rampage you two were on?"
        c "You know about that?"
        scene expression eye_blink("images/ep008/ep008_ce_smile") with dissolve
        ce "Considering the noise you were making, who doesn’t?"
    elif True:
        c "Fuck, I didn’t realize, I’ll go talk to him soon."
        scene expression eye_blink("images/ep008/ep008_ce") with dissolve
        ce "Please do."
    return

label ep008_jade_talk:
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_j") with dissolve
    j "Mistress Eva is alive?"
    c "She is."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_j_smile") with dissolve
    j "I'm so glad to hear that."
    j "How did she look?"
    c "Regal is the word I think."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_j_doubt") with dissolve
    j "Regal?"
    c "Yes, Eva appears to have become the Queen of the Acarhyn."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_j") with dissolve
    j "The Virgin Queen..."
    c "Exactly."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_j_doubt") with dissolve
    j "I wonder how that happened."
    c "I intend to find out."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_j") with dissolve
    if ep007_j_injured:
        menu:
            "Ask about her injury [JadePath]" if True:
                $ ep008_j_concern = True
                c "How’s your injury?"
                scene expression eye_blink("images/ep008/ep008_erigone_quarters_j_smile") with dissolve
                j "A lot better!"
                j "The Acarhyn treated my wound while we were held prison."
                j "The restorative balm they used must have accelerated the healing process."
                c "I’m glad to see you up and about."
                c "Just be wary of the Acarhyn’s kindness, it might come at a price."
                scene expression eye_blink("images/ep008/ep008_erigone_quarters_j") with dissolve
            "Note lack of injury" if True:
                c "Seems you can perform your duties again?"
                j "I can, master."
                j "The Acarhyn treated my wound while we were held prison."
                j "The restorative balm they used must have accelerated the healing process."
                c "Good."
                c "Just don’t rely on the Acarhyn’s kindness too much, it might come at a price."

    j "Are we still prisoners?"
    c "No, we're not."
    c "We've been given permission to roam the castle grounds and use any of the facilities."
    j "There's supposed to be a bath."
    c "There is."
    j "I think I'm going to make use of it shortly."
    c "Enjoy yourself."
    return

label ep008_kit_erigone_talk:
    scene expression eye_blink("images/ep008/ep008_erigone_ki") with dissolve
    if game.is_special:
        ki "Fuck me, your sister is a queen?!"
    elif True:
        ki "Fuck me, our friend is a queen?!"
    c "It sure seems like it."
    ki "That’s just so weird."
    scene expression eye_blink("images/ep008/ep008_erigone_ki_doubt") with dissolve
    ki "They took her from Lanan to become their queen?"
    c "Maybe not her specifically, but something must have happened after she was kidnapped."
    c "Maybe they mistook her for someone else?"
    scene expression eye_blink("images/ep008/ep008_erigone_ki_serious") with dissolve
    ki "Could be."
    ki "I tried to ask around, but most of the Acarhyn don't seem to be in the mood for small talk."
    ki "It’s also a little weird, because us and Thim seem to be the only men in the palace."
    c "Now that you mention it, I haven’t seen any other men, apart from the prisoner down below."
    ki "Apparently most of the men live in the countryside."
    ki "From the few conversations I managed to strike up, it seems that the guy in the dungeon didn’t lie about men being sold as sex slaves."
    ki "They don’t call them slaves of course, just like Jade is your ‘attendant’..."
    c "You’re worried we’ll get auctioned off as well?"
    ki "Nah, I think we’re protected because of our connection with Eva."
    ki "Also, it’s been a long time since there was an auction."
    c "Well, I’m sure you’d fetch a high price."
    scene expression eye_blink("images/ep008/ep008_erigone_ki_grin") with dissolve
    ki "Naturally, I’d be the star stud in the Acarhyn fuck stable."
    c "Thanks, now I have to live with that mental image."
    scene ep008_erigone_ki_laugh with dissolve
    ki "You’re very welcome."
    c "But you’re chatting up the Acarhyn?"
    c "I thought you’d hate them for what they did to you."
    scene expression eye_blink("images/ep008/ep008_erigone_ki_serious") with dissolve
    ki "Make no mistake, I do hate them."
    ki "And I’d happily blow this whole palace up if I had the chance."
    ki "But what are we going to do against these overwhelming odds?"
    c "I get your point."
    scene expression eye_blink("images/ep008/ep008_erigone_ki") with dissolve
    ki "I’d say we learn as much as possible from them while they’re still semi-friendly."
    ki "A little bit of extra knowledge is always helpful."
    scene expression eye_blink("images/ep008/ep008_erigone_ki_serious") with dissolve
    ki "But if I ever met the one who stabbed me in the gut, I don’t know what I’d do."
    if ep008_commander_sex:
        menu:
            "Tell him about Athryn [KitPath]" if True:
                $ ep008_kit_truth = True
                c "So about that...{w} I met her."
                ki "Fuck."
                c "I didn’t know whether to tell you."
                c "She’s one of the guards that took us prisoner."
                scene expression eye_blink("images/ep008/ep008_erigone_ki_doubt") with dissolve
                ki "Really?{w} I don’t remember her."
                ki "Everything about Lanan is such a blur."
                ki "What did you do when you realized it was her?"
                if ep008_athryn_choke:
                    c "I nearly choked the life out of her."
                    scene expression eye_blink("images/ep008/ep008_erigone_ki_serious") with dissolve
                    ki "Serves her right!"
                elif True:
                    c "To be honest, I didn’t do anything."
                    scene expression eye_blink("images/ep008/ep008_erigone_ki_serious") with dissolve
                    ki "Yeah I don’t know what I would have done."
                ki "Fuck, I think I’m going to get drunk on this terrible beer they’re serving."
                c "I’ll join you."
                ki "Thanks."
                scene ep008_erigone_ki_drinking with dissolve
                "Kit and I got heavily drunk that night and remained in the dining hall after everyone had deserted the place."
                "I’m sure the Acarhyn were very annoyed by the bawdy songs and tall tales we sounded out loudly for everyone to hear."
                "We staggered back to our quarters, only to emerge with a throbbing hangover next morning."
            "Don’t tell him" if True:

                c "Choke the life out of her?"
                scene expression eye_blink("images/ep008/ep008_erigone_ki_doubt") with dissolve
                ki "Maybe..."
                scene expression eye_blink("images/ep008/ep008_erigone_ki_serious") with dissolve
                ki "Fuck."
                ki "That’s a dark place to go to."
                ki "I think I’m just going to enjoy this terrible beer they’re serving."
                c "In that case, enjoy!"
    elif True:
        c "Choke the life out of her?"
        scene expression eye_blink("images/ep008/ep008_erigone_ki_doubt") with dissolve
        ki "Maybe..."
        scene expression eye_blink("images/ep008/ep008_erigone_ki_serious") with dissolve
        ki "Fuck."
        ki "That’s a dark place to go to."
        ki "I think I’m just going to enjoy this terrible beer they’re serving."
        c "In that case, enjoy!"
    return

label ep008_ziv_talk:
    scene ep008_ziv with dissolve
    c "Enjoying the view?"
    scene expression eye_blink("images/ep008/ep008_ziv_alt") with dissolve
    zi "It has a strange kind of beauty to it."
    c "All of the spaceship wreckage really complements the vastness of the jungle."
    zi "Something like that."
    zi "It sure is a strange place."
    zi "You'd think a culture like this would never be able to sustain itself and yet they have done marvellously well by the looks of it."
    c "I think their genetics gave them an advantage."
    zi "Probably."
    zi "But the level of engineering sophistication combined with their obsession for martial culture is really peculiar."
    scene expression eye_blink("images/ep008/ep008_ziv_alt_sigh") with dissolve
    "Ziv looked out over the treetops and sighed."
    scene expression eye_blink("images/ep008/ep008_ziv_alt") with dissolve
    zi "I've been meaning to talk to you."
    c "You have?"
    zi "Yes, but of course all kinds of events intervened."
    if ep006_raene_accept and ep006_ra_comfort:
        scene expression eye_blink("images/ep008/ep008_ziv_alt_smile") with dissolve
        zi "I just wanted to say that you surprise me, [p_name]."
        c "Thanks, I guess?"
        zi "Oh, I don't mean it in a negative way."
        zi "I just want you to know that I really appreciate the way you've treated Raene so far."
        zi "She's been bravely undergoing the treatment, but I've seen her grow more confident since we've joined the crew."
        zi "And I think you had some part in building her confidence."
        c "After all she's suffered through, I think she deserves some happiness and a life of her own."
        scene expression eye_blink("images/ep008/ep008_ziv_alt_serious") with dissolve
        zi "Exactly."
        zi "I'm glad I'm able to at least contribute some small part to that, but it's good to see others doing the same."
        zi "A kind word, a shoulder to lean on, all those things, however small, are very important."
        scene expression eye_blink("images/ep008/ep008_ziv_alt_look") with dissolve
        "Ziv smiled at me and looked out over the jungle again."
        scene expression eye_blink("images/ep008/ep008_ziv_alt_smile") with dissolve
        zi "It seems we'll be here on Erigone for the time being."
        c "Yes, I think so."
    elif ((ep004_ra_confront_angry + ep004_ra_doubt + ep004_ra_angry + ep005_ra_intimidate + ep006_ra_berate + ep006_ra_ignore) > 1) or ep004_ziv_impolite:
        scene expression eye_blink("images/ep008/ep008_ziv_alt_serious") with dissolve
        zi "You don't particularly like us, do you?"
        c "Who, the Rhenkoy?"
        zi "Well, I was thinking more of Raene and me."
        c "Oh."
        menu:
            "Confirm [red]\[Closes Ziv and Raene Paths\]" if True:
                $ ep008_ziv_dislike = True
                c "Well, in all honesty, I don't think we're going to be the best of friends."
                c "That doesn't mean you can't be part of the crew though."
                zi "Thank you for your honesty."
                zi "I feel the same way."

                if (ep004_ra_confront_angry + ep004_ra_doubt + ep004_ra_angry + ep005_ra_intimidate + ep006_ra_berate + ep006_ra_ignore) > 1:
                    scene expression eye_blink("images/ep008/ep008_ziv_alt_angry") with dissolve
                    zi "Though I think the way you've treated Raene is just appalling."
                    c "You're entitled to that opinion, but I hope you're not offended when I say that I just don't care."
                    zi "I thought as much."
                    zi "Yes, I think you're very right, we're never going to be the best of friends."
                zi "Well, we won't be in your way then."
                scene expression eye_blink("images/ep008/ep008_ziv_alt_sigh") with dissolve
                "Ziv sighed and looked out over the jungle again, effectively ignoring me."
                return
            "Deny" if True:
                c "I have zero problems with both of you."
                zi "That surprises me."
                c "How so?"

                if (ep004_ra_confront_angry + ep004_ra_doubt + ep004_ra_angry + ep005_ra_intimidate + ep006_ra_berate + ep006_ra_ignore) > 1:
                    scene expression eye_blink("images/ep008/ep008_ziv_alt_doubt") with dissolve
                    zi "Your behavior towards Raene has been strange at best."
                    zi "Not very mindful of her feelings."
                    c "Raene is a complete cipher to me."
                    c "All those layers of shyness..."
                    zi "It frustrates you?"
                    c "It does."
                    scene expression eye_blink("images/ep008/ep008_ziv_alt_serious") with dissolve
                    zi "I don't know if Raene will ever lose her shy nature and she certainly doesn't need to."
                    zi "So the question is, will you be able to live with that?"
                    c "Of course..."
                elif ep004_ziv_impolite:
                    scene expression eye_blink("images/ep008/ep008_ziv_alt_angry") with dissolve
                    zi "From the way you’ve dealt with me, it’s clear you don’t particularly care if you hurt someone’s feelings."
                    c "Maybe, but it’s how I deal with everyone."
                    scene expression eye_blink("images/ep008/ep008_ziv_alt_doubt") with dissolve
                    zi "Maybe..."
                elif True:
                    scene expression eye_blink("images/ep008/ep008_ziv_alt_doubt") with dissolve
                    zi "It's hard to put into words, but you seem less aloof with the other members of the crew."

                if not ep004_ziv_impolite:
                    scene expression eye_blink("images/ep008/ep008_ziv_alt_serious") with dissolve
                    zi "Do you have any problems with me?"
                    zi "Some species can't deal with the nature of our dual sexuality or even with Raene being a trans girl."

                    menu:
                        "Remain neutral [red]\[Closes Ziv and Raene Paths\]" if True:
                            $ ep008_ziv_neutral = True
                            c "I have no particular opinion on that to be honest."
                            scene expression eye_blink("images/ep008/ep008_ziv_alt_doubt") with dissolve
                            zi "I see."
                            zi "Well, nevertheless, I hope there won't be any friction between us."
                            c "I'm sure there won't be."
                            zi "If you say so."
                            scene expression eye_blink("images/ep008/ep008_ziv_alt_sigh") with dissolve
                            "Feeling there wasn't much else to say, I left Ziv as she stared out over the jungle again."
                            return
                        "Don't mind [gr]\[Ziv and Raene Paths\]" if True:
                            $ ep008_ziv_accept = True
                            c "I don't have any problems at all with either your sexuality or Raene's gender."
                            c "It's simply who you are, nothing more."
                            scene expression eye_blink("images/ep008/ep008_ziv_alt_smile") with dissolve
                            zi "I'm glad you feel that way."
                        "Don't like it [red]\[Closes Ziv and Raene Paths\]" if True:
                            c "Well, I must admit that your sexuality is something very foreign."
                            c "Raene's gender is also hard to wrap my mind around."
                            scene expression eye_blink("images/ep008/ep008_ziv_alt_angry") with dissolve
                            zi "I see."
                            zi "Well, in that case I hope your inability to cope with either of our genders won't cause any friction between us."
                            c "I'm sure it won't."
                            zi "If you say so."
                            scene expression eye_blink("images/ep008/ep008_ziv_alt_sigh") with dissolve
                            "Feeling there wasn't much else to say, I left Ziv as she stared out over the jungle again."
                            return
                        "Don't like Raene [red]\[Closes Raene Path\]" if True:
                            $ ep008_raene_dislike = True
                            c "Well, in all honesty, I don't think me and Raene are going to be the best of friends."
                            c "We're too different."
                            scene expression eye_blink("images/ep008/ep008_ziv_alt_doubt") with dissolve
                            zi "In what way?"
                            c "Raene is a complete cipher to me."
                            c "All those layers of shyness..."
                            zi "It frustrates you?"
                            c "It does."
                            scene expression eye_blink("images/ep008/ep008_ziv_alt_serious") with dissolve
                            zi "I don't know if Raene will ever lose her shy nature and she certainly doesn't need to."
                            zi "So the question is, will you be able to live with that?"
                            c "Of course...{w} I just think we won't be friends."
                            c "Nothing wrong with that, right?"
                            zi "I guess not."
                elif True:
                    zi "Nevertheless, I hope there won't be any friction between us."
                    c "I'm sure there won't be."
                    scene expression eye_blink("images/ep008/ep008_ziv_alt_doubt") with dissolve
                    zi "If you say so."
                    scene expression eye_blink("images/ep008/ep008_ziv_alt_sigh") with dissolve
                    "Feeling there wasn't much else to say, I left Ziv as she stared out over the jungle again."
                    return

    menu:
        "Tell Ziv you like her [ZivPath]" if not ep004_ziv_impolite:
            $ ep008_ziv_like = True
            c "Though I must admit I'm sorry we haven't spent more time getting to know each other."
            c "There always seems to be a new crisis to deal with."
            zi "You can say that again."
            scene expression eye_blink("images/ep008/ep008_ziv_alt") with dissolve
            if not ep006_raene_accept and not ep006_ra_comfort:
                zi "Though we'll be here on Erigone for the time being, it seems."
                c "Yes I think so."
            c "So, considering we have all this free time on our hands, let’s do something together in the coming days."
            scene expression eye_blink("images/ep008/ep008_ziv_alt_smile") with dissolve
            zi "I’d like that."
            c "Good, maybe we could explore that jungle together."
            c "See you around, Ziv."
            zi "You too, [p_name]."
        "Leave her" if True:
            c "Was there anything else you wanted to talk about?"
            scene expression eye_blink("images/ep008/ep008_ziv_alt_serious") with dissolve
            zi "No, not really."
            zi "Thank you for taking the time though."
            c "No worries."
            scene expression eye_blink("images/ep008/ep008_ziv_alt_sigh") with dissolve
            "Feeling there wasn't much else to say, I left Ziv as she stared out over the jungle again."
    return

label ep008_raene_talk:
    scene ep008_ra with dissolve
    "I found Raene sitting alone in the spacious dining hall of the castle."
    scene expression eye_blink("images/ep008/ep008_ra_closeup") with dissolve
    ra "Hey [p_name_short]!"
    c "Hey there, you sound positively cheerful."
    scene expression eye_blink("images/ep008/ep008_ra_closeup_doubt") with dissolve
    ra "Am I?"
    c "Yes, you look the part too."
    scene expression eye_blink("images/ep008/ep008_ra_closeup_shy") with dissolve
    ra "I went into the shower just now..."
    ra "..."
    scene expression eye_blink("images/ep008/ep008_ra_closeup_doubt") with dissolve
    ra "Sorry, but I'm sure you don't want to hear about this..."
    c "I'm sure I do want to."
    scene expression eye_blink("images/ep008/ep008_ra_closeup_surprise") with dissolve
    ra "Really?"
    c "Raene...{w} How many times do I need to repeat it?"
    scene expression eye_blink("images/ep008/ep008_ra_closeup_smile") with dissolve
    ra "Alright, I hear you."
    ra "So I went into the shower and looked at my reflection."
    ra "And for the first time I really saw a part myself shining through, my true self."
    scene expression eye_blink("images/ep008/ep008_ra_closeup_doubt") with dissolve
    ra "Pfff, it sounds so pretentious when I say it out loud."
    c "No, it doesn't."
    scene expression eye_blink("images/ep008/ep008_ra_closeup_serious") with dissolve
    ra "I knew the injections Ziv has been giving me were working."
    ra "Slowly, but still."
    ra "First I noticed that my body lost some of its angular lines."
    ra "And then nothing else happened, or so it seemed."
    ra "The changes are still small, but my bust is finally starting to develop."
    scene expression eye_blink("images/ep008/ep008_ra_closeup_smile") with dissolve
    ra "It's really going to work out like I hoped."
    c "I'm happy for you, Raene."
    c "You deserve this and more."
    scene expression eye_blink("images/ep008/ep008_ra_closeup") with dissolve
    ra "Thank you!"
    menu:
        "Invite her to the baths [RaenePath]" if True:
            $ ep008_raene_baths = True
            c "We should celebrate."
            c "There are baths here in the castle and we're welcome to use them."
            scene expression eye_blink("images/ep008/ep008_ra_closeup_surprise") with dissolve
            ra "You're asking me to go to the baths with you."
            c "I am."
            c "There's a steam bath and they even do massages."
            scene expression eye_blink("images/ep008/ep008_ra_closeup_fear") with dissolve
            ra "But everyone will see me..."
            c "That's kind of the point."
            scene expression eye_blink("images/ep008/ep008_ra_closeup_serious") with dissolve
            ra "Okay, but I don't have any swimwear."
            c "I'm going to take care of that, don't worry."
            c "So, do we have a date?"
            scene expression eye_blink("images/ep008/ep008_ra_closeup_serious") with dissolve
            ra "I think so...{w} yes...{w} we do!"
            "Raene was both happy and a little confused when I left her."
            scene expression eye_blink("images/ep008/ep008_ra_closeup_smile") with dissolve
            "I went straight to the courtyard of the castle where several market stalls and tents were pitched."
            scene ep008_market with dissolve
            "One of the stalls was owned by a tailor, specializing in the utilitarian brand of fashion most Acarhyn seemed to fancy."
            scene ep008_market_stall with dissolve
            "With some effort, I was able to convince the woman to create a set of delicate swimwear for me."
            "The garments would be finished in two days and I just hoped I'd guessed Raene's measurements correctly."
        "Leave her" if True:
            c "Take care, Raene."
            scene expression eye_blink("images/ep008/ep008_ra_closeup_smile") with dissolve
            ra "You too, [p_name]."
    return

label ep008_raene_baths:
    scene ep008_market_alt with dissolve
    "The tailor messaged me one day early to tell me she'd completed my order."
    "After collecting the wrapped package at the market, I decided to surprise Raene."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra") with dissolve
    ra "Oh, hey [p_name_short]!"
    c "Hey Raene, are you ready to go?"
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_doubt") with dissolve
    ra "Ready?"
    c "Don't tell me you've forgotten our visit to the baths."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_fear") with dissolve
    ra "Oh...{w} no...{w} but I don't have any clothes."
    c "I told you I'd take care of that."
    c "Here you go."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_doubt") with dissolve
    ra "Thank you."
    scene ep008_erigone_quarters_ra_gift with dissolve
    "I could tell Raene was very much on edge and I sincerely hoped she would appreciate my gift."
    "Instead of tearing through the wrap, she very carefully unwrapped the paper, prolonging the tension both of us felt."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_shock") with dissolve
    "When she finally held the bikini, her face became a flurry of emotions, alternating between shock and delight."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_smile") with dissolve
    ra "It's such a beautiful gift, [p_name]."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_doubt") with dissolve
    ra "But I really can't wear this."
    c "You're welcome, of course, but why can't you wear it?"
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_fear") with dissolve
    ra "People might see me."
    c "That's kind of the point."
    c "You told me you were so happy with all the changes that were happening."
    c "So I asked the tailor at the market to create something that would accentuate the shape your body is slowly taking on."
    c "I hope it fits you."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_smile") with dissolve
    ra "Maybe I could try it on here in my room."
    c "Whatever makes you feel comfortable."
    c "Should I leave?"
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_serious") with dissolve
    ra "No, stay, I do want you to see it."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_sad") with dissolve
    ra "I sounded too ungrateful just now, didn't I?"
    c "Raene...{w} Why aren't you already changing clothes in the next room?"
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_doubt") with dissolve
    ra "Right.{w} Right.{w} I shouldn't fret so much. I-"
    c "Raene!"
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_smile") with dissolve
    ra "I'm going!{w} I'm going!"
    "She smiled as she stepped out of the room to get changed."
    "A few minutes later she returned."
    scene ep008_erigone_quarters_ra_clothes:
        yalign 1.0
        ease 8 yalign 0.01
    $ renpy.pause()
    "To my relief, the bikini bottom and top both fit perfectly."
    "The seamstress had done a great job based on my description."
    "Never before had Raene shown so much skin to me, always favoring the tight-fitting stiff harness that didn't do much to grace her figure."
    "Still, I could see the many small changes the treatment had wrought upon her body."
    "The lines of her face had softened, as had her shoulders."
    "Her hips were rounding out, changing her poise ever so slightly."
    "Raene cast me a very shy smile and looked as if she'd dart out to the side room again at any moment."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_clothes_fear") with dissolve
    ra "So, what do you think?"
    c "I think you look absolutely perfect."
    ra "You do?"
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_clothes_doubt") with dissolve
    ra "You don't have to be kind, just tell me the truth."
    c "Raene...{w} I just did."
    c "So, how about a swim?"
    "I could tell she was torn between assent and declining my invitation."
    c "We'll bring towels and if it all becomes too uncomfortable you drape yourself in one of them and we'll leave."
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_clothes_serious") with dissolve
    ra "Okay."
    c "Okay?"
    scene expression eye_blink("images/ep008/ep008_erigone_quarters_ra_clothes_smile") with dissolve
    ra "Yes, let's do it."
    "Raene quickly changed again in the side room and we found our way through the many corridors of the Citadel."
    scene ep008_baths_ra with dissolve
    "The baths were empty, much to Raene's relief."
    "At the far end of the room there were two privacy screens which allowed us to change into our swimwear."
    scene expression eye_blink("images/ep008/ep008_baths_ra_alt") with dissolve
    "I was already testing the temperature of the water when Raene emerged from behind the screen."
    scene expression eye_blink("images/ep008/ep008_baths_ra_closeup") with dissolve
    ra "Is the water cold?"
    c "I don't think so, but there's only one way to find out."
    "I slipped into the water, which turned out to be comfortably warm."
    "Raene followed me soon after."
    scene ep008_baths_ra_water with dissolve
    ra "Ooh, it's actually very nice and warm."
    scene ep008_baths_ra_water_alt with dissolve
    "Raene floated next to me and closed her eyes, luxuriating in the comfortable warmth of the water."
    "I did the same, enjoying the moment in silence, except for the occasional splash caused by a moving limb."
    scene expression eye_blink("images/ep008/ep008_baths_ra_water_closeup") with dissolve
    ra "I'd almost forgotten how wholesome a bath can feel."
    ra "I always relished the thought of coming back to a steaming tub after going on a horse-ride on Verdigris."
    c "You did that a lot, horseriding?"
    scene expression eye_blink("images/ep008/ep008_baths_ra_water_closeup_smile") with dissolve
    ra "I did."
    ra "It was one of the few possibilities where I could escape home, more or less."
    c "Must have felt free, didn't it?"
    ra "It sure did."
    c "Were they real horses, by the way?"
    scene expression eye_blink("images/ep008/ep008_baths_ra_water_closeup") with dissolve
    ra "No, high quality artificial ones."
    ra "I mean the Church is filthy rich, but not that rich."
    c "Maybe the original pilgrims took a few real animals with them on one of the Migrations."
    ra "I wish."
    scene expression eye_blink("images/ep008/ep008_baths_ra_water_closeup_smile") with dissolve
    ra "Are you able to ride?"
    c "I've had some lessons, so I'd probably wouldn't embarrass myself too much."
    ra "Maybe I can help you brush up on your skills here on Erigone."
    c "The Acarhyn breed horses?"
    scene expression eye_blink("images/ep008/ep008_baths_ra_water_closeup_doubt") with dissolve
    ra "I think I saw stables bordering the courtyard."
    c "It makes sense actually, considering their devotion to the whole Medieval thing."
    scene expression eye_blink("images/ep008/ep008_baths_ra_water_closeup") with dissolve
    ra "Right, I had a few books on Medieval knights back on Verdigris."
    c "Well, as long as we don't get mixed up in some weird jousting tournament, I'd be willing to check out those stables together with you."
    scene expression eye_blink("images/ep008/ep008_baths_ra_water_closeup_smile") with dissolve
    ra "I'd like that."
    scene ep008_baths_ra_women_alt with dissolve
    "Two women entered the baths and the tenseness that came over Raene was instantly visible."
    c "Good day ladies, the water is lovely."
    $ woman_name = "Acarhyn"
    scene ep008_baths_ra_women with dissolve
    woman "We’re eager to join you."
    "My attempt to act casual and defuse the situation didn't work."
    scene ep008_baths_ra_women_shock with vpunch
    "Raene watched the women enter the water with a fearful look in her eyes."
    c "There's nothing to worry about, Raene."
    "Raene was already inching towards the steps of the pool."
    scene ep008_baths_ra_water_women_run with dissolve
    "As soon as the women splashed around in the water she exited the bath and darted towards the safety of the privacy screens."
    scene ep008_baths_ra_water_women_alone with dissolve
    woman "Is your girlfriend okay?"
    c "I'll go check on her."
    scene expression eye_blink("images/ep008/ep008_baths_ra_screens") with vpunch
    "Raene was already putting on her clothes when I reached her."
    ra "It's been lovely, it really has been, but I really need to get back to my quarters."
    ra "Thank you for the company and for the gift."
    scene ep008_baths_ra_walk with dissolve
    "Before I could get a word in edgewise, she was already heading for the exit."
    "I didn't want to cause a scene and upset Raene even further by calling out to her."
    scene ep008_baths_j_ra with dissolve
    "Just as Raene was leaving the baths, she passed Jade."
    j "Hey Raene."
    ra "Hey."
    scene expression eye_blink("images/ep008/ep008_baths_j") with dissolve
    "A little puzzled, Jade walked towards me, largely ignoring the naked Acarhyn in the pool."
    scene expression eye_blink("images/ep008/ep008_baths_j_closeup") with dissolve
    if (ep003_jade_curt + ep004_jade_dom + ep005_jade_punish + ep007_j_rude) > 2:
        j "Is she okay, master?"
    elif True:
        j "Is she okay, [p_name_short]?"
    c "I think so."
    c "The women just startled her, I guess."
    scene expression eye_blink("images/ep008/ep008_baths_j_closeup_doubt") with dissolve
    j "Because they were playing with each other's breasts?"
    c "What?"
    c "Oh...{w} No, that's new."
    scene ep008_baths_kiss with dissolve
    "The women obviously thought they were now alone, or didn't care that anyone saw them."
    "One of the Acarhyn was sucking on the hard nipples of the other woman leaning on the edge of the pool."
    scene expression eye_blink("images/ep008/ep008_baths_j_closeup_smile") with dissolve
    j "Do you want to leave them to it, or enjoy the show?"
    menu:
        "Stay in the baths [JadePath]" if True:
            c "It would be rude to interrupt them..."
            j "Very."
            call ep008_jade_sex from _call_ep008_jade_sex
        "Leave the baths" if True:
            c "Better leave, this could lead to problems."
            j "Of course."
            scene ep008_baths_exit with dissolve
            "The women didn’t even notice us and continued their lovemaking when we walked past them towards the exit."
    return

label ep008_j_baths:
    "Jade had asked me to join her in the communal baths she had visited regularly since our arrival at the Citadel."
    "Curious about what drew her to the place, I ventured to the baths."
    scene ep008_baths_women with dissolve
    "I must admit the two naked women frolicking around in the baths startled me a little."
    "Intrigued, I made my way to the changing area at the far end of the room. "
    scene ep008_baths_j_alt with dissolve
    "Jade entered the pool a short while after I arrived and glanced at the women while walking towards me."
    scene expression eye_blink("images/ep008/ep008_baths_j_closeup") with dissolve
    j "It seems we have some company."
    c "We do."
    scene expression eye_blink("images/ep008/ep008_baths_j_closeup_doubt") with dissolve
    j "Have they been playing with each other's breasts all the time you were here?"
    c "What?"
    c "Oh...{w} No, that's new."
    scene ep008_baths_kiss with dissolve
    "The women obviously thought they were now alone, or didn't care that anyone saw them."
    "One of the Acarhyn was sucking on the hard nipples of the other woman leaning on the edge of the pool."
    scene expression eye_blink("images/ep008/ep008_baths_j_closeup_smile") with dissolve
    j "Do you want to leave them to it, or enjoy the show?"
    menu:
        "Stay in the baths [JadePath]" if True:
            c "It would be rude to interrupt them..."
            j "Very."
            call ep008_jade_sex from _call_ep008_jade_sex_1
        "Leave the baths" if True:
            c "Better leave, this could lead to problems."
            j "Of course."
            scene ep008_baths_exit with dissolve
            "The women didn’t even notice us and continued their lovemaking when we walked past them towards the exit."
    return

label ep008_av_sex:
    if _in_replay:
        $ av_name = "Aven"

    scene ep008_av_naked with dissolve
    "Aven slipped out of her panties and made herself comfortable on the bed, while I busied myself with getting out of my clothes as fast as possible."
    if game.is_special:
        "My cock was already hardening when I looked at my beautiful cousin, waiting for me to share her bed."
    elif True:
        "My cock was already hardening when I looked at my beautiful girlfriend, waiting for me to share her bed."
    scene ep008_av_finger with dissolve
    "She shivered as my lips caressed her breastbone, my fingers tiptoeing over her thighs towards her groin."
    "With a heavy sigh, Aven opened her legs further."
    scene ep008_av_finger_alt with dissolve
    "Her pussy glistened wet and I felt her moisture cling to my fingertips as I pressed them against her pussy."
    av "Oh [p_name_short]!"
    scene ep008_av_finger_closeup with dissolve
    "With some effort, Aven pulled my face towards hers and she looked at me longingly."
    if is_patreon() and renpy.has_label("extra_scene_16") and not _in_replay:
        call extra_scene_16 from _call_extra_scene_16
    elif True:
        av "Could we...{w} Just skip all that?"
        av "I just really want you inside of me."
    "I could tell she was a little embarrassed by her own request, but it turned my arousal up several notches."
    scene ep008_av_sex_penetrate with dissolve
    "Grinning, I grabbed her legs and pulled her towards me."
    "She let out a surprised cry and giggled as my cock slapped against her abdomen."
    scene ep008_av_sex_penetrate_closeup with dissolve
    av "I’m ready!"
    "Her obvious nervousness made her vulnerable and adorable at the same time."
    "I suddenly knew I’d have to be gentle with her."
    scene ep008_av_sex_penetrate_alt with dissolve
    "Her lower lips parted when I pressed the tip of my cock against her entrance."
    "Very slowly I entered her."
    scene ep008_av_sex_penetrate_alt_closeup with dissolve
    "Aven’s expression was pained at first, her eyes closed and her fists clenched."
    "Her tight pussy felt amazing, but I hesitated at inserting the last few inches of my girth."
    av "Don’t stop, please don’t stop now!"
    scene ep008_av_sex_penetrate_alt_closeup_pleasure with dissolve
    "When I made the final push and Aven’s eyes fluttered open and a smile suddenly graced her face."
    av "Oh, that’s it!"
    av "That feels so good."
    av "Make love to me, [p_name_short]!"
    show ep008_av_sex with dissolve
    "She folded her legs across my lower back, locking me into our intimate embrace."
    "I began to move, very slowly at first."
    "My cock was drenched in her moisture by now and made my passage through her ribbed tunnel extra pleasurable."
    show ep008_av_sex_closeup with dissolve
    av "You’re so deep inside me!"
    av "Keep going, please don’t stop now."
    "Her comments encouraged me to pick up the pace a little."
    "She held me tight as I plunged in and out of her wet slit with increasing intensity."
    scene ep008_av_sex_alt with dissolve
    av "Keep fucking me like that."
    av "Your cock feels so good."
    scene ep008_av_fucking with dissolve
    "By now we were fucking so fiercely that Aven had to draw up her legs even further."
    "My balls slapped against her cunt when my cock buried itself deeply inside her vagina."
    scene ep008_av_fucking_alt with dissolve
    "Her breathing was ragged as I worked her up into a carnal frenzy."
    "My shaft, covered in her juices, stabbed her pussy in quick succession causing Aven to cry out in rapture."
    av "I...{w} I...{w} I..."
    scene ep008_av_fucking_orgasm with vpunch
    "Before she could even form the words of a sentence, Aven orgasmed massively."
    "Her body shook and thrashed beneath me and her fingers raked fitfully through my hair."
    "When her climax subsided into small tremors and less violent convulsions, she was finally able to whisper."
    av "I love you."
    scene ep008_av_fucking_kiss with dissolve
    "I kissed her in response."
    "We embraced tightly and my cock slipped out of her warm pussy, but I didn’t mind because my lips on hers was all that mattered."
    scene ep008_av_fucking_kiss_alt with dissolve
    "Aven turned on her side with me behind her."
    "As she opened her legs again I prepared to enter her cunt from behind."
    "Her soft ass was pressing against my abdomen and I cupped her face in my hands."
    show ep008_av_sex_side with dissolve
    "She let out a long moan when my cock slid inside of her."
    av "Don’t hold back now."
    av "I want to feel all of you!"
    show ep008_av_sex_side_alt with dissolve
    "The final stretch didn’t take long, I was already near my climax when I’d entered her again."
    scene ep008_av_sex_side_closeup with dissolve
    av "Keep going, just like that!{w} Oh!{w} Just like that!"

    menu:
        "Creampie [gr]\[Aven Creampie\]" if True:
            $ ep008_av_creampie = True
            av "Please [p_name_short], I don’t want you to pull out!"
            av "Just cum inside me."
            show ep008_av_sex_side_alt with vpunch
            "I fulfilled her wish right after when a wealth of cum pulsed inside her vagina."
            scene ep008_av_sex_side_creampie with flash
            with flash
            "Semen oozed out of her wet pussy as soon as my cock slipped out of her, spurting some stray droplets of cum on her body."
        "Body" if True:
            av "Please [p_name_short], I want it all over my body!"
            scene ep008_av_sex_side_body with flash
            with flash
            "I fulfilled her wish right after when I pulled out and sprayed a wealth of cum on her belly and lower chest."
    scene ep008_av_sex_post with dissolve
    "Completely spent, I held her in my arms as we both drifted away in a sweet postcoital sleep."
    $ renpy.end_replay()
    return

label ep008_jade_sex:
    if _in_replay:
        $ ep005_jade_punish = False
        $ ep004_jade_dom = False
        $ ep004_jade_apologize = True

    scene ep008_baths_j_spy with dissolve
    "Jade looked intently at the women on the other side of the room."
    "One of them had left the water and kissed her friend."
    "Their moans echoed throughout the pool chamber."
    scene ep008_baths_j_spy_closeup with dissolve
    "The woman with the facial tattoos lifted herself half out of the water to receive the violent kisses of her partner."
    "While we both spied on the women, Jade had inched closer towards me and pressed her hand against my pants."
    "She was already topless and her panties also fell to the floor pretty quickly."
    scene ep008_baths_j_spy_closeup_alt with dissolve
    j "You really are enjoying the show!"
    scene ep008_baths_j_spy_lick with dissolve
    "The short-haired woman now lay on the side of the pool with the other girl between her legs."
    "Jade rubbed my cock through the fabric of my pants at the same rhythm as the girl’s pussy was being licked."
    "She quickly undressed me and went down on her knees."
    show ep008_jade_suck with dissolve
    "Her lips enveloped my cock and she started to suck."
    "While Jade was working on my cock, I could still see what the women in the pool were up to."
    scene ep008_baths_j_spy_lick_alt with dissolve
    "The short-haired girl was on her knees, offering her ass to the tattooed woman, who hungrily licked the moist lips pushed into her face."
    scene ep008_baths_j_spy_lick_wide with dissolve
    "Jade and I were trying to be silent, but the women had no such qualms and moaned loudly."
    show ep008_jade_suck_alt with dissolve
    "I’m sure that if they weren’t so preoccupied, they would have heard Jade behind the privacy screen, gagging softly on my cock as it hit the back of her throat."
    "Jade had made a beautiful mess of her face and my cock, strings of her saliva clinging to my cock and her lips."
    show ep008_jade_sex with dissolve
    "I made her stand upright and hooked a leg under my arm."
    "Cradling her ass cheeks, I slid my wet cock inside her equally wet pussy."
    j "Oh yes!"
    scene ep008_jade_sex_wide with dissolve
    "Jade quickly stifled any further outcries and instead whispered inside my ear."
    if ep005_jade_punish and ep004_jade_dom and not ep004_jade_apologize:
        j "Please fuck me hard, master."
    elif True:
        j "Please fuck me hard, [p_name_short]."
    j "I want all of it inside me."
    j "Take me.{w} Take me hard."
    show ep008_jade_sex_alt with dissolve
    "I lost track of the women as Jade’s pussy put me under a spell of pure lust."
    "In that moment, nothing else but my hard cock penetrating her tight warm slit existed."
    "Jade gasped for air every time my dick hit her deep and she clenched her teeth to avoid crying out in pleasure."
    scene ep008_baths_j_spy_lick_closeup_pussy with dissolve
    "When I came back to my senses somewhat, I noticed that the women were still entangled in the same way."
    "The short-haired woman was writhing on the floor, a slave to the stimulation of her friend’s tongue."
    scene ep008_baths_j_spy_lick_closeup with vpunch
    "She drooled on the tile floor and opened her mouth to let out a long and husky cry of pleasure."
    "The girl started to shudder and nearly slid back into the pool, but her friend kept her firmly in place, her face still pressed against her convulsing pussy."
    scene ep008_jade_fuck with dissolve
    "I pressed Jade against the privacy screen and entered her cunt from behind."
    scene ep008_jade_fuck_closeup with dissolve
    j "Fuck me master, fuck me hard, please!"
    scene ep008_jade_fuck with dissolve
    "Grabbing her flanks I pressed her against me in order to root my cock even deeper inside her cunt."
    "I’d lost interest in the women in the pool, who were still making love."
    scene ep008_jade_fuck_alt with dissolve
    "All my attention was on Jade, on possessing her body completely."
    "The privacy screen nearly toppled over because of the violence of my thrusts."
    "I knew I was close."
    scene ep008_jade_fuck_closeup with dissolve
    "Jade noticed my struggle and she started whispering in my ear again."

    menu:
        "Creampie [gr]\[Jade Creampie\]" if True:
            $ ep008_j_creampie = True
            j "Please don’t pull out."
            j "I want all of your cum inside me."
            j "Please!{w} Please!"
            with vpunch
            "With a heavy grunt I blasted her vagina full of warm cum."
            scene ep008_jade_fuck_creampie with flash
            with flash
            "When my cock slipped from her gash, a flood of semen started dripping out of her, coating her thighs."
        "Body" if True:
            j "Please, cover me in your cum."
            j "I want all of it on my body."
            j "Please!{w} Please!"
            scene ep008_jade_fuck_body with flash
            with flash
            "With a heavy grunt I sprayed her back with strands of warm cum, nearly hitting her shoulder blades."
        "Facial" if True:
            j "Please, paste my face with your cum."
            j "I want to taste it."
            j "Please!{w} Please!"
            "She went back on her knees and took my twitching cock."
            scene ep008_jade_fuck_facial with flash
            with flash
            "I sprayed her face with warm cum and coated her hands."
            "Jade licked her fingers in appreciation."
    scene expression eye_blink("images/ep008/ep008_jade_fuck_post") with dissolve
    j "Thank you, this has been the best visit to the baths yet."
    "We put on our clothing and emerged from behind the privacy screen."
    scene ep008_jade_fuck_post_women with dissolve
    "The women didn’t notice us immediately, but when they did they both looked at us defiantly."
    "Both Jade and I just smiled knowingly and walked out of the bath chamber."
    $ renpy.end_replay()
    return

label ep008_commander:
    scene ep008_commander_table with dissolve
    "I was about to leave the dining hall when the commander of the Acarhyn caught my eye."
    "She waved me over to her table."
    scene expression eye_blink("images/ep008/ep008_commander") with dissolve
    rah "[p_name]."
    c "Commander."
    rah "Please no need for formalities, call me Rahia."
    $ warrior_name = "Rahia"

    python:
        codex_rahia = add_codex_entry(
            Codex,
            __("Characters"),
            __("Rahia"),
            [
                __("The commander of the warrior caste of the Acarhyn. She led the attack on Lanan P-10 during which Eva was kidnapped.")
            ],
            "images/codex/Rahia.webp"
        )

    scene expression eye_blink("images/ep008/ep008_commander_smile") with dissolve
    rah "I was curious to know how you and your friends are settling in."
    rah "If there’s anything lacking, please let me know."
    rah "Your imprisonment was a mistake we’d like to put behind us."
    "I was a little startled by her friendly tone and I wondered how much her queen had a hand in that."
    c "Considering you nearly blasted us to pieces when we broke atmosphere, we’re doing quite well."
    c "The fact that our ship is being repaired is reassuring, but my guess is that this is mostly on behest of the Queen."
    scene expression eye_blink("images/ep008/ep008_commander") with dissolve
    rah "She gave the order, yes."
    c "I thought as much."
    rah "One of your crew mates is coordinating the repairs, I believe."
    c "That would be Thyia."
    c "And I think she’s just as much keeping an eye out for any trickery on your part, as she is overseeing the work."
    rah "You don’t like us very much, do you, [p_name]?"
    c "Are you fucking surprised?!"
    if game.is_special:
        c "You invaded a foreign moon, killed scores of people, kidnapped my sister and nearly killed my best friend."
    elif True:
        c "You invaded a foreign moon, killed scores of people, kidnapped my childhood friend and nearly killed my best friend."
    c "So yeah, I don’t like you very much."
    rah "I understand."
    rah "I will not apologize for our actions however."
    rah "But know we did not rejoice in the things we had to do."
    rah "I do hope we can work on a mutual understanding."
    if ep008_warrior_yell:
        c "Unlikely."
    elif True:
        c "Maybe..."
    c "Well, I’m going to leave you to your duties."
    scene expression eye_blink("images/ep008/ep008_commander_sexy") with dissolve
    rah "Please, [p_name], there are some things I’d like to discuss in private."
    rah "Maybe we can share a drink in my quarters."
    "Now that request really shook me."
    "I had a feeling what that private discussion might lead to..."
    "But did I want to pass up a chance of maybe knowing more of Eva’s situation?"
    menu:
        "Come with her [RahiaPath]" if True:
            $ ep008_commander_visit = True
            c "That would be a pleasure."
            rah "Good, follow me."
            scene ep008_rahia_corridor with dissolve
            "I followed Rahia through the corridors to an area where I hadn’t been before."
            "The door opened to a large room, adorned with martial decorations."
            scene ep008_rahia_drinks with dissolve
            "Rahia talked while she poured us two drinks."
            scene expression eye_blink("images/ep008/ep008_rahia_closeup") with dissolve
            rah "I’m going to be straightforward with you."
            rah "You intrigue me, [p_name]."
            rah "Back on Lanan P-10, you appeared to be just another hapless kid, way in over his head."
            rah "But then you went on a mad quest through the galaxy to find our Queen."
            scene expression eye_blink("images/ep008/ep008_rahia_closeup_smile") with dissolve
            rah "And I reckon the man who stands before me today is someone very different from the boy on Lanan."
            c "I’m not sure."
            c "Why were you on Lanan anyway?"
            scene expression eye_blink("images/ep008/ep008_rahia_closeup") with dissolve
            rah "Because it was foretold."
            c "Foretold?"
            rah "Our ancient writings predicted a major event on Lanan P-10."
            rah "The writings were correct."
            c "You acted on prophecy?"
            scene expression eye_blink("images/ep008/ep008_rahia_closeup_doubt") with dissolve
            rah "Yes, we did.{w} You sound surprised?"
            c "It’s a little unexpected."
            c "I thought you were raiders, or an invasion force."
            scene expression eye_blink("images/ep008/ep008_rahia_closeup") with dissolve
            rah "Yes, I see why you’d think that."
            c "What did the prophecy tell you?"
            rah "I can’t divulge that."
            c "Can’t, or won’t?"
            rah "It is deemed forbidden knowledge by the priestesses."
            c "I don’t think I’ve actually met one of your priestesses."
            scene expression eye_blink("images/ep008/ep008_rahia_closeup_serious") with dissolve
            rah "Oh, but I’m sure you will."
            rah "Ever since the prophecies turned out to be true for once, Erylin has been insufferable."
            c "Erylin?"
            rah "She’s the head priestess and one of the Queen’s advisers."
            rah "It used to be that the warrior caste was the most important, but things have changed."
            rah "People generally ignored the ravings of the priestesses, until Lanan P-10 changed everything."
            rah "Normally there are a great many of them in the Citadel, sticking their noses in everything."
            scene expression eye_blink("images/ep008/ep008_rahia_closeup") with dissolve
            rah "I believe Erylin went on some vision quest in the jungle with her entourage and will return in a few days."
            c "Right, I’m sure I’ll be delighted I can make her acquaintance."
            c "But when can I see Eva, your Queen?"
            scene expression eye_blink("images/ep008/ep008_rahia_closeup_serious") with dissolve
            rah "I’m afraid that’s also very much in the hands of Erylin."
            rah "She controls the Queen’s Guard now, instead of us."
            rah "You can formally petition our Queen, of course."
            c "So you’ve told me."
            rah "I’m sorry I can’t be of more help."

            python:
                codex_erylin = add_codex_entry(
                    Codex,
                    __("Characters"),
                    __("Erylin"),
                    [
                        __("Leader of the priest caste of the Acarhyn. Has become a powerful political player at the Acarhyn court after the prophecy about the Virgin Queen leading the Acarhyn to Lanan P-10 seemingly turned out to be true.")
                    ]
                )

            scene expression eye_blink("images/ep008/ep008_rahia_closeup_smile") with dissolve
            rah "That wasn’t the reason I asked you to come to my quarters anyway."
            rah "I know you have a warrior’s heart."
            scene expression eye_blink("images/ep008/ep008_rahia_closeup") with dissolve
            rah "A warrior’s heart is rare among the men we normally obtain."
            c "Kidnap, you mean?"
            scene expression eye_blink("images/ep008/ep008_rahia_closeup_smile") with dissolve
            rah "It would be an honor to share my bed with you."
            "I needed a minute to process what she was offering me, but when Rahia started to remove her armor, the confusion ended."

            menu:
                "Fuck her [RahiaPath]" if True:
                    $ ep008_commander_sex = True
                    c "I accept, of course."
                    call ep008_commander_sex from _call_ep008_commander_sex
                "Politely decline" if True:
                    $ e008_rahia_decline_polite = True
                    c "I’m sorry, but I must decline."
                    scene expression eye_blink("images/ep008/ep008_rahia_closeup") with dissolve
                    rah "Suit yourself."
                    "I’m sure she didn’t like my answer, but I felt relieved when I was on my way back again to my quarters."
        "Rudely decline [red]\[- to Warrior alliance\]" if True:
            $ e008_rahia_decline_rude = True
            c "Just fuck off, will you?"
            scene expression eye_blink("images/ep008/ep008_commander_angry") with dissolve
            rah "I should have you publicly flogged, you know that?!"
            c "And you’re quick to show your true colors."
            c "I repeat, fuck off."
            scene ep008_commander_angry_alt with dissolve
            "I abandoned the commander as she slammed her fist down on the table in anger."
        "Politely decline" if True:
            $ e008_rahia_decline_polite = True
            c "I’m still getting my bearings around here."
            c "And I’m very tired, so I hope you don’t mind if I decline."
            scene expression eye_blink("images/ep008/ep008_commander") with dissolve
            rah "Not at all, maybe another time."
    return


label ep008_commander_sex:
    if _in_replay:
        $ warrior_name = "Rahia"
        $ ep008_athryn_fucked = False
        $ ep008_athryn_fucked_last = False
        $ ep008_frisa_fucked = False
        $ ep008_frisa_fucked_last = False
        $ ep008_frisa_anal = False

    scene ep008_commander_undress with dissolve
    "The woman had shed her armor in record time, a feat that would probably be impossible with true Medieval armor."
    scene ep008_commander_naked with dissolve
    "I didn't really have time to ponder the issue, because I was too busy looking at her muscular body."
    "Her abdomen almost seemed to be made out of chiseled granite, powerful muscles rippling underneath her skin."
    "Rahia's large breasts had the same statuesque quality."
    "She knelt on the bed, showing off her powerful thighs and looked at me expectingly."
    rah "How will you have me?"
    scene ep008_commander_naked_behind with dissolve
    "The woman crept on the bed and unashamedly showed her ass to me."
    "Every fiber in her being exuded power and control."
    "I longed to make her mine and walked around the bed to face her."
    scene ep008_commander_naked_alt with dissolve
    rah "Tell me."
    c "I'm going to make you crazy with my tongue first."
    c "Make you lose all control, until you're ready to get fucked."
    rah "Such bravado."
    rah "I’d like to see you make good on that claim."
    show ep008_commander_lick with dissolve
    "I moved behind Rahia, grabbed her by her sides and brought her cunt to my mouth."
    "My hands on her well-muscled buttocks kept her in place as my tongue pressed against her pussy."
    "I parted her labia and licked the entire length of her gash slowly."
    "When I reached her taint I moved back towards her clitoris."
    "Rahia started rocking back and forth and made encouraging noises."
    scene ep008_commander_lick_closeup_alt with dissolve
    rah "Is that all you’ve got?"
    "Despite her dismissive words, I noticed the tenseness that edged them."
    "I kept going at her slit, but picked up the pace."
    "My tongue moved rapidly from side to side, swirling around her clit."
    "When I tasted the first droplets of her juices, I knew I was on the right path."
    "Rahia didn’t make any derisive comments for a while, but breathed heavily instead."

    menu:
        "Lick her anus [gr]\[Anus Lick\]" if True:
            $ ep008_anus_lick = True
            "I decided to surprise her."
            show ep008_commander_lick_alt with dissolve
            "In one motion, starting from her swollen clit, I made my way upwards."
            "I surprised her by pressing the tip of my tongue inside her anus and stimulating her there as well."
            rah "Oh fuck, what are you doing?!"
            rah "Oooooh, you dirty boy!"
            "When my tongue came back to stimulate her clitoris again, her slit was coated in her juices."
            c "I think you’re ready for my cock now, aren’t you?"
        "Just fuck her" if True:
            c "I think you’re ready for my cock now, aren’t you?"

    scene ep008_commander_lick_alt_closeup with dissolve
    "Rahia was too proud to say anything, but I wanted an answer."
    c "Or we could just stop here and part ways."
    rah "We both know you aren’t going to do that."
    c "I might, just to make a point."
    c "I can be very petty, you know."
    c "Just answer the question."
    c "Are you ready to take my dick?"
    rah "Yes, yes I am."
    rah "Please give me your thick hard cock."
    scene ep008_commander_sex_doggy_closeup with dissolve
    "I stood up behind her and pulled her towards me."
    "This wasn’t the time to be subtle, so I pushed the tip against Rahia’s opening and entered her."
    "The gasp she let out satisfied me more than I dared to admit."
    scene ep008_commander_sex_doggy_alt with dissolve
    "I didn’t give her time to catch her breath and started to fuck her without mercy."
    "At first she endured it silently, but when my cock hit her deeper inside her vagina with each thrust, low moans erupted from the muscular woman."
    scene ep008_commander_sex_doggy with dissolve
    rah "Harder! Fuck me harder with that large cock!"
    "Her muscles rippled beneath her skin while she took my dick without reluctance."
    rah "Fuck me like a slut, [p_name]."
    c "Show me what kind of slut you are, Rahia."
    scene ep008_commander_penetrate with dissolve
    "I slid on the bed and pulled Rahia on top of me."
    "She squatted on top of me and guided my wet cock inside her fuckhole."
    show ep008_commander_sex with dissolve
    "Straining the muscles of her legs and thighs, she rode me reverse cowgirl."
    rah "I can feel your cock so deep inside me, [p_name]!"
    scene ep008_commander_sex_alt with dissolve
    "Although the position we were in allowed her more control, I managed to take some of it from her by holding her middle and attacking her cunt with vicious short thrusts."
    scene ep008_commander_sex_closeup with dissolve
    rah "Make my pussy yours, [p_name]!"
    rah "Harder! Harder! Oooh!"
    scene ep008_commander_sex_women with dissolve
    "The door had opened, something I hadn't noticed until after two Acarhyn stood before the bed I was fucking Rahia on."
    $ woman_name = "Acarhyn"
    $ woman_portrait = "side_frisa"
    $ woman2_name = "Acarhyn"
    $ woman2_portrait = "side_athryn"
    woman "You summoned us, Commander."
    woman2 "Is he treating you well, Commander?"
    rah "Oh fuck yes. Come join us."
    woman "Certainly, Commander."
    "I was too busy fucking Rahia to understand the implications of what just happened."
    scene ep008_commander_sex_women_naked_alt with dissolve
    "Only when the two women undressed themselves did I realize I’d have to pleasure three women all of a sudden."
    "One of them looked vaguely familiar."
    "When she turned towards us I knew her as one of the guards who took us prisoner back in the jungle."
    "But then it hit me, she was the one that had nearly killed Kit back on Lanan!"
    scene ep008_commander_sex_women_naked with dissolve
    woman2 "He sure has a nice cock, doesn’t he?"
    woman "Yes, I can’t wait to taste it."
    rah "Frisa, Athryn, join us."
    $ woman2_name = "Athryn"
    $ woman_name = "Frisa"

    if is_patreon() and renpy.has_label("extra_scene_15") and not _in_replay:
        call extra_scene_15 from _call_extra_scene_15

        scene ep008_commander_sex_women_approach with dissolve
        "Having abandoned the dildo, both women approached the bed."
        "Frisa walked a little unsteady and her eyes still burned with lust."
        "Athryn wore a provocative smile and radiated a sexual hunger equaled by the older woman flanking her."
    elif True:
        scene ep008_commander_sex_women_approach with dissolve

    "It took me everything to not throw Rahia off the bed and attack the fair skinned girl."
    "Instead I thought of something else."
    "If Athryn was so eager to get fucked, I’d show her..."
    menu ep008_commander_group_sex:
        "Fuck Athryn" if not ep008_athryn_fucked:
            $ ep008_athryn_fucked = True
            if ep008_frisa_fucked:
                $ ep008_athryn_fucked_last = True

            scene ep008_commander_group_penetrate with dissolve
            "I made Athryn lie down on the bed and pushed open her legs."
            rah "Athryn, you’re going to enjoy this."
            woman2 "I’m sure I will."

            menu:
                "Choke her [RahiaPath]" if True:
                    $ ep008_athryn_choke = True
                    c "Don’t be too sure of that."
                    scene ep008_athryn_fear with dissolve
                    woman2 "What?!"
                    scene ep008_athryn_choke with vpunch
                    "I didn’t really think about what I did next and quickly put my hands around her throat and squeezed."
                    "Frisa gasped and started to come to the girl’s defence, but Rahia held her back."
                    c "You fucking tried to kill my friend!"
                    scene ep008_athryn_choke_alt with dissolve
                    "Athryn clawed at my arms in a futile attempt to pry my hands from her throat."
                    "The other two women could have killed me by now, defending Athryn, but they just looked at us both."
                    "Rahia wore a curious expression."
                    if game.is_special:
                        c "You ran a sword through my friend, just because he tried to run after my sister!"
                    elif True:
                        c "You ran a sword through my friend, just because he tried to run after Eva!"
                    scene ep008_athryn_choke_closeup with dissolve
                    woman2 "I...{w} I..."
                    "Athryn was struggling for air and thrashing her legs."
                    scene ep008_athryn_choke_alt with dissolve
                    rah "I think you owe [p_name] an apology, Athryn."
                    c "You owe Kit an apology."
                    scene ep008_athryn_choke_closeup with dissolve
                    woman2 "I...{w} I’m...{w} s...{w} sorry!"
                    "I could tell the girl was nearly losing consciousness and released my grip on hear throat."
                    "She violently gasped for air, regaining herself with fits and starts."
                    scene ep008_athryn_sad with dissolve
                    "When she was able to speak again, she looked me directly in the eyes."
                    woman2 "I’m truly very sorry for what happened."
                    "Her voice was shaky and hoarse, but the sentiment she managed to convey seemed sincere."
                    woman2 "Please use me in any way you deem fit."
                    scene ep008_rahia_smile with dissolve
                    rah "Show her what you’re made of, [p_name]."
                    "Somehow the violence had riled up the women even more."
                "Just fuck her" if True:
                    "It was unfortunate the women outnumbered me and were skilled in martial combat, otherwise I’d made Athryn pay for what she did right then and there."
                    "Instead, I focused my aggression and resolved to make her pussy pay the price for what she’d done."

            "I forced one leg towards her body and held her arms downward."
            show ep008_commander_group_sex with dissolve
            "Pinning her, I slid my cock inside her tight slit."
            woman2 "Oh fuck!{w} Fuck!{w} He’s so big!"
            show ep008_commander_group_sex_alt with dissolve
            "Frisa crouched beside the girl’s head and kissed her flushed cheeks."
            woman "You can take him, just relax."
            woman "You’re nice and wet, just enjoy his thick hard cock inside you."
            woman2 "I am!{w} Oh!{w} He feels so good inside of me."
            "Rahia was smiling and fingering her cunt as she watched me fuck Athryn."
            rah "Don’t hold back, [p_name], she’s dripping wet and eager."
            "I decided to follow her advice and buried my cock deep inside the pale girl’s cunt."
            "She rolled her eyes backwards and for an instant I was afraid she might lose consciousness."
            show ep008_commander_group_sex_closeup with dissolve
            "Instead she moaned deeply and released a flood of her own juices."
            woman2 "F-f-fuck!"
            "Still holding her down, I fucked her with abandon."
            "Her ass lifted from the bed with each thrust and her small breasts bounced violently."
            woman2 "Don’t stop, don’t stop!"
            "Her nails dug into one of my arms as she took my cock deep inside her tight cunt."
            scene ep008_commander_group_sex_closeup_rahia with dissolve
            "Rahia was fingering both her pussy and asshole, her fingers coming back drenched wet with her pussy juices."
            rah "That’s it, [p_name]."
            rah "Do you like what he’s doing to you, Athryn?"
            scene ep008_commander_group_sex_closeup_athryn with dissolve
            woman2 "I love it!{w} I love it!"
            rah "Why don’t you fuck her like the slut she truly is?"
            woman "Yes, fuck her like a little bitch!"
            "I had an idea what both women meant, so I pulled out of her."
            show ep008_commander_group_lick with dissolve
            "Athryn looked a little frustrated at first, but obeyed when Rahia made her squat on top of the older woman."
            "The older woman pawed greedily at my cock and lapped up the pussy juice that covered my shaft as I rubbed my cock all over her face."
            scene ep008_commander_group_lick_closeup with dissolve
            rah "Frisa is cleaning that cock for you, Athryn, you made such a mess."
            woman2 "I just want him inside me again, please!"
            show ep008_commander_group_lick_alt with dissolve
            "The commander treated Athryn to some passionate tongue kissing as I prepared to penetrate the girl again."
            "Frisa kept licking my shaft, but raised her head to lick the pale girl’s pussy as well."
            scene ep008_commander_group_lick_doggy with dissolve
            "I slid inside her."
            woman2 "Oh yes, that’s it!"
            woman2 "Make me feel good, please!"
            scene ep008_commander_group_lick_doggy_closeup with dissolve
            "Rahia had turned her attention to Frisa’s pussy which was already getting fingered by her other friend."
            "Frisa was getting her cunt licked and Athryn’s pussy got the same attention while filled with my throbbing cock."
            "Athryn’s soft round ass bounced up and down as I fucked her with increasing speed."
            scene ep008_commander_group_lick_doggy_alt with dissolve
            rah "Do you love that big cock inside of you, Athryn?"
            woman2 "I love it!{w} It feels so good!{w} Fuck me harder!"
            woman2 "I want to feel that big cock all inside me."
            if not ep008_athryn_fucked_last:
                rah "Not so greedy, girl, I think Frisa wants to have fun with [p_name] too."
                rah "Swap places."
                jump ep008_commander_group_sex
        "Fuck Frisa" if not ep008_frisa_fucked:
            $ ep008_frisa_fucked = True
            if ep008_athryn_fucked:
                $ ep008_frisa_fucked_last = True
            scene ep008_commander_group_doggy_penetrate with dissolve
            if not ep008_athryn_fucked_last:
                "Despite her loud longing moans, Athryn complied with her commander’s order."
                "She was now at the bottom and already licking Frisa’s wet slit."
            elif True:
                "I wanted to fuck the older woman first."
                "When Frisa knew I had selected her, she got on all fours."
            "Rahia stood beside us, playing with her breasts and rubbing her cunt."
            rah "She’s so ready for you, [p_name]."
            "Despite being a serving girl, Frisa was almost as muscular as Rahia."
            "When I held her sides, I could feel the muscles straining in anticipation of the dicking she was about to receive."
            show ep008_commander_group_doggy with dissolve
            "Because of the attention Athryn was giving the woman’s cunt, I entered her ribbed tunnel with relative ease."
            woman "Mmmm, yes.{w} Keep licking my puss, Athryn."
            "The pale girl kept her tongue busy between the older woman’s legs, while I penetrated Frisa balls deep."
            woman "Fuck me!"
            "I didn’t hesitate and did just that."
            "My balls smacked against Athryn’s face as I pounded the woman on top of her without mercy."
            woman "Oh yes, yes, keep fucking that pussy!"
            "Juice was streaming down her thighs as Frisa was stimulated from both ends."
            "I heard Rahia moan next to me."
            scene ep008_commander_group_doggy_closeup_alt with dissolve
            rah "Why don’t you surprise her?"
            "I had an idea what she meant..."

            menu:
                "Anal" if True:
                    $ ep008_frisa_anal = True
                    "I slipped out of Frisa’s dripping cunt."
                    scene ep008_commander_group_doggy_tease with dissolve
                    "Holding my cock, I teased her first by sliding the tip across her wet slit."
                    woman "Mmmm, put it back in please!"
                    "She was about to speak when I pushed the head of my dick against the folds of her anus."
                    "I didn’t wait for her reaction and stuffed my cock inside her asshole."
                    scene ep008_commander_group_doggy_closeup with dissolve
                    woman "Aaah!"
                    rah "Take it, Frisa, you can do it."
                    rah "Take that long hard cock inside your ass."
                    "Frisa gritted her teeth while the entire length of my veined shaft disappeared inside her taut asshole."
                    woman "Oh fuck! It’s so big."
                    rah "Now fuck her."
                    show ep008_commander_group_doggy_alt with dissolve
                    "The first few thrusts I encountered some resistance, but then Frisa was used to my girth."
                    "I slapped her ass as I sodomized her and she yelped in response."
                    woman "Don’t stop fucking my ass, you feel so good inside me!"
                "Vaginal" if True:
                    "However, I didn’t want to leave Frisa’s dripping cunt."
                    show ep008_commander_group_doggy with dissolve
                    "So I burrowed even deeper inside her vagina, making short violent thrusts that took her breath away."
                    woman "Don’t stop fucking me, you feel so good inside me!"

            if not ep008_frisa_fucked_last:
                rah "You've treated her very well."
                rah "Now swap places."
                jump ep008_commander_group_sex

    "Fucking the women was starting to wear me out and I felt close to blowing my load."

    menu:
        "Anal Creampie" if ep008_frisa_fucked_last and ep008_frisa_anal:
            "Frisa’s asshole was so tight and stimulating me in all the right ways."
            "Grabbing hold of her tightly, I rode her hard and fast."
            scene ep008_commander_group_anal_creampie with flash
            with flash
            "She moaned like an animal as I filled her ass to the brim with warm cum."
            scene ep008_commander_group_anal_creampie_alt with dissolve
            "As my seed started dripping from her anus, Athryn opened her mouth and greedily drank the stream that dribbled down."
        "Creampie Rahia [gr]\[Rahia Creampie\]" if True:
            $ ep008_rahia_creampie = True
            if ep008_frisa_fucked_last:
                "Despite how wonderful Frisa felt, I decided Rahia deserved my seed."
                "I pulled out of the older woman and pulled Rahia towards me."
            elif True:
                "Despite how wonderful Athryn felt, I decided Rahia deserved my seed."
                "I pulled out of the younger girl and pulled Rahia towards me."
            scene ep008_commander_rahia_fuck with vpunch
            "After entering her I managed one or two thrusts before filling her pussy to the brim with warm cum."
            scene ep008_commander_rahia_creampie with flash
            with flash
            "When I pulled out of her, Frisa and Athryn went between their commander’s legs to lap up the seed that was now oozing out of her slit."
        "Creampie Athryn [gr]\[Athryn Creampie\]" if ep008_athryn_fucked_last:
            $ ep008_athryn_creampie = True
            "Athryn’s tight little pussy gave me such a wonderful feeling, I decided I’d finish inside her."
            "Grabbing hold of her tightly, I rode her hard and fast."
            scene ep008_commander_athryn_creampie with flash
            with flash
            "She moaned like an animal as I filled her pussy to the brim with warm cum."
            scene ep008_commander_athryn_creampie_alt with dissolve
            "As my seed started dripping from her slit, Frisa opened her mouth and greedily drank the stream that dribbled down."
        "Creampie Frisa [gr]\[Frisa Creampie\]" if ep008_frisa_fucked_last:
            $ ep008_frisa_creampie = True
            if ep008_frisa_anal:
                "Despite the wonderful feeling her ass gave me, I wanted to finish inside Frisa’s pussy."
            elif True:
                "Frisa’s cunt gave me such a wonderful feeling, I decided I’d finish inside her."
            "Grabbing hold of her tightly, I rode her hard and fast."
            scene ep008_commander_group_creampie with flash
            with flash
            "She moaned like an animal as I filled her pussy to the brim with warm cum."
            scene ep008_commander_group_creampie_alt with dissolve
            "As my seed started dripping from her slit, Athryn opened her mouth and greedily drank the stream that dribbled down."
        "Bodies" if True:
            scene ep008_commander_group_bodies_alt with dissolve
            "Rahia noticed my mounting climax and slipped onto the bed."
            rah "He’s ready, girls."
            rah "Spray your cum all over us, [p_name]."
            scene ep008_commander_group_bodies with flash
            with flash
            "The girls got into position and I managed to shoot my warm seed over Frisa’s ass and the other girl’s chests."
        "Facial" if True:
            scene ep008_commander_group_facial_alt with dissolve
            "Rahia noticed my mounting climax and slipped onto the bed."
            rah "He’s ready, girls."
            rah "Spray your cum all over our faces, [p_name]."
            scene ep008_commander_group_facial with flash
            with flash
            "The girls got into position and I managed to blast my warm seed over their faces and chests."
    scene ep008_commander_group_post with dissolve
    "The Acarhyn cleaned themselves and sat close to each other on the bed."
    rah "As I said, a warrior’s heart."
    rah "You have well and truly fucked us."
    woman "If you ever want to visit us..."
    woman2 "Just let us know."
    "I gathered my things and slipped out of the commander’s bed chamber."
    scene black with fade
    $ renpy.end_replay()

    python:
        codex_athryn = add_codex_entry(
            Codex,
            __("Characters"),
            __("Athryn"),
            [
                __("An Acarhyn warrior who was present at the attack on Lanan P-10. She stabbed Kit while he was trying to run after Eva as she was being dragged away."),
                __("Athryn was later encountered in the Acarhyn Citadel as one of the commander's lovers.")

            ],
            "images/codex/Athryn.webp"
        )

        codex_frisa = add_codex_entry(
            Codex,
            __("Characters"),
            __("Frisa"),
            [
                __("An Acarhyn servant and one of the commander's lovers.")
            ],
            "images/codex/Frisa.webp"
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
