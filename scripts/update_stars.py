"""Rewrite the Stars cell of every README table row from the GitHub API."""
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


def main(path="README.md"):
    lines = open(path).read().split("\n")
    for i, line in enumerate(lines):
        if m := ROW.match(line):
            lines[i] = f"{m[1]}★ {fmt(stars(m[2]))}{m[3]}"
    open(path, "w").write("\n".join(lines))


if __name__ == "__main__":
    assert fmt(994) == "994" and fmt(1312) == "1.3k" and fmt(326241) == "326.2k" and fmt(2000) == "2k"
    main(*sys.argv[1:])
