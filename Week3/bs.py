from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")
# print(r)  # afiseaza incarcarea paginii cu succes
# print(r.text) # afiseaza sursa paginii
link = BeautifulSoup(r.text, "html.parser")
# print(link)

title = link.find_all('div', attrs={'class': 'contentDiv'})
# print(title)
header = []
for i in title:
    # print(i)
    for tr_index in i.find_all('table'):
        # print(tr_index)
        # for td_index in tr_index.find_all('tr'):
        # print(td_index)
        # if td_index.find_add('th'):
        # print(td_index.find_all('th'))
        # for th_index in td_index.find_all('th'):
        #     print(th_index.get_text())
        #     header.append(th_index.get_text())
        header = [th_index.get_text() for th_index in tr_index.find_all('th')]
print(header)
