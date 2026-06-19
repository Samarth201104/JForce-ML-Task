import pandas as pd

INPUT_FILE = "data/input.csv"
OUTPUT_FILE = "data/output.csv"

df = pd.read_csv(INPUT_FILE)

df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

df = df.sort_values(
    by=["Roll No", "Subject", "Date"],
    ascending=[True, True, False]
)

result = []

for (roll_no, subject), group in df.groupby(["Roll No", "Subject"]):

    marks = group["Marks"].tolist()[:3]

    marks += [0] * (3 - len(marks))

    result.append({
        "Roll No": roll_no,
        "Subject": subject,
        "M1": marks[0],
        "M2": marks[1],
        "M3": marks[2],
        "Date": group.iloc[0]["Date"].strftime("%d-%m-%y")
    })

output_df = pd.DataFrame(result)

output_df.to_csv(OUTPUT_FILE, index=False)

print(f"Output saved to {OUTPUT_FILE}")
print(output_df)