(function () {
  'use strict';

  // --- Old single-page links (skazka.tours/#enquire and the like) go to the new pages ---
  var MOVED = { how: '/method/', itineraries: '/journeys/', journeys: '/journeys/', regions: '/regions/', founder: '/guides/', guides: '/guides/',
                'house-rules': '/method/#house-rules', faq: '/questions/', enquire: '/enquire/' };
  if (location.pathname === '/' && location.hash && MOVED[location.hash.slice(1)] && !document.getElementById(location.hash.slice(1))) {
    location.replace(MOVED[location.hash.slice(1)]);
    return;
  }

  // --- Nav scroll state ---
  var nav = document.getElementById('site-nav');
  function onScroll() {
    if (!nav) return;
    if (window.scrollY > 20 || nav.hasAttribute('data-solid')) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
    // the vehicle on the nav drives as far as you have read
    var max = document.documentElement.scrollHeight - window.innerHeight;
    nav.style.setProperty('--p', max > 0 ? Math.min(1, window.scrollY / max).toFixed(4) : '0');
    // the chat steps back once reading starts
    var chat = document.querySelector('.concierge'), panel = document.getElementById('concierge-panel');
    if (chat) chat.classList.toggle('is-compact', window.scrollY > 240 && !(panel && panel.classList.contains('open')));
  }
  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () { onScroll(); ticking = false; });
  }, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();

  // --- Phone menu: close on choosing a chapter or pressing Escape ---
  var menu = document.getElementById('nav-menu');
  if (menu) {
    menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { menu.removeAttribute('open'); }); });
    document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape' && menu.hasAttribute('open')) { menu.removeAttribute('open'); menu.querySelector('summary').focus(); } });
    menu.addEventListener('toggle', function () {
      document.documentElement.style.overflow = menu.open ? 'hidden' : '';
      document.documentElement.classList.toggle('menu-open', menu.open);
    });
  }

  // --- FAQ accordion ---
  var faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    var q = item.querySelector('.faq-q');
    item.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');
      faqItems.forEach(function (f) {
        f.classList.remove('open');
        var fq = f.querySelector('.faq-q');
        if (fq) fq.setAttribute('aria-expanded', 'false');
      });
      if (!isOpen) {
        item.classList.add('open');
        if (q) q.setAttribute('aria-expanded', 'true');
      }
    });
    if (q) q.addEventListener('keydown', function (ev) {
      if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); item.click(); }
    });
  });

  // --- Chip groups (single / multi) ---
  document.querySelectorAll('.chip-group').forEach(function (group) {
    var key = group.getAttribute('data-chip-group');
    var mode = group.getAttribute('data-chip-mode') || 'single';
    var hidden = document.getElementById('f-' + key);
    var selected = [];
    group.querySelectorAll('.chip').forEach(function (chip) {
      chip.addEventListener('click', function (ev) {
        ev.preventDefault();
        var val = chip.getAttribute('data-value');
        if (mode === 'single') {
          var wasOn = chip.classList.contains('selected');
          group.querySelectorAll('.chip').forEach(function (c) {
            c.classList.remove('selected');
            c.setAttribute('aria-pressed', 'false');
          });
          // tapping the chosen chip again clears it
          if (wasOn) { selected = []; }
          else { chip.classList.add('selected'); chip.setAttribute('aria-pressed', 'true'); selected = [val]; }
        } else {
          var on = chip.classList.toggle('selected');
          chip.setAttribute('aria-pressed', on ? 'true' : 'false');
          var idx = selected.indexOf(val);
          if (idx > -1) selected.splice(idx, 1); else selected.push(val);
        }
        if (hidden) hidden.value = selected.join(', ');
        renderLetter();
      });
    });
  });

  // --- East Africa Time (UTC+3, no daylight saving) ---
  function eatMinutes() {
    var d = new Date();
    return (d.getUTCHours() * 60 + d.getUTCMinutes() + 180) % 1440;
  }
  function fmt(m) {
    var h = Math.floor(m / 60), mm = m % 60;
    return (h < 10 ? '0' : '') + h + ':' + (mm < 10 ? '0' : '') + mm;
  }

  // --- "Now booking": a rolling window, three to ten months ahead of today in Kenya ---
  (function () {
    var el = document.getElementById('hero-booking'); if (!el) return;
    var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var now = new Date(Date.now() + 3 * 3600 * 1000);            // Kenya is UTC+3
    function ahead(n) { var d = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth() + n, 1)); return MONTHS[d.getUTCMonth()] + ' ' + d.getUTCFullYear(); }
    el.textContent = ahead(3) + ' \u2014 ' + ahead(10);
  })();

  // --- A day in the field: what the camp is doing right now ---
  var NOW_LINES = {
    tea: 'Tea is going round the tents. Nobody is quite awake.',
    dawn: 'Out for the dawn light. The first drive of the day is on.',
    breakfast: 'Breakfast in the bush, somewhere out on the plains.',
    midday: 'Midday heat. Camp is quiet; most guests are resting.',
    afternoon: 'Out again. The afternoon drive runs until sunset.',
    sunset: 'The sun is going down over the plains.',
    night: 'Dinner under the stars, and tomorrow is being planned.'
  };
  var dayMoments = document.querySelectorAll('.day-moment');
  var dayTime = document.getElementById('day-now-time');
  var dayText = document.getElementById('day-now-text');
  var sky = document.getElementById('sky');
  var eatClock = document.getElementById('eat-clock');
  var dayStrip = document.getElementById('day-strip');
  var dayScrolled = false;

  // --- Hero follows the Kenya day: dawn, day, sunset, night ---
  // Only the sunset clip exists so far, so the other phases re-tint it (see CSS).
  // To give a phase its own footage: add /assets/hero-<phase>.mp4 and /assets/hero-poster-<phase>.jpg,
  // then add the phase name to data-clips on the hero video, e.g. data-clips="sunset dawn".
  var heroEl = document.querySelector('.hero');
  var heroVideo = document.getElementById('hero-video');
  var heroStill = document.getElementById('hero-fallback');
  var heroClips = heroVideo ? (heroVideo.getAttribute('data-clips') || 'sunset').split(/\s+/) : [];
  var heroStills = heroVideo ? (heroVideo.getAttribute('data-stills') || '').split(/\s+/) : [];
  // A phase can also be a still photograph: add /assets/hero-<phase>.jpg and list the phase in data-stills.
  var STILL_ALT = { day: 'An elephant walking through golden grass in daylight' };
  var BASE_ALT = heroStill ? heroStill.alt : '';
  function phaseAt(m) {
    if (m >= 330 && m < 480) return 'dawn';     // 05:30 - 08:00
    if (m >= 480 && m < 990) return 'day';      // 08:00 - 16:30
    if (m >= 990 && m < 1140) return 'sunset';  // 16:30 - 19:00
    return 'night';
  }
  function setHeroPhase(m) {
    if (!heroEl || !heroVideo || !heroStill) return;
    var phase = phaseAt(m);
    if (heroEl.getAttribute('data-phase') === phase) return;
    heroEl.setAttribute('data-phase', phase);
    var kind = phase === 'sunset' ? 'base' : heroClips.indexOf(phase) > -1 ? 'clip' : heroStills.indexOf(phase) > -1 ? 'still' : 'tint';
    // own footage or photograph: no tint
    if (kind === 'clip' || kind === 'still') heroEl.setAttribute('data-own-clip', ''); else heroEl.removeAttribute('data-own-clip');
    if (kind === 'still') heroEl.setAttribute('data-still', ''); else heroEl.removeAttribute('data-still');

    // the video
    var wantVideo = kind === 'clip' ? phase : 'sunset';
    if (kind === 'still') { heroVideo.pause(); }
    else {
      if ((heroVideo.getAttribute('data-playing') || 'sunset') !== wantVideo) {
        heroVideo.innerHTML = kind === 'clip' ? '' : '<source src="/assets/hero.webm" type="video/webm"><source src="/assets/hero.mp4" type="video/mp4">';
        if (kind === 'clip') heroVideo.src = '/assets/hero-' + phase + '.mp4'; else heroVideo.removeAttribute('src');
        heroVideo.poster = kind === 'clip' ? '/assets/hero-poster-' + phase + '.jpg' : '/assets/hero-poster.jpg';
        heroVideo.setAttribute('data-playing', wantVideo);
        heroVideo.load();
      }
      var playing = heroVideo.play(); if (playing && playing.catch) playing.catch(function () {});
    }

    // the still image beneath it (and the whole picture, for a still phase)
    var wantStill = kind === 'still' ? '/assets/hero-' + phase + '.jpg' : kind === 'clip' ? '/assets/hero-poster-' + phase + '.jpg' : '/assets/hero-poster.jpg';
    if (heroStill.getAttribute('src') !== wantStill) {
      heroStill.classList.add('is-loading');   // fade the new picture in once it has arrived
      heroStill.onload = heroStill.onerror = function () { heroStill.classList.remove('is-loading'); };
      heroStill.src = wantStill;
      heroStill.alt = kind === 'still' ? (STILL_ALT[phase] || '') : BASE_ALT;
      if (heroStill.complete) heroStill.classList.remove('is-loading');
    }
  }
  var heroNow = document.getElementById('hero-now-text');
  var NOW_SHORT = {
    tea: 'tea is going round the tents', dawn: 'the dawn drive is out', breakfast: 'breakfast in the bush',
    midday: 'the camp is resting', afternoon: 'the afternoon drive is out', sunset: 'the sun is going down',
    night: 'dinner under the stars'
  };
  function renderDay() {
    var m = eatMinutes();
    if (dayTime) dayTime.textContent = fmt(m);
    if (eatClock) eatClock.textContent = fmt(m) + ' \u00b7 EAT, UTC+3';
    var current = null;
    dayMoments.forEach(function (el) {
      if (m >= parseInt(el.getAttribute('data-from'), 10)) current = el;
      el.classList.remove('is-now');
    });
    setHeroPhase(m);
    var asleep = !current || m >= 1290; // before 05:30 or after 21:30
    if (heroNow) heroNow.textContent = fmt(m) + ' in Kenya \u00b7 ' + (asleep ? 'the camp is asleep' : NOW_SHORT[current.getAttribute('data-sky')]);
    if (asleep) {
      if (dayText) dayText.textContent = 'The camp is asleep. Tea comes round at 05:30.';
    } else {
      current.classList.add('is-now');
      if (dayText) dayText.textContent = NOW_LINES[current.getAttribute('data-sky')] || '';
      // on narrow screens, bring the current moment into the strip's view once
      if (!dayScrolled && dayStrip && dayStrip.scrollWidth > dayStrip.clientWidth) {
        dayStrip.scrollLeft += current.getBoundingClientRect().left - dayStrip.getBoundingClientRect().left - 2;
        dayScrolled = true;
      }
    }
    if (sky) {
      // the sun rides the arc from about 06:15 to 18:40; the moon keeps the night
      var t = (m - 375) / (1120 - 375);
      var night = t < 0 || t > 1;
      sky.classList.toggle('is-night', night);
      if (!night) {
        sky.style.setProperty('--x', ((1 - Math.cos(Math.PI * t)) / 2).toFixed(4));
        sky.style.setProperty('--y', Math.sin(Math.PI * t).toFixed(4));
      }
    }
  }
  renderDay();
  setInterval(renderDay, 30000);

  // --- The enquiry note that writes itself ---
  var picked = { journey: '' };
  var letterText = document.getElementById('letter-text');
  function val(id) { var el = document.getElementById(id); return el ? el.value.trim() : ''; }
  function listJoin(items) {
    if (items.length < 2) return items.join('');
    return items.slice(0, -1).join(', ') + ' and ' + items[items.length - 1];
  }
  function composeLetter() {
    var group = val('f-group'), n = parseInt(val('f-travelers'), 10) || 0;
    var dates = val('f-dates'), flex = val('f-flexible');
    var interests = val('f-interests'), pace = val('f-pace');
    var name = val('f-name'), note = val('f-note');
    var solo = group === 'Solo traveler' || (!group && n === 1);
    var We = solo ? 'I' : 'We', we = solo ? 'I' : 'we', us = solo ? 'me' : 'us';
    var lines = [];

    var who = '';
    if (group === 'Couple') who = "We're a couple";
    else if (group === 'Family') who = "We're a family" + (n > 1 ? ' of ' + n : '');
    else if (group === 'Friends') who = "We're " + (n > 1 ? n + ' friends' : 'a group of friends');
    else if (solo) who = "I'm travelling on my own";

    var when = '';
    if (dates) when = 'hoping to come ' + dates.replace(/^(late|early|mid|end|around|in|sometime|next|this|any|maybe)\b/i, function (x) { return x.toLowerCase(); });
    var flexPart = { 'Firm': ', and the dates are firm', 'Within a week': ', give or take a week', 'Within a month': ', give or take a month', "Whenever's best": '' }[flex];
    if (flex === "Whenever's best") when = dates ? when + ', or whenever you think is best' : 'happy to come whenever you think is best';
    else if (when && flexPart) when += flexPart;

    if (who && when) lines.push(who + ', ' + when + '.');
    else if (who) lines.push(who + '.');
    else if (when) lines.push((solo ? "I'm " : "We're ") + when + '.');

    if (picked.journey) lines.push('\u201c' + picked.journey + '\u201d looked like a good starting point.');
    if (interests) lines.push(We + ' love ' + listJoin(interests.split(', ').map(function (x) {
      return { 'Coastal finish': 'a coastal finish', 'Hot-air balloon': 'a hot-air balloon flight' }[x] || x.toLowerCase();
    })) + '.');
    if (pace) lines.push({
      'Slower \u2014 fewer moves': 'A slower pace suits ' + us + ', with fewer moves.',
      'Balanced': 'A balanced pace suits ' + us + '.',
      'Fuller \u2014 see more': We + "'d like to see as much as " + we + ' can.'
    }[pace] || '');
    if (note) lines.push('Also: ' + note.replace(/[.\s]+$/, '').replace(/^[A-Z](?=[a-z])/, function (c) { return c.toLowerCase(); }) + '.');

    if (!lines.filter(Boolean).length && !name) return '';
    return 'Dear Kimani,\n\n' + lines.filter(Boolean).join(' ') + '\n\n\u2014 ' + (name || '');
  }
  function renderLetter() {
    if (!letterText) return;
    var text = composeLetter();
    if (text && text !== letterText.textContent) {
      var box = document.getElementById('letter');
      if (box) { box.classList.remove('is-fresh'); void box.offsetWidth; box.classList.add('is-fresh'); }
    }
    if (text) {
      letterText.textContent = text;
      letterText.classList.remove('is-empty');
    } else {
      letterText.textContent = 'Dear Kimani, \u2026 your answers will turn into a short letter here.';
      letterText.classList.add('is-empty');
    }
  }
  ['f-dates', 'f-travelers', 'f-name', 'f-note'].forEach(function (id) {
    var el = document.getElementById(id);
    if (el) el.addEventListener('input', renderLetter);
  });
  try {
    var chosen = new URLSearchParams(location.search).get('journey');
    if (chosen && letterText) { picked.journey = chosen.replace(/[<>]/g, '').slice(0, 80); renderLetter(); }
  } catch (e) {}

  // --- Multi-step Enquire form ---
  var form = document.getElementById('enquire-form');
  if (form) {
    var stepsEls = form.querySelectorAll('.form-step');
    var dots = form.querySelectorAll('.form-progress-dot');
    var backBtn = document.getElementById('form-back');
    var nextBtn = document.getElementById('form-next');
    var submitBtn = document.getElementById('form-submit');
    var bodyEl = document.getElementById('enquire-body');
    var successEl = document.getElementById('enquire-success');
    var currentStep = 0;

    function renderStep() {
      stepsEls.forEach(function (s, i) {
        if (i === currentStep) s.removeAttribute('hidden');
        else s.setAttribute('hidden', '');
      });
      dots.forEach(function (d, i) {
        if (i <= currentStep) d.classList.add('active');
        else d.classList.remove('active');
      });
      if (currentStep === 0) backBtn.setAttribute('hidden', ''); else backBtn.removeAttribute('hidden');
      if (currentStep === stepsEls.length - 1) {
        nextBtn.setAttribute('hidden', '');
        submitBtn.removeAttribute('hidden');
      } else {
        nextBtn.removeAttribute('hidden');
        submitBtn.setAttribute('hidden', '');
      }
    }
    renderStep();

    nextBtn.addEventListener('click', function () {
      if (currentStep < stepsEls.length - 1) { currentStep++; renderStep(); }
    });
    backBtn.addEventListener('click', function () {
      if (currentStep > 0) { currentStep--; renderStep(); }
    });

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var get = function (id) { var el = document.getElementById(id); return el ? el.value : ''; };
      var name = get('f-name');
      var email = get('f-email');
      var dates = get('f-dates');
      var flexible = get('f-flexible');
      var group = get('f-group');
      var travelers = get('f-travelers');
      var interests = get('f-interests');
      var pace = get('f-pace');
      var note = get('f-note');

      var subject = 'Trip enquiry \u2014 ' + (name || 'new guest');
      var letter = composeLetter();
      var bodyLines = [
        letter,
        '',
        '\u2014 the details \u2014',
        'Starting point: ' + (picked.journey || '\u2014'),
        'Dates: ' + dates + (flexible ? ' (' + flexible + ')' : ''),
        'Group: ' + group + (travelers ? ' \u00b7 ' + travelers + ' travellers' : ''),
        'Interests: ' + interests,
        'Pace: ' + pace,
        'Contact: ' + name + ' \u00b7 ' + email,
        'Note: ' + note
      ];
      var mailto = 'mailto:hello@skazka.tours?subject=' + encodeURIComponent(subject) +
                   '&body=' + encodeURIComponent(bodyLines.join('\n'));

      if (bodyEl) bodyEl.setAttribute('hidden', '');
      if (successEl) successEl.removeAttribute('hidden');

      window.location.href = mailto;
    });
  }

  // --- Concierge widget open/close + chat ---
  var conciergeToggle = document.getElementById('concierge-toggle');
  var conciergePanel = document.getElementById('concierge-panel');
  var conciergeLabel = document.getElementById('concierge-toggle-label');
  if (conciergeToggle && conciergePanel) {
    conciergeToggle.addEventListener('click', function () {
      var open = conciergePanel.classList.toggle('open');
      onScroll();
      conciergeLabel.textContent = open ? 'Close' : 'Chat with Kimani';
      conciergeToggle.setAttribute('aria-label', open ? 'Close concierge chat' : 'Open concierge chat');
    });
  }

  var RESPONSES = {
    "When's best for the Mara?": "Great migration peak is July through October, but I actually prefer late June \u2014 the crowds haven't arrived and the grass is shorter. Shoulder months are quieter and much better value.",
    "What does a typical day look like?": "There is no typical day. But often: 5:30 tea, out by 6 for the dawn light, breakfast in the bush around 10, rest at camp through midday heat, out again 3:30 until sunset. Dinner under the stars. We adjust everything daily.",
    "Do you take families?": "Yes \u2014 with care. I've taken guests as young as five. For children we slow the pace, cut driving hours, and lean into walks, camp projects, and nighttime astronomy. It becomes calmer and stays just as interesting."
  };
  var conciergeBody = document.getElementById('concierge-body');
  function appendMsg(from, text) {
    var div = document.createElement('div');
    div.className = 'concierge-msg ' + from;
    div.textContent = text;
    conciergeBody.appendChild(div);
    conciergeBody.scrollTop = conciergeBody.scrollHeight;
  }
  function sendConcierge(text) {
    if (!text) return;
    document.querySelectorAll('.concierge-prompt').forEach(function (el) { el.remove(); });
    appendMsg('you', text);
    setTimeout(function () {
      var reply = RESPONSES[text] || "Good question \u2014 let me write you a proper answer. If you share your email on the Plan a trip page, I'll reply personally within the day.";
      appendMsg('kimani', reply);
    }, 700);
  }
  document.querySelectorAll('.concierge-prompt').forEach(function (btn) {
    btn.addEventListener('click', function () {
      sendConcierge(btn.getAttribute('data-prompt'));
    });
  });
  var conciergeForm = document.getElementById('concierge-form');
  var conciergeInput = document.getElementById('concierge-input');
  if (conciergeForm) {
    conciergeForm.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var val = conciergeInput.value.trim();
      if (val) { sendConcierge(val); conciergeInput.value = ''; }
    });
  }
})();
