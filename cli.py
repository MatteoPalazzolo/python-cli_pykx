import argparse
from tools import get_steam_banner, git_push

def main():
    parser = argparse.ArgumentParser(description="My Obsidian Toolbox CLI")
    
    # Add subcommands for each tool
    subparsers = parser.add_subparsers(dest="tools", required=True, help="Choose a tool.")

    # Tool 1: steam banner
    parser_tool1 = subparsers.add_parser("banner", help="Get steam banner url for a specific videogame.")
    parser_tool1.add_argument("-n", "--name", type=str, required=True, help="Videogame Name")
    parser_tool1.set_defaults(func=get_steam_banner)

    # Tool 2: git push
    parser_tool2 = subparsers.add_parser("push", help="Push all Obsidian valuts to Github.")
    parser_tool2.set_defaults(func=git_push)

    # Tool 3: ...

    args = parser.parse_args()
    args.func(args)

    #parser.print_help()

if __name__ == "__main__":
    main()