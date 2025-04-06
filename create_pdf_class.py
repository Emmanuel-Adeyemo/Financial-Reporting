
class PDFReport(FPDF):
    def header(self):
        # Title
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'Account Statement Summary', border=False, ln=True, align='C')
        self.ln(10)

    def footer(self):
        # Footer
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', border=False, ln=False, align='C')

    def add_title(self, title):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def add_section(self, title, content):
        # Add sections to the PDF
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, content)
        self.ln()

    def add_table(self, monthly_totals):
        # Add column heads
        self.set_font('Helvetica', 'B', 12)
        self.cell(40, 10, 'Month', 1, 0, 'C')
        self.cell(40, 10, 'Total Debit (Naira)', 1, 0, 'C')
        self.cell(50, 10, 'Total Credit (Naira)', 1, 0, 'C')
        self.cell(60, 10, 'Remaining Balance (Naira)', 1, 1, 'C')

        # ADd table rows
        self.set_font('Helvetica', '', 12)
        for month, totals in monthly_totals.items():
            month_format = datetime.strptime(month, '%Y-%b')
            self.cell(40, 10, month_format.strftime('%B, %Y'), 1, 0, 'C') # Month, yEar format
            self.cell(40, 10, f"{totals['DEBIT']:,.2f}", 1, 0, 'C')
            self.cell(50, 10, f"{totals['CREDIT']:,.2f}", 1, 0, 'C')
            self.cell(60, 10, f"{totals['BALANCE']:,.2f}", 1, 1, 'C')
