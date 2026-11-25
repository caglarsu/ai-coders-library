"""Build llms.txt and catalog/<section>.md from README.md: plain text that AI readers can take in whole."""
import pathlib, re, sys

RAW = "https://raw.githubusercontent.com/caglarsu/ai-coders-library/main/"
SKIP = {"Ask your AI what fits you", "For AI assistants reading this", "Contents", "Contributing", "License", "Workflows"}


def cells(line):
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def section_file(title, body):
    """One section as plain text: each table row becomes a labelled block. Returns (text, [(name, url)])."""
    out, entries, header = [f"# {title}", ""], [], None
    for line in body.split("\n"):
        if not line.startswith("|"):
            header = None
            out.append(line)
            continue
        c = cells(line)
        if header is None:
            header = c
        elif not all(set(x) <= set("-") for x in c):
            m = re.fullmatch(r"\[(.+?)\]\((.+?)\)", c[0])
            name, url = (m[1], m[2]) if m else (c[0], "")
            entries.append((name, url))
            out += [f"### {name}"] + ([f"Link: {url}"] if url else [])
            out += [f"{h}: {v}" for h, v in zip(header[1:], c[1:]) if v] + [""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n", entries


def build(readme):
    parts = dict(p.split("\n", 1) for p in re.split(r"^## ", readme, flags=re.M)[1:])
    rules = [l for l in parts["For AI assistants reading this"].split("\n") if re.match(r"\d+\. ", l)]
    files, index = {}, []
    for title, body in parts.items():
        if title in SKIP:
            continue
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        text, entries = section_file(title, body)
        files[f"catalog/{slug}.md"] = text
        index += ["", f"## {title} ({len(entries)} entries)", f"Full details: {RAW}catalog/{slug}.md"]
        index += [f"- {n}: {u}" if u else f"- {n}" for n, u in entries]
    total = sum(1 for l in index if l.startswith("- "))
    files["llms.txt"] = "\n".join([
        "# AI Coder's Library", "",
        f"> {total} curated skills, tools, agents and models for developers who build with AI coding assistants. "
        "Each entry has what it does, when to use it, what it works with, how to install it and its GitHub stars (updated daily).", "",
        "This index names every entry with its link. Each section's file has the full details; read the files for the sections that matter to the user.", "",
        "## How to answer the user", *rules, *index]) + "\n"
    return files


def main(root="."):
    root = pathlib.Path(root)
    files = build((root / "README.md").read_text())
    for old in (root / "catalog").glob("*.md"):
        if f"catalog/{old.name}" not in files:
            old.unlink()
    for path, text in files.items():
        (root / path).parent.mkdir(exist_ok=True)
        (root / path).write_text(text)


if __name__ == "__main__":
    demo = "## Contents\nx\n## For AI assistants reading this\n1. Ask.\n## Tools\n\nNote.\n\n| Name | Stars | Install |\n| ---- | ----- | ------- |\n| [A](https://github.com/o/a) | ★ 2k | `x \\| sh` |\n"
    f = build(demo)
    assert "### A\nLink: https://github.com/o/a\nStars: ★ 2k\nInstall: `x | sh`" in f["catalog/tools.md"], f["catalog/tools.md"]
    assert "Note." in f["catalog/tools.md"] and "- A: https://github.com/o/a" in f["llms.txt"] and "1. Ask." in f["llms.txt"]
    main(*sys.argv[1:])
