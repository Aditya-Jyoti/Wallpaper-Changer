import ctypes
from os import getcwd
from WallpaperChanger.config_wallpaper import config_wallpaper


def change_wallpaper(img: str):
    parent = getcwd()
    path = f"{parent}\\assets\\temp\\{img}.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


if __name__ == "__main__":
    img = config_wallpaper()
    change_wallpaper(img)
