import pyttsx3
import PyPDF2
book=open('PRAGYA ANAND Resume.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
speaker=pyttsx3.init()
for num in range(0,pages):
    page=pdfReader.getPage(0)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()