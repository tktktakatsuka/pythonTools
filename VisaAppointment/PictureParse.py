import sys
import os
from PIL import Image
import pyocr
import pyocr.builders
from plyer import notification


TESSERACT_PATH = 'C:\\python\work\\pythonTool\\VisaAppointment\\Tesseract-OCR'
TESSDATA_PATH = 'C:\\python\work\\pythonTool\\VisaAppointment\\Tesseract-OCR\\tessdata'

os.environ["PATH"] += os.pathsep + TESSERACT_PATH
os.environ["TESSDATA_PREFIX"] = TESSDATA_PATH

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))

fname = "test.png"
txt = tool.image_to_string(
    Image.open("C:\\python\work\\pythonTool\\VisaAppointment\\test.png"),
    lang="eng",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print( txt )




if "We are currently at full capacity. Please try again later" in txt:
    notification.notify(
    title="Pythonで通知",
    message="ここにメッセージを書きます",
    app_name="アプリの名前",
    app_icon="C:\\python\\work\\pythonTool\\VisaAppointment\\ReserveOK.ico",
    timeout=3

)
