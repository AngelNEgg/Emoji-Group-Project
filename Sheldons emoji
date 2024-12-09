import simplegui
height = 200
width = 200

def draw_handler(canvas):
    # all drawing happens here
    # canvas.draw_point[x,y], "color"

    canvas.draw_circle((width/2,height/2), 50, 30, "black", "black")
    canvas.draw_circle((width/2,height/2), 80, 30, "black")
    canvas.draw_circle((width/2,(height/2) +33), 5, 50, "white")
    canvas.draw_circle(((width/2) +33,(height/2) -30), 10, 10, "white")
    canvas.draw_circle(((width/2) -30,(height/2) -30), 10, 10, "white")








#library.create_frame(title,width, height)

frame = simplegui.create_frame("Python Colors",200,200)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)
frame.start()
