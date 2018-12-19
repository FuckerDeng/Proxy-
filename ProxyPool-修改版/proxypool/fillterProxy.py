import requests
from lxml import etree
import time
import threading

class Fillter():
	def __init__(self):
		self.checkHttpsUrl = "https://www.baidu.com/content-search.xml"
		self.hh = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.6.2"
		}
	ips = []
	lock=threading.Lock()

	def chekproxy(self,proxy,full_ip):
		try:
			re = requests.get(self.checkHttpsUrl,proxies = {proxy.lower():proxy.lower()+"://"+full_ip},timeout = 7)
			#print(re.text)
			if re.status_code == 200 and "百度搜索" in re.text:
				Fillter.lock.acquire()
				Fillter.ips.append([proxy,proxy.lower()+"://"+full_ip])
				Fillter.lock.release()
		except Exception as e:
			pass

	def check(proxyList):
		try:
			for aaa in proxyList:
				t = threading.Thread(target = self.chekproxy,args = ("https",aaa))
				t.start()
		except Exception as e:
			print(e)
		proxies = Fillter.ips
		Fillter.ips = []
		return proxies



if __name__ == "__main__":
	
	Fillter()

