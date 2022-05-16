def on_forever():
    if input.acceleration(Dimension.Y) < -100:
        if input.acceleration(Dimension.X) < -100:
            basic.show_leds("""
                # # # # .
                                # # . . .
                                # . # . .
                                # . . # .
                                . . . . #
            """)
        else:
            if input.acceleration(Dimension.X) > 100:
                basic.show_leds("""
                    . # # # #
                                        . . . # #
                                        . . # . #
                                        . # . . #
                                        # . . . .
                """)
            else:
                if input.acceleration(Dimension.Y) < -100:
                    basic.show_leds("""
                        . . # . .
                                                . # # # .
                                                # . # . #
                                                . . # . .
                                                . . # . .
                    """)
    else:
        if input.acceleration(Dimension.Y) > 100:
            if input.acceleration(Dimension.X) < -100:
                basic.show_leds("""
                    . . . . #
                                        # . . # .
                                        # . # . .
                                        # # . . .
                                        # # # # .
                """)
            else:
                if input.acceleration(Dimension.X) > 100:
                    basic.show_leds("""
                        # . . . .
                                                . # . . #
                                                . . # . #
                                                . . . # #
                                                . # # # #
                    """)
                else:
                    basic.show_leds("""
                        . . # . .
                                                . . # . .
                                                # . # . #
                                                . # # # .
                                                . . # . .
                    """)
        else:
            if input.acceleration(Dimension.X) < -100:
                basic.show_leds("""
                    . . # . .
                                        . # . . .
                                        # # # # #
                                        . # . . .
                                        . . # . .
                """)
            else:
                if input.acceleration(Dimension.X) > 100:
                    basic.show_leds("""
                        . . # . .
                                                . . . # .
                                                # # # # #
                                                . . . # .
                                                . . # . .
                    """)
                else:
                    basic.show_icon(IconNames.YES)
basic.forever(on_forever)
