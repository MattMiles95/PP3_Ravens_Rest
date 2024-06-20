## Manual Testing

Feature | Expected Outcome | Result
--- | --- | ---
ASCII Art | ASCII Art of a raven, the games title, the 'How to Play' banner and the 'Game Over' banner. | Pass
type_text() | Words are printed to the terminal one character at a time in random intervals between .001 and .06 seconds. | Pass
main_menu() | Takes Player to how_to_play() or character_selection(). Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
how_to_play() | Takes Player to main_menu() or character_selection(). Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
start_game() | Takes Player to foyer() or intro_a(). Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
intro_a() | Features multiple choices: 'i photograph', 'help', 'exit'. Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
intro_b() | Features multiple choices: 'i photograph', 'help', 'exit'. Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
intro_c() | Features multiple choices: 'pc', 'i flashlight', 'l', 'n', 'help', 'exit'. Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
intro_d() | Features multiple choices: 'i doors', 'help', 'pc', 'exit'. Incorrect input by Player generates an message notifying the Player of the error and prompting them to try again. | Pass
foyer() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'e', 'w', 's', 'i desk', 'i computer', 'i bell', 'let there be light'. Incorrect input by Player generates a generic error message with useful hints. | Pass
staff_only_cupboard() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 's', 'i note', 'i knife'. Incorrect input by Player generates a generic error message with useful hints. | Pass
east_wing() | Features multiple choices: 'l', 'help', 'pc', 'exit', 'heal', 'e', 'w', 's', 'i newspaper', 'i computer', 'i bell', 'let there be light'. Incorrect input by Player generates a generic error message with useful hints. | Pass

## Bugs and Fixes

Feature | Expected Outcome | Actual Outcome | Fix
--- | --- | --- | ---
Characters being randomly generated | Hero and Villain appear within User and CPU cards | Cards remained blank | moved arrays that stored characters below respective variable declarations
