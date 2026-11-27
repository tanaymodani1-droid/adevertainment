# Advertainment · Round 2 game (v17)

Live: https://advertainment1.vercel.app

- `index.html`: the game (team laptops). `admin.html`: OC control panel.
- `src/`: page source. Build with `python3 make.py .` inside `src/`.
- `data/`: the 27-brand data (`pairs44.json`), the scripts that build it, and `audit.py`, which checks every brand.
- `case-study/`: the case-study round site.
- `pdf-lib.js`: used by the game to export decks.

## How the round works
1. **Lock 1:** unscramble the launch city (2 or 3 fake letters are mixed in).
2. **Lock 2:** pick the one persona out of 12 who fits all 6 evidence clues (A to F). A wrong pick jams the lock for 2 minutes.
3. **Vault:** 5 dials, each a two-step question on clues #27 to #30. The code is the same for every team (see the OC panel).

The answer key is on the OC panel (admin.html), so it is not repeated here.
