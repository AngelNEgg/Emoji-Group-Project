import simplegui

height = 600
width = 600
scale = 0.25

def draw(canvas):
  
# face 1 (Angel)
  canvas.draw_circle((width/2,height/2), 100, 10, "#fcb503", "#fcd703")
  canvas.draw_circle((width/2-25,height/2-25), 5, 10, "Black")
  canvas.draw_circle((width/2+25,height/2-25), 5, 10, "Black")
  canvas.draw_line((width/2-50,height/2+25),(width/2+50,height/2+25), 5, "brown")
  
# face 2 (Sheldon)
  canvas.draw_circle((width/2,height/2), 50, 30, "black", "black")
  canvas.draw_circle((width/2,height/2), 80, 30, "black")
  canvas.draw_circle((width/2,(height/2) +33), 5, 50, "white")
  canvas.draw_circle(((width/2) +33,(height/2) -30), 10, 10, "white")
  canvas.draw_circle(((width/2) -30,(height/2) -30), 10, 10, "white")

# face 3 (Nafisa)
    canvas.draw_circle((width/2.8, height/3), width/3 - 50, 10, "#ADD8E6", "#ADD8E6")
    canvas.draw_circle((width/4,height/3), width/20 + 5, 10, "Black", "Black")
    canvas.draw_circle((width/2 + 10, height/3), width/20 + 5, 10, "Black", "Black")
    canvas.draw_polygon([(width/4 - 15, height/2 + 30), (width/4 - 15, height/3 + 30), (width/4 - 15, height - 20) ], 35, "Blue", "Blue")
    canvas.draw_polygon([(width/2 + 5, height/3 + 30), (width/2 + 5, height/3 + 30), (width/2 + 5, height - 20) ], 35, "Blue", "Blue")

# face 4


# frame setup
frame = simplegui.create_frame("Emojis", width, height)
frame.set_draw_handler(draw)
frame.start()
