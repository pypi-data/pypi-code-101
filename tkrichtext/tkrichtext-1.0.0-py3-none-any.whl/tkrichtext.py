from tkinter import Tk,Frame
from threading import Thread
import ctypes
user32=ctypes.windll.user32

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System')
from System.Windows.Forms import RichTextBox
from System.Drawing import Font
from System import String,Single


class TkRichtext(Frame):
    '''显示*.rtf文件的tkinter富文本组件'''

    def __init__(self,master,width,height):
        Frame.__init__(self,master,width=width,height=height)
        font=Font(String('微软雅黑'),Single(13))
        self.rt=RichTextBox()
        self.rt.Font=font
        self.rthwnd=int(str(self.rt.Handle))
        user32.SetParent(self.rthwnd,self.winfo_id())
        user32.MoveWindow(self.rthwnd,0,0,width,height,True)
        self.bind('<Configure>',self.__resize)

    def __resize(self,event):
        self.rt.Width=self.winfo_width()
        self.rt.Height=self.winfo_height()

    def loadfile(self,path):
        #载入*.rtf文件
        self.rt.LoadFile(path)


def test():
    a=Tk()
    a.geometry('600x600+5+5')

    rt=TkRichtext(a,500,500)
    rt.pack(fill='both',expand='True')
    #rt.loadfile(r"E:\Py软件\Tin文件\软件说明.rtf")

    a.mainloop()

if __name__=='__main__':
    test()
