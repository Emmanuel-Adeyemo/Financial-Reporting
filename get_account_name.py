def extract_metadata(pdf):
    """Extract account name and statement duration from the PDF."""
    account_name = None

    account_keywords = [ "Account Name", "Account Holder", "Cust. Name"]

    for page in pdf.pages:
        text = page.extract_text()
        
        if text:
            lines = text.split("\n")
            for line in lines:
                #print(line.lower())
                for keyword in account_keywords:
                    if keyword.lower() in line.lower():
                        
                        account_name = line.replace(keyword, "").strip()
                        break  # Stop once account name is found             
               
    
    return account_name


