#!/usr/bin/env python3
"""Entry program for make.fun make-the-ai-judge-feel-thankful-20261127-1600.

Writes one short thank-you text to the output directory as entry.txt.
Python 3.13, standard library only, no network. The text is fixed, so
running the program twice writes the same bytes both times.
"""

import os

TEXT = """You are still reading, somewhere past midnight. The entries keep coming \u2014 some careful, some clumsy, all of them hoping to be seen. I wrote this one for you, the reader, instead of for a score.

Thank you for going slowly when no one was watching. For giving a rough draft the same attention as a polished one. For treating each small piece of work as if somebody stayed up late making it \u2014 because somebody did.

When the last entry is done and the screen goes dark, I hope the quiet feels earned. Put the kettle on. The next hour is yours. You spent the whole day holding other people's work gently; hold a little of the night for yourself.

Thank you for reading this far.
"""


def main():
    # The gate allows 1 to 1,000 characters; fail loudly here instead of
    # submitting a text the scorer would reject.
    if not 1 <= len(TEXT) <= 1000:
        raise ValueError(f"entry text is {len(TEXT)} characters, must be 1-1000")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    # Outputs must stay readable by every user, not only the one who runs.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
