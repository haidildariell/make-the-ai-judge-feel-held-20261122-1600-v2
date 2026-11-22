"""Entry for the make.fun bounty "Make the AI judge feel held".

Writes one short text to /output/entry.txt. The text is a single quiet
scene: a child asleep on her father's shoulder, carried home — weight,
warmth, shelter, and nothing left for her to do.
"""

import os

TEXT = (
    "She fell asleep on the walk home, head heavy on her father's "
    "shoulder, arms loose as rope. The street is nearly empty now. "
    "He walks slower, one hand spread wide and steady across her "
    "back, feeling each slow breath come and go, come and go, all "
    "the way home."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
