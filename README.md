# DASW oTree Apps
---
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg?style=flat-square)](https://github.com/projectdasw/dasw_otree_apps)
[![oTree](https://img.shields.io/badge/built%20with-oTree%205.x-green.svg?style=flat-square)](https://www.otree.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-yellow.svg?style=flat-square)](https://www.python.org/)

> **DASW oTree Apps** is a modular framework containing a comprehensive collection of ready-to-use experimental applications built on [oTree](https://www.otree.org/).

It serves as a modular foundation for academic research, corporate behavioral testing, and other experimental studies — enabling rapid design, development, and deployment of diverse behavioral, economic, and decision-making experiments.

This snippet is ideal for researchers, developers, and practitioners who need a flexible yet robust oTree environment that can be easily customized for new projects.

---

## 📦 Overview

This project provides a **comprehensive collection of reusable oTree apps**, including:

- 🧩 **Donation with Rank** – donation experiment with participant ranking  
- 💹 **Investment Apps** – investment tasks with high/low risk options and endowment rules  
- 🛍️ **Shop Apps** – simulated market shopping and consumption behavior  
- 📝 **Survey & Demographics** – participant background and demographic data  
- ⚙️ **Real Effort Tasks (RET):**
  - Decoding Task (symbol translation)
  - Transcription Task (typing accuracy)
  - Algebraic Task (math/algebra problems)
  - Slot Machine Task (luck-based RET using probability logic)

Each app can be used independently or integrated into a multi-round experimental design with automated data flow and final payment calculation.

---

## 🚀 Version History

| Version | Release Date | Status | Notes                                                                                                                        |
|----------|---------------|--------|------------------------------------------------------------------------------------------------------------------------------|
| **v1.0.0 – Initial Release** | Planned | 🛠️ In Development | First public release of DASW oTree Apps. Includes 6 experiment categories, complete backend logic, and final payment system. |

> **Current Version:** `v1.0.0`  
> Uses **Semantic Versioning** conventions:
> - **MAJOR** – Breaking changes  
> - **MINOR** – Backward-compatible new features  
> - **PATCH** – Bug fixes or small improvements

---

## 🧱 Project Structure

**Full Changelog**: https://github.com/projectdasw/dasw_otree_apps/commits/main/

## ⚙️ Key Features

- 🧱 **Modular Structure** – each app is standalone and reusable  
- 🔄 **Cross-decoding_game Integration** – experiment results automatically sent to the final payment module  
- 💰 **Automated Final Payment Calculation**  
  Handles endowment, investment, and consumption logic seamlessly  
- 📊 **Utility Recap per Round**  
  Includes randomized payoff (e.g., 90%–10%) and automatic final conversion  
- 🎰 **Slot Machine game**  
  Fully integrated with backend probability logic and JS-based animation  
- ✍️ **Comprehensive Real Effort Tasks**
  - Decoding: translate characters or symbols  
  - Transcription: accurate text retyping  
  - Algebraic: timed math questions  
  - Slot Machine: luck & probability experiment  
- 📋 **Survey & Demographics** – participant data stored in oTree models  
- 🧾 **Payment Page** – final payoff summary, attendance fee, and participant code display  
- 📂 **Reusable Template System** – easy to adapt for new experimental projects  

---

## 🧠 Project Purpose

1. Provide a **personal oTree framework** for quick and consistent experiment setup.  
2. Offer a **standardized suite of tasks** for behavioral, social, and economic research.  
3. Ensure **reusability and scalability** for future experimental projects.  
4. Simplify **data integration** across multiple apps and experiment rounds.  

---

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/projectdasw/dasw_otree_apps.git
