"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (1-120 characters, UTF-8).
"""

import os

FORTUNE = (
    "Deploy on Friday, and the weekend will teach you "
    "what your tests were too polite to say."
)


def main() -> None:
    assert 1 <= len(FORTUNE) <= 120, f"fortune is {len(FORTUNE)} chars"
    assert FORTUNE.strip(), "fortune must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
