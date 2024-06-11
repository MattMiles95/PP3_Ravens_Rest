from pyfiglet import figlet_format
from pprint import pprint

def main_menu():
    raven_image = r"""
                      ⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡟⠋⢻⣷⣄⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣷⣿⣿⣿⣿⣿⣶⣾⣿⣿⠿⠿⠿⠶⠄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⠟⠻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣆⣤⠿⢶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    title = r"""
    ______  ___  _   _ _____ _   _ _ _____ 
    | ___ \/ _ \| | | |  ___| \ | ( )  ___|
    | |_/ / /_\ \ | | | |__ |  \| |/\ `--. 
    |    /|  _  | | | |  __|| . ` |  `--. \
    | |\ \| | | \ \_/ / |___| |\  | /\__/ /
    \_| \_\_| |_/\___/\____/\_| \_/ \____/ 

    ______ _____ _____ _____ 
    | ___ \  ___/  ___|_   _|
    | |_/ / |__ \ `--.  | |  
    |    /|  __| `--. \ | |  
    | |\ \| |___/\__/ / | |  
    \_| \_\____/\____/  \_/  

    """
    spacer = ' ' * 1

    for a, b in zip(raven_image.split('\n'), title.split('\n')):
        print(f"{a}{spacer}{b}")

    print("\nWelcome to Raven's Rest, a text-based adventure game!")
    print("\nI'm Poe, your digital Game Master (or 'GM' for short). Type out what you want to do, and I'll try my best to make it happen! If this is your first time playing, please be sure to read the rules before you start.")
    print("\nTo start the game, type 'play'.")
    print("\nTo read how to play, type 'h2p'.\n")

    while True:
        main_menu_choice = input()

        if main_menu_choice.lower() == "play":
            character_selection()
            break
        elif main_menu_choice.lower() == "h2p":
            how_to_play()
            break
        else:
            print("\nI don't know that one... Type 'play' to start the game or 'h2p' to read how to play.\n")

player_card = {
    "character": "Lee Kennedy",
    "health": 100,
    "attack": 10,
    "weapon": "Unarmed",
    "inventory": []
}

def character_selection():
    print("\nChoose your character:")
    print("\nLee Kennedy \nAge: 36 \nOccupation: Locksmith \nHobby: Bird Watching")
    print("\nClaire Greenfield \nAge: 29 \nOccupation: Programmer \nHobby: Kickboxing")
    while True:
        character_choice = input("\nType 'l' for Lee or 'c' for Claire:")

        if character_choice.lower() == "l":
            player_card["character"] = "Lee Kennedy"
            player_card["attack"] = 10
            start_game()
            break
        elif character_choice.lower() == "c":
            player_card["character"] = "Claire Greenfield"
            player_card["attack"] = 20
            start_game()
            break
        else:
            print("\nI don't know that one... Type 'l' for Lee or 'c' for Claire.")

def start_game():
    print("\nYou've started the game!")
    pprint(player_card)

# Start the game
main_menu()