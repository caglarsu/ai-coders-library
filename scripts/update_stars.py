"""Rewrite the Stars cell of every README table row from the GitHub API, then sort each table by stars."""
import json, os, re, sys, urllib.request

ROW = re.compile(r"^(\| \[[^\]]+\]\(https://github\.com/([\w.-]+/[\w.-]+)\) \| )[^|]*( \|.*)$")


def fmt(n):
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def stars(repo):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    if token := os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as r:
        return json.load(r)["stargazers_count"]


def sort_tables(lines, counts):
    """Sort each run of consecutive repo rows by star count, highest first."""
    out, run = [], []
    for line in lines + [""]:
        if line in counts:
            run.append(line)
            continue
        out += sorted(run, key=lambda l: -counts[l])
        run = []
        out.append(line)
    return out[:-1]


def main(path="README.md", fetch=stars):
    lines = open(path).read().split("\n")
    counts = {}
    for i, line in enumerate(lines):
        if m := ROW.match(line):
            n = fetch(m[2])
            lines[i] = f"{m[1]}★ {fmt(n)}{m[3]}"
            counts[lines[i]] = n
    open(path, "w").write("\n".join(sort_tables(lines, counts)))


if __name__ == "__main__":
    assert fmt(994) == "994" and fmt(1312) == "1.3k" and fmt(326241) == "326.2k" and fmt(2000) == "2k"
    a, b, c = "| [a](https://github.com/o/a) | ★ 1 | x |", "| [b](https://github.com/o/b) | ★ 9 | x |", "| [c](https://github.com/o/c) | ★ 5 | x |"
    assert sort_tables(["# t", a, b, "", c, a], {a: 1, b: 9, c: 5}) == ["# t", b, a, "", c, a]
    main(*sys.argv[1:])
