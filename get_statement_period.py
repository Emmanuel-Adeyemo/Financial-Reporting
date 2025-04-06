
def extract_metadata_from_transactions(transactions):
    """Calculate statement duration from the first and last transaction dates."""
    statement_duration = None

    if transactions:
        
        try:
            sorted_transactions = transactions #sorted(transactions, key=lambda x: x.get("TXN_DATE"))

            # get first and last dates
            start_date = sorted_transactions[1].get("TXN_DATE")  # First txn date
            end_date = sorted_transactions[-2].get("TXN_DATE")  # Last txn date

            # format out
            if start_date and end_date:
                statement_duration = f"{start_date} to {end_date}"
        except Exception as e:
            print(f"Error calculating statement duration: {e}")

    return statement_duration


