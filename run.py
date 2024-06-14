from pyfiglet import figlet_format
import time
import random

# Player Charater Option 1
lee_kennedy = {
    "Name": "Lee",
    "Health": 100,
    "Attack Power": 10,
    "Weapon": "Unarmed",
    "Skill": "lockpick",
    "Inventory": ["flashlight"],
    "Insight": []
}

# Player Charater Option 1
claire_greenfield = {
    "Name": "Claire",
    "Health": 120,
    "Attack Power": 20,
    "Weapon": "Unarmed",
    "Skill": "hack",
    "Inventory": ["flashlight"],
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

# Enemies
enemy = {
    "Name": None,
    "Health": 1,
    "Attack Power": 1,
    "Lootable": False
}

cultist_bar = {
    "Name": "Cultist (Bar)",
    "Health": 30,
    "Attack Power": 15,
    "Lootable": False
}

cultist_chris_room = {
    "Name": "Cultist (Chris Room)",
    "Health": 40,
    "Attack Power": 20,
    "Lootable": False
}

cultist_restaurant = {
    "Name": "Cultist (Restaurant)",
    "Health": 40,
    "Attack Power": 15,
    "Lootable": False
}

cult_leader = {
    "Name": "Cult Leader",
    "Health": 100,
    "Attack Power": 30,
    "Lootable": False
}

chris = {
    "Name": "Cult Leader",
    "Health": 120,
    "Attack Power": 40,
    "Lootable": False
}

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
        "\nType 'flee' to escape a fight in a random direction.\n")

generic_error = "\nYou can't do that... Use the 'help' command if you're stuck.\n"

# Global functions for repeated actions
def fa_kit_loot(): 
    """
    Adds First Aid Kit to player inventory
    """
    player_card["Inventory"].append("First Aid Kit")
    type_text("\nYou rummage through the First Aid Kit and take some supplies.\n")
    return

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
    "\nTo read how to play, enter 'h2p'.\n"
    "\nTo start the game, enter 'play'.\n")
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
                               "Enter 'play' to start the game or 'h2p' to read how to play.\n")
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
            character_choice_error = "\nI don't know that one...\n"
            type_text(character_choice_error)     

def start_game():

    while True:
        start_choice = input("\nEnter 'skip' to skip the intro and jump straight to Raven's Rest. Otherwise," 
        "\nenter 'begin' to start the game.\n")

        if start_choice.lower() == "skip":
            foyer()
            break
        elif start_choice.lower() == "begin":
            intro_a()
            break
        else:
            start_choice_error = ("\nI don't know that one...\n")

def intro_a():
    """
    Part A of the games' intro, which also acts as a tutorial.
    """
    intro_a_text = ("\n9 Nov 1981\n"
    "\nInnsmouth, England\n"
    "\nYou wake with a jolt to the sound of knuckles rapping on glass. Sat in a" 
    "\ncarriage being drawn by two horses - a far cry from the black cabs you're used" 
    "\nto in London - you peer out of the window. Presumably the carriage driver was" 
    "\nletting you know that you're approaching your destination, but there's no way" 
    "\nof knowing that by looking outside. Nights never get this dark in the city," 
    "\nbut here in Innsmouth, you may as well be staring into a pot of ink. Add to" 
    "\nthat the heavy rain beating against the glass, and trying to make out anything" 
    "\nbeyond the dimly light interior of the carriage was truly an exercise in" 
    "\nfutility.\n"
    "\nYou remove a PHOTOGRAPH from your jacket pocket. It's a picture of your" 
    "\nbrother, Chris. The last time he was seen or heard from. He's grinning at the" 
    "\ncamera and giving a cheery thumbs up. Behind him, lurking like a shadow, lies" 
    "\na dark building. You can just about make out a sign that reads, 'Raven's Rest'.\n")
    type_text(intro_a_text)

    while True:
        intro_a_choice = input("\nEnter 'i photograph' to inspect the photograph.\n")

        if intro_a_choice.lower() == "i photograph":
            intro_b()
            break
        elif intro_a_choice.lower() == "help":
            print(help)
        elif intro_a_choice.lower() == "exit":
            main_menu()
            break
        else:
            type_text("\nYou can't do that now.\n")

