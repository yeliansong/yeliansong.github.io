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
})();
