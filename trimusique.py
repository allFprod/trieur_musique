import subprocess

subprocess.run(["pip", "install", "tinytag"]) #install la librairie tinytag

import shutil, os
from tinytag import TinyTag
from tqdm import tqdm

def trie(repertoir) :
    """
    Entrée : répertoir d'action
    récupère tout les fichiers wav, mp3 et
    
    et les tries par artiste dans un fichier du nom de celui-ci crée par python
    """
    
    lst = os.listdir(repertoir) #ajoute dans une liste (python) la liste des noms fichiers présent dans le répertoir
    
    if 'sans_nom' not in lst :
        print(lst)
        os.mkdir(repertoir + "sans_nom")
        #crée un fichié sans_nom si il n'est pas présent
    
    
    for f in tqdm(lst) : # lis les noms des fichiers
        #remplace les caractères gênants
        f = f.replace('é','e')
        f = f.replace('à','afe')
        f = f.replace('$','s')
        f = f.replace('@','a')
        #mets le nom en minuscule
        f = f.lower()
        
        #récupère le nom de l'artiste
        tag: TinyTag = TinyTag.get(repertoir + f)
        artist = tag.artist
        
        if '.WAV' in f or '.mp3' in f or 'm4a' in f: #si le nom est un fichier musique alors
            
            if artist is None : #si il n'y a pas d'artiste : ranger dans le répertoir "sans_nom"
                shutil.move(repertoir + "" + f, repertoir + "sans_nom")
            elif artist not in os.listdir(repertoir) : #sinon si il n'y a pas de répertoir au nom de l'artiste le crée puis déplacer
                os.mkdir(repertoir + artist)
                shutil.move(repertoir + f, repertoir + artist)
            else :
                shutil.move(repertoir + f, repertoir + artist) #sinon déplacer
        
        



rep = input("Veuillez entrer le repertoir (avec des '/' et nonpas des '\')")
trie(rep)
            
        
            
            

            
    
    
    
    



