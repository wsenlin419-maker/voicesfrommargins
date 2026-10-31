# Margins & Meaning · 边缘与意义

An interdisciplinary research platform that brings together young students and scholars across disciplines — documenting underrepresented discourses and studying the social structures that shape language, identity, inequality, and public policy.

🌐 **Live site**: https://marginsmeaning.org

---

## About

Margins & Meaning ("Voices from the Margins Project") is an independent, nonpartisan research platform. We connect young researchers across linguistics, psychology, sociology, discourse analysis, and quantitative & qualitative methods, documenting voices and discourses that are underrepresented in public life.

## Preview

<!-- TODO: 把下面的 screenshot.png 换成真实截图。
     方式一：把截图存成 screenshot.png 放进本仓库；
     方式二：用 picture 仓库的直链，例如
     https://raw.githubusercontent.com/wsenlin419-maker/picture/main/xxx.png -->
![Margins & Meaning — site preview](screenshot.png)

## Features

- 🌐 Bilingual (English / 中文) with one-click switching
- 🎙️ **Voices Archive** — field recordings with metadata, transcriptions & ethics notes
- 🗺️ **Interactive maps** (ECharts) — dialect regions & ethnic minorities of China
- 📊 **Data & Insights** — visual framing dataset
- ✍️ Research / Writing / Field Notes / Blog sections
- 🔍 Full-text search with keyword highlighting
- 🌙 Dark mode · 📥 Downloads · 💬 Comments (Giscus) · 📬 Newsletter (Formspree)

## Tech Stack

- Plain HTML + [Tailwind CSS](https://tailwindcss.com) (CDN) + vanilla JavaScript
- [ECharts](https://echarts.apache.org) for maps
- [marked.js](https://marked.js.org) for Markdown rendering
- [Lucide](https://lucide.dev) icons
- [Giscus](https://giscus.app) comments (GitHub Discussions)
- [Formspree](https://formspree.io) forms
- [Contentful](https://contentful.com) headless CMS

## Project Structure

```
index.html          # the entire site (single-page app)
china-geo.json      # map geometry data
favicon.png         # 32×32 icon
favicon-16.png      # 16×16 icon
favicon-48.png      # 48×48 icon
README.md
```

## Content Management

Site content lives in **Contentful** (articles, team members, downloads, voice entries). Edit content in Contentful — no code changes needed. The site fetches the Contentful Delivery API at runtime.

## Deployment

This repository is served by **GitHub Pages**. To update the site:

1. Edit `index.html` locally
2. Push `index.html` + `china-geo.json` + `favicon*.png`
3. GitHub Pages redeploys automatically to https://marginsmeaning.org

## Contributing

We welcome student collaborators and early-career researchers. See the [Opportunities](https://marginsmeaning.org) section on the site, or contact us below.

## Contact

- Email: marginsmeaning@163.com
- Site: https://marginsmeaning.org

## License

© Margins & Meaning. All content is provided for **non-commercial, educational, and research use only**. You may read, share, and cite with full attribution (author, title, *Margins & Meaning*, date, URL). Commercial use or substantial reproduction requires prior written permission — contact marginsmeaning@163.com.
