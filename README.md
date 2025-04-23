# 🧩 Non-Verbal Communication Tracker for Children with ASD

**Members:**  
Liliane Zukerman and Sharon Fogel

---

## 🎯 Goal
To monitor and analyze the non-verbal communication progress of pre-verbal children with Autism Spectrum Disorder (ASD).

---

## 📝 Description

This project will enable the **daily/weekly/monthly logging of non-verbal behaviors** such as:

- Gestures (e.g., waving)
- Vocalizations
- Eye contact
- Reactions to simple commands

The data will be stored in a database (**SQLite or PostgreSQL**) and analyzed using **Python and Pandas**.

We are not sure about implementing a full dashboard, but we aim to create **basic visual outputs or summaries** of progress over time.

---

## ✨ Bonus Feature

We plan to support **multiple languages** (*Portuguese, English, and Hebrew*) for descriptions and interface elements — making the tool accessible to both **parents and professionals** in multicultural environments.

---

## 📦 Installation Instructions

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/SharonFogel89/Non-Verbal-Communication-Tracker-for-Children-with-ASD
cd Non-Verbal-Communication-Tracker-for-Children-with-ASD
```

# For Windows:

```bash
python -m venv my_env
venv\Scripts\activate
```

# For Linux/Mac:
```bash
python3 -m venv my_env
source my_env/bin/activate
```

# Install dependencies
```bash
pip install -r requirements.txt
```
---

## 🗓️ Project Timeline

| Date       | Task Description                                  |
|------------|---------------------------------------------------|
| 23/04      | Define core functionalities and data modeling     |
| 24/04      | Create and initialize the database (SQLite/PostgreSQL) |
| 25/04      | Implement data entry interface (CLI or simple UI) |
| 26/04      | Data analysis logic + basic visual summaries      |
| 27/04      | Finalize presentation and documentation           |

---
# 🧠 Non-Verbal Communication Tracker – Core Features

## 1. Register a Child
- **Fields**: Name, Date of birth, Date of diagnosis, Additional notes

## 2. Register an Observer
- **Fields**: Name, Relationship (e.g., mother, therapist, assistant), Notes (e.g., “Autism specialist”)

## 3. Record a Behavior
- **Fields**:
  - Date of behavior
  - Child
  - Observer
  - Type of behavior (e.g., gesture, eye contact)
  - Category (e.g., social, communication)
  - Duration (if applicable)
  - Free description (e.g., “Waved back when greeted bye”)
  - Is it consolidated? (Boolean)

## 4. List of Records
- View all recorded behaviors by date
- Filter by:
  - Type
  - Category
  - Observer

## 5. Summary by Category or Type
- Show how many records there are per:
  - Category (e.g., social, communication)
  - Type (e.g., eye contact, vocalization)

## 6. Simple Alerts
- Example: “No new behaviors recorded in 7 days.”
- Helps detect regressions or oversights

## 7. Recording of Milestones
- Record important developmental events
  - Examples:
    - "Imitated gesture for the first time"
    - "Responded to name"
- Can be used to highlight achievements

## 8. CSV Export
- Export data to Excel/CSV format
- Useful for sharing with therapists or saving as a history

## 9. Multilingual Interface (Basic)
- Initial support for:
  - Portuguese 🇧🇷
  - English 🇺🇸
  - Hebrew 🇮🇱
---
## ❤️ Dedication

This project is dedicated to **Hannah Zukerman**, my beloved daughter, whose strength and uniqueness inspire this work.
