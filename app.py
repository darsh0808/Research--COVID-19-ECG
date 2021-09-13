# run coomand: python app.py pdf4/normal/

from pdf2image import convert_from_path
import os
import sys
import shutil

outputdir = "cd4_pdf3/"
count = 1

def convert(file, outputdir):
    global count
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    pages = convert_from_path(file)
    for page in pages:
        myfile = outputdir + 'image' + str(count) + '.jpg'
        count = count + 1
        page.save(myfile, "JPEG")
        print(myfile)
    print(file)

args = sys.argv
if len(args) > 1:
    file = args[1]
    # convert(file, outputdir)

pdfs = os.listdir(file)
j = 0

for i in range(len(pdfs)):
    if pdfs[i].endswith('.pdf'):
        j = j + 1
        convert(file + pdfs[i], outputdir)
    else:
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)
            shutil.copy(file + pdfs[i], outputdir)
        


# print(len(pdfs))
# print(j)






