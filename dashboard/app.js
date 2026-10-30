
const CATEGORIES = ['PRIMARY', 'WORKFLOW', 'REFERENCE'];

async function loadSites() {
  const res = await fetch('data/sites.json');
  const sites = await res.json();
  
  const dashboard = document.getElementById('dashboard');
  
  CATEGORIES.forEach(cat => {
    const section = document.createElement('div');
    section.innerHTML = `<h2 style="grid-column:1/-1;margin:20px 0 10px;border-bottom:1px solid #222">${cat}</h2>`;
    dashboard.appendChild(section);
    
    sites.filter(s => s.category === cat).forEach(site => {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <img src="https://www.google.com/s2/favicons?domain=${new URL(site.url).hostname}&sz=64" alt="">
        <div class="category">${site.category}</div>
        <h3>${site.name}</h3>
        <div class="desc">${site.description}</div>
        <a href="${site.url}" target="_blank">OPEN</a>
      `;
      dashboard.appendChild(card);
    });
  });
}

document.getElementById('search').addEventListener('input', e => {
  const q = e.target.value.toLowerCase();
  document.querySelectorAll('.card').forEach(c => {
    c.style.display = c.textContent.toLowerCase().includes(q) ? '' : 'none';
  });
});

loadSites();
