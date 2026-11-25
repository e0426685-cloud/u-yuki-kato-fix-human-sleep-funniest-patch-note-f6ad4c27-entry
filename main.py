"""Fix Human Sleep: funniest patch note entry.

Writes a single-line patch note announcing that human sleep is fixed
to /output/entry.txt. The note must be 1-160 UTF-8 characters, one line.
"""

import os

ENTRY_TEXT = (
    "Fixed: humans now fall asleep in 8 seconds. "
    "Known issue: dreams still ship untested, "
    "and 3 a.m. dread is now a paid add-on."
)

MAX_CHARS = 160


def validate_entry(text):
    """Check one patch-note line against the competition gate.

    The gate requires UTF-8 text of 1 to 160 characters, a single line,
    and not only white space. Returns the cleaned line, or raises
    AssertionError naming the violated rule.
    """
    cleaned = text.strip()
    assert cleaned, "entry text must not be empty"
    assert "\n" not in cleaned, "entry must be a single line"
    assert len(cleaned) <= MAX_CHARS, (
        "entry is %d chars, over the %d cap" % (len(cleaned), MAX_CHARS)
    )
    return cleaned


def main():
    text = validate_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)
    print("wrote %s (%d chars)" % (path, len(text)))


if __name__ == "__main__":
    main()
