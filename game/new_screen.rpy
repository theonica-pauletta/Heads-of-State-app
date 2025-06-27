screen navigation():

    fixed:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            #textbutton _("Start") action Start()
            imagebutton auto "gui/mm_start_%s.png" xpos 184 ypos 258 focus_mask True action Start() hovered [ Play("sound", "audio/select.mp3")]

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")


        #textbutton _("Preferences") action ShowMenu("preferences")
        imagebutton auto "gui/mm_prefrences_%s.png" xpos 707 ypos 297 focus_mask True action ShowMenu("preferences") hovered [ Play("sound", "audio/select.mp3")]

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()
            

        #textbutton _("About") action ShowMenu("about")
        imagebutton auto "gui/mm_info_%s.png" xpos 1292 ypos 250 focus_mask True action ShowMenu("about") hovered [ Play("sound", "audio/select.mp3")]

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        #    ## Help isn't necessary or relevant to mobile devices.
        #    textbutton _("Help") action ShowMenu("help")

        #if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
        #    textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")