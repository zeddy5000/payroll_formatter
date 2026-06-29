import pandas as pd


def process_file(file):

    # Read file
    if file.name.lower().endswith(".csv"):

        df = pd.read_csv(
            file,
            header=None
        )

    elif file.name.lower().endswith(".xlsx"):

        df = pd.read_excel(
            file,
            header=None,
            engine="openpyxl"
        )

    elif file.name.lower().endswith(".xls"):

        df = pd.read_excel(
            file,
            header=None,
            engine="xlrd"
        )

    else:
        raise ValueError(
            "Unsupported file type."
        )

    employees = []

    current_employee = None

    for _, row in df.iterrows():

        section = (
            str(row[0]).strip()
            if pd.notna(row[0])
            else ""
        )

        field = (
            str(row[1]).strip()
            if pd.notna(row[1])
            else ""
        )

        value = (
            str(row[2]).strip()
            if pd.notna(row[2])
            else ""
        )

        # Start new employee
        if section == "Personal Details":

            if (
                current_employee
                and current_employee.get("Name")
            ):
                employees.append(
                    current_employee
                )

            current_employee = {}

        if current_employee is None:
            continue

        if not field:
            continue

        ignore_fields = {
            "Payslip",
            "Niger Delta University",
            "Wilberforce Island",
            "Bayelsa State",
        }

        if field in ignore_fields:
            continue

        field = (
            field.replace("--------------->", "")
            .replace("---------->", "")
            .replace("------------------->", "")
            .strip()
        )

        current_employee[field] = value

    # Add final employee
    if (
        current_employee
        and current_employee.get("Name")
    ):
        employees.append(
            current_employee
        )

    output_df = pd.DataFrame(
        employees
    )

    output_df = output_df.fillna(0)

    print(
        f"Employees Found: {len(output_df)}"
    )

    print(
        f"Columns Found: {len(output_df.columns)}"
    )

    print(output_df.head())

    return output_df