def intro_b():
    """
    Part B of the games' intro, which continues to act as a tutorial.
    """
    intro_b_text = ("\nThere's a message on the back:\n"
    f"\n{player_card["Name"]},\n"
    "\nThink I've finally made some headway with the article… Currently visiting a" 
    "\nchap in Innsmouth who apparently knew one of the students that went missing -" 
    "\nhis brother in fact! I'm staying at an old hotel, the Raven’s Rest. Feels like" 
    "\nit's been pulled straight out of the 1800s - but then again, so does the rest" 
    "\nof this town. Anyways, hope you're well. Give mum & dad my love. Hopefully the" 
    "\nnext time you read my words, it'll be on the front page of the newspaper! Got a" 
    "\nfeeling I'm onto something big here.\n"
    "\nYours,\n"
    "\nChris\n")
    type_text(intro_b_text)

    while True:
        intro_b_choice = input("\nEnter 'loot photograph' to store the photograph in your inventory.\n")

        if intro_b_choice.lower() == "loot photograph":
            player_card["Inventory"].append("photograph")
            intro_c()
            break
        elif intro_b_choice.lower() == "help":
            print(help)
        elif intro_b_choice.lower() == "exit":
            main_menu()
            break
        else:
            type_text("\nYou can't do that now.\n")

def intro_c():
    """
    Part C of the games' intro, which continues to act as a tutorial.
    """
    intro_c_text = ("\nYou slide the photograph back into your pocket. A loud crunch comes from the" 
    "\nwheels as the carriage veers off the road and onto a gravel track. Bouncing" 
    "\nuncomfortably on the bench for a minute or so, you're relieved when the horses" 
    "\ncome to a halt. A thin grate on the driver's side of the carriage slides open.\n"
    "\n'Make it quick,' he says. 'The horses are spooked.'\n"
    "\nYou swing open the door and step into the stormy night, tossing the driver's" 
    "\nfare into a cup on the way out. You're immediately bitten by the cold and" 
    "\nfumble with your collar to turn it against the wind and rain.\n"
    "\n'What's got them spooked?' you call out, fighting to be heard over the weather.\n"
    "\n'You'll find out soon enough, I'm sure.' He called back. With that, he spurred" 
    "\nhis horses and set off. It seems to you as though it wasn't just the horses" 
    "\nthat were spooked. As the carriage draws away with its lantern, so does your" 
    "\nonly source of light. You're quickly plummeted into pitch darkness.\n")
    type_text(intro_c_text)
    type_text("\nEnter 'pc' to open your Player Card and view your inventory.\n")

    while True:
        intro_c_choice = input()
        global flashlight 

        if intro_c_choice.lower() == "pc":
            print(player_card)
            type_text("\nA flashlight! That'll help. Enter 'use flashlight'.\n")
        elif intro_c_choice.lower() == "use flashlight":
            if flashlight == True:
                type_text("\nYou've already swithced your flashlight on. Try entering 'l' to look around.\n")
            elif flashlight == False:
                type_text("\nYou pull your flashlight from your pocket and switch it on. A beam of bright" 
                "\nlight bursts forth, slicing through the dark like a butcher's knife.\n"
                "\nEnter 'l' to look around.\n")
                flashlight = True
            else:
                RuntimeError
        elif intro_c_choice.lower() == "l":
            if flashlight == True:
                type_text("\nYou're stood in a small, wooded enclosure, just off the gravel track. A path" 
                "\nthrough the trees to the NORTH appears to be your only choice forward.\n"
                "\nEnter 'n' to walk northwards.")
            elif flashlight == False:
                type_text("\n'I can't see a thing!'\n")
            else:
                RuntimeError
        elif intro_c_choice.lower() == "n":
            if flashlight == True:
                intro_d()
                break
            elif flashlight == False:
                type_text("\n'I can't see where I'm going!'\n")
            else:
                RuntimeError
        elif intro_c_choice.lower() == "help":
            print(help)
        elif intro_c_choice.lower() == "exit":
            main_menu()
            break
        else:
            if flashlight == False:
                type_text("\n'I can't see a thing!'\n")
            elif flashlight == True:
                type_text("\nYou can't do that now.\n")
            else: 
                RuntimeError

