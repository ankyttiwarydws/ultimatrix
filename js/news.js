const searchBar = document.getElementById("searchBar");
const categoryButtons = document.querySelectorAll(".category-btn");
const newsFeed = document.querySelector(".news-feed");
const articles = Array.from(document.querySelectorAll(".news-item"));

// Sort by newest first
articles.sort((a, b) => {
    const timeA = new Date(a.querySelector(".timestamp").textContent);
    const timeB = new Date(b.querySelector(".timestamp").textContent);
    return timeB - timeA;
});
articles.forEach(article => newsFeed.appendChild(article));

function getActiveCategories() {
    return Array.from(categoryButtons)
        .filter(btn => btn.classList.contains("active"))
        .map(btn => btn.getAttribute("data-category").toLowerCase());
}

function applyFilters() {
    const query = searchBar.value.toLowerCase();
    const selectedCategories = getActiveCategories();

    articles.forEach(article => {
        const title = article.querySelector("h2").textContent.toLowerCase();
        const description = article.querySelector("p:not(.timestamp)").textContent.toLowerCase();
        const category = article.getAttribute("data-category").toLowerCase();

        const keywordMatch = title.includes(query) || description.includes(query);
        const categoryMatch = selectedCategories.includes(category);

        article.style.display = (keywordMatch && categoryMatch) ? "block" : "none";
    });
}

searchBar.addEventListener("input", applyFilters);

searchBar.addEventListener("input", () => {
    const query = document.getElementById("searchBar").value.toLowerCase();

    renderedArticles.forEach(article => {
        const title = article.querySelector("h2")?.textContent.toLowerCase() || "";
        const description = article.querySelector(".summary")?.textContent.toLowerCase() || "";
        // const timestamp = article.querySelector(".timestamp")?.textContent.toLowerCase() || "";
        const match = title.includes(query) || description.includes(query);// || timestamp.includes(query)
        article.style.display = match ? "block" : "none";
    });
});
const articleList = [];
// const articleList = require('./data/news/news-urls.json');
// import fs from 'fs/promises';

// const rawData = await fs.readFile('/data/news/news-urls.json', 'utf-8');
// const articleList = JSON.parse(rawData);
// print( articleList)
fetch('/data/news/news-urls.json')
  .then(response => response.json())
  .then(urlsData => {
    articleList = urlsData.map(item => item.url);
    console.log(articleList); // You can render these or load content dynamically
  })
  .catch(err => console.error('Fetch error:', err));
  
// print( articleList)

const renderedArticles = [];
const headlinesSection = document.getElementById("headlines-section");
const todaySection = document.getElementById("today-section");
const yesterdaySection = document.getElementById("yesterday-section");
const earlierSection = document.getElementById("earlier-section");

function getDateOnly(dateStr) {
    return new Date(dateStr).toISOString().split("T")[0]; // "YYYY-MM-DD"
}

function lazyLoadArticlesFromJSON(articleData) {
    const today = getDateOnly(new Date());
    const yesterday = getDateOnly(new Date(Date.now() - 86400000));

    // Step 1: Create placeholders
    articleData.forEach(item => {
        const placeholder = document.createElement("article");
        placeholder.classList.add("news-placeholder");
        placeholder.setAttribute("data-url", item.url);

        // Insert into headlines as initial observation target
        headlinesSection.appendChild(placeholder);
    });

    // Step 2: Lazy Load Articles
    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const url = el.getAttribute("data-url");
                if (el.dataset.loaded) return;
                el.dataset.loaded = "true";

                fetch(url)
                    .then(res => res.text())
                    .then(html => {
                        const parser = new DOMParser();
                        const doc = parser.parseFromString(html, "text/html");

                        const title = doc.querySelector("#news-title")?.textContent || "Untitled";
                        const desc = doc.querySelector("#news-short-desc")?.textContent || "";
                        const timestampRaw = doc.querySelector("#news-timestamp")?.textContent || "";
                        const synopsis = doc.querySelector("#news-synopsis")?.textContent || "";
                        const articleTag = doc.querySelector("#news-article");
                        const isHeadline = articleTag?.getAttribute("data-headline") === "true";
                        const publishedDate = getDateOnly(timestampRaw);

                        el.classList.remove("news-placeholder");
                        el.classList.add("news-item");
                        el.innerHTML = `
                <a href="${url}" target="_blank"><h2>${title}</h2></a>
                <p class="timestamp">${timestampRaw}</p>
                <p class="summary">${desc}</p>
                <div class="extra-content" style="max-height: 0; overflow: hidden; opacity: 0; transition: max-height 0.5s ease, opacity 0.5s ease;">
                  <p>${synopsis}</p>
                  <a href="${url}" target="_blank"><button class="read-full-btn">Read Full Story</button></a>
                </div>
                <button class="read-more-btn">Read More</button>
              `;

                        renderedArticles.push(el);

                        // ✅ Insert into correct section
                        if (isHeadline) {
                            headlinesSection.appendChild(el);
                        } else if (publishedDate === today) {
                            todaySection.appendChild(el);
                        } else if (publishedDate === yesterday) {
                            yesterdaySection.appendChild(el);
                        } else {
                            earlierSection.appendChild(el);
                        }
                    })
                    .catch(err => {
                        el.innerHTML = `<p>❗ Failed to load article.</p>`;
                        console.error("Error fetching:", url, err);
                    });

                obs.unobserve(el);
            }
        });
    }, { rootMargin: "0px 0px 200px 0px" });

    document.querySelectorAll(".news-placeholder").forEach(el => observer.observe(el));
}

// Step 3: Event Delegation for Read More button
document.querySelector("#dynamic-news-feed").addEventListener("click", (e) => {
    if (e.target.classList.contains("read-more-btn")) {
        const articleEl = e.target.closest(".news-item");
        const extra = articleEl.querySelector(".extra-content");

        document.querySelectorAll(".news-item .extra-content").forEach(section => {
            if (section !== extra) {
                section.classList.remove("expanded");
                section.style.maxHeight = "0";
                section.style.opacity = "0";
                section.parentElement.querySelector(".read-more-btn").textContent = "Read More";
            }
        });

        const isExpanded = extra.classList.contains("expanded");
        if (!isExpanded) {
            extra.classList.add("expanded");
            extra.style.maxHeight = "500px";
            extra.style.opacity = "1";
            e.target.textContent = "Show Less";
        } else {
            extra.classList.remove("expanded");
            extra.style.maxHeight = "0";
            extra.style.opacity = "0";
            e.target.textContent = "Read More";
        }
    }
});

// 🚀 Kickstart on load
window.addEventListener("DOMContentLoaded", () => {
    lazyLoadArticlesFromJSON(articleList);
});