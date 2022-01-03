from pytube import YouTube
import time
path="C:\\Users\\USER"
print("Paste the link: ")
link=input("")
ob=YouTube(link)
c=int(input("1. Enter one for good quality\
    \n2.Enter 2 for the low quality\
        \n Enter your choice: "))
if(c==1):
    quality=ob.streams.get_highest_resolution()
elif(c==2):
    quality=ob.streams.get_lowest_resolution()
print("feching video")
file_size=quality.filesize
ab=file_size/(1024*1024)
print(f"video length :{ab}")
print("Downloading the video please wait")
print("20%")
print("////")
time.sleep(5)
print("30%")
print("///////")
time.sleep(5)
print("40%")
print("///////////")
time.sleep(5)
print("50%")
print("////////////////")
time.sleep(5)
print("70%")
print("////////////////////////")
time.sleep(5)
print("80%")
print("////////////////////////")
time.sleep(5)
print("90%")
print("//////////////////////////////")
quality.download(path)
print("100%")
print("//////////////////////////////////////////////////////////////////////////////////////")
print("Download sucessfully")