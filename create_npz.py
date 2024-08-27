import numpy as np
import cv2
import glob
import os


def npz():

    path =  "/*.png"
    path2 = "/test_h5"
    for i, img_path in enumerate(glob.glob(path)):
        
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        label_path = img_path.replace('images', 'labels')
        label = cv2.imread(label_path, flags=0)

        label[label == 0] = 0
        
        label[label != 0] = 1

        np.savez(os.path.join(path2, str(i + 1)), image=image, label=label)
        print('finished:', i + 1)

    print('Finished')


npz()
