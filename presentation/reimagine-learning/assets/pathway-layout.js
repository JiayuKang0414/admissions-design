(() => {
  const pathway = document.getElementById('learning-pathway');
  if (!pathway || !window.customElements) return;

  const installSpacing = () => {
    const root = pathway.shadowRoot;
    if (!root || root.querySelector('[data-learning-pathway-spacing]')) return;

    const style = document.createElement('style');
    style.setAttribute('data-learning-pathway-spacing', '');
    style.textContent = `
      :host(#learning-pathway) .pathway-container-lock-wrapper {
        min-height: 0;
      }
    `;
    root.appendChild(style);
  };

  // Reapply after native lazy initialization or a component rerender.
  pathway.addEventListener('umdComponent:ready', installSpacing);
  customElements.whenDefined('umd-element-pathway').then(installSpacing);
})();
