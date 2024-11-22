import requests, re, pyperclip, time
from PIL import Image
from io import BytesIO
from types import SimpleNamespace


def get_steam_banner(args) -> str:
    game_name: str = args.name
    show: bool = args.show

    ans = requests.get(
        "https://store.steampowered.com/search",
        params={
            "term": game_name,
            "ignore_preferences": 1,
            "ndl": 1
        }
    )

    regex = r"https:\/\/store\.steampowered\.com\/app\/(\d+)"
    match = re.findall(regex, ans.text)
    game_ids = list(match)

    game_image_url = f"https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/{game_ids[0]}/header.jpg"

    if show:
        _download_and_show_image(game_image_url)

    pyperclip.copy(game_image_url)
    print(game_image_url)
    return game_image_url


def _download_and_show_image(game_image_url:str):
    ans = requests.get(game_image_url)

    if ans.status_code == 200:
        img_data = BytesIO(ans.content)
        Image.open(img_data).show()
        time.sleep(5) # input()
    else:
        print(f"Failed to fetch image. HTTP status code: {ans.status_code}")


if __name__ == "__main__":
    game_name = input("Enter Game Name: ")
    args = SimpleNamespace(**{"name":game_name,"show":True})
    game_image_url = get_steam_banner(args)