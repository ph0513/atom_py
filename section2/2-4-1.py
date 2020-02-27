import os
import subprocess
import pytube

yt=pytube.YouTube("https://www.youtube.com/embed/Sv8KnD9nOQo")
video1=yt.streams.all()
# print('videos',video1)

for i in range(len(video1)): # 다운로드 type 모두 출력
    print(i,',',video1[i])

vnum=int(input("다운받을 화질을 선택해 주세요(0~21) : "))

# down_dir="D:/down/youtube"
# video1[0].download(down_dir) #

parent_dir="D:/down/youtube"
video1[vnum].download(parent_dir) #

print("다운로드 완료")

# new_music="D:/down/youtube/new_music.mp3" #
#
# default_filename=video1[0].default_filename
# subprocess.call(['ffmpeg', '-i',os.path.join(parent_dir,default_filename),
# os.path.join(parent_dir,new_music)])
#
# print("변환 완료")

new_filename=input("변환할 mp3파일명을 입력하세요 : ")
last_name=new_filename+".mp3"

default_filename=video1[vnum].default_filename
subprocess.call(['ffmpeg', '-i',os.path.join(parent_dir,default_filename),
os.path.join(parent_dir,last_name)])

print("변환 완료")
