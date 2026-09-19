/* Helpers de coreografia do estúdio (GSAP, timeline única pausada). */
window.KJ = (function () {
  // Envolve cada palavra do título num span inline-block, preservando <br> e <span class="acento">.
  function words(root) {
    var out = [];
    function walk(node) {
      var kids = Array.prototype.slice.call(node.childNodes);
      kids.forEach(function (k) {
        if (k.nodeType === 3) {
          var parts = k.textContent.split(/([ \t\n\r]+)/);
          var frag = document.createDocumentFragment();
          parts.forEach(function (p) {
            if (!p) return;
            if (/^[ \t\n\r]+$/.test(p)) { frag.appendChild(document.createTextNode(' ')); return; }
            var s = document.createElement('span');
            s.className = 'w';
            s.textContent = p;
            frag.appendChild(s);
            out.push(s);
          });
          node.replaceChild(frag, k);
        } else if (k.nodeType === 1 && k.tagName !== 'BR') {
          walk(k);
        }
      });
    }
    walk(root);
    return out;
  }
  function intro(tl, opts) {
    opts = opts || {};
    tl.fromTo('.logo', { opacity: 0, scale: 0.9 }, { opacity: 1, scale: 1, duration: 0.6, ease: 'power2.out' }, 0);
    tl.fromTo('.kicker', { opacity: 0, x: opts.kickerCentered ? 0 : -24, y: opts.kickerCentered ? -12 : 0 },
      { opacity: 1, x: 0, y: 0, duration: 0.5, ease: 'power2.out' }, 0.15);
    var w = words(document.querySelector('.titulo'));
    tl.fromTo(w, { opacity: 0, y: 56 }, { opacity: 1, y: 0, duration: 0.7, ease: 'back.out(1.2)', stagger: 0.055 }, 0.3);
    return w;
  }
  function pop(tl, el, t, big) {
    tl.fromTo(el, { opacity: 0, scale: 0, rotation: -10 },
      { opacity: 1, scale: 1, rotation: 0, duration: big ? 0.7 : 0.55, ease: big ? 'back.out(2.4)' : 'back.out(2)' }, t);
  }
  function rise(tl, el, t, dy, dur, extra) {
    var from = { opacity: 0, y: dy, scale: 0.94 }, to = { opacity: 1, y: 0, scale: 1, duration: dur || 1, ease: 'power3.out' };
    if (extra) { for (var k in extra) { from[k] = extra[k]; to[k] = extra[k]; } }
    tl.fromTo(el, from, to, t);
  }
  function slide(tl, el, t, dx, dur, stagger) {
    tl.fromTo(el, { opacity: 0, x: dx }, { opacity: 1, x: 0, duration: dur || 0.6, ease: 'power3.out', stagger: stagger || 0 }, t);
  }
  function up(tl, el, t, dy, dur, stagger) {
    tl.fromTo(el, { opacity: 0, y: dy }, { opacity: 1, y: 0, duration: dur || 0.6, ease: 'power3.out', stagger: stagger || 0 }, t);
  }
  function fade(tl, el, t, dur) {
    tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: dur || 0.6, ease: 'power2.out' }, t);
  }
  // Flutuação sutil e finita: parte de y=0 e volta a y=0 exatamente em t+6 s.
  function float(tl, el, t, amp, extra) {
    var end = window.KJ_END || 8;
    var to = { y: -(amp || 8), duration: (end - t) / 4, ease: 'sine.inOut', repeat: 3, yoyo: true };
    if (extra) { for (var k in extra) { to[k] = extra[k]; } }
    tl.to(el, to, t);
  }
  return { words: words, intro: intro, pop: pop, rise: rise, slide: slide, up: up, fade: fade, float: float };
})();
