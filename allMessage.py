import requests
from bs4 import BeautifulSoup
import json


def carDetail():
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"}
    sum = 1
    html = ""
    while True:
        s = requests.session()
        url = "https://carsearch.audi.cn/usedcar/i/s%7C10,AACG,AACH,AABY,AACI,AACJ/l%7C12,"+str(sum)+",STAT_GWPLUS,U/controller.htm?act=list&v=4&scrolling=1"
        s.keep_alive = False  # 关闭多余连接
        response = s.get(url,headers=header)
        newHtml = response.content.decode('utf8')
        allPage = []
        if newHtml != html:
            carMessage = json.loads(newHtml)["html"]
            soup = BeautifulSoup(carMessage,"lxml")
            carName = soup.findAll("h3")
            carConfiguration = soup.select(".description")
            carPrice = soup.select(".price")
            carCompany = soup.select(".vtp-link")
            carAgeAndMileage = soup.select(".summary-data-list")
            carImg = soup.select(".picture")
            for i in range(len(carName)):
                name = carName[i].text
                configuration = carConfiguration[i].text
                price = carPrice[i].text
                company = carCompany[i].text
                age = carAgeAndMileage[i].find_all("li")[0].find_all("p")[1].text
                mileage = carAgeAndMileage[i].find_all("li")[1].find_all("p")[1].text
                img = carImg[i].find("img")["src"]
                onePage = {name:name,configuration:configuration,price:price,company:company,age:age,mileage:mileage,img:img}
                allPage.append(onePage)
            html = newHtml
            print("第" + str(sum) + "页抓取完毕")
            sum+=1
    return allPage


if __name__ == "__main__":
    print(carDetail())