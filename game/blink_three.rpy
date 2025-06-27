init -1:
    transform blink_three(old_widget=None, new_widget=None):
        delay 3.0

        # Show the old scene under the animation and block its events.
        old_widget
        events False

        # Top black bar (anchored at top):
        parallel:
            At(Solid("#000"), xalign=0.5, yalign=0.0, xsize=1.0, ysize=0.0)
            linear 0.25 ysize 0.5
            pause 0.5
            linear 0.25 ysize 0.0

        # Bottom black bar (anchored at bottom):
        parallel:
            At(Solid("#000"), xalign=0.5, yalign=1.0, xsize=1.0, ysize=0.0)
            linear 0.25 ysize 0.5
            pause 0.5
            linear 0.25 ysize 0.0

        # Repeat the close-pause-open sequence three times total.
        repeat 3

        # Finally, show the new scene and re-enable events.
        new_widget
        events True
