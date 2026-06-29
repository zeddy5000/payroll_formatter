# Payroll Formatter

A Django-powered payroll transformation tool that converts unstructured payroll/payslip files into a structured tabular format suitable for reporting, auditing, payroll analysis, and further processing.

## Features

- Upload payroll files in:
  - `.xls`
  - `.xlsx`
  - `.csv`

- Automatically:
  - Detect employee records
  - Extract employee details
  - Extract earnings and allowances
  - Extract deductions
  - Extract loan balances
  - Build a unified dataset

- Dynamic column generation:
  - Any field discovered in any employee record becomes a column.
  - Missing values are automatically filled with `0`.

- Preview transformed data before download.

- Download processed payroll in:
  - CSV
  - XLSX
  - XLS

---

## Example Transformation

### Input Structure

```text
Personal Details
Name                  John Doe
Rank                  ASS II
Bank Name             UBA

Gross Details
Salary                100000
Housing               25000
Responsibility        5000

Deductions
Tax Paid              3000
```

### Output Structure

| Name | Rank | Salary | Housing | Responsibility | Tax Paid |
|--------|--------|--------|--------|--------|--------|
| John Doe | ASS II | 100000 | 25000 | 5000 | 3000 |

Each employee occupies a single row.

---

## Technology Stack

- Python
- Django
- Pandas
- OpenPyXL
- XLRD

---

## Project Structure

```text
payroll_formatter/
│
├── manage.py
│
├── formatter/
│   ├── forms.py
│   ├── services.py
│   ├── urls.py
│   ├── views.py
│   │
│   └── templates/
│       └── formatter/
│           ├── upload.html
│           └── preview.html
│
└── config/
    ├── settings.py
    ├── urls.py
    └── ...
```

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd payroll_formatter
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install django pandas openpyxl xlrd
```

---

## Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## Usage

### Step 1

Upload a payroll file:

- XLS
- XLSX
- CSV

### Step 2

The application:

- Parses employee records
- Detects fields dynamically
- Creates a structured dataframe
- Fills missing values with `0`

### Step 3

Preview the transformed data.

### Step 4

Download the processed file as:

- CSV
- XLSX
- XLS

---

## Data Processing Logic

The parser:

1. Reads the uploaded file.
2. Detects employee boundaries using:

```text
Personal Details
```

3. Extracts:

### Personal Details

- Name
- Rank
- Scale & Step
- Bank Name
- Bank A/c
- Department
- Month

### Earnings

- Salary
- Housing
- Medical
- Responsibility
- Drivers Welfare
- Hazard
- Allowances
- Inducement
- etc.

### Deductions

- Tax Paid
- Education Levy
- Union Dues
- Salary Advance
- Cooperative Contributions
- Loan Repayments
- etc.

### Loan Balances

- Salary Advance Balance
- Cooperative Balance
- Total Loan Balances

4. Builds a unified dataset where:

```text
Employee = One Row
Field = One Column
```

5. Missing values become:

```text
0
```

---

## Dependencies

```text
Django
Pandas
OpenPyXL
XLRD
```

Generate requirements file:

```bash
pip freeze > requirements.txt
```

---

## Future Improvements

- Authentication
- User accounts
- Upload history
- Background processing for large files
- Docker support
- Bulk file processing
- Export to PDF
- Audit reports
- Data validation dashboard

---

## Author

Developed as a payroll data transformation utility for converting unstructured payroll records into standardized tabular datasets.
