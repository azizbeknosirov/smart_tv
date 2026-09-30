// Susambil TV — service worker
// Menyu doim yangi ma'lumot bilan ishlaydi (network-first). Internet uzilsa,
// oxirgi ko'rilgan menyu keshdan ko'rsatiladi.
const CACHE = 'susambil-v1';
const PRECACHE = ['/tv/', '/pwa/icon-192.png'];

// Faqat ochiq (login talab qilmaydigan) yo'llar keshlanadi.
// /panel/, /admin/, /api/auth/ va boshqalar HECH QACHON keshlanmaydi.
function isCacheable(url) {
  const p = url.pathname;
  return (
    p === '/' ||
    p === '/tv/' ||
    p === '/api/tv-menu/' ||
    p === '/api/tv-settings/' ||
    p.startsWith('/media/') ||
    p.startsWith('/pwa/')
  );
}

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((c) => c.addAll(PRECACHE))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin || !isCacheable(url)) return;

  event.respondWith(
    fetch(req)
      .then((res) => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
        }
        return res;
      })
      .catch(() => caches.match(req).then((hit) => hit || caches.match('/tv/')))
  );
});