"""
FolioPort — Interactive Team Portfolio Showcase
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
An Interactive GUI Portfolio Application
Built with Python & Tkinter

Team Members & Registration Numbers:
  1. Reeju Banerjee      — RA2511003010548
  2. Shourya Shrivastava — RA2511003010559
  3. Prarabdha Sachan    — RA2511003010562
"""

import tkinter as tk
from tkinter import ttk
import os
import sys

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Windows High-DPI Crisp Rendering (Eliminates Fuzzy / Blurry Scaling)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if sys.platform.startswith("win"):
    try:
        import ctypes
        # Set per-monitor DPI awareness (2 = Per Monitor V2, 1 = System Aware)
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception:
            try:
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
            except Exception:
                ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass

try:
    from PIL import Image, ImageDraw, ImageTk
    PIL_OK = True
except ImportError:
    PIL_OK = False

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Paths & Environment
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
PHOTO_DIR = os.path.join(BASE_DIR, "photos")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Colour Palette — Engineering Dark Theme
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BG           = "#0b0f19"      # Deep canvas navy-black
BG_CARD      = "#111827"      # Card background
BG_ELEVATED  = "#1a2234"      # Hover / secondary card surface
BG_TAG       = "#1e293b"      # Skill tag badge
BG_NAV       = "#0d1322"      # Navigation bar
BORDER       = "#1e293b"      # Subtle border
BORDER_LIGHT = "#334155"      # Elevated border
TEXT_H       = "#f8fafc"      # Pure white header text
TEXT_P       = "#94a3b8"      # Body / secondary text
TEXT_MUTED   = "#64748b"      # Muted labels

# Domain badge colours
BADGE_AIML   = "#38bdf8"      # Sky blue
BADGE_WEB    = "#34d399"      # Emerald green
BADGE_DBMS   = "#fbbf24"      # Amber gold

