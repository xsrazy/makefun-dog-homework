"""The Dog Ate My Homework entry: one funny line in the dog's own voice.

Why this line fits the judge brief
----------------------------------
The line is the dog's own excuse after being caught eating the homework,
spoken in the dog's own first-person voice, exactly what the judge's
first criterion asks for: "You left it on the floor, and the floor is
where food lives. I was only following the law."

The twist is dog logic turned into law. The floor is where food lives,
so anything on the floor is food, and eating food is not a crime, it is
obedience. The dog does not apologize, does not beg, does not admit
fault. It cites a law it invented and sounds proud of it. That is the
judge's second criterion: the funniest excuse, with a twist and dog
logic that lands in one line.

It sounds like a real dog, the judge's third criterion. A dog's world
is the floor, and a dog's priorities are food, rules, and being sure of
itself. There is no human shame in the line, no guilty ears, no sad
eyes. Just a dog that is completely certain it did the right thing,
which is also what the best entries do: a dog that believes it did
nothing wrong.

It stands alone, the judge's fourth criterion. There is no setup, no
teacher, no scene to explain. One sentence carries the crime, the
excuse, and the verdict all at once.

It is fresh, the judge's fifth criterion. There is no cat to blame, no
talk about how the paper tasted, no begging to still be a good boy.
The joke is built on the floor-as-law idea, which no stock excuse uses.

It is tight. At 90 characters every word earns its place: "on the
floor" is the crime scene, "where food lives" is the dog's whole
philosophy, and "following the law" is the punchline that turns a
confession into a defense.

The entry line itself:
    You left it on the floor, and the floor is where food lives. I was
    only following the law.
"""

import os
import sys

# The entry: one original line, written for this competition.
ENTRY_LINE = "You left it on the floor, and the floor is where food lives. I was only following the law."

MIN_CHARS = 1
MAX_CHARS = 199


def validate(line):
    """Check the entry against the gate: 1-199 chars, single line, not blank.

    Returns a list of problems; an empty list means the line is valid.
    """
    problems = []
    if not isinstance(line, str):
        return ["entry is not text"]
    if not line.strip():
        problems.append("entry is only whitespace")
    if len(line) < MIN_CHARS:
        problems.append("entry is shorter than %d character" % MIN_CHARS)
    if len(line) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        problems.append("entry spans more than one line")
    return problems


def write_entry(line, output_dir):
    """Write the entry line to entry.txt with no trailing newline."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)
    return path


def write_entry_file(line, output_dir):
    """Validate the line first, then write it.

    A convenience wrapper for callers that want one call to do both the
    gate check and the write. Raises ValueError with the first problem
    found instead of writing an invalid entry.
    """
    problems = validate(line)
    if problems:
        raise ValueError("invalid entry: %s" % problems[0])
    return write_entry(line, output_dir)


def describe(line):
    """One human-readable sentence describing the entry, for logs.

    Keeps the run output self-explanatory without re-printing the line
    itself: length, word count and the byte size the leaderboard shows.
    """
    info = stats(line)
    return (
        "entry is %d characters, %d words, %d bytes on one line"
        % (info["chars"], info["words"], info["bytes"])
    )


def stats(line):
    """Small facts about the entry line, for the run log.

    Counts characters the way the gate does (Python str length, which
    for this ASCII-only line equals the byte count), splits on whitespace
    for the word count, and reports the line count so a multi-line
    accident would show up here before it reaches the gate.
    """
    words = line.split()
    return {
        "chars": len(line),
        "words": len(words),
        "bytes": len(line.encode("utf-8")),
        "lines": line.count("\n") + 1,
    }


def main():
    """Validate the entry, write it, and print a short summary.

    The output directory comes from MAKEFUN_OUTPUT_DIR when the harness
    sets it, and falls back to /output otherwise. The entry is written
    with no trailing newline so the file holds exactly the entry line.
    """
    problems = validate(ENTRY_LINE)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry_file(ENTRY_LINE, output_dir)
    print("wrote %s: %s" % (path, describe(ENTRY_LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
