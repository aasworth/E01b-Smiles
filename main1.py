#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(800, 600, "Smiley Face Example")
arcade.set_background_color(open_color.white)
# Start the render process. This must be done before any drawing commands.
arcade.start_render()


# Draw the smiley face:
# (x,y,radius,color)
arcade.draw_circle_filled(400, 300, 100, open_color.yellow_3)
# (x,y,radius,color,border_thickness)
arcade.draw_circle_outline(400, 300, 100, open_color.black,4)

#(x,y,width,height,color)
arcade.draw_ellipse_filled(370,350,15,25,open_color.black)
arcade.draw_ellipse_filled(430,350,15,25,open_color.black)
arcade.draw_circle_filled(375,360,3,open_color.gray_2)
arcade.draw_circle_filled(435,360,3,open_color.gray_2)

#(x,y,width,height,color,start_degrees,end_degrees,border_thickness)
arcade.draw_arc_outline(400,300,60,50,open_color.black,190,350,4)



# Finish the render
# Nothing will be drawn without this.
# Must happen after all draw commands
arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()
