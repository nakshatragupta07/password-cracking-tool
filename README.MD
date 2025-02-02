# Password Cracking Tool

## Project Description

The Password Cracking Tool is a Python-based utility designed to help demonstrate common password-cracking techniques while emphasizing cybersecurity best practices and PCI compliance awareness. The tool offers multiple approaches to test the strength of passwords, including:

- Brute Force Attack: Iteratively generates and tests all possible combinations of characters up to a specified length.
- Dictionary Attack: Uses a provided wordlist to guess common or weak passwords.
- Password Strength Checker: Evaluates passwords based on length, the inclusion of digits, uppercase letters, and special characters.
- PCI Compliance Check: Ensures that a given password meets PCI DSS standards (e.g., minimum length, inclusion of numbers, uppercase letters, and special characters).

Designed for educational purposes and practical demonstrations, this tool can be used to raise awareness about secure password practices and to illustrate potential vulnerabilities in weak password policies.

## Installation Instructions

Follow these steps to set up and run the Password Cracking Tool on your local machine:

### Prerequisites

- Python 3.7 or higher installed on your system.
- Basic command-line (CLI) familiarity.

### Steps

1. Clone the Repository:

   ```bash
   git clone https://github.com/yourusername/password-cracking-tool.git
   cd password-cracking-tool
   ```

2. Set Up a Virtual Environment:

   It is recommended to use a virtual environment to manage dependencies.

   - On Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Install Required Libraries:

   The project uses standard Python libraries; however, you can install additional dependencies if needed. For now, ensure you have the following libraries installed:

   ```bash
   pip install --upgrade pip
   pip install pyinstaller
   ```

   > Note: The core libraries (`hashlib`, `itertools`, `string`, `argparse`, `time`) are part of Python's standard library and do not require separate installation.

4. Run the Tool:

   The tool is designed to be run via the command-line interface. You can test its functionality with a sample command:

   ```bash
   python password_cracker.py --brute-force "YourPassword123!"
   ```

   Use the available command-line arguments to choose the desired function:
   - `--brute-force` : Perform a brute force attack.
   - `--dictionary` : Perform a dictionary attack.
   - `--check-strength` : Check the strength of the password.
   - `--pci-check` : Verify PCI compliance of the password.

   For example, to check the strength and PCI compliance of a password:

   ```bash
   python password_cracker.py "YourPassword123!" --check-strength --pci-check
   ```

5. Optional - Create an Executable:

   If you want to package the tool as a standalone executable, use PyInstaller:

   ```bash
   pyinstaller --onefile password_cracker.py
   ```

   After the build process, the executable will be available in the `dist` folder.

## Usage Examples

Once installed, you can run various functionalities as shown below:

- Brute Force Attack:
  ```bash
  python password_cracker.py "YourPassword123!" --brute-force
  ```

- Dictionary Attack:
  ```bash
  python password_cracker.py "YourPassword123!" --dictionary
  ```

- Password Strength & PCI Compliance Check:
  ```bash
  python password_cracker.py "YourPassword123!" --check-strength --pci-check
  ```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or additional features.
