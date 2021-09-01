
image ep002_nyiruan_cave_pussy_closeup_alt = Movie(play="movies/ep002/ep002_nyiruan_cave_pussy_closeup_alt.webm")
image ep002_nyiruan_cave_suck_alt = Movie(play="movies/ep002/ep002_nyiruan_cave_suck_alt_closeup.webm")
image ep002_nyiruan_cave_fisting = Movie(play="movies/ep002/ep002_nyiruan_cave_fisting.webm")
image ep002_nyiruan_cave_line_fuck_alt = Movie(play="movies/ep002/ep002_nyiruan_cave_line_fuck_alt.webm")
image ep002_nyiruan_cave_line_fuck_closeup = Movie(play="movies/ep002/ep002_nyiruan_cave_line_fuck_closeup.webm")
image ep002_nyiruan_cave_line_fuck_virgin_breasts = Movie(play="movies/ep002/ep002_nyiruan_cave_line_fuck_virgin_breasts.webm")
image ep002_nyiruan_cave_line_fuck_virgin_fuck = Movie(play="movies/ep002/ep002_nyiruan_cave_line_fuck_virgin_fuck.webm")
image ep002_thyia_bed_penetrate = Movie(play="movies/ep002/ep002_thyia_bed_penetrate.webm")
image ep002_thyia_nipples = Movie(play="movies/ep002/ep002_thyia_nipples.webm")