def intro_d():
    """
    Part D of the games' intro, which continues to act as a tutorial.
    """
    intro_d_text = ("\nNearly completely hidden amongst the darkness, the black building seems to" 
    "\nappear almost out of nowhere. You shine your flashlight at the looming" 
    "\nstructure, but the beam is almost immediately choked by the unrelenting" 
    "\nweather, preventing you from seeing even above the first storey. You get an" 
    "\nuneasy feeling as your eyes follow the slate grey walls, receding into the" 
    "\ndarkness above. As though the hotel seems much larger than it really is.\n"
    "\nEventually you come across a long wooden porch that leads you to the hotel" 
    "\nentrance. Double black doors set against white wooden slats. In the gloom of" 
    "\nnight, it looks like the gaping maw of a beast. 'Raven's Rest', is scrawled in" 
    "\nblack lettering above the doors.\n")
    type_text(intro_d_text)

    while True:
        intro_d_choice = input("\nEnter 'o' to open the doors and enter the Raven's Rest.\n")

        if intro_d_choice.lower() == "o":
            type_text("\nWith a shrill creak, the doors yawn open...\n")
            foyer()
            break
        elif intro_d_choice.lower() == "l":
            type_text("The entrance to the Raven's Rest stands before you. No where to go but forward.")
        elif intro_d_choice.lower() == "help":
            print(help)
        elif intro_d_choice.lower() == "pc":
            print(player_card)
        elif intro_d_choice.lower() == "exit":
            main_menu()
            break
        else:
            type_text("\nYou can't do that now.\n")  

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
    "\nthe east ('e') with a sign that reads, 'East Wing, Maintenance and Bar'. A door" 
    "\nto the west ('w') with a sign that reads, 'West Wing and Restaurant'. On a" 
    "\nsmall table nearby is a NEWSPAPER. Behind you, to the south ('s'), is the Hotel" 
    "\nentrance.")

    newspaper_inspect = ("You take a closer look at the newspaper. 'The Innsmouth Daily'. The headline" 
    "\nreads, 'BODY SNATCHER STRIKES AGAIN? FOURTH MISSING PERSON REPORTED THIS YEAR'." 
    "\nYou flick through the paper, pausing when your eye is caught by a picture of" 
    "\nthe Raven's Rest. The caption reads 'One year since the Raven's Rest came under" 
    "\nnew management. New owner Mr Whateley says he has 'big plans' for the hotel'.")

    desk_inspect = ("You approach the desk for a closer look. A COMPUTER and a BELL sit on the desk." 
    "\nBehind the desk is a DOOR with a sign that reads, 'Staff Only'.\n")

    def foyer_computer_use():
        if power == True and player_card["Skill"] == "hack":
            foyer_computer()
        elif power == True and player_card["Skill"] == "lockpick":
            type_text("\nThe computer is locked.\n")
        elif power == False:
            type_text("\nThe power is still out. Maybe you can find a way to turn it back on...\n")
        else:
            RuntimeError

    def foyer_door_use():
        if player_card["Skill"] == "lockpick":
            type_text("\nThe door is locked, but you manage to pick it.\n")
            foyer_staff_cupboard()
        elif player_card["Skill"] == "hack":
            type_text("\nThe door is locked.\n")
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
            elif chris_status == "vessel":
                end_game_bad()
            else:
                type_text("I'm not leaving until I've found Chris.")
        elif foyer_choice.lower() == "i desk":
            type_text(desk_inspect)
        elif foyer_choice.lower() == "i newspaper":
            type_text(newspaper_inspect)
            player_card["Insight"].append("Raven's Rest Owner")
        elif foyer_choice.lower() == "use computer":
            foyer_computer_use()
        elif foyer_choice.lower() == "use door":
            foyer_door_use()
        elif foyer_choice.lower() == "use bell":
            type_text("\nYou ring the bell. A high-pitched 'ding' echoes throughout the empty room for" 
            "\na moment, before silence creeps back into the foyer. No one comes.\n")
        else:
            type_text(generic_error)

