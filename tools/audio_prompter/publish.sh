#!/usr/bin/env bash
# Publish docs/ to the public GitHub repo buldukfirat0/thesis (GitHub Pages).
#
# The thesis repo itself is NOT pushed to GitHub: its history contains
# opencode.json with a live API key, and GitHub is public. Only the built
# prompter page and its build scripts go out, through a separate checkout
# in .gh-publish/ (gitignored).
#
# Usage:  bash tools/audio_prompter/publish.sh ["commit message"]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PUB="$ROOT/.gh-publish"
MSG="${1:-Update audio prompter}"

if [ ! -d "$PUB/.git" ]; then
  git clone git@github.com:buldukfirat0/thesis.git "$PUB"
fi

cd "$PUB"
git fetch origin main
git checkout -B main origin/main

mkdir -p docs tools/audio_prompter
cp "$ROOT/docs/index.html" "$ROOT/docs/sw.js" "$ROOT/docs/manifest.webmanifest" docs/
cp "$ROOT/tools/audio_prompter/build.py" \
   "$ROOT/tools/audio_prompter/content_dml.py" \
   "$ROOT/tools/audio_prompter/shell.html" \
   "$ROOT/tools/audio_prompter/publish.sh" tools/audio_prompter/

# Pages serves this repo from the root, so the root page just forwards to the prompter
cat > index.html <<'HTML'
<!doctype html>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=docs/index.html">
<title>DFB ve DML sesli calisma</title>
<p style="font-family:system-ui;background:#14181f;color:#e8ecf2;padding:24px">
Yonlendiriliyor: <a style="color:#d9a03f" href="docs/index.html">docs/index.html</a>
HTML

git add -A
if git diff --cached --quiet; then
  echo "nothing changed"
else
  git commit -q -m "$MSG"
  git push origin main
  echo "pushed -> https://buldukfirat0.github.io/thesis/"
fi
