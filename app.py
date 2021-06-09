import tkinter as tk
import os
from tkinter import filedialog as fd, NORMAL, END
import matplotlib.pyplot as plt
import numpy as np
import pptk
import sqlite3
from PIL import Image, ImageTk
from tkvideo import tkvideo
import datetime
from mul_points import CMulPoints
from way_creator import CWayCreator

font_big_btn = ("Times", "30", "bold italic")
font_normal_btn = ("Times", "24", "bold italic")
font_small_btn = ("Times", "14")
from gallery import *

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('600x600')
        self.title('App ... ... ... ...')

        # int
        self.__my_gallery = Gallery()
        self.__file_xyz = ""

        if not os.path.exists("database.db"):
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute('''CREATE TABLE ways
                           (id text, file_name text, x real, y real, z real)''')
            sql = '''
                INSERT INTO ways(id , file_name , x , y , z )
                VALUES(?,?,?,?,?)
            '''
            con.close()
        # end int
        self.nav_frame = tk.Frame(self)
        self.nav_frame.grid(column=0,row=0)

        self.next_btn = tk.Button(self.nav_frame, text='Home', command=self.frame1_visible,
                                                                  background = "white",
                                                                  foreground = "black",font =font_normal_btn,width=7)
        self.next_btn.grid(column=0,row=0,pady= 10,padx= 10)
        self.next_btn2 = tk.Button(self.nav_frame, text='Process', command    = self.frame2_visible,
                                                                 background = "white",
                                                                 foreground = "black",
                                                                       font = font_normal_btn,width=7)
        self.next_btn2.grid(column=0,row=1,pady= 10,padx= 10)
        self.next_btn3 = tk.Button(self.nav_frame, text='Gallery', command    =self.frame3_visible,
                                                                 background = "white",
                                                                 foreground = "black",
                                                                       font = font_normal_btn,width=7 )
        self.next_btn3.grid(column=0,row=2,pady= 10,padx= 10)

        self.next_btn4 = tk.Button(self.nav_frame, text='Way', command    =self.frame4_visible,
                                                                 background = "white",
                                                                 foreground = "black",
                                                                       font = font_normal_btn,width=7 )
        self.next_btn4.grid(column=0,row=3,pady= 10,padx= 10)


        # First Frame
        self.frame1 = tk.Frame(self)
        self.frame1.grid(column=1,row=0)

        self.txt_label_photo = tk.Label(self.frame1,text="3D Point App", font=font_big_btn)
        self.txt_label_photo.grid(row=0,sticky="EW",pady= 20,padx= 10)

        self.frame3 = tk.Frame(self)
        start_img = Image.open("3d_printer.jpg").resize((400,400))
        start_img = ImageTk.PhotoImage(start_img)
        self.photo_label_start = tk.Label(self.frame1, image = start_img)
        self.photo_label_start.image = start_img
        self.photo_label_start.grid(row=1,pady= 20,padx= 10,sticky="EW")

        # Secound Frame
        self.frame2 = tk.Frame(self)

        self.txt_label_2 = tk.Label(self.frame2,text="File processing",font=font_big_btn)
        self.txt_label_2.grid(row=0,column=0,sticky="EW",pady=5,padx= 10)

        self.file_xyz = None

        self.entry_file_xyz = tk.Entry(self.frame2, font=font_small_btn, width=25)
        self.entry_file_xyz.insert(0,"Choose file")
        self.entry_file_xyz.config(state='disabled')
        self.entry_file_xyz.grid(column=0,row=1,pady= 10,padx= 10)

        self.next_photo_btn = tk.Button(self.frame2, text='select file', command    = self.__select_file_xyz,
                                                                         background = "white",
                                                                         foreground = "black",
                                                                       font = font_small_btn,width=10 )
        self.next_photo_btn.grid(column=1,row=1,pady= 10,padx= 10)

        self.entry_save_file = tk.Entry(self.frame2, font=font_small_btn, width=25)
        self.entry_save_file.grid(column=0,row=2,pady= 10,padx= 10)

        self.apply_save_file_btn = tk.Button(self.frame2, text='apply', command    = self.__set_save_file,
                                                                         background = "white",
                                                                         foreground = "black",
                                                                       font = font_small_btn,width=10 )
        self.apply_save_file_btn.grid(column=1,row=2,pady= 10,padx= 10)

        self.player_label = tk.Label(self.frame2)
        self.player_label.grid(row=3,columnspan=3, sticky="EW")
        self.player = tkvideo("C:\\Users\\Dell\\Desktop\\Js\\Video.mkv",self.player_label , loop=1, size=(400, 300))
        self.player.play()


        self.start_way_btn = tk.Button(self.frame2, text='START', command    = self.__start_create_way,
                                                                         background = "white",
                                                                         foreground = "black",
                                                                        font = font_small_btn, )
        self.start_way_btn.grid( pady=10, padx=10, row=4,columnspan=3, sticky="EW")
        self.preview_way_btn = tk.Button(self.frame2, text='PREVIEW', command    = self.__preview,
                                                                         background = "white",
                                                                         foreground = "black",
                                                                        font = font_small_btn, )
        self.preview_way_btn.grid( pady=10, padx=10, row=5,columnspan=3, sticky="EW")

        # Third Frame
        self.frame3 = tk.Frame(self)
        default_img = Image.open("Galeria/default.jpg").resize((300, 300))
        default_img = ImageTk.PhotoImage(default_img)
        self.photo_label = tk.Label(self.frame3, image = default_img)
        self.photo_label.image = default_img
        self.photo_label.grid(column=1,row=1,pady= 10,padx= 10)

        self.next_photo_btn = tk.Button(self.frame3, text='>', command    =self.__next_photo,
                                                                 background = "white",
                                                                 foreground = "black",
                                                                       font = font_small_btn )
        self.next_photo_btn.grid(column=2,row=1,pady= 10,padx= 10)


        self.prev_photo_btn = tk.Button(self.frame3, text='<', command    =self.__prev_photo,
                                                                background = "white",
                                                                     foreground = "black",
                                                                       font = font_small_btn )
        self.prev_photo_btn.grid(column=0,row=1,pady= 10,padx= 10)

        self.results = tk.Listbox(self.frame3)
        self.results.grid(row=2,sticky="EW",columnspan = 5)

        self.show_btn = tk.Button(self.frame3, text='SHOW', command    =self.__read_file,
                                                                background = "white",
                                                                     foreground = "black",
                                                                       font = font_small_btn )
        self.show_btn.grid(column=1,row=3,pady= 5,padx= 10,sticky="EW")

        self.show_btn = tk.Button(self.frame3, text='VIEW SELECTED FILE FROM DB ', command    =self.__show_plot_db,
                                                                background = "white",
                                                                     foreground = "black",
                                                                       font = font_small_btn )
        self.show_btn.grid(column=1,row=4,pady= 5,padx= 10,sticky="EW")



        # 4 Frame
        self.frame4 = tk.Frame(self)
        self.txt_label = tk.Label(self.frame4,text="Add extra points", font=font_big_btn)
        self.txt_label.grid(row=0,sticky="EW",pady= 20,padx= 10)


        self.txt_description = tk.Label(self.frame4,text="Nr points", font=font_small_btn)
        self.txt_description.grid(column=0,row=2,pady= 10,padx= 10,sticky="W")

        self.entry_nr_points = tk.Entry(self.frame4, font=font_small_btn, width=15)
        self.entry_nr_points.grid(column=0,row=2, sticky="E" ,pady= 10,padx= 10)

        self.entry_file = tk.Entry(self.frame4, font=font_small_btn, width=25)
        self.entry_file.insert(0,"Choose file")
        self.entry_file.config(state='disabled')
        self.entry_file.grid(column=0,row=1,pady= 10,padx= 10)

        self.selct_file_btn = tk.Button(self.frame4, text='select file', command    = self.__select_file_xyz2,
                                                                         background = "white",
                                                                         foreground = "black",
                                                                       font = font_small_btn,width=10 )
        self.selct_file_btn.grid(column=1, row=1, pady=10, padx=10)

        self.apply_point_btn = tk.Button(self.frame4, text='apply', command    = self.__create_point,
                                                                         background = "white",
                                                                         foreground = "black",
                                                                       font = font_small_btn,width=10 )
        self.apply_point_btn.grid(column=1,row=2,pady= 10,padx= 10)
        self.show_btn = tk.Button(self.frame4, text='SHOW', command    =self.__show_cloud_point,
                                                                background = "white",
                                                                     foreground = "black",
                                                                       font = font_small_btn )
        self.show_btn.grid(sticky="EW",row=3,pady= 10,padx= 10,columnspan=3)

        self.save_btn = tk.Button(self.frame4, text='SAVE SELECTED POINT TO DB', command    =self.__save_to_db,
                                                                background = "white",
                                                                     foreground = "black",
                                                                       font = font_small_btn )
        self.save_btn.grid(sticky="EW",row=4,pady= 10,padx= 10,columnspan=3)

    def frame1_visible(self):
        self.frame2.grid_remove()
        self.frame3.grid_remove()
        self.frame4.grid_remove()
        self.frame1.grid(column=1,row=0)

    def frame2_visible(self):
        self.frame1.grid_remove()
        self.frame3.grid_remove()
        self.frame4.grid_remove()
        self.frame2.grid(column=1,row=0)

    def frame3_visible(self):
        self.frame2.grid_remove()
        self.frame1.grid_remove()
        self.frame4.grid_remove()
        self.frame3.grid(column=1, row=0)

        images = []
        for root, dirs, files in os.walk("./Galeria"):
            for filename in files:
                images.append("./Galeria/" + filename)
        self.__my_gallery.set_galerry(images)


    def frame4_visible(self):
        self.frame2.grid_remove()
        self.frame1.grid_remove()
        self.frame3.grid_remove()
        self.frame4.grid(column=1, row=0)



    def __next_photo(self):
        img = self.__my_gallery.get_next_photo()
        self.photo_label['image'] = img
        self.photo_label.image = img

    def __prev_photo(self):
        img = self.__my_gallery.get_prev_photo()
        self.photo_label['image'] = img
        self.photo_label.image = img

    def __read_file(self):

        con = sqlite3.connect('database.db')
        cur = con.cursor()

        files = []
        for row in cur.execute('SELECT file_name FROM ways group by file_name'):
            files.append(row[0])

        self.results.delete(0, tk.END)
        try:
            for file_name in (files):
                self.results.insert(tk.END,file_name)
        except:
            pass

    def __select_file_xyz(self):
        file_name = fd.askopenfilename()
        if file_name != "":
            self.__file_xyz = file_name
            self.entry_file_xyz.config(state=NORMAL)
            self.entry_file_xyz.delete(0, END)
            self.entry_file_xyz.insert(0, file_name.split("/")[-1])
            self.entry_file_xyz.config(state='disabled')

    def __select_file_xyz2(self):
        file_name = fd.askopenfilename()
        if file_name != "":
            self.__file_xyz = file_name
            self.entry_file.config(state=NORMAL)
            self.entry_file.delete(0, END)
            self.entry_file.insert(0, file_name.split("/")[-1])
            self.entry_file.config(state='disabled')

        else:
            self.__file_xyz = ""
            self.entry_file_xyz.config(state=NORMAL)
            self.entry_file_xyz.delete(0, END)
            self.entry_file_xyz.insert(0, "Choose file")
            self.entry_file_xyz.config(state='disabled')

    def __set_save_file(self):
        self.__save_file = self.entry_save_file.get()

    def __start_create_way(self):
        if self.__file_xyz != "" and self.__save_file != "":
            cwc = CWayCreator(self.__file_xyz,"./Files/"+self.__save_file)
            cwc.run()

    def __preview(self):
        if self.__file_xyz != "":
            with open(self.__file_xyz) as plik:
                tab = [list(map(float, wiersz.split(' '))) for wiersz in plik]

            fig = plt.figure()
            ax = fig.gca(projection='3d')
            P=np.array(tab)
            z = P[:,2]
            x = P[:,0]
            y = P[:,1]
            ax.scatter(x,y, z, c='b', marker='v')

            ax.legend()
            plt.show()

    def __create_point(self):
        points = CMulPoints(self.__file_xyz)
        points.run(int(self.entry_nr_points.get()))


    def __show_cloud_point(self):
        with open(self.__file_xyz) as plik:
            tab = [list(map(float, wiersz.split(' '))) for wiersz in plik]

        P1 =np.array(tab)
        v = pptk.viewer(P1)
        v.set(point_size=0.1)

    def __save_to_db(self):
        if self.__file_xyz != "":
            with open(self.__file_xyz) as plik:
                tab = [list(map(float, wiersz.split(' '))) for wiersz in plik]

            date_time = datetime.datetime.now()
            id = str(date_time) +"-"+ self.__file_xyz.split("/")[-1]
            filename = self.__file_xyz

            con = sqlite3.connect('database.db')
            cur = con.cursor()
            sql = '''
                INSERT INTO ways(id , file_name , x , y , z )
                VALUES(?,?,?,?,?)
            '''
            for row in tab:
                cur.execute(sql, (id, filename, row[0], row[1], row[2]))
            con.commit()
            con.close()


    def __show_plot_db(self):
        last_sel = ""
        for i in self.results.curselection():
            last_sel = self.results.get(i)
        if last_sel != "":
            with open(last_sel) as plik:
                tab = [list(map(float, wiersz.split(' '))) for wiersz in plik]
            v = pptk.viewer(np.array(tab))
            v.set(point_size=0.1)
