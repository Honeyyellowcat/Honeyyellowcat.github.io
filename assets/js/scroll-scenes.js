// Scroll "scenes" for the homepage: one section's content is in full
// focus at a time (the dissolve), and -- independently -- each orbital
// trajectory above a section heading lights up as it enters the
// viewport and stays lit while the heading is in view.
//
// Deliberately narrow in scope:
//   - Section dissolve progress is measured from each .scene-section's
//     own, untouched bounding box -- the section itself is never
//     animated, so it always keeps its normal content-driven
//     height/width, with no extra spacers and no full-screen height
//     rules. Only descendants marked .scene-content dissolve; opacity +
//     a small translateY only, never scale, so nothing shrinks or pulls
//     the layout inward. The fade window is sized relative to the
//     viewport, not to any section's own height, and entry/exit windows
//     overlap at the handoff so neighbors don't peek in but there's
//     never a blank stretch either.
//   - Trajectory progress is a SEPARATE calculation, measured from the
//     .trajectory-wrap element's own position (not the section's, and
//     not gated by the section's dissolve opacity -- that coupling was
//     the bug: the arc stayed dim exactly while it should have been
//     drawing in). It ramps up as the arc's top edge rises into the
//     viewport and then holds at fully-lit, rather than fading back out
//     the way the section dissolve does.
//   - Only reads scroll position (passive listener) -- never calls
//     preventDefault, never sets scrollTop/scrollTo. No snapping, no
//     scroll hijacking.
//   - Skips all scroll-driven animation under prefers-reduced-motion,
//     and the .js-scenes class (which every affected CSS rule is scoped
//     under) is only added once this script actually runs, so a JS
//     failure -- or reduced motion -- leaves every section's content at
//     full opacity in its natural position (a fully readable static
//     layout), and every trajectory at the static resting state set in
//     the markup (arc fully drawn, marker at its resting transform).
//   - Never touches focus or tab order -- dissolved content stays in the
//     normal DOM flow and remains focusable; tabbing or jumping to a nav
//     link scrolls it into view natively, which this script then picks
//     up on the very next frame.
(function () {
    var sections = document.querySelectorAll('.scene-section');
    var contactPulse = document.querySelector('.contact-pulse');

    function clamp01(n) {
        return n < 0 ? 0 : n > 1 ? 1 : n;
    }

    function smoothstep(n) {
        return n * n * (3 - 2 * n);
    }

    var prefersReducedMotion = window.matchMedia &&
        window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // One-shot signal pulse on the Contact dot: fires once, the first
    // time it enters the viewport, regardless of reduced-motion (the
    // global CSS rule already crushes the animation duration for those
    // visitors, so triggering it is harmless and the element itself
    // never moves).
    if (contactPulse && 'IntersectionObserver' in window) {
        var pulseObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-pulsing');
                    pulseObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.6 });
        pulseObserver.observe(contactPulse);
    }

    if (!sections.length || prefersReducedMotion) return;

    document.documentElement.classList.add('js-scenes');

    // Pre-resolve each trajectory's path + progress stroke + marker +
    // total length once. The progress stroke draws along the path as you
    // scroll: its dasharray is set to the path's own length (one
    // continuous dash) and its dashoffset is driven by the trajectory's
    // own entry progress (see trajectoryProgressFor below).
    var trajectories = [];
    document.querySelectorAll('.trajectory-wrap').forEach(function (wrap) {
        var path = wrap.querySelector('.trajectory-path');
        var progress = wrap.querySelector('.trajectory-progress');
        var marker = wrap.querySelector('.trajectory-marker');
        if (path && marker && typeof path.getTotalLength === 'function') {
            var length = path.getTotalLength();
            if (progress) {
                progress.style.strokeDasharray = length;
                progress.style.strokeDashoffset = length;
            }
            trajectories.push({
                wrap: wrap,
                path: path,
                progress: progress,
                marker: marker,
                length: length
            });
        }
    });

    var ticking = false;

    // Section dissolve: one section "in focus" at a time. Fades in as its
    // top edge rises through the viewport, fades out as its bottom edge
    // nears the top. Both windows are sized off the viewport height, so
    // entry/exit timing stays consistent no matter how tall any given
    // section's content is. Because one section's bottom and the next
    // section's top are the same document position, this guarantees
    // overlap at the handoff -- both are already mid-fade (not near zero)
    // at the moment they meet.
    function dissolveProgressFor(rect, vh, fadeZone) {
        var enter = clamp01((vh - rect.top) / fadeZone);
        var exit = clamp01(rect.bottom / fadeZone);
        return smoothstep(Math.min(enter, exit));
    }

    // Trajectory progress: ramps 0 -> 1 as the arc's own top edge rises
    // from the bottom of the viewport into it, reaching fully-lit well
    // before the arc (and the heading just below it) is centered, then
    // holds there -- it does not fade back out while still in view, and
    // is never multiplied by the section's dissolve opacity.
    function trajectoryProgressFor(rect, vh, zone) {
        if (rect.bottom <= 0) return 0;
        return smoothstep(clamp01((vh - rect.top) / zone));
    }

    function update() {
        var vh = window.innerHeight;
        var fadeZone = vh * 0.6;
        var trajectoryZone = vh * 0.5;

        sections.forEach(function (section) {
            var eased = dissolveProgressFor(section.getBoundingClientRect(), vh, fadeZone);
            var shift = (1 - eased) * 14; // small, subtle px shift only

            var contentEls = section.querySelectorAll('.scene-content');
            for (var i = 0; i < contentEls.length; i++) {
                contentEls[i].style.setProperty('--scene-opacity', eased.toFixed(3));
                contentEls[i].style.setProperty('--scene-shift', shift.toFixed(1) + 'px');
            }
        });

        trajectories.forEach(function (t) {
            var eased = trajectoryProgressFor(t.wrap.getBoundingClientRect(), vh, trajectoryZone);
            var point = t.path.getPointAtLength(eased * t.length);
            t.marker.setAttribute('transform', 'translate(' + point.x.toFixed(2) + ',' + point.y.toFixed(2) + ')');
            if (t.progress) {
                t.progress.style.strokeDashoffset = (t.length * (1 - eased)).toFixed(2);
            }
        });

        ticking = false;
    }

    function onScroll() {
        if (!ticking) {
            window.requestAnimationFrame(update);
            ticking = true;
        }
    }

    update();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
})();