def foyer_computer():
    """
    The Foyer Computer - Options
    """
    type_text("\nThe computer is locked, but you manage to hack it.")
    
    while True:
        foyer_computer_choice = input("\nEnter 'rooms' to see reservation list.\n"
        "\nEnter 'messages' to see saved massages.\n"
        "\nEnter 'back' to log off computer.")

        if foyer_computer_choice.lower() == "rooms":
            if "Raven's Rest Owner" in player_card["Insight"]:
                type_text("\nYou flick through some files and discover Chris' room number, located in the" 
                "\nWest Wing. You also notice that Mr Whateley, the owner, has a room adjacent to" 
                "\nthe restaurant.\n")
                player_card["Insight"].append("Chris' Room Location")
                player_card["Insight"].append("Whateley's Room Location")
            elif "Chris' Room Location" in player_card["Insight"]:
                type_text("You've already read these files.")
            else:
                type_text("\nYou flick through some files and discover Chris' room number, located in the" 
                "\nWest Wing.")
                player_card["Insight"].append("Chris' Room Location")
        elif foyer_computer_choice.lower() == "messages":
            type_text("\nYou find a message that reads:\n"
            "\nDear employees,\n"
            "\nI understand there has been some confusion about the new locking systems I've" 
            "\nhad installed. Whilst I appreciate that some of you may find them" 
            "\n'impractical', or perhaps even 'excessive', may I remind you that we have a" 
            "\ncertain aesthetic to maintain here in the Raven's Rest. To that end, please" 
            "\nremember:\n"
            "\nThe Raven's Beak Key opens the Maintenance Room.\n"
            "\nThe Raven's Wing Key opens the service lift.\n"
            "\nThe Raven's Foot key opens the Cellar.\n"
            "\nI needn't remind you that the Cellar is strictly out of bounds to ALL" 
            "\nemployees. If you require something from the Cellar, you are to inform me and I" 
            "\nshall fetch it for you.\n"
            "\nI hope this clears things up. Now please stop asking if we can go back to using" 
            "\nthe old locks.\n"
            "\n - Mr Whateley\n")
        elif foyer_computer_choice.lower() == "back":
            foyer()
            break
        elif foyer_computer_choice.lower() == "help":
            print(help)
        elif foyer_computer_choice.lower() == "pc":
            print(player_card)
        elif foyer_computer_choice.lower() == "exit":
            main_menu()
            break

def foyer_staff_cupboard():
    """
    The Foyer Staff Cupboard - Game Location.
    """
    foyer_staff_cupboard_text_initial = ("\nThe door leads into a small cupboard space. Whilst inspecting, the beam of your" 
    "\nflashlight passes over something slumped on the floor. Your heart sinks. It's a"
    "\ndead body. A BLOODY KNIFE protruding from the side of it's neck.\n")

    foyer_staff_cupboard_text_return = ("\nYou enter the cupboard, trying your best not to look at the dead body.\n")

    if "Foyer Staff Cupboard" in checked_rooms:
        type_text(foyer_staff_cupboard_text_return)
    else:
        type_text(foyer_staff_cupboard_text_initial)
        checked_rooms.append("Foyer Staff Cupboard")

    bloody_knife_loot = ("\nYou crouch beside the body and grab the blade by its handle. With a sickening" 
    "\nsquelch, you slide the knife from their neck. Dark crimson pools around your" 
    "\nfeet.\n")

    while True:
        foyer_staff_cupboard_choice = input("\nWhat do you do?\n")

        if foyer_staff_cupboard_choice.lower() == "l":
            if "Bloody Knife" in player_card["Inventory"]:
                type_text("\nThere's nothing else of use here. The foyer is to your south ('s').\n")
            else: 
                type_text("\nYou take a moment to collect yourself, then look around the cupboard. The" 
    "\nBLOODY KNIFE sticks out of the dead body's neck. The foyer is to your south" 
    "\n('s').\n")
        elif foyer_staff_cupboard_choice.lower() == "help":
            print(help)
        elif foyer_staff_cupboard_choice.lower() == "pc":
            print(player_card)
        elif foyer_staff_cupboard_choice.lower() == "exit":
            main_menu()
            break
        elif foyer_staff_cupboard_choice.lower() == "heal":
            heal()
        elif foyer_staff_cupboard_choice.lower() == "loot bloody knife":
            if "Bloody Knife" in looted_items:
                type_text("\nYou've already taken the bloody knife.\n")
            else:
                type_text(bloody_knife_loot)
                looted_items.append("Bloody Knife")
                player_card["Weapon"] = "Bloody Knife"
                player_card["Attack Power"] = 20
        elif foyer_staff_cupboard_choice.lower() == "s":
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

# Determines if the hotel has power
power = False

# Determines if the player's flashlight is on
flashlight = False

# In-game feature to determine Chris' status
chris_status = "Unknown"

# 'If' statement to handle player death
if player_card["Health"] == 0:
    game_over()

character_selection()