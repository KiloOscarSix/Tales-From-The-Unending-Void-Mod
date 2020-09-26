init python:
    mod = Character("OscarSix", color="#0f0")

    gr = "{color=#0f0}"
    red = "{color=#f00}"
    blue = "{color=#00f}"

    CelinePath = "{color=#0f0}[Celine Path]"
    JadePath = "{color=#0f0}[Jade Path]"
    JadeLovePath = "{color=#0f0}[Jade Love Path]"
    JadeSubPath = "{color=#0f0}[Jade Sub Path]"
    ThimPath = "{color=#0f0}[Thim Path]"
    VessPath = "{color=#0f0}[Vess Path]"
    KitPath = "{color=#0f0}[Kit Path]"
    LillyPath = "{color=#0f0}[Lilly Path]"
    NadyaPath = "{color=#0f0}[Nadya Path]"
    AvenPath = "{color=#0f0}[Aven Path]"
    ThyiaPath = "{color=#0f0}[Thyia Path]"
    DeeRoPath = "{color=#0f0}[Dee&Ro Path]"
    RaenePath = "{color=#0f0}[Raene Path]"
    ZivPath = "{color=#0f0}[Ziv Path]"
    LuzanePath = "{color=#0f0}[Luzane Path]"
    HannahPath = "{color=#0f0}[Hannah Path]"
    TrellkaPath = "{color=#0f0}[Trellka Path]"

    EndRelationship = "{color=#f00}[End Relationship]"

screen modOptions():
    tag menu
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 50
        spacing 100

        text "Walkthrough Options" style "modTextHeader"

        text "Turn on and off character paths" style "modTextBody" xcenter 0.5

    frame:
        xcenter 0.5
        ycenter 0.5
        padding (20, 20)
        grid 5 3:
            spacing 50
            style_prefix "check"

            textbutton "Celine Path":
                action ToggleVariable("CelinePath", true_value="{color=#0f0}[Celine Path]", false_value="")

            textbutton "Jade Path's":
                action [ToggleVariable("JadePath", true_value="{color=#0f0}[Jade Path]", false_value=""), ToggleVariable("JadeLovePath", true_value="{color=#0f0}[Jade Love Path]", false_value=""), ToggleVariable("JadeSubPath", true_value="{color=#0f0}[Jade Sub Path]", false_value="")]

            textbutton "Thim Path":
                action ToggleVariable("ThimPath", true_value="{color=#0f0}[Thim Path]", false_value="")

            textbutton "Vess Path":
                action ToggleVariable("VessPath", true_value="{color=#0f0}[Vess Path]", false_value="")

            textbutton "Kit Path":
                action ToggleVariable("KitPath", true_value="{color=#0f0}[Kit Path]", false_value="")

            textbutton "Lilly Path":
                action ToggleVariable("LillyPath", true_value="{color=#0f0}[Lilly Path]", false_value="")

            textbutton "Nadya Path":
                action ToggleVariable("NadyaPath", true_value="{color=#0f0}[Nadya Path]", false_value="")

            textbutton "Aven Path":
                action ToggleVariable("AvenPath", true_value="{color=#0f0}[Aven Path]", false_value="")

            textbutton "Thyia Path":
                action ToggleVariable("ThyiaPath", true_value="{color=#0f0}[Thyia Path]", false_value="")

            textbutton "Dee & Ro Path":
                action ToggleVariable("DeeRoPath", true_value="{color=#0f0}[Dee&Ro Path]", false_value="")

            textbutton "Raene Path":
                action ToggleVariable("RaenePath", true_value="{color=#0f0}[Raene Path]", false_value="")

            textbutton "Ziv Path":
                action ToggleVariable("ZivPath", true_value="{color=#0f0}[Ziv Path]", false_value="")

            textbutton "Luzane Path":
                action ToggleVariable("LuzanePath", true_value="{color=#0f0}[Luzane Path]", false_value="")

            textbutton "Hannah Path":
                action ToggleVariable("HannahPath", true_value="{color=#0f0}[Hannah Path]", false_value="")

            textbutton "Trellka Path":
                action ToggleVariable("TrellkaPath", true_value="{color=#0f0}[Trellka Path]", false_value="")


    textbutton _("Return") action ShowMenu("save"), Hide("modWalkthroughOptions"):
        yanchor 1.0
        pos (100, 1030)
        text_style "modTextButtonHeader"
