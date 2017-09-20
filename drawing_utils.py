import sys
sys.path.append('../')
import stddraw



def draw_graph(points, color):
    stddraw.setPenColor(color)
    prev = None
    for point in points:
        if prev is not None: 
            stddraw.line(*prev, *point)
        prev = point








