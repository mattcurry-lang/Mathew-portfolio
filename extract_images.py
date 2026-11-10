"""Pulls the four embedded images out of your OLD portfolio file into ./img/
Usage:  python3 extract_images.py path/to/old-portfolio.html
Writes: img/hero.jpg  img/mattchat.jpg  img/curry-ai.jpg  img/dekut-hub.jpg
Order matters: it expects them in this order in the old file (your photo, then the three project screenshots)."""
import re, sys, base64, os
src = open(sys.argv[1], encoding='utf-8').read()
imgs = re.findall(r'data:image/jpeg;base64,([A-Za-z0-9+/=]+)', src)
names = ['hero', 'mattchat', 'curry-ai', 'dekut-hub']
if len(imgs) < 4:
    sys.exit(f'Found only {len(imgs)} embedded jpegs, expected 4.')
os.makedirs('img', exist_ok=True)
for n, b in zip(names, imgs):
    open(f'img/{n}.jpg', 'wb').write(base64.b64decode(b))
    print('wrote', f'img/{n}.jpg')
