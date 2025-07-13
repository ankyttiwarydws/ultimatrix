
document.getElementById("theme-toggle").addEventListener("click", () => {
  const root = document.documentElement;
  const current = root.getAttribute("data-theme");
  root.setAttribute("data-theme", current === "dark" ? "light" : "dark");
});

function toggleDarkMode() {
  const body = document.body;
  body.classList.toggle("dark-mode");
  localStorage.setItem("theme", body.classList.contains("dark-mode") ? "dark" : "light");
}

// Auto-apply saved mode
document.addEventListener("DOMContentLoaded", () => {
  const saved = localStorage.getItem("theme");
  if (saved === "dark") document.body.classList.add("dark-mode");
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