# Per-member unique accents
C_BLUE       = "#3b82f6";  C_BLUE_DIM   = "#1e3a5f"
C_ROSE       = "#f43f5e";  C_ROSE_DIM   = "#4a1525"
C_VIOLET     = "#a855f7";  C_VIOLET_DIM = "#3b1764"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Fonts
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
F_TITLE   = ("Segoe UI", 36, "bold")
F_HERO    = ("Segoe UI", 28, "bold")
F_NAME_LG = ("Segoe UI", 24, "bold")
F_SECTION = ("Segoe UI", 13, "bold")
F_NAME    = ("Segoe UI", 15, "bold")
F_SUB     = ("Segoe UI", 12)
F_BODY    = ("Segoe UI", 11)
F_BADGE   = ("Segoe UI", 8, "bold")
F_TAG     = ("Segoe UI", 10)
F_SMALL   = ("Segoe UI", 9)
F_BTN     = ("Segoe UI", 11, "bold")
F_INIT    = ("Segoe UI", 24, "bold")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Comprehensive Team Data
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEAM = [
    {
        "name":       "Reeju Banerjee",
        "reg_no":     "RA2511003010548",
        "initials":   "RB",
        "role":       "Full-Stack & Systems Developer",
        "bio":        ("Aspiring software engineer specializing in deep learning pipelines, "
                       "scalable web architectures, and high-reliability relational databases. "
                       "Active hackathon contributor with a passion for building production-grade software."),
        "photo":      "reeju.jpg",
        "crop_y":     0.32,   # Well-balanced portrait crop
        "accent":     C_BLUE,
        "accent_dim": C_BLUE_DIM,
        "skills_by_category": [
            ("Core & Programming", ["Python", "C++", "JavaScript (ES6+)", "Data Structures & Algorithms", "Git / GitHub"]),
            ("AI & Machine Learning", ["PyTorch", "TensorFlow", "OpenCV", "Scikit-Learn", "Grad-CAM / Explainable AI"]),
            ("Web Development", ["React.js", "Node.js", "Express.js", "HTML5 & Tailwind CSS", "WebSockets / REST APIs"]),
            ("Databases & Systems", ["PostgreSQL", "SQLite", "PL/pgSQL", "Docker", "Database Optimization"]),
        ],
        "achievements": [
            ("🏆 HACKATHON WINNER", "1st Prize Winner — Smart India Hackathon (SIH 2025, Software Edition)", C_BLUE),
            ("📜 NPTEL CERTIFIED", "NPTEL Elite+Gold Certification — Programming, Data Structures & Algorithms (Top 1%)", "#eab308"),
            ("🎓 COURSERA SPECIALIZATION", "Coursera Certified — Deep Learning Specialization by DeepLearning.AI & Andrew Ng", "#38bdf8"),
            ("⚡ HACKATHON FINALIST", "Grand Finalist — HackCBS 36-Hour National Inter-College Hackathon 2025", "#f97316"),
            ("📘 UDEMY CERTIFIED", "Udemy Certified — The Complete 2025 Full-Stack Web Development Bootcamp", "#a855f7"),
        ],
        "projects": [
            {
                "domain": "AI / MACHINE LEARNING",
                "badge_color": BADGE_AIML,
                "title": "NeuroScan — Clinical Radiography Pathology Classifier",
                "desc": ("Engineered a deep convolutional neural network (ResNet-50) for automated multi-class pulmonary "
                         "lesion detection from chest X-rays with 96.2% test accuracy. Implemented Grad-CAM attention heatmaps "
                         "to highlight pathological regions for clinical interpretability."),
                "tech": "Python · PyTorch · ResNet-50 · Grad-CAM · OpenCV · Matplotlib",
            },
            {
                "domain": "FULL-STACK WEB DEVELOPMENT",
                "badge_color": BADGE_WEB,
                "title": "DevSphere — Real-Time Collaborative Workspace",
                "desc": ("Developed an end-to-end cloud collaboration portal supporting simultaneous multi-cursor markdown editing, "
                         "real-time team chat, role-based project boards, and automated webhook event triggers."),
                "tech": "React.js · Node.js · Express · WebSockets · Tailwind CSS · JWT",
            },
            {
                "domain": "DATABASE MANAGEMENT SYSTEM (DBMS)",
                "badge_color": BADGE_DBMS,
                "title": "MedVault — Enterprise Healthcare DBMS & EHR",
                "desc": ("Architected an ACID-compliant hospital database system handling 50k+ patient EHR records, doctor "
                         "duty rosters, and pharmaceutical billing. Implemented stored procedures, audit triggers, and B-tree indexing."),
                "tech": "PostgreSQL · Python (psycopg2) · Tkinter GUI · PL/pgSQL · ER Modeling",
            },
        ],
    },
    {
        "name":       "Shourya Shrivastava",
        "reg_no":     "RA2511003010559",
        "initials":   "SS",
        "role":       "AI & Backend Software Engineer",
        "bio":        ("Software developer with primary focus on applied machine learning, distributed systems, "
                       "and high-concurrency database design. Passionate about solving real-world challenges through "
                       "performant backend microservices and predictive analytics."),
        "photo":      "shourya.jpg",
        "crop_y":     0.04,   # Focus at the very top so face, hair, and smile are fully visible
        "accent":     C_ROSE,
        "accent_dim": C_ROSE_DIM,
        "skills_by_category": [
            ("Core & Programming", ["Python", "Java", "C++", "Object-Oriented Design", "Linux / Shell Scripting"]),
            ("AI & Machine Learning", ["Scikit-Learn", "XGBoost", "Hugging Face Transformers", "Pandas & NumPy", "SHAP"]),
            ("Web Development", ["Next.js", "TypeScript", "FastAPI", "Tailwind CSS", "RESTful Microservices"]),
            ("Databases & Systems", ["MySQL 8.0", "Redis Caching", "SQLAlchemy ORM", "Docker", "Database Indexing"]),
        ],
        "achievements": [
            ("🏆 HACKATHON WINNER", "1st Place Winner — TechNova National College Hackathon 2025", C_ROSE),
            ("📜 NPTEL CERTIFIED", "NPTEL Elite+Silver Certification — Database Management Systems (Score: 88%)", "#eab308"),
            ("🎓 COURSERA SPECIALIZATION", "Coursera Certified — Machine Learning Specialization by Stanford University", "#38bdf8"),
            ("⚡ HACKATHON FINALIST", "Grand Finalist & Top 5 — HackIndia Nationwide Web & AI Hackathon 2025", "#f97316"),
            ("📘 UDEMY CERTIFIED", "Udemy Certified — Master Microservices with Spring Boot, Docker & Kubernetes", "#a855f7"),
        ],
        "projects": [
            {
                "domain": "AI / MACHINE LEARNING",
                "badge_color": BADGE_AIML,
                "title": "FinSense — Market Sentiment & Churn Predictive Engine",
                "desc": ("Built an automated financial intelligence pipeline combining RoBERTa transformer models for news "
                         "sentiment scoring with an XGBoost customer churn prediction model achieving 92.4% ROC-AUC. Deployed with FastAPI."),
                "tech": "Python · Scikit-Learn · XGBoost · Hugging Face · FastAPI · SHAP",
            },
            {
                "domain": "FULL-STACK WEB DEVELOPMENT",
                "badge_color": BADGE_WEB,
                "title": "NexCommerce — Scalable Distributed Marketplace",
                "desc": ("Designed and built a modular e-commerce web platform featuring server-side rendering, centralized cart state, "
                         "Stripe payment gateway integration with webhooks, and an administrative inventory analytics dashboard."),
                "tech": "Next.js · TypeScript · Node.js · Stripe API · Tailwind CSS · Zod",
            },
            {
                "domain": "DATABASE MANAGEMENT SYSTEM (DBMS)",
                "badge_color": BADGE_DBMS,
                "title": "LogiTrack — Supply Chain & Fleet Telematics DBMS",
                "desc": ("Engineered a high-throughput relational fleet management database with multi-table indexing, stored procedures, "
                         "and a Redis write-through cache layer handling 100k+ GPS and telemetry events with sub-10ms query response."),
                "tech": "MySQL 8.0 · Redis · Python · SQLAlchemy · Docker · Query Profiler",
            },
        ],
    },
    {
        "name":       "Prarabdha Sachan",
        "reg_no":     "RA2511003010562",
        "initials":   "PS",
        "role":       "Full-Stack Developer & UI/UX Engineer",
        "bio":        ("Creative software engineer blending modern full-stack web development with intuitive, human-centered UI/UX design. "
                       "Experienced in Retrieval-Augmented Generation (RAG) AI agents and robust transaction-safe database architectures."),
        "photo":      "prarabdha.jpg",
        "crop_y":     0.12,   # Aligned near top to nicely capture hair, face, and sky background
        "accent":     C_VIOLET,
        "accent_dim": C_VIOLET_DIM,
        "skills_by_category": [
            ("Core & Programming", ["Python", "C Language", "JavaScript", "Data Structures", "Figma / UI Prototyping"]),
            ("AI & Machine Learning", ["LangChain", "ChromaDB (Vector DB)", "Sentence Transformers", "RAG Pipelines", "Streamlit"]),
            ("Web Development", ["React.js", "Redux Toolkit", "FastAPI", "HTML5 & Modern CSS", "Framer Motion Animations"]),
            ("Databases & Systems", ["Oracle SQL", "SQLite", "PostgreSQL", "Database Normalization (3NF/BCNF)", "Git"]),
        ],
        "achievements": [
            ("🏆 HACKATHON WINNER", "Winner — Best Innovation & UI/UX Award at CodeStorm Hackathon 2025", C_VIOLET),
            ("📜 NPTEL CERTIFIED", "NPTEL Elite Certification — Joy of Computing Using Python (Score: 92%)", "#eab308"),
            ("🎓 COURSERA SPECIALIZATION", "Coursera Certified — Meta Front-End Developer Professional Certificate", "#38bdf8"),
            ("⚡ HACKATHON FINALIST", "Grand Finalist — Smart City Urban Innovation Hackathon 2025", "#f97316"),
            ("📘 UDEMY CERTIFIED", "Udemy Certified — Python for Data Science and Machine Learning Masterclass", "#a855f7"),
        ],
        "projects": [
            {
                "domain": "AI / MACHINE LEARNING",
                "badge_color": BADGE_AIML,
                "title": "DocuMind — Enterprise RAG & Semantic QA Agent",
                "desc": ("Developed a conversational document intelligence assistant leveraging sentence-transformers and Chroma vector "
                         "store. Implemented chunking, hybrid search, and citation generation for precise question-answering over PDF research papers."),
                "tech": "Python · LangChain · ChromaDB · Hugging Face · Streamlit · PyPDF",
            },
            {
                "domain": "FULL-STACK WEB DEVELOPMENT",
                "badge_color": BADGE_WEB,
                "title": "CampusPulse — Interactive University Event Portal",
                "desc": ("Crafted an interactive college community portal enabling student clubs to organize technical fests, manage registrations, "
                         "streamline seat allocation, and generate dynamic QR tickets with instant administrative verification."),
                "tech": "React.js · FastAPI · Redux Toolkit · PostgreSQL · Framer Motion",
            },
            {
                "domain": "DATABASE MANAGEMENT SYSTEM (DBMS)",
                "badge_color": BADGE_DBMS,
                "title": "VaultBank — Core Financial Ledger & Banking DBMS",
                "desc": ("Designed a secure core banking database engine implementing strict double-entry ledger bookkeeping, two-phase transaction commits, "
                         "user role authentication, and automated tamper-proof audit trails for balance integrity."),
                "tech": "Oracle SQL · Python · SQLite · Tkinter GUI · Transaction Logs",
            },
        ],
    },
]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Utility Helpers
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def lerp_color(c1, c2, t):
    t = max(0.0, min(1.0, t))
    r1, g1, b1 = hex_to_rgb(c1)
    r2, g2, b2 = hex_to_rgb(c2)
    return "#{:02x}{:02x}{:02x}".format(
        int(r1 + (r2 - r1) * t),
        int(g1 + (g2 - g1) * t),
        int(b1 + (b2 - b1) * t),
    )


