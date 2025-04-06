import pdfplumber

def extract_table_with_pdfplumber(pdf_path, output_path, password=None):
    """Extract table and dynamically map headers to JSON format using pdfplumber."""
    structured_data = []  
    account_info = {}

    try:
        # Open the PDF and extract data
        with pdfplumber.open(pdf_path, password=password) as pdf:
            # Extract metadata (Account name)
            account_name = extract_metadata(pdf)
            account_info["account_name"] = account_name

            tables = []

            # check step 1
            try:
                for page in pdf.pages:
                    table = page.extract_table()
                     #print(table)
                    if table:
                        tables.extend(table)  # combine into a single list
                print("Step One succeeded: Extracted all tables into a single list.")
            
            except Exception as e:
                print(f"Step One failed: {e}. Falling back to Step Two...")

                # if failed, use step 2
                tables = []  # Reset tables
                try:
                    for page in pdf.pages:
                        table = page.extract_table()
                        if table:
                            tables.append(table)  # append separately
                    print("Step Two succeeded: Extracted tables page-by-page.")
                
                except Exception as fallback_error:
                    print(f"Step Two failed: {fallback_error}. Unable to extract tables.")
                    raise  # exception, if both fails

            # if successful
            if tables:
                try:
                    
                    actual_header = find_matching_headers(poss_words, tables)[0]
                    mapped_headers = match_headers(actual_header)

                    
                    for row in tables:
                        transaction = {}
                        for i, cell in enumerate(row):
                            # print(cell)
                            if cell is not None:  
                                # Remove \n from value
                                clean_cell = cell.replace("\n", "").strip()
                                if actual_header[i] in mapped_headers:  
                                    transaction[mapped_headers[actual_header[i]]] = clean_cell
                        structured_data.append(transaction)
                    
                    print("Data processed successfully.")
                
                except Exception as processing_error:
                    print(f"Error during data processing: {processing_error}.")
                    raise  

    except Exception as e:
        print(f"Critical error: Unable to open or process the PDF. Error: {e}.")
        raise  

    # get statement duration from the transactions
    account_info["statement_duration"] = extract_metadata_from_transactions(structured_data)

    # remove empty dictionaries
    filtered_data = [entry for entry in structured_data if any(value is not None for value in entry.values())]
    #print(filtered_data)
    
    # combine all results
    result = {"account_info": account_info, "transactions": filtered_data}

    #return filtered_data
    # save to a JSON file
    try:
        with open(output_path, "w") as json_file:
            json.dump(result, json_file, indent=4)
        print(f"Extracted transactions saved to {output_path}")
    
    except Exception as save_error:
        print(f"Error saving JSON data: {save_error}.")
        raise  
