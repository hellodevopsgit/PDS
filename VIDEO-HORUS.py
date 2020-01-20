import os
import shutil
import cv2
sInputFileName='C:/VKHCG/01-Vermeulen/00-RawData/dog.mp4'
sDataBaseDir='C:/VKHCG/05-DS/9999-Data/temp'
if os.path.exists(sDataBaseDir):
    shutil.rmtree(sDataBaseDir)
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
print('Start Movie to Frames') 
vidcap = cv2.VideoCapture(sInputFileName)
success,image = vidcap.read()
count = 0
while success:
    success,image = vidcap.read()
    sFrame=sDataBaseDir + str('/dog-frame-' + str(format(count, '04d')) + '.jpg')
    print('Extracted: ', sFrame)
    cv2.imwrite(sFrame, image)  
    if os.path.getsize(sFrame) == 0:
        count += -1
        os.remove(sFrame) 
        print('Removed: ', sFrame)
    if cv2.waitKey(10) == 27: 
        break
    if count > 100:
        break
    count += 1
print('Generated : ', count, ' Frames')
print('Movie to Frames HORUS - Done')