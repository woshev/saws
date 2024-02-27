import urllib

from shiftlab_ocr.doc2text.reader import Reader


urllib.request.urlretrieve(
  'https://raw.githubusercontent.com/konverner/shiftlab_ocr/main/demo_image.png',
   'test.png')
   
reader = Reader()
result = reader.doc2text("test.png")
print(result[0])