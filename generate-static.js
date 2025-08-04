
const fs = require('fs');
const path = require('path');

// Load your JSON data
const articles = require('./data/news/news-data.json');

function slugify(title) {
  return title
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9\s-]/g, '') // Remove special characters
    .replace(/\s+/g, '-')         // Replace spaces with hyphens
    .replace(/-+/g, '-');         // Collapse multiple hyphens
}

// Template function for generating HTML
function generateHTML(article) {
  return `<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>${article.title} | Ultimatix</title>
  <link rel="stylesheet" href="/css/style.css" />
  <link rel="stylesheet" href="/css/blogs.css" />
  <link rel="stylesheet" href="/css/news-sports.css" />
  <link rel="stylesheet" href="/css/news-sports-pages.css" />
  <script src="/js/script.js" defer></script>
</head>
<body>
  <div id="header"></div>
  <main>
    <section class="section-main">
      <article>
        <h1>${article.title}</h1>
        <h2>${article.shortDesc}</h2>
        <p class="timestamp">${article.timestamp}</p>
        <p>${article.synopsis}</p>
      </article>
      <section class="news-media">
        <img src="${article.imageSrc}" alt="${article.imageAlt}" />
      </section>
      <section class="news-full-story">
        <h2>Full Story</h2>
        ${article.fullStory.map(p => `<p>${p}</p>`).join('\n')}
        <p><a href="${article.author}">Read Here: ${article.author}</a></p>
      </section>
      <section class="article-footer">
        <p>🖊️ Written by: <strong>${article.author}</strong></p>
        <p>📡 Source: <a href="${article.sourceURL}">${article.sourceURL}</a></p>
        <p>🎓 Image Credit: <em>${article.imageCredit}</em></p>
        <p>📜 Legal Disclaimer: This article is for informational purposes only. All facts are accurate to the best of our knowledge at time of publication. Reproduction without permission is prohibited.</p>
      </section>
    </section>
  </main>
  <div id="footer"></div>
</body>
</html>`;
}
const pageIndex = [];
// Write each file
articles.forEach((article, index) => {
  const category = article.category.toLowerCase();
  const date = article.date; // Format: YYYY-MM-DD
  const slug = slugify(article.title);
  const folderPath = path.join(__dirname, 'news', category, date);
  fs.mkdirSync(folderPath, { recursive: true });

  const filePath = path.join(folderPath, `${slug}.html`);
  fs.writeFileSync(filePath, generateHTML(article));


  pageIndex.push({
    url: `/news/${category}/${date}/${slug}.html`
  });

  // const filename = `article-${index + 1}.html`;
  // const htmlContent = generateHTML(article);
  // fs.writeFileSync(path.join(__dirname, 'static', filename), htmlContent);
  // console.log(`✅ ${filename} created`);
});

fs.writeFileSync(
  JSON_FILE = path.join('data', 'news', 'news-urls.json'),
  // path.join(__dirname, 'news-pages.json'),
  JSON.stringify(pageIndex, null, 2)
);
console.log('news-urls.json created');