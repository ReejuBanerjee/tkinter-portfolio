# FolioPort — Interactive Team Portfolio Showcase

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-brightgreen.svg)](https://docs.python.org/3/library/tkinter.html)
[![DPI-Aware](https://img.shields.io/badge/Display-High--DPI%20Crisp-purple.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

**FolioPort** is a modern, interactive desktop GUI portfolio application developed in Python using Tkinter. It showcases individual portfolios for a 3-member engineering team, highlighting categorized technical skills, verified certifications (NPTEL, Coursera, Udemy, Hackathons), and production-grade projects spanning **AI / Machine Learning**, **Full-Stack Web Development**, and **Database Management Systems (DBMS)**.

---

## 👥 Team Members

| Member Name | Registration Number | Specialization / Role | Focus Domains |
| :--- | :--- | :--- | :--- |
| **Reeju Banerjee** | `RA2511003010548` | Full-Stack & Systems Developer | ResNet-50 CV, React/Node, PostgreSQL EHR |
| **Shourya Shrivastava** | `RA2511003010559` | AI & Backend Software Engineer | Transformers NLP, Next.js, MySQL Telematics |
| **Prarabdha Sachan** | `RA2511003010562` | Full-Stack & UI/UX Engineer | LangChain RAG, React/FastAPI, Banking Ledger |

---

## ✨ Features

- **High-DPI Razor-Sharp Rendering**: Integrates Windows Per-Monitor V2 DPI awareness (`shcore.SetProcessDpiAwareness(2)`) to eliminate font and border blurriness on 125%/150% scaled displays.
- **Interactive Navigation**:
  - Landing showcase cards with real-time hover glow effects.
  - One-click navigation into each member's deep portfolio.
  - Global `<Escape>` shortcut and header back buttons to return to the home screen.
- **Dynamic Circular Photo Cropping**: Smart aspect-ratio and vertical anchor positioning (`crop_y`) with anti-aliased elliptical masking using Pillow.
- **Categorized Technical Proficiencies**:
  - Core & Programming
  - AI & Machine Learning
  - Full-Stack Web Development
  - Databases, DevOps & Systems
- **Industry & Academic Credentials**:
  - Verified NPTEL Elite+Gold / Silver Certifications
  - Stanford University & Meta Coursera Specializations
  - Udemy Full-Stack & Microservices Bootcamps
  - Smart India Hackathon (SIH), TechNova, and CodeStorm Winner / Finalist honors
- **Comprehensive Project Showcase**: Each member features 3 distinct projects explicitly aligned with **AI/ML**, **Web Development**, and **DBMS**.
- **Smooth Scrolling**: Integrated vertical scrollbar and responsive mousewheel navigation.

---

## 📂 Project Structure

```
tkinter-portfolio/
│
├── portfolio_app.py        # Main Tkinter GUI application script
├── README.md               # Documentation and setup instructions
├── .gitignore              # Git ignored files & cache
│
└── photos/                 # High-resolution team profile photos
    ├── reeju.jpg           # Reeju Banerjee
    ├── shourya.jpg         # Shourya Shrivastava
    └── prarabdha.jpg       # Prarabdha Sachan
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.8 or newer** installed. Tkinter comes bundled with standard Python distributions on Windows and macOS.

Check your Python installation:
```bash
python --version
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ReejuBanerjee/tkinter-portfolio.git
   cd tkinter-portfolio
   ```

2. **Install the required dependencies:**
   Only `Pillow` is required for high-resolution circular photo processing and masking:
   ```bash
   pip install pillow
   ```

---

## 🖥️ Running the Application

Execute the main script from the project root directory:

```bash
python portfolio_app.py
```

### ⌨️ Controls & Shortcuts
- **Click any Member Card**: Opens the member's detailed portfolio page.
- **`Esc` Key**: Returns to the home page from anywhere in the application.
- **`← Back to FolioPort` Button**: Located in the top sticky nav bar.
- **Mouse Wheel / Trackpad**: Scrolls smoothly through long portfolio pages.

---

## 🛠️ Built With

- **Python 3** — Core language
- **Tkinter & ttk** — Native GUI toolkit & layout management
- **Pillow (PIL)** — Image processing, aspect-ratio smart cropping & circular alpha masking
- **Windows ctypes API** — Native Per-Monitor V2 high-DPI scaling

---

## 📄 License

This project was developed for academic project submission and portfolio display. All rights reserved.
