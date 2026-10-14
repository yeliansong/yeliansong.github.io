(() => {
  const body = document.body;
  const saved = localStorage.getItem('blog-theme');
  if (saved === 'dark' || (!saved && matchMedia('(prefers-color-scheme: dark)').matches)) body.classList.add('dark');
  document.querySelector('.theme-toggle')?.addEventListener('click', () => {
    body.classList.toggle('dark');
    localStorage.setItem('blog-theme', body.classList.contains('dark') ? 'dark' : 'light');
  });
  const search = document.querySelector('#post-search');
  const posts = [...document.querySelectorAll('#post-grid .post-card')];
  const count = document.querySelector('#post-count');
  const update = () => {
    const query = search?.value.trim().toLowerCase() || '';
    let visible = 0;
    posts.forEach(post => { const show = post.dataset.search.includes(query); post.hidden = !show; if (show) visible++; });
    if (count) count.textContent = `${visible} 篇`;
  };
  search?.addEventListener('input', update); update();
  const tocLinks = [...document.querySelectorAll('.article-toc a')];
  const sections = tocLinks.map(link => document.querySelector(link.getAttribute('href'))).filter(Boolean);
  if (sections.length) {
    const setActive = id => tocLinks.forEach(link => link.classList.toggle('active', link.getAttribute('href') === `#${id}`));
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (visible[0]) setActive(visible[0].target.id);
    }, {rootMargin: '-15% 0px -70% 0px'});
    sections.forEach(section => observer.observe(section));
    setActive(sections[0].id);
  }
  const articleImages = [...document.querySelectorAll('.prose img')];
  if (articleImages.length) {
    const lightbox = document.createElement('button');
    lightbox.className = 'image-lightbox';
    lightbox.type = 'button';
    lightbox.setAttribute('aria-label', '关闭图片预览');
    lightbox.innerHTML = '<img alt="">';
    document.body.append(lightbox);
    const preview = lightbox.querySelector('img');
    const close = () => {
      lightbox.classList.remove('open');
      body.classList.remove('lightbox-open');
      preview.removeAttribute('src');
    };
    articleImages.forEach(img => {
      img.classList.add('zoomable-image');
      img.addEventListener('click', () => {
        preview.src = img.currentSrc || img.src;
        preview.alt = img.alt || '文章图片预览';
        lightbox.classList.add('open');
        body.classList.add('lightbox-open');
      });
    });
    lightbox.addEventListener('click', close);
    document.addEventListener('keydown', event => { if (event.key === 'Escape') close(); });
  }
})();
