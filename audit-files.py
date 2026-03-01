import os, re

def is_slug(name):
    return bool(re.match(r'^[a-z0-9][a-z0-9\-]*\.md$', name))

def has_title(path):
    try:
        with open(path, encoding='utf-8') as f:
            text = f.read(500)
        if not text.startswith('---'):
            return False
        end = text.find('\n---', 3)
        if end == -1:
            return False
        fm = text[3:end]
        return bool(re.search(r'^title\s*:', fm, re.MULTILINE))
    except:
        return False

no_slug_has_title = []
no_slug_no_title = []
slug_no_title = []

for root, dirs, files in os.walk('content'):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    parts = root.replace('\\', '/').split('/')
    if 'private' in parts:
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        slug_ok = is_slug(f)
        title_ok = has_title(path)
        if not slug_ok and not title_ok:
            no_slug_no_title.append(path)
        elif not slug_ok:
            no_slug_has_title.append(path)
        elif not title_ok:
            slug_no_title.append(path)

print(f"Non-slug filename, has title:     {len(no_slug_has_title)}")
print(f"Non-slug filename, missing title: {len(no_slug_no_title)}")
print(f"Slug filename, missing title:     {len(slug_no_title)}")

print(f"\nSample non-slug (has title):")
for p in no_slug_has_title[:8]:
    print(f"  {os.path.basename(p)}")

print(f"\nSample non-slug (missing title):")
for p in no_slug_no_title[:8]:
    print(f"  {os.path.basename(p)}")

print(f"\nSample slug (missing title):")
for p in slug_no_title[:8]:
    print(f"  {os.path.basename(p)}")
