import requests
from bs4 import BeautifulSoup


class InternShipData:
    def __init__(self):
        self.title = None
        self.company_name = None
        self.duration = None


def get_internship_information():
    url = "https://job.incruit.com/jobdb_list/searchjob.asp?ct=14&ty=1&cd=4"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    soup = soup.find('div', {'class': 'n_job_list_default'})

    title = []
    companyname = []
    duration = []
    # 인턴십 제목 찾는 파트
    temp = soup.find_all('span', {'class': 'accent'})
    for t in temp:
        atag = t.find_all('a')[-1] # 마지막에 나오는 atag만 가져옴
        if atag.get('title') is not None:
            title.append(atag['title'])

    # 인턴십 회사명
    temp = soup.find_all('span', {'class': 'links'})
    for t in temp:
        atag = t.find('a')
        if atag.get('title') is not None:
            companyname.append(atag['title'])

    # 인턴십 만기일
    temp = soup.find_all('div', {'class': 'ddays'})
    for t in temp:
        ptag = t.find_all('p')
        duration.append(ptag[-1].get_text())

    total_list = []
    for i in range(len(title)):
        intern_data = InternShipData()
        intern_data.title = title[i]
        intern_data.company_name = companyname[i]
        intern_data.duration = duration[i]
        total_list.append(intern_data)

    return total_list
