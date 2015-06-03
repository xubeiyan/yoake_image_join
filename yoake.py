#coding:utf-8
from PIL import Image
import sys
jpgFile = 'cha_s03'
#print jpgFile


def yoake_cha_join(fileList, newImageFile, type = 1):
	imgA = Image.open(fileList + 'a.jpg')
	imgB = Image.open(fileList + 'b.jpg')
	imgC = Image.open(fileList + 'c.jpg')
	imgD = Image.open(fileList + 'd.jpg')
	
	
	if not (imgA.size[0] == imgB.size[0] and imgB.size[0] == imgC.size[0]):
		print "the widths of a,b,c not equal"
		return
		
	if not (imgA.size[1] + imgB.size[1] + imgC.size[1] == imgD.size[1]):
		print "the sum of heights of a,b,c not equal to the height of d"
		return 
		
	print "FileName: " + fileList + '.jpg'
	print "Width=" + str(imgA.size[0] + imgD.size[0])
	print "Height=" + str(imgD.size[1])
	#newImgWidth = sourceImg[0].size
	
	newImg = Image.new('RGB', (imgA.size[0] + imgD.size[0], imgD.size[1]), 255)
		
	if type == 1:
		newImg.paste(imgA, (0, 0))
		newImg.paste(imgB, (0, imgA.size[1]))
		newImg.paste(imgC, (0, imgA.size[1] + imgB.size[1]))
		newImg.paste(imgD, (imgA.size[0], 0))
	else:
		newImg.paste(imgA, (imgA.size[0], 0))
		newImg.paste(imgB, (imgA.size[0], imgA.size[1]))
		newImg.paste(imgC, (imgA.size[0], imgA.size[1] + imgB.size[1]))
		newImg.paste(imgD, (0, 0))
	
	newImg.save(newImageFile)
	
yoake_cha_join(jpgFile, jpgFile + '.jpg', 1)