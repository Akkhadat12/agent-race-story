(() => {
  const scenes = [...document.querySelectorAll('.scene')];
  const announcement = document.getElementById('scene-announcement');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let current = 0;
  let transitioning = false;
  let timer = null;

  for (const image of document.querySelectorAll('.art')) {
    if (image.loading !== 'eager') {
      const preload = new Image();
      preload.src = image.src;
    }
  }

  function announce() {
    announcement.textContent = scenes[current].getAttribute('aria-label') || '';
  }

  function activate(index) {
    for (let i = 0; i < scenes.length; i++) {
      scenes[i].classList.toggle('active', i === index);
      scenes[i].classList.remove('leaving');
      scenes[i].setAttribute('aria-hidden', i === index ? 'false' : 'true');
      scenes[i].inert = i !== index;
    }
    current = index;
    announce();
  }

  function advance() {
    if (transitioning || current >= scenes.length - 1) return;
    const previous = scenes[current];
    const next = current + 1;
    transitioning = true;
    previous.classList.remove('active');
    previous.classList.add('leaving');
    previous.setAttribute('aria-hidden', 'true');
    previous.inert = true;
    current = next;
    const incoming = scenes[current];
    incoming.classList.add('active');
    incoming.setAttribute('aria-hidden', 'false');
    incoming.inert = false;
    announce();
    clearTimeout(timer);
    timer = setTimeout(() => {
      previous.classList.remove('leaving');
      transitioning = false;
      timer = null;
    }, reducedMotion.matches ? 150 : 980);
  }

  function returnToCover() {
    if (current === 0 && !transitioning) return;
    clearTimeout(timer);
    timer = null;
    transitioning = false;
    activate(0);
  }

  function isEditable(element) {
    return !!element?.closest?.('input,textarea,select,[contenteditable=""],[contenteditable="true"],[role="textbox"]');
  }

  document.querySelectorAll('[data-advance]').forEach(button => {
    button.addEventListener('click', advance);
  });

  window.addEventListener('keydown', event => {
    if (event.repeat || event.ctrlKey || event.metaKey || event.altKey || event.shiftKey || isEditable(event.target)) return;
    if (event.code === 'KeyR') {
      event.preventDefault();
      returnToCover();
      return;
    }
    if (event.code === 'Space') {
      if (event.target?.closest?.('a,button:not([data-advance]),[role="button"]:not([data-advance])')) return;
      event.preventDefault();
      advance();
    }
  });

  activate(0);
})();
