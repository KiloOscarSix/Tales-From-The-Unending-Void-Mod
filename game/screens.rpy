

default persistent.modGalleryUnlock = False









init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)








init -501 screen relationship_toggle():
    if gui.relationship_screen and ("ep001_celine_talk" in globals() and ep001_celine_talk) and not _in_replay:
        imagebutton:
            auto "gui/button/button_relationships_%s.png" action Show("relationships")
            keyboard_focus False
            keysym "r"
            xalign 1.0
            yoffset 15
            xoffset -25

init -1 python:
    config.overlay_screens.append("relationship_toggle")














init -501 screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background im.MatrixColor("gui/textbox.png", im.matrix.brightness(0) * im.matrix.opacity(float(preferences.say_screen_visibility) / float(100)), xpos=320, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height


    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    outlines [ (absolute(1), (0, 0, 0), absolute(1), absolute(1)) ]
    kerning 1

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    outlines [ (absolute(1), (0, 0, 0), absolute(1), absolute(1)) ]
    kerning 1











init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

    outlines [ (absolute(2), (0, 0, 0, 210), absolute(1), absolute(1)) ]
    kerning 1

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

    outlines [ (absolute(2), (0, 0, 0, 210), absolute(1), absolute(1)) ]
    kerning 2









init -501 screen choice(items):
    style_prefix "choice"

    if len(items) > 4:
        vpgrid:
            cols 2

            for i in items:
                textbutton i.caption action i.action
    else:
        vbox:
            for i in items:
                textbutton i.caption action i.action



define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    yalign 0.90
    yanchor 1.0

    spacing gui.choice_spacing

init -1 style choice_vpgrid:
    spacing 25
    xmaximum 1900

    xalign 0.5
    yalign 0.8

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







init -501 screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            if not _in_replay and 'Codex' in globals() and Codex._size_all is not 0:
                textbutton _("Codex") action ShowMenu("encyclopaedia_list", Codex) keysym "c"
            textbutton _("Prefs") action ShowMenu('preferences')




init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")











init -501 screen navigation():

    if renpy.get_screen("main_menu") and main_menu:
        hbox:
            style_prefix "main_menu"

            xalign 0.5
            xanchor 0.5
            spacing 40

            use navigation_buttons
    else:
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            use navigation_buttons






init -501 screen navigation_buttons():
    if main_menu:

        textbutton _("Start") action Start()

    else:

        textbutton _("History") action ShowMenu("history")

        textbutton _("Save") action ShowMenu("save")

    textbutton _("Load") action ShowMenu("load")

    if not main_menu and not _in_replay:
        textbutton _("Codex") action ShowMenu("encyclopaedia_list", Codex)

    textbutton _("Preferences") action ShowMenu("preferences")

    if _in_replay:

        textbutton _("End Replay") action EndReplay(confirm=True)

    if not _in_replay:
        textbutton _("Scene Gallery") action ShowMenu("scenes")

    if not main_menu:

        textbutton _("Main Menu") action MainMenu()

    textbutton _("About") action ShowMenu("about")

    if renpy.variant("pc"):


        textbutton _("Help") action ShowMenu("help")


        textbutton _("Quit") action Quit(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








init -501 screen main_menu():
    tag menu



    style_prefix "main_menu"

    add gui.main_menu_background


    frame




    frame style "main_menu_navigation_frame":
        use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    add Image("gui/tales_from_the_unending_void.png", xalign=0.5, ypos=205)

    hbox:
        xpos 1.0
        xoffset -40
        yalign 0
        yoffset 20
        xanchor 1.0

        if is_patreon() and renpy.has_label("extra_scene_01"):
            if game.is_special:
                text "v[config.version] • Taboo Edition, Extra Scenes" size 20 color gui.selected_color
            else:
                text "v[config.version] • Standard Edition, Extra Scenes" size 20 color gui.selected_color
        else:
            if game.is_special:
                text "v[config.version] • Taboo Edition" size 20 color gui.selected_color
            else:
                text "v[config.version] • Standard Edition" size 20 color gui.selected_color

    button:
        style "patreon_button"

        xpos 30
        yalign 1.0
        yoffset -20
        xanchor 0

        action OpenURL('https://www.patreon.com/perverteer')
        has hbox
        add "gui/patreon.png"
        text "Support me on  Patreon:\nwww.patreon.com/perverteer" style "patreon_button_text"


    imagebutton:
        xpos 1.0
        yalign 1.0
        xoffset -40
        yoffset -40
        xanchor 1.0

        action OpenURL('https://www.patreon.com/perverteer')

        auto "gui/perverteer_%s.png"












init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text

init -1 style main_menu_navigation_frame:
    xfill True
    yalign 0.75
    background None

init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

init -1 style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

init -1 style main_menu_title:
    properties gui.text_properties("title")

init -1 style main_menu_version:
    properties gui.text_properties("version")

init -1 style main_menu_button:
    properties gui.button_properties("navigation_button")

init -1 style main_menu_button_text:
    properties gui.button_text_properties("navigation_button")
    hover_color gui.hover_color
    selected_color gui.selected_color
    idle_color gui.selected_color

    outlines [ (absolute(2), (0, 0, 0), absolute(1), absolute(1)) ]

init -1 style patreon_button is gui_button

init -1 style patreon_button_text is main_menu_button_text:
    size 22
    xpos 15
    ypos 27
    hover_color gui.hover_color
    selected_color gui.selected_color
    idle_color gui.selected_color










init -501 screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 420
    yfill True

init -1 style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

init -1 style game_menu_viewport:
    xsize 1380

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 15

init -1 style game_menu_label:
    xpos 75
    ysize 180

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


init -501 screen relationships():
    tag menu
    style_prefix "relationships"

    zorder 100


    modal True

    python:
        relationships = [
            {
                'name': 'Céline',
                'image': 'gui/portraits/portrait_celine.webp',
                'romance': "Yes" if celine_romance else "No",
                'pregnancy': "Yes" if celine_pregnant else "No",
                'visible': True if ("ep001_celine_talk" in globals() and ep001_celine_talk) else False,
            },
            {
                'name': 'Jade',
                'image': 'gui/portraits/portrait_jade.webp',
                'romance': "Yes" if jade_romance else "Yes {size=-5}(Submissive){/size}" if jade_submissive else "No",
                'pregnancy': "Yes" if jade_pregnant else "No",
                'visible': True if ("ep001_jade_hj" in globals() and ep001_jade_hj) or ("ep002_jade_talk" in globals() and ep002_jade_talk) else False,
            },
            {
                'name': 'Vess',
                'image': 'gui/portraits/portrait_vess.webp',
                'romance': "Yes" if vess_romance else "No",
                'pregnancy': "Yes" if vess_pregnant else "No",
                'visible': True if ("ep002_vess_talk" in globals() and ep002_vess_talk) else False,
            },
            {
                'name': 'Thyia',
                'image': 'gui/portraits/portrait_thyia.webp',
                'romance': "Yes" if thyia_romance else "No",
                'pregnancy': "Yes" if thyia_pregnant else "No",
                'visible': True if ("ep002_cargo_completed" in globals() and ep002_cargo_completed) else False,
            },
            {
                'name': 'Lilly',
                'image': 'gui/portraits/portrait_lilly.webp',
                'romance': "Yes" if lilly_romance else "No",
                'pregnancy': "Yes" if lilly_pregnant else "No",
                'visible': True if ("ep001_lilly_talk" in globals() and ep001_lilly_talk) else False,
            },
            {
                'name': 'Ziv',
                'image': 'gui/portraits/portrait_ziv.webp',
                'romance': "Yes" if ziv_romance else "No",
                'pregnancy': "Yes" if ziv_pregnant else "No",
                'visible': True if ("ep004_skarak" in globals() and ep004_skarak) else False,
            },
            {
                'name': 'Raene',
                'image': 'gui/portraits/portrait_raene.webp',
                'romance': "Yes" if raene_romance else "No",
                'pregnancy': "No",
                'visible': True if ("ep004_skarak" in globals() and ep004_skarak) else False,
            },
            {
                'name': 'Aven',
                'image': 'gui/portraits/portrait_aven.webp',
                'romance': "Yes" if aven_romance else "No",
                'pregnancy': "Yes" if aven_pregnant else "No",
                'visible': True if ("ep002_university_completed" in globals() and ep002_university_completed) else False,
            },
            {
                'name': 'Nadya',
                'image': 'gui/portraits/portrait_nadya.webp',
                'romance': "Yes" if nadya_romance else "No",
                'pregnancy': "Yes" if nadya_pregnant else "No",
                'visible': True if ("ep002_university_completed" in globals() and ep002_university_completed) else False,
            },
            {
                'name': 'Eva',
                'image': 'gui/portraits/portrait_eva.webp',
                'romance': "Yes" if eva_romance else "No",
                'pregnancy': "Yes" if eva_pregnant else "No",
                'visible': False,
            }
        ]


    frame:
        style_prefix "relationships"

        xfill True
        yfill True
        background Color(gui.muted_color).replace_opacity(0.95)

        has vbox
        hbox:
            xfill True

            text _("Relationships"):
                style "main_menu_title"
                xalign 0
                yoffset 40
                xoffset 75

            textbutton _("Close"):
                xalign 1.0
                yoffset 40
                xoffset -40
                action Hide("relationships")

        frame:
            xsize 1760
            xoffset 75
            yoffset 175
            background None

            has hbox:
                xfill True
                spacing 50
                box_wrap True
                box_wrap_spacing 50

            for character in relationships:
                if character["visible"]:
                    hbox:
                        xsize 485
                        spacing 5

                        add character['image']

                        vbox:
                            hbox:
                                spacing 15

                                text character['name'] italic True size 50 color gui.accent_color font gui.interface_text_font

                            text _("Relationship: %s") % (character['romance'])
                            if "pregnancy" in character:
                                text _("Pregnant: %s") % (character['pregnancy'])

    key "r" action Hide("relationships")

init -1 style relationships_button_text:
    size 30
    idle_color gui.accent_color
    hover_color gui.hover_color

init -1 style relationships_grid:
    spacing 60
    xalign 0.5
    yalign 0.5

init -1 style relationships_text:
    size 30

init -1 style relationships_item_text:
    size 150




init 9 python:
    scene_gallery_page = 0
    if not is_patreon():
        scene_gallery_page = 1

    if 'p_name' not in locals():
        p_name = "Camran"
        p_name_short = "Cam"

init -501 screen scenes():
    tag menu






    $ episode = scene_gallery[scene_gallery_page]

    use game_menu(_("Scene Gallery")):

        style_prefix "scenes"

        vbox:
            vbox:
                ymaximum 740
                xfill True


                text episode['title'] font "fonts/Oswald-Bold.ttf" color gui.accent_color size 30

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    xfill True
                    yfill True
                    yoffset 25

                    has vpgrid:
                        xfill True
                        cols 3
                        spacing 25

                    for scene_object in episode['scenes']:
                        button:
                            action Replay(scene_object['label'], {}, locked=persistent.modGalleryUnlock)
                            frame:
                                if renpy.seen_label(scene_object['label']) or persistent.modGalleryUnlock == False:
                                    add Frame(scene_object['image'], 0, 0)
                                else:
                                    add Frame("gui/locked.png", 0, 0)
                            text scene_object['text']

            hbox:
                style_prefix "scenes_buttons"
                yoffset 40
                spacing 15
                box_wrap True
                box_wrap_spacing 15




                for page in range(1, len(scene_gallery)+1):
                    if page is 1 and is_patreon():
                        textbutton __("Extras") action SetVariable("scene_gallery_page", page-1)
                    elif not page is 1:
                        textbutton __("Ep")+str(page-1) action SetVariable("scene_gallery_page", page-1)

                if persistent.modGalleryUnlock:
                    textbutton "Unlock Scenes":
                        action SetVariable("persistent.modGalleryUnlock", False)
                else:
                    textbutton "Lock Scenes":
                        action SetVariable("persistent.modGalleryUnlock", True)



init -1 style scenes_frame:
    hover_background gui.hover_color
    xsize 364
    ysize 210

init -1 style scenes_text:
    size 20
    yalign 1.0
    hover_color gui.hover_color

init -1 style scenes_button:
    xsize 375
    ysize 260

init -1 style scenes_scrollbar:
    unscrollable "hide"

init -1 style scenes_vscrollbar:
    unscrollable "hide"








init -501 screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:
            $ game_name = config.name
            label "[game_name!t]"
            text _("Version ") + _("[config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n" font gui.text_font size 30

            label _("Music")

            null height 30

            vpgrid:
                xfill True
                cols 4
                spacing 30
                mousewheel False
                side_xalign 0.5

                for track in gui.tracks:
                    vbox:
                        xsize 500

                        text track["title"] font gui.text_font size 30
                        text track["composer"] font gui.text_font size 25
                        text _("{a=[track[website]]}[track[website]]{/a}") font gui.text_font size 20
                        text _("License: ") + _("{a=[track[license_url]]}[track[license]]{/a}") font gui.text_font size 20

            null height 60

            text _("{size=-8}Uses portions of the {a=https://github.com/jsfehler/renpy-encyclopaedia}Encyclopaedia Framework for Ren'Py{/a} by jsfehler") font gui.text_font
            text _("{size=-8}Ashtar Flying Disk, Federation Interceptor HN48, Endor Battlecruiser, Sky Ranger Domminator, Titan Class II Cargo Ship, Wraith Raider Starship, Eagle 5 Transport models created by {a=https://www.renderosity.com/?uid=767619}sevein/Herminio Nieves{/a}") font gui.text_font
            text _("{size=-8}Crucero Space Army model created by {a=http://www.sharecg.com/pf/full_uploads.php?pf_user_name=thomasjeromenewton}Antonio Amador{/a}") font gui.text_font
            text _("{size=-8}Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") font gui.text_font


define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size











init -501 screen save():
    tag menu


    use file_slots(_("Save"))


init -501 screen load():
    tag menu


    use file_slots(_("Load"))


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:

                        action If(renpy.get_screen("save"), true=Show("save_name_modal", accept=FileSave(slot)), false=FileLoad(slot))

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileSaveName(slot):
                            style "slot_name_text"

                        hbox:
                            xsize 375

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")) font gui.text_font:
                                style "slot_time_text"

                            key "save_delete" action FileDelete(slot)

                            if FileLoadable(slot):
                                imagebutton:
                                    idle "gui/button/button_delete_idle.png"
                                    hover "gui/button/button_delete_hover.png"

                                    action FileDelete(slot)

                                    xalign 1.0


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 75
    ypadding 5

init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")



init -501 screen save_name_modal(accept=NullAction()):
    modal True
    add Solid("#000000") alpha 0.8

    frame:
        padding gui.confirm_frame_borders.padding
        xsize 650
        xalign 0.5
        yalign 0.5

        has vbox:
            xalign 0.5
            spacing 20

        label _("Please name your save:"):
            text_color gui.text_color
            xalign 0.5

        null height 10

        input size 40 color gui.hover_color default store.save_name changed set_save_name length 25 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 -/*":
            yalign 1.0
            xalign 0.5
            xysize (550, 40)

        textbutton _("Save game"):
            xalign 0.5
            action [accept, Hide("save_name_modal")]

        key "game_menu" action Hide("save_name_modal")

init -1 python:
    def set_save_name(new_name):
        store.save_name = new_name








init -501 screen preferences():
    tag menu


    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if 'p_name' in globals():
                    vbox:
                        style_prefix "buttons"
                        label _("Player Names")
                        textbutton _("Name: ")+p_name action Show("custom_input_modal", label_text="Change name", variable_name="p_name")
                        textbutton _("Nickname: ")+p_name_short action Show("custom_input_modal", label_text="Change nickname", variable_name="p_name_short")

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))




                vbox:
                    style_prefix "pref"
                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("Russian") action Language("russian")


                vbox:
                    style_prefix "radio"
                    label _("Notifications")
                    textbutton _("Show") action gui.SetPreference("codex_notifications", True)
                    textbutton _("Hide") action gui.SetPreference("codex_notifications", False)

                vbox:
                    style_prefix "radio"
                    label _("Relationships")
                    textbutton _("Show") action gui.SetPreference("relationship_screen", True)
                    textbutton _("Hide") action gui.SetPreference("relationship_screen", False)

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                    label _("Dialog Box Visibility")

                    bar value FieldValue(_preferences, "say_screen_visibility", range=100, max_is_zero=False, style="slider", step=1, action=Function(say_screen_visibility))

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style buttons_label is pref_label
init -1 style buttons_label_text is pref_label_text
init -1 style buttons_button is gui_button
init -1 style buttons_button_text is gui_button_text
init -1 style buttons_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 338

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_slider:
    xsize 525

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 675









init -501 screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what font gui.text_font

        if not _history_list:
            label _("The dialogue history is empty."):
                style "history_empty"



define -1 gui.history_allow_tags = set()


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.") font gui.text_font

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.") font gui.text_font

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.") font gui.text_font

    hbox:
        label _("Escape")
        text _("Accesses the game menu.") font gui.text_font

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.") font gui.text_font

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.") font gui.text_font

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.") font gui.text_font

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.") font gui.text_font

    hbox:
        label "H"
        text _("Hides the user interface.") font gui.text_font

    hbox:
        label "S"
        text _("Takes a screenshot.") font gui.text_font

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.") font gui.text_font

    hbox:
        label "R"
        text _("Shows the relationships screen") font gui.text_font

    hbox:
        label "C"
        text _("Shows the codex") font gui.text_font


init -501 screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.") font gui.text_font

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.") font gui.text_font

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.") font gui.text_font

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.") font gui.text_font

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.") font gui.text_font


init -501 screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 375
    right_padding 30

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    font gui.text_font
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide("notify")


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos
    xalign 1.0

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")
    color gui.hover_color









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







init -1 style pref_vbox:
    variant "medium"
    xsize 675



init -501 screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()
        textbutton _("Hide") action ui.callsinnewcontext("_hide_windows")

init -1 style window:
    variant "small"
    background "gui/phone/textbox.png"

init -1 style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

init -1 style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 510

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 600

init -1 style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

init -1 style slider_pref_vbox:
    variant "small"
    xsize None

init -1 style slider_pref_slider:
    variant "small"
    xsize 900
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
