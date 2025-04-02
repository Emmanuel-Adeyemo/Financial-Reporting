import pdfplumber
import json

# Define mapping for standard keys to possible header names
header_mapping = {
    "TXN_DATE": ["txn date", "transaction date", "post date", "posted date", "date", "transdate", 'posted\ndate'],
    "VAL_DATE": ["val date", "value date", "valuedate", 'value\ndate'],
    "REMARKS": ["remarks", "description", "narration", "transaction details"],
    "DEBIT": ["debit", "debit amount", "outflow", "withdrawal"],
    "CREDIT": ["credit", "credit amount", "inflow", "deposit"],
    "BALANCE": ["balance", "account balance", "closing balance"]
}

poss_words = [
    ["txn date", "transaction date", "post date", "posted date", "date", "transdate", 'posted\ndate'],
    ["val date", "value date", "valuedate", 'value\ndate'],
    ["remarks", "description", "narration", "transaction details"],
    ["debit", "debit amount", "outflow", "withdrawal"],
    ["credit", "credit amount", "inflow", "deposit"],
    ["balance", "account balance", "closing balance"]
]

def find_matching_headers(poss_words, col_headers):
    matching_headers = []  # List to store header lists that match the condition
    for header_list in col_headers:
        found_keywords = []
        for word_group in poss_words:            
            for keyword in word_group:
                for header in header_list:
                    if header is not None:
                        if keyword.lower() in header.lower():  # Case-insensitive comparison
                            found_keywords.append(keyword)
                            break
        if len(found_keywords) >= 2:  # If two or more keywords match
            matching_headers.append(header_list)
    return matching_headers
