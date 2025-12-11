# Shift Scheduling Algorithm

A Python-based automation tool designed to optimize employee shift assignments. This project solves the problem of manual scheduling by generating a fair, constraint-based weekly roster and exporting the results to Excel.

##  Overview
Managing shift schedules manually is time-consuming and prone to errors. This algorithm automates the process by considering:
* **Employee Availability:** Ensures employees are only assigned to days they can work.
* **Workload Balancing:** Enforces a maximum number of shifts per employee to prevent burnout.
* **Randomized Fairness:** Uses statistical randomization to distribute shifts among eligible candidates.

##  Tech Stack
* **Python 3.x**
* **Pandas:** For efficient data manipulation and DataFrame management.
* **NumPy:** For vectorized operations and random selection logic.
* **OpenPyXL:** For exporting the final schedule to an Excel report.

##  How It Works
1.  **Input Data:** The script initializes an availability matrix (Days vs. Employees).
2.  **Processing:** It iterates through each required shift, filtering available candidates based on constraints.
3.  **Selection:** A candidate is selected using a randomized approach to ensure fairness.
4.  **Output:** The final schedule is displayed in the console and saved automatically as `weekly_schedule.xlsx`.

##  Installation & Usage

1.  **Clone the repository** (or download the script):
    ```bash
    git clone [https://github.com/your-username/shift-scheduling-algorithm.git](https://github.com/your-username/shift-scheduling-algorithm.git)
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas numpy openpyxl
    ```

3.  **Run the script:**
    ```bash
    python scheduler.py
    ```

4.  **Check the output:**
    Open the generated `weekly_schedule.xlsx` file to see the results.

##  Future Improvements
* Load employee data directly from an external CSV/Excel file.
* Add a Graphical User Interface (GUI) for non-technical users.
* Implement more complex constraints (e.g., minimum rest time between shifts).

---
*Created by Gal Shalom*
