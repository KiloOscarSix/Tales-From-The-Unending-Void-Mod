init python:
    import re

    gr = "{color=#0f0}"
    red = "{color=#f00}"
    blue = "{color=#00f}"

define pathDict = {
    "CelinePath":"{color=#0f0}[Celine Path]",
    "JadePath":"{color=#0f0}[Jade Path]",
    "JadeLovePath":"{color=#0f0}[Jade Love Path]",
    "JadeSubPath":"{color=#0f0}[Jade Sub Path]",
    "ThimPath":"{color=#0f0}[Thim Path]",
    "VessPath":"{color=#0f0}[Vess Path]",
    "KitPath":"{color=#0f0}[Kit Path]",
    "LillyPath":"{color=#0f0}[Lilly Path]",
    "NadyaPath":"{color=#0f0}[Nadya Path]",
    "AvenPath":"{color=#0f0}[Aven Path]",
    "ThyiaPath":"{color=#0f0}[Thyia Path]",
    "DeeRoPath":"{color=#0f0}[Dee&Ro Path]",
    "RaenePath":"{color=#0f0}[Raene Path]",
    "ZivPath":"{color=#0f0}[Ziv Path]",
    "LuzanePath":"{color=#0f0}[Luzane Path]",
    "HannahPath":"{color=#0f0}[Hannah Path]",
    "RahiaPath":"{color=#0f0}[Rahia Path]",
    "CaesePath":"{color=#0f0}[Caese Path]",
}

define EndRelationship = "{color=#f00}[End Relationship]"

init python:
    for key, value in pathDict.iteritems():
        setattr(store, key, value)

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    tag menu
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 50
        spacing 50

        text "Walkthrough Options" style "modTextHeader" xcenter 0.5

        text "Turn on and off character paths" style "modTextBody" xcenter 0.5

        frame:
            yoffset -25
            padding (20, 20)
            vpgrid:
                cols 5
                spacing 50
                style_prefix "check"

                for key, value in pathDict.iteritems():
                    $ wtText = re.findall('[A-Z][^A-Z]*', key)
                    textbutton " ".join(wtText):
                        action ToggleVariable(key, true_value=value, false_value="")

    textbutton _("Return") action ShowMenu("save"), Hide("modWalkthroughOptions"):
        yanchor 1.0
        pos (100, 1030)
        text_style "modTextButtonHeader"
