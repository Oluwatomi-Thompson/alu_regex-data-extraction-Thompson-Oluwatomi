import re

# 1. Email Extraction
def extract_email(text):
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.findall(email_regex, text)

# 2. URL Extraction
def extract_url(text):
    url_regex = r"(https?:\/\/[^\s]+)"
    return re.findall(url_regex, text)

# 3. Phone Number Extraction
def extract_phonenumber(text):
    phone_regex = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"
    return re.findall(phone_regex, text)

# 4. Credit Card Number Extraction
def extract_creditcardnumber(text):
    card_regex = r"\b(?:\d{4}[- ]?){3}\d{4}\b"
    return re.findall(card_regex, text)

# 5. Time Extraction
def extract_time(text):
    time_regex = r"\b((1[0-9]|0?[0-9]|2[0-3]):[0-5][0-9]\s?(AM|PM|am|pm)?)"
    matches = re.findall(time_regex, text)
    return [m[0] for m in matches]

# Sample Text
sample_text = """
Email: user@example.com, firstname.lastname@company.co.uk
URL: https://www.example.com, https://subdomain.example.org/page
Phone: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Card: 1234 5678 9012 3456, 1234-5678-9012-3456
Time: 14:30, 2:30 PM, 09:15 am
"""

# Running the Extraction using sample text
print("Emails:", extract_email(sample_text))
print("URLs:", extract_url(sample_text))
print("Phone Numbers:", extract_phonenumber(sample_text))
print("Credit Card Numbers:", extract_creditcardnumber(sample_text))
print("Times:", extract_time(sample_text))
