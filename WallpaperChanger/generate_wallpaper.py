import requests
from typing import List
from datetime import datetime


def generate_wallpaper_image(size: List[int], search: List[str]) -> str:
    size_str = "x".join(str(i) for i in size)
    search_str = ",".join(search)
    image_name = f"wallpaper_{datetime.now().strftime(r'%d%m%y%H%M%S')}"

    response = requests.get(
        f"https://source.unsplash.com/random/{size_str}/?{search_str}"
    )

    with open(
        f"f:/Programming/Wallpaper-Changer/assets/wallpapers/{image_name}.png", "wb"
    ) as f:
        f.write(response.content)

    return image_name
