# CodeAlpha Backend Development Tasks 🚀

This repository contains backend projects completed during the CodeAlpha Internship using Python Flask and SQLite.

---

## ✂️ TASK 1: Simple URL Shortener
A lightweight URL shortener backend built with Python Flask and SQLite.
- **Features:** Generates unique short codes, stores mapping in SQLite database, and automatically redirects short links to the destination URL.
- **Main Code File:** `app.py`
- **Dependencies:** `requirements.txt`

---

## 🍽️ TASK 3: Restaurant Management System
A Python Flask backend application with SQLite integration to manage restaurant operations smoothly.
- **Database Models:** Structure for Menu items, Tables status, and Orders data tracking.
- **Data Automations:** Placing an order automatically updates the seating table status to 'Booked'.
- **REST APIs:** Endpoints to fetch menu details (`GET /api/menu`) and process new orders (`POST /api/orders`).
- **Main Code File:** `restaurant_app.py`
- **Dependencies:** `requirements_restaurant.txt`
- 
---

## 📅 TASK 2: Event Registration System
A Python Flask backend system that handles upcoming event management and secure user registration.
- **Database Models:** Structure for Events data tracking and linked Registrations mapping.
- **Logic Automations:** Submitting a registration form automatically subtracts 1 seat from the event's available seats counter.
- **REST APIs:** Endpoints to view available events list (`GET /api/events`) and process user registration data (`POST /api/register`).
- **Main Code File:** `event_app.py`
- **Dependencies:** `requirements_event.txt`
- 

---

## 🧬 TASK 1: DNA/Protein Sequence Analysis
Bioinformatics analysis mapping homologous matching patterns across biological sequence databases.
- **Target Sequence:** Human Insulin Protein extracted from NCBI/UniProt.
- **Analysis Execution:** BLASTp alignment mapping to document genetic similarities.
- **Documentation File:** `blast_analysis.txt` capturing max identity scores and evaluation metrics.
- 

---

## 📅 TASK 2: Multiple Sequence Alignment
Bioinformatics mapping that traces molecular similarities and variations across 5 distinct mammalian sequences.
- **Protein Family:** Mammalian Insulin Family (Human, Chimpanzee, Macaque, Mouse, Blue Whale).
- **Core Methodology:** Multiple Sequence Alignment executed via the Clustal Omega algorithm.
- **Main Analysis File:** `msa_alignment.txt` documenting fully conserved active domains and cross-species structural links.
- 

# Task 1: Simple Storage Smart Contract

## Project Description
Yeh aik buniyaadi Solidity Smart Contract hai jo blockchain par aik integer value ko store karta hai. Is mein value ko barhane (increment) aur kam karne (decrement) ke functions mojood hain.

## How to Test
1. Is code ko **Remix IDE** (remix.ethereum.org) par copy-paste karein.
2. Solidity Compiler tab mein ja kar ise **Compile** karein.
3. Deploy & Run Transactions tab mein ja kar contract ko **Deploy** karein.
4. Deploy hone ke baad `increment` aur `decrement` buttons par click kar ke check karein ke `storedValue` change ho rahi hai ya nahi.
5. 
