def checkFileType(param):
    if "/png;" in param:
        return "png"
    elif "/pdf;" in param:
        return "pdf"
    elif "/doc" in param:
        return "doc"
    else:
        return "docx"


def FileData(param):
    str = ";base64,"
    idx = param.index(str) + len(str)
    return param[idx:]


def addFile_pdf(param):
    with open(f"apps/Analysis/userfiles/userfile.pdf", "wb") as k:
        k.write(param)
    k.close()


def addFile_png(param):
    with open(f"apps/Analysis/userfiles/userfile.png", "wb") as k:
        k.write(param)
    k.close()


def addFile_doc(param):
    with open(f"apps/Analysis/userfiles/userfile.doc", "wb") as k:
        k.write(param)
    k.close()


def addFile_docx(param):
    with open(f"apps/Analysis/userfiles/userfile.docx", "wb") as k:
        k.write(param)
    k.close()


def addFile(fileData, fileType):
    if fileType == "pdf":
        addFile_pdf(fileData)
    elif fileType == "png":
        addFile_png(fileData)
    elif fileType == "doc":
        addFile_doc(fileData)
    else:
        addFile_docx(fileData)
