from pyfiglet import figlet_format
import time
import random

# Player Charater Option 1
lee_kennedy = {
    "Name": "Lee Kennedy",
    "Health": 100,
    "Attack Power": 10,
    "Weapon": "Unarmed",
    "Skill": "lockpick",
    "Inventory": [],
    "Insight": []
}

# Player Charater Option 1
claire_greenfield = {
    "Name": "Claire Greenfield",
    "Health": 120,
    "Attack Power": 20,
    "Weapon": "Unarmed",
    "Skill": "hack",
    "Inventory": [],
    "Insight": []
}

# Populated once Player Character selected
player_card = {
    "Name": "",
    "Health": 100,
    "Attack Power": 10,
    "Weapon": "Unarmed",
    "Skill": "",
    "Inventory": [],
    "Insight": []
    }

# List of rooms Player has checked
checked_rooms = []

# Help variable, for use in game
help = ("\nType 'exit' to quit to main menu."
        "\nType 'pc' to view Player Card."
        "\nType 'n', 'e', 's', 'w', 'u', 'd' to move north, south, east, west, up or down."
        "\nType 'l' to look around."
        "\nType 'i' followed by an OBJECT to inspect that object."
        "\nType 'use' followed by an OBJECT to inspect that object."
        "\nType 'loot' followed by an OBJECT to add it to your inventory."
        "\nType 'heal' to use a First Aid Kit."
        "\nType 'atk' followed by an ENEMY to attack."
        "\nType 'flee' to escape a room in a random direction.\n")

# Global functions for repeated actions
def fa_kit_loot(): 
    """
    Adds First Aid Kit to player inventory
    """
    player_card["Inventory"].append("First Aid Kit")
    type_text("\nYou rummage through the First Aid Kit and take some supplies.\n")

def heal():
    """
    Uses a First Aid Kit to heal 30 hp
    """
    if "First Aid Kit" in player_card["Inventory"]:
        player_card["Health"] += 30
        player_card["Inventory"].remove("First Aid Kit")
        type_text("\nYou use a First Aid Kit and heal 30 hp.\n")
        return
    else:
        type_text("\nYou don't have any First Aid Kits!\n")

# End Game Functions
#def game_over():

#def end_game_good():

#def end_game_bad():

def type_text(text):
    """
    Prints text one character at a time to create a 'typing' animation.
    """
    #for char in text:
    #    print(char, end='', flush=True)
    #    time.sleep(random.uniform(0.001, 0.09))
    print(text)

def main_menu():
    """
    The menu the Player is presented with when opening the app.
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

    start_up_text = ("\nWelcome to Raven's Rest, a text-based adventure game!" 
    "\nI'm Poe, your digital Game Master (or 'GM' for short)." 
    "\nType out what you want to do, and I'll try my best to make it happen!" 
    "\nIf this is your first time playing, please be sure to read the rules before" 
    "\nyou start.\n" 
    "\nTo read how to play, type 'h2p'.\n"
    "\nTo start the game, type 'play'.\n")
    type_text(start_up_text)

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
    Section to explain the rules to the Player and instructions on how to play the game.
    """
    how_to_play_poe_1 = ("\nRaven's Rest is a text-based adventure game. You control your character by" 
    "\nentering commands in the terminal. The goal is to navigate the Raven's Rest" 
    "\nHotel and find your brother, completing puzzles and defeating enemies as you go.\n"
    "\nHere are the rules:\n")

    rules = ("\n1. Mind your manners! Don't interrupt your GM. If you type" 
             "\nwhilst Poe is typing, you might cause an error, preventing your" 
             "\nnext command from being recognised. Let him finish before typing" 
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
             "\nThe following are common commands you'll use throughout the game:\n")

    how_to_play_poe_2 = ("\nThis list is not exhaustive. It just gives examples of common"
                        "\ncommands you'll use. Remember to use the 'help' command if you get" 
                        "\nstuck, or consult your Player Card by using the 'pc' command to see if" 
                        "\nyour character has a skill or item that might be useful.\n"
                        "\nGood luck, and have fun!\n")

    type_text(how_to_play_poe_1)
    print(figlet_format("How to Play\n", justify="center"))
    type_text(rules)
    type_text(help)
    type_text(how_to_play_poe_2)

    while True:
        leave_how_to_play = input("\nType 'play' to start the game or 'back' to return to the main menu.\n")

        if leave_how_to_play.lower() == "back":
            main_menu()
            break
        elif leave_how_to_play.lower() == "play":
            character_selection()
            break
        else:
            leave_how_to_play_error = ("\nI don't know that one... Type 'play' to start the game or 'back' to" 
            "\nreturn to the main menu.")
            type_text(leave_how_to_play_error)

