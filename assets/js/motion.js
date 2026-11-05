// Shared interactive motion: scroll-reveal entrances and a pointer-responsive
// spotlight. Both are progressive enhancement:
//   - .reveal content is fully visible without this script (see the
//     .js-scoped CSS in assets/css/style.css) — it only animates in if a
//     tiny inline script at the top of <body> has already added the "js"
//     class to <html>, which only happens when JS is actually running.
//   - The spotlight only attaches on devices with a real mouse/trackpad
//     (checked via the "hover: hover" + "pointer: fine" media query), so it
//     never partially-activates on touchscreens.
// Reduced motion is handled globally in style.css (transition/animation
// durations are crushed to near-zero for prefers-reduced-motion: reduce),
// so no extra branching is needed here beyond what's already in the CSS.
(function () {
    var revealEls = document.querySelectorAll('.reveal');
    if (revealEls.length) {
        if ('IntersectionObserver' in window) {
            var io = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        io.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
            revealEls.forEach(function (el) { io.observe(el); });
        } else {
            // No IntersectionObserver support — just show everything.
            revealEls.forEach(function (el) { el.classList.add('is-visible'); });
        }
    }

    var canHover = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    if (canHover) {
        document.querySelectorAll('.spotlight').forEach(function (el) {
            el.addEventListener('mousemove', function (e) {
                var rect = el.getBoundingClientRect();
                el.style.setProperty('--x', (e.clientX - rect.left) + 'px');
                el.style.setProperty('--y', (e.clientY - rect.top) + 'px');
            });
        });
    }
})();
