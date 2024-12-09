import simplegui 
width = 600
height = 600
def draw(canvas):
    canvas.draw_circle((width/2.8, height/3), width/3 - 50, 10, "#ADD8E6", "#ADD8E6")
    canvas.draw_circle((width/4,height/3), width/20 + 5, 10, "Black", "Black")
    canvas.draw_circle((width/2 + 10, height/3), width/20 + 5, 10, "Black", "Black")
    canvas.draw_polygon([(width/4 - 15, height/2 + 30), (width/4 - 15, height/3 + 30), (width/4 - 15, height - 20) ], 35, "Blue", "Blue")
    canvas.draw_polygon([(width/2 + 5, height/3 + 30), (width/2 + 5, height/3 + 30), (width/2 + 5, height - 20) ], 35, "Blue", "Blue")
   
    
frame = simplegui.create_frame("Pictures", width, height) 
frame.set_draw_handler(draw)
frame.start()   
