import requests, re, pyperclip
from PIL import Image
from io import BytesIO


def get_steam_banner(args) -> str :
    
    game_name: str = args.name
    print(game_name)

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

    pyperclip.copy(game_image_url)
    print(game_image_url)
    return game_image_url


if __name__ == "__main__":
    game_name = input("Enter Game Name: ")
    game_image_url = get_steam_banner(game_name)
    ans = requests.get(game_image_url)

    if ans.status_code == 200:
        img_data = BytesIO(ans.content)
        Image.open(img_data).show()
        input()
    else:
        print(f"Failed to fetch image. HTTP status code: {ans.status_code}")