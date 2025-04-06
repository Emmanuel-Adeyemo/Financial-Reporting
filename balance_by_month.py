def balance_by_month(json_path):
    
    with open(json_path, 'r') as file:
        bank_dta = json.load(file)

    account_name = bank_dta['account_info']['account_name']
    statement_duration = bank_dta['account_info']['statement_duration']

    monthly_totals = collections.defaultdict(lambda: {'DEBIT': Decimal('0.00'), 'CREDIT': Decimal('0.00'), 'BALANCE': Decimal('0.00')})
    
    for transaction in bank_dta['transactions']:
        post_date = transaction.get('TXN_DATE', '').strip()
    
        if not post_date:  # if post date is empty
            continue
    
        post_date_formatted = format_date(post_date)
        if post_date_formatted:
            month_year = post_date_formatted.strftime('%Y-%b')
        else:
            continue
    
        debit_month_value = transaction.get('DEBIT', "NA").replace(',',"")
        #print(debit_month)
        #print('#')
        if debit_month_value.replace('.', '').isdigit():        
            monthly_totals[month_year]['DEBIT'] += Decimal(debit_month_value)
    
        credit_month_value = transaction.get('CREDIT', 'NA').replace(',', '')
        if credit_month_value.replace('.', '').isdigit():
            monthly_totals[month_year]['CREDIT'] += Decimal(credit_month_value)

        balance_month_value = transaction.get('BALANCE', 'NA').replace(',', '')
        if balance_month_value.replace('.', '').isdigit():
            monthly_totals[month_year]['BALANCE'] = Decimal(balance_month_value) # this should save the last bal of month
    
    

    return monthly_totals, account_name, statement_duration
    
