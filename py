import pandas as pd
import numpy as np

#  Data setup

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

#  (1 = Available, 0 = Unavailable)

data = {
    'Danny': [1, 1, 0, 1, 1],
    'Sarah': [1, 0, 1, 0, 1],
    'Yossi': [0, 1, 0, 1, 1],
    'Noa': [1, 1, 1, 1, 0],
    'Amit': [0, 0, 1, 1, 1]
}

# Index = Days, Columns = Employees
df_availability = pd.DataFrame(data, index=days)

print(df_availability)


MAX_SHIFTS = 3

schedule_results = []
shifts_count = pd.Series(0, index=df_availability.columns)

for day in df_availability.index:
    current_day_row = df_availability.loc[day]
    available_workers = current_day_row[current_day_row == 1].index.tolist()
    valid_candidates = [w for w in available_workers if shifts_count[w] < MAX_SHIFTS]

    selected_worker = None

    if len(valid_candidates) > 0:
        selected_worker = np.random.choice(valid_candidates)
        shifts_count[selected_worker] += 1
    else:
        selected_worker = "--- No Candidate ---"

    schedule_results.append({
        'Day': day,
        'Assigned Employee': selected_worker
    })


df_schedule = pd.DataFrame(schedule_results)

print("=== Final Weekly Schedule ===")
print(df_schedule)
print("\n=== Workload Check ===")
print(shifts_count)

output_filename = 'weekly_schedule.xlsx'
df_schedule.to_excel(output_filename, index=False)

print(f"\n[SUCCESS] Schedule saved to '{output_filename}' successfully!")