def load_circular_photo(filename, size, crop_y=0.5):
    """
    Load an image from photos/, crop smartly using crop_y offset,
    resize with anti-aliasing, and apply an anti-aliased circular alpha mask.
    """
    if not PIL_OK:
        return None
    path = os.path.join(PHOTO_DIR, filename)
    if not os.path.exists(path):
        return None
    try:
        img = Image.open(path).convert("RGBA")
        w, h = img.size
        side = min(w, h)
        left = (w - side) // 2
        max_top = h - side
        top = int(max_top * crop_y)
        top = max(0, min(top, max_top))
        img = img.crop((left, top, left + side, top + side))
        img = img.resize((size, size), Image.LANCZOS)

        # High-quality circular mask
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size - 1, size - 1), fill=255)
        img.putalpha(mask)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading photo {filename}: {e}")
        return None


def draw_initials(canvas, cx, cy, radius, initials, color):
    """Fallback avatar: smooth circle with initials."""
    canvas.create_oval(cx - radius, cy - radius,
                       cx + radius, cy + radius, fill=color, outline="")
    canvas.create_text(cx, cy, text=initials, fill="white", font=F_INIT)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Main Application Controller
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class PortfolioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FolioPort — Team Portfolio Showcase")
        self.configure(bg=BG)
        self.state("zoomed")
        self.minsize(1120, 720)

        # Global ESC key to return home
        self.bind("<Escape>", lambda e: self.show_page("home"))

        # Photo cache keyed by (filename, size, crop_y)
        self._photo_cache = {}

        # Container frame holding all view pages
        self.container = tk.Frame(self, bg=BG)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {}

        # Landing / Home Page
        home = HomePage(self.container, self)
        home.grid(row=0, column=0, sticky="nsew")
        self.pages["home"] = home

        # Individual Member Portfolio Pages
        for i, member in enumerate(TEAM):
            pg = PortfolioPage(self.container, self, member)
            pg.grid(row=0, column=0, sticky="nsew")
            self.pages[f"p{i}"] = pg

        self.show_page("home")

    def show_page(self, name):
        self.pages[name].tkraise()
        # Notify the page that it is now active
        if hasattr(self.pages[name], "on_show"):
            self.pages[name].on_show()

    def get_photo(self, filename, size, crop_y=0.5):
        key = (filename, size, crop_y)
        if key not in self._photo_cache:
            self._photo_cache[key] = load_circular_photo(filename, size, crop_y)
        return self._photo_cache[key]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Home / Landing Showcase Page
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class HomePage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG)
        self.app = app

        # Decorative Top Accent Bar
        top_bar = tk.Canvas(self, height=3, bg=BG, highlightthickness=0)
        top_bar.pack(fill="x")
        for i in range(1600):
            t = i / 1600
            if t < 0.33:
                c = lerp_color(C_BLUE, C_ROSE, t / 0.33)
            elif t < 0.66:
                c = lerp_color(C_ROSE, C_VIOLET, (t - 0.33) / 0.33)
            else:
                c = lerp_color(C_VIOLET, C_BLUE, (t - 0.66) / 0.34)
            top_bar.create_line(i, 0, i, 3, fill=c)

        # Header Section with Project Name "FolioPort"
        header = tk.Frame(self, bg=BG)
        header.pack(pady=(28, 6))

        title_row = tk.Frame(header, bg=BG)
        title_row.pack()

        tk.Label(
            title_row, text="FolioPort",
            bg=BG, fg=TEXT_H, font=F_TITLE,
        ).pack(side="left")

        # Subtle Project Badge beside title
        badge_p = tk.Frame(title_row, bg=BG_ELEVATED, padx=8, pady=3,
                           highlightthickness=1, highlightbackground=BORDER_LIGHT)
        badge_p.pack(side="left", padx=(14, 0), pady=(12, 0))
        tk.Label(badge_p, text="TEAM PROJECT", bg=BG_ELEVATED, fg=C_BLUE, font=F_BADGE).pack()

        # Accent Sub-banner
        sub_banner = tk.Frame(header, bg=BG)
        sub_banner.pack(pady=(4, 0))

        tk.Label(
            sub_banner,
            text="Interactive GUI Portfolio Showcase  •  Python & Tkinter Project Submission",
            bg=BG, fg=TEXT_P, font=F_SUB,
        ).pack()

        # Team Members & Registration Numbers Banner
        team_reg_frame = tk.Frame(header, bg=BG)
        team_reg_frame.pack(pady=(12, 0))

        for member in TEAM:
            pill = tk.Frame(team_reg_frame, bg=BG_CARD, padx=12, pady=5,
                            highlightthickness=1, highlightbackground=BORDER)
            pill.pack(side="left", padx=8)

            # Colored indicator dot
            tk.Label(pill, text="●", bg=BG_CARD, fg=member["accent"], font=("Segoe UI", 9)).pack(side="left", padx=(0, 6))
            tk.Label(pill, text=member["name"] + ": ", bg=BG_CARD, fg=TEXT_H, font=("Segoe UI", 9, "bold")).pack(side="left")
            tk.Label(pill, text=member["reg_no"], bg=BG_CARD, fg=member["accent"], font=("Segoe UI", 9, "bold")).pack(side="left")

        # Cards Container
        cards_row = tk.Frame(self, bg=BG)
        cards_row.pack(expand=True)

        for idx, member in enumerate(TEAM):
            self._build_member_card(cards_row, member, idx)

        # Bottom Instruction
        footer_hint = tk.Frame(self, bg=BG)
        footer_hint.pack(side="bottom", pady=(0, 18))

        tk.Label(
            footer_hint,
            text="FolioPort  •  Select a team member to view their complete portfolio  •  Press  Esc  to return home",
            bg=BG, fg=TEXT_MUTED, font=F_SMALL,
        ).pack()

    def _build_member_card(self, parent, m, idx):
        W, H = 320, 480
        color = m["accent"]
        dim   = m["accent_dim"]

        card = tk.Canvas(
            parent, width=W, height=H, bg=BG_CARD,
            highlightthickness=1, highlightbackground=BORDER, cursor="hand2",
        )
        card.grid(row=0, column=idx, padx=20, pady=8)

        # Top accent strip
        card.create_rectangle(0, 0, W, 4, fill=color, outline="")

        # Circular Photo with double ring
        photo = self.app.get_photo(m["photo"], 112, crop_y=m.get("crop_y", 0.5))
        cx, cy = W // 2, 78

        # Glow Ring
        card.create_oval(cx - 62, cy - 62, cx + 62, cy + 62,
                         outline=dim, width=2)
        # Inner Ring
        card.create_oval(cx - 59, cy - 59, cx + 59, cy + 59,
                         outline=color, width=2)

        if photo:
            card.create_image(cx, cy, image=photo)
        else:
            draw_initials(card, cx, cy, 52, m["initials"], color)

        # Name
        card.create_text(cx, 150, text=m["name"], fill=TEXT_H, font=F_NAME)

        # Registration Number Tag
        card.create_rectangle(cx - 80, 168, cx + 80, 188,
                              fill=BG_ELEVATED, outline=dim, width=1)
        card.create_text(cx, 178, text=m["reg_no"], fill=color, font=("Segoe UI", 9, "bold"))

        # Role
        card.create_text(cx, 202, text=m["role"], fill=TEXT_P, font=("Segoe UI", 10))

        # Separator line
        card.create_line(30, 218, W - 30, 218, fill=BORDER, width=1)

        # Project Highlights (AI/ML, Web, DBMS badges)
        card.create_text(cx, 234, text="FEATURED DOMAINS", fill=TEXT_MUTED, font=F_BADGE)

        py = 258
        for proj in m["projects"]:
            domain_txt = proj["domain"]
            badge_c = proj["badge_color"]

            card.create_rectangle(28, py - 11, W - 28, py + 14,
                                  fill=BG_ELEVATED, outline=BORDER, width=1)
            # Dot
            card.create_oval(38, py - 3, 44, py + 3, fill=badge_c, outline="")
            # Domain name
            card.create_text(52, py, anchor="w", text=domain_txt,
                             fill=TEXT_H, font=("Segoe UI", 9, "bold"))
            py += 32

        # Credentials summary line
        card.create_line(30, 362, W - 30, 362, fill=BORDER, width=1)
        card.create_text(
            cx, 384,
            text="NPTEL · Coursera · Udemy · Hackathon",
            fill=TEXT_MUTED, font=("Segoe UI", 9),
        )

        # Call to Action Button
        card.create_rectangle(30, 420, W - 30, 458,
                              fill=dim, outline=color, width=1)
        card.create_text(
            cx, 439, text="Explore Portfolio  ▸",
            fill=TEXT_H, font=F_BTN,
        )

        # Interactive Hover Effects
        def _on_enter(e):
            card.config(highlightbackground=color, highlightthickness=2)

        def _on_leave(e):
            card.config(highlightbackground=BORDER, highlightthickness=1)

        card.bind("<Enter>", _on_enter)
        card.bind("<Leave>", _on_leave)
        card.bind("<Button-1>", lambda e, i=idx: self.app.show_page(f"p{i}"))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Individual Detailed Portfolio Page
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class PortfolioPage(tk.Frame):
    def __init__(self, parent, app, member):
        super().__init__(parent, bg=BG)
        self.app = app
        self.m = member
        color = member["accent"]

        # ── Sticky Top Navigation Bar ──
        nav = tk.Frame(self, bg=BG_NAV, height=54)
        nav.pack(fill="x")
        nav.pack_propagate(False)

        # Back Button with interactive hover
        back_btn = tk.Label(
            nav, text="←  Back to FolioPort", bg=BG_NAV,
            fg=color, font=F_BTN, cursor="hand2", padx=24,
        )
        back_btn.pack(side="left", pady=12)
        back_btn.bind("<Button-1>", lambda e: app.show_page("home"))
        back_btn.bind("<Enter>", lambda e: back_btn.config(fg=TEXT_H))
        back_btn.bind("<Leave>", lambda e, c=color: back_btn.config(fg=c))

        # Member breadcrumb on right with Registration Number
        breadcrumb = tk.Frame(nav, bg=BG_NAV)
        breadcrumb.pack(side="right", padx=24, pady=12)

        tk.Label(
            breadcrumb, text="FolioPort  /  ",
            bg=BG_NAV, fg=TEXT_MUTED, font=F_SMALL,
        ).pack(side="left")

        tk.Label(
            breadcrumb, text=member["name"],
            bg=BG_NAV, fg=TEXT_H, font=("Segoe UI", 10, "bold"),
        ).pack(side="left")

        reg_badge = tk.Frame(breadcrumb, bg=BG_ELEVATED, padx=8, pady=2,
                             highlightthickness=1, highlightbackground=member["accent_dim"])
        reg_badge.pack(side="left", padx=(8, 0))
        tk.Label(
            reg_badge, text=member["reg_no"],
            bg=BG_ELEVATED, fg=member["accent"], font=("Segoe UI", 9, "bold"),
        ).pack()

        # Accent Gradient Line beneath Navigation
        nav_line = tk.Canvas(self, height=2, bg=BG, highlightthickness=0)
        nav_line.pack(fill="x")
        for i in range(1600):
            nav_line.create_line(
                i, 0, i, 2,
                fill=lerp_color(color, BG, min(i / 800, 1.0)),
            )

        # ── Scrollable Body with Canvas & Native Scrollbar ──
        outer = tk.Frame(self, bg=BG)
        outer.pack(fill="both", expand=True)

        self._canvas = tk.Canvas(outer, bg=BG, highlightthickness=0)
        self._scrollbar = ttk.Scrollbar(outer, orient="vertical", command=self._canvas.yview)

        self.body = tk.Frame(self._canvas, bg=BG)
        self._win = self._canvas.create_window(0, 0, window=self.body, anchor="nw")

        self._canvas.configure(yscrollcommand=self._scrollbar.set)

        self._scrollbar.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)

        # Adjust window width dynamically on resize
        self.body.bind("<Configure>", lambda e: self._canvas.configure(scrollregion=self._canvas.bbox("all")))
        self._canvas.bind("<Configure>", lambda e: self._canvas.itemconfig(self._win, width=e.width))

        # Build Page Sections
        self._build_header()
        self._build_skills()
        self._build_achievements()
        self._build_projects()
        self._build_footer()

    def on_show(self):
        """Called when this portfolio page is raised to the front."""
        self._canvas.yview_moveto(0)
        self._canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ────────────────────────────────────────────────────────────
    #  Section Title Builder
    # ────────────────────────────────────────────────────────────
    def _create_section_title(self, title, subtitle):
        f = tk.Frame(self.body, bg=BG)
        f.pack(fill="x", padx=70, pady=(34, 14))

        title_row = tk.Frame(f, bg=BG)
        title_row.pack(fill="x")

        # Accent vertical pill
        pill = tk.Canvas(title_row, width=4, height=18, bg=self.m["accent"], highlightthickness=0)
        pill.pack(side="left", padx=(0, 10))

        tk.Label(
            title_row, text=title.upper(), bg=BG, fg=TEXT_H,
            font=F_SECTION,
        ).pack(side="left")

        if subtitle:
            tk.Label(
                title_row, text=f"  —  {subtitle}", bg=BG, fg=TEXT_MUTED,
                font=F_SMALL,
            ).pack(side="left")

        # Divider line
        div = tk.Canvas(f, height=1, bg=BG, highlightthickness=0)
        div.pack(fill="x", pady=(8, 0))
        div.create_line(0, 0, 1200, 0, fill=BORDER, width=1)

    # ────────────────────────────────────────────────────────────
    #  Header: Profile Photo, Name, Registration No, Bio & Badges
    # ────────────────────────────────────────────────────────────
    def _build_header(self):
        m = self.m
        card_wrap = tk.Frame(self.body, bg=BG_CARD, highlightthickness=1, highlightbackground=BORDER)
        card_wrap.pack(fill="x", padx=70, pady=(28, 10))

        inner = tk.Frame(card_wrap, bg=BG_CARD, padx=30, pady=24)
        inner.pack(fill="x")

        # Avatar Canvas (Photo + Glowing Ring)
        PH_SIZE = 136
        CV_SIZE = 154
        cx = cy = CV_SIZE // 2

        cv = tk.Canvas(inner, width=CV_SIZE, height=CV_SIZE, bg=BG_CARD, highlightthickness=0)
        cv.pack(side="left", padx=(0, 30))

        # Circular Photo with fixed top offset
        photo = self.app.get_photo(m["photo"], PH_SIZE, crop_y=m.get("crop_y", 0.5))
        if photo:
            cv.create_image(cx, cy, image=photo)
        else:
            draw_initials(cv, cx, cy, PH_SIZE // 2 - 4, m["initials"], m["accent"])

        # Accent Rings
        cv.create_oval(cx - (PH_SIZE // 2 + 5), cy - (PH_SIZE // 2 + 5),
                       cx + (PH_SIZE // 2 + 5), cy + (PH_SIZE // 2 + 5),
                       outline=m["accent_dim"], width=2)
        cv.create_oval(cx - (PH_SIZE // 2 + 2), cy - (PH_SIZE // 2 + 2),
                       cx + (PH_SIZE // 2 + 2), cy + (PH_SIZE // 2 + 2),
                       outline=m["accent"], width=2)

        # Right Bio Information Column
        info = tk.Frame(inner, bg=BG_CARD)
        info.pack(side="left", fill="both", expand=True)

        name_reg_row = tk.Frame(info, bg=BG_CARD)
        name_reg_row.pack(anchor="w")

        tk.Label(
            name_reg_row, text=m["name"], bg=BG_CARD, fg=TEXT_H,
            font=F_NAME_LG, anchor="w",
        ).pack(side="left")

        # Registration Number Badge
        reg_pill = tk.Frame(name_reg_row, bg=BG_ELEVATED, padx=10, pady=3,
                            highlightthickness=1, highlightbackground=m["accent_dim"])
        reg_pill.pack(side="left", padx=(14, 0))
        tk.Label(
            reg_pill, text=f"Reg. No: {m['reg_no']}",
            bg=BG_ELEVATED, fg=m["accent"], font=("Segoe UI", 10, "bold"),
        ).pack()

        tk.Label(
            info, text=m["role"], bg=BG_CARD, fg=m["accent"],
            font=("Segoe UI", 12, "bold"), anchor="w",
        ).pack(anchor="w", pady=(4, 10))

        tk.Label(
            info, text=m["bio"], bg=BG_CARD, fg=TEXT_P,
            font=F_BODY, anchor="w", wraplength=760, justify="left",
        ).pack(anchor="w")

        # Quick summary badge row
        summary_row = tk.Frame(info, bg=BG_CARD)
        summary_row.pack(anchor="w", pady=(14, 0))

        badges = [
            ("Project", "FolioPort"),
            ("Reg ID", m["reg_no"]),
            ("Domains", "AI/ML · Web · DBMS"),
            ("Framework", "Python & Tkinter"),
        ]
        for label, val in badges:
            b_frame = tk.Frame(summary_row, bg=BG_ELEVATED, padx=10, pady=4,
                               highlightthickness=1, highlightbackground=BORDER)
            b_frame.pack(side="left", padx=(0, 10))
            tk.Label(b_frame, text=label + ": ", bg=BG_ELEVATED, fg=TEXT_MUTED, font=F_BADGE).pack(side="left")
            tk.Label(b_frame, text=val, bg=BG_ELEVATED, fg=TEXT_H, font=F_SMALL).pack(side="left")

    # ────────────────────────────────────────────────────────────
    #  Technical Skills — Clearly Stated & Categorized
    # ────────────────────────────────────────────────────────────
    def _build_skills(self):
        self._create_section_title("Technical Skills & Proficiencies", "Categorized by Specialization")

        container = tk.Frame(self.body, bg=BG)
        container.pack(fill="x", padx=70, pady=(0, 10))

        categories = self.m["skills_by_category"]

        for idx, (cat_name, skills) in enumerate(categories):
            r, c = divmod(idx, 2)
            container.grid_columnconfigure(c, weight=1)

            box_border = tk.Frame(container, bg=BORDER)
            box_border.grid(row=r, column=c, padx=8, pady=8, sticky="nsew")

            box = tk.Frame(box_border, bg=BG_CARD, padx=16, pady=14)
            box.pack(fill="both", expand=True, padx=1, pady=1)

            # Category Header
            cat_header = tk.Frame(box, bg=BG_CARD)
            cat_header.pack(fill="x", pady=(0, 10))

            tk.Label(
                cat_header, text="◆", bg=BG_CARD, fg=self.m["accent"], font=("Segoe UI", 9),
            ).pack(side="left", padx=(0, 6))

            tk.Label(
                cat_header, text=cat_name.upper(), bg=BG_CARD, fg=TEXT_H,
                font=("Segoe UI", 10, "bold"),
            ).pack(side="left")

            # Skills Pills Flow
            pills_frame = tk.Frame(box, bg=BG_CARD)
            pills_frame.pack(fill="x")

            for s_idx, skill in enumerate(skills):
                pill_bg = tk.Frame(pills_frame, bg=BG_ELEVATED, padx=10, pady=5,
                                   highlightthickness=1, highlightbackground=BORDER)
                pill_bg.pack(side="left", padx=4, pady=4)

                tk.Label(
                    pill_bg, text=skill, bg=BG_ELEVATED, fg=TEXT_P, font=F_TAG,
                ).pack()

    # ────────────────────────────────────────────────────────────
    #  Achievements — NPTEL, Coursera, Udemy, Hackathons
    # ────────────────────────────────────────────────────────────
    def _build_achievements(self):
        self._create_section_title("Achievements & Credentials", "Hackathons, Certifications & Honors")

        ach_frame = tk.Frame(self.body, bg=BG)
        ach_frame.pack(fill="x", padx=70, pady=(0, 10))

        for tag, title, tag_color in self.m["achievements"]:
            row_border = tk.Frame(ach_frame, bg=BORDER)
            row_border.pack(fill="x", pady=5)

            row = tk.Frame(row_border, bg=BG_CARD, padx=16, pady=12)
            row.pack(fill="both", expand=True, padx=1, pady=1)

            # Credential Badge Pill
            badge = tk.Frame(row, bg=BG_ELEVATED, padx=10, pady=4,
                             highlightthickness=1, highlightbackground=tag_color)
            badge.pack(side="left", padx=(0, 14))

            tk.Label(
                badge, text=tag, bg=BG_ELEVATED, fg=tag_color, font=F_BADGE,
            ).pack()

            # Description
            tk.Label(
                row, text=title, bg=BG_CARD, fg=TEXT_H,
                font=F_BODY, anchor="w",
            ).pack(side="left", fill="x", expand=True)

            # Interactive Hover Effect
            def _bind_hover(target, border_widget):
                target.bind("<Enter>", lambda e: border_widget.config(bg=self.m["accent"]))
                target.bind("<Leave>", lambda e: border_widget.config(bg=BORDER))

            _bind_hover(row, row_border)

    # ────────────────────────────────────────────────────────────
    #  Projects — AI/ML, Web Dev, DBMS For Each Member
    # ────────────────────────────────────────────────────────────
    def _build_projects(self):
        self._create_section_title("Featured Projects", "AI/ML  •  Full-Stack Web Dev  •  DBMS")

        proj_container = tk.Frame(self.body, bg=BG)
        proj_container.pack(fill="x", padx=70, pady=(0, 10))

        accent = self.m["accent"]

        for j, proj in enumerate(self.m["projects"]):
            proj_container.grid_columnconfigure(j, weight=1)

            card_border = tk.Frame(proj_container, bg=BORDER)
            card_border.grid(row=0, column=j, padx=8, pady=8, sticky="nsew")

            card = tk.Frame(card_border, bg=BG_CARD, padx=20, pady=18)
            card.pack(fill="both", expand=True, padx=1, pady=1)

            # Domain Tag
            domain_badge = tk.Frame(card, bg=BG_ELEVATED, padx=8, pady=3,
                                    highlightthickness=1, highlightbackground=proj["badge_color"])
            domain_badge.pack(anchor="w", pady=(0, 10))

            tk.Label(
                domain_badge, text=proj["domain"], bg=BG_ELEVATED,
                fg=proj["badge_color"], font=F_BADGE,
            ).pack()

            # Project Title
            tk.Label(
                card, text=proj["title"], bg=BG_CARD, fg=TEXT_H,
                font=F_NAME, anchor="w", wraplength=270, justify="left",
            ).pack(anchor="w", pady=(0, 8))

            # Project Description
            tk.Label(
                card, text=proj["desc"], bg=BG_CARD, fg=TEXT_P,
                font=F_SMALL, anchor="w", wraplength=270, justify="left",
            ).pack(anchor="w", pady=(0, 16))

            # Tech Stack Footer
            tech_frame = tk.Frame(card, bg=BG_CARD)
            tech_frame.pack(fill="x", side="bottom")

            tk.Label(
                tech_frame, text="Tech Stack:", bg=BG_CARD, fg=TEXT_MUTED,
                font=("Segoe UI", 8, "bold"), anchor="w",
            ).pack(anchor="w")

            tk.Label(
                tech_frame, text=proj["tech"], bg=BG_CARD, fg=accent,
                font=("Segoe UI", 9), anchor="w", wraplength=270, justify="left",
            ).pack(anchor="w", pady=(2, 0))

            # Interactive hover glow
            def _proj_enter(e, b=card_border, c=accent):
                b.config(bg=c)
            def _proj_leave(e, b=card_border):
                b.config(bg=BORDER)

            for w in (card_border, card, *card.winfo_children()):
                w.bind("<Enter>", _proj_enter)
                w.bind("<Leave>", _proj_leave)

    # ────────────────────────────────────────────────────────────
    #  Footer
    # ────────────────────────────────────────────────────────────
    def _build_footer(self):
        tk.Frame(self.body, bg=BG, height=36).pack()
        foot = tk.Frame(self.body, bg=BG_NAV)
        foot.pack(fill="x")
        tk.Label(
            foot,
            text=(f"FolioPort © 2026  •  {self.m['name']} ({self.m['reg_no']})  •  "
                  "Python & Tkinter Project Submission  •  Press Esc to Return Home"),
            bg=BG_NAV, fg=TEXT_MUTED, font=F_SMALL,
        ).pack(pady=16)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Main Execution
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":
    app = PortfolioApp()
    app.mainloop()
