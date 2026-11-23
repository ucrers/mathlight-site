"""Builds Mathlight's support, privacy and legal pages in English, German and Turkish."""

BADGE = '<svg viewBox="0 0 32 32"><path d="M16 5v4M7 9l2.5 2.5M25 9l-2.5 2.5M9 22h14M11 26h10M12 18a5 5 0 1 1 8 0c-1 1-1.5 2-1.5 4h-5c0-2-.5-3-1.5-4z"/></svg>'
TICK = '<div class="tick" aria-hidden="true"><svg viewBox="0 0 12 12"><path d="M2.5 6.2l2.3 2.3 4.7-5"/></svg></div>'
EMAIL = '<span class="email">ucar.ersin@outlook.de</span>'
ADDRESS = 'Ersin Ucar, Körnerstr. 27, 47166 Duisburg'

LANGS = {
  'en': dict(support='index.html', privacy='privacy.html', name='English',
    nav=('Support', 'Privacy Policy', 'Impressum'), footer='Mathlight for iPhone'),
  'de': dict(support='de.html', privacy='privacy-de.html', name='Deutsch',
    nav=('Support', 'Datenschutz', 'Impressum'), footer='Mathlight für iPhone'),
  'tr': dict(support='tr.html', privacy='privacy-tr.html', name='Türkçe',
    nav=('Destek', 'Gizlilik Politikası', 'Impressum'), footer='iPhone için Mathlight'),
}

def ticks(items):
    return '\n'.join(f'      <li>{TICK}<span>{t}</span></li>' for t in items)

def sections(items):
    out = []
    for title, body in items:
        inner = '\n'.join(f'      <li>{b}</li>' for b in body) if isinstance(body, list) else f'    <p>{body}</p>'
        if isinstance(body, list): inner = f'    <ul>\n{inner}\n    </ul>'
        out.append(f'  <section>\n    <h2>{title}</h2>\n{inner}\n  </section>')
    return '\n\n'.join(out)

def page(lang, kind, title, lead, description, card_title, card, body):
    L = LANGS[lang]
    current = {'support': 0, 'privacy': 1, 'impressum': 2}[kind]
    links = [L['support'], L['privacy'], 'impressum.html']
    mark = ' aria-current="page"'
    nav = '\n'.join(f'    <a href="{h}"{mark if i == current else ""}>{t}</a>' for i, (h, t) in enumerate(zip(links, L['nav'])))
    other = ' · '.join(f'<a href="{LANGS[o][kind if kind != "impressum" else "support"]}" lang="{o}">{LANGS[o]["name"]}</a>' for o in LANGS if o != lang)
    card_html = f'<ul>\n{ticks(card)}\n    </ul>' if isinstance(card, list) else f'<p>{card}</p>'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="style.css">
</head>
<body>
<main>
  <header>
    <div class="badge" aria-hidden="true">
      {BADGE}
    </div>
    <div>
      <h1>{title}</h1>
      <p class="lead">{lead}</p>
    </div>
  </header>

  <nav aria-label="Pages">
{nav}
  </nav>

  <div class="card">
    <h2>{card_title}</h2>
    {card_html}
  </div>

{body}

  <footer>{L["footer"]} · {other}</footer>
