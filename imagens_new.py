#Importa biblioteca de interação com o SO
import os
#Importa biblioteca de manipulação de imagens
from PIL import Image
#Importa biblioteca de manipulação de arrays
import numpy as np

imagens_site = r"C:\Users\user\Documents\GitHub\imagens_site"

for imagem in os.listdir(imagens_site):
    if imagem.endswith(".jpg") or imagem.endswith(".png"):
        local_img = os.path.join(imagens_site, imagem)
        img = Image.open(local_img).convert('RGB')
        img_arr = np.array(img)

        # Alterar cordenadas da imagem com cor branca
        img_arr[376:, 364:, :] = (255, 255, 255)

        img = Image.fromarray(img_arr)
        img.save(local_img)