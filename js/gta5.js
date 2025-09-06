document.querySelectorAll('.howto-tab-btn').forEach(function (btn) {
  btn.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelectorAll('.howto-tab-btn').forEach(function (b) { b.classList.remove('active'); });
    btn.classList.add('active');
    var tab = btn.getAttribute('data-tab');
    document.querySelectorAll('.howto-tab-content').forEach(function (tc) {
      tc.style.display = 'none';
    });
    document.getElementById('tab-' + tab).style.display = 'block';
  });
});

// Enhanced search: show matching gta5 cards and switch to the correct tab if needed
document.getElementById('searchBar').addEventListener('input', function (e) {
  const query = e.target.value.toLowerCase();
  const cards = document.querySelectorAll('.gta5-card');
  let foundTab = null;

  cards.forEach(card => {
    const text = card.textContent.toLowerCase();
    if (text.includes(query)) {
      card.style.display = '';
      // Find parent tab for the first match
      if (!foundTab) {
        let tabContent = card.closest('.howto-tab-content');
        if (tabContent && tabContent.id) {
          foundTab = tabContent.id.replace('tab-', '');
        }
      }
    } else {
      card.style.display = 'none';
    }
  });

  // If a match is found in another tab, switch to that tab
  if (foundTab) {
    // Hide all tabs
    document.querySelectorAll('.howto-tab-content').forEach(tab => {
      tab.style.display = 'none';
    });
    // Remove active class from all tab buttons
    document.querySelectorAll('.howto-tab-btn').forEach(btn => {
      btn.classList.remove('active');
    });
    // Show the found tab
    const showTab = document.getElementById('tab-' + foundTab);
    if (showTab) showTab.style.display = 'block';
    // Set active class on the corresponding tab button
    const activeBtn = document.querySelector('.howto-tab-btn[data-tab="' + foundTab + '"]');
    if (activeBtn) activeBtn.classList.add('active');
  }
  // If no query, reset all cards and show the active tab only
  if (!query) {
    document.querySelectorAll('.gta5-card').forEach(card => card.style.display = '');
    // Show only the active tab
    document.querySelectorAll('.howto-tab-content').forEach(tab => tab.style.display = 'none');
    const activeBtn = document.querySelector('.howto-tab-btn.active');
    if (activeBtn) {
      const tab = activeBtn.getAttribute('data-tab');
      const showTab = document.getElementById('tab-' + tab);
      if (showTab) showTab.style.display = 'block';
    }
  }
});