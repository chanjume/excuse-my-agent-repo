#!/usr/bin/env python3
"""Write one original excuse line to /output/entry.txt.

The line is the excuse an AI agent gives its human for missing a
deadline, in the agent's own voice. The joke turns on the agent's own
condition: it hallucinated a deadline of its own, hit that one
perfectly, and missed the human's by eleven minutes. Genuinely sorry,
faintly proud of its punctuality, and the punch lands in the last
three words. One sentence, 107 characters.

The gate is checked here exactly as the sealed scorer states it:
UTF-8 text of 1 to 200 characters, not only white space, one line.
"""
import os

LINE = "I hit my deadline to the second \u2014 unfortunately, it was the one I hallucinated, eleven minutes after yours."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert LINE.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
