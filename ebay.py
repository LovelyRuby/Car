import requests
import re
from bs4 import BeautifulSoup
import json

header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
          # "Cookie":'__utmz=96128154.1536914414.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; cto_lwid=8b0845c4-512d-42f4-bad8-315fdc9aa532; G_ENABLED_IDPS=google; __stripe_mid=c99c07d3-2b53-4ebd-bd7e-870ea41a6f0f; __utma=96128154.1852173920.1536914414.1537177619.1537431782.4; __utmc=96128154; __stripe_sid=91369b27-93d3-4d43-b548-3fad0d317409; _xsrf=2|4453d1e6|059f7727663a84e74374828f128aca73|1537433701; bsid=9ed54638a5be4f2f8d6710b38e3f6de3; __utmt=1; __utmb=96128154.2.10.1537431782; _timezone=8; sweeper_uuid=0ff6805e76124a329f7b52f5c54a07f1; sweeper_session="2|1:0|10:1537433898|15:sweeper_session|84:OGE0Njk0ZWYtOTQ5ZS00NzFhLTg3OTYtMGRhY2QzYjY1MTA0MjAxOC0wOS0yMCAwODo1ODoxOC40NTUyODc=|fe63051b385697590f1c3d0829b8f3a17fbb117a255e9364dd22782f38dc4a7d"'
          }
response = requests.get("https://carsearch.audi.cn/usedcar/i/s%7C9,AA%7C10,AACG,AACH/l%7C12,2,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=0",headers=header)
html = response.content.decode('utf8')
carMessage = json.loads(html)["html"]
print(carMessage)
# out = re.sub(pattern,pattern2,html)
# print(out)