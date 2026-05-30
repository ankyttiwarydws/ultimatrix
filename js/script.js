// Unified dark mode toggle for all pages
function toggleDarkMode() {
  const isDark = document.body.classList.toggle('dark-mode');
  localStorage.setItem('ultimatrix-dark-mode', isDark ? 'dark' : 'light');
  updateToggleIcon(isDark);
}

function updateToggleIcon(isDark) {
  const moon = document.getElementById('moon-icon');
  const sun = document.getElementById('sun-icon');
  if (moon && sun) {
    if (isDark) {
      moon.style.display = 'none';
      sun.style.display = 'block';
    } else {
      moon.style.display = 'block';
      sun.style.display = 'none';
    }
  }
}

// On page load, apply dark mode if set in localStorage
document.addEventListener('DOMContentLoaded', function () {
  const mode = localStorage.getItem('ultimatrix-dark-mode');
  if (mode === 'dark') {
    document.body.classList.add('dark-mode');
  } else {
    document.body.classList.remove('dark-mode');
  }
});

fetch('/header.html')
  .then(res => res.text())
  .then(data => {
    document.getElementById('header').innerHTML = data;
    const isDark = document.body.classList.contains('dark-mode');
    updateToggleIcon(isDark);
  });

fetch('/footer.html')
  .then(res => res.text())
  .then(data => document.getElementById('footer').innerHTML = data);