# Job Application Tracker 🚀

A self-hosted, mobile-first web application designed to track job applications efficiently. Built with Python (Flask), it features a modern UI, dynamic interactions, and powerful Excel integration tailored for the North American job market.

## ✨ Key Features

*   **Mobile-First Design**: Responsive interface built with **Tailwind CSS** and **DaisyUI**, perfect for tracking on the go.
*   **Dynamic UX**: Uses **HTMX** for smooth, single-page-application (SPA) like interactions without full page reloads.
*   **Comprehensive Tracking**: Track 14 essential fields including:
    *   Company, Job Title, Location
    *   Status (Applied, OA, Interview, Offer, etc. - Color Coded)
    *   Dates (Applied, Last Contacted, Next Follow-up)
    *   Recruiter Info, Referral Contacts, Resume Versions
    *   Salary/TC Range, Priority
*   **Rainbow Excel Export** 🌈:
    *   One-click export to a beautifully formatted `.xlsx` file.
    *   Features an alternating 8-color "Rainbow" row style.
    *   Includes data validation dropdowns for 'Status' and 'Source' for easy offline editing.
*   **Excel Import** 📤:
    *   Bulk upload applications using the standard template.
    *   Automatically maps columns to database fields.
*   **Secure**: User authentication (Login/Register) with password hashing.

## 🛠️ Tech Stack

*   **Backend**: Python 3, Flask 3.0, Flask-SQLAlchemy (SQLite), Flask-Login
*   **Frontend**: HTML5, Tailwind CSS, DaisyUI, HTMX
*   **Data Processing**: Pandas, OpenPyXL

## 🚀 Getting Started

### Prerequisites

*   Python 3.8+
*   Git

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Alixcacn/Job-Application-Tracker.git
    cd Job-Application-Tracker
    ```

2.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    python app.py
    ```
    The application will start at `http://localhost:5000`.

## 📖 Usage Guide

### 1. Dashboard
The main view lists all your applications as responsive cards.
*   **Status Badges**: Visual indicators (Green for Offer, Yellow for Interview, etc.).
*   **Quick Actions**: Edit, Delete, or visit the Job Link directly from the card.

### 2. Adding Jobs
Click the **+** button in the bottom navigation to open the "Add Application" modal. All fields are optional except Company and Job Title.

### 3. Import / Export
*   **Export**: Click the **Export** button in the header to download your data in the custom "Rainbow" Excel format.
*   **Import**: Click **Import** to upload an existing Excel file. Ensure your Excel columns match the standard format (Company, Job Title, etc.).

## 📦 Deployment (Self-Hosted)

To run this on a server 24/7 (e.g., VPS, Raspberry Pi):

1.  **Install Gunicorn** (Production WSGI server):
    ```bash
    pip install gunicorn
    ```
2.  **Run with Gunicorn**:
    ```bash
    # Run on port 8000
    gunicorn -w 4 -b 0.0.0.0:8000 app:app
    ```
3.  **Keep it running**: Use extensive process managers like `systemd` or `supervisor` to keep the app alive in the background.

## 📄 Database

The application uses a local `job_tracker.db` SQLite file.
*   This file is **automatically created** when you first run the app.
*   **Note**: The database file is ignored by Git (via `.gitignore`) to protect your personal data.

---
*Created for the Job Hunt 2026. Good luck!* 🤞
