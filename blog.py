"""
A stupid simple blog generator.
"""
import shutil
from collections import namedtuple
from pathlib import Path
from string import Template


# Directories
POSTS_DIR = Path('posts')
TEMPLATE = Template(Path('layout.html').open().read())
STATIC_DIR = Path('static')
SITE_DIR = Path('_site')
SITE_POSTS_DIR = SITE_DIR / 'posts'


# "Models"
Post = namedtuple('Post', ['filename', 'meta', 'content'])


def collect_posts():
    return list(POSTS_DIR.glob('*.txt'))


def process_meta(meta_raw):
    meta = {}
    meta_lines = meta_raw.strip().split('\n')
    for line in meta_lines:
        k, v = line.split(':')
        meta[k.strip()] = v.strip()
    return meta


def process_content(content_raw):
    content_lines = content_raw.strip().split('\n\n')
    title, post_content = content_lines[0], '\n'.join(f'<p>{line}</p>' for line in content_lines[1:])
    return f'<h2 class="post-title">{title}</h2>\n' + post_content


def process_posts(post_files):
    posts = []
    for post in post_files:
        with post.open() as pf:
            pf_content = pf.read()
        meta_raw, content_raw = pf_content.split('--')
        fname = post.name.replace('.txt', '.html')
        p = Post(fname, process_meta(meta_raw), process_content(content_raw))
        posts.append(p)
    return posts


def write_files(posts):
    SITE_POSTS_DIR.mkdir()
    for post in posts:
        with (SITE_POSTS_DIR / post.filename).open('w') as of:
            title = post.meta.get('title')
            body_class = post.meta.get('body_class', 'post'),
            of.write(TEMPLATE.substitute(title=title, body_class=body_class, content=post.content))
    shutil.copytree(STATIC_DIR, SITE_DIR / 'static')


def write_index(posts):
    links = {}
    for post in posts:
        href = f'posts/{post.filename}'
        dt = post.meta.get('date')
        title = post.meta.get('title')
        links[dt] = f'<a href="{href}">{dt}</a>: {title}'

    sorted_posts = dict(sorted(links.items(), reverse=True))
    post_list = '\n'.join(f'<li>{link}</li>' for link in sorted_posts.values())

    with (SITE_DIR / 'index.html').open('w') as of:
        content = '\n'.join(['<ul>', post_list, '</ul>'])
        of.write(TEMPLATE.substitute(title='Archive', body_class='index', content=content))


def write_posts(posts):
    write_files(posts)
    write_index(posts)


if __name__ == '__main__':
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()
    write_posts(process_posts(collect_posts()))
    raise SystemExit(0)

