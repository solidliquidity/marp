import subprocess
import os
import time
import asyncio
from telegram import Bot
from telegram.error import TelegramError

def create_settings(theme="default", classes=None):
    classes_str = "\n - " + "\n - ".join(classes) if classes else ""
    return f"""---
marp: true
theme: {theme}
class:{classes_str}
"""

def create_slide(title, content, position=""):
    slide = f"""---
{'' if not position else f'style: {position}'}
# {title}
{content}
"""
    return slide

class PythonMarp:
    def __init__(self, theme="default", classes=None, output_file="marp_presentation.html"):
        self.settings = create_settings(theme, classes)
        self.slides = []
        self.output_file = output_file

    def add_slide(self, title, content, position=""):
        self.slides.append(create_slide(title, content, position))

    def generate_presentation(self):
        """Generate HTML presentation first, then optionally convert to PDF"""
        # Create markdown content
        marp_content = self.settings + "\n".join(self.slides)
        
        # Write to HTML file
        html_file = self.output_file
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(marp_content)
        
        print(f"HTML presentation saved as: {html_file}")
        return html_file  # Return the path so it can be used later

    def convert_to_pdf(self, html_file=None):
        """Convert the presentation to PDF using marp-cli"""
        if html_file is None:
            html_file = self.output_file
            
        pdf_output = html_file.replace(".html", ".pdf")
        
        result = subprocess.run(
            ["npx", "@marp-team/marp-cli", html_file, "--pdf", "--output", pdf_output],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"PDF exported to {pdf_output}")
            return pdf_output
        else:
            print(f"Error converting to PDF: {result.stderr}")
            return None

async def send_to_telegram(token, chat_id, pdf_path, caption=None):
    """Send a PDF file to Telegram"""
    bot = Bot(token=token)
    try:
        with open(pdf_path, 'rb') as pdf_file:
            await bot.send_document(
                chat_id=chat_id,
                document=pdf_file,
                caption=caption,
                filename=os.path.basename(pdf_path)
            )
        print(f"PDF sent successfully to Telegram chat {chat_id}")
        return True
    except Exception as e:
        print(f"Error sending to Telegram: {e}")
        return False