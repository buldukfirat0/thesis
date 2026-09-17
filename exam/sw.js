// bump CACHE when index.html changes; the old copy is then dropped
const CACHE = 'exam-prompter-20260917-190025';
// clips have content-hash names and never change, so they live in their own cache
// that survives page updates
const AUDIO = 'exam-prompter-audio';
const ASSETS = ['./', './index.html', './manifest.webmanifest'];
self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks =>
    Promise.all(ks.filter(k => k.startsWith('exam-prompter-') && k !== CACHE && k !== AUDIO).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  if (new URL(e.request.url).pathname.includes('/audio/')) {
    e.respondWith(caches.open(AUDIO).then(c => c.match(e.request).then(r => r ||
      fetch(e.request).then(res => { if (res.ok) c.put(e.request, res.clone()); return res; }))));
    return;
  }
  e.respondWith(caches.match(e.request, {ignoreSearch: true}).then(r => r || fetch(e.request)));
});
