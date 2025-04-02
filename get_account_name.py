def extract_metadata(pdf):
    """Extract account name and statement duration from the PDF."""
    account_name = None

    # Define a list of possible phrases indicating account name
    account_keywords = [ "Account Name", "Account Holder", "Cust. Name"]

    # Loop through each page in the PDF
    for page in pdf.pages:
        # Extract the text content of the page
        text = page.extract_text()
        
        if text:
            # Look for account name
            lines = text.split("\n")
            for line in lines:
                for keyword in account_keywords:
                    if keyword.lower() in line.lower():
                        # Extract everything after the keyword
                        account_name = line.replace(keyword, "").strip()
                        break  # Stop once account name is found             
               
    
    return account_name


