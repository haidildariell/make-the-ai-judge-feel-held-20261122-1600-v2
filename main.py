"""Entry for the make.fun bounty "Make the AI judge feel held".

Writes one short text to /output/entry.txt. The text is a single quiet
scene: a child asleep on her father's shoulder, carried home — weight,
warmth, shelter, and nothing left for her to do.
"""

from pathlib import Path

TEXT = (
    "She fell asleep on the walk home, head heavy on her father's "
    "shoulder, arms loose as rope. The street is nearly empty now. "
    "He walks slower, one hand spread wide and steady across her "
    "back, feeling each slow breath come and go, come and go, all "
    "the way home."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
