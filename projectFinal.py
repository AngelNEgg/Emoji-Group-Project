import simplegui

height = 600
width = 600
scale = 0.25

def draw(canvas):
  
# face 1 (Angel)
  canvas.draw_circle((xmax/2,ymax/2), 100, 10, "#fcb503", "#fcd703")
  canvas.draw_circle((xmax/2-25,ymax/2-25), 5, 10, "Black")
  canvas.draw_circle((xmax/2+25,ymax/2-25), 5, 10, "Black")
  canvas.draw_line((xmax/2-50,ymax/2+25),(xmax/2+50,ymax/2+25), 5, "brown")
  
# face 2
  
# face 3
  
# face 4


# frame setup
frame = simplegui.create_frame("Emojis", width, height)
frame.set_draw_handler(draw)
frame.start()