def character_selection():
    """
    Section where the Player must select their Player Character.
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
            type_text("\nYou have selected Lee Kennedy.\n")
            start_game()
            break
        elif character_choice.lower() == "c":
            player_card.update(claire_greenfield)
            type_text("\nYou have selected Claire Greenfield.\n")
            start_game()
            break
        else:
            character_choice_error = "\nI don't know that one... Type 'l' for Lee or 'c' for Claire."
            type_text(character_choice_error)     

def start_game():
    """
    The game's intro and first area
    """
    intro_text = ("\nRain drops drum against the windshield of your car as you roll along the winding"
                  "\ncountry road. The night is black and water blurs your view like ink poured over" 
                  "\nglass. Between swipes of the wiperblades, you see it. Looming ahead of you," 
                  "\ncaught in the beam of the headlights. The Raven's Rest Hotel.\n"
                  "\nYou pull off the road into a small car park. Gravel crunches beneath the tyres" 
                  "\nas you slowly come to a halt. You kill the engine and are immediately plummeted" 
                  "\ninto pitch darkness. Neither the car park nor the hotel offer any light. You" 
                  "\npull out your mobile phone, the dim glow flooding the interior of your car, and" 
                  "\nopen a photo. Your brother, Chris, grins up at you. The photo was taken 1 week" 
                  "\nago. The last time anyone had seen or heard from him. In the background of the" 
                  "\nimage, lurking like a shadow, sits the Raven's Rest Hotel. Taking a moment to" 
                  "\nsteel yourself, you switch on your phone's flashlight, release the lock on the" 
                  "\ncar door and step out into the night.\n" 
                  "\nCold bites at you as you turn your collar against the wind and rain. You hold"
                  "\nthe light of your phone up to the hotel, though it's beam is almost instantly"
                  "\nchoked by the unrelenting weather. You can make out the dark slate walls of the"
                  "\nhotel, but as they stretch into the night sky, you're unable to see beyond even"
                  "\nthe second storey. Skirting along a large, wooden porch, you eventually come"
                  "\nacross a door.\n")
    type_text(intro_text)

    while True:
        intro_choice = input("\nType 'o' to open the door.\n")

        if intro_choice.lower() == "o":
            type_text("\nWith a shrill creak, the door yawns open...\n")
            foyer()
            break
        elif intro_choice.lower() == "help":
            print(help)
        elif intro_choice.lower() == "pc":
            print(player_card)
        elif intro_choice.lower() == "exit":
            main_menu()
            break
        else:
            intro_error = '\n"I have to go inside. For Chris."\n'
            type_text(intro_error)  

def foyer():
    """
    The Hotel Foyer - the first room the Player enters.
    """
    foyer_text_initial = ("\nYou step into a wide, empty Foyer. The beam of your flashlight barely"
    "\npenertrates the surrounding shadows as you pan across the room. Ahead of you" 
    "\nbeneath the gloomy red glow of an emergency lamp, you see the reception DESK." 
    "\nOn both the EAST and WEST sides of the room are doors leading out of the Foyer.\n")

    foyer_text_return = ("\nYou step again into the wide, empty Foyer.\n")

    if "Foyer" in checked_rooms:
        type_text(foyer_text_return)
    else:
        type_text(foyer_text_initial)
        checked_rooms.append("Foyer")

    foyer_look = ("\nYou look around the Foyer. You see the reception DESK ahead of you, a door to"
    "\nto the EAST ('e') and a door to the WEST ('w'). The entrance to the hotel is"
    "\nbehind you, to the SOUTH ('s').")

    desk_inspect = ("You approach the desk for a closer look. A COMPUTER and a BELL sit on the desk." 
    "\nBehind the desk is a DOOR with a sign that reads, 'Staff Only'.\n")

    foyer_computer_claire = ("\nThe computer is locked, but you manage to hack it. You flick through some" 
    "\nfiles nand discover Chris' room number, located on the 1st Floor East Wing.\n")
    foyer_computer_lee = ("\nThe computer is locked.\n")

    def foyer_computer_use():
        if power == True and player_card["Skill"] == "hack":
            type_text(foyer_computer_claire)
            player_card["Insight"].append("Chris' room location, ")
        elif power == True and player_card["Skill"] == "lockpick":
            type_text("foyer_computer_lee")
        elif power == False:
            type_text("\nThe power is still out. Maybe you can find a way to turn it back on...\n")
        else:
            RuntimeError
    
    foyer_door_use_lee = "\nThe door is locked, but you manage to pick it.\n"
    foyer_door_use_claire = "\nThe door is locked.\n"

    def foyer_door_use():
        if player_card["Skill"] == "lockpick":
            type_text(foyer_door_use_lee)
            foyer_staff_room()
        elif player_card["Skill"] == "lockpick":
            type_text(foyer_door_use_claire)
        else:
            RuntimeError

    while True:
        foyer_choice = input("\nWhat do you do?\n")

        if foyer_choice.lower() == "l":
            type_text(foyer_look)
        elif foyer_choice.lower() == "help":
            print(help)
        elif foyer_choice.lower() == "pc":
            print(player_card)
        elif foyer_choice.lower() == "exit":
            main_menu()
            break
        elif foyer_choice.lower() == "heal":
            heal()
        elif foyer_choice.lower() == "e":
            type_text("\nYou exit out of the east door.\n")
            east_wing()
            break
        elif foyer_choice.lower() == "w":
            type_text("\nYou exit out of the west door.\n")
            west_wing()
            break
        elif foyer_choice.lower() == "s":
            if chris_status == "alive":
                end_game_good()
            elif chris_status == "dead":
                end_game_bad()
            elif chris_status == "infected":
                end_game_bad()
            else:
                type_text("I'm not leaving until I've found Chris.")
        elif foyer_choice.lower() == "i desk":
            type_text(desk_inspect)
        elif foyer_choice.lower() == "use computer":
            foyer_computer_use()
        elif foyer_choice.lower() == "use door":
            foyer_door_use()
        elif foyer_choice.lower() == "use bell":
            type_text("\nYou ring the bell. A high-pitched 'ding' echoes throughout the empty room for" 
            "\na moment, before silence creeps back into the foyer. No one comes.\n")
        else:
            foyer_error = "\nYou can't do that... Use the 'help' command if you're stuck.\n"
            type_text(foyer_error)

def foyer_staff_room():
    """
    The Foyer Staff Room - Game Location.
    """
    foyer_staff_room_text_initial = ("\nThe door leads into a small cupboard space. Whilst inspecting, the beam of your" 
    "\nflashlight passes over something slumped on the floor. Your heart sinks. It's a"
    "\ndead body. A BLOODY KNIFE protruding from the side of it's neck.\n")

    foyer_staff_room_text_return = ("\nYou enter the cupboard, trying your best not to look at the dead body.\n")

    if "Foyer Staff Room" in checked_rooms:
        type_text(foyer_staff_room_text_return)
    else:
        type_text(foyer_staff_room_text_initial)
        checked_rooms.append("Foyer Staff Room")

    bloody_knife_loot = ("\nYou crouch beside the body and grab the blade by its handle. With a sickening" 
    "\nsquelch, you slide the knife from their neck. Dark crimson pools around your" 
    "\nfeet.\n")

    while True:
        foyer_staff_room_choice = input("\nWhat do you do?\n")

        if foyer_staff_room_choice.lower() == "l":
            if "Bloody Knife" in player_card["Inventory"]:
                type_text("\nThere's nothing else of use here. The foyer is to your SOUTH ('s').\n")
            else: 
                type_text("\nYou take a moment to collect yourself, then look around the cupboard. The" 
    "\nBLOODY KNIFE sticks out of the dead body's neck. The foyer is to your SOUTH" 
    "\n('s').\n")
        elif foyer_staff_room_choice.lower() == "help":
            print(help)
        elif foyer_staff_room_choice.lower() == "pc":
            print(player_card)
        elif foyer_staff_room_choice.lower() == "exit":
            main_menu()
            break
        elif foyer_staff_room_choice.lower() == "heal":
            heal()
        elif foyer_staff_room_choice.lower() == "loot bloody knife":
            if "Bloody Knife" in player_card["Inventory"]:
                type_text("\nYou've already taken the bloody knife.\n")
            else:
                type_text(bloody_knife_loot)
                player_card["Inventory"].append("Bloody Knife")
                player_card["Weapon"] = "Bloody Knife"
                player_card["Attack Power"] = 20
        elif foyer_staff_room_choice.lower() == "s":
            type_text("\nYou exit to the south, returning to the Foyer.\n")
            foyer()
            return
        else:
            foyer_staff_room_error = "\nYou can't do that... Use the 'help' command if you're stuck.\n"
            type_text(foyer_staff_room_error)

#def east_wing_1():
    #checked_rooms.append("East Wing 1")

#def west_wing_1():
    #checked_rooms.append("West Wing 1")

# Start the game
#main_menu()

# In-game feature to determine if the hotel has power
power = False

# In-game feature to determine Chris' status
chris_status = "Unknown"

# 'If' statement to handle player death
if player_card["Health"] == 0:
    game_over()

character_selection()