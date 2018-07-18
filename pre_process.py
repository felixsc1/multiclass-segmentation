import sys
sys.path.append(sct_dir)
sys.path.append(sct_scripts)
from resample.nipy_resample import resample_image
from sct_image import set_orientation
import numpy as np
from paths import sct_scripts, sct_dir



def check_orientation(image, orientation):
    if image.orientation != orientation:
        print image.orientation
        image = set_orientation(image, orientation)
    return image

def check_resolution(image, resolution):
    res_w, res_h = list(np.around(image.dim[4:6], 2))
    res_str = str(res_w)+"x"+str(res_h)
    if res_str != resolution:
        print res_str
        image = resample_image(image, resolution, 'mm', 'linear', verbose=0)
    return image