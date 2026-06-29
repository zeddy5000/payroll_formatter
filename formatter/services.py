import pandas as pd


def process_file(file):
    df = pd.read_csv(file)

    values = df.iloc[:, 0].dropna().tolist()

    rows = []

    for i in range(0, len(values), 10):
        rows.append(values[i:i + 10])

    columns = [
        "Name",
        "Department",
        "Role",
        "Email",
        "Phone",
        "Address",
        "State",
        "Country",
        "Salary",
        "Employee ID",
    ]

    return pd.DataFrame(rows, columns=columns)