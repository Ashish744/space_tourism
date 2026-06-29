import re
from pathlib import Path

canonical_footer = '''<footer style="background:linear-gradient(180deg, #02050d 0%, #0a0f25 55%, #101a3d 100%); border-top:1px solid rgba(255,255,255,0.08); padding:72px 24px 32px; position:relative; overflow:hidden;">
    <div style="position:absolute; inset:auto 0 0 0; height:1px; background:linear-gradient(90deg, transparent, rgba(106,61,232,0.5), transparent);"></div>
    <div style="max-width:1180px; margin:0 auto; display:grid; grid-template-columns:1.2fr 0.9fr 0.9fr 0.9fr 1fr; gap:28px; align-items:start;">
      <div>
        <a href="index.html" style="display:inline-flex; align-items:center; justify-content:center; width:220px; height:72px; background:rgba(139, 156, 200, 0.06); border:1px dashed rgba(139, 156, 200, 0.28); border-radius:8px; padding:10px 14px;">
          <img src="logo (1).webp" alt="CosmosVoyage logo" style="height:100%; width:auto; object-fit:contain; display:block;">
        </a>
        <p style="margin-top:18px; font-size:14px; color:#8B9CC8; line-height:1.8; max-width:320px;">Where premium space travel meets precision planning, comfort, and unforgettable views beyond the horizon.</p>
        <div style="display:flex; gap:10px; margin-top:22px;">
          <a href="404.html" style="width:40px; height:40px; display:flex; align-items:center; justify-content:center; border-radius:999px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08);"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#8B9CC8" stroke-width="1.5"><path d="M6 6L18 18M18 6L6 18"/></svg></a>
          <a href="404.html" style="width:40px; height:40px; display:flex; align-items:center; justify-content:center; border-radius:999px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08);"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#8B9CC8" stroke-width="1.5"><path d="M6 8h12M6 12h12M6 16h8"/><rect x="2" y="4" width="20" height="16" rx="3"/></svg></a>
          <a href="404.html" style="width:40px; height:40px; display:flex; align-items:center; justify-content:center; border-radius:999px; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08);"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#8B9CC8" stroke-width="1.5"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37Z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
        </div>
      </div>
      <div>
        <h4 style="font-family:'Space Mono', monospace; font-size:10px; color:#E8EDFF; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:16px;">Explore</h4>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin:0; padding:0;">
          <li><a href="destination.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Destinations</a></li>
          <li><a href="tourpackages.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Packages</a></li>
          <li><a href="gallery.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Gallery</a></li>
          <li><a href="about.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">About us</a></li>
          <li><a href="contact.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4 style="font-family:'Space Mono', monospace; font-size:10px; color:#E8EDFF; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:16px;">Mission</h4>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin:0; padding:0;">
          <li><a href="404.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">ISS Expedition</a></li>
          <li><a href="404.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Moon Orbit</a></li>
          <li><a href="404.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Mars Flyby</a></li>
          <li><a href="404.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Private Charter</a></li>
        </ul>
      </div>
      <div>
        <h4 style="font-family:'Space Mono', monospace; font-size:10px; color:#E8EDFF; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:16px;">Support</h4>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin:0; padding:0;">
          <li><a href="404.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Help Center</a></li>
          <li><a href="404.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Booking Process</a></li>
          <li><a href="404.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Safety Info</a></li>
          <li><a href="404.html" style="font-size:14px; color:#8B9CC8; text-decoration:none;">Mission Control</a></li>
        </ul>
      </div>
      <div>
        <div style="background:linear-gradient(180deg, rgba(13,27,69,0.92), rgba(10,15,37,0.98)); border:1px solid rgba(255,255,255,0.08); border-radius:16px; padding:18px;">
          <p style="font-family:'Space Mono', monospace; font-size:10px; color:#C9933A; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:10px;">Stay updated</p>
          <p style="font-size:14px; color:#8B9CC8; line-height:1.6;">Get launch updates, mission news, and exclusive offers.</p>
          <form id="footerSignupForm" style="display:flex; gap:8px; margin-top:14px;">
            <input id="footerSignupEmail" class="newsletter-input" type="email" name="email" placeholder="Email address" required style="flex:1; background:#0A0F25; border:1px solid rgba(255,255,255,0.08); color:#E8EDFF; padding:12px 14px; border-radius:10px; outline:none;">
            <button type="submit" class="newsletter-submit" style="background:linear-gradient(90deg, #6A3DE8, #8B5FF5); color:#fff; border:none; border-radius:10px; padding:12px 18px; cursor:pointer;">Go</button>
          </form>
          <div id="footerSignupSuccess" style="display:none; margin-top:12px; padding:12px 14px; border-radius:12px; background:rgba(106,61,232,0.15); color:#E8EDFF; font-size:14px; text-align:center;">✓ Submitted</div>
          <div id="footerSignupError" style="display:none; margin-top:12px; padding:12px 14px; border-radius:12px; background:rgba(232,59,59,0.15); color:#FF8A8A; font-size:14px; text-align:center;">Please enter a valid email address.</div>
        </div>
      </div>
    </div>
    <div style="max-width:1180px; margin:28px auto 0; border-top:1px solid rgba(255,255,255,0.08); padding-top:18px; display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; font-size:12px; color:#6F7EA7;">
      <p>© 2026 CosmosVoyage. All rights reserved.</p>
      <div style="display:flex; gap:18px; flex-wrap:wrap;">
        <a href="404.html" style="color:#6F7EA7; text-decoration:none;">Privacy</a>
        <a href="404.html" style="color:#6F7EA7; text-decoration:none;">Terms</a>
        <a href="404.html" style="color:#6F7EA7; text-decoration:none;">Cookies</a>
      </div>
    </div>
  </footer>'''

footer_media = '''
/* Footer mobile */
@media (max-width: 768px) {
  footer { padding: 48px 18px 28px !important; }
  footer > div[style*="max-width"] { grid-template-columns: 1fr !important; gap: 24px !important; }
  footer > div[style*="max-width"] > div { width: 100% !important; }
  footer > div:last-of-type { flex-direction: column !important; align-items: flex-start !important; gap: 12px !important; }
  footer > div:last-of-type div { width: 100%; justify-content: flex-start; }
  footer #footerSignupForm { flex-direction: column !important; }
  footer #footerSignupForm input,
  footer #footerSignupForm button { width: 100% !important; }
}
'''

for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    if '<footer' not in text or '</footer>' not in text:
        continue
    start = text.rfind('<footer')
    end = text.rfind('</footer>')
    if start == -1 or end == -1:
        print(f'skipping {path}: footer markers not found')
        continue
    new_text = text[:start] + canonical_footer + text[end + len('</footer>'):]
    if '/* Footer mobile */' not in new_text:
        style_match = re.search(r'(<style[^>]*>)(.*?)(</style>)', new_text, re.DOTALL | re.IGNORECASE)
        if style_match:
            before, style_content, after = style_match.group(1), style_match.group(2), style_match.group(3)
            if 'footer > div[style*="max-width"]' not in style_content:
                style_content = style_content + footer_media
                new_text = new_text[:style_match.start()] + before + style_content + after + new_text[style_match.end():]
        else:
            head_end = new_text.lower().find('</head>')
            if head_end != -1:
                style_tag = '<style>\n' + footer_media + '</style>\n'
                new_text = new_text[:head_end] + style_tag + new_text[head_end:]
    path.write_text(new_text, encoding='utf-8')
    print(f'updated {path}')
