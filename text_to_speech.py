from matplotlib.pyplot import text
import pyttsx3
import PyPDF2
book=open("RUBIK_PDF.pdf","rb")
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
#print(pages)
speaker=pyttsx3.init()
page=pdfreader.getPage(0)
text=page.extract_text()
speaker.say(text)
speaker.runAndWait()