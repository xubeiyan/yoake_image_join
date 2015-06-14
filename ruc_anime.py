#coding:utf-8
#!/usr/bin/python

from PIL import Image
import sys

def init():
	#print "parameter:" + str(len(sys.argv))
	if len(sys.argv) == 1:
		print "At least 1 parameter..."
		print "python ruc_anime.py inputFileList [outputFileName] [combineType]"
		print "example: python ruc_anime.py 1.jpg,2.jpg"
		print "example: python ruc_anime.py 1.jpg,2.jpg last.jpg"
		print "example: python ruc_anime.py 1.jpg,2.jpg last.jpg 0"
		exit()
		
	inputFileArray = sys.argv[1].split(",")
	#case when argv is greater than 2
	if len(sys.argv) > 2:
		outputFileName = sys.argv[2]
	else:
		outputFileName = "output.jpg"
	#case when argv is greater than 3
	if len(sys.argv) > 3:
		if sys.argv[3] == "0" or sys.argv[3] == "horizonal":
			combineType = 0
		else:
			combineType = 1
	else:
		combineType = 1
		
	print "input file: " + ",".join(inputFileArray)
	print "output file: " + outputFileName
	print "combine type: " + str(combineType)
	return inputFileArray, outputFileName, combineType

def jpg_join(fileList, newImageFile, type):
	openFile = []
	widthTemp = 0
	heightTemp = 0
	
	if type == 1: #horizonal 横向
		for x in range(0, len(fileList)):
			#print "x:" + str(x)
			openFile.append(Image.open(fileList[x]))
			if heightTemp == 0:
				heightTemp = openFile[x].size[1]
				
			if openFile[x].size[1] != heightTemp:
				print fileList[x] + " has height " + str(openFile[x].size[1]) + ", not equal " + str(heightTemp)
				return -1
				
			widthTemp += openFile[x].size[0]
		newImg = Image.new('RGB', (widthTemp, heightTemp), 255)
		
		pasteWidth = 0
		for file in openFile:
			newImg.paste(file, (pasteWidth, 0))
			pasteWidth += file.size[0]
		
	elif type == 0: #vertical 纵向
		for x in range(0, len(fileList)):
			#print "x:" + str(x)
			openFile.append(Image.open(fileList[x]))
			if widthTemp == 0:
				widthTemp = openFile[x].size[0]
				
			if openFile[x].size[0] != widthTemp:
				print fileList[x] + " has width " + str(openFile[x].size[0]) + ", not equal " + str(widthTemp)
				return -1
				
			heightTemp += openFile[x].size[1]
		newImg = Image.new('RGB', (widthTemp, heightTemp), 255)
		
		pasteHeight = 0
		for file in openFile:
			newImg.paste(file, (0, pasteHeight))
			pasteHeight += file.size[1]
		
		
	newImg.save(newImageFile)
	
input, output, type = init()

jpg_join(input, output, type)	