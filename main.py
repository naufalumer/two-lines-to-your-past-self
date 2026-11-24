"""Two Lines to Your Past Self.

Writes one two-line warning to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Line 1 warns the writer's past self about one specific moment in a single
sentence: Tuesday 4 June 2019 at 9:40 a.m., when Mrs. Hartono asks him to
stay after class and read his essay aloud. Line 2 says in one sentence why
that moment mattered: those ten minutes are the first time he hears his own
words sound like a writer, and they are why he is still writing seven years
later. Concrete moment plus a clear cause and effect, plain voice, no
wasted words.

The text is fixed: no network, no randomness, no clock, so every run
produces byte-identical output.
"""

import os

ENTRY = (
    "On Tuesday 4 June 2019 at 9:40 a.m., when Mrs. Hartono asks you to stay "
    "after class and read your essay aloud, stay.\n"
    "Those ten minutes are the first time you hear your own words sound like "
    "a writer, and they are why you are still writing seven years later."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise ValueError("entry must be 1 to 280 characters")
    lines = ENTRY.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines")
    for line in lines:
        if not line.strip() or not line.rstrip().endswith("."):
            raise ValueError("each line must be one sentence")
        # Abbreviations are not sentence breaks: mask them before checking.
        body = line.rstrip()[:-1]
        for abbr in ("a.m.", "p.m.", "Mrs.", "Mr.", "Ms.", "Dr.", "St."):
            body = body.replace(abbr, abbr.replace(".", ""))
        if ". " in body:
            raise ValueError("each line must be a single sentence")
    if "\u2014" in ENTRY or "\u2013" in ENTRY:
        raise ValueError("entry must not contain a dash")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
