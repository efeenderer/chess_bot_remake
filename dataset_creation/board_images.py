import os
from dotenv import load_dotenv
load_dotenv()
import numpy as np
import cv2
import time as t
import random


# The aim of this script is to put chess pieces and arrows like it's a usual Virtual Chess match.


#Here, the board and background images' dirs are put in lists. Later, they'll be randomly selected.
boards = os.path.join(os.getenv("dataset_dir") , "boards", "cropped")
boards = [boards+"/"+board for board in os.listdir(boards)]                     

backgrounds = os.path.join(os.getenv("dataset_dir") , "boards", "backgrounds")
backgrounds = [backgrounds+"/"+background for background in os.listdir(backgrounds)]

save_dir = ""


for i in range(10300):      # Put how many images you'd like in your dataset instead of 10000
    board_rnd_selection =   random.randint(0, len(boards) - 1)
    background_rnd_selection = random.randint(0,len(backgrounds) - 1)

    board = cv2.imread(boards[board_rnd_selection])
    background = cv2.imread(backgrounds[background_rnd_selection])

    bg_w, bg_h = background.shape[1],background.shape[0]
    
    bg_min = min(bg_w,bg_h)

    if bg_min < 10:
        continue

    if bg_min < board.shape[0]:
        rnd_size = random.randint( (bg_min - 5)//4 , bg_min - 5)
        board = cv2.resize(board,(rnd_size,rnd_size), cv2.INTER_AREA)
    else:
        rnd_size = random.randint(200,board.shape[0])
        board = cv2.resize(board,(rnd_size,rnd_size), cv2.INTER_AREA)

    brd_h = brd_w = board.shape[0]
    
    y1= random.randint(0, bg_h - brd_h)
    y2 = y1 + brd_h
    x1 = random.randint(0, bg_w - brd_w)
    x2 =  x1 + brd_w

    background[y1:y2,x1:x2] = board
    cv2.imshow("lala",background)
    cv2.waitKey(1)


    #print(f"{board.shape}\n{background.shape}\n")

    




