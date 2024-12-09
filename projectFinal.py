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
  canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#ADD8E6", "#ADD8E6")
  canvas.draw_circle((width/3,height/2), width/20 + 5, 10, "Black", "Black")
  canvas.draw_circle((width/1.5 + 15, height/2), width/20 + 5, 10, "Black", "Black")
  canvas.draw_circle((width/3 - 30, height/2 - 40), width/20 - 5, 10, "#ADD8E6", "#ADD8E6")
  canvas.draw_circle((width/1.5 + 45, height/2 - 40), width/20 - 5, 10, "#ADD8E6", "#ADD8E6")
  canvas.draw_polygon([(width/3 - 10, height/2 + 30), (width/3 - 10, height/2 + 30), (width/3 - 10, height - 20) ], 35, "Blue", "Blue")
  canvas.draw_polygon([(width/1.5 + 5, height/2 + 30), (width/1.5 + 5, height/2 + 30), (width/1.5 + 5, height - 20) ], 35, "Blue", "Blue")
  canvas.draw_circle((width/2,height - 100), width/20 + 5, 10, "Black", "Black")

# face 4


# frame setup
frame = simplegui.create_frame("Emojis", width, height)
frame.set_draw_handler(draw)
frame.start()
