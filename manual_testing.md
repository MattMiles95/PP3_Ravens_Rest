## Manual Testing

Feature | Expected Outcome | Result
--- | --- | ---
ASCII Art | ASCII Art of a raven, the games title, the 'How to Play' banner and the 'Game Over' banner. | Pass
type_text() | Words are printed to the terminal one character at a time in random intervals between .001 and .06 seconds. | Pass
main_menu() | Calls how_to_play() or character_selection(). Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
how_to_play() | Calls main_menu() or character_selection(). Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
start_game() | Calls foyer() or intro_a(). Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
intro_a() | Features multiple choices: 'i photograph', 'help', 'exit'. Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | All if/elif statement options perform as expected
intro_b() | Features multiple choices: 'i photograph', 'help', 'exit'. Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | All if/elif statement options perform as expected
intro_c() | Features multiple choices: 'pc', 'i flashlight', 'l', 'n', 'help', 'exit'. Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | All if/elif statement options perform as expected
intro_d() | Features multiple choices: 'i doors', 'help', 'pc', 'exit'. Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | All if/elif statement options perform as expected
foyer() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'e', 's', 'w', 'i desk', 'i computer', 'i bell', 'let there be light'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
foyer_computer_use() | Tests if global variable 'power' is False and if "hack" in player_card['Skill'] | All if/elif statement options perform as expected
foyer_door_use() | Tests if "lockpick" in player_card['Skill'] | if statement performs as expected
foyer_computer() | Features multiple choices: 'r', 'm', 'back'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
staff_only_cupboard() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 's', 'i note', 'i knife'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
east_wing() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'n', 'e', 's', 'w', 'i newspaper'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
west_wing() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'n', 'e', 's', 'w', 'i body'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
supplies_cupboard() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'n', 'i first aid kit'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
maintenance_room() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'w', 'i body', 'i circuit breaker'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
library() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'e', 's', 'w', 'i body', 'i notes', 'i book', 'atk', 'flee'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
flee() - Library variant | Randomly calls west_wing() or garden() | Pass
 bar() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 's', 'w', 'i flashlight', 'i body', 'i bar', 'i ledger'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
 flee() - Bar variant | Randomly calls east_wing() or garden() | Pass
 garden() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'e', 's', 'w', 'i flower beds', 'i pitchfork', 'y', 'n'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected
 chris_room() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'n', 'i body', 'i notes', 'i computer', 'i bathroom', 'i safe', 'atk', 'flee'. Incorrect input by Player generates a generic error message with useful hints. | All if/elif statement options perform as expected

## Bugs and Fixes

Feature | Expected Outcome | Actual Outcome | Fix
--- | --- | --- | ---
Characters being randomly generated | Hero and Villain appear within User and CPU cards | Cards remained blank | moved arrays that stored characters below respective variable declarations
