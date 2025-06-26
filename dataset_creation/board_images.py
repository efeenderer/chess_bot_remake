import os
from dotenv import load_dotenv
load_dotenv()
import cv2
import random
import pandas as pd


# The aim of this script is to put chess pieces and arrows like it's a usual Virtual Chess match.
dataset_dir = os.getenv("dataset_dir")

#Here, the board and background images' dirs are put in lists. Later, they'll be randomly selected.
boards = os.path.join(dataset_dir , "boards", "cropped")
boards = [boards+"/"+board for board in os.listdir(boards)]                     

backgrounds = os.path.join(dataset_dir , "boards", "backgrounds")
backgrounds = [backgrounds+"/"+background for background in os.listdir(backgrounds)]

save_dir_train = os.path.join(dataset_dir,"boards","train")
save_dir_val = os.path.join(dataset_dir,"boards","val")

os.makedirs(save_dir_train,exist_ok=True)
os.makedirs(save_dir_val,exist_ok=True)

os.makedirs(save_dir_train+"/images",exist_ok=True)
os.makedirs(save_dir_val+"/images",exist_ok=True)

labels = []

# ----- TRAIN SET ----- #

for i in range(10000):      # Put how many images you'd like in your dataset instead of 10000
    board_rnd_selection =   random.randint(0, len(boards) - 1)
    background_rnd_selection = random.randint(0,len(backgrounds) - 1)

    board = cv2.imread(boards[board_rnd_selection])
    background = cv2.imread(backgrounds[background_rnd_selection])

    bg_w, bg_h = background.shape[1],background.shape[0]
    
    bg_min = min(bg_w,bg_h)

    if bg_min < 35:
        i -= 1
        continue

    if bg_min < board.shape[0]:
        rnd_size = random.randint( (bg_min - 5)//1.5 , bg_min - 5)
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


    file_name = f"train_synthetic_{i:05}.jpg"

    labels.append([file_name,
            x1,y1,
            x2,y1,
            x2,y2,
            x1,y2
            ])
    
    cv2.imwrite(save_dir_train+f"/images/{file_name}",background)
    
df = pd.DataFrame(labels, columns=["filename", "x1", "y1", "x2", "y2","x3", "y3","x4", "y4"])
df.to_csv(f"{save_dir_train}/labels.csv", index=False)




# ----- VALIDATION SET ----- #

labels = []
for i in range(2500):      # And this part is for validation. The exact same process.
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


    file_name = f"val_synthetic_{i:05}.jpg"

    labels.append([file_name,
            x1,y1,
            x2,y1,
            x2,y2,
            x1,y2
            ])
    
    cv2.imwrite(save_dir_val+f"/images/{file_name}",background)
    
df = pd.DataFrame(labels, columns=["filename", "x1", "y1", "x2", "y2","x3", "y3","x4", "y4"])
df.to_csv(f"{save_dir_val}/labels.csv", index=False)