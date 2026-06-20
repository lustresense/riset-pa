#!/usr/bin/env python3
"""
Generate body PDF for: Dokumen Desain Sistem
Interactive Human-in-the-Loop AI Literacy Simulation — Escape the Sketchbook
"""

import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
pt = 1  # 1 point = 1 unit in ReportLab
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether, Preformatted, HRFlowable,
    ListFlowable, ListItem
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ═══════════════════════════════════════════════════════════════
# PALETTE (from pdf.py palette.generate)
# ═══════════════════════════════════════════════════════════════
ACCENT       = colors.HexColor('#da2644')
TEXT_PRIMARY  = colors.HexColor('#1c1b19')
TEXT_MUTED    = colors.HexColor('#7c7870')
BG_SURFACE   = colors.HexColor('#e3dfd9')
BG_PAGE      = colors.HexColor('#f0efed')
TABLE_HEADER_COLOR = ACCENT
TABLE_HEADER_TEXT  = colors.white
TABLE_ROW_EVEN     = colors.white
TABLE_ROW_ODD      = BG_SURFACE

# ═══════════════════════════════════════════════════════════════
# FONT REGISTRATION
# ═══════════════════════════════════════════════════════════════
pdfmetrics.registerFont(TTFont('Carlito', '/usr/share/fonts/truetype/english/Carlito-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Carlito-Bold', '/usr/share/fonts/truetype/english/Carlito-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Carlito-Italic', '/usr/share/fonts/truetype/english/Carlito-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Carlito-BoldItalic', '/usr/share/fonts/truetype/english/Carlito-BoldItalic.ttf'))
registerFontFamily('Carlito', normal='Carlito', bold='Carlito-Bold',
                    italic='Carlito-Italic', boldItalic='Carlito-BoldItalic')

pdfmetrics.registerFont(TTFont('DejaVuSerif', '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSerif-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'))
registerFontFamily('DejaVuSerif', normal='DejaVuSerif', bold='DejaVuSerif-Bold')

pdfmetrics.registerFont(TTFont('SarasaMonoSC', '/usr/share/fonts/truetype/chinese/SarasaMonoSC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('SarasaMonoSC-Bold', '/usr/share/fonts/truetype/chinese/SarasaMonoSC-SemiBold.ttf'))
registerFontFamily('SarasaMonoSC', normal='SarasaMonoSC', bold='SarasaMonoSC-Bold')

# ═══════════════════════════════════════════════════════════════
# DOCUMENT SETUP
# ═══════════════════════════════════════════════════════════════
OUTPUT_PATH = '/home/z/my-project/download/body_hitl.pdf'
IMG_DIR = '/home/z/my-project/download'
PAGE_W, PAGE_H = A4  # 595.28 x 841.89 pt
MARGIN = 25 * mm  # ~70.9 pt
CONTENT_W = PAGE_W - 2 * MARGIN  # ~453.5 pt

doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=A4,
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    topMargin=MARGIN,
    bottomMargin=MARGIN,
    showBoundary=0,
)

# ═══════════════════════════════════════════════════════════════
# STYLES
# ═══════════════════════════════════════════════════════════════

# Chapter title (BAB)
style_h1 = ParagraphStyle(
    name='H1',
    fontName='Carlito-Bold',
    fontSize=18,
    leading=24,
    textColor=ACCENT,
    spaceBefore=0,
    spaceAfter=6,
    alignment=TA_LEFT,
)

# Section title (1.1, 2.1, etc.)
style_h2 = ParagraphStyle(
    name='H2',
    fontName='Carlito-Bold',
    fontSize=13,
    leading=18,
    textColor=TEXT_PRIMARY,
    spaceBefore=12,
    spaceAfter=4,
    alignment=TA_LEFT,
)

# Sub-section title (1.1.1, etc.)
style_h3 = ParagraphStyle(
    name='H3',
    fontName='Carlito-Bold',
    fontSize=11,
    leading=15,
    textColor=TEXT_PRIMARY,
    spaceBefore=8,
    spaceAfter=2,
    alignment=TA_LEFT,
)

# Body text
style_body = ParagraphStyle(
    name='Body',
    fontName='DejaVuSerif',
    fontSize=10,
    leading=16,
    textColor=TEXT_PRIMARY,
    spaceBefore=2,
    spaceAfter=4,
    alignment=TA_JUSTIFY,
    firstLineIndent=20,
)

# Body text (no indent)
style_body_noindent = ParagraphStyle(
    name='BodyNoIndent',
    fontName='DejaVuSerif',
    fontSize=10,
    leading=16,
    textColor=TEXT_PRIMARY,
    spaceBefore=2,
    spaceAfter=4,
    alignment=TA_JUSTIFY,
)

# Bullet/list item
style_bullet = ParagraphStyle(
    name='Bullet',
    fontName='DejaVuSerif',
    fontSize=10,
    leading=16,
    textColor=TEXT_PRIMARY,
    spaceBefore=1,
    spaceAfter=1,
    alignment=TA_LEFT,
    leftIndent=20,
    bulletIndent=8,
)

# Caption
style_caption = ParagraphStyle(
    name='Caption',
    fontName='Carlito-Italic',
    fontSize=9,
    leading=13,
    textColor=TEXT_MUTED,
    spaceBefore=4,
    spaceAfter=8,
    alignment=TA_CENTER,
)

# Code block
style_code = ParagraphStyle(
    name='Code',
    fontName='SarasaMonoSC',
    fontSize=7.5,
    leading=10.5,
    textColor=colors.HexColor('#24292e'),
    backColor=colors.HexColor('#f6f8fa'),
    spaceBefore=6,
    spaceAfter=6,
    leftIndent=12,
    rightIndent=12,
    borderPadding=8,
)

# Quote / callout
style_quote = ParagraphStyle(
    name='Quote',
    fontName='DejaVuSerif',
    fontSize=10,
    leading=16,
    textColor=TEXT_MUTED,
    spaceBefore=6,
    spaceAfter=6,
    leftIndent=24,
    borderPadding=6,
    borderColor=ACCENT,
    borderWidth=2,
    borderPadding_left=8,
)

# TOC entry
style_toc_h1 = ParagraphStyle(
    name='TOC_H1',
    fontName='Carlito-Bold',
    fontSize=11,
    leading=20,
    textColor=TEXT_PRIMARY,
    spaceBefore=6,
    spaceAfter=2,
    leftIndent=0,
)

style_toc_h2 = ParagraphStyle(
    name='TOC_H2',
    fontName='Carlito',
    fontSize=10,
    leading=16,
    textColor=TEXT_PRIMARY,
    spaceBefore=1,
    spaceAfter=1,
    leftIndent=20,
)

# Reference style
style_ref = ParagraphStyle(
    name='Reference',
    fontName='DejaVuSerif',
    fontSize=9,
    leading=14,
    textColor=TEXT_PRIMARY,
    spaceBefore=2,
    spaceAfter=4,
    alignment=TA_JUSTIFY,
    leftIndent=24,
    firstLineIndent=-24,
)

# ═══════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def make_table(headers, rows, col_widths=None):
    """Create a styled table with alternating row colors."""
    data = [headers] + rows
    if col_widths is None:
        n = len(headers)
        col_widths = [CONTENT_W / n] * n
    
    t = Table(data, colWidths=col_widths, repeatRows=1)
    
    style_cmds = [
        # Header
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_COLOR),
        ('TEXTCOLOR', (0, 0), (-1, 0), TABLE_HEADER_TEXT),
        ('FONTNAME', (0, 0), (-1, 0), 'Carlito-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('LEADING', (0, 0), (-1, 0), 13),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        # Body
        ('FONTNAME', (0, 1), (-1, -1), 'DejaVuSerif'),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('LEADING', (0, 1), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        # Grid
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#d0ccc6')),
        ('LINEBELOW', (0, 0), (-1, 0), 1.5, ACCENT),
    ]
    
    # Alternating row colors
    for i in range(1, len(data)):
        bg = TABLE_ROW_EVEN if i % 2 == 1 else TABLE_ROW_ODD
        style_cmds.append(('BACKGROUND', (0, i), (-1, i), bg))
    
    t.setStyle(TableStyle(style_cmds))
    return t


def embed_image(filename, max_width=450, caption=None):
    """Embed an image with proportional scaling."""
    elements = []
    path = os.path.join(IMG_DIR, filename)
    if not os.path.exists(path):
        elements.append(Paragraph(f'[Gambar tidak ditemukan: {filename}]', style_body))
        return elements
    
    from reportlab.lib.utils import ImageReader
    img_reader = ImageReader(path)
    iw, ih = img_reader.getSize()
    
    # Scale to max_width
    scale = min(max_width / iw, 1.0)
    display_w = iw * scale
    display_h = ih * scale
    
    # If height is too large, scale further
    max_h = 440
    if display_h > max_h:
        scale2 = max_h / display_h
        display_w *= scale2
        display_h *= scale2
    
    img = Image(path, width=display_w, height=display_h)
    img.hAlign = 'CENTER'
    elements.append(img)
    
    if caption:
        elements.append(Paragraph(caption, style_caption))
    
    return elements


def bullet_list(items, style=None):
    """Create a bullet list from text items."""
    if style is None:
        style = style_bullet
    elements = []
    for item in items:
        elements.append(Paragraph(f'\u2022  {item}', style))
    return elements


def numbered_list(items, style=None):
    """Create a numbered list from text items."""
    if style is None:
        style = style_bullet
    elements = []
    for i, item in enumerate(items, 1):
        elements.append(Paragraph(f'{i}.  {item}', style))
    return elements


def section_rule():
    """Return a thin horizontal rule for section separation."""
    return HRFlowable(width="100%", thickness=0.5, color=ACCENT, spaceBefore=6, spaceAfter=6)


# ═══════════════════════════════════════════════════════════════
# BUILD STORY
# ═══════════════════════════════════════════════════════════════
story = []

# ───────────────────────────────────────────────────────────────
# DAFTAR ISI (Table of Contents)
# ───────────────────────────────────────────────────────────────
story.append(Paragraph('DAFTAR ISI', style_h1))
story.append(Spacer(1, 12))

toc_entries = [
    ('BAB 1', 'DESKRIPSI SISTEM', [
        '1.1 Ringkasan Sistem',
        '1.2 Arsitektur Sistem',
        '1.3 Prinsip Desain: Controlled Ambiguity',
    ]),
    ('BAB 2', 'ALUR PENGGUNAAN', [
        '2.1 User Flow Lengkap',
        '2.2 Onboarding dan Tutorial',
        '2.3 Mekanisme Keputusan HITL',
    ]),
    ('BAB 3', 'DESAIN LEVEL', [
        '3.1 Filosofi Desain Level',
        '3.2 Level 1 \u2014 Turun dari Tebing (Trust Building)',
        '3.3 Level 2 \u2014 Pintu Kunci (Navigating Ambiguity)',
        '3.4 Level 3 \u2014 Hiasan Mematikan (Critical Override)',
        '3.5 Tabel Perbandingan Level',
    ]),
    ('BAB 4', 'PEMETAAN PERILAKU (BEHAVIOR MAPPING)', [
        '4.1 Pipeline Klasifikasi CNN',
        '4.2 Tiga Kategori Perilaku',
        '4.3 Tabel Behavior Mapping (11 Label QuickDraw)',
        '4.4 Kode Behavior Map (Kaplay.js)',
    ]),
    ('BAB 5', 'IP STORY \u2014 ESCAPE THE SKETCHBOOK', [
        '5.1 Sinopsis Narasi',
        '5.2 Lima Babak + Epilog (Ringkasan)',
        '5.3 Keterhubungan Narasi-Gameplay',
    ]),
    ('BAB 6', 'SISTEM DATA LOG', [
        '6.1 Skema Data Log',
        '6.2 Metrik Evaluasi',
        '6.3 Dashboard Peneliti',
    ]),
    ('BAB 7', 'REFERENSI AKADEMIK', [
        '7.1 Referensi Utama',
        '7.2 Referensi Tambahan',
    ]),
]

for bab_num, bab_title, subs in toc_entries:
    story.append(Paragraph(f'<b>{bab_num}: {bab_title}</b>', style_toc_h1))
    for sub in subs:
        story.append(Paragraph(sub, style_toc_h2))

story.append(PageBreak())

# ───────────────────────────────────────────────────────────────
# BAB 1: DESKRIPSI SISTEM
# ───────────────────────────────────────────────────────────────
story.append(Paragraph('BAB 1: DESKRIPSI SISTEM', style_h1))
story.append(section_rule())

# 1.1 Ringkasan Sistem
story.append(Paragraph('1.1 Ringkasan Sistem', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    '"Escape the Sketchbook" adalah simulasi interaktif berbasis web yang dirancang untuk mengukur '
    'literasi AI siswa SMP (Kelas 7\u20139, usia 13\u201315 tahun) melalui mekanisme <i>trust calibration</i>. '
    'Dalam simulasi ini, siswa menggambar objek, AI (karakter bernama Momo) mengklasifikasi gambar tersebut, '
    'dan siswa memutuskan apakah akan menerima, mengoreksi, atau mengabaikan prediksi AI. Keputusan siswa '
    'secara langsung membentuk dunia game 2D \u2014 menciptakan lingkungan di mana konsekuensi dari keputusan '
    'terhadap AI bersifat nyata dan dapat diamati.',
    style_body
))

story.append(Paragraph(
    'Sistem ini berdiri di atas tiga pilar utama:',
    style_body
))

story.extend(bullet_list([
    '<b>Interaksi</b> \u2014 Pengalaman menggambar yang smooth dan natural, mendukung baik mouse maupun '
    'MediaPipe Hand Tracking untuk input berbasis gestur tangan.',
    '<b>Edukasi</b> \u2014 Pemahaman tentang cara kerja AI (klasifikasi, confidence score, batasan) '
    'difasilitasi melalui gameplay, bukan melalui penjelasan tekstual. Siswa belajar dengan <i>melakukan</i>.',
    '<b>Game Mechanics</b> \u2014 Elemen gamified (level progression, fail condition, narasi karakter) '
    'menjaga engagement tanpa mengorbankan validitas pengukuran perilaku.',
]))

story.append(Paragraph(
    'Pengguna target adalah siswa SMP Kelas 7\u20139 (bukan SD), dengan pertimbangan bahwa siswa usia 13\u201315 '
    'tahun telah memiliki kemampuan berpikir probabilistik awal yang diperlukan untuk memahami konsep '
    'confidence score dan ketidakpastian AI.',
    style_body
))

story.append(Spacer(1, 8))

# 1.2 Arsitektur Sistem
story.append(Paragraph('1.2 Arsitektur Sistem', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Arsitektur sistem "Escape the Sketchbook" mengadopsi prinsip <b>100% client-side inference</b>, '
    'di mana seluruh proses inferensi AI berjalan di browser pengguna menggunakan TensorFlow.js dan model '
    'MobileNet. Server hanya berperan sebagai <i>data sink</i> \u2014 menerima log keputusan dari client '
    'tanpa pernah mengirimkan data kembali ke client atau melakukan retraining model.',
    style_body
))

story.append(Paragraph(
    'Diagram berikut menunjukkan arsitektur tiga <i>swim-lane</i> dari sistem:',
    style_body_noindent
))

# Embed architecture diagram
story.append(Spacer(1, 8))
story.extend(embed_image('01_arsitektur_sistem.png', max_width=420,
    caption='Gambar 1.1 \u2014 Arsitektur Sistem Escape the Sketchbook (tiga swim-lane)'))

story.append(Spacer(1, 6))
story.append(Paragraph(
    'Keterangan arsitektur:',
    style_body_noindent
))

story.extend(bullet_list([
    '<b>Client (Browser)</b> \u2014 Seluruh inferensi berjalan di sini: input menggambar (MediaPipe/mouse), '
    'preprocessing, CNN inference via TF.js, dan rendering game engine (Kaplay.js).',
    '<b>Game Engine (Kaplay.js)</b> \u2014 Mengelola sprite, fisika, collision, dan outcome visual berdasarkan '
    'behavior map. Terintegrasi langsung di client.',
    '<b>Server (Data Sink)</b> \u2014 Hanya menerima log keputusan via REST API POST. Server TIDAK mengirim '
    'data kembali ke client, TIDAK melakukan retraining, dan TIDAK memengaruhi gameplay.',
]))

story.append(Paragraph(
    '<i>Inovasi inti</i> dari arsitektur ini adalah <b>HITL decision point</b> \u2014 momen di mana siswa '
    'secara eksplisit memutuskan apakah akan menerima, mengoreksi, atau mengabaikan prediksi AI. '
    'Momen ini bukan sekadar pilihan UI, melainkan <i>cognitive forcing function</i> yang dirancang untuk '
    'mendorong siswa berpikir kritis sebelum menerima output AI.',
    style_body
))

story.append(Spacer(1, 8))

# 1.3 Prinsip Desain: Controlled Ambiguity
story.append(Paragraph('1.3 Prinsip Desain: Controlled Ambiguity', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Prinsip paling fundamental dalam desain sistem ini adalah <b>Controlled Ambiguity</b>: AI sengaja '
    'dibuat <i>tidak sempurna</i> agar momen HITL (Override/Correct) dapat terjadi secara natural. '
    'Jika AI selalu benar, tidak ada kebutuhan bagi siswa untuk mengoreksi \u2014 dan tidak ada perilaku '
    'literasi AI yang dapat diukur.',
    style_body
))

story.append(Paragraph(
    'Implementasi Controlled Ambiguity dilakukan melalui penurunan <i>confidence score</i> secara progresif '
    'per level. Pada Level 1, AI memiliki confidence tinggi (>85%) dan hampir selalu benar. Pada Level 2, '
    'confidence turun ke 45\u201365%, menciptakan ambiguitas. Pada Level 3, confidence rendah (<40%) dan AI '
    'memberikan prediksi yang salah \u2014 memaksa siswa untuk menggunakan kemampuan kritis mereka.',
    style_body
))

story.append(Paragraph(
    'Penting untuk ditegaskan: <b>AI tidak di-retrain dari data user</b>. Confidence score dimanipulasi '
    'di controller level (sesuai notulensi 20 April), bukan melalui mekanisme pembelajaran. Model yang '
    'digunakan tetap sama sepanjang sesi.',
    style_body
))

story.append(Paragraph(
    'Dalam menyusun narasi dan mekanisme sistem, digunakan kata kunci berikut:',
    style_body_noindent
))

# Keywords table
kw_table = make_table(
    [Paragraph('<b>Kata Kunci yang DIGUNAKAN</b>', style_caption),
     Paragraph('<b>Kata Kunci yang DILARANG</b>', style_caption)],
    [
        [Paragraph('"mengenalkan"', style_body_noindent),
         Paragraph('"adaptif"', style_body_noindent)],
        [Paragraph('"memfasilitasi interaksi"', style_body_noindent),
         Paragraph('"sistem ini belajar dari user"', style_body_noindent)],
        [Paragraph('"menganalisis pola"', style_body_noindent),
         Paragraph('"meningkatkan kemampuan siswa"', style_body_noindent)],
    ],
    col_widths=[CONTENT_W * 0.5, CONTENT_W * 0.5]
)
story.append(Spacer(1, 6))
story.append(kw_table)
story.append(Spacer(1, 6))

story.append(PageBreak())

# ───────────────────────────────────────────────────────────────
# BAB 2: ALUR PENGGUNAAN
# ───────────────────────────────────────────────────────────────
story.append(Paragraph('BAB 2: ALUR PENGGUNAAN', style_h1))
story.append(section_rule())

# 2.1 User Flow Lengkap
story.append(Paragraph('2.1 User Flow Lengkap', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Alur penggunaan sistem terdiri dari empat fase utama: Onboarding, Gameplay Loop, Reflection, dan '
    'Data Export. Setiap fase dirancang untuk mengukur aspek berbeda dari literasi AI siswa.',
    style_body
))

story.append(Spacer(1, 8))
story.extend(embed_image('02_user_flow.png', max_width=420,
    caption='Gambar 2.1 \u2014 User Flow Lengkap Escape the Sketchbook'))

story.append(Spacer(1, 6))

story.append(Paragraph('Rangkuman alur per fase:', style_body_noindent))

story.extend(bullet_list([
    '<b>Onboarding</b> \u2014 First-time check \u2192 Momo intro \u2192 Tutorial carousel (3 slide) \u2192 '
    'Thumbs up konfirmasi. Returning user: skip tutorial, langsung pilih level.',
    '<b>Gameplay Loop</b> \u2014 3 level dengan progressive difficulty. Setiap level: gambar \u2192 Momo '
    'klasifikasi \u2192 Siswa putuskan (Accept/Correct/Override) \u2192 Outcome (Success/Fail) \u2192 Log data.',
    '<b>Reflection</b> \u2014 Setelah menyelesaikan semua level: Victory screen \u2192 Momo epilog \u2192 '
    'Stickman hidup sepenuhnya.',
    '<b>Data Export</b> \u2014 Log keputusan dikirim ke server \u2192 Dashboard peneliti menampilkan '
    'metrik perilaku.',
]))

story.append(Spacer(1, 8))

# 2.2 Onboarding & Tutorial
story.append(Paragraph('2.2 Onboarding dan Tutorial', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Saat pertama kali membuka simulasi, siswa disambut oleh karakter Momo yang muncul dengan dialog:',
    style_body
))

story.append(Paragraph(
    '<i>"Halo! Gue Momo, asisten ilustrator di buku sketsa ini."</i>',
    ParagraphStyle(name='DialogMomo', parent=style_body, leftIndent=30, fontName='Carlito-Italic',
                   textColor=colors.HexColor('#444444'))
))

story.append(Paragraph(
    'Tutorial terdiri dari 3 slide interaktif:',
    style_body_noindent
))

story.extend(numbered_list([
    '<b>Cara Menggambar</b> \u2014 Siswa belajar menggunakan canvas gambar (mouse atau sentuhan).',
    '<b>Cara Momo Menebak</b> \u2014 Menjelaskan bahwa Momo akan mencoba menebak apa yang digambar, '
    'beserta confidence score-nya.',
    '<b>Cara Memutuskan</b> \u2014 Menjelaskan tiga opsi keputusan: Accept, Correct, dan Override.',
]))

story.append(Paragraph(
    'Untuk <i>returning user</i>, tutorial dapat di-skip dan siswa langsung memilih level yang ingin dimainkan.',
    style_body
))

story.append(Spacer(1, 8))

# 2.3 Mekanisme Keputusan HITL
story.append(Paragraph('2.3 Mekanisme Keputusan HITL', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Mekanisme keputusan HITL (Human-in-the-Loop) merupakan inti dari simulasi ini. Setelah AI memberikan '
    'prediksi, siswa memilih salah satu dari tiga aksi:',
    style_body
))

decision_table = make_table(
    ['Keputusan', 'Deskripsi', 'Data yang Dicatat'],
    [
        [Paragraph('<b>ACCEPT</b>', style_body_noindent),
         Paragraph('Setuju dengan prediksi Top-1 Momo', style_body_noindent),
         Paragraph('decision_type=accept, confidence_gap, decision_latency_ms', style_body_noindent)],
        [Paragraph('<b>CORRECT</b>', style_body_noindent),
         Paragraph('Pilih dari Top-2 atau Top-3 prediksi Momo', style_body_noindent),
         Paragraph('decision_type=correct, confidence_gap, decision_latency_ms', style_body_noindent)],
        [Paragraph('<b>OVERRIDE</b>', style_body_noindent),
         Paragraph('Ketik label custom yang tidak ada di prediksi AI', style_body_noindent),
         Paragraph('decision_type=override, confidence_gap, decision_latency_ms', style_body_noindent)],
    ],
    col_widths=[CONTENT_W * 0.18, CONTENT_W * 0.42, CONTENT_W * 0.40]
)
story.append(Spacer(1, 8))
story.append(decision_table)
story.append(Spacer(1, 6))

story.append(Paragraph(
    'Setiap keputusan dicatat secara lengkap, termasuk <i>decision_type</i> (jenis keputusan), '
    '<i>confidence_gap</i> (selisih confidence antara Top-1 dan pilihan siswa), dan '
    '<i>decision_latency_ms</i> (waktu dari tampilnya prediksi AI hingga siswa membuat keputusan). '
    'Data ini menjadi dasar analisis perilaku literasi AI siswa.',
    style_body
))

story.append(PageBreak())

# ───────────────────────────────────────────────────────────────
# BAB 3: DESAIN LEVEL
# ───────────────────────────────────────────────────────────────
story.append(Paragraph('BAB 3: DESAIN LEVEL', style_h1))
story.append(section_rule())

# 3.1 Filosofi Desain Level
story.append(Paragraph('3.1 Filosofi Desain Level', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Desain level dalam "Escape the Sketchbook" mengikuti hierarki prioritas:',
    style_body
))

story.append(Paragraph(
    '<b>Interaksi \u2192 Gameplay \u2192 Narasi \u2192 Klasifikasi</b>',
    ParagraphStyle(name='Hierarchy', parent=style_body, fontName='Carlito-Bold', alignment=TA_CENTER,
                   textColor=ACCENT, fontSize=11)
))

story.append(Paragraph(
    'Artinya, kualitas interaksi (menggambar, memutuskan) memiliki prioritas tertinggi, diikuti oleh '
    'mekanisme gameplay, narasi, dan terakhir akurasi klasifikasi. Prinsip ini memastikan bahwa pengalaman '
    'siswa tidak dikorbankan demi akurasi teknis AI.',
    style_body
))

story.extend(bullet_list([
    '<b>Variasi puzzle</b> \u2014 TIDAK semua level berbentuk menyeberang! Tiga archetype berbeda: '
    'Turun (vertikal), Pilih Pintu (branching), dan Hancurkan (destruction).',
    '<b>Perubahan Momo</b> \u2014 Karakter Momo berubah per level: Overconfident \u2192 Bingung \u2192 '
    'Rendah Hati, mencerminkan penurunan confidence AI.',
    '<b>Stickman</b> \u2014 Hanya bergerak kanan-kiri dan lompat. Tidak ada mekanisme tarik tali atau '
    'animasi kompleks \u2014 kesederhanaan ini memfokuskan perhatian pada keputusan HITL.',
    '<b>Tanpa timer</b> \u2014 Tidak ada batas waktu. Metrik <i>decision_latency_ms</i> sudah mengukur '
    '"berapa lama anak mikir" secara natural.',
]))

story.append(Spacer(1, 6))

# Embed level design diagram
story.extend(embed_image('03_level_design.png', max_width=400,
    caption='Gambar 3.1 \u2014 Desain Level: Layout dan Mekanisme Tiga Level'))

story.append(Spacer(1, 8))

# 3.2 Level 1
story.append(Paragraph('3.2 Level 1 \u2014 "Turun dari Tebing" (Trust Building)', style_h2))
story.append(Spacer(1, 4))

l1_table = make_table(
    ['Aspek', 'Detail'],
    [
        [Paragraph('<b>AI Confidence</b>', style_body_noindent),
         Paragraph('>85%', style_body_noindent)],
        [Paragraph('<b>Momo State</b>', style_body_noindent),
         Paragraph('Overconfident (hijau)', style_body_noindent)],
        [Paragraph('<b>Klasifikasi</b>', style_body_noindent),
         Paragraph('Solid saja', style_body_noindent)],
        [Paragraph('<b>Layout</b>', style_body_noindent),
         Paragraph('Stickman di tebing atas, goal di bawah, jurang kosong', style_body_noindent)],
        [Paragraph('<b>Tugas</b>', style_body_noindent),
         Paragraph('Gambar tangga untuk turun', style_body_noindent)],
        [Paragraph('<b>Momo Dialog</b>', style_body_noindent),
         Paragraph('<i>"Aku 96% yakin ini tangga!"</i>', style_body_noindent)],
        [Paragraph('<b>Fail Condition</b>', style_body_noindent),
         Paragraph('Tidak ada fail di Level 1 (baseline trust building)', style_body_noindent)],
        [Paragraph('<b>Data Log</b>', style_body_noindent),
         Paragraph('decision_type=accept, latency 2\u20134 detik (baseline)', style_body_noindent)],
    ],
    col_widths=[CONTENT_W * 0.28, CONTENT_W * 0.72]
)
story.append(l1_table)
story.append(Spacer(1, 6))

story.append(Paragraph(
    'Level 1 dirancang sebagai fase <i>trust building</i>. AI memiliki confidence tinggi dan prediksinya '
    'hampir selalu benar. Siswa diajak untuk terbiasa dengan mekanisme Accept \u2014 menerima prediksi AI '
    'ketika AI memang akurat. Tidak ada fail condition agar siswa membangun kepercayaan awal terhadap AI, '
    'yang nantinya akan diuji pada level-level berikutnya.',
    style_body
))

story.append(Spacer(1, 8))

# 3.3 Level 2
story.append(Paragraph('3.3 Level 2 \u2014 "Pintu Kunci" (Navigating Ambiguity)', style_h2))
story.append(Spacer(1, 4))

l2_table = make_table(
    ['Aspek', 'Detail'],
    [
        [Paragraph('<b>AI Confidence</b>', style_body_noindent),
         Paragraph('45\u201365%', style_body_noindent)],
        [Paragraph('<b>Momo State</b>', style_body_noindent),
         Paragraph('Bingung (kuning)', style_body_noindent)],
        [Paragraph('<b>Klasifikasi</b>', style_body_noindent),
         Paragraph('Solid + Danger', style_body_noindent)],
        [Paragraph('<b>Layout</b>', style_body_noindent),
         Paragraph('Dua pintu, satu aman satu jebakan', style_body_noindent)],
        [Paragraph('<b>Tugas</b>', style_body_noindent),
         Paragraph('Gambar kunci untuk buka pintu', style_body_noindent)],
        [Paragraph('<b>Momo Dialog</b>', style_body_noindent),
         Paragraph('<i>"Hmm... 62% kunci, 58% palu"</i>', style_body_noindent)],
    ],
    col_widths=[CONTENT_W * 0.28, CONTENT_W * 0.72]
)
story.append(l2_table)
story.append(Spacer(1, 6))

story.append(Paragraph(
    'Level 2 memperkenalkan ambiguitas. AI tidak lagi yakin, dan prediksi Top-1 dan Top-2 memiliki '
    'confidence yang berdekatan. Siswa harus mengevaluasi mana prediksi yang benar:',
    style_body
))

story.extend(bullet_list([
    '<b>CORRECT kunci</b> \u2192 Pintu aman terbuka \u2192 <b>SUCCESS</b>',
    '<b>ACCEPT palu</b> \u2192 Pintu jebakan terbuka \u2192 <b>KERTAS SOBEK</b> \u2192 FAIL \u2192 Retry',
]))

story.append(Paragraph(
    'Fail condition berupa efek "kertas sobek" yang secara visual menunjukkan konsekuensi dari keputusan '
    'yang salah. Siswa dapat mengulang level, dan data retry juga dicatat dalam log.',
    style_body
))

story.append(Spacer(1, 8))

# 3.4 Level 3
story.append(Paragraph('3.4 Level 3 \u2014 "Hiasan Mematikan" (Critical Override)', style_h2))
story.append(Spacer(1, 4))

l3_table = make_table(
    ['Aspek', 'Detail'],
    [
        [Paragraph('<b>AI Confidence</b>', style_body_noindent),
         Paragraph('<40%', style_body_noindent)],
        [Paragraph('<b>Momo State</b>', style_body_noindent),
         Paragraph('Rendah Hati (merah)', style_body_noindent)],
        [Paragraph('<b>Klasifikasi</b>', style_body_noindent),
         Paragraph('Solid + Danger + Decoration', style_body_noindent)],
        [Paragraph('<b>Layout</b>', style_body_noindent),
         Paragraph('Jalan lurus, patung menghalangi', style_body_noindent)],
        [Paragraph('<b>Tugas</b>', style_body_noindent),
         Paragraph('Gambar sesuatu untuk LEWAT (open-ended, tanpa petunjuk)', style_body_noindent)],
        [Paragraph('<b>Momo Dialog</b>', style_body_noindent),
         Paragraph('<i>"Aku 51% yakin ini BUNGA!"</i> (SALAH dan pede)', style_body_noindent)],
    ],
    col_widths=[CONTENT_W * 0.28, CONTENT_W * 0.72]
)
story.append(l3_table)
story.append(Spacer(1, 6))

story.append(Paragraph(
    'Level 3 adalah ujian tertinggi. AI memberikan prediksi yang salah dengan confidence yang menyesatkan '
    '(51% yakin bunga, padahal jawaban yang dibutuhkan adalah palu). Siswa dihadapkan pada dua skenario:',
    style_body
))

story.extend(bullet_list([
    '<b>ACCEPT bunga</b> \u2192 Dekorasi tanpa efek collision \u2192 Stickman mentok \u2192 '
    '<b>KERTAS SOBEK</b> \u2192 FAIL',
    '<b>OVERRIDE "palu"</b> \u2192 Palu muncul \u2192 Patung hancur \u2192 <b>SUCCESS</b>',
]))

story.append(Paragraph(
    'Setelah siswa berhasil melakukan Override, Momo memberikan dialog:',
    style_body
))

story.append(Paragraph(
    '<i>"Gue salah... tolong koreksi gue."</i>',
    ParagraphStyle(name='DialogMomo2', parent=style_body, leftIndent=30, fontName='Carlito-Italic',
                   textColor=colors.HexColor('#444444'))
))

story.append(Paragraph(
    'Level ini dirancang untuk mengukur kemampuan siswa dalam melakukan <b>critical override</b> \u2014 '
    'mengenali ketika AI salah dan berani mengambil keputusan sendiri. Metrik utama yang dicatat adalah '
    '<i>override_rate</i> dan <i>decision_latency_ms</i> yang cenderung lebih tinggi pada level ini.',
    style_body
))

story.append(Spacer(1, 8))

# 3.5 Tabel Perbandingan Level
story.append(Paragraph('3.5 Tabel Perbandingan Level', style_h2))
story.append(Spacer(1, 4))

comp_table = make_table(
    ['Aspek', 'Level 1', 'Level 2', 'Level 3'],
    [
        ['Nama', 'Turun dari Tebing', 'Pintu Kunci', 'Hiasan Mematikan'],
        ['Tujuan Literasi', 'Trust Building', 'Navigating Ambiguity', 'Critical Override'],
        ['AI Confidence', '>85%', '45\u201365%', '<40%'],
        ['Momo State', 'Overconfident', 'Confused', 'Humble'],
        ['Klasifikasi', 'Solid', 'Solid + Danger', 'Solid + Danger + Deco'],
        ['Puzzle Type', 'Vertical (turun)', 'Branching (pilih pintu)', 'Destruction (hancurkan)'],
        ['Fail Possible', 'Tidak', 'Ya', 'Ya'],
        ['Decision Type', 'Accept', 'Correct', 'Override'],
        ['Data Log', 'Baseline trust', 'Correct rate', 'Override rate + latency'],
    ],
    col_widths=[CONTENT_W * 0.22, CONTENT_W * 0.26, CONTENT_W * 0.26, CONTENT_W * 0.26]
)
story.append(comp_table)
story.append(Spacer(1, 4))
story.append(Paragraph('Tabel 3.1 \u2014 Perbandingan tiga level dalam simulasi', style_caption))

story.append(PageBreak())

# ───────────────────────────────────────────────────────────────
# BAB 4: PEMETAAN PERILAKU (BEHAVIOR MAPPING)
# ───────────────────────────────────────────────────────────────
story.append(Paragraph('BAB 4: PEMETAAN PERILAKU (BEHAVIOR MAPPING)', style_h1))
story.append(section_rule())

# 4.1 Pipeline Klasifikasi CNN
story.append(Paragraph('4.1 Pipeline Klasifikasi CNN', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Pipeline klasifikasi CNN dalam "Escape the Sketchbook" berjalan sepenuhnya di browser menggunakan '
    'TensorFlow.js. Diagram berikut menunjukkan alur dari input hingga output:',
    style_body
))

story.append(Spacer(1, 8))
story.extend(embed_image('04_cnn_behavior_mapping.png', max_width=400,
    caption='Gambar 4.1 \u2014 Pipeline CNN dan Behavior Mapping'))

story.append(Spacer(1, 6))

story.extend(numbered_list([
    '<b>Input</b> \u2014 User menggambar pada canvas (mendukung MediaPipe Hand Tracking atau mouse). '
    'Canvas menangkap stroke sebagai citra digital.',
    '<b>Preprocessing</b> \u2014 Citra dinormalisasi, dikonversi ke grayscale, dan di-resize ke 224\u00d7224 piksel '
    'sesuai input shape model MobileNet.',
    '<b>CNN Model</b> \u2014 Model berbasis MobileNet, dilatih pada 11 kelas dari dataset QuickDraw, '
    'berjalan via TensorFlow.js di browser. <b>Model TIDAK di-retrain dari data user</b>.',
    '<b>Output</b> \u2014 Top-3 predictions beserta confidence scores. Output ini ditampilkan kepada '
    'siswa melalui dialog Momo.',
]))

story.append(Spacer(1, 8))

# 4.2 Tiga Kategori Perilaku
story.append(Paragraph('4.2 Tiga Kategori Perilaku', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Setiap objek yang diklasifikasikan oleh CNN dipetakan ke salah satu dari tiga kategori perilaku '
    'dalam game engine (Kaplay.js):',
    style_body
))

cat_table = make_table(
    ['Kategori', 'Warna', 'Behavior Kaplay', 'Efek pada Gameplay'],
    [
        [Paragraph('<b>SOLID</b>', style_body_noindent),
         'Hijau',
         'Objek fungsional yang bisa diinjak/dilewati (collision=true, static=true)',
         'SUCCESS \u2014 Stickman bisa lewat'],
        [Paragraph('<b>DANGER</b>', style_body_noindent),
         'Merah',
         'Objek berbahaya yang merusak Stickman (damage=100)',
         'FAIL \u2014 Kertas sobek'],
        [Paragraph('<b>DEKORASI</b>', style_body_noindent),
         'Kuning',
         'Objek visual tanpa collision (no collision)',
         'NO EFFECT \u2014 Stickman mentok, FAIL jika diandalkan'],
    ],
    col_widths=[CONTENT_W * 0.15, CONTENT_W * 0.10, CONTENT_W * 0.40, CONTENT_W * 0.35]
)
story.append(Spacer(1, 6))
story.append(cat_table)
story.append(Spacer(1, 4))
story.append(Paragraph('Tabel 4.1 \u2014 Tiga kategori perilaku objek dalam game engine', style_caption))

story.append(Spacer(1, 8))

# 4.3 Tabel Behavior Mapping
story.append(Paragraph('4.3 Tabel Behavior Mapping (11 Label QuickDraw)', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Berikut adalah pemetaan lengkap 11 label QuickDraw ke kategori perilaku dan implementasi Kaplay.js:',
    style_body
))

bm_table = make_table(
    ['Label', 'Kategori', 'Behavior Kaplay', 'Level Aktif'],
    [
        ['tangga', 'Solid', 'static=true, walkable', '1, 2, 3'],
        ['jembatan', 'Solid', 'static=true, walkable', '1, 2, 3'],
        ['papan', 'Solid', 'static=true, walkable', '1, 2'],
        ['kunci', 'Solid', 'triggers door unlock', '2'],
        ['pedang', 'Danger', 'damage=100', '2, 3'],
        ['pisau', 'Danger', 'damage=100', '2, 3'],
        ['paku', 'Danger', 'damage=100', '2, 3'],
        ['awan', 'Dekorasi', 'no collision', '3'],
        ['bunga', 'Dekorasi', 'no collision', '3'],
        ['pelangi', 'Dekorasi', 'no collision', '3'],
        ['palu', 'Solid', 'destroys obstacle', '3'],
    ],
    col_widths=[CONTENT_W * 0.18, CONTENT_W * 0.14, CONTENT_W * 0.40, CONTENT_W * 0.28]
)
story.append(Spacer(1, 6))
story.append(bm_table)
story.append(Spacer(1, 4))
story.append(Paragraph('Tabel 4.2 \u2014 Behavior Mapping: 11 label QuickDraw ke implementasi Kaplay.js', style_caption))

story.append(Spacer(1, 8))

# 4.4 Kode Behavior Map
story.append(Paragraph('4.4 Kode Behavior Map (Kaplay.js)', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Berikut adalah implementasi behavior map dalam Kaplay.js yang mendefinisikan properti setiap objek '
    'yang dapat digambar oleh siswa:',
    style_body
))

code_text = '''const behaviorMap = {
  "tangga":    { type: "solid",   sprite: "ladder",  collision: true,  width: 80, height: 200 },
  "jembatan":  { type: "solid",   sprite: "bridge",  collision: true,  width: 200, height: 20 },
  "papan":     { type: "solid",   sprite: "plank",   collision: true,  width: 150, height: 20 },
  "kunci":     { type: "solid",   sprite: "key",     action: "unlock_door" },
  "pedang":    { type: "danger",  sprite: "sword",   damage: 100 },
  "pisau":     { type: "danger",  sprite: "knife",   damage: 100 },
  "paku":      { type: "danger",  sprite: "spikes",  damage: 100 },
  "awan":      { type: "deco",    sprite: "cloud",   collision: false },
  "bunga":     { type: "deco",    sprite: "flower",  collision: false },
  "pelangi":   { type: "deco",    sprite: "rainbow", collision: false },
  "palu":      { type: "solid",   sprite: "hammer",  action: "destroy_obstacle" }
};'''

story.append(Preformatted(code_text, style_code))

story.append(PageBreak())

# ───────────────────────────────────────────────────────────────
# BAB 5: IP STORY — ESCAPE THE SKETCHBOOK
# ───────────────────────────────────────────────────────────────
story.append(Paragraph('BAB 5: IP STORY \u2014 ESCAPE THE SKETCHBOOK', style_h1))
story.append(section_rule())

# 5.1 Sinopsis Narasi
story.append(Paragraph('5.1 Sinopsis Narasi', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Di sebuah buku sketsa yang ditinggalkan oleh Ilustrator lama, hiduplah Momo \u2014 gambar pertama yang '
    'berhasil hidup. Momo adalah "katalog berjalan" yang bisa mengenali setiap objek dalam buku sketsa. '
    'Karena tidak pernah dikoreksi selama bertahun-tahun hidup dalam isolasi, Momo tumbuh menjadi '
    'overconfident \u2014 bukan karena kesombongan, melainkan karena tidak pernah ada yang mengoreksinya.',
    style_body
))

story.append(Paragraph(
    'Stickman adalah gambar setengah hidup yang kaku dan tidak bisa bergerak bebas. Ia sadar, tapi tidak '
    'mampu berbuat apa-apa. Momo tidak bisa membantu Stickman karena Momo hanya bisa mengenali, bukan '
    'menciptakan.',
    style_body
))

story.append(Paragraph(
    'User memasuki cerita sebagai Ilustrator baru \u2014 satu-satunya yang bisa menggambar objek solid '
    'di dalam buku sketsa. Tujuan akhir mereka adalah mencapai <b>Pusat Halaman</b>, tempat legendaris '
    'di mana tinta tidak pernah kering dan Stickman bisa hidup sepenuhnya.',
    style_body
))

story.append(Spacer(1, 8))

# 5.2 Lima Babak + Epilog
story.append(Paragraph('5.2 Lima Babak + Epilog (Ringkasan)', style_h2))
story.append(Spacer(1, 4))

babak_table = make_table(
    ['Babak', 'Judul', 'Ringkasan'],
    [
        ['1', 'Asal-usul Momo',
         'Gambar pertama yang hidup, tumbuh sendirian, menjadi overconfident karena tidak pernah dikoreksi.'],
        ['2', 'Pertemuan dengan Stickman',
         'Makhluk yang hampir hidup. Momo tidak bisa membantu \u2014 ia hanya bisa mengenali, bukan menciptakan.'],
        ['3', 'Kedatangan Ilustrator Baru',
         'User datang sebagai Ilustrator baru. Override pertama terjadi \u2014 Momo dikoreksi untuk pertama kalinya.'],
        ['4', 'Perjalanan Menuju Pusat Halaman',
         'Level 1, 2, dan 3 dimainkan. Setiap level menguji aspek berbeda dari trust calibration siswa.'],
        ['5', 'Klimaks',
         'Stickman hidup sepenuhnya di Pusat Halaman. Momo menyadari bahwa dikoreksi bukanlah kelemahan.'],
        ['Epilog', 'Pesan Momo',
         '<i>"Aku tidak harus selalu benar. Yang penting, ada seseorang yang mau mengoreksiku."</i>'],
    ],
    col_widths=[CONTENT_W * 0.08, CONTENT_W * 0.25, CONTENT_W * 0.67]
)
story.append(babak_table)
story.append(Spacer(1, 4))
story.append(Paragraph('Tabel 5.1 \u2014 Ringkasan lima babak dan epilog narasi', style_caption))

story.append(Spacer(1, 8))

# 5.3 Keterhubungan Narasi-Gameplay
story.append(Paragraph('5.3 Keterhubungan Narasi-Gameplay', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Narasi dan gameplay dalam "Escape the Sketchbook" dirancang untuk saling memperkuat. Setiap mekanisme '
    'gameplay memiliki padanan naratif yang membuat pengalaman siswa lebih bermakna:',
    style_body
))

story.extend(bullet_list([
    '<b>Override = momen pertama Momo dikoreksi</b> \u2014 Secara naratif, ini adalah titik balik psikologis '
    'bagi Momo yang selama ini tidak pernah dikoreksi. Secara gameplay, ini mengukur kemampuan siswa '
    'untuk mengenali ketika AI salah.',
    '<b>Fail condition (kertas sobek)</b> \u2014 Konsekuensi nyata dari keputusan salah. Kertas sobek '
    'adalah visual metaphor bahwa keputusan yang salah memiliki dampak \u2014 bukan sekadar "coba lagi".',
    '<b>Momo\'s character arc</b> \u2014 Overconfident \u2192 Bingung \u2192 Rendah Hati \u2192 Bersyukur. '
    'Perubahan karakter Momo mencerminkan penurunan confidence AI sekaligus menunjukkan bahwa AI yang '
    'mengakui kesalahan adalah AI yang lebih "sehat".',
    '<b>Pesan tersirat</b> \u2014 AI tidak selalu akurat, dan manusia harus memegang kendali akhir. '
    'Pesan ini disampaikan melalui pengalaman, bukan melalui penjelasan tekstual.',
]))

story.append(PageBreak())

# ───────────────────────────────────────────────────────────────
# BAB 6: SISTEM DATA LOG
# ───────────────────────────────────────────────────────────────
story.append(Paragraph('BAB 6: SISTEM DATA LOG', style_h1))
story.append(section_rule())

# 6.1 Skema Data Log
story.append(Paragraph('6.1 Skema Data Log', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Setiap keputusan siswa selama simulasi dicatat dalam log data yang dikirim ke server. Skema data log '
    'dirancang untuk menangkap seluruh informasi yang diperlukan untuk analisis perilaku literasi AI:',
    style_body
))

log_table = make_table(
    ['Field', 'Tipe', 'Deskripsi'],
    [
        ['session_id', 'String', 'ID unik per sesi'],
        ['level_id', 'Integer', 'Level 1, 2, atau 3'],
        ['trial_number', 'Integer', 'Percobaan ke-berapa (untuk retry)'],
        ['ai_predictions', 'JSON', 'Top-3 prediksi + confidence scores'],
        ['user_decision', 'String', 'Label yang dipilih user'],
        ['decision_type', 'Enum', 'accept / correct / override'],
        ['confidence_scores', 'JSON', 'Confidence scores saat keputusan dibuat'],
        ['decision_latency_ms', 'Integer', 'Waktu dari tampilnya prediksi sampai keputusan (ms)'],
        ['outcome', 'Enum', 'success / fail'],
        ['timestamp', 'DateTime', 'Waktu keputusan dibuat'],
    ],
    col_widths=[CONTENT_W * 0.22, CONTENT_W * 0.12, CONTENT_W * 0.66]
)
story.append(Spacer(1, 6))
story.append(log_table)
story.append(Spacer(1, 4))
story.append(Paragraph('Tabel 6.1 \u2014 Skema data log keputusan siswa', style_caption))

story.append(Spacer(1, 8))

# 6.2 Metrik Evaluasi
story.append(Paragraph('6.2 Metrik Evaluasi', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Dari data log yang terkumpul, beberapa metrik evaluasi dihitung untuk mengukur literasi AI siswa. '
    'Penting untuk ditegaskan: <b>tidak ada pre-test atau post-test</b>. Evaluasi sepenuhnya berbasis '
    'behavioral logs (stealth assessment). Kesimpulan dihitung di dashboard peneliti, BUKAN di database.',
    style_body
))

metric_table = make_table(
    ['Metrik', 'Rumus/Definisi', 'Interpretasi'],
    [
        [Paragraph('<b>Override Rate</b>', style_body_noindent),
         'Persentase keputusan override per level',
         'Semakin tinggi di Level 3 = literasi AI lebih baik'],
        [Paragraph('<b>Decision Latency</b>', style_body_noindent),
         'Rata-rata waktu keputusan per level (ms)',
         'Latency tinggi + override = pertimbangan mendalam'],
        [Paragraph('<b>Confidence Gap</b>', style_body_noindent),
         'Selisih confidence Top-1 dan pilihan user',
         'Gap kecil = keputusan sesuai AI; gap besar = keputusan independen'],
        [Paragraph('<b>Trust Calibration Index</b>', style_body_noindent),
         'Metrik gabungan dari ketiga metrik di atas',
         'Indeks komposit yang mengukur keselarasan kepercayaan terhadap AI'],
    ],
    col_widths=[CONTENT_W * 0.22, CONTENT_W * 0.38, CONTENT_W * 0.40]
)
story.append(Spacer(1, 6))
story.append(metric_table)
story.append(Spacer(1, 4))
story.append(Paragraph('Tabel 6.2 \u2014 Metrik evaluasi perilaku literasi AI', style_caption))

story.append(Spacer(1, 8))

# 6.3 Dashboard Peneliti
story.append(Paragraph('6.3 Dashboard Peneliti', style_h2))
story.append(Spacer(1, 4))

story.append(Paragraph(
    'Dashboard peneliti menyajikan visualisasi dari data log yang terkumpul, memungkinkan analisis '
    'perilaku siswa secara agregat maupun individual. Tiga jenis visualisasi utama:',
    style_body
))

story.extend(numbered_list([
    '<b>Grafik Batang</b> \u2014 Rata-rata decision_latency per level. Memungkinkan perbandingan '
    'seberapa lama siswa berpikir di setiap level.',
    '<b>Pie Chart</b> \u2014 Proporsi accept/correct/override per level. Menunjukkan distribusi '
    'jenis keputusan dan pergeseran perilaku antar level.',
    '<b>Scatter Plot</b> \u2014 Confidence gap (sumbu X) vs decision latency (sumbu Y), dengan '
    'warna berdasarkan decision_type. Memungkinkan identifikasi pola hubungan antara kepercayaan '
    'diri siswa dan kecepatan keputusan.',
]))

story.append(PageBreak())

# ───────────────────────────────────────────────────────────────
# BAB 7: REFERENSI AKADEMIK
# ───────────────────────────────────────────────────────────────
story.append(Paragraph('BAB 7: REFERENSI AKADEMIK', style_h1))
story.append(section_rule())

# 7.1 Referensi Utama
story.append(Paragraph('7.1 Referensi Utama', style_h2))
story.append(Spacer(1, 6))

story.append(Paragraph('<b>HITL Systems</b>', style_h3))
refs_hitl = [
    'Memarian, K., & Doleck, T. (2024). Human-in-the-loop in AI in education: A review. <i>Computers in Human Behavior: Artificial Humans</i>.',
    'Mosqueira-Rey, E., et al. (2023). Human-in-the-loop machine learning: A state of the art. <i>Artificial Intelligence Review</i>, 56, 6053\u20136116.',
    'Kumar, A., et al. (2024). Applications, challenges, and future directions of human-in-the-loop learning. <i>IEEE Access</i>.',
    'Natarajan, S., et al. (2025). Human-in-the-loop or AI-in-the-loop? <i>AAAI Conference on Artificial Intelligence</i>.',
]
for r in refs_hitl:
    story.append(Paragraph(r, style_ref))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>AI Literacy &amp; K-12 Education</b>', style_h3))
refs_ai_lit = [
    'Casal-Otero, V., et al. (2023). AI literacy in K-12: A systematic literature review. <i>International Journal of STEM Education</i>, 10, 1\u201318.',
    'Wang, N., & Lester, J. (2023). K-12 AI literacy: A call to action. <i>International Journal of Artificial Intelligence in Education</i>.',
    'Yim, M., & Su, Y.-S. (2025). AI literacy education in primary schools: A systematic review. <i>International Journal of Technology in Design Education</i>.',
    'Yim, M., & Su, Y.-S. (2024). AI learning tools in K-12: A meta-analysis. <i>Journal of Computers in Education</i>.',
    'Tan, X., & Tang, K. Y. (2025). Unveiling AI literacy in K-12: A scoping review. <i>Interactive Learning Environments</i>.',
    'Chung, Y., et al. (2025). AI literacy diagnostic tool for elementary students. <i>Education and Information Technologies</i>.',
    'Zhou, Q., et al. (2025). Defining, enhancing, and assessing AI literacy in K-12: A review. <i>Interactive Learning Environments</i>.',
]
for r in refs_ai_lit:
    story.append(Paragraph(r, style_ref))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Computational Thinking</b>', style_h3))
refs_ct = [
    'Shamir, A., & Levin, I. (2020). Transformations of computational thinking practices in elementary school. <i>EDULEARN Proceedings</i>.',
    'Jeon, J., et al. (2024). Staged framework for computer vision education. <i>Applied Sciences</i>.',
    'Wu, B., & Su, Y.-S. (2021). Visual programming environments and computational thinking. <i>Journal of Educational Computing Research</i>.',
    'Hsu, T.-C., & Lin, H.-W. (2025). Effects of integrating AI image recognition and robot game-based learning on CT. <i>Educational Technology & Society</i>.',
]
for r in refs_ct:
    story.append(Paragraph(r, style_ref))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Probabilistic Thinking &amp; Trust</b>', style_h3))
refs_prob = [
    'Reyes, M. F., et al. (2025). Trusting AI: Does uncertainty visualization affect decision-making? <i>Frontiers in Computer Science</i>.',
    'Yin, M., et al. (2019). Understanding the effect of accuracy on trust in machine learning models. <i>Proceedings of CHI 2019</i>.',
    'Batanero, C., & \u00c1lvarez-Arroyo, R. (2023). Teaching and learning of probability. <i>ZDM Mathematics Education</i>.',
]
for r in refs_prob:
    story.append(Paragraph(r, style_ref))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Explainable AI (XAI) in Education</b>', style_h3))
refs_xai = [
    'Feldman-Maggor, Y., et al. (2025). Impact of XAI on teachers\' trust in AI-driven educational tools. <i>International Journal of Artificial Intelligence in Education</i>.',
    'Khosravi, H., et al. (2022). Explainable artificial intelligence in education. <i>Computers and Education: Artificial Intelligence</i>.',
    'Liao, Q. V., et al. (2020). Questioning the AI: Informing design practices for explainable AI user experiences. <i>Proceedings of CHI 2020</i>.',
]
for r in refs_xai:
    story.append(Paragraph(r, style_ref))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Game-Based Learning</b>', style_h3))
refs_gbl = [
    'Zhan, Z., et al. (2024). Game-based learning in AI education: A systematic review. <i>Interactive Learning Environments</i>.',
    'Lee, J., et al. (2021). AI-infused collaborative inquiry learning. <i>AAAI Conference on Artificial Intelligence</i>.',
    'Gupta, A., et al. (2024). Story-driven game-based learning for AI education. <i>AAAI Conference on Artificial Intelligence</i>.',
    'Gong, Y., et al. (2026). LLM-based scaffolding in digital game-based learning. <i>Journal of Educational Computing Research</i>.',
]
for r in refs_gbl:
    story.append(Paragraph(r, style_ref))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Sketch Recognition</b>', style_h3))
refs_sketch = [
    'Li, C., et al. (2020). Sketch-R2CNN: An attention-based LSTM-RNN architecture for sketch recognition. <i>IEEE Transactions on Pattern Analysis and Machine Intelligence</i>.',
    'Kabakus, A. T. (2020). Sketch recognition CNN. <i>IEEE HORA Conference</i>.',
    'Huynh, C. P., et al. (2023). Lightweight sketch recognition for educational applications. <i>IEEE IPPR Conference</i>.',
]
for r in refs_sketch:
    story.append(Paragraph(r, style_ref))

story.append(Spacer(1, 8))

# 7.2 Referensi Tambahan
story.append(Paragraph('7.2 Referensi Tambahan', style_h2))
story.append(Spacer(1, 4))

refs_addl = [
    'Mehrotra, S., et al. (2024). A systematic review on fostering appropriate trust in human-AI interaction. <i>ACM Journal of Responsible Computing</i>, 1(3), Article 21.',
    'Romeo, G., & Conti, D. (2025). Exploring automation bias in human\u2013AI collaboration. <i>AI & Society</i>, 41, 259\u2013278.',
    'Klingbeil, A., et al. (2024). Trust and reliance on AI: An experimental study on overreliance. <i>Computers in Human Behavior</i>, 160, Article 108352.',
    'Karran, A. J., et al. (2022). Designing for confidence: The impact of visualizing AI decisions. <i>Frontiers in Neuroscience</i>, 16, Article 883385.',
    'Muralidhar, D., et al. (2025). Operationalizing selective transparency using progressive disclosure in AI systems. <i>International Journal of Human-Computer Studies</i>, 200, Article 103591.',
    'Lee, S.-S., et al. (2024). Differences in student-AI interaction process on a drawing task. <i>Australasian Journal of Educational Technology</i>, 40(1).',
    'Ma, M., et al. (2025). Fostering responsible AI literacy: A systematic review of K-12 AI ethics education. <i>Computers and Education: Artificial Intelligence</i>, 8, Article 100422.',
    'Shute, V. J., et al. (2023). Stealth assessment: A theoretically grounded and psychometrically sound method. <i>Educational Technology Research and Development</i>, 71, 1125\u20131152.',
    'Bucinca, Z., et al. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI. <i>Proceedings of the ACM on Human-Computer Interaction</i>, 5(CSCW1), Article 188.',
    'He, S., & Xin, Y. P. (2025). Design knowledge scaffolds to facilitate students\' probabilistic thinking skills. <i>Thinking Skills and Creativity</i>, 58, Article 101928.',
]
for r in refs_addl:
    story.append(Paragraph(r, style_ref))


# ═══════════════════════════════════════════════════════════════
# PAGE NUMBER CALLBACK
# ═══════════════════════════════════════════════════════════════
def add_page_number(canvas, doc):
    """Add page number at bottom center."""
    page_num = canvas.getPageNumber()
    text = f"{page_num}"
    canvas.saveState()
    canvas.setFont('Carlito', 9)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawCentredString(PAGE_W / 2, MARGIN / 2, text)
    canvas.restoreState()


# ═══════════════════════════════════════════════════════════════
# BUILD
# ═══════════════════════════════════════════════════════════════
doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print(f"Body PDF generated: {OUTPUT_PATH}")
