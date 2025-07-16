

// Unified dark mode toggle for all pages
function toggleDarkMode() {
  const isDark = document.body.classList.toggle('dark-mode');
  localStorage.setItem('ultimatrix-dark-mode', isDark ? 'dark' : 'light');
}

// On page load, apply dark mode if set in localStorage
document.addEventListener('DOMContentLoaded', function() {
  const mode = localStorage.getItem('ultimatrix-dark-mode');
  if (mode === 'dark') {
    document.body.classList.add('dark-mode');
  } else {
    document.body.classList.remove('dark-mode');
  }
});


// const themeToggle = document.getElementById("theme-toggle");

// function applyTheme(theme) {
//   if (theme === "dark") {
//     document.body.classList.add("dark-mode");
//   } else {
//     document.body.classList.remove("dark-mode");
//   }
//   localStorage.setItem("theme", theme);
// }

// function getPreferredTheme() {
//   const saved = localStorage.getItem("theme");
//   if (saved) return saved;
//   // Fallback to system preference
//   return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
// }

// themeToggle.addEventListener("click", () => {
//   const isDark = document.body.classList.toggle("dark-mode");
//   localStorage.setItem("theme", isDark ? "dark" : "light");
// });

// document.addEventListener("DOMContentLoaded", () => {
//   applyTheme(getPreferredTheme());
// });


// const themeToggle = document.getElementById("theme-toggle");

// function applyTheme(theme) {
//   if (theme === "dark") {
//     document.body.classList.add("dark-mode");
//   } else {
//     document.body.classList.remove("dark-mode");
//   }
//   localStorage.setItem("theme", theme);
// }

// function getPreferredTheme() {
//   const saved = localStorage.getItem("theme");
//   if (saved) return saved;
//   return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
// }

// themeToggle.addEventListener("click", () => {
//   const isDark = !document.body.classList.contains("dark-mode");
//   applyTheme(isDark ? "dark" : "light");
// });

// document.addEventListener("DOMContentLoaded", () => {
//   applyTheme(getPreferredTheme());
// });