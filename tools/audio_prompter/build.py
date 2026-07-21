#!/usr/bin/env python3
"""Build the offline audio prompter for the talk.

Reads the sentence list from content_dml.py, renders every sentence with edge-tts
in five voices (cached in mp3cache/), embeds the clips as base64 into the app shell
from shell.html, and writes:

    docs/index.html            -> published by GitHub Pages, service worker added
    EXAMPLE/prompter.html      -> same page, for opening straight from disk

Usage:  python3 tools/audio_prompter/build.py
Only sentences whose text changed are re-rendered, so rebuilds are fast.
"""
import base64
import concurrent.futures as cf
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from content_dml import PARTS, VOICES

EDGE = "/home/firat/snap/code/247/.local/bin/edge-tts"
CACHE = os.path.join(HERE, "mp3cache")
SHELL = os.path.join(HERE, "shell.html")
DOCS = os.path.join(ROOT, "docs", "index.html")
LOCAL = os.path.join(ROOT, "EXAMPLE", "prompter.html")
os.makedirs(CACHE, exist_ok=True)

TITLE = "DFB, DML ve EAM sesli calisma"
H1 = "DFB laser &middot; DML &middot; EAM"
ALBUM = "DFB - EAM sesli calisma"


def spoken_of(disp, spoken):
    return spoken or disp


def clip_path(voice_key, txt):
    h = hashlib.sha1((VOICES[voice_key] + "|" + txt).encode()).hexdigest()[:16]
    return os.path.join(CACHE, f"{voice_key}_{h}.mp3")


# ---------------------------------------------------------------- render
flat = [spoken_of(d, s) for p in PARTS for _, items in p["sections"] for d, s in items]
jobs = [(clip_path(k, t), VOICES[k], t) for t in flat for k in VOICES]


def render(job):
    path, vid, txt = job
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        return 0
    for _ in range(4):
        subprocess.run([EDGE, "--voice", vid, "--text", txt, "--write-media", path],
                       capture_output=True)
        if os.path.exists(path) and os.path.getsize(path) > 1000:
            return 1
    raise RuntimeError(f"edge-tts failed for {vid}: {txt[:50]}")


with cf.ThreadPoolExecutor(max_workers=6) as ex:
    new = sum(ex.map(render, jobs))
print(f"clips: {len(jobs)} total, {new} newly rendered")

# ---------------------------------------------------------------- durations
durs = {k: [] for k in VOICES}
for txt in flat:
    for k in VOICES:
        d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "csv=p=0", clip_path(k, txt)],
                           capture_output=True, text=True).stdout.strip()
        durs[k].append(round(float(d), 3))

# ---------------------------------------------------------------- data
data = []
for p in PARTS:
    secs = []
    for title, items in p["sections"]:
        out = [{"t": d, "a": {k: base64.b64encode(open(clip_path(k, spoken_of(d, s)), "rb").read()).decode()
                              for k in VOICES}} for d, s in items]
        secs.append({"title": title, "items": out})
    data.append({"num": p["num"], "name": p["name"], "sections": secs})

n = sum(len(s["items"]) for d in data for s in d["sections"])
assert all(len(v) == n for v in durs.values())

# ---------------------------------------------------------------- html
shell = open(SHELL, encoding="utf-8").read()
shell = shell.replace("<title>Seminer calismasi</title>", f"<title>{TITLE}</title>")
shell = shell.replace("<h1>Seminer &mdash; sesli calisma</h1>", f"<h1>{H1}</h1>")
shell = shell.replace("b.textContent = 'Slide ' + s.num + ' · ' + s.name;",
                      "b.textContent = s.num + ' · ' + s.name;")
shell = shell.replace("artist: 'Slide ' + s.num + ' · ' + s.sec,",
                      "artist: s.name + ' · ' + s.sec,")
shell = shell.replace("album: 'Seminer sesli calisma'", f"album: '{ALBUM}'")
assert "Slide ' + s.num" not in shell and "Seminer" not in shell

lines = shell.split("\n")
i = next(k for k, l in enumerate(lines) if l.startswith("const DURS = "))
lines[i] = ("const DATA = " + json.dumps(data, ensure_ascii=False) + ";\n"
            "const DURS = " + json.dumps(durs) + ";")
page = "\n".join(lines)

os.makedirs(os.path.dirname(DOCS), exist_ok=True)
open(LOCAL, "w", encoding="utf-8").write(page)

# published copy: installable, and cached by a service worker so the phone keeps
# working with no connection after the first visit
ver = time.strftime("%Y%m%d-%H%M%S", time.gmtime(os.path.getmtime(LOCAL)))
head_extra = ('<link rel="manifest" href="manifest.webmanifest">\n'
              '<meta name="theme-color" content="#14181f">\n')
sw_reg = ("<script>\n"
          "if ('serviceWorker' in navigator) "
          "window.addEventListener('load', () => navigator.serviceWorker.register('sw.js'));\n"
          "</script>\n")
pub = page.replace("</head>", head_extra + "</head>", 1).replace("</body>", sw_reg + "</body>", 1)
open(DOCS, "w", encoding="utf-8").write(pub)

sw = f"""// bump CACHE when index.html changes; the old copy is then dropped
const CACHE = 'prompter-{ver}';
const ASSETS = ['./', './index.html', './manifest.webmanifest'];
self.addEventListener('install', e => {{
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
}});
self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(ks =>
    Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
}});
self.addEventListener('fetch', e => {{
  if (e.request.method !== 'GET') return;
  e.respondWith(caches.match(e.request, {{ignoreSearch: true}}).then(r => r || fetch(e.request)));
}});
"""
open(os.path.join(os.path.dirname(DOCS), "sw.js"), "w").write(sw)

manifest = {
    "name": TITLE, "short_name": "DFB/DML", "start_url": "./index.html",
    "display": "standalone", "background_color": "#14181f", "theme_color": "#14181f",
    "icons": [],
}
open(os.path.join(os.path.dirname(DOCS), "manifest.webmanifest"), "w").write(
    json.dumps(manifest, ensure_ascii=False, indent=2))

print(f"{n} sentences, {len(data)} parts, cache version {ver}")
print(f"  {DOCS} ({os.path.getsize(DOCS)/1e6:.1f} MB)")
print(f"  {LOCAL} ({os.path.getsize(LOCAL)/1e6:.1f} MB)")
