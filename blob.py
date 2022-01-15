import math

class Blob:
    def __init__(self,x=0,y=0):
        self.minx = x
        self.miny = y
        self.maxx = x
        self.maxy = y

    def add_point(self,x,y):
        self.minx = min(self.minx,x)
        self.miny = min(self.miny,y)
        self.maxx = max(self.maxx,x)
        self.maxy = max(self.maxy,y)

    def point_distance(self,x,y):
        cx = (self.maxx + self.minx) / 2
        cy = (self.maxy + self.miny) / 2
        width = self.maxx - self.minx
        height = self.maxy - self.miny

        disx = max(0, abs(cx - x) - width/2 )
        disy = max(0, abs(cy - y) - height/2 )
        return math.sqrt(  math.pow( disx ,2) + math.pow(disy,2) )

    def blob_distance(self,blob):
        s_cx = (self.maxx + self.minx) / 2
        s_cy = (self.maxy + self.miny) / 2
        s_width = self.maxx - self.minx
        s_height = self.maxy - self.miny

        b_cx = blob.maxx + blob.minx / 2
        b_cy = blob.maxy + blob.miny / 2
        b_width = blob.maxx - blob.minx
        b_height = blob.maxy - blob.miny

        disx = max(0, abs(s_cx - b_cx) - s_width/2 - b_width/2 )
        disy = max(0, abs(s_cy - b_cy) - s_height/2 - b_height/2 )
        return math.sqrt(  math.pow( disx ,2) + math.pow(disy,2) )

    def is_circle(self): # is not really a precice check but it solves a lot of problems
        w = self.maxx - self.minx
        h = self.maxy - self.miny
        return abs(w-h) < 5

    def __str__(self):
        return f'{self.minx},{self.miny},{self.maxx},{self.maxy}'

