from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


#Function1

def select_path():

    # تسمح للمستخدم بإختيار مسار حفظ الملف
    path = filedialog.askdirectory()
    path_label.config(text = path)

#Fucntion2

def downlaod_file():
    # جلب المقطع من الرابط
    get_link = link_field.get()

    # get selected path
    user_path = path_label.cget("text")
    screen.title('جاري التحميل ...')

    #module from Youtube download the video with highest resolution .
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()

    #تحويل الملف الى المسار المحدد عن طريق مكتبة shutil
    shutil.move(mp4_video,user_path)
    screen.title('انتهى التحميل ...')

#هنا اسم البرنامج و حجم الواجهة

screen =Tk ()
title = screen.title('Downloader v1.0')
Canvas = Canvas(screen, width = 500 , height = 500)
Canvas.pack()


#ادخال الرابط , شريط الإدخال, حجم الخط
link_field = Entry(screen, width= 50)
link_label = Label(screen, text= ("ألصق الرابط بالأسفل "), font = (15))

#اختيار المسار لحفظ الملف
path_label = Label(screen, text= ("اختار مسار الملف اللي تبغا تحفظ فيه"),font = (15))
select_btn = Button(screen, text= "select", command = select_path)
#نافذة اختيار مسار الملف
Canvas.create_window(250, 280 , window = path_label)
Canvas.create_window(250, 330 , window = select_btn)

Canvas.create_window(250,170, window = link_label)
Canvas.create_window(250,220, window = link_field)

#زر التحميل
download_btn = Button(screen, text= "download the file !!", command= downlaod_file)

#اضافة زر التحميل الى  canvas
Canvas.create_window(250, 390, window= download_btn)

#استمرار تشغيل النافذة
screen.mainloop()
