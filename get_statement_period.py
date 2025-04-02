
def extract_metadata_from_transactions(transactions):
    """Calculate statement duration from the first and last transaction dates."""
    statement_duration = None

    if transactions:
        # Sort transactions by the TXN_DATE key to ensure chronological order
        try:
            sorted_transactions = transactions #sorted(transactions, key=lambda x: x.get("TXN_DATE"))

            # Extract the first and last dates
            start_date = sorted_transactions[1].get("TXN_DATE")  # First transaction date
            end_date = sorted_transactions[-2].get("TXN_DATE")  # Last transaction date

            # Format the statement duration
            if start_date and end_date:
                statement_duration = f"{start_date} to {end_date}"
        except Exception as e:
            print(f"Error calculating statement duration: {e}")

    return statement_duration


