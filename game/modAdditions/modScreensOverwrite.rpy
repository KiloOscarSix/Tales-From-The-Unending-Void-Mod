screen navigation_buttons():
    if main_menu:
        textbutton _("Start") action Start()

    else:
        textbutton _("Mod Options") action Show("modOptions")

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

screen scenes():
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
