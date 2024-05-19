
            const mediaElements = document.querySelectorAll('.photo img, .photo video');
    
            mediaElements.forEach(media => {
                media.addEventListener('click', () => {
                    mediaElements.forEach(m => {
                        if (m !== media) {
                            m.classList.remove('expanded');
                        }
                    });
                    media.classList.toggle('expanded');
                });
            });