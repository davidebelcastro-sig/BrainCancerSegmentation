import cv2
import numpy as np

'''
#TODO
'''
def get_contourn(immagine_segmentata):
    for x in range(len(immagine_segmentata)):
        for y in range(len(immagine_segmentata)):
            if immagine_segmentata[x][y][0] == 0 and  immagine_segmentata[x][y][1] == 255  and  immagine_segmentata[x][y][2] == 0:
                immagine_segmentata[x][y][0] = 255
                immagine_segmentata[x][y][1] = 255
                immagine_segmentata[x][y][2] = 255
            else:
                immagine_segmentata[x][y][0] = 0
                immagine_segmentata[x][y][1] = 0
                immagine_segmentata[x][y][2] = 0
    immagine_segmentata =  cv2.cvtColor(immagine_segmentata, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(immagine_segmentata,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    return contours[0]
'''
#TODO
'''
def modify_light_contorno(immagine_iniziale,contorno,percentuale,segno):
    immagine_iniziale = cv2.cvtColor(immagine_iniziale, cv2.COLOR_BGR2GRAY)
    copia = immagine_iniziale.copy()
    lista_pixel = []
    cv2.drawContours(copia, [contorno], -1, 255, -1)
    for i in range(0,immagine_iniziale.shape[0]):
        for y in range(0,immagine_iniziale.shape[1]):
            if copia[i][y] == 255:
                lista_pixel.append((i,y))
    if segno == 1:
        for pixel in lista_pixel:
            immagine_iniziale[pixel[0]][pixel[1]]=min(immagine_iniziale[pixel[0]][pixel[1]] + (immagine_iniziale[pixel[0]][pixel[1]]*percentuale)/100,255)
    else:
        for pixel in lista_pixel:
            immagine_iniziale[pixel[0]][pixel[1]] = max(immagine_iniziale[pixel[0]][pixel[1]] - (immagine_iniziale[pixel[0]][pixel[1]]*percentuale)/100,0)
    return immagine_iniziale
'''
#TODO
'''
def get_only_contorno(immagine_iniziale,contorno):
    immagine_iniziale = cv2.cvtColor(immagine_iniziale, cv2.COLOR_BGR2GRAY)
    mask = np.zeros(immagine_iniziale.shape[:2], np.uint8)
    cv2.drawContours(mask, [contorno], -1, 255, -1)
    result = cv2.bitwise_and(immagine_iniziale, immagine_iniziale, mask=mask)
    return result
'''
Main entry point for the filter script
'''
def main(data,path):
    print(data)
    # if data[0] != 0:
    #     contorno = get_contourn(cv2.imread(path))
    #     check = int(data[0])
    #     if check>0: 
    #         segno = 1 
    #     else: segno = -1
    #     result = modify_light_contorno(cv2.imread(path),contorno,check,segno)
    #     if data[1] and data[2] and data[3]== 'Pass': 
    #         return result
    #     else:
    #         pass
    if data[2] == 'Yes':
        print('voglio il contorno')
        contorno = get_contourn(cv2.imread(path))
        result = get_only_contorno(cv2.imread(path),contorno)
        return []
    else:
        print('non voglio il contorno')