"""Everyday Wonder — one sentence that makes a small everyday moment strange and new."""

LINE = "My shadow on the morning wall arrived half a second late, and I spent the whole walk to work wondering which of us was leading."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
