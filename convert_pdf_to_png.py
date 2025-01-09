import fitz  # PyMuPDF
import os

def convert_pdf_to_png(pdf_path, output_folder):
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"No such file: '{pdf_path}'")
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    try:
        # Open the PDF document
        pdf_document = fitz.open(pdf_path)
        
        # Iterate through each page and convert to PNG
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            pix = page.get_pixmap()
            output_file = os.path.join(output_folder, f"Page-{page_num + 1}.png")
            pix.save(output_file)
        
        print(f"PDF converted successfully. Images saved in '{output_folder}'")
    except fitz.FitzError as e:
        raise RuntimeError(f"Failed to open or process PDF: {e}")
    except Exception as e:
        raise RuntimeError(f"Failed to convert PDF to PNG: {e}")

# Get the current script path
current_path = os.path.dirname(os.path.abspath(__file__))

# Define the PDF file path and output folder path
pdf_file_path = os.path.join(current_path, "sample.pdf") # Change this to your PDF file path
output_folder_path = os.path.join(current_path, "output")

# Convert the PDF to PNG images
convert_pdf_to_png(pdf_file_path, output_folder_path)
