# Password Audit Tool

A Python-based tool for auditing password strength, checking for breaches, generating secure passwords, and providing actionable recommendations. This tool leverages the [Have I Been Pwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) API to check if passwords have been compromised in known data breaches.

## Features

- **Single Password Audit**: Analyze the strength and breach status of a single password.
- **Batch Password Audit**: Process a file containing multiple passwords and generate a detailed report.
- **Password Strength Analysis**: Evaluate passwords for length, character variety, and commonality.
- **Breach Checking**: Check if a password has been exposed in known breaches using the Pwned Passwords API.
- **Secure Password Generation**: Generate strong, random passwords.
- **Personalized Recommendations**: Get tips to improve password strength based on analysis.
- **Comprehensive Reporting**: Output results to the console and optionally to a report file.

## Directory Structure

```
password_audit/
├── .gitignore                 # Git ignore rules
├── .python-version           # Python version specification
├── README.md                 # Project documentation
├── main.py                   # Main application entry point
├── pyproject.toml            # Project configuration and dependencies
├── uv.lock                   # Dependency lock file
├── requirements.txt          # Legacy pip requirements
├── analyzer/                 # Core analysis modules
│   ├── __init__.py
│   ├── breach_checker.py     # Have I Been Pwned API integration
│   ├── bulk_pwd_checker.py   # Batch processing functionality
│   ├── generator.py          # Secure password generation
│   ├── recommender.py        # Security recommendations engine
│   └── strength_checker.py   # Password strength analysis
├── data/                     # Static data files
│   └── common_passwords.txt  # Database of common/weak passwords
├── sample/                   # Example input files
│   └── passwords.txt         # Sample password list for testing
└── reports/                  # Generated audit reports
    └── audit_report.txt      # Sample output report
```

## Installation

``` sh
 Prerequisites

Python 3.8 or higher
Internet connection (for breach checking)

Method 1: Using pip
bash# Clone the repository
git clone https://github.com/yourusername/password_audit.git
cd password_audit

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


Method 2: Using Poetry 
bash# Clone the repository
git clone https://github.com/yourusername/password_audit.git
cd password_audit

# Install with Poetry
poetry install
poetry shell


Method 3: Using UV (Fastest)
bash# Clone the repository
git clone https://github.com/yourusername/password_audit.git
cd password_audit

# Install with UV
uv sync
source .venv/bin/activate
   ```

## Usage

Run the main script:

```sh
python main.py
```

### Interactive Menu

You will see:

```
What would you like to do?
1. Audit a single password
2. Process a batch of passwords
3. Generate a secure password
4. Exit
```

#### 1. Audit a Single Password

- Enter a password when prompted.
- The tool will:
  - Check if the password has been breached.
  - Analyze its strength.
  - Provide recommendations for improvement.

#### 2. Process a Batch of Passwords

- Enter the path to a file containing passwords (one per line).
- The tool will:
  - Audit each password.
  - Output a summary report (see `audit_report.txt` for sample output).

#### 3. Generate a Secure Password

- The tool will generate and display a strong password.

#### 4. Exit

- Quit the program.

## Example Output

```
Password Report:
length: 12
has_uppercase: True
has_lowercase: True
has_digits: True
has_special_characters: True
strength: Excellent
is_common: False

Recommendations:
- Your password looks strong! great work!
```

🔗 API Integration

- Uses the [Have I Been Pwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) API for breach checking.
- No passwords are sent directly; only partial hashes are used for privacy.

⚙️ Customization

- **Common Passwords List**: Update `data/common_passwords.txt` to customize the list of common passwords.
- **Batch Input**: Place your password files in the `sample/` directory for batch processing.


📄 License

This project is licensed under the MIT License.

---

**Author:** Adarsh Tiwari
