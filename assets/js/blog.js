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

  if (linkedinRotator) {
    loadLinkedInPost(currentIndex);

    setInterval(() => {
      currentIndex = (currentIndex + 1) % postUrls.length;
      loadLinkedInPost(currentIndex);
    }, 5000);
  }
});
