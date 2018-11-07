import requests
from bs4 import BeautifulSoup
import json
from Utils import SqlUtils
import time

def carDetail(url):
    count = 0
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"}
    sum = 1
    html = ""
    mid = 4
    allPage = []
    while True:
        s = requests.session()
        carUrl = url[:url.find("C12,")+mid]+str(sum)+url[url.find("C12,")+mid+1:]
        s.keep_alive = False  # 关闭多余连接
        response = s.get(carUrl,headers=header)
        newHtml = response.content.decode('utf8')
        if newHtml != html:
            carMessage = json.loads(newHtml)["html"]
            soup = BeautifulSoup(carMessage,"lxml")
            carName = soup.select(".details")
            carConfiguration = soup.select(".description")
            carPrice = soup.select(".price")
            carCompany = soup.select(".vtp-link")
            carAgeAndMileage = soup.select(".summary-data-list")
            sellDetails = soup.select(".dealer-imprint-info")
            carImg = soup.select(".image-container")
            for i in range(len(carName)):
                img = []
                name = carName[i].contents[1]["data-track-eventname"]
                configuration = carConfiguration[i].text
                price = carPrice[i].text
                company = carCompany[i].text
                age = carAgeAndMileage[i].find_all("li")[0].find_all("p")[1].text
                mileage = carAgeAndMileage[i].find_all("li")[1].find_all("p")[1].text
                img1 = "https:"+carImg[i].find_all("div")[0].find("img")["src"]
                img2 = "https:"+carImg[i].find_all("div")[1].find("img")["src"]
                img.append(img1)
                img.append(img2)
                cellAddressItem = sellDetails[i].find("div").text.split(" ")#.find_all("p")[1].text
                #['', '云南联迪汽车服务有限公司', '昆明市盘龙区白龙路522号650216', '昆明市', '联系人:黎兆麟', '电话:', '13888377509', '']
                cellAddress = cellAddressItem[2][:-6]
                cellName = cellAddressItem[4][4:]
                cellPhone = cellAddressItem[-2]
                onePageItems = {"carName":name,"carConfiguration":configuration,"carPrice":price,"carName":age,"carMileage":mileage,"carImg":img,"cellCompany":company,"cellAddress":cellAddress,"cellName":cellName,"cellPhone":cellPhone}
                onePage = json.dumps(onePageItems)
                allPage.append(onePage)
            html = newHtml
            count+=len(carName)
            print("第" + str(sum) + "页抓取完毕,已获取"+str(count)+"条数据")
            sum+=1
        else:
            break
    print("该车型爬取完毕")
    return allPage


if __name__ == "__main__":
    TT = "https://carsearch.audi.cn/usedcar/i/s%7C10,AACG,AACH,AABY,AACI,AACJ/l%7C12,2,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
    A1 = "https://carsearch.audi.cn/usedcar/i/s%7C10,AACO,AACV/l%7C12,6,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
    A3 = "https://carsearch.audi.cn/usedcar/i/s%7C10,AAAJ,AAAQ,AADC,AAAO,AADK,AADQ,AADD/l%7C12,2,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
    A4 = "https://carsearch.audi.cn/usedcar/i/s%7C10,AABV,AADP/l%7C12,3,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
    A5 = "https://carsearch.audi.cn/usedcar/i/s%7C10,AABS,AAAY,AABW,AACZ,AACN,AABT,AABK,AACM/l%7C12,4,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
    A6 = "https://carsearch.audi.cn/usedcar/i/s%7C10,AACD,AAAZ,AADR,AAER,AAEI,AABN,AABI/l%7C12,5,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
    A7 = "https://carsearch.audi.cn/usedcar/i/s%7C10,AACP,AADB,AACX/l%7C12,5,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
    全系 = "https://carsearch.audi.cn/usedcar/i/s/l%7C12,3,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
    官方认证 = "https://carsearch.audi.cn/usedcar/i/s%7C1150,1/l%7C12,2,STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
    startTime = time.time()
    all = carDetail(全系)
    SqlUtils.insert(all)
    endTime = time.time()
    print("用时间",endTime-startTime,'s')
    input("按任意键关闭")