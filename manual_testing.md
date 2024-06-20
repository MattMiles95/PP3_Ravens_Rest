## Manual Testing

Feature | Expected Outcome | Result
--- | --- | ---
ASCII Art | ASCII Art of a raven, the games title, the 'How to Play' banner and the 'Game Over' banner. | Pass
Type Text Function | Words are printed to the terminal one character at a time in random intervals between .001 and .06 seconds. | Pass
main_menu() | Takes Player to how_to_play() or character_selection(). Incorrect input by Player generates an message notifying the Player of the error, and prompting them to try again. | Pass
how_to_play() | Links Player to 'How to Play' section or 'Character Selection'. Incorrect input by Player generates an message notifying the Player of the error, and prompting them to try again. | Pass

## Bugs and Fixes

Feature | Expected Outcome | Actual Outcome | Fix
--- | --- | --- | ---
Characters being randomly generated | Hero and Villain appear within User and CPU cards | Cards remained blank | moved arrays that stored characters below respective variable declarations
