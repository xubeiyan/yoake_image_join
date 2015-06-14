yoake.py是用来拼接《更胜夜明前的琉璃色》角色图的Python程序……    
ruc_anime.py是用来拼接品知的漫版版头图的Python程序……顺便可以用来拼任何图……    

###python库要求
使用了[PIL](http://www.pythonware.com/products/pil/)库

###使用方法
python ruc_anime.py inputFileList [outputFileName] [combineType]     
inputFileList是要拼接的图片文件名，outputFileName是输出的文件格式，默认是output.jpg，combineType是拼接模式0代表纵向，1代表横向，默认是1  
   
example:      
		python ruc_anime.py 1.jpg,2.jpg 
		python ruc_anime.py 1.jpg,2.jpg last.jpg
		python ruc_anime.py 1.jpg,2.jpg last.jpg 0  