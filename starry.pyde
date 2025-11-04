swirls = []

def setup():
    size(960, 760)
    frameRate(60)
    global painting
    painting = loadImage("starryNight.jpg")

def draw():
    background(0)
    image(painting, 0, 0)
    
    # Animate each swirl
    for swirl in swirls:
        # how big the swirl will be popping (use cosine wave function so it move infinitely like waves from -1 to 1)
        scale_amount = cos(frameCount * 0.15 + swirl['offset'] * PI) * 0.12 + 1
        
        # Scale from swirl center
        pushMatrix()
        translate(swirl['x'], swirl['y']) # make the swirl expand
        scale(scale_amount) # scale it up
        translate(-swirl['x'], -swirl['y']) # make the swirl shrinks to original size
        
        tint(255, 204)  # 20% transparency for smooth blending during 3D effect
        
        # Prevents crashes by giving boundary (for centerpoint of mouse) to where can be animated
        x = int(swirl['x'] - 30) 
        y = int(swirl['y'] - 30)
        
        # checking for centerpoint of the mouse when clicking is in the bound (that's why we have to +30 so do need to check the sides that is not in bound)
        if x + 30 >= 0 and y + 30 >= 0 and x + 30 <= width and y + 30 <= height:
            copy(painting, x, y, 60, 60, x, y, 60, 60) # 60 is to double the size (originally 30) when animated the swirl
        
        noTint()
        popMatrix()
        
        # Instructions (white text and size of the text)
        fill(255, 255, 255)
        textSize(13)
        text("Click to add swirls | C to clear | P to save swirls | Swirls: " + str(len(swirls)), 10, 20)

def mouseClicked():
    import random
    new_swirl = {
        'x': mouseX, 
        'y': mouseY, 
        'size': 30,
        'offset': random.uniform(0, 3)
    }
    swirls.append(new_swirl)
    print("Added swirl #" + str(len(swirls)) + ": " + str(new_swirl))
    
def keyPressed():
    if key == 'c' or key == 'C':
        swirls[:] = []
        print("Cleared all swirls!")

    # give coordinates to the animations
    elif key == 'p' or key == 'P':
        print("swirls = [")
        for swirl in swirls:
            print("    " + str(swirl) + ",")
        print("]")
        print("\n")
