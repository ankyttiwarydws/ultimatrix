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