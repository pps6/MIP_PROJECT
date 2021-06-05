from fpdf import FPDF
import pandas as pd
import numpy as np
from datetime import datetime



def create_pdf(filename,fraud_cases):
     
    # Create instance of FPDF class
    # Letter size paper, use inches as unit of measure
    pdf=FPDF(format='letter', unit='in')
     
    # Add new page. Without this you cannot create the document.
    pdf.add_page()
     
    # Remember to always put one of these at least once.
    pdf.set_font('Times','',10.0) 
     
    # Effective page width, or just epw
    epw = pdf.w - 2*pdf.l_margin
     
    # Set column width to 1/4 of effective page width to distribute content 
    # evenly across table and page
    col_width = epw/4
     
    # Since we do not need to draw lines anymore, there is no need to separate
    # headers from data matrix.
    
    now = datetime.now() 
    timestamp = now.strftime('%B %d %Y %H-%M-%S')

    headers = ['Sr No.','Index','Time','Amount']
     
     
    # Text height is the same as current font size
    th = pdf.font_size
      
    # Line break equivalent to 4 lines
    
    pdf.set_font('Times','',9.0)
    pdf.cell(epw,0.0,timestamp,align='R')

    pdf.ln(4*th)
    pdf.set_font('Times','B',14.0) 
    pdf.cell(epw, 0.0, 'Fraudulent Transactions', align='C')
    pdf.set_font('Times','',12.0) 
    pdf.ln(0.5)
    if len(fraud_cases) <= 0:
        pdf.cell(epw,0.0,'No transactions found',align='C')
        pdf.ln(0.5)
    else:
        pdf.cell(epw,0.0,f'{len(fraud_cases)} fraud transactions found',align='C')
        pdf.ln(0.5) 
        transactions = pd.read_csv(filename, index_col=None)
        subset = transactions[["Time","Amount"]]
        x = subset.loc[fraud_cases,:]
        # x['Index'] = fraud_cases
        x.reset_index(inplace=True)
        # print(x.head())
        x = np.array(x)

        pdf.set_font('Times','B',10.0)
        for i in range(4):
            # Enter data in colums
            pdf.cell(col_width, 2*th, str(headers[i]), border=1,align='C')
        pdf.ln(2*th)
         

        pdf.set_font('Times','',10.0)
        # Here we add more padding by passing 2*th as height
        for row in range(0,len(x)):
            pdf.cell(col_width, 2*th, str(row+1), border=1,align='C')
            for col in range(3):
                # Enter data in colums
                pdf.cell(col_width, 2*th, str(x[row][col]), border=1,align='C')
         
            pdf.ln(2*th)
     
    output_filename = 'output_' + timestamp + '.pdf'
    #output_filename = 'output_June_05.pdf'
    pdf.output(output_filename,'F')
    return output_filename
     
if __name__ == '__main__':
    fraud_cases = [4,5,6,7,8]
    create_pdf('/home/nilay/test/MIP_PROJECT/datasets/data_part1.csv',fraud_cases)
