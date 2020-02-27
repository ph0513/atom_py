from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

mvList = ['179181', '186821', '187321', '186613', '181925', '190026', '172816', '176306', '190325', '187350']
# mvList = ['179181']
with requests.session() as s :
    for mv in mvList :
        urlT = "https://movie.naver.com/movie/bi/mi/basic.nhn?code="+mv
        url = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code="+mv+"&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="
        listP = []
        scoreP = []
        run = True
        i = 1
        saveStr = ""

        rt = s.get(urlT)
        soupT = BeautifulSoup(rt.text, "html.parser")
        mvTitle = str(soupT.select_one("#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)").text)

        #영화 리뷰의 평가내용 및 평점 추출
        while run :
            urlF = url+str(i)
            r = s.get(urlF)
            soup = BeautifulSoup(r.text, "html.parser")
            list = soup.select("span[id^=_filtered_ment_]")
            score = soup.select("div.star_score > em")
            listP += list
            scoreP += score
            i += 1
            if soup.select_one("#pagerTagAnchor"+str(i)) is None :
                run = False

            #10페이지 까지만 추출
            if i > 10 :
                run = False
        #추출한 내용및 평점을 txt파일로 저장
        for i in range(len(listP)-1, -1, -1) :
            content = listP[i].text.strip()
            scr = int(scoreP[i].text)
            star = "★"*(scr//2)+"☆"*(scr%2)
            saveStr += "내용 : {},\n평점 : {} {}\n\n".format(content, star, scr)
        saveStr += "총 리뷰 수 : {}".format(len(listP))
        mvTitle = mvTitle.replace(":","_")
        savePath = "D:/최규리T(공유)/BIG_Py/mv"+mvTitle+".txt"
        with open(savePath, 'wt') as saveFile :
            saveFile.write(saveStr)
