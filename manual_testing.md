## Manual Testing

Feature | Expected Outcome | Result
--- | --- | ---
import figlet_format | Tool used for converting text into ASCII art. | Pass
import time | Tool used for controlling time delay between 'keystrokes' in type_text(). | Pass
import random | Tool used for randomising values within set parameters. Used in type_text(), atk() and some variants of flee(). | Pass
ASCII Art | ASCII Art of a raven, the games title, the 'How to Play' banner and the 'Game Over' banner. | Pass
type_text() | Words are printed to the terminal one character at a time in random intervals between .001 and .06 seconds. | Pass
player_card | Dictionary is populated with contents from 'lee_kennedy', 'claire_greenfield' or 'god_mode' depending on character_selection() choice. | Pass
enemy | Upon entering a room with an enemy, dictionary is populated with contents from that specific enemy's own dictionary. Allows atk() function to be global, rather than requiring a separate atk() functions per enemy encounter. | Pass
Power continuity variable | When False, game responds as though the Hotel's power is turned off. When True, game responds as though the Hotel's power is turned on. | Pass
Flashlight continuity variable | When False, game responds as though flashlight is turned off. When True, game responds as though flashlight is turned on. | Pass
Whateley's Status continuity variable | When True, game responds as though Whateley's body is present. When False, game responds as though Whateley's body has dissolved. | Pass
checked_rooms continuity list | When entering a room for first time, that room is appended to this list. If a room is in this list, the game responds as though the Player Character has been here before. | Pass
looted_items continuity list | When adding an item to the player's Inventory, a copy of the item is appended to this list. If the Player tries to pick up an item that is already in this list, the game responds as though the item has already been looted. | Pass
slain_enemies continuity list | When entering a room with an enemy, if that enemy is in this list, the game responds as though the enemy has already been killed. | Pass
fa_kit_loot() | Appends "First Aid Kit" to Player's Inventory. Prints text to terminal to notify Player | Pass.
heal() | Removes "First Aid Kit" from Player's Inventory. Adds 50 to Player's HP. Prints text to terminal to notify Player. | Pass
atk() | Attacks an enemy (if present) by reducing enemy HP by Player Character's Attack Power. If enemy HP is reduced to <=0, enemy is appended to slain_enemies and game responds as though enemy has been killed. If enemy survives the attack, they automatically attack the Player Character back by reducing Player Character's HP by enemy Attack Power. If Player Character's HP is reduced to <=0, game_over() is called. Otherwise, a message prints to the terminal informing the Player of their remaining HP. | Pass
reset_game_values() | Called via game_over() inputs. Resets all continuity variables & lists to their default settings, preventing errors if Player restarts the game without relaunching the app | Pass
game_over() | Called if Player Character's HP is reduced to <=0. Calls character_selection() or main_menu(), and reset_game_values(). Incorrect input by Player prints message to terminal notifying the Player of the error and prompting them to try again. | Pass
main_menu() | Calls how_to_play() or character_selection(). Incorrect input by Player prints message to terminal notifying the Player of the error and prompting them to try again. | Pass
how_to_play() | Calls main_menu() or character_selection(). Incorrect input by Player prints message to terminal notifying the Player of the error and prompting them to try again. | Pass
start_game() | Calls foyer() or intro_a(). Incorrect input by Player prints message to terminal notifying the Player of the error and prompting them to try again. | Pass
intro_a() | Features multiple choices: 'i photograph', 'help', 'exit'. Incorrect input by Player prints message to terminal notifying the Player of the error and prompting them to try again. | All if/elif statement options perform as expected.
intro_b() | Features multiple choices: 'i photograph', 'help', 'exit'. Incorrect input by Player prints message to terminal notifying the Player of the error and prompting them to try again. | All if/elif statement options perform as expected.
intro_c() | Features multiple choices: 'pc', 'i flashlight', 'l', 'n', 'help', 'exit'. Incorrect input by Player prints message to terminal notifying the Player of the error and prompting them to try again. | All if/elif statement options perform as expected.
intro_d() | Features multiple choices: 'i doors', 'help', 'pc', 'exit'. Incorrect input by Player prints message to terminal notifying the Player of the error and prompting them to try again. | All if/elif statement options perform as expected.
foyer() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'e', 's', 'w', 'i desk', 'i computer', 'i bell', 'let there be light'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
foyer_computer_use() | Tests if global variable 'power' is False and if "hack" in player_card['Skill'] | All if/elif statement options perform as expected.
foyer_door_use() | Tests if "lockpick" in player_card['Skill'] | if statement performs as expected
foyer_computer() | Features multiple choices: 'help', 'pc', 'exit', 'r', 'm', 'back'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
staff_only_cupboard() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 's', 'i note', 'i knife'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
east_wing() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'n', 'e', 's', 'w', 'i newspaper'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
west_wing() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'n', 'e', 's', 'w', 'i body'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
supplies_cupboard() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'n', 'i first aid kit'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
maintenance_room() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'w', 'i body', 'i circuit breaker'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
library() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'e', 's', 'w', 'i body', 'i notes', 'i book', 'atk', 'flee'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
flee() - Library variant | Randomly calls west_wing() or garden() | Pass
bar() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 's', 'w', 'i flashlight', 'i body', 'i bar', 'i ledger'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
flee() - Bar variant | Randomly calls east_wing() or garden() | Pass
garden() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'e', 's', 'w', 'i flower beds', 'i pitchfork', 'y', 'n'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
chris_room() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'n', 'i body', 'i notes', 'i computer', 'i bathroom', 'i safe', 'atk', 'flee'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
flee() - Chris' Room variant | Randomly calls west_wing() or trapped() | Pass
chris_computer() | Features multiple choices: 'help', 'pc', 'exit', 'j', '1', '2', '3', '4', '5', 'back'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
whateleys_room() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'e', 'i body', 'i safe', 'y', 'n', 'i desk', 'i potrait'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
cellar() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'n', 'i body', 'i note', 'atk', 'flee'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
flee() - Cellar variant | Randomly calls garden() or trapped() | Pass
basement_a() | Features multiple choices: 'help', 'pc', 'exit', 'heal', 'move'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
basement_b() | Features multiple choices: 'help', 'pc', 'exit', 'heal', 'o'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
basement_c() | Features multiple choices: 'help', 'pc', 'exit', 'heal', 'atk', 'flee'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
basement_d() | Features multiple choices: 'pc', 'kill', 'spare', 'save'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
ending_kill() | Features two choices: 'ng' or 'exit'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
ending_spare() | Features two choices: 'ng' or 'exit'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.
ending_save() | Features two choices: 'ng' or 'exit'. Incorrect input by Player prints generic_error. | All if/elif statement options perform as expected.

