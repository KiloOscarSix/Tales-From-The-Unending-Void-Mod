define gr = "{color=#0f0}"
define red = "{color=#f00}"
define blue = "{color=#00f}"

define CelinePath = "{color=#0f0}[Celine Path]",
define JadePath = "{color=#0f0}[Jade Path]",
define JadeLovePath = "{color=#0f0}[Jade Love Path]",
define JadeSubPath = "{color=#0f0}[Jade Sub Path]",
define ThimPath = "{color=#0f0}[Thim Path]",
define VessPath = "{color=#0f0}[Vess Path]",
define KitPath = "{color=#0f0}[Kit Path]",
define LillyPath = "{color=#0f0}[Lilly Path]",
define NadyaPath = "{color=#0f0}[Nadya Path]",
define AvenPath = "{color=#0f0}[Aven Path]",
define ThyiaPath = "{color=#0f0}[Thyia Path]",
define DeeRoPath = "{color=#0f0}[Dee&Ro Path]",
define RaenePath = "{color=#0f0}[Raene Path]",
define ZivPath = "{color=#0f0}[Ziv Path]",
define LuzanePath = "{color=#0f0}[Luzane Path]",
define HannahPath = "{color=#0f0}[Hannah Path]",
define RahiaPath = "{color=#0f0}[Rahia Path]",
define CaesePath = "{color=#0f0}[Caese Path]",

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xalign 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action NullAction() text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action NullAction() text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)
