import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from ast import literal_eval
import re
from colorutils import as_matplotlib_color


def from_stdin(filename):
    prefix = os.path.splitext(filename)[0]
    with open(filename) as file_:
        width, height = literal_eval(file_.readline().replace(' ',','))
        img = np.zeros((height,width,3))
        for i,line in enumerate(file_):
            triplets = re.split('[()]+', line)[1:-1]
            triplets = [literal_eval(t) for t in triplets]
            for j,pxl in enumerate(triplets):
                img[i,j] = as_matplotlib_color(pxl)
    mpimg.imsave(prefix+'.png', img)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read stdin triplets into an image fil')
    parser.add_argument('filename',  help='name of the textfile containing colors as triplets')
    args = parser.parse_args()
    filename = args.filename
    from_stdin(filename)