</main>
</body>
</html>
'''

PAGES = {}

# Support pages.
PAGES['index.html'] = page('en', 'support', 'Mathlight Support', 'Learn math by doing it, on iPhone.',
  'Help and contact for Mathlight, the interactive math app for iPhone.', 'Need help?',
  f'Write to {EMAIL}. Tell me your iPhone model, your iOS version, the lesson and what happened. I usually answer within a few days.',
  sections([
    ('Questions', [
      '<strong>Which language does the app use?</strong> The language of your iPhone: English, German or Turkish. To change it for Mathlight only, open the Settings app → <span class="path">Apps → Mathlight → Language</span>.',
      '<strong>Why is a lesson locked?</strong> Unit 1 of every course is free. The other units need Mathlight Plus.',
      '<strong>How many practice problems are free?</strong> 5 right answers a day. Plus has no limit.',
      '<strong>Where is my progress saved?</strong> Only on your iPhone. Deleting the app deletes your progress.',
    ]),
    ('Mathlight Plus', [
      '<strong>Bought Plus before, or got a new iPhone?</strong> Open the paywall and tap <span class="path">Restore Purchases</span>, with the same Apple Account.',
      '<strong>Cancel</strong> in the Settings app → <span class="path">your name → Subscriptions → Mathlight</span>, at least 24 hours before it renews.',
      '<strong>Refunds</strong> are handled by Apple at <a href="https://reportaproblem.apple.com" target="_blank" rel="noopener">reportaproblem.apple.com</a>.',
    ]),
  ]))

PAGES['de.html'] = page('de', 'support', 'Mathlight Support', 'Mathe lernen, indem du sie machst, auf dem iPhone.',
  'Hilfe und Kontakt für Mathlight, die interaktive Mathe-App für das iPhone.', 'Brauchst du Hilfe?',
  f'Schreib an {EMAIL}. Nenne dein iPhone-Modell, deine iOS-Version, die Lektion und was passiert ist. Ich antworte meistens innerhalb weniger Tage.',
  sections([
    ('Fragen', [
      '<strong>Welche Sprache nutzt die App?</strong> Die Sprache deines iPhones: Deutsch, Englisch oder Türkisch. Nur für Mathlight änderst du sie in der Einstellungen-App unter <span class="path">Apps → Mathlight → Sprache</span>.',
      '<strong>Warum ist eine Lektion gesperrt?</strong> Einheit 1 jedes Kurses ist kostenlos. Die anderen Einheiten brauchen Mathlight Plus.',
      '<strong>Wie viele Übungsaufgaben sind kostenlos?</strong> 5 richtige Antworten pro Tag. Mit Plus gibt es keine Grenze.',
      '<strong>Wo wird mein Fortschritt gespeichert?</strong> Nur auf deinem iPhone. Wenn du die App löschst, ist auch dein Fortschritt weg.',
    ]),
    ('Mathlight Plus', [
      '<strong>Plus schon gekauft oder ein neues iPhone?</strong> Öffne die Plus-Seite und tippe auf <span class="path">Käufe wiederherstellen</span>, mit demselben Apple Account.',
      '<strong>Kündigen</strong> in der Einstellungen-App unter <span class="path">dein Name → Abonnements → Mathlight</span>, mindestens 24 Stunden vor der Verlängerung.',
      '<strong>Erstattungen</strong> laufen über Apple: <a href="https://reportaproblem.apple.com" target="_blank" rel="noopener">reportaproblem.apple.com</a>.',
    ]),
  ]))

PAGES['tr.html'] = page('tr', 'support', 'Mathlight Destek', 'iPhone’da matematiği yaparak öğren.',
  'iPhone için etkileşimli matematik uygulaması Mathlight için yardım ve iletişim.', 'Yardım mı lazım?',
  f'{EMAIL} adresine yaz. iPhone modelini, iOS sürümünü, hangi ders olduğunu ve ne olduğunu anlat. Genelde birkaç gün içinde cevap veririm.',
  sections([
    ('Sorular', [
      '<strong>Uygulama hangi dili kullanıyor?</strong> iPhone’unun dilini: Türkçe, İngilizce veya Almanca. Sadece Mathlight için değiştirmek istersen Ayarlar uygulamasında <span class="path">Uygulamalar → Mathlight → Dil</span> bölümüne git.',
      '<strong>Bir ders neden kilitli?</strong> Her kursun 1. ünitesi ücretsiz. Diğer üniteler için Mathlight Plus gerekir.',
      '<strong>Kaç alıştırma sorusu ücretsiz?</strong> Günde 5 doğru cevap. Plus ile sınır yok.',
      '<strong>İlerlemem nerede saklanıyor?</strong> Sadece iPhone’unda. Uygulamayı silersen ilerlemen de silinir.',
    ]),
    ('Mathlight Plus', [
      '<strong>Plus’ı daha önce aldın ya da yeni bir iPhone’un mu var?</strong> Plus sayfasını aç ve aynı Apple Hesabı ile <span class="path">Satın Alımları Geri Yükle</span>’ye dokun.',
      '<strong>İptal</strong> için Ayarlar uygulamasında <span class="path">adın → Abonelikler → Mathlight</span> bölümüne git; yenilemeden en az 24 saat önce.',
      '<strong>İadeler</strong> Apple üzerinden yapılır: <a href="https://reportaproblem.apple.com" target="_blank" rel="noopener">reportaproblem.apple.com</a>.',
    ]),
  ]))

# Privacy pages.
PAGES['privacy.html'] = page('en', 'privacy', 'Mathlight Privacy Policy', 'Last updated: November 23, 2026',
  'Mathlight collects no data. Your progress stays on your iPhone.', 'In short', [
    'Mathlight does not collect your data. The developer never sees what you do in the app.',
    'Your progress stays on your iPhone.',
    'No account, no ads, no analytics, no tracking.',
    'Purchases go through Apple. The developer never gets your payment details.',
  ], sections([
    ('What Mathlight stores', 'The lessons you finished, your practice answers (to show your streak, daily goal and skills) and a few settings, such as the last course you opened. All of it is stored only on your iPhone. Mathlight has no server and sends nothing over the internet.'),
    ('Mathlight Plus', 'Mathlight Plus is a subscription through the App Store. Apple handles the payment. The app only learns whether Plus is active for your Apple Account, and the developer never gets your name, email or payment details.'),
    ('What Mathlight doesn’t do', ['No analytics, crash trackers or advertising.', 'No tracking across other apps or websites.', 'No selling or sharing of data, because none is collected.']),
    ('Deleting your data', 'Deleting the app removes everything it stored on your iPhone.'),
    ('This website', 'This site is hosted by GitHub Pages. It uses no cookies, no analytics and no fonts or scripts from other servers. GitHub may log your IP address for security, as described in <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">GitHub’s privacy statement</a>.'),
    ('Emails and your rights', 'If you write to the developer, your email address and message are used only to answer you (Art. 6(1)(b) and (f) GDPR) and are deleted once they are no longer needed, unless the law requires keeping them longer. You have the right to access, correct and delete your data, to restrict or object to its use, and to data portability (Art. 15–21 GDPR). You can also complain to a data protection authority, for example the one in North Rhine-Westphalia (LDI NRW).'),
    ('Children', 'Mathlight doesn’t collect personal data from anyone, children included.'),
    ('Changes', 'If this policy changes, the new version will be posted on this page with a new date.'),
    ('Contact', f'Mathlight is made by {ADDRESS}, Germany. For questions about privacy, write to {EMAIL}.'),
  ]))

PAGES['privacy-de.html'] = page('de', 'privacy', 'Mathlight Datenschutzerklärung', 'Stand: 23. November 2026',
  'Mathlight sammelt keine Daten. Dein Fortschritt bleibt auf deinem iPhone.', 'Kurz gesagt', [
    'Mathlight sammelt keine Daten über dich. Der Entwickler sieht nie, was du in der App machst.',
    'Dein Fortschritt bleibt auf deinem iPhone.',
    'Kein Konto, keine Werbung, keine Analyse, kein Tracking.',
    'Käufe laufen über Apple. Der Entwickler bekommt nie deine Zahlungsdaten.',
  ], sections([
    ('Was Mathlight speichert', 'Die Lektionen, die du abgeschlossen hast, deine Übungsantworten (für Serie, Tagesziel und Fähigkeiten) und ein paar Einstellungen, zum Beispiel den zuletzt geöffneten Kurs. Alles liegt nur auf deinem iPhone. Mathlight hat keinen Server und sendet nichts über das Internet.'),
    ('Mathlight Plus', 'Mathlight Plus ist ein Abo über den App Store. Apple wickelt die Zahlung ab. Die App erfährt nur, ob Plus für deinen Apple Account aktiv ist. Der Entwickler bekommt nie deinen Namen, deine E-Mail oder deine Zahlungsdaten.'),
    ('Was Mathlight nicht macht', ['Keine Analyse-Tools, keine Absturz-Tracker, keine Werbung.', 'Kein Tracking über andere Apps oder Websites.', 'Kein Verkauf und keine Weitergabe von Daten, weil keine gesammelt werden.']),
    ('Daten löschen', 'Wenn du die App löschst, ist alles weg, was sie auf deinem iPhone gespeichert hat.'),
    ('Diese Website', 'Diese Seite liegt bei GitHub Pages. Sie nutzt keine Cookies, keine Analyse und keine Schriften oder Skripte von anderen Servern. GitHub kann deine IP-Adresse aus Sicherheitsgründen speichern, wie in der <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">Datenschutzerklärung von GitHub</a> beschrieben.'),
    ('E-Mails und deine Rechte', 'Wenn du dem Entwickler schreibst, werden deine E-Mail-Adresse und deine Nachricht nur genutzt, um dir zu antworten (Art. 6 Abs. 1 lit. b und f DSGVO), und gelöscht, sobald sie nicht mehr gebraucht werden, außer das Gesetz verlangt eine längere Aufbewahrung. Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Widerspruch und Datenübertragbarkeit (Art. 15–21 DSGVO). Außerdem kannst du dich bei einer Datenschutz-Aufsichtsbehörde beschweren, zum Beispiel bei der Landesbeauftragten für Datenschutz und Informationsfreiheit Nordrhein-Westfalen (LDI NRW).'),
    ('Kinder', 'Mathlight sammelt von niemandem personenbezogene Daten, auch nicht von Kindern.'),
    ('Änderungen', 'Wenn sich diese Erklärung ändert, steht die neue Fassung mit neuem Datum auf dieser Seite.'),
    ('Verantwortlich und Kontakt', f'Verantwortlich im Sinne der DSGVO: {ADDRESS}, Deutschland. Fragen zum Datenschutz an {EMAIL}.'),
  ]))

PAGES['privacy-tr.html'] = page('tr', 'privacy', 'Mathlight Gizlilik Politikası', 'Son güncelleme: 23 Kasım 2026',
  'Mathlight hiçbir veri toplamaz. İlerlemen iPhone’unda kalır.', 'Kısaca', [
    'Mathlight senin hakkında veri toplamaz. Geliştirici uygulamada ne yaptığını asla görmez.',
    'İlerlemen iPhone’unda kalır.',
    'Hesap yok, reklam yok, analiz yok, izleme yok.',
    'Satın almalar Apple üzerinden yapılır. Geliştirici ödeme bilgilerini asla almaz.',
  ], sections([
    ('Mathlight neleri saklar', 'Bitirdiğin dersleri, alıştırma cevaplarını (seri, günlük hedef ve beceriler için) ve son açtığın kurs gibi birkaç ayarı. Hepsi sadece iPhone’unda saklanır. Mathlight’ın bir sunucusu yoktur ve internet üzerinden hiçbir şey göndermez.'),
    ('Mathlight Plus', 'Mathlight Plus, App Store üzerinden alınan bir aboneliktir. Ödemeyi Apple yapar. Uygulama sadece Apple Hesabın için Plus’ın açık olup olmadığını öğrenir; geliştirici adını, e-postanı veya ödeme bilgilerini asla almaz.'),
    ('Mathlight’ın yapmadıkları', ['Analiz aracı, çökme izleyici veya reklam yok.', 'Başka uygulama veya sitelerde izleme yok.', 'Veri satışı veya paylaşımı yok, çünkü hiçbir veri toplanmaz.']),
    ('Verilerini silmek', 'Uygulamayı silersen iPhone’unda sakladığı her şey silinir.'),
    ('Bu web sitesi', 'Bu site GitHub Pages üzerinde barındırılır. Çerez, analiz ya da başka sunuculardan yazı tipi veya betik kullanmaz. GitHub, <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">GitHub gizlilik bildiriminde</a> anlatıldığı gibi güvenlik için IP adresini kaydedebilir.'),
    ('E-postalar ve hakların', 'Geliştiriciye e-posta yazarsan, e-posta adresin ve mesajın sadece sana cevap vermek için kullanılır (GDPR madde 6/1 b ve f). Artık gerekmediğinde silinir; yasal bir saklama zorunluluğu varsa bu sürenin sonunda silinir. Verilerine erişme, onları düzeltme ve silme, işlenmelerini kısıtlama, itiraz etme ve veri taşınabilirliği hakların vardır (GDPR madde 15–21). Ayrıca bir veri koruma denetim makamına, örneğin Kuzey Ren-Vestfalya veri koruma makamına (LDI NRW) şikâyette bulunabilirsin.'),
    ('Çocuklar', 'Mathlight, çocuklar dahil kimseden kişisel veri toplamaz.'),
    ('Değişiklikler', 'Bu politika değişirse yeni sürüm bu sayfada yeni bir tarihle yayınlanır.'),
    ('İletişim', f'Mathlight’ı yapan: {ADDRESS}, Almanya. Gizlilikle ilgili sorular için {EMAIL} adresine yaz.'),
  ]))

# Legal notice (German law), one page.
PAGES['impressum.html'] = page('de', 'impressum', 'Impressum', 'Legal notice',
  'Impressum (legal notice) for Mathlight.', 'Angaben gemäß § 5 DDG',
  'Ersin Ucar<br>Körnerstr. 27<br>47166 Duisburg<br>Deutschland',
  sections([('Kontakt', f'Telefon: +49 151 25039100<br>E-Mail: {EMAIL}')]))

for name, html in PAGES.items():
    open(name, 'w', encoding='utf-8').write(html)
print(len(PAGES), 'pages')
