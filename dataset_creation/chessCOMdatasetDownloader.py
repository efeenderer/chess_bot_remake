import numpy as np
import time as t
import os
import requests
from dotenv import load_dotenv
load_dotenv()

headers = {'User-Agent': 'DatasetCollectionForSchoolProject/ (efe.ender.er@gmail.com)'} #I'm too afraid to have problems for trying to download this fkn set

BASE_URL = "https://images.chesscomfiles.com/chess-themes/pieces"

piece_types = ['neo','game_room','wood','glass','gothic','classic','metal','bases','neo_wood','icy_sea','club','ocean','newspaper','space','cases','condal','8_bit',
               'marble','book','alpha','bubblegum','dash','graffiti','light','lolz','luca','maya','modern','nature','neon','sky','tigers','tournament','vintage']

piece_names = ['bp','wp',
               'bn','wn',
               'bb','wb',
               'br','wr',
               'bq','wq',
               'bk','wk']

sizes = np.linspace(100,300,9)

flag = False

directory = os.path.join( os.getenv("dataset_dir") , "chess_com_pieces" )
os.makedirs(directory,exist_ok=True)       #In case it's not created already

for piece_type in piece_types:
    for piece_name in piece_names:
        for size in sizes:

            if not flag:
                URL = BASE_URL+"/"+piece_type+"/"+str(int(size))+"/"+piece_name+".png" #  EXAMPLE:      https://images.chesscomfiles.com/chess-themes/pieces/tournament/101/wq.png
                try:
                    response = requests.get(URL,headers=headers)
                    response.raise_for_status()

                           # Create an .env file and put your dataset path as "dataset" OR Assign your dataset path to this "directory" variable

                    filename = os.path.join(directory+"\\"+URL.split("/")[-3]+"_"+URL.split("/")[-2]+"_"+URL.split("/")[-1])

                    with open(filename, 'wb') as f:
                        f.write(response.content)
                        f.close()

                    print(f"Indirildi: {filename}")
                    t.sleep(0.1)
                    
                except requests.RequestException as e:
                    print(f"Idirmede hata oluştu: {URL} - {e}") 



            





