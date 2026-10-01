/* Khandesh Kitchen — interactions */
(function () {
  'use strict';

  /* ── Sticky navbar state ─────────────────────────────── */
  const nav = document.getElementById('nav');
  const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 24);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ── Mobile burger menu ─────────────────────────────── */
  const burger = document.getElementById('burger');
  const links = document.getElementById('navLinks');
  const closeMenu = () => {
    burger.classList.remove('is-open');
    links.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  };
  burger.addEventListener('click', () => {
    const open = links.classList.toggle('is-open');
    burger.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
  });
  links.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));

  /* ── Active section highlighting ────────────────────── */
  const sections = ['home', 'about', 'menu', 'gallery', 'visit']
    .map(id => document.getElementById(id))
    .filter(Boolean);
  const navAnchors = [...links.querySelectorAll('.nav__link')];
  const spy = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      navAnchors.forEach(a =>
        a.classList.toggle('is-active', a.getAttribute('href') === '#' + e.target.id)
      );
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  sections.forEach(s => spy.observe(s));

  /* ── Menu tabs ──────────────────────────────────────── */
  const tabs = document.querySelectorAll('.menu__tab');
  const panels = document.querySelectorAll('.menu__panel');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const cat = tab.dataset.cat;
      tabs.forEach(t => {
        const active = t === tab;
        t.classList.toggle('is-active', active);
        t.setAttribute('aria-selected', String(active));
      });
      panels.forEach(p => {
        const active = p.dataset.cat === cat;
        p.classList.toggle('is-active', active);
        p.hidden = !active;
      });
    });
  });

  /* ── Reveal on scroll ───────────────────────────────── */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach((e, i) => {
        if (e.isIntersecting) {
          e.target.style.transitionDelay = Math.min(i * 70, 280) + 'ms';
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('is-in'));
  }

  /* ── Gallery lightbox ───────────────────────────────── */
  const lightbox = document.getElementById('lightbox');
  const lbImg = lightbox.querySelector('img');
  const lbCap = lightbox.querySelector('figcaption');
  const items = [...document.querySelectorAll('.gallery__item img')];
  let current = 0;

  const show = i => {
    current = (i + items.length) % items.length;
    const img = items[current];
    lbImg.src = img.src;
    lbImg.alt = img.alt;
    lbCap.textContent = img.closest('figure').querySelector('figcaption').textContent;
  };
  const openLb = i => { show(i); lightbox.classList.add('is-open'); lightbox.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden'; };
  const closeLb = () => { lightbox.classList.remove('is-open'); lightbox.setAttribute('aria-hidden', 'true'); document.body.style.overflow = ''; };

  items.forEach((img, i) =>
    img.closest('figure').addEventListener('click', () => openLb(i))
  );
  lightbox.querySelector('.lightbox__close').addEventListener('click', closeLb);
  lightbox.querySelector('.lightbox__nav--prev').addEventListener('click', () => show(current - 1));
  lightbox.querySelector('.lightbox__nav--next').addEventListener('click', () => show(current + 1));
  lightbox.addEventListener('click', e => { if (e.target === lightbox) closeLb(); });
  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('is-open')) return;
    if (e.key === 'Escape') closeLb();
    if (e.key === 'ArrowLeft') show(current - 1);
    if (e.key === 'ArrowRight') show(current + 1);
  });

  /* ── Open-now badge (11:00–23:00 IST) ───────────────── */
  const openBadge = document.querySelector('.visit__open');
  if (openBadge) {
    const now = new Date();
    const ist = new Date(now.getTime() + (now.getTimezoneOffset() + 330) * 60000);
    const h = ist.getHours();
    const isOpen = h >= 11 && h < 23;
    openBadge.textContent = isOpen ? '● Open Now' : '● Opens at 11:00 AM';
    openBadge.style.color = isOpen ? '#1c7a34' : '#a3271b';
  }

  /* ── Pause hero-adjacent video when out of view ─────── */
  const video = document.getElementById('promoVideo');
  if (video && 'IntersectionObserver' in window) {
    const vio = new IntersectionObserver(entries => {
      entries.forEach(e => { if (!e.isIntersecting && !video.paused) video.pause(); });
    }, { threshold: 0.25 });
    vio.observe(video);
  }
})();