label episode002:
    $ save_name = "Episode 2"

    $ ep002_lilly_comfort = False
    $ ep002_lilly_understanding = False
    $ ep002_thyia_talk = False
    $ ep002_thyia_sex = False
    $ ep002_thyia_creampie = False
    $ ep002_cargo = False
    $ ep002_university = False
    $ ep002_cargo_completed = False
    $ ep002_university_completed = False
    $ ep002_pit_thim = False
    $ ep002_ro_lie = False
    $ ep002_ro_orgy = False
    $ ep002_ro_help = False
    $ ep002_dee_creampie = False
    $ ep002_ro_virgin_creampie = False
    $ ep002_thyia_acceptance = False

    scene black with fade
    centered "{=chapter_heading}EPISODE 2{/=chapter_heading}"

    scene ep002_missile_approach with dissolve
    call location_screen (__("Unknown, TGN Ypotryll in pursuit of TGN Enfield"), True) from _call_location_screen_4

    scene ep002_cockpit_camran with dissolve
    c "How long until impact?"
    ce "Less than two minutes."
    c "Fuck!"
    scene ep002_cockpit_kit with dissolve
    ki "Can't we outrun them?"
    scene ep002_cockpit_celine with dissolve
    ce "Not at this speed."
    ce "We could..."
    ce "No."
    c "Say it!"
    ce "We could burst our Drive..."
    scene ep002_cockpit_kit with dissolve
    ki "That's suicide!"
    scene ep002_ship_closeup with dissolve
    "Every Terran ship comes equipped with a so-called Sylas-Karzen drive, named after the two scientists who built the first prototype after many centuries of development."
    "The Sylas-Karzen drive allowed mankind to finally travel faster than light, opening up the galaxy for exploration."
    "The Ypotryll had powered down its S-K drive as soon as it reached the habitable zone of Alpha Centauri, to avoid high-speed collisions with the many stations in the system."
    "It also allowed us to escape the hangar bay on the Enfield."
    "Céline's proposal was extremely risky. By burning up the entire fuel reserve of the S-K drive we would 'burst' away at tremendous speed towards an unknown destination."
    "Bursting no longer constitutes linear travel at the speed of light, but is more akin to a hyperspace jump."
    "A random hyperspace jump in total darkness, that is."
    "There's no way of knowing how far a ship will travel when it bursts its drive."
    "The chances of ending up somewhere in an uninhabited cluster without any fuel left are far too great."
    "This is the main reason why almost every species in the known galaxy uses the relatively safe jump-gates for hyperspace travel."
    "No sane captain would consider bursting their S-K drive, but we didn't have many options."

    python:
        codex_sk_drive = add_codex_entry(
            Codex,
            __("Technology"),
            __("The Sylas-Karzen drive"),
            [
                __("Enables Faster Than Light Travel, allowing mankind to explore and conquer the stars. The development of the Sylas-Karzen drive by Professor Hermann Sylas and Dr. Josephine Karzen is the result of several centuries of research, primarily based on the theories of Burkhard Heim and Miguel Alcubierre."),
                __("'Bursting' a drive allows for hyperspace travel, but without a clear destination and is deemed extremely dangerous.")
            ]
        )

    scene ep002_cockpit_camran with dissolve
    c "Do it."
    "Céline gritted her teeth and began punching in the sequence to overload the drive."
    scene ep002_cockpit_celine with dissolve
    ce "Thirty seconds to impact."
    "A button lit up and began blinking an angry red."
    ki "I love you all, guys."
    ki "I..."
    "At that moment I smashed the button and the entire ship began to hum."
    scene ep002_ship_missiles with dissolve
    ce "Fifteen seconds to impact."
    "By that time we were shaking in our seats and the noise of the drive overload became almost too much to bear."
    scene ep002_cockpit_celine_alt with dissolve
    ce "T-ten..."
    "The ship began to accelerate, accompanied by a heavy groan from the ship as the weight of an enormous amount of G's threatened to tear it apart."
    "We wouldn't have survived that amount of force if it weren't for the ship's shields and our genetically enhanced bodies."
    with vpunch
    with hpunch
    with vpunch
    "A great booming sound started vibrating through the Enfield, overwhelming all of our senses."
    scene ep002_ship_burst with hpunch
    with hpunch
    "In the corner of my eye I saw Céline slumping in her seat, as she lost consciousness."
    "The stars visible through the window outside became illuminated smears and the ship groaned as it was nearly ripped apart."
    "That's when the missiles hit."
    with vpunch
    play music "music/bent-and-broken.ogg" fadein 1.0 fadeout 4

    scene black with fade
    "Everything went black."

    scene ep002_ship_drift with dissolve
    call location_screen (__("Unknown, drifting"), True) from _call_location_screen_5

    "I was the first to regain consciousness."
    "Céline still sat slumped in her seat and Lilly and Kit lay on the ground, but the ship showed seven lifeforms present."
    if not ep001_vess_truth:
        "Which struck me as odd, as there should be five..."

    if celine_romance:
        scene ep002_ship_lilly_kit with dissolve
        "Ignoring the life support systems, I checked on Céline and Kit first."
        scene ep002_ship_celine_unconscious with dissolve
        "Kit was still out, so was Lilly, Céline stirred as soon as I touched her shoulder."
    elif True:
        scene ep002_ship_lilly_kit with dissolve
        "Ignoring the life support systems, I checked on Lilly and Kit first."
        scene ep002_ship_celine_unconscious with dissolve
        "Both Lilly and Kit were still out, Céline stirred as soon as I touched her shoulder."

    scene ep002_ship_celine_conscious with dissolve
    c "Are you okay, Céline?"
    ce "Ugh, my head."
    ce "I think I'm fine."
    ce "How are the others?"
    c "Still out."
    ce "Are Jade and Thim still back there?"
    c "Oh fuck, some of the cargo wasn't tied down when we jumped..."
    c "I'll check on them."

    scene ep002_ship_cargo_bay with dissolve
    "Bracing for the worst I went into the small cargo bay of the ship to look for Jade and Thim."
    "It didn't take me long to find Thim."

    if ep001_vess_truth:
        "Vess and Jade were huddled over Thim's body."
        "The ship's systems had already told me he was alive, but he might have received further injuries when we performed the Burst."
        scene ep002_ship_cargo_bay_vess_jade with dissolve
        c "Are you both okay?"
        j "Yes, Master [p_name]."
        ve "I think so."
        c "And Thim?"
        j "He doesn't look any worse for wear than when we dragged him onto the ship."
        ve "When the engines began to spin up we strapped ourselves to storage containers."
        c "Good thinking."
        scene expression eye_blink("images/ep002/ep002_ship_cargo_bay_jade") with dissolve
        j "What happened?"
        c "We burst our Drive."
        scene expression eye_blink("images/ep002/ep002_ship_cargo_bay_vess") with dissolve
        ve "You did what?"
        c "Long story."
        c "Short version is that we were pursued by rockets, we overloaded our engine, jumped to an unknown location and now we seem to be safe."
        c "For the moment..."
        ve "Unknown location?"
        c "Yes."
        ve "So we could be lightyears away from Lanan?"
        c "We would be dead otherwise and let's not jump to conclusions."
        c "Just wait here until I check on the others again."
        scene expression eye_blink("images/ep002/ep002_ship_cargo_bay_jade_alt") with dissolve
        j "Yes, master."
        ve "If you say so..."
        scene ep002_ship_celine_kit_lilly_conscious with dissolve
        ce "How are Thim and the girls doing?"
        c "They're all fine."
    elif True:
        "I found Jade huddled over Thim's body."
        "The ship's systems had already told me he was alive, but he might have received further injuries when we performed the Burst."
        c "Are you okay?"
        scene ep002_ship_cargo_bay_jade with dissolve
        j "Yes, Master [p_name]."
        c "And Thim?"
        j "He doesn't look any worse for wear than when we dragged him onto the ship."
        j "When the engines began to spin up I strapped us to storage containers."
        c "Good thinking."
        j "What happened?"
        c "We burst our Drive."
        j "That's very risky, isn't it?"
        c "It sure is, but we would have died otherwise."
        scene ep002_ship_cargo_bay_jade_alt with dissolve
        j "I heard Commander Szuzume on the radio, she really went through with it..."
        c "She did..."
        scene ep002_ship_cargo_bay_containers with vpunch
        "At that moment I heard something shuffle at the back of some storage containers."
        "As I sprinted towards them, I saw a female form hiding behind a crate."
        scene ep002_ship_cargo_bay_containers_vess with vpunch
        c "Vess?"
        ve "I'm sorry..."
        c "What are you doing here?"
        ve "I followed you to the hangar bay and got on the ship during the consternation with that boy."
        scene ep002_ship_cargo_bay_containers_vess_closeup with dissolve
        ve "I need to find them, [p_name], my family is all I've got left."
        "The problems just kept piling on top of me..."
        c "I still intend to go after those cunts, but you might have noticed that we ran into a lot of trouble when we left the Ypotryll."
        c "So I'm handing you over to my attendant for the time being."
        c "We'll speak later."
        ve "Okay..."
        scene ep002_ship_cargo_bay_vess_jade_curious with dissolve
        c "Jade, this is Vess."
        c "Until we figure out where we go from here I want you two to stay in this cargo hold and care for Thim here."
        c "There's an intercom near the door if he gives you trouble when he wakes up."
        j "Yes, master."
        "I left the girls with Thim, but made sure to lock the hatch to the cargo bay in case of any surprises."
        scene ep002_ship_celine_kit_lilly_conscious with dissolve
        ce "How are they doing?"
        c "Jade's fine and Thim too, he's still unconscious, though."
        c "We seem to have gained another crew member though..."
        ce "What?!"
        c "One of the girls from the village followed me to the hangar bay and hid on the Enfield."
        c "She wants to search for her family."
        ki "Fuck. Like things aren't complicated enough."

    scene expression eye_blink("images/ep002/ep002_ship_lilly_angry") with vpunch
    "When I turned towards Kit I caught the furious look on Lilly's face."
    "A contempt that I had never seen before."
    l "You stupid fuck!"
    l "You selfish fucking bastard!"
    scene ep002_ship_lilly_angry_punch with vpunch
    "She stormed at me, surprising Kit and Céline, and tried to hit me."
    "Her fists rained blows on my chest until the grief that was clearly eating at her finally overtook her."
    scene ep002_ship_lilly_hug with dissolve
    "Not sure what to do, I held her tight while sobs wracked her body."

    menu:
        "Comfort her [LillyPath]" if True:
            $ ep002_lilly_comfort = True
            c "I'm sorry, Lilly."
            c "I didn't mean for this to happen."
            c "All I wanted..."
            l "You wanted what?!"
            scene ep002_ship_lilly_hug_angry with dissolve
        "Stay silent" if True:
            scene ep002_ship_lilly_hug_angry with dissolve
            l "Why don't you say something?!"

    "It took a while for her to wrestle herself out of my arms, as if she didn't realize the person she hated held her close."
    l "All you did was create a big fucking mess."
    l "Like I said you would."
    l "We don't know where we are."
    l "We're deserters now."
    l "And the fucking ship is shot up beyond repair."
    c "Is that true?"
    scene expression eye_blink("images/ep002/ep002_ship_celine_serious") with dissolve
    ce "We took a hit from the detonation of the first rocket."
    ce "Could be worse, but our main thrusters are fried."
    scene ep002_ship_lilly_hug_angry with dissolve
    l "Tell him about the fuel, Cé."
    scene expression eye_blink("images/ep002/ep002_ship_celine_serious") with dissolve
    ce "Yes, we have a small reserve left, but it's not going to take us far, especially with the thrusters being down."
    c "That's bad."
    c "Any inhabited planets in this system?"
    c "What system is this anyway?"
    scene expression eye_blink("images/ep002/ep002_ship_celine_serious") with dissolve
    ce "Just one."
    ce "We’re somewhere near Alpha Vulpeculae..."
    ce "Planet’s called Vulpes Velox according to the computer."
    c "That doesn’t sound like it’s controlled by the Sovereignty."
    ce "It isn’t, it appears we’re way out of human space."
    c "Can we get there, to Velox, I mean?"
    ce "I think so."
    ce "Though landing is going to be a challenge."
    c "Then that's our destination."
    scene expression eye_blink("images/ep002/ep002_ship_lilly_angry_alt") with dissolve
    l "Just like that..."
    l "What about saving Eva?"
    l "Your big fucking plan to save everyone?!"
    l "Now we're just going to fucking float to the nearest planet and just see where we go from there?"

    menu:
        "Be understanding [LillyPath]" if True:
            $ ep002_lilly_understanding = True
            c "I get why you're angry, but that's exactly what we're going to do, because it's the only thing we can do right now."
            if game.is_special:
                l "Not good enough, brother."
            elif True:
                l "Not good enough, [p_name_short]."
            l "Fuck it, I'm going to check on that bloody stowaway you've saddled us with."
            scene ep002_ship_lilly_exit with dissolve
            "Lilly walked out, slamming the entry hatch behind her."
        "Get angry" if True:
            c "Fuck Lilly, lay off it."
            c "It's the only thing we can do right now."
            c "I suggest you accept the status quo for the time being or fuck off on the next transport you can catch on that nearby planet."
            scene expression eye_blink("images/ep002/ep002_ship_lilly_angry_alt") with vpunch
            l "Fuck! You!"
            scene ep002_ship_lilly_exit with dissolve
            "Lilly ran out of the cockpit, slamming the entry hatch behind her."

    ki "She's really pissed."
    c "Yes, thank you, Captain Obvious."
    scene ep002_ship_celine_kit with dissolve
    c "Now, that planet."
    c "How long until we get there?"
    "Céline conjured up the necessary calculations using the ship's computer and after a few minutes we were crawling towards our destination using only our secondary thrusters."

    scene ep002_vulpes_velox with dissolve
    call location_screen (__("Vulpes Velox, near Alpha Vulpeculae, Orbit"), True) from _call_location_screen_6

    "After what seemed like an eternity, the Enfield finally pierced the atmosphere of the planet we were hoping to land on."
    "The descent was rough, which might have had something to do with our inexperience piloting ships."
    "Though the planet was supposed to be inhabited, there was no guarantee that its residents were intelligent enough to either repair a ship or even have a meaningful conversation with us."
    scene ep002_ship_celine_steering with dissolve
    "Several settlements began to pop up on the ship’s nav computer."
    c "Could you target one of the smaller settlements?"
    ce "Sure, but why not the larger towns?"
    c "Landing this battered thing in a large port might attract a little too much unwanted attention."
    ce "I could probably set us down in the outskirts of this settlement, roughly a hundred people living there."
    c "Sounds good to me."
    c "We’ll explore the surroundings on foot after we land."
    scene expression eye_blink("images/ep002/ep002_ship_kit_closeup") with dissolve
    c "How are you feeling Kit?"
    c "Up for a little walk?"
    ki "I would, if it wasn’t for this damn wheelchair."
    ce "I’d go with you, but I need to check the computer, get a sense of where we are."
    ki "Guess that leaves Lilly..."
    ki "Or your attendant, maybe that girl..."
    ki "Or Thim..."
    c "I’m not sure if I should ask Lilly..."
    c "And the other girls don’t have any formal training."
    ki "It’s either that or hiking with the Great Duke Von Skandersfelt..."

    menu:
        "Ask Lilly" if True:
            "The Enfield was a very small vessel, so finding Lilly didn’t pose too much of a problem."
            scene ep002_ship_lilly_jade_vess with dissolve
            "I found her with the others in the cargo bay."
            c "Lilly I..."
            l "No [p_name_short], not now."
            l "Please leave me alone."
            if ep002_lilly_comfort and ep002_lilly_understanding:
                l "At least for a while."
            elif True:
                l "Preferably forever."
            scene expression eye_blink("images/ep002/ep002_ship_thim") with dissolve
            "So Thim went with me, something we both enjoyed so very much."
            "At least he kept silent about the head injury he got from Jade..."
        "Ask Thim [ThimPath]" if True:
            scene expression eye_blink("images/ep002/ep002_ship_thim") with dissolve
            c "Thim, are you feeling well enough to come with me?"
            t "Your attendant hit me on the fucking head with a wrench."
            c "I noticed..."
            c "We had to act quickly."
            c "But are you feeling better now?"
            scene expression eye_blink("images/ep002/ep002_ship_thim_curious") with dissolve

            if ep001_thim_talk and ep001_medbay_thim_talk:
                t "I guess, why?"
            elif True:
                t "Why?"
            c "We’re going to land soon near a town and I want to check it out."
            c "Get supplies and we need to do something about this ship."
            if ep001_thim_talk and ep001_medbay_thim_talk:
                t "Do something about the ship, you mean sell it?"
                c "Maybe."
            elif True:
                t "Why?"
                c "Is that the only question you can ask?"
            c "I sure as hell don’t want to keep flying in a TGN-tagged ship, so we’ll have to figure something out."
            c "I’ll let the others know what the plan is."
            if ep001_thim_talk and ep001_medbay_thim_talk:
                t "Okay, I’ll get ready."
            elif True:
                t "Suit yourself."

    scene ep002_ship_celine_steering with dissolve
    "As I headed back to Céline, the ship started moving to the co-ordinates punched into the computer earlier."
    c "Does this ship have a internal coms?"
    ce "Doesn’t every ship?"
    c "I think so, most of the finer details of ship-fairing I learnt from books or when I was paying attention to the instructor droning on about it, which wasn’t often."
    ce "Just talk in here, that should work."
    scene ep002_ship_camran with dissolve
    c "Listen up people."
    c "In a few moments we’ll touch down on Vulpes Velox, somewhere in the wilderness."
    c "There’s a town nearby and I intend to check it out on foot, together with Thim, the rest stays here to guard the ship."

    play music [ "music/reparateur.ogg", "music/eastminster.ogg" ] fadeout 4 fadein 1.0

    scene ep002_vulpes_velox_landed with dissolve
    call location_screen (__("Vulpes Velox, near Alpha Vulpeculae, Surface"), True) from _call_location_screen_7

    "After we landed, Thim and I headed out."

    scene ep002_walking_thim with dissolve
    t "Does this town have the resources we need?"
    c "I don’t know, hopefully there’s a workshop or something."
    c "We might need to fly to the nearest spaceport anyway, but I don’t want our presence known to each and everyone out there just yet."
    c "We’re outside of human space, so the chances of the Sovereignty impounding our ship and throwing us in a jail cell are minimal, but the locals could be just as hostile."

    if ep001_thim_talk and ep001_medbay_thim_talk:
        t "There’s supposed to be a lot of hostility against the Sovereignty."
        c "Yeah and if that’s really true I think it’s a little unhealthy to fly a broken TGN gunship inside alien territory."
        t "Agreed."
    elif True:
        t "Great..."

    scene ep002_vulpes with dissolve
    "The surface of Vulpes Velox turned out to be just as dull as Lanan, but we weren’t really there to see the sights."
    "It didn’t take long for us to reach the settlement, which turned out to be a broad street flanked by some makeshift houses."

    python:
        codex_vulpes = add_codex_entry(
            Codex,
            __("Planets"),
            __("Vulpes Velox"),
            [
                __("Location: Somewhere near Alpha Vulpeculae"),
                __("The first planet visited by [p_name] and friends after their escape from the TGN Ypotryll."),
                __("Most of the world is covered by desert, though there are several larger settlements. Thyia's workshop is located in one of the smaller towns on Vulpes Velox.")
            ]
        )

    "The place was almost deserted, but for a person sitting on a porch."
    scene expression eye_blink("images/ep002/ep002_vulpes_thim") with dissolve
    c "Let’s ask one of the locals for some directions."
    t "I think that guy over there isn’t human.."
    c "We’re in alien territory, that’s bound to happen."
    scene ep002_vulpes with dissolve
    "Within the Sovereignty contact with other species is greatly discouraged, except for the interactions with Tw’ill attendants."
    "Kit and I did have some experience with alien species, as the brothels of Alf Cen were somewhat indiscriminate when it came to hiring personnel."
    "Of course, trying to talk to a drugged-up whore is a little different from having a casual conversation with an unknown alien race."
    "This type of ‘first contact’ was, in other words, kind of a big deal."
    "We were prepared though, our language implants supported hundreds of different languages."
    scene ep002_vulpes_alien with dissolve
    c "Excuse me sir, after a long voyage, our ship needs some urgent repairs."
    c "I was wondering if there’s a shipyard or workshop nearby."
    $ man_name = "Alien"
    $ man_portrait = "side_man"
    man "Try Thyia."
    "So yeah, that wasn’t very momentous..."
    scene ep002_vulpes_workshop with dissolve
    "The location the guy pointed us to turned out to be a small workshop near a scrapyard."
    "It was a far cry from the professional shipyards we knew from the Sovereignty, but maybe they were open to doing some illicit work on TGN property."
    scene ep002_vulpes_workshop_thyia with dissolve
    "We pressed a buzzer and after a while the large door of the workshop slowly opened, revealing a woman waiting for us inside."
    th "Hiya, boys."

    python:
        codex_thyia = add_codex_entry(
            Codex,
            __("Characters"),
            __("Thyia"),
            [
                __("Thyia is a salvager and engineer working out of her workshop on Vulpes Velox.")
            ],
            "images/codex/Thyia.webp"
        )

    th "What brings you to this beautiful town?"
    th "Looking for work?"
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_closeup") with dissolve
    c "We’ve just landed."
    c "And we’re looking for supplies and someone that can help us with our ship."
    th "I might be able to help you on both counts."
    th "Define ‘help us with our ship’."
    th "Does it need repairing?"
    c "Refuelling at the very least, we were in a hurry."
    th "What kind of ship is she?"
    c "A light fighter."
    th "A fighter?"
    th "You plan on refuelling a lightly armored fighter, a ship that lacks any serious firepower, and go back out into the system?"
    c "We’re not sure..."
    th "You’re absolutely mad...{w} that’s suicide!"
    if not ep001_thim_talk or not ep001_medbay_thim_talk:
        t "He is, just not officially diagnosed."
        c "Shut up, Thim."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_skeptical") with dissolve
    th "It’s a wonder you weren’t shot down by an enemy ship the instant you arrived here."
    th "Something tells me this trip of yours wasn’t planned, or you’re monumentally stupid."
    th "I’m going with the first, but I’m not ruling out the second explanation yet."
    "Noticing we were losing what little credibility we had very fast, I decided to tell the woman at least part of the truth."
    c "All right, we commandeered it."
    if game.is_special:
        c "We’re mounting an expedition to rescue my sister, who was abducted, along with many others, during a training mission."
    elif True:
        c "We’re mounting an expedition to rescue one of my best friends, who was abducted, along with many others, during a training mission."
    th "Training mission?"
    th "What are you, mercenaries?"
    c "We’re with the Terran Galactic Navy."
    t "At least we were..."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_angry") with vpunch
    th "Get the fuck of out of here, this instant."
    th "My shop isn’t available to Sovereignty-fucks."
    t "Nice going, [p_name]..."
    t "Hey lady, we deserted, all right?"
    t "We’re not part of any fucking Navy any longer, our boy here made sure of that."
    c "Our superiors didn’t seem interested in rescuing anyone and we were headed back to the Naval Academy, leaving all those people to die."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_skeptical") with dissolve
    if game.is_special:
        c "That’s when I decided to steal a ship and go look for Eva, my sister."
    elif True:
        c "That’s when I decided to steal a ship and go look for Eva, my friend."
    c "When they noticed we were leaving, our command cruiser fired several missiles which we evaded by bursting our drive."
    c "And we ended up here."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_laugh") with dissolve
    th "It’s official, you’re monumentally stupid."
    th "So the two of you came here in a TGN light fighter?"
    c "Actually, there’s seven of us in total."
    th "Seven? You’re taking the piss..."
    th "And you’re going to fly away in a light fighter with all those people on board?"
    c "We’re still weighing our options."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_serious") with dissolve
    th "Didn’t they teach you anything useful at the academy?"
    th "Fighters of that class can’t support that many passengers on extended flights."
    th "You’re better off leaving the damn thing in whatever bog you landed it and boarding the next transport freighter out of here."
    c "Leaving you with an abandoned TGN aircraft to sell to the highest bidder?"
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_smile") with dissolve
    th "I see you’re not that stupid, after all."
    th "All right, I’m willing to buy it from you."
    th "I know enough about these babies to be able to retrofit it and the TGN will be none the wiser for it."
    c "Money is nice and all, but you just said so yourself: we need a bigger ship."
    c "I saw one in your yard."
    c "How much ship does our top-of-the-bill military fighter buy us?"
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_serious") with dissolve
    th "Not much, considering the amount of work involved to hide the fact that it’s a stolen TGN bird."
    c "I’m sure we can work something out."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_smile") with dissolve
    th "Are you now?"
    th "Well, as a matter of fact, I might have a ship that’s perfect for you."
    th "It’s a trading ship, older model, but still perfectly capable of long distances."
    th "Now, that fighter might pay for half of it, but I have some cargo that needs to be delivered."
    th "Here’s the deal, I’m going to buy that fighter from you, no further questions asked."
    th "But only if you agree to deliver that cargo for me, using the trading ship you may buy from me."
    th "After you’ve completed the cargo run, I’ll consider the payment done in full."
    c "What’s the catch?"
    c "We’re not smuggling slaves or anything?"
    th "No, nothing like that."
    th "Though I urge you not to get caught by any of the authorities."
    c "So illegal goods?"
    t "Why are you trusting us with those, you just said we were crazy?"
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_serious") with dissolve
    th "It’s better if you don’t know too much about the cargo."
    th "I’ve been sitting on it for quite a while now and there’s nobody in the area who wants to do a transport run."
    th "I guess they have their own interests to take care of."
    th "But the R’o tribe that contacted me is still waiting for it."
    c "What’s stopping us from just flying away with our new ship and keeping the cargo for ourselves?"
    th "Ah yes, I thought about that."
    th "One of you needs to stay behind with me until you return safe and sound."
    c "You’re asking for a bargaining chip?"
    t "A hostage?"
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_smile") with dissolve
    th "It’s the cost of doing business."
    c "I’m not sure if that’s acceptable."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_serious") with dissolve
    th "I’m not sure you have any choice."
    c "There must be something else to sweeten the deal."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thyia_smile") with dissolve
    th "Like what?"

    menu:
        "Propose to talk some more [ThyiaPath]":
            $ ep002_thyia_talk = True
            c "Let’s discuss that over a couple of drinks."
            c "You and I."
            c "Thim, why don’t you explore the town some more?"
            t "What, why?"
            t "Oh..."
            "Disgruntled, Thim left Thyia’s workshop and I followed her further inside."
            scene expression eye_blink("images/ep002/ep002_thyia_talk") with dissolve
            th "So, what kind of sweetness did you have in mind, sugar?"
            c "I don’t know yet."
            c "Have you been living here long?"
            th "A while."
            c "Must get lonely."
            th "Depends, there are a lot of aliens around."
            c "I met one, didn’t seem that friendly."
            th "Well, maybe they grow on you after a while."
            c "Sure..."
            c "You’re not from the Sovereignty?"
            scene expression eye_blink("images/ep002/ep002_thyia_talk_serious") with dissolve
            th "Fuck no, I was born free."
            c "Free?"
            th "On a station somewhere, details are not important."
            th "I’ve had my share of experiences with the Sovereignty though and they’re a bunch of fascists."

            menu:
                "Contest":
                    c "Isn’t that a logical result of running such a vast empire?"
                    th "No, it isn’t."
                    th "I take it you never met the Vrarr or the Paltrowians?"
                    c "Doesn’t ring a bell, though the Paltrowians do."
                    c "But the Paltrowian girl I talked to wasn’t much into politics."
                    scene expression eye_blink("images/ep002/ep002_thyia_talk_skeptical") with dissolve
                    "Thyia stifled a groan of disapproval at my statement, but quickly hid her emotions under the careful facade of disinterest."
                    th "Yeah, I think I know where you spoke to her..."
                "Agree":
                    c "You’re not speaking to a true believer here."
                    c "And I can’t speak for the rest, but I’m pretty sure there’s no love remaining for the Sovereignty after what transpired."
                    th "If you say so..."

            th "But weren’t you negotiating with me?"
            th "All you've done so far is yapping about my life."
            th "Interesting strategy, but a girl has gotta wonder..."
            c "What do you wonder?"
            th "What your angle is?"

            menu:
                "Propose sex [ThyiaPath]":
                    $ ep002_thyia_sex = True
                    c "Well, you're an attractive woman for starters."
                    scene expression eye_blink("images/ep002/ep002_thyia_talk_sexy") with dissolve
                    th "Thank you."
                    th "You’re not looking too bad yourself."
                    c "Glad you mention that."

                    call ep002_thyia_sex from _call_ep002_thyia_sex

                    c "I thought..."
                    th "You'd sweeten the deal, I know."
                    th "You were really sweet, but I don't mix business and pleasure."
                    th "Just deliver the cargo and I'll take that spaceship off your hands, leaving you with a perfect replacement."
                    "Yes, she played me...{w} at least the fucking was good..."
                "Never mind":

                    c "Never mind, I’m going to discuss your proposal with the others."
                    th "Suit yourself."
                    th "Just hurry, because if you’re spotted and one of the locals decides to contact the TGN, I've never met you."
                    th "No wait, I guess you should get the tour of the ship first, before you talk to your friends."

            th "I guess you should get the tour of the ship first, before you talk to your friends."
        "Never mind":
            c "Never mind, I’m going to discuss your proposal with the others."
            th "Suit yourself."
            th "Just hurry, because if you’re spotted and one of the locals decides to contact the TGN, I've never met you."
            th "No wait, I guess you should get the tour of the ship first, before you talk to your friends."

    scene ep002_vulpes_workshop_yard with dissolve
    "The woman took us out into the scrapyard which was mostly filled with junk and one large spaceship."
    "It was one of the ugliest ships I'd ever seen, possessing none of the aggressive sleekness Sovereignty ships commonly possess."
    "The cargo hauler was an old beast, obviously retrofitted with guns and extra armored plating."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_yard_thyia") with dissolve
    th "Guys, meet the Iron Bastard."
    t "Seems like a very apt name."
    c "No shit..."
    th "Looks can be deceiving, boys."
    th "This baby can haul several tons of cargo, while defending herself in a fight."
    th "The previous owner also invested in extra armor."
    th "Some weird alloy, with traces of a couple of good old Earthly metals."
    c "Hence the name?"
    th "The first part, for sure."
    th "The ship can hold up to ten crew members and maybe more, if you're willing to share bunk space."
    c "Sounds real cosy."
    th "Let's take a look inside."
    scene expression eye_blink("images/ep002/ep002_vulpes_bastard_cockpit") with dissolve
    th "This is the bridge, weapons control is here too, but most of it is automated."
    scene expression eye_blink("images/ep002/ep002_vulpes_bastard_crew_quarters") with dissolve
    th "Crew quarters, there's a small kitchen further down the hallway."
    th "Most of this level is taken up by crew bunks."
    th "There are a couple of private quarters, for the captain and any officers."
    scene expression eye_blink("images/ep002/ep002_vulpes_bastard_engine_room") with dissolve
    th "Same deal on the lower level, except for the fact that the engine room and cargo bay are also located here."
    th "The Bastard comes equipped with a regular S-K drive."
    th "Nothing fancy, so I wouldn't recommend attempts to outrun pirates or do some stratospheric flight acrobatics on a regular basis."
    scene expression eye_blink("images/ep002/ep002_vulpes_bastard_cargo_bay") with dissolve
    th "The engine room also gives in-door access to the cargo bay."
    th "Cargo is already loaded, you just need to deliver it on time, at the location I'll provide you."
    th "There's a second bay in the belly of the ship, but it's mostly empty and looks the same as this one, but bigger."
    th "So that concludes the tour."
    th "Any questions?"
    c "You're sure this thing flies?"
    scene expression eye_blink("images/ep002/ep002_vulpes_bastard_cargo_bay_serious") with dissolve
    th "Not the question I was expecting, but yes, I'm sure."
    th "I know it looks old, like one of those cargo planes from the 21st century, but this is a perfectly serviceable ship."
    c "If you say so."
    th "I wouldn't be doing business in this shithole for this long if my word wasn't good."
    th "Now go get your friends and get that cargo to its destination."

    python:
        codex_iron_bastard = add_codex_entry(
            Codex,
            __("Technology"),
            __("Iron Bastard"),
                [
                    __("An aging cargo hauler outfitted with extra armored plating and guns by a string of owners. Part of the name stems from the alloy used in the armored plating, containing metals from Earth."),
                    __("The Iron Bastard is offered as a replacement for the TGN Enfield by Thyia after [p_name] and friends have escaped from the TGN Ypotryll.")
                ]
            )

    scene ep002_vulpes_velox_landed with dissolve
    "We headed back and informed the others."
    "Not everyone was as enthusiastic about the prospect of becoming cargo runners, but I managed to impress the necessity of the situation on all of them."
    "After collecting all of our belongings from the Enfield, we left a locator beacon for Thyia and headed out towards the settlement."
    scene expression eye_blink("images/ep002/ep002_vulpes_workshop_yard_kit") with dissolve
    ki "Wow, [p_name_short], what a piece of junk!"
    c "That's called vintage charm, my friend."
    ki "If you say so..."
    scene ep002_iron_bastard with dissolve
    "We all entered the ship and began the process of choosing a bunk."
    "For some reason both Lilly and I ended up with private quarters, while Céline and Kit shared a room."
    "Thim put his stuff in another multi-bunk room and Vess joined him there, making sure to get the bed on the opposite side of the room."
    scene ep002_iron_bastard_crew with dissolve
    "After everybody settled down, I called the whole crew to the bridge to tell them the plan I had cooked up in the meantime."
    c "This ship will be ours as soon as we do one thing."
    l "The cargo run you mentioned."
    c "Exactly."
    c "After that delivery we're free to do as we please with this ship, as the Enfield covers the rest of the payment."
    c "Because Thyia doesn't trust us completely, I had to agree to one condition."
    scene ep002_iron_bastard_crew_lilly with dissolve
    l "Here it comes..."
    c "One of us has to stay behind as a guarantee."
    l "A hostage, you mean."
    c "Not really..."
    l "I'll do it."
    l "I'll stay behind."
    "I thought Lilly was a little too eager in her willingness to stay behind."
    "Unfortunately, she picked up on my skepticism."
    scene ep002_iron_bastard_crew_lilly_angry with dissolve
    l "What?"
    l "Are you afraid I'll run?"
    c "I don't know."
    l "Where would I go, [p_name_short]?"
    l "We fucking burned all our bridges by running and I know there's no way back."
    l "So you don't have to be afraid I'll go hitchhike back home at the earliest opportunity."
    l "You've condemned us all to staying together."
    c "I..."
    c "So you'll stay behind?"
    scene ep002_iron_bastard_crew_lilly with dissolve
    l "That's what I said, didn't I?"
    l "Just get back as soon as possible."
    scene ep002_iron_bastard_crew_alt with dissolve
    c "Yes, about that."
    c "There's another thing I want to do as soon as possible, maybe even before delivering that cargo."
    c "We have to find out who those women were that kidnapped Eva."
    c "Who are these aliens, do they have a homeworld, what's their angle in abducting random humans?"
    c "So we need someone with experience in the field, someone who can help us further."
    scene ep002_iron_bastard_crew_lilly_surprise with dissolve
    l "Are you really thinking of asking her?!"
    c "Yes, I am."
    l "We haven't seen her in ages, [p_name_short], maybe she hates our guts!"
    c "I'm willing to try, at least we know where she lives."
    scene ep002_iron_bastard_crew_alt with dissolve
    ki "This is all really fascinating guys, but who are you talking about?"
    scene ep002_iron_bastard_crew_lilly with dissolve
    if game.is_special:
        l "[p_name_short] wants to visit our Aunt Nadya, she's a xenologist."
        c "Xenoanthropologist, to be exact."
        l "Right and she lived with us for several years, until she and her daughter suddenly left us."
        l "Mom and Dad had a falling out with her, is the official reason, but it could be anything."
    else:
        l "[p_name_short] wants to visit an old friend of the family, Nadya."
        c "She's a xenologist."
        l "Xenoanthropologist, to be exact."
        c "Right and she lived with us for several years..."
        l "And then she suddenly left, together with Aven."
        l "Leaving us completely alone."

    l "For all we know she doesn't want to have anything to do with us."
    c "Or it could be the reunion of a lifetime, we just don't know."
    scene ep002_iron_bastard_crew_alt with dissolve
    ce "A xenologist does sound like someone who might be able to find out more about those warrior women."
    c "Exactly. She happens to be one of the best in her field."
    c "I know she teaches at a university and I want to visit her there, provided she isn't on some field trip."
    ki "So we're to deliver the cargo first and go to the university later?"
    c "I'm not sure, we might have some leeway on that delivery..."
    t "It didn't sound that way to me..."

    menu:
        "[gr]Deliver cargo first":
            $ ep002_cargo = True
            c "Better deliver that cargo first and be done with it."
            ki "Your decision."
            c "Let’s do that cargo run."
        "Go to university first":
            $ ep002_university = True
            if game.is_special:
                c "I’m afraid we’ll lose momentum if we don’t contact my aunt first."
            else:
                c "I’m afraid we’ll lose momentum if we don’t contact Nadya first."
            ki "Your decision."
            c "Let’s go to the university."

    c "Start the engines, Céline!"
    scene ep002_iron_bastard_clearing with dissolve
    "Thyia had made sure the Iron Bastard was able to taxi out of the scrapyard."
    "As Vulpes Velox consisted mostly of desert, we had no trouble finding a clear spot to take off to the stars."
    scene black with fade

    if ep002_cargo:
        call location_screen (__("Unknown, En route to Nyiruan 12-Beta"), False) from _call_location_screen_8
    else:
        call location_screen (__("Unknown, En route to Ryūjin Prime"), False) from _call_location_screen_9

    call ep002_conversations from _call_ep002_conversations

    if ep002_cargo:
        call ep002_cargo_run from _call_ep002_cargo_run

        play music [ "music/eastminster.ogg", "music/reparateur.ogg" ] fadeout 4 fadein 1.0

        scene ep002_vulpes_workshop_enfield with dissolve
        call location_screen (__("Vulpes Velox, Thyia's Workshop"), True) from _call_location_screen_10

        call ep002_cargo_run_positive from _call_ep002_cargo_run_positive
    else:

        play music [ "music/a-new-year.ogg", "music/floating-cities.ogg" ] fadeout 4 fadein 1.0

        call ep002_university from _call_ep002_university

    if not ep002_university_completed:
        play music [ "music/a-new-year.ogg", "music/floating-cities.ogg" ] fadeout 4 fadein 1.0

        call location_screen (__("Unknown, En route to Ryūjin Prime"), False) from _call_location_screen_11

        if game.is_special:
            "We immediately took off to find my aunt at the university on Ryūjin Prime."
        else:
            "We immediately took off to find Nadya at the university on Ryūjin Prime."

        call ep002_conversations from _call_ep002_conversations_1

        call ep002_university from _call_ep002_university_1
    return

    label ep002_cargo_run_positive:
        "Thyia's workshop looked largely unchanged, though I noticed the Enfield in the scrapyard, already half dismantled."
        scene ep002_vulpes_workshop_thyia_lilly with dissolve
        "I found Thyia and Lilly inside, enjoying a cup of coffee together."
        th "Good, you're back."
        th "Any trouble unloading the cargo?"
        c "A little, but nothing we couldn't handle."
        c "Though we sure as hell earned our reward."
        th "Of course."
        if game.is_special:
            th "Just so you know, your sister has been a great help these past few days."
        else:
            th "Just so you know, Lilly has been a great help these past few days."
        scene ep002_vulpes_workshop_thyia_lilly_smile with dissolve
        l "I just helped you clean and stuff."
        th "Yeah, yeah, I finally had someone intelligent to talk to, that counts for a lot here in these parts."
        th "You may have noticed that I've already towed your previous ship in the yard."
        th "With the delivery of the cargo, the Iron Bastard is officially yours."
        th "I'll change the ownership records right away, give me a sec."
        scene ep002_vulpes_workshop_couch with dissolve
        "Thyia sat behind her console to change the records, while I waited on the couch."
        "I had a good view of the town and noticed a couple of figures approaching the workshop."

        play music "music/pariah-no-melody.ogg" fadeout 4 fadein 1.0

        "During our last visit, the town was deserted and the advancing group looked very determined, menacingly so."
        c "Are you expecting company, Thyia?"
        th "No? Why?"
        c "There's a group of guys about to enter the workshop."
        th "Are they armed?"
        l "Looks like it."
        scene expression eye_blink("images/ep002/ep002_vulpes_workshop_couch_thyia_fear") with dissolve
        th "Fuck!"
        c "Acquaintances of yours?"
        th "More like unwelcome guests."
        scene ep002_vulpes_workshop_thug with dissolve
        $ gl_name = "Thug"
        gl "Helloooo...{w} anybody home???"
        th "You know I am, Glixken."
        $ gl_name = "Glixken"
        gl "Okay, okay..."
        gl "Enough with the niceties."
        scene ep002_vulpes_workshop_thug_serious with dissolve
        gl "We've come to collect."
        th "You gave me another month, that was two weeks ago!"
        gl "Well yeah, I changed my mind."
        th "We had a deal!"
        gl "We did, you borrowed money from us and promised to pay it back after one year, with interest."
        gl "We're now entering the third year and the loan still isn't paid in full."
        gl "So I'd say I pretty much get to make up the fucking rules, don't you?"
        scene ep002_vulpes_workshop_thugs with dissolve
        "The atmosphere was tense as soon as that nasty alien and his friends entered the workshop, but Glixken's last words really ruined the mood..."
        "The grins of the trigger-happy thugs brandishing their energy weapons also didn't inspire much confidence."
        "Lilly and I stood dumb-founded, obviously feeling the same dread."
        scene ep002_vulpes_workshop_thug_serious_alt with dissolve
        gl "I want my money."
        th "I can give you a cut, right now."
        gl "Not good enough."
        th "Look Glixken, I don't have the full amount."
        th "Business is tight and work is scarce."
        gl "Don't give me your fucking excuses, cunt!"
        gl "Pay up!"
        gl "Or I could just cut your throat and take this workshop for myself, sell it off...{w} make some quick credits."
        th "Please Glixken! I need more time!"
        th "I can get you the money."
        scene ep002_vulpes_workshop_thug_smile with dissolve
        gl "Really now?"
        gl "Hear that boys?"
        gl "Well now, I'm not unreasonable."
        gl "We're going to see if there are any good whores to be fucked in this town and come back tomorrow."
        gl "If you don't have the money by then, all of this will be mine, including your body."
        th "Yes, Glixken."
        scene ep002_vulpes_workshop_thugs_leaving with dissolve
        "Thyia stood there with clenched fists, staring at the backs of the thugs leaving her workshop."
        "I had a sour taste in my mouth, this could have ended very badly."
        scene ep002_vulpes_workshop_thugs_lilly_alt with dissolve
        l "Are you okay?"
        th "No."
        l "What are you going to do?"
        th "Fuck."
        th "I don't know."
        th "I think I need to run."
        c "Think so too, that Glixken didn't look like he was joking around."
        th "He's the worst of the worst, not very bright though, otherwise he would have left some guards."
        c "Too sure of himself, I think."
        th "Nevertheless, I never should have taken that loan."
        th "Stupid, stupid, stupid."
        scene ep002_vulpes_workshop_thugs_thyia_packing with dissolve
        "Thyia frantically started gathering several of her personal belongings and destroying anything personal she couldn't take with her."
        "Lilly helped her and tried to reassure the obviously frightened woman."
        "When they were done, Thyia looked at me expectantly."
        scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thugs_thyia") with dissolve
        th "I know you have room for a passenger on the Bastard and I can pay."
        c "You're going to pay with the money we just brought you?"
        th "So what?"

        menu:
            "Accept her [ThyiaPath] [LillyPath]":
                $ ep002_thyia_acceptance = True
                c "Nothing, just appreciating the irony."
                c "You're more than welcome on the Bastard."
                scene expression eye_blink("images/ep002/ep002_vulpes_workshop_thugs_thyia_smile") with dissolve
                l "Especially if it saves you from cunts like Glixken."
                th "Good, let's get moving then!"
            "Refuse her":
                c "Sorry, but no, the crew is large enough as it is."
                th "What, but I can pay?!"
                scene ep002_vulpes_workshop_thugs_thyia_disbelief with dissolve
                l "Why do you always need to be such a fucking cunt, [p_name]?!"
                l "Of course she's coming with us."
                l "Thyia, I invite you to come with us and keep your money."
                scene ep002_vulpes_workshop_thugs_thyia_smile with dissolve
                th "Thank you Lilly and I'll pay for my passage."
                if game.is_special:
                    th "Your brother seems to value money over people, so..."
                else:
                    th "Your friend seems to value money over people, so..."

        stop music fadeout 4.0

        scene ep002_iron_bastard_engine_room_thyia with dissolve
        "Thyia settled for sleeping in the engine room, the hum of the machines was supposedly soothing her, or so she told us."

        python:
            codex_thyia = update_codex_entry(codex_thyia, None,
                [
                    __("Thyia is a salvager and engineer originally working out of her workshop on Vulpes Velox. She was born outside the Sovereignty on a space station and values her independence."),
                    __("After a run-in with Glixken and his crew, she's forced to flee and join the crew on the Iron Bastard.")
                ]
            )

        return

    label ep002_cargo_run_negative:
        play music "music/pariah-no-melody.ogg" fadeout 4 fadein 1.0

        scene ep002_vulpes_workshop_enfield with dissolve
        "When I arrived near Thyia's workshop I immediately sensed there was something amiss."
        scene ep002_vulpes_workshop_thugs_alt with dissolve
        "Entering the shop, I found Lilly and Thyia cornered by a group of thugs pointing guns at them."
        $ gl_name = "Thug"
        gl "And who the fuck is this?"
        l "[p_name], look out!"
        "I just stood there as the leader of the thugs turned to me."
        scene ep002_vulpes_workshop_thugs_alt_serious with dissolve
        gl "Stay right where you are, boy, the girls and I have some business to discuss."
        gl "Now, where were we...{w} right...{w} my money..."
        th "I can give you a cut, Glixken, right now."
        th "The one who just came inside carries it."
        $ gl_name = "Glixken"
        gl "Not good enough."
        th "Look Glixken, I don't have the full amount."
        th "Business is tight and work is scarce."
        scene ep002_vulpes_workshop_thugs_alt_angry with dissolve
        gl "Don't give me your fucking excuses, cunt!"
        gl "Pay up!"
        gl "Or I could just cut your throat and take this workshop for myself, sell it off...{w} make some quick credits."
        th "Please Glixken! I need more time!"
        th "I can get you the money."
        scene ep002_vulpes_workshop_thugs_alt_smile with dissolve
        gl "Really now?"
        gl "Hear that boys?"
        gl "Well now, I'm not unreasonable."
        gl "We're going to see if there are any good whores to be fucked in this town and come back tomorrow."
        gl "If you don't have the money by then, all of this will be mine, including your body and the little girl's too."
        th "Yes, Glixken."
        scene ep002_vulpes_workshop_thugs_leaving_alt with dissolve
        "Defeated, Thyia crawled further into her corner, taking a crying Lilly in her arms."
        "The only thing I could do was stare at the backs of the thugs leaving the workshop, a sour taste in my mouth."

        play music [ "music/eastminster.ogg", "music/reparateur.ogg" ] fadeout 4 fadein 1.0

        scene ep002_vulpes_workshop_thugs_thyia_corner with dissolve
        c "Are you okay?"
        th "No."
        scene ep002_vulpes_workshop_thugs_thyia_corner_angry with vpunch
        th "What the fuck took you so long?!"
        th "It was supposed to be a simple cargo run...{w} Two days tops."
        th "Instead you're gone for days!"
        scene ep002_vulpes_workshop_thugs_lilly with dissolve
        l "I was worried sick."
        c "We got side-tracked..."
        scene ep002_vulpes_workshop_thugs_thyia_corner_angry_alt with vpunch
        th "You what?!"
        l "Unbelievable..."
        th "Do you know how dangerous Glixken and his crew are?!"
        c "I didn’t know I was on the clock, I agreed to do that cargo run."
        c "You didn’t specify the time."
        c "Who the fuck were those guys anyway?"
        th "Glixken and his crew."
        th "Nasty fucker, does a lot of debt collecting."
        th "I never should have taken that loan."
        th "Fuck!"
        scene ep002_vulpes_workshop_thugs_lilly with dissolve
        l "What are you going to do?"
        th "I don't know."
        th "I think I need to run."
        c "Think so too, that Glixken didn't look like he was joking around."
        c "He also didn't seem very bright, because he didn't leave any guards, that works in our advantage."
        c "Gather your things, I think it's time to leave while those fuckers are still drunk on cheap pussy."
        scene ep002_vulpes_workshop_thugs_thyia_packing with dissolve
        "Thyia frantically started gathering several of her personal belongings and destroying anything personal she couldn't take with her."
        "Lilly helped her and tried to reassure the obviously frightened woman."
        "When they were done, Thyia looked at me expectantly."
        scene ep002_vulpes_workshop_thugs_thyia with dissolve
        th "I know you have room for a passenger on the Bastard and I can pay."
        c "You're going to pay with the money we just brought you?"
        th "So what?"

        menu:
            "Accept her [ThyiaPath] [LillyPath]":
                $ ep002_thyia_acceptance = True
                c "Nothing, just appreciating the irony."
                c "You're more than welcome on the Bastard."
                scene ep002_vulpes_workshop_thugs_thyia_smile with dissolve
                l "Especially if it saves you from cunts like Glixken."
                th "Good, let's get moving then!"
            "Refuse her":
                c "Sorry, but no, the crew is large enough as it is."
                scene ep002_vulpes_workshop_thugs_thyia_disbelief with dissolve
                th "What, but I can pay?!"
                l "Why do you always need to be such a fucking cunt, [p_name]?!"
                l "Of course she's coming with us."
                l "Thyia, I invite you to come with us and keep your money."
                scene ep002_vulpes_workshop_thugs_thyia_smile with dissolve
                th "Thank you Lilly and I'll pay for my passage."
                if game.is_special:
                    th "Your brother seems to value money over people, so..."
                else:
                    th "Your friend seems to value money over people, so..."

    stop music fadeout 4.0

    scene ep002_iron_bastard_engine_room_thyia with dissolve
    "Thyia settled for sleeping in the engine room, the hum of the machines was supposedly soothing her, or so she told us."

    python:
        codex_thyia = update_codex_entry(codex_thyia, None,
            [
                __("Thyia is a salvager and engineer originally working out of her workshop on Vulpes Velox. She was born outside the Sovereignty on a space station and values her independence."),
                __("After a run-in with Glixken and his crew, she's forced to flee and join the crew on the Iron Bastard.")
            ]
        )

    return

    label ep002_thyia_sex:
        scene ep002_thyia_kiss with vpunch
        "I didn’t hesitate and stepped towards her, grabbing her and kissing her full on the lips."
        th "Mmmm, easy now."
        "Something in her eyes made me grab her in my arms and before we knew it, we were kissing and I was fiddling with the clasps of her work clothes."
        scene ep002_thyia_naked with dissolve:
            yalign 1.0
            ease 8 yalign 0.01
        $ renpy.pause()
        "As her garments fell to the floor, more and more of her gorgeous body became visible."
        "She voiced no protest, so I continued kissing her, eventually making my way down to her breasts."
        show ep002_thyia_nipples with dissolve
        "Her nipples were already hard and when I took one of them in my mouth, Thyia let out a moan of delight."
        "Suckling them, elicited her first proactive response, as she pressed my head closer to her bosom."
        scene ep002_thyia_navel with dissolve
        "I let my tongue trail from her heaving breasts down to her navel."
        th "There’s a bed just right there."
        scene ep002_thyia_bed with dissolve
        "Wordlessly I pushed her on the bed and continued to kiss her, targeting her sex by pushing her legs apart and flicking my tongue over her moist labia."
        "Her back arched as I concentrated on her pussy and treated her to the most intense pussy licking I was capable of."
        th "Right there!"
        th "Take me, [p_name]!"
        show ep002_thyia_bed_penetrate with dissolve
        "I didn’t hesitate and pulled her closer towards my cock, sliding easily past her wet lips."
        th "Yes, that’s right!"
        "The events of the past days flashed through my mind and I had a hard time concentrating on making love to Thyia."
        "She appeared to notice and looked deeply into my eyes."
        scene ep002_thyia_bed_penetrate_closeup with dissolve
        th "Don’t think. Fuck."
        scene ep002_thyia_bed_fuck with dissolve
        "Her words helped me overcome my sudden absentmindedness and I doubled down on fucking her tight pussy."
        "Thyia clearly started to enjoy herself, her moans and cries stimulating me to reward her with even more intense thrusts."
        scene ep002_thyia_bed_fuck_alt with dissolve
        th "Keep doing that...{w} Please keep doing that!!!"
        "That plea triggered an orgasm so violent I temporarily lost all presence of where I was."

        menu:
            "Creampie [gr]\[Thyia Creampie\]":
                $ ep002_thyia_creampie = True
                scene ep002_thyia_bed_creampie with vpunch
                "I had no choice but to keep fucking her and my seed flowed inside of her with those last desperate thrusts."
                scene ep002_thyia_bed_creampie_alt with flash
                with flash
                "Thyia wore a satisfied smile on her face as I pulled out my cock, making way for a steady stream of cum from her convulsing vagina."
                "The sight of her creamy pussy nearly made me want to fuck her all over again."
            "Body":
                scene ep002_thyia_bed_body with flash
                with flash
                "At the last moment, I pulled out and smothered her belly and breasts with my seed, looking at Thyia with a satisfied smile."
                "The sight of her body nearly made me want to fuck her all over again."
            "Facial":
                scene ep002_thyia_bed_facial with flash
                with flash
                "At the last moment, I pulled out and couldn't resist covering her face."
                "Thyia's satisfied smile quickly flashed into a surprised scowl before turning into a lewd grin."
                th "Ah, you're one of those guys?"
                c "I guess I am."
                "Thyia clearly didn't mind all that cum on her face and licked eagerly at the corners of her mouth."
                "The sight nearly made me want to fuck her all over again."
        scene expression eye_blink("images/ep002/ep002_thyia_bed_post") with dissolve
        th "I'd love to chat, but I think you've got some work to do."
        c "Right..."
        $ renpy.end_replay()
        return

    label ep002_cargo_run:
        scene ep002_nyiruan with dissolve
        play music [ "music/black-bird.ogg", "music/firesong.ogg" ] fadeout 4 fadein 1.0
        call location_screen (__("Nyiruan 12-Beta, Approach"), True) from _call_location_screen_12

        "After we punched in the coordinates we received from Thyia we were ready for anything."
        if not ep002_university_completed:
            "But the trip turned out to be uneventful, just a series of jump-gates."
            "The S-K drive worked, there were no space pirates, no shooting matches...{w} nothing."
        else:
            "But the trip turned out to be uneventful, just a series of jump-gates, no space pirates, no shooting matches...{w} nothing."

        python:
            codex_nyiruan = add_codex_entry(
                Codex,
                __("Planets"),
                __("Nyiruan 12-Beta"),
                [
                    __("Homeworld of the R'o, a tribal species of humanoids. The planet has a moderate climate and is very green and fertile, allowing for the lifestyle the R'o tribes still practice - farming, hunting and gathering.")
                ]
            )

        "This was looking like the easy cargo run Thyia promised."
        scene ep002_nyiruan_cargo with dissolve
        c "Okay, the crates should already be loaded on haulers, so it should be a matter of driving those to the center of the settlement."
        c "After that, we collect the payment, return to Thyia and go our merry way."
        ki "Sounds good."
        t "Sounds too easy."
        c "Thanks for that, Thim..."
        c "Anyway, the R'o tribe ahead is waiting for us."
        c "Let's get moving."
        scene ep002_nyiruan_cargo_jungle with dissolve
        "The lush vegetation made movement a little difficult, but it was a nice change from the barren worlds we visited so far."
        "The alien jungle was teeming with wildlife and there were hundreds of different flowers I never knew existed."
        "When we arrived in the village, the elders were already waiting for us, they were a decidedly male bunch."

        python:
            codex_ro = add_codex_entry(
                Codex,
                __("Species"),
                __("R'o"),
                [
                    __("The R’o are a tribal race without much interest in outer space. A few of them can be encountered on space stations, as can be expected. Most of the R’o live and die on their home planet, Nyiruan 12-Beta, after a hard life of farming or hunting and gathering."),
                    __("[p_name] and crew encounter a tribe of R'o during their cargo delivery run on Nyiruan.")
                ],
                "images/codex/Ro.webp"
            )

        scene ep002_nyiruan_cargo_tribe with dissolve
        c "Greetings, we've brought a shipment of the goods you require."
        "Before one of the elders could speak, I saw their eyes grow extremely wide."
        "I've come to learn that this is never a good sign, regardless of which type of alien you're dealing with."
        $ man_name = "R'o Chieftain"
        $ man_portrait = "side_man"
        man "Are those...{w} women..."

        menu:
            "[gr]Truth":
                c "Yes, this here is Céline and Jade is over there."
                scene ep002_nyiruan_cargo_tribe_angry with dissolve
            "Lie":
                $ ep002_ro_lie = True
                c "No, those are just human males with different outward characteristics."
                scene ep002_nyiruan_cargo_tribe_angry with vpunch
                man "Don't play me for a fool, those are women!"
        man "The cargo is defiled!"
        man "A woman's touch has ruined this shipment."
        c "Is this some kind of obscure bargaining tactic?"
        man "Bargaining?"
        man "No."
        man "We R'o do not bargain."
        man "We will pay you the full amount, as soon as this shipment is cleansed."
        c "Cleansed?"
        if ep002_ro_lie:
            man "You will do penance in the Pit of Despair."
        else:
            man "One of your male crew members will have to do penance in the Pit of Despair."

        c "Pit of Despair..."
        c "This penance ritual, is it dangerous?"
        man "No, only for the faint of heart."
        scene ep002_nyiruan_cargo_tribe_surrounded with dissolve
        "At that point we were completely surrounded by a band of angry-looking R'o warriors carrying spears and other pointy things."
        "Thyia didn't provide us with weapons, other than the guns mounted on our ship which was a little too far away."
        "Royally fucked is what we were."

        if not ep002_ro_lie:
            menu:
                "[gr]Go yourself":
                    c "I will bear the punishment of this misstep."
                "Let Thim go":
                    $ ep002_pit_thim = True
                    c "A captain shouldn't leave his crew, Thim will do the penance."
                    scene ep002_nyiruan_cargo_tribe_thim with dissolve
                    t "What the fuck [p_name_short]?!"
                    t "You're sending me to that pit?"
                    scene ep002_nyiruan_cargo_tribe_surrounded with dissolve
                    c "I'm sure it won't be that bad."
                    scene ep002_nyiruan_cargo_tribe_thim with vpunch
                    t "Fuck you, you fucking piece of shit!"

        man "Good, my men will escort you to the entrance of the Pit."
        man "They will stand guard until the night has passed and you emerge again."
        man "Your debt will be paid."

        if ep002_pit_thim:
            "The guards escorted Thim to the caves, leaving the me to complete the business side of the transaction."
            scene ep002_nyiruan_iron_bastard with dissolve
            "We returned to the Bastard to get some sleep and wait for Thim to emerge from the cave again."
            "I'd be lying if I didn't feel a hint of guilt for throwing Thim before the wolves."
            "He might not die, but who knows what awaited him in those caves..."
            "During breakfast the ship's computer indicated that there was someone at the entrance."
            scene ep002_nyiruan_iron_bastard_thim with dissolve
            "It turned out to be Thim, accompanied by two grim-faced warriors."
            c "Thim, did you..."
            t "Fuck you, [p_name]."
            "Thim never spoke of what happened during his night in the Pit of Despair, especially not to me."
            "Someone once described Thim's face to me when asked about that fateful night, a shit-faced grin was not the expression I expected..."
        else:
            "The guards escorted me to the caves, leaving the others to complete the business side of the transaction."
            scene ep002_nyiruan_cave with dissolve
            "The cave wasn't very far from the R'o village and I was pushed rather unceremoniously inside the dark mound of the cave entrance."
            "I was about to ask questions to the guards, but they immediately launched into some incomprehensible, monotonous prayer, while barring the entrance."
            scene ep002_nyiruan_cave_interior with dissolve
            "As there was no light I decided to head deeper into the cave, feeling my way by touching the walls, which were slick with moisture."
            "After stumbling for a few meters I noticed the faint, orange flickering of torch light up ahead."
            "I walked further until I stood at the precipice of a large chamber where I knew in an instant I'd hit the jackpot."
            scene ep002_nyiruan_cave_women with dissolve
            $ dee_name = "R'o Woman"
            dee "Ah, a male."
            dee "Have you come to do penance?"
            c "I have."
            dee "Come over here then and make yourself comfortable among us."
            scene expression eye_blink("images/ep002/ep002_nyiruan_cave_dee") with dissolve
            dee "My name is D'ee."
            $ dee_name = "D'ee"
            c "Are there only women down here?"
            dee "Mostly, the children and the older ones caring for them are further down below."
            c "But why?"
            dee "A decree of Our Holiness."
            c "Decree?"
            dee "A few years ago, our shaman started preaching from a gospel he said he'd received directly from the gods."
            dee "They told him that women were impure and that males should dominate the earth."
            dee "His sermons weren't very successful until our old chieftain died and was replaced with his son, a true believer in the new religious doctrine."
            scene expression eye_blink("images/ep002/ep002_nyiruan_cave_dee_sad") with dissolve
            dee "So through a series of decisions by the new chieftain, we were becoming more and more marginalized."
            dee "Until one night, all the women were rounded up and taken to this cave here, where we've lived ever since."
            c "Damn..."
            c "Surely this isn't sustainable in the long run, if there are no children being born?"
            scene expression eye_blink("images/ep002/ep002_nyiruan_cave_dee") with dissolve
            dee "Sometimes one of the males is sent down to do penance."
            dee "We then do what we can to keep the tribe alive."
            dee "The men have already come for any boys that have been born here and taken them topside when they're at a certain age."
            scene expression eye_blink("images/ep002/ep002_nyiruan_cave_dee_sad") with dissolve
            dee "But it isn't sustainable, I agree."

            menu:
                "Offer to help them [DeeRoPath]":
                    $ ep002_ro_help = True
                    c "Is there anything I could do to help?"
                    c "Couldn't you escape?"
                    scene expression eye_blink("images/ep002/ep002_nyiruan_cave_dee_smile") with dissolve
                    dee "We're with too many, it would take hours to empty the caves and the males would surely notice."
                    dee "Our only hope would be to contact another tribe and tell them of our situation, I'm sure they would intervene to stop this madness."
                    c "Do you have a tribe in mind?"
                    dee "Yes, my uncle is chieftain of another tribe, I could convince him."
                    c "So you should escape, alert him."
                    dee "Maybe...{w} But how?"
                    c "Those guards will be coming for me tomorrow morning, right?"
                    c "I'll create a diversion and you try to sneak out of the cave and flee to that uncle of yours."
                    dee "That sounds dangerous, but it might work."
                    c "No harm in trying, right?"
                    scene expression eye_blink("images/ep002/ep002_nyiruan_cave_dee_sad") with dissolve
                    dee "We will be punished, for sure, but it might all be worth it."
                    scene ep002_nyiruan_cave_women_alt with dissolve
                    "D'ee conferred with the other women to gauge the amount of support for the escape plan."
                    scene expression eye_blink("images/ep002/ep002_nyiruan_cave_dee") with dissolve
                    dee "A majority is in favor of the plan, I'm going to do it."
                    c "Great, I hope this will help you get out of this ridiculous situation."
                    dee "Thank you, you're very kind."
                    dee "We'd like to reward you for your selfless actions."
                    c "No need..."
                    scene expression eye_blink("images/ep002/ep002_nyiruan_cave_dee_smile") with dissolve
                    dee "Are you sure?"
                    dee "You seem sexually compatible with us...{w} we could all have...{w} a good time..."

                    menu:
                        "Have sex with them [DeeRoPath]":
                            $ ep002_ro_orgy = True
                            c "It would be an honor."

                            call ep002_ro_orgy from _call_ep002_ro_orgy

                            scene ep002_nyiruan_cave_sleep with dissolve
                            "As the entertaining part of the night had passed, it was time for me to do some play-acting and help D'ee escape."
                        "Decline the offer":
                            c "There's no need for that, I just want to help you."
                            dee "That's a shame, but we understand and won't pressure you."
                            scene ep002_nyiruan_cave_sleep_alt with dissolve
                            "Despite D'ee's promises I didn't sleep very well."
                            "Every time I opened my eyes the hungry stares of the women were there and I could swear I felt soft hands touching my skin when I was asleep."
                            "One of the women told us that morning had broken, so it was time for me do some play-acting."

                    scene ep002_nyiruan_cave_guards_panic with dissolve
                    "As soon as the guards came down, the women started to panic."
                    $ woman_name = "R'o Woman"
                    woman "He's not waking up!"
                    woman "You have to do something."
                    "Through my semi-closed eyes I made out two guards, the number that was stationed outside."
                    "They approached me with caution as I began to shudder and convulse."
                    woman "Do something!"
                    $ man_name = "R'o Guard"
                    $ man_portrait = "side_man"
                    scene ep002_nyiruan_cave_guards_panic_approach with dissolve
                    man "What can we do woman, we know nothing about humans?!"
                    "I continued my poor impression of an epileptic seizure until I was sure D'ee had enough time to sneak out of the cave and opened my eyes dramatically."
                    scene ep002_nyiruan_cave_guards_panic_shock with vpunch
                    c "YOU!"
                    man "What?"
                    c "Oh...{w} Nothing, just a little fit."
                    c "I have those from time to time."
                    scene ep002_nyiruan_cave_guards_panic_serious with dissolve
                    man "You're strange beings, human."
                    c "I won't argue with that."
                    c "Am I free to leave now?"
                    man "We're to escort you to your ship."
                    c "Good."
                    scene ep002_nyiruan_cave_guards_woman with dissolve
                    c "Thank you ladies, for the hospitality."
                    c "I hope you won't have to remain in these caves forever."
                    woman "Thank you [p_name], good luck on your journey."
                    "The guards clearly didn't have the patience for any more niceties and motioned me to follow them."
                    scene ep002_nyiruan_iron_bastard with dissolve
                    "They took me straight to the Iron Bastard and left me before the entrance door."
                    "Céline was the first to greet me and after sharing a few details with the crew we headed back to Vulpes Velox."
                "Do nothing":
                    c "I'm not sure if I can gift you new offspring..."
                    scene expression eye_blink("images/ep002/ep002_nyiruan_cave_dee_smile") with dissolve
                    dee "We're not asking you to, but we're really bored here too..."
                    dee "You seem sexually compatible with us...{w} Would you..."

                    menu:
                        "Have sex with them [DeeRoPath]":
                            $ ep002_ro_orgy = True
                            c "It would be an honor."

                            call ep002_ro_orgy from _call_ep002_ro_orgy_1

                            scene ep002_nyiruan_cave_sleep with dissolve
                            "As the entertaining part of the night had passed, it was time for me to get some sleep and wait for the guards to arrive again."
                        "Decline the offer":
                            c "Sorry, but I just want to get through the night and be on my way."
                            dee "That's a shame, but we won't pressure you."
                            scene ep002_nyiruan_cave_sleep_alt with dissolve
                            "Despite D'ee's promises I didn't sleep very well."
                            "Every time I opened my eyes the hungry stares of the women were there and I could swear I felt soft hands touching my skin when I was asleep."
                            scene ep002_nyiruan_cave_guards with dissolve
                            "Two guards entered the cave and motioned me to follow them."
                            scene ep002_nyiruan_iron_bastard with dissolve
                            "They took me straight to the Iron Bastard and left me before the entrance door."
                            "Céline was the first to greet me and after sharing a few details with the crew we headed back to Vulpes Velox."

            python:
                entry = [
                    __("R'o woman encountered by [p_name] in the Pit of Despair when he does penance.")
                ]

                if ep002_ro_help:
                    entry.append(__("With the help of [p_name] she escapes the Pit in order for her to contact her uncle and possibly save the tribe from the male-centric ideology that's slowly destroying it."))

                codex_dee = add_codex_entry(
                    Codex,
                    __("Characters"),
                    __("D'ee"),
                    entry,
                    "images/codex/Dee.webp"
                )

        scene black with fade

        call location_screen (__("Unknown, En route to Nyiruan 12-Beta"), False) from _call_location_screen_13

        $ ep002_cargo_completed = True

        return

    label ep002_ro_orgy:
        if _in_replay:
            $ dee_name = "D'ee"

        scene ep002_nyiruan_cave_laying with dissolve
        dee "Lie down with us then and relax..."
        "I did as I was told and immediately felt soft hands undressing me."
        scene ep002_nyiruan_cave_naked with dissolve
        "The women worked quickly, but delicately and I just gaped at the writhing mass of naked bodies right inside my grasp."

        if is_patreon() and renpy.has_label("extra_scene_03") and not _in_replay:
            call extra_scene_03 from _call_extra_scene_03

        scene ep002_nyiruan_cave_kiss with dissolve
        "D'ee pressed her cool lips on mine and we exchanged a kiss fueled by mutual longing and desire."
        dee "Just relax and let us fuck...{w} you..."
        scene ep002_nyiruan_cave_breasts with dissolve
        "She presented her breasts, nipples erect, and I started licking and sucking them, eliciting moans from the alien woman."
        "My view was obscured by the beautiful ass of another woman, but I knew they'd freed my growing erection, because I felt the tell-tale sensation of tongue tips darting over the glans."
        scene ep002_nyiruan_cave_suck with dissolve
        "Uttering coherent speech was becoming harder and harder, so I resorted to encouraging grunts."
        "My roar echoed throughout the cave as one of the women engulfed my dripping cock with her mouth and started sucking."
        scene ep002_nyiruan_cave_breasts_kiss with dissolve
        "D'ee's breasts were wet from my attentions and she bowed down for another kiss."
        dee "Have you ever tasted R'o pussy?"
        c "N-never..."
        scene ep002_nyiruan_cave_pussy with dissolve
        "D'ee proceeded to lower herself on my face and I felt her sex press against my lips."
        "I eagerly opened my mouth and stuck out my tongue to split her labia and ate her out."
        show ep002_nyiruan_cave_suck_alt with dissolve
        "All the while, no less than three women were taking turns sucking my dick, making it very hard not to blast their faces with a fountain of cum."
        "R'o women got apparently very wet, because D'ee's juices started flowing freely over my face as I licked her ferociously."
        show ep002_nyiruan_cave_pussy_closeup_alt with dissolve
        dee "Keep going like that!"
        dee "[p_name], oh [p_name]!"
        scene ep002_nyiruan_cave_pussy_closeup with dissolve
        "Alien as she was, I knew D'ee was close to orgasm, so I doubled my efforts."
        "When she released, my face was flooded with her fragrant ejaculate and I continued to lick her until the flow stopped."
        show ep002_nyiruan_cave_fisting with dissolve
        "The cave was filled with sounds of women moaning as I pleasured D'ee and the others pleasured themselves."
        "The women going down on my cock were playing with my balls and licking my taint, driving me absolutely crazy."
        "I couldn't stave off my orgasm any longer and let go of any remnant of bodily control."
        scene ep002_nyiruan_cave_suck_facial with dissolve
        "D'ee crept off my face, revealing my cock splashing semen over the faces of the three eager R'o women."
        scene ep002_nyiruan_cave_suck_facial_kiss with dissolve
        "They began to kiss each other and lap up my cum, savoring the taste, as soon as I was done ejaculating."
        dee "Are you up for more?"
        c "Fuck yes!"
        "Having been up close with R'o pussy, I yearned to fuck one, preferably multiple, long and hard."
        "It was quickly decided among the women that D'ee was granted the privilege of getting fucked first."
        scene ep002_nyiruan_cave_penetrate with dissolve
        "She grabbed my dick resolutely and pushed it against her moist lips, relishing the feeling."
        scene ep002_nyiruan_cave_fuck with vpunch
        "The R'o woman then took my full length at once, her ass bouncing beautifully on impact."
        "D'ee obviously enjoyed the feeling of my hard cock penetrating her depths, because she smiled at me in delight and started to ride me."
        "I didn't think she could get any wetter, but pretty soon we were both covered in the nectar flowing from her pussy."
        "Her natural lubricant allowed me to penetrate her deeply, something that gave D'ee immense pleasure."
        scene ep002_nyiruan_cave_fuck_alt with dissolve
        "As I played with her full breasts and firm nipples she moaned long and hard, her voice echoing in the night."
        dee "Aaaah!!!"
        dee "Ooooh!!!"

        scene ep002_nyiruan_cave_guards with dissolve
        $ man_name = "R'o Guard"
        $ man_portrait = "side_man"
        man "It has begun."
        scene ep002_nyiruan_cave_guards_alt with dissolve
        man "Terrible..."

        scene ep002_nyiruan_cave_fuck_closeup with dissolve
        "D'ee shifted her body to allow me to plunge new-found depths inside her love tunnel."
        "The feeling aroused D'ee even more and her pussy juices became a steady flow, a puddle forming beneath our bodies."
        "The R'o woman began to tremble and convulse, her body overtaken by her orgasm."
        scene ep002_nyiruan_cave_fuck_closeup_orgasm with vpunch
        "The other women looked in awe as D'ee screamed at the top of her lungs, experiencing a climax so intense that she nearly lost control of her senses."
        "Incapacitated as D'ee was, I took over and continued to pound her wet hole, close to orgasming myself."

        menu:
            "Creampie [gr]\[Dee Creampie\]":
                $ ep002_dee_creampie = True
                scene ep002_nyiruan_cave_fuck_creampie with vpunch
                "My cock belonged inside her and when the moment of release came I stayed firmly inside her cunt as the seed started flowing."
                scene ep002_nyiruan_cave_fuck_creampie_alt with flash
                with flash
                "Having released my last volley of cum, I slipped out of D'ee's gash and a splash of her ejaculate, mixed with mine started to drip on the ground."
            "Body":
                "Wanting to make my mark on her, I opted for her beautifully toned belly and pulled out as soon as my seed started flowing."
                scene ep002_nyiruan_cave_fuck_body with flash
                with flash
                "While releasing volleys of cum on her belly, D'ee's gash released a splash of her ejaculate, mixing it with mine."
        scene ep002_nyiruan_cave_fuck_post with dissolve
        "Thoroughly exhausted, I lay a while with D'ee in my arms, the other women looking a little jealous at us."
        "After an hour of laying with D'ee, a murmur started, several women were conferring among themselves."
        scene ep002_nyiruan_cave_line with dissolve
        "From the corner of my eye I saw several women lining themselves up, getting on all fours, asses in the air."
        "One R'o woman came up to D'ee and me and looked at us inquisitively."
        $ woman_name = "R'o Woman"
        $ woman_portrait = "side_woman"
        woman "We know it's selfish, but we want you too, [p_name]..."
        "Something about that display of asses and the way she phrased the question made me forget all exhaustion."
        scene ep002_nyiruan_cave_line_kiss with dissolve
        "I got up and kissed the woman."
        c "I want you all too!"
        "She smiled and positioned herself on all fours next to the other women."
        scene ep002_nyiruan_cave_line_penetrate with dissolve
        "I grabbed one of the women's flanks and pushed my cock against her pussy."
        "She moaned in encouragement, so I didn't hesitate and thrust my dick between the lips of her gash."
        scene ep002_nyiruan_cave_line_fuck with dissolve
        "The woman wasn't as wet as D'ee, but the sublime, ribbed feel of her tunnel was just as good."
        "Because I'd orgasmed twice already I'd gotten better at delaying my next orgasm, so I was able to treat her pussy right until it was time to go to her lovely neighbor."
        show ep002_nyiruan_cave_line_fuck_alt with dissolve
        "Fucking women in series like that was a strange notion at first, but the myriad of feelings their pussies gave me, more than made up for the awkwardness."
        show ep002_nyiruan_cave_line_fuck_closeup with dissolve
        "One of the women was even wetter than D'ee and I had a hard time keeping my cock inside her."
        "By that time I was so horny, I smeared her ejaculate all over her body and mine, so our skin glistened beautifully in the torchlight."
        scene ep002_nyiruan_cave_line_fuck_virgin with dissolve
        "I felt I could fuck these glorious women for hours on end, even start at the beginning again, until I entered the last girl."
        "She was the youngest woman in the row, with beautiful, perky breasts and a very sweet face."
        scene ep002_nyiruan_cave_line_fuck_virgin_dee with dissolve
        "D'ee came up to me and whispered something in my ear."
        dee "Be gentle with her...{w} she's still a virgin..."
        $ woman_name = "R'o Virgin"
        woman "I'm ready for him, mother..."
        "Her sweet voice nearly made me lose it and I bent over to kiss her first, to shake the feeling of immediate release."
        show ep002_nyiruan_cave_line_fuck_virgin_breasts with dissolve
        "My fingers trailed her small breasts, lingering at the nipples and she gasped in ecstasy."
        c "You're very beautiful."
        "The girl just giggled and wiggled slightly with her ass."
        scene ep002_nyiruan_cave_line_fuck_virgin_ass with dissolve
        "I took the hint and lay my erection between her ass cheeks."
        "Trailing my finger over her spine I noticed that she was holding her breath, with my other hand I pushed my cock against her labia."
        scene ep002_nyiruan_cave_line_fuck_virgin_penetrate with dissolve
        "The girl gritted her teeth as my glans entered her pussy, but she was already so wet I didn't have any trouble sliding inside her."
        "Her cherry was a treat, very tight and very moist."
        "Already with my first thrusts I had her moaning with pleasure."
        show ep002_nyiruan_cave_line_fuck_virgin_fuck with dissolve
        "I grabbed one of her firm breasts with one hand and grabbed the youthful flesh of her buttocks with the other and fucked her boldly."
        "She was salivating as each thrust went deeper inside her hitherto unexplored vagina."
        "Her ejaculate was leaking in abundance on the floor and streaming along her muscular thighs."
        scene ep002_nyiruan_cave_line_fuck_virgin_fuck_closeup with dissolve
        woman "Aaah! [p_name]!"
        "I knew I had her close, so I fucked her a little faster, grabbing her ass and pulling her firmly onto my cock."
        "Her hooded eyes fluttered open as she was hit with the overpowering waves of her first vaginal orgasm."
        scene ep002_nyiruan_cave_line_fuck_virgin_fuck_closeup_orgasm with dissolve
        woman "[p_name]! I'm cumming!!!"
        "The sound of her sweet voice, edged with a little disbelief, combined with her constricting vagina, made me spent my seed."
        menu:
            "Creampie [gr]\[Ro Creampie\]":
                $ ep002_ro_virgin_creampie = True
                scene ep002_nyiruan_cave_line_fuck_virgin_fuck_creampie with vpunch
                "Determined her deflowering should be a proper fuck, I remained inside her and let my semen flow freely."
                scene ep002_nyiruan_cave_line_fuck_virgin_fuck_creampie_alt with flash
                with flash
                woman "Mmmm, it f-feels so w-warm!"
                scene ep002_nyiruan_cave_line_fuck_virgin_fuck_post with dissolve
                "We both collapsed to the floor, where I held the still-trembling girl tightly a smile on her face, pussy juice and seed dripping out of her on the floor."
            "Body":
                "Determined to reward her body after such a thorough deflowering, I pulled my cock out and sprayed her back with a wealth of semen."
                scene ep002_nyiruan_cave_line_fuck_virgin_fuck_body with flash
                with flash
                woman "Mmmm, there's so much of it!"
                scene ep002_nyiruan_cave_line_fuck_virgin_fuck_post with dissolve
                "We both collapsed to the floor, where I held the still-trembling girl tightly a smile on her face, pussy juice dripping out of her on the floor."
        "After a while, I heard D'ee's voice from afar."
        "I was a little worried the women were up for more, because I was completely battered after so many hours of pleasure."
        scene ep002_nyiruan_cave_line_fuck_post_dee with dissolve
        dee "Morning is about to break."
        dee "I speak for all the women, when I say thank you for the incredible night you've granted us."
        c "I feel I should thank you!"
        dee "No need, we just took what we wanted..."
        c "Trust me, it felt as good for me as it did for you."
        dee "Good, in that case it was an exchange as equals."
        scene black with fade
        $ renpy.end_replay()
        return

    label ep002_university:
        scene ep002_ryujin_docks with dissolve
        call location_screen (__("Ryūjin Prime, Docks"), True) from _call_location_screen_14

        if not ep002_cargo_completed:
            if game.is_special:
                "Thyia didn't lie, the ship had a functioning S-K drive and after a series of tedious jump-gate crossings, we arrived as planned in orbit of Ryūjin Prime where Aunt Nadya was supposed to live and work."
            else:
                "Thyia didn't lie, the ship had a functioning S-K drive and after a series of tedious jump-gate crossings, we arrived as planned in orbit of Ryūjin Prime where Nadya was supposed to live and work."
        else:
            if game.is_special:
                "After a series of tedious jump-gate crossings, we arrived as planned in orbit of Ryūjin Prime where Aunt Nadya was supposed to live and work."
            else:
                "After a series of tedious jump-gate crossings, we arrived as planned in orbit of Ryūjin Prime where Nadya was supposed to live and work."

        "As soon as we docked our ship's computer was bombarded with information about the planet."
        "Ryūjin Prime was a planet consumed by a vast metropolis, everything else was just a barren wasteland where nobody dared to live."

        python:
            if game.is_special:
                codex_ryujin_prime = add_codex_entry(
                    Codex,
                    __("Planets"),
                    __("Ryūjin Prime"),
                    [
                        __("Location: Cat’s Eye Nebula"),
                        __("The majority of Ryūjin Prime is covered in a large metropolis, while the rest of the planet is virtually uninhabitable. The weather is artificially controlled and the climate is therefore very moderate, unless that control slips and the heavy rains start to fall."),
                        __("The most important feature of Ryūjin Prime is the university, home to an incredible amount of aliens, all devoted to the pursuit of science."),
                        __("Ryūjin Prime is also the home of [p_name]'s aunt and cousin after they left Tuolovi.")
                    ]
                )
            else:
                codex_ryujin_prime = add_codex_entry(
                    Codex,
                    __("Planets"),
                    __("Ryūjin Prime"),
                    [
                        __("Location: Cat’s Eye Nebula"),
                        __("The majority of Ryūjin Prime is covered in a large metropolis, while the rest of the planet is virtually uninhabitable. The weather is artificially controlled and the climate is therefore very moderate, unless that control slips and the heavy rains start to fall."),
                        __("The most important feature of Ryūjin Prime is the university, home to an incredible amount of aliens, all devoted to the pursuit of science."),
                        __("Ryūjin Prime is also the home of Professor Nadya Grivans after she left Tuolovi.")
                    ]
                )
        "Céline waded through all the offers about entertainment, ship repairs, jobs to find the address of the university."
        if game.is_special:
            "I decided on a small party consisting of Céline and Vess to go look for my aunt and cousin."
        else:
            "I decided on a small party consisting of Céline and Vess to go look for Nadya and Aven."
        scene ep002_ryujin_docks_vess_celine with dissolve
        ve "I'm glad you chose me to come with you."
        ve "I felt so cooped up in the Enfield and now in the Bastard."
        c "I can understand that."
        c "Have you ever been off-planet?"
        ve "No, I haven't, not since..."
        c "Ryūjin is going to be an experience in that case."
        c "It's going to be crowded, loud and there'll be lots to see."
        c "Please stick with either Céline or me, because the streets might not be so kind to the lost."
        ve "Understood!"
        ce "Ready to head out?"
        ce "I've loaded the coordinates on our communicators, it should be easy to find."
        scene ep002_ryujin_city with dissolve
        "Even I wasn't fully prepared for the hectic experience that Ryūjin Prime was."
        "The enormous flow of people, crisscrossing each other in some delicate ballet, really took some time getting used to."
        "Céline's locator signal provided us with the necessary directions and it didn't take us long to reach the campus of Ryūjin Prime University."
        scene ep002_ryujin_university with dissolve
        $ man_name = "Robot"
        $ man_portrait = "side_man"
        man "Good day sir, how may I be of service?"
        if game.is_special:
            c "We're looking for Professor Nadya Valenmann de Lonval."
        else:
            c "We're looking for Professor Nadya Grivans."
        man "Residence 42-ZB."
        man "Shall I load the coordinates onto one of your devices?"
        c "Yes please."
        scene ep002_ryujin_university_residences with dissolve
        "Following the locator signal provided by the concierge bot, we left the common area of the campus, missing out on most of the sights and entered the residential zones."
        c "This should be it."
        "I pushed the door buzzer and we waited."
        "Nothing happened for several minutes."
        "I was about to hit the buzzer again when the door finally opened."
        scene expression eye_blink("images/ep002/ep002_ryujin_university_residences_door") with dissolve
        $ av_name = "Woman"
        av "Hmm?"
        if game.is_special:
            c "Hi, we're looking for Professor Valenmann de Lonval."
        else:
            c "Hi, we're looking for Professor Grivans."
        av "Are you her students?"
        c "No, we're not, we have a question for her."
        av "She isn't here, try again later."
        c "Wait!"
        c "I'm her nephew, it's really important that we speak to her."
        av "I told you she isn't here, but you're welcome to wait if you want to."
        av "Coffee?"
        scene ep002_ryujin_university_apartment with dissolve
        "After we shuffled into the small apartment, the terse woman got busy making coffee for us."
        if game.is_special:
            "Something about her was familiar, she looked vaguely like a raven-haired mix between Eva and Lilly."
        else:
            "Something about her was familiar, a distant memory, long forgotten."
        av "Here you go."
        av "Nadya is teaching at the moment, she'll be back in a few hours."
        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_kitchen") with dissolve
        av "I didn't get your names?"
        c "[p_name]."
        ce "Céline, pleased to meet you."
        ve "I'm Vess."
        if game.is_special:
            av "I'm Aven, Nadya's daughter."
        else:
            av "I'm Aven, a friend of Nadya's."
        $ av_name = "Aven"

        if game.is_special:
            av "Hello cousin [p_name_short]..."
        else:
            av "Hello [p_name_short]..."
        c "Aven! It's been a while!"

        if game.is_special:
            python:
                codex_aven = add_codex_entry(
                    Codex,
                    __("Characters"),
                    __("Aven"),
                    [
                        __("Raven-haired cousin of [p_name] and the daughter of Nadya. A skilled fighter and diplomat, Aven often accompanies her mother on scientific expeditions.")
                    ],
                    "images/codex/Aven.webp"
                )
        else:
            python:
                codex_aven = update_codex_entry(codex_aven, None,
                    [
                        __("Childhood friend of [p_name]. Was taken away from Tuolovi by Nadya as a child. A skilled fighter and diplomat, Aven often accompanies Nadya on scientific expeditions.")
                    ]
                )

        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_aven_smile") with dissolve
        av "You can sure say that."
        av "I think the last time we saw each other was when you were eight and I was nine years old?"
        c "I think so."
        c "I mostly remember crying, because you were both gone one day."
        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_aven") with dissolve
        av "Yeah, that was...{w} sudden..."
        c "How have you been all these years?"
        if game.is_special:
            av "Good, Mom quickly established herself as a teacher here at the academy, eventually obtaining a professorship."
        else:
            av "Good, Nadya quickly established herself as a teacher here at the academy, eventually obtaining a professorship."
        av "So I was raised here mostly."
        c "You're a xenologist too?"
        av "Hah, not really."
        if game.is_special:
            av "I know a little about it, because of Mom."
        else:
            av "I know a little about it, because of Nadya."
        av "I accompany her on her travels, to keep her safe."
        ve "You're like...{w} her bodyguard?"
        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_aven_smile") with dissolve
        av "Something like that."
        av "I know how to handle myself in a fight, but I get to play the diplomat often too."
        if game.is_special:
            av "Diplomacy is not one of my mother's strong suits."
        else:
            av "Diplomacy is not one of her strong suits."
        c "I don't remember her as being impatient."
        av "She isn't, except when it comes to her work, she can be very demanding..."
        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_aven_sit") with dissolve
        if game.is_special:
            av "How are your sisters, [p_name]?"
        else:
            av "How are Lilly and Eva, [p_name]?"
        c "Lilly is fine, she couldn't come along unfortunately."
        c "Eva is...{w} she..."
        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_aven_sit_concern") with dissolve
        av "Fuck...{w} She's all right, isn't she?"
        c "We don't know."
        c "We were on a training mission and ran into an ambush, Eva got taken..."
        av "Fuck."
        av "By whom?"
        c "Unclear."
        if game.is_special:
            c "We hope Aunt Nadya can identify the creatures that took Eva from us."
        else:
            c "We hope Nadya can identify the creatures that took Eva from us."
        av "She just might, let's hope she comes back soon."
        scene ep002_ryujin_university_apartment_aven_alt with dissolve
        "Aven poured us more coffee while we waited another two hours."
        "Finally, the door opened and a woman stood in the doorway looking directly at me."
        na "[p_name]?!"
        scene ep002_ryujin_university_apartment_nadya_hug with dissolve
        "Disregarding the girls in the room, Nadya ran towards me and took me in her arms."
        na "Is it really you?"
        if game.is_special:
            c "Yes, Aunt Nadya, it's me."
        else:
            c "Yes, Nadya, it's me."

        python:
            if game.is_special:
                codex_nadya = add_codex_entry(
                    Codex,
                    __("Characters"),
                    __("Nadya"),
                    [
                        __("Mother of Aven and sister to Agust. After her sudden departure from Tuolovi she settled as a professor in Xenoanthropology at the university on Ryūjin Prime, where she lives with her daughter.")
                    ],
                    "images/codex/Nadya.webp"
                )
            else:
                codex_nadya = add_codex_entry(
                    Codex,
                    __("Characters"),
                    __("Nadya"),
                    [
                        __("Family friend who left Tuolovi together with Aven under mysterious circumstances. After her unwilling departure from Tuolovi she settled as a professor in Xenoanthropology at the university on Ryūjin Prime, where she lives with Aven.")
                    ],
                    "images/codex/Nadya.webp"
                )

        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_nadya") with dissolve
        na "It's been so long."
        na "Why did you decide to come and visit?"
        if game.is_special:
            na "How are your sisters?"
        else:
            na "How are Lilly and Eva?"
        na "Are you still at the academy?"
        "I was a little unsure which question I should answer first, so I started telling her about Eva, her other questions would be answered soon enough."
        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_nadya_sad") with dissolve
        na "Abducted...{w} Dreadful..."
        na "How's Lilly coping with all this?"
        if game.is_special:
            c "She's a strong girl, Aunt Nadya, you know that."
        else:
            c "She's a strong girl, Nadya, you know that."
        na "Yes, she was always feisty."
        c "That hasn't changed."
        na "Eva was always more cautious..."
        na "What a terrible situation."
        c "We were hoping you could shed some light on the situation."
        c "Maybe you've heard of a race of humanoid warrior women."
        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_nadya_unsure") with dissolve
        c "The ones we saw were really muscular and using very old weaponry, swords and stuff."
        c "They looked just like human women, just more angular and very aggressive."
        na "Never heard of anything like that, but maybe the university library has more on the topic."
        na "Why don't you head back to your ship while I research some things."
        na "As soon as I have news, I'll come find you in the docks."
        c "Sounds good."
        c "And thank you, I know this is coming totally out of the blue and..."
        scene expression eye_blink("images/ep002/ep002_ryujin_university_apartment_nadya_smile") with dissolve
        if game.is_special:
            na "Nonsense, you're family."
            na "Of course I'm going to help you, no matter what."
        else:
            na "Nonsense, it's Eva we're talking about."
            na "Of course I'm going to help you, no matter what."
        scene ep002_ryujin_docks with dissolve
        "We left the apartment and headed back to our ship where another round of waiting began."
        "Very late in the evening, after eating a quick dinner, we received a signal."
        scene ep002_ryujin_docks_nadya with dissolve
        "Nadya was standing outside, together with Aven."
        c "Hi!"
        c "Did you find anything?"
        na "Unfortunately, no."
        na "But I have an idea who might help us further."
        na "Having researched the warrior women, I've come to the conclusion they might not be a different race."
        na "They could be augmented humans, or something like that."
        c "Augmented humans?"
        c "That's illegal, right?"
        scene ep002_ryujin_docks_nadya_serious with dissolve
        na "Not everywhere..."
        na "There were several clandestine research programs dealing with experiments on humans."
        na "Information is scarce, but that's where my source comes in."
        na "The guy I know is a little peculiar and he always insists on contact through me personally."
        na "So Aven and me are coming with you, if that's all right."
        c "That's fantastic!"
        na "I have some savings so I can pay for our upkeep for some time, but my university salary isn't much, so I'm not sure how long I can manage."
        c "We'll figure something out."
        scene ep002_ryujin_docks_nadya_smile with dissolve
        na "That's the spirit!"
        c "Aven, you're looking a little doubtful."
        av "No, it's fine."
        if game.is_special:
            av "I'm just a little overwhelmed by the suddenness of Mom's decision."
        else:
            av "I'm just a little overwhelmed by the suddenness of Nadya's decision."
        av "But I'm sticking with her, no matter what."
        c "In that case, welcome aboard!"

        $ ep002_university_completed = True

        scene black with fade
        if not ep002_cargo:
            call location_screen (__("Unknown, En route to Nyiruan 12-Beta"), False) from _call_location_screen_15
        else:
            scene ep002_ryujin with dissolve
            call location_screen (__("Unknown, En route to Ryūjin Prime"), True) from _call_location_screen_16

        call ep002_conversations from _call_ep002_conversations_2

        if not ep002_cargo:
            call ep002_cargo_run from _call_ep002_cargo_run_1

            call ep002_cargo_run_negative from _call_ep002_cargo_run_negative_1

            call ep002_conversations from _call_ep002_conversations_3

        "I called everyone to the cockpit to hear the plan for our next destination."
        scene expression eye_blink("images/ep002/ep002_iron_bastard_cockpit") with dissolve
        c "So, Nadya has an idea who we should contact to get more information about those warrior women."
        na "I do."
        scene expression eye_blink("images/ep002/ep002_iron_bastard_cockpit_na") with dissolve
        na "It’s my strong suspicion that the women aren’t alien at all, but rather augmented human beings."
        na "Of course I could be wrong and you were ambushed by an undocumented race of humanoid women, but it seems unlikely."
        na "Several clandestine laboratories have existed over the years, experimenting on humans."
        scene ep002_iron_bastard_cockpit with dissolve
        ce "That’s illegal, right?"
        scene expression eye_blink("images/ep002/ep002_iron_bastard_cockpit_na") with dissolve
        na "Experimenting on any sentient life form is illegal."
        na "But that hasn’t stopped people from doing it, the Sovereignty included."
        na "Most of those experiments never leave the lab or are hunted down and destroyed very quickly."
        ki "To keep things under wraps."
        na "Exactly."
        na "If those women are the result of experimentation, it seems that they have somehow successfully escaped that fate."
        na "Research into these kinds of experimentation programs is virtually non-existent in academic circles."
        scene ep002_iron_bastard_cockpit_na_alt with dissolve
        c "Why?"
        na "Because you quickly deal with rumors, hearsay and outright conspiracy theories."
        na "And if you hit upon the truth, it could become very dangerous as the parties involved in the experimentation might take an interest in your research."
        c "So you have to be either very daring or mad to research those topics?"
        na "Exactly."
        na "And Karan Hreir is both."
        na "He’s the one we’re going to visit."
        na "The journey isn’t going to be easy, because his home is located inside an asteroid field and the man is notoriously paranoid."
        scene expression eye_blink("images/ep002/ep002_iron_bastard_cockpit") with dissolve
        t "Great..."
        c "Well, at least we were warned beforehand."
        c "I’m sure Mr. Hreir will listen to reason."
        na "I sure hope so."
        scene black with fade

        play music "music/hiding-your-reality.ogg" fadein 1.0 fadeout 4

        "We set course to the asteroid field, ready to meet Karan Hreir."
        scene ep002_iron_bastard_exterior with dissolve
        call location_screen (__("Hreir Asteroid Base, Approach"), True) from _call_location_screen_17

        "As we made the final jump to our location, the ship suddenly shuddered and alarms started to go off."
        scene ep002_iron_bastard_cockpit_alarm with vpunch
        c "What is happening?"
        ce "We were hit by something!"
        ce "Asteroid!"
        c "Damage?"
        ce "Minimal, our armor took most of the beating."
        ce "But there’s a whole field of those buggers right in front of us."
        scene ep002_iron_bastard_cockpit_asteroids with dissolve
        "Céline then pulled up the image of the asteroid field and we were all shocked by the whirling mass of rocks before us."
        c "How the fuck are we going to navigate in that?"
        ki "Dumb luck?"

        jump episode003

        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
