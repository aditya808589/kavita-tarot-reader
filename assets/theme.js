document.addEventListener('DOMContentLoaded', () => {
  const menuButton = document.querySelector('[data-menu-button]');
  const nav = document.querySelector('[data-nav]');
  menuButton?.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    menuButton.setAttribute('aria-expanded', String(open));
  });

  document.querySelectorAll('[data-tarot-card]').forEach((card) => {
    card.addEventListener('click', () => card.classList.toggle('is-revealed'));
    card.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        card.classList.toggle('is-revealed');
      }
    });
  });
});
