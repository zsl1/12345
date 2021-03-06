from selenium import webdriver
import os
import requests
import re
from urllib.request import urlopen


# 全局声明的可以写到配置文件，这里为了读者方便看，故只写在一个文件里面
# 图片地址
picpath = r'E:\Python_Doc\Images'
# 网站地址
ooxx_url = "http://jandan.net/ooxx/page-{}#comments"
# chromedriver地址
# chromedriver = "C:\Program Files\Python36\Scripts\chromedriver.exe"


# 保存路径的文件夹，没有则自己创建,不能创建目录
def setpath(name):
	path = os.path.join(picpath, name)
	if not os.path.isdir(path):
		os.mkdir(path)
	return path


# 用chrome headless打开网页
def gethtml(url):
	# options = webdriver.ChromeOptions()

	# options.add_argument('--headless')
	# browser = webdriver.Chrome(chromedriver, chrome_options=options)
	
	# browser = webdriver.Chrome(chrome_options=options)
	browser = webdriver.PhantomJS()
	browser.get(url)
	html = browser.page_source
	browser.quit()
	return html


# 打开网页返回网页内容
def open_webpage(html):
	reg = r"(http:\S+(\.jpg|\.png))"
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	return imglist


# 保存照片
def savegirl(path, url):
	# content = urlopen(url).read()

	request = urlopen(url) #这里是要读取内容的url  
	content = request.read() #读取，一般会在这里报异常  
	request.close() #记得要关闭  

	with open(path + '/' + url[-11:], 'wb') as code:
		code.write(content)


def do_task(path, index):
	print("正在抓取第 %s 页" % index)
	web_url = ooxx_url.format(index)
	htmltext = gethtml(web_url)
	imglists = open_webpage(htmltext)
	print("抓取成功，开始保存 %s 页图片" % index)
	for j in range(len(imglists)):
		savegirl(path, imglists[j][0])


if __name__ == '__main__':
	filename = "OOXX"
	for i in range(1, 310):
		filepath = setpath(filename+'\\'+str(i))
		do_task(filepath, i)