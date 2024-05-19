
        document.querySelectorAll('.code-box').forEach(box => {
            box.addEventListener('click', () => {
                box.classList.toggle('expanded');
            });
        });