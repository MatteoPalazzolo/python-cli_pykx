### mimg
import glob, os, yaml
from collections import defaultdict


def ph_img() -> str:
    ANALYSIS_PATH = _get_analysis_path_from_config()

    # lista dei percorsi delle cartelle Anime, Film, Videogiochi...
    media_types: list[str] = [os.path.basename(e) for e in glob.glob(ANALYSIS_PATH + "*")if os.path.isdir(e)]

    # per ogni categoria (Anime, Film, Videogiochi...) cerca in tutti i file 
    #  e aggiungi a content quelli che hanno l'immagine di default
    content: dict[str,list] = defaultdict(lambda: [])
    for t in media_types:
        media_path_list: str = glob.glob(ANALYSIS_PATH + t + "\\*.md")
        for media_path in media_path_list:
            if _has_default_img(media_path):
                content[t].append(os.path.basename(media_path))

    # converti il dict in yaml e stampa
    print(yaml.dump(dict(content), default_flow_style=False, allow_unicode=True))
    return content

def _get_analysis_path_from_config() -> str:
    with open("config.yaml", "r", encoding="UTF-8") as file:
        config = yaml.safe_load(file)
        analysis_path = config["analysis_path"]
        return analysis_path

def _has_default_img(media_path:str) -> bool:
    with open(media_path, "r", encoding="UTF-8") as file:
        return "![](replace.jpg)" in file.read()

if __name__ == "__main__":
    ph_img()