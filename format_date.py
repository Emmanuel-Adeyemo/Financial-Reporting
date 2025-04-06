def format_date(transaction_date):
    """ 
    Parse transaction date with correct format 
    """

    try:
        return datetime.strptime(transaction_date, '%d-%b-%y') 
    except ValueError:

        try:
            return datetime.strptime(transaction_date, '%d-%m-%y')
        except ValueError:

            return None
