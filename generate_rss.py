# -*- coding: utf-8 -*-
import json, urllib.request, html, time, re
from datetime import datetime, timezone
from email.utils import format_datetime

SPACE = 'egroy8ctp4pz'
TOKEN = 'EwsY0dizhi2jZi8YvMXlxEK7kTTSVS5hstk6oyWg6NU'
SITE = 'https://marginsmeaning.org'

def g(v):
    if isinstance(v, dict):
        return v.get('en-US') or v.get('zh-CN') or ''
    return v or ''

def fetch(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(1.5 * (i + 1))

def normalize_url(u):
    u = (u or '').strip()
    m = re.match(r'https?://github\.com/([^/]+)/([^/]+)/blob/(.+)$', u)
    if m:
        u = f"https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}/{m.group(3)}"
    if u.startswith('//'):
        u = 'https:' + u
    if ' ' in u or '"' in u:
        return ''
    return u

def mime_from_ext(u):
    u = u.lower().split('?')[0]
    for ext, m in [('.jpg','image/jpeg'),('.jpeg','image/jpeg'),('.png','image/png'),
                   ('.gif','image/gif'),('.webp','image/webp'),('.bmp','image/bmp'),
                   ('.avif','image/avif'),('.svg','image/svg+xml')]:
        if u.endswith(ext):
            return m
    return 'image/jpeg'

data = fetch(f"https://cdn.contentful.com/spaces/{SPACE}/environments/master/entries"
             f"?content_type=article&access_token={TOKEN}&locale=*&order=-sys.createdAt")

assets = {}
if 'includes' in data and 'Asset' in data['includes']:
    for a in data['includes']['Asset']:
        try:
            fu = a['fields']['file']['en-US']['url']
            ct = a['fields']['file']['en-US'].get('contentType', 'image/jpeg')
            assets[a['sys']['id']] = (normalize_url(fu), ct)
        except Exception:
            pass

items = []
for it in data.get('items', []):
    f = it.get('fields', {})
    slug = g(f.get('slug')); title = g(f.get('title')); excerpt = g(f.get('excerpt')); pub = g(f.get('publishDate'))
    if not slug or not title:
        continue
    cover = f.get('coverUrl')
    cu = g(cover) if isinstance(cover, dict) else (cover or '')
    ci = f.get('coverImage'); cid = None
    if isinstance(ci, dict) and 'sys' in ci.get('en-US', {}):
        cid = ci['en-US']['sys'].get('id')
    if cu:
        img = normalize_url(cu); mime = mime_from_ext(img)
    elif cid and cid in assets:
        img, mime = assets[cid]
    else:
        img, mime = '', 'image/jpeg'
    dt = None
    try:
        dt = datetime.strptime(pub[:10], '%Y-%m-%d').replace(tzinfo=timezone.utc)
    except Exception:
        pass
    items.append((pub or '', title, slug, excerpt, format_datetime(dt) if dt else '', img, mime))

items.sort(key=lambda x: x[0], reverse=True)

def esc(s):
    return html.escape(s or '', quote=True)

out = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/"><channel>']
out.append(f'<title>{esc("Margins & Meaning")}</title>')
out.append(f'<link>{SITE}</link>')
out.append(f'<description>{esc("Language, identity, inequality, and policy research.")}</description>')
out.append('<language>en</language>')
for pub, title, slug, excerpt, pubdate, img, mime in items:
    link = f"{SITE}/#article/{slug}"
    out.append('<item>')
    out.append(f'<title>{esc(title)}</title>')
    out.append(f'<link>{esc(link)}</link>')
    out.append(f'<guid isPermaLink="false">{esc(slug)}</guid>')
    if pubdate:
        out.append(f'<pubDate>{pubdate}</pubDate>')
    out.append(f'<description><![CDATA[{excerpt}]]></description>')
    if img:
        out.append(f'<media:content url="{esc(img)}" medium="image" type="{mime}" />')
        out.append(f'<media:thumbnail url="{esc(img)}" />')
        out.append(f'<enclosure url="{esc(img)}" type="{mime}" />')
    out.append('</item>')
out.append('</channel></rss>')

open('rss.xml', 'w', encoding='utf-8').write('\n'.join(out))
print('done', len(items), 'items -> Desktop/rss.xml')
