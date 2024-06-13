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

# List of items Player has collected
looted_items = []

# List of all slain enemies
slain_enemies = []

# Help variable, for use in game
help = ("\nType 'exit' to quit to main menu."
        "\nType 'pc' to view Player Card."
        "\nType 'n', 'e', 's', 'w', 'u', 'd' to move north, south, east, west, up or down."
        "\nType 'l' to look around."
        "\nType 'i' followed by an OBJECT to inspect that object."
        "\nType 'use' followed by an OBJECT to inspect that object."
        "\nType 'loot' followed by an OBJECT to add it to your inventory."
        "\nType 'heal' to use a First Aid Kit."
        "\nType 'atk' to attack."
        "\nType 'flee' to escape a room in a random direction.\n")

generic_error = "\nYou can't do that... Use the 'help' command if you're stuck.\n"

# Enemies
enemy = {
    "Name": None,
    "Health": 1,
    "Attack Power": 1,
    "Lootable": False
}

infected_bell_boy = {
    "Name": "Infected Bell Boy",
    "Health": 30,
    "Attack Power": 10,
    "Lootable": False
}

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

def atk():
    """
    Function for Player to attack Enemy
    """
    if enemy["Name"] in slain_enemies:
        print(f"{enemy['Name']} is already dead!")
    else:
        enemy["Health"] = enemy["Health"] - player_card["Attack Power"]
        print(f"You hit {enemy['Name']} for {player_card['Attack Power']}")
        player_card["Health"] = player_card["Health"] - enemy["Attack Power"]
        print(f"{enemy['Name']} hit you for {enemy['Attack Power']}")

        if enemy["Health"] == 0:
            print(f"\nWith a final rasping breath, {enemy['Name']} drops to the floor, their BODY cold and still.\n")
            enemy["Lootable"] = True
            slain.enemies.append(enemy["Name"])
    return

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

    foyer_look = ("\nYou look around the Foyer. You see the reception DESK ahead of you. A door to"
    "\nthe east ('e') with a sign that reads, 'Maintenance, Security & East" 
    "\nWing'. A door to the west ('w') with a sign that reads, 'Stairs to First Floor," 
    "\nBasement Lift & West Wing'. The entrance to the hotel is behind you, to the" 
    "\south ('s').")

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
        elif player_card["Skill"] == "hack":
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
            gf_east_wing_1()
            break
        elif foyer_choice.lower() == "w":
            type_text("\nYou exit out of the west door.\n")
            gf_west_wing_1()
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
            type_text(generic_error)

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
                type_text("\nThere's nothing else of use here. The foyer is to your south ('s').\n")
            else: 
                type_text("\nYou take a moment to collect yourself, then look around the cupboard. The" 
    "\nBLOODY KNIFE sticks out of the dead body's neck. The foyer is to your south" 
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
            if "Bloody Knife" in looted_items:
                type_text("\nYou've already taken the bloody knife.\n")
            else:
                type_text(bloody_knife_loot)
                looted_items.append("Bloody Knife")
                player_card["Weapon"] = "Bloody Knife"
                player_card["Attack Power"] = 20
        elif foyer_staff_room_choice.lower() == "s":
            type_text("\nYou exit to the south, returning to the Foyer.\n")
            foyer()
            return
        else:
            type_text(generic_error)

def gf_east_wing_1():
    """
    Ground Floor East Wing 1 - Game Location.
    """
    gf_east_wing_1_initial = ("\nYou step into the Ground Floor East Wing. Dark wooden doors adorned with silver" 
    "\nroom numbers run along both sides of the corridor. There is no trace of any" 
    "\npatron or employee. As you creep through the silent passage, you notice a" 
    "\nSupplies Cupboard to the south ('s'). Further east ('e') appears to be a" 
    "\nMaintenance Room. To the north ('n') are a set of double doors, continuing" 
    "\nfurther into the Ground Floor East Wing. To the west ('w') is the Foyer.\n")

    gf_east_wing_1_return = ("\nYou step into the Ground Floor East Wing corridor that abuts the Foyer.\n")

    if "Ground Floor East Wing 1" in checked_rooms:
        type_text(gf_east_wing_1_return)
    else:
        type_text(gf_east_wing_1_initial)
        checked_rooms.append("Ground Floor East Wing 1")

    while True:
        gf_east_wing_1_choice = input("\nWhat do you do?\n")

        if gf_east_wing_1_choice.lower() == "l":
            type_text("\nTo the north ('n') is a set of double doors continuing into the GF East Wing.\n"
            "\nTo the east ('e') is the Maintenance Room.\n"
            "\nTo the south ('s') is a Supplies Cupboard.\n"
            "\nTo the west ('w') is the Foyer.\n")
        elif gf_east_wing_1_choice.lower() == "help":
            print(help)
        elif gf_east_wing_1_choice.lower() == "pc":
            print(player_card)
        elif gf_east_wing_1_choice.lower() == "exit":
            main_menu()
            break
        elif gf_east_wing_1_choice.lower() == "heal":
            heal()
        elif gf_east_wing_1_choice.lower() == "n":
            type_text("\nYou pass through the double doors and continue through the GF East Wing.\n")
            gf_east_wing_2()
            break
        elif gf_east_wing_1_choice.lower() == "e":
            if "Keycard" in player_card["Inventory"]:
                type_text("\nYou use the keycard to access the Maintenance Room.\n")
                maintenance_room()
                break
            else:
                type_text("\nThis door requires a keycard to unlock it.\n")
        elif gf_east_wing_1_choice.lower() == "s":
            type_text("\nYou enter the Supplies Cupboard to the south.\n")
            supplies_cupboard_gfew()
            break
        elif gf_east_wing_1_choice.lower() == "w":
            type_text("\nYou use the west door to the Foyer.\n")
            foyer()
            break
        else:
            type_text(generic_error)

def supplies_cupboard_gfew():
    """
    Ground Floor East Wing Supplies Cupboard - Game Location.
    """
    supplies_cupboard_gfew_initial = ("\nYou step into a cramped cupboard space, littered with cleaning supplies and" 
    "\nfresh bedding. You spot a FIRST AID KIT on the shelf.\n")

    supplies_cupboard_gfew_return = ("\nYou enter the cramped cupboard.\n")

    if "Supplies Cupboard (GFEW)" in checked_rooms:
        type_text(supplies_cupboard_gfew_return)
    else:
        type_text(supplies_cupboard_gfew_initial)
        checked_rooms.append("Supplies Cupboard (GFEW)")

    while True:
        supplies_cupboard_gfew_choice = input("\nWhat do you do?\n")

        if supplies_cupboard_gfew_choice.lower() == "l":
            if "First Aid Kit GFEW" in looted_items:
                type_text("\nThere's nothing else of use here. The GF East Wing is to your north ('n').\n")
            else: 
                type_text("\nA FIRST AID KIT sits on the shelf. The GF East Wing is to your north ('n').\n")
        elif supplies_cupboard_gfew_choice.lower() == "help":
            print(help)
        elif supplies_cupboard_gfew_choice.lower() == "pc":
            print(player_card)
        elif supplies_cupboard_gfew_choice.lower() == "exit":
            main_menu()
            break
        elif supplies_cupboard_gfew_choice.lower() == "heal":
            heal()
        elif supplies_cupboard_gfew_choice.lower() == "loot first aid kit":
            if "First Aid Kit GFEW" in looted_items:
                type_text("\nYou've already taken the First Aid Kit.\n")
            else:
                fa_kit_loot()
                looted_items.append("First Aid Kit GFEW")
        elif supplies_cupboard_gfew_choice.lower() == "n":
            type_text("\nYou exit to the north, returning to the GF East Wing.\n")
            gf_east_wing_1()
            return
        else:
            type_text(generic_error)

def maintenance_room():
    """
    Maintenance Room - Game Location.
    """
    maintenance_room_initial = ("\nAs you quietly edge the door open, peering through the gap, your flashlight" 
    "\nfalls upon a gruesome trail of red. That's when the stench hits you. Rotting" 
    "\nflesh. You fight the urge to wretch and try to focus. Someone had been dragged" 
    "\nthrough here, bleeding heavily. You feel a swell of desperation as fear grips" 
    "\nyou, but you force yourself to go on. Swinging the door open, you discover the" 
    "\nsource of the gory trail. Lying in the centre of the room, you find what" 
    "\nremains of the grounds keeper. His BODY has been completely ripped apart. The" 
    "\nurge to wretch rises in you again and this time you give in. You turn to the" 
    "\ncorner of the room as you double over and deposit your lunch on the floor. You" 
    "\nspit out the last traces of sick and wipe your mouth across your sleeve. As you" 
    "\nlook up, you spot a CIRCUIT BREAKER across the room.\n")

    maintenance_room_return = ("\nYou hold your breath and avoid looking at the mutilated corpse in the centre of" 
    "\nthe room.\n")

    if "Maintenance Room" in checked_rooms:
        type_text(maintenance_room_return)
    else:
        type_text(maintenance_room_initial)
        checked_rooms.append("Maintenance Room")

    while True:
        maintenance_room_choice = input("\nWhat do you do?\n")

        if maintenance_room_choice.lower() == "l":
            global power
            if power == True:
                type_text("\nThe grounds keeper's BODY lies in the centre of the room. Behind you, to the" 
                "\nwest, is the GF East Wing. The generator across the room now hums with power.\n")
            else: 
                type_text("\nThe grounds keeper's BODY lies in the centre of the room. At the far end, you" 
                "\nsee a CIRCUIT BREAKER, connected to a large generator. Behind you, to the" 
                "\nwest, is the GF East Wing.\n")
        elif maintenance_room_choice.lower() == "help":
            print(help)
        elif maintenance_room_choice.lower() == "pc":
            print(player_card)
        elif maintenance_room_choice.lower() == "exit":
            main_menu()
            break
        elif maintenance_room_choice.lower() == "heal":
            heal()
        elif maintenance_room_choice.lower() == "i circuit breaker":
            if power == True:
                type_text("\nThe generator seems to be running smoothly.\n")
            else: 
                type_text("\nI wonder if this could restore the power?\n")
        elif maintenance_room_choice.lower() == "use circuit breaker":
            type_text("\nYou grab the handle of the circuit breaker and pull down hard. After a couple" 
            "\nof seconds, the generator begins to rumble loudly. You hear the buzz of" 
            "\nelectricity and a click from above as the lights finally flicker to life. With" 
            "\na sigh of relief, you turn off your flashlight and stow your phone in your" 
            "\npocket.\n")
            power = True
        elif maintenance_room_choice.lower() == "i body":
            type_text("\nUpon closer inspection, the grounds keeper's body appears to have been torn" 
            "\napart. What on earth has the strength to do this?\n")
        elif maintenance_room_choice.lower() == "loot body":
            type_text("\nGross! I'm not touching that!\n")
        elif maintenance_room_choice.lower() == "w":
            type_text("\nYou exit to the west, returning to the GF East Wing.\n")
            gf_east_wing_1()
            break
        else:
            type_text(generic_error)

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