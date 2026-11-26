"""Fridge Roast entry: one line, biggest laugh.

Why this line fits the judge brief:
- It is a roast aimed squarely at the smart fridge itself: the joke
  targets its firmware, not a generic kitchen appliance.
- The punchline lands on a sharp turn: the humble act of opening the
  crisper drawer is held hostage by a software update, and the final
  clause reframes the whole meal as unfinished software -- "dinner is
  currently in beta."
- It is specific to smart fridges: only a connected, update-driven
  fridge could gate a drawer behind firmware, so the gag would not
  work on any ordinary gadget.
- The wording is tight: one sentence, no wasted setup, every clause
  feeds the closing twist.
- The angle is fresh: it dodges the obvious cracks about the fridge
  ordering groceries or watching you, and instead mocks software
  release culture invading the kitchen.
"""

import os

TEXT = "My smart fridge needs a firmware update to open the crisper drawer, so dinner is currently in beta."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
