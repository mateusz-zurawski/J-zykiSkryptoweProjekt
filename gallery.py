from PIL import Image, ImageTk

class Gallery:
    def __init__(self):
        self.__photo_gallery_list = []
        self.__current_photo = 0

    def set_galerry(self,images):
        self.__photo_gallery_list = images

    def get_next_photo(self):
        size = len(self.__photo_gallery_list)

        if size > 0 and self.__current_photo < size - 1:
            img = Image.open(self.__photo_gallery_list[self.__current_photo+1]).resize((300, 300))
            img = ImageTk.PhotoImage(img)
            self.__current_photo += 1
            return img

        elif size != 0:
            img = Image.open(self.__photo_gallery_list[0]).resize((300, 300))
            img = ImageTk.PhotoImage(img)
            self.__current_photo = 0
            return img

        return None

    def get_prev_photo(self):
        size = len(self.__photo_gallery_list)
        if size > 0 and self.__current_photo > 0:
            img = Image.open(self.__photo_gallery_list[self.__current_photo - 1]).resize((300, 300))
            img = ImageTk.PhotoImage(img)
            self.__current_photo -= 1
            return img
        elif size != 0:
            img = Image.open(self.__photo_gallery_list[size - 1]).resize((300, 300))
            img = ImageTk.PhotoImage(img)
            self.__current_photo = size - 1
            return img
        return None