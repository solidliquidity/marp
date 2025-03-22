from marp import PythonMarp, send_to_telegram
import os
import asyncio

# Example usage
marp_presentation = PythonMarp(theme="night", classes=["invert", "lead"])
marp_presentation.add_slide("SolidLiquidity", "TL;DR")
marp_presentation.add_slide("Conclusion", "- Thank you for your time\n- Questions?")
html_file = marp_presentation.generate_presentation()
print(f"First presentation file: {html_file}")  # Debug line to see what's returned

# RESET LOCAL PATH for stocks presentation
import sys
sys.path.append('/Users/solidliquidity/Downloads/projects/alpha_vantage')
import alpha_vantage
from alpha_vantage.stockmarkdown import analyze_stock

# Telegram

from os import getenv
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_BOT_TOKEN = getenv("BOT_TOKEN")  # Replace with your actual token
TELEGRAM_CHAT_ID = getenv("CHAT_ID")      # Replace with your actual chat ID

async def send_pdf_to_telegram():
    if os.path.exists(pdf_file):
        caption = f"Stock Analysis Report - {', '.join(stocks)}"
        result = await send_to_telegram(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, pdf_file, caption)
        if result:
            print("PDF sent successfully to Telegram!")
        else:
            print("Failed to send PDF to Telegram.")
    else:
        print(f"Error: PDF file {pdf_file} not found")

def send_marp_presentation_to_telegram(html_file):
    if html_file is None:
        html_file = "marp_presentation.html"
        print(f"Using default filename: {html_file}")

    # marp-cli must be installed
    pdf_file = html_file.replace(".html", ".pdf")
    os.system(f"npx @marp-team/marp-cli {html_file} --pdf --output {pdf_file}")
    print(f"PDF exported to {pdf_file}")
    asyncio.run(send_pdf_to_telegram())
    return 

marp_presentation = PythonMarp(theme="night", classes=["invert", "lead"])
marp_presentation.add_slide("SolidLiquidity", "TL;DR")
stocks = ["MVST", 'ACHR']
for stock in stocks:
    try:
        stock_data = analyze_stock(stock, lookback_days=180)
        marp_presentation.add_slide(stock, stock_data)
        html_file = marp_presentation.generate_presentation()
        print(f"HTML file path: {html_file}")  # Debug line
        send_marp_presentation_to_telegram()
    except Exception as e:
        print(f"Error analyzing {stock}: {str(e)}")
        continue



