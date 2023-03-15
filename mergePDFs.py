import os
import logging
import platform
from PyPDF2 import PdfMerger


def merge_pdfs(input_dir, output_path):
    try:
        merger = PdfMerger()
        for filename in os.listdir(input_dir):
            if filename.endswith('.pdf'):
                filepath = os.path.join(input_dir, filename)
                merger.append(filepath)
        merger.write(output_path)
        merger.close()
        logging.info('Merged PDFs successfully.')
        if platform.system() == 'Windows':
            os.startfile(output_path) # open the merged PDF file on Windows
        else:
            os.system(f"open '{output_path}'") # open the merged PDF file on macOS and Linux
    except Exception as e:
        logging.error(f'Error mergin PDFs: {str(e)}')

if __name__ == '__main__':
    # set the logging config to print all logging messages with level info or higher severity (includes error)
    # to the console. 
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    input_dir = input('provide path/to/folder/with/pdfs: ')
    output_path = input('provide path/to/output/merged.pdf: ')
    merge_pdfs(input_dir, output_path)
