import pyttsx3
from PyPDF2 import PdfReader

try:
    pdf_path = 'Engineering Fundamentals.pdf'
    pdfReader = PdfReader(pdf_path)
    total_pages = len(pdfReader.pages)
    print("Total pages:", total_pages)

    bot = pyttsx3.init()

    start_page = int(input("Enter the starting page number: "))

    if start_page < 1 or start_page > total_pages:
        print("Invalid page number.")
    else:
        for num in range(start_page - 1, total_pages):
            page = pdfReader.pages[num]
            text = page.extract_text()
            print(text)
            bot.say(text)
            bot.runAndWait()

        speaker.stop()

except Exception as e:
    print("An error occurred:", str(e))
