# Regex Assignemnt - Python

## Overview
This project shows how to use the  Python's in-built "re" module (Regular Expresions) to extract data from text.
The script extracts:

- Email addresses
- URLs
- Phone Numbers
- Credit card numbers
- Times (This is in 12-hour and 24-hour format)

Note: You can modify the sample text or use your own text to text the functions.

## Requirements
- Python 3 or above installed on your ssytem

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/Oluwatomi-Thompson/alu_regex-data-extraction-Thompson-Oluwatomi
cd alu_regex-data-extraction-Thompson-Oluwatomi
```

2. Run the Python script:
```bash
python index.py
```

3. The extracted data will then be printed in your terminal.

## Example Output
```text
Emails: ['user@example.com', 'firstname.lastname@company.co.uk']
URLs: ['https://www.example.com', 'https://subdomain.example.org/page']
Phone Numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
Credit Card Numbers: ['1234 5678 9012 3456', '1234-5678-9012-3456']
Times: ['14:30', '2:30 PM', '09:15 am']
```

## Project Structure
```bash
alu_regex-data-extraction-Thompson-Oluwatomi/
│── index.py   
│── README.md 
```
