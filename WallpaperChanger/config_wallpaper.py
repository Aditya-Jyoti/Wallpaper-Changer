import requests
import toml
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
from .generate_wallpaper import generate_wallpaper_image


with open("settings.toml", "r") as f:
    settings = toml.load(f)

OFFSET = 80


def create_weather_image() -> None:
    response = requests.get(settings["settings"]["image"])
    with open("assets/temp/temp_widget.png", "wb") as f:
        f.write(response.content)

    widget_image = Image.open("assets/temp/temp_widget.png")
    widget_image = widget_image.crop((0, 28, 507, 139))
    widget_image.save("assets/temp/weather_widget.png")

    return


def config_wallpaper() -> str:
    def get_text_dimensions(text: str, font: ImageFont.FreeTypeFont) -> Tuple[int, int]:
        ascent, descent = font.getmetrics()

        text_width = font.getmask(text).getbbox()[2]
        text_height = font.getmask(text).getbbox()[3] + descent
        return (text_width, text_height)

    wallpaper_name = generate_wallpaper_image(
        [settings["wallpaper"]["width"], settings["wallpaper"]["height"]],
        settings["wallpaper"]["search_queries"],
    )

    wallpaper = Image.open(f"assets/wallpapers/{wallpaper_name}.png")
    drawable_wallpaper = ImageDraw.Draw(wallpaper)

    bold_font = ImageFont.truetype(settings["fonts"]["bold"], 60)
    regular_font = ImageFont.truetype(settings["fonts"]["regular"], 40)

    welcome_text = settings["settings"]["welcome_text"]
    welcome_size = get_text_dimensions(welcome_text, bold_font)

    drawable_wallpaper.text(
        (
            settings["wallpaper"]["width"] // 2 - welcome_size[0] // 2,
            settings["wallpaper"]["height"] // 2 - welcome_size[1] // 2 - OFFSET // 2,
        ),
        text=welcome_text,
        font=bold_font,
    )

    create_weather_image()
    widget_image = Image.open("assets/temp/weather_widget.png")

    wallpaper.paste(
        widget_image,
        (
            settings["wallpaper"]["width"] // 2 - widget_image.size[0] // 2,
            settings["wallpaper"]["height"] // 2
            - widget_image.size[1] // 2
            + OFFSET // 2,
        ),
        mask=widget_image,
    )

    wallpaper.save(f"assets/temp/{wallpaper_name}.jpg")

    return wallpaper_name


