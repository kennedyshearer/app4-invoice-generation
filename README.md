# Invoice Generation App

A Python application that automatically converts Excel invoice files into professional PDF invoices. This tool processes Excel files containing invoice data and generates formatted PDF invoices with company branding.

## 🚀 Features

- **Automatic Excel to PDF Conversion**: Processes multiple Excel files in batch
- **Professional Invoice Formatting**: Creates clean, professional-looking PDF invoices
- **Company Branding**: Includes company logo and branding elements
- **Automatic Calculations**: Calculates totals and subtotals automatically
- **Batch Processing**: Handles multiple invoice files at once
- **Structured Data**: Expects standardized Excel format with specific columns

## 📋 Requirements

- Python 3.6+
- pandas
- fpdf
- openpyxl (for Excel file reading)

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/app4-invoice-generation.git
cd app4-invoice-generation
```

2. Install required dependencies:
```bash
pip install pandas fpdf openpyxl
```

## 📁 Project Structure

```
app4-invoice-generation/
├── main.py              # Main application script
├── invoices/            # Directory containing Excel invoice files
│   ├── 10001-2023.1.18.xlsx
│   ├── 10002-2023.1.18.xlsx
│   └── 10003-2023.1.18.xlsx
├── PDFs/               # Generated PDF invoices
│   ├── 10001-2023.1.18.pdf
│   ├── 10002-2023.1.18.pdf
│   └── 10003-2023.1.18.pdf
├── pythonhow.png       # Company logo
└── README.md
```

## 📊 Excel File Format

Your Excel files should be named in the format: `{invoice_number}-{date}.xlsx`

Example: `10001-2023.1.18.xlsx`

The Excel file should contain a sheet named "Sheet 1" with the following columns:
- `product_id` - Product identifier
- `product_name` - Name of the product
- `amount_purchased` - Quantity purchased
- `price_per_unit` - Price per unit
- `total_price` - Total price for this item

## 🚀 Usage

1. Place your Excel invoice files in the `invoices/` directory
2. Ensure your company logo (`pythonhow.png`) is in the root directory
3. Run the application:
```bash
python main.py
```

4. Generated PDF invoices will be saved in the `PDFs/` directory

## 📄 Generated PDF Features

Each generated PDF invoice includes:
- Invoice number and date (extracted from filename)
- Professional table format with all product details
- Automatic total calculation
- Company branding with logo
- Clean, readable formatting

## 🔧 Customization

To customize the application for your business:

1. **Company Logo**: Replace `pythonhow.png` with your company logo
2. **Company Name**: Update the company name in the code (currently "PythonHow")
3. **Styling**: Modify fonts, colors, and layout in `main.py`
4. **Column Names**: Update the column processing if your Excel format differs

## 📝 Example Output

The application generates professional PDF invoices with:
- Header with invoice number and date
- Tabular data with product details
- Automatic total calculation
- Company branding at the bottom

## ⚠️ Notes

- Ensure Excel files follow the expected naming convention
- The application expects specific column names in the Excel files
- Generated PDFs will overwrite existing files with the same name
- Make sure the `PDFs/` directory exists before running the script

## 🐛 Troubleshooting

- **File not found errors**: Ensure Excel files are in the `invoices/` directory
- **Column errors**: Verify Excel files have the expected column names
- **PDF generation errors**: Check that the `PDFs/` directory exists and is writable
- **Logo errors**: Ensure `pythonhow.png` is in the root directory

---

**Built with ❤️ using Python, pandas, and FPDF**
