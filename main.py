import sys
import threading
import time

from pynput import keyboard,mouse
from PIL import ImageGrab

from blob import Blob

# colors are not linear but this works
def close_color(color):
    (r,g,b) = color
    reference_color = (106, 199, 0) 
    diff = abs( reference_color[0] - r ) + abs( reference_color[1] - g ) + abs( reference_color[2] - b )
    return diff < 20

#todo (maybe make a gui , maybe give some message to the user to know that the bot is on without having to look at the console or at the gui, make it console-less)


if __name__ == "__main__":
    print("this is a bot for the game https://mouseaccuracy.com/ (remember to change the color of the dots to green)")
    print("press <ctrl>+<alt>+h  to start the bot (will make the bot click green dots) ")
    print("press <ctrl>+<alt>+i  to stop the bot ")
    print("press <esc> to end the program ")

    state = {
        "bot_running" : False
    }
    mouse_controller = mouse.Controller()
    keyboard_controller = keyboard.Controller()

    def bot_loop():
        while state["bot_running"]:
            img = ImageGrab.grab()
            img = img.resize((  int(img.width/4) , int(img.height/4))) #reduce size to make detection faster
            blobs = []
            for y in  range(0,img.height):
                for x in  range(0,img.width):
                    color = img.getpixel( (x,y) )
                    if close_color(color) :
                        closest_blob_point = None
                        for blob in blobs:
                            d = blob.point_distance(x,y)
                            if closest_blob_point is None or d < closest_blob_point[1] :
                                closest_blob_point = ( blob,d)
                        #if it is zero is already inside
                        if closest_blob_point is not None and closest_blob_point[1] < 10: 
                            closest_blob_point[0].add_point(x,y)
                        else:
                            blobs.append(Blob( x,y ))
            for blob in blobs:
                if not blob.is_circle():
                    continue
                cx = (blob.minx + blob.maxx)/2
                cy = (blob.miny + blob.maxy)/2
                mouse_controller.position = (cx *4,cy*4 )
                mouse_controller.click(mouse.Button.left)
            time.sleep(0.2)


    def start():
        state["bot_running"] = True
        print("bot is running")
        t = threading.Thread(target=bot_loop)
        t.start()

    def finish():
        print("bot is not running")
        state["bot_running"] = False

    with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+h': start,
        '<ctrl>+<alt>+i': finish,
        '<esc>':sys.exit
        }) as h:
        h.join()






