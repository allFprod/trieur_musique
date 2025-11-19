import subprocess

subprocess.run(["pip", "install", "tinytag"])

import shutil, os
from tinytag import TinyTag
from tqdm import tqdm

def trie(repertoir) :
    
    lst = os.listdir(repertoir)
    
    if 'autre' not in lst :
        print(lst)
        os.mkdir(repertoir + "sans_nom")
    
    
    for f in tqdm(lst) :
        f = f.replace('é','e')
        f = f.replace('à','afe')
        f = f.replace('$','s')
        f = f.replace('@','a')
        f = f.lower()
        tag: TinyTag = TinyTag.get(repertoir + f)
        artist = tag.artist
        if '.WAV' in f or '.mp3' in f or 'm4a' in f:
            if artist is None :
                shutil.move(repertoir + "" + f, repertoir + "sans_nom")
            elif artist not in os.listdir(repertoir) :
                os.mkdir(repertoir + artist)
                shutil.move(repertoir + f, repertoir + artist)
            else :
                shutil.move(repertoir + f, repertoir + artist)
        
        



rep = input("Veuillez entrer le repertoir (avec des '/' et nonpas des '\')")
trie(rep)
            
        
            
            

            
    
    
    
    