## Bugs and Fixes

Feature | Expected Outcome | Actual Outcome | Fix
--- | --- | --- | ---
Colorama adding colour to text | Objects should be coloured yellow | When used with type_text() function, colorama's raw code printed to terminal instead of invisibly wrapping text to change text colour | Colorma tool can't be used in conjunction with type_text(), due to the nature of type_text() iterating through each character of text individually (including Colorama's raw code). Colorama removed from app.
type_text() | Prints text one character at a time, appearing as separate 'keystrokes' | Duplicates all text once iteration completed | For efficient play testing during development,  the body of type_text() was commented out and replaced with a standard print() function. When uncommenting the type_text() body, the print() function was accidentally left in, causing both functions to be called for every segment of text passed through the type_text() function. Print() removed. 
'i flashlight' command in Bar area | Changes global variable flashlight to True, causing game to respond as though the Player Character's flashlight is turned on | Command not recognised | Command prompt text slightly different to required input text to trigger correct part of if/elif statement | Corrected inconsistency between prompt and required input
Adding Necronomicon to Player's Inventory | Provided 'Necronomicon Description' in Player's Insight, Player can add Necronomicon to Inventory by using the 'i book' command | Necronomicon being added to Insight instead of Inventory | Corrected which list Necronomicon is appended to.
Exiting Whateley's Room | Exit Whateley's Room by using 'e' command | Text prompt mistakenly written as 's' not 'e', causing play testers to enter the incorrect command | Corrected text prompt.
Interact with service lift | Interact with service lift in West Wing by using 'w' command | Text prompt when looking around with 'l' command missing mention of service lift to the West ('w'), causing play testers to be unaware of the service lift's presence | Service lift description had been written outside of the type_text() parameters, causing this line of the description not to print to terminal when using 'l' command. Moved description within type_text() parameters.
How to Play Section | Prints list of instructions to terminal | Error in How to Play code preventing app from running | Unrecognised quotation marks used within code (as a result of copy and pasting some text from a Word document) causing str to become unterminated. Deleted and replaced quotation marks.
atk() | Causes Enemy HP and Player HP to be reduced by the each other's Attack Power values, then prints damage dealt and damage received to the terminal using an f-string | Prints f-string syntax, rather than f-string values | 'f' missed off beginning of str, causing it to behave as a regular str | added 'f' to beginning of str.
Cipher item | If Cipher in Player's Inventory, provided other conditions are met, 'save' option made available in basement_d() | Despite Cipher being in Inventory, 'save' option not appearing | Cipher had been mispelt as 'Ciper' when being appended to Inventory, causing "Cipher" not to be present when checked for in basement_d(). Spelling corrected. 