document.addEventListener('DOMContentLoaded', () => {

  // -------- LinkedIn Rotator --------
  const linkedinRotator = document.getElementById('linkedin-rotator');
  const postUrls = [
    "https://www.linkedin.com/embed/feed/update/urn:li:share:7376982482161893376",
    "https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7324119910182215680",
    "https://www.linkedin.com/embed/feed/update/urn:li:share:7351335245255802881",
    "https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7363603029893242880",
    "https://www.linkedin.com/embed/feed/update/urn:li:share:7161103067940016128",
    "https://www.linkedin.com/embed/feed/update/urn:li:share:7376982482161893376",
    "https://www.linkedin.com/embed/feed/update/urn:li:share:7235483681610461184",
    "https://www.linkedin.com/embed/feed/update/urn:li:share:7178473338766340096"
  ];

  let currentIndex = 0;

  function loadLinkedInPost(index) {
    linkedinRotator.innerHTML = `<iframe class="linkedin-post"
      src="${postUrls[index]}"
      height="400" width="100%" frameborder="0" allowfullscreen
      title="LinkedIn Post"></iframe>`;
  }

  loadLinkedInPost(currentIndex);

  setInterval(() => {
    currentIndex = (currentIndex + 1) % postUrls.length;
    loadLinkedInPost(currentIndex);
  }, 5000);


  // -------- Blog Slider Controls --------
  const slider = document.getElementById('blog-slider');
  const wrapper = document.getElementById('blog-slider-wrapper');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');

  let scrollPosition = 0;

  function getPanelWidth() {
    const panel = slider.querySelector('.panel');
    return panel ? panel.offsetWidth + 32 : 0; // gap-8 = 2rem = 32px
  }

  function updateSlider() {
    slider.style.transform = `translateX(-${scrollPosition}px)`;
  }

  nextBtn.addEventListener('click', () => {
    const panelWidth = getPanelWidth();
    const maxScroll = slider.scrollWidth - wrapper.offsetWidth;

    if (scrollPosition < maxScroll) {
      scrollPosition = Math.min(scrollPosition + panelWidth, maxScroll);
      updateSlider();
    }
  });

  prevBtn.addEventListener('click', () => {
    const panelWidth = getPanelWidth();

    if (scrollPosition > 0) {
      scrollPosition = Math.max(scrollPosition - panelWidth, 0);
      updateSlider();
    }
  });
});
