init python:
    cheatItems = []
    cheatCatagorys = []

    class CheatItem:
        def __init__(self, catagory, name, variable, kind="Slider", minValue=0, maxValue=0, trueValue=True, falseValue=False):
            self.catagory = catagory
            self.name = name
            self.variable = variable
            if kind == "Slider":
                self.minValue = minValue
                self.maxValue = maxValue
            elif kind == "Button":
                self.trueValue = trueValue
                self.falseValue = falseValue
            else:
                raise Exception("Unsupported Cheat Type")
            self.kind = kind
            # if self not in cheatItems:
            cheatItems.append(self)

    # Emily1 = CheatItem("Emily", "Love Points", "emLP", maxValue=30)
    # Emily2 = CheatItem("Emily", "Corruption Route", "carolroute", kind="Button")

    for cheatItem in cheatItems:
        if cheatItem.catagory not in cheatCatagorys:
            cheatCatagorys.append(cheatItem.catagory)

screen cheatMenu():
    modal True
    zorder 200

    default shownCheatMenu = cheatItems[0] or None

    add "/modAdditions/images/cheatMenuBackground.png"

    fixed:
        xysize (1024, 66)
        pos (57, 9)

        hbox:
            xcenter 0.5
            ycenter 0.5
            spacing 100
            for cheatCatagory in cheatCatagorys:
                textbutton cheatCatagory:
                    action [Function(renpy.retain_after_load), SetScreenVariable("shownCheatMenu", cheatCatagory)]
                    text_style "modTextButtonHeader"

    for cheatCatagory in cheatCatagorys:
        if shownCheatMenu == cheatCatagory:
            use cheatMenuValues(cheatMenuChar=cheatCatagory)

    imagebutton:
        action Hide("cheatMenu"), Hide("cheatMenuValues"), SetVariable("quick_menu", True)
        idle "/modAdditions/images/cheatMenuBackButton.png"
        hover im.MatrixColor("/modAdditions/images/cheatMenuBackButton.png", im.matrix.brightness(0.2))
        pos (1111, 33)

screen cheatMenuValues(cheatMenuChar="General"):
    tag cheatmenu

    vbox:
        pos (50, 137)
        spacing 50
        vpgrid:
            cols 4
            spacing 50
            for cheatItem in cheatItems:
                if cheatItem.catagory == cheatMenuChar and cheatItem.kind == "Slider":
                        vbox:
                            spacing 20
                            text "[cheatItem.name] Points:" style "modTextBody2"
                            fixed:
                                xysize (234, 28)

                                bar value VariableValue(cheatItem.variable, cheatItem.maxValue-cheatItem.minValue, offset=cheatItem.minValue):
                                    left_bar Frame("gui/bar/left.png", 10, 0)
                                    right_bar Frame("gui/bar/right.png", 10, 0)
                                text "{:}".format(getattr(store, cheatItem.variable)) align(0.5, 0.5)
        vpgrid:
            cols 4
            spacing 50
            for cheatItem in cheatItems:
                if cheatItem.catagory == cheatMenuChar and cheatItem.kind == "Button":
                    vbox:
                        style_prefix "check"
                        textbutton "[cheatItem.name]":
                            action ToggleVariable(cheatItem.variable, true_value=cheatItem.trueValue, false_value=cheatItem.falseValue)
