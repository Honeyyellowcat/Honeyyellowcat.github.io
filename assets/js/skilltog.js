
        function toggleSection(id) {
            const section = document.getElementById(id);
            const icon = document.getElementById(`icon-${id}`);
            section.classList.toggle('hidden');
            icon.classList.toggle('rotate-180');
        }