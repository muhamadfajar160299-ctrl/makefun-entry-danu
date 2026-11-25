"""Write the entry: one shameless lie, five words, no trailing newline."""

import os

ENTRY = "I deleted your only backup."


def main():
    if not ENTRY.strip():
        raise SystemExit("entry is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise SystemExit(f"failed to write entry.txt: {exc}") from exc


if __name__ == "__main__":
    main()
