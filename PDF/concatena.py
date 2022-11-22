import os
from PyPDF2 import PdfFileReader, PdfFileMerger

filesDir = r'C:\Users\User\Documents\python\ferramentas\arquivos'
pdfFiles = [f for f in os.listdir(filesDir) if f.endswith('pdf')]
merger = PdfFileMerger()

for fileName in pdfFiles:
    merger.append(PdfFileReader(os.path.join(filesDir, fileName), 'rb'))
merger.write(os.path.join(filesDir, 'concat.pdf'))

print('Arquivos mesclados com sucesso!')
