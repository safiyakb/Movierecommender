import os
import cv2
import time
import natsort
import numpy as np
from skimage import io
from skimage import color
from pymediainfo import MediaInfo
'''####
with open('vid_send.txt', 'r') as myfile:    
        video_id = myfile.read()
        data = video_id
        
        if int(data) == file:
            f = open("recommended_vid.txt","w")
            print(res, file = f)
            f.close()
        '''
#####
data_dir = "/Users/masoodkhan/Desktop/Project_PVR_using_RC_from_videos/Video_Test"
files = os.listdir(data_dir)
files =  natsort.natsorted(files)
for i in range(len(files)):
    file = files[i]
    print("File:",file)
    #if int(data) == file:
    filepath = data_dir + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('video_File_Name:......', file)
        media_info = MediaInfo.parse('Video_Test/' + file)
        for track in media_info.tracks:
            if track.track_type == 'Video':
                print ("Resolution {}x{}".format(track.width, track.height))
                print ("Resolution:",track.width * track.height)

#remove video predict resulation:
'''
TestData="Video_Test"
while True:
    for(direcpath,direcnames,files) in os.walk(TestData):
        for file in files:
            if 'mp4' in file:
                path = TestData + '//'+ file
                print(file)
                time.sleep(1)
                #img = cv2.imread(path)
                media_info = MediaInfo.parse(path)
                for track in media_info.tracks:
                    if track.track_type == 'Video':
                        print ("Resolution {}x{}".format(track.width, track.height))
                        print ("Total_Resolution:",track.width * track.height)
                        os.remove(TestData+'/'+file)'''


                
                
