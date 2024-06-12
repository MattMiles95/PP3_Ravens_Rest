from pyfiglet import figlet_format
import time
import random
from colorama import init, Fore, Style

# Initialise colorama
init(autoreset=True)

# Player Charater Option 1
lee_kennedy = {
    "Name": "Lee Kennedy",
    "Health": 100,
    "Attack Power": 10,
    "Weapon": "Unarmed",
    "Inventory": []
}

# Player Charater Option 1
claire_greenfield = {
    "Name": "Claire Greenfield",
    "Health": 120,
    "Attack Power": 20,
    "Weapon": "Unarmed",
    "Inventory": []
}

# Populated once Player Character selected
player_card = {}

def type_text(text):
    """
    Prints text one character at a time to create a 'typing' animation.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.001, 0.09))

def main_menu():
    """
    The menu the User is presented with when opening the app.
    """
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

    intro = ("\nWelcome to Raven's Rest, a text-based adventure game!" 
    "\nI'm Poe, your digital Game Master (or 'GM' for short)." 
    "\nType out what you want to do, and I'll try my best to make it happen!" 
    "\nIf this is your first time playing, please be sure to read the rules before" 
    "\nyou start.\n" 
    "\nTo read how to play, type 'h2p'.\n"
    "\nTo start the game, type 'play'.\n")
    type_text(intro)

    while True:
        main_menu_choice = input()

        if main_menu_choice.lower() == "play":
            character_selection()
            break
        elif main_menu_choice.lower() == "h2p":
            how_to_play()
            break
        else:
            main_menu_error = ("\nI don't know that one..." 
                               "Type 'play' to start the game or 'h2p' to read how to play.\n")
            type_text(main_menu_error)

def how_to_play():
    """
    Section to explain the rules to the User and instructions on how to play the game.
    """
    how_to_play_intro = ("\nRaven's Rest is a text-based adventure game. You control your" 
    "\ncharacter by entering commands in the terminal. The goal is to navigate the Raven's" 
    "\nRest Hotel and find your brother, completing puzzles and defeating enemies as you go.\n"
    "\nHere are the rules:\n")
    
    how_to_play_text = ("\n1. Mind your manners! Don't interrupt your GM. If you type" 
                        "\nwhilst Poe is typing, you might cause an error, preventing your" 
                        "\nnext answer from being recognised. Let him finish before typing" 
                        "\nanything.\n"
                        "\n2. If you type something that isn't a command, you'll be prompted" 
                        "\nto try again.\n"
                        "\n3. You can quit to the main menu at any time by using the 'exit'" 
                        "\ncommand. But be aware, you'll lose all progress and there's no way to" 
                        "\nreload a previous game.\n"
                        "\n4. If you get stuck, type 'help' to see a list of commands you" 
                        "\ncan use.\n"
                        "\n5. Once you start the game, you will have to select a character." 
                        "\nTake note of your character's bio, as their individual skills and" 
                        "\nexperiences might be useful later on.\n"
                        "\n6. You can bring up your character's 'Player Card' at any time" 
                        "\nby using the 'pc' command. Here you'll see your character's current" 
                        "\nstats and any items in your inventory.\n"
                        "\n7. The Raven's Rest can be a dangerous place. Your 'Attack Power'" 
                        "\nstat determines how much damage you can do in a single attack." 
                        "\nBe sure to pick up any weapons you might find to help you deal" 
                        "\nmore damage.\n"
                        "\n8. Keep an eye on your health. If it drops to zero, that's" 
                        "\ngame over. Healing items can be found and used to keep you going.\n"
                        "\nThe following are common commands you'll use throughout the game:\n"
                        "\n'n', 's', 'e' and 'w' to move north, south, east and west, respectively."
                        "\n'l' to look around the room you're in."
                        "\n'i' followed by an object to inspect that object."
                        "\n'u' followed by an object to use that object."
                        "\n'loot' followed by an object to put that object in your inventory."
                        "\n'atk' to attack an enemy."
                        "\n'flee' to flee from a fight, back to the previous room.\n"
                        "\nThis list is not exhaustive. It just gives examples of common"
                        "\ncommands you'll use. Remember to use the 'help' command if you get" 
                        "\nstuck, or consult your Player Card by using the 'pc' command to see if" 
                        "\nyour character has a skill or item that might be useful.\n"
                        "\nGood luck, and have fun!\n")
    
    how_to_play_text_color = "object"
    colored_how_to_play_text = how_to_play_text.replace(how_to_play_text_color, f"{Fore.YELLOW}{how_to_play_text_color}{Style.RESET_ALL}")
    type_text(how_to_play_intro)
    print(figlet_format("How to Play\n", justify="center"))
    type_text(colored_how_to_play_text)

    while True:
        leave_how_to_play = input("\nType 'play' to start the game or 'back' to return to the main menu.\n")

        if leave_how_to_play.lower() == "back":
            main_menu()
            break
        elif leave_how_to_play.lower() == "play":
            character_selection()
            break
        else:
            leave_how_to_play_error = "\nI don't know that one... Type 'play' to start the game or 'back' to return to the main menu."
            type_text(leave_how_to_play_error)

def character_selection():
    """
    Section where the User must select their Player Character.
    """
    character_selection_text = ("\nChoose your character:\n"
    "\nLee Kennedy" 
    "\nAge: 36" 
    "\nOccupation: Locksmith" 
    "\nHobby: Bird Watching\n"
    "\nClaire Greenfield" 
    "\nAge: 29" 
    "\nOccupation: Programmer" 
    "\nHobby: Kickboxing\n")
    type_text(character_selection_text)

    while True:
        character_choice = input("\nType 'l' for Lee or 'c' for Claire:")

        if character_choice.lower() == "l":
            player_card.update(lee_kennedy)
            start_game()
            break
        elif character_choice.lower() == "c":
            player_card.update(claire_greenfield)
            start_game()
            break
        else:
            character_choice_error = "\nI don't know that one... Type 'l' for Lee or 'c' for Claire."
            type_text(character_choice_error)     

def start_game():
    """
    The game's intro and first area
    """
    print("\nYou've started the game!")
    print(player_card)

# Start the game
main_menu()