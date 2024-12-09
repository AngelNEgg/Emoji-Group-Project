import simplegui 
width = 600
height = 600
def draw(canvas):
    canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#ADD8E6", "#ADD8E6")
    canvas.draw_circle((width/3,height/2), width/20 + 5, 10, "Black", "Black")
    canvas.draw_circle((width/1.5 + 15, height/2), width/20 + 5, 10, "Black", "Black")
    canvas.draw_circle((width/3 - 30, height/2 - 40), width/20 - 5, 10, "#ADD8E6", "#ADD8E6")
    canvas.draw_circle((width/1.5 + 45, height/2 - 40), width/20 - 5, 10, "#ADD8E6", "#ADD8E6")
    canvas.draw_polygon([(width/3 - 10, height/2 + 30), (width/3 - 10, height/2 + 30), (width/3 - 10, height - 20) ], 35, "Blue", "Blue")
    canvas.draw_polygon([(width/1.5 + 5, height/2 + 30), (width/1.5 + 5, height/2 + 30), (width/1.5 + 5, height - 20) ], 35, "Blue", "Blue")
    canvas.draw_circle((width/2,height - 100), width/20 + 5, 10, "Black", "Black")
    
frame = simplegui.create_frame("Pictures", width, height) 
frame.set_draw_handler(draw)
frame.start()   
