# Import the os module, for the os.walk function
import os

def convertRst(dirname,fname,fc):
    for ix, line in enumerate(fc):
        if line == "" or line.isspace():
            fc.insert(1,"#"*(len(fc[0])-1)+"\n")
            fc.insert(2,"\n")
            return
        line = ':'+line[3:]
        if line.startswith(':title'):
            line = line[7:].lstrip()
            fc[ix] = line
        if line.startswith(':date'):
            line = line.replace('-','/')
        fc[ix] = line

def convertMd(dirname,fname,fc):
    # remove first line
    # remove line with -->
    #call convertRst()
    del fc[0]
    ix = fc.index('-->\n')
    del fc[ix]
    for ix, line in enumerate(fc):
        if line == "" or line.isspace():
            return
        line = line[3:].capitalize()
        if line.startswith('Date'):
            line = line.replace('-','/')
        fc[ix] = line

def convertMeta(dirname, fname, fc):
    if fname.endswith('rst'):
        convertRst(dirname,fname,fc)
    elif fname.endswith('md'):
        convertMd(dirname,fname,fc)


# Set the directory you want to start from
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('Processing file %s' % fname)
        if fname.endswith('rst') or fname.endswith('md'):
            with open(os.path.join(dirName,fname),'r',encoding='utf8') as currentFile:
                fc = currentFile.readlines()
            convertMeta(dirName,fname,fc)
            with open(os.path.join(dirName,fname),'w',encoding='utf8') as currentFile:
                currentFile.write("".join(fc))
