from bs4 import BeautifulSoup
import requests,openpyxl,time

excel = openpyxl.Workbook()
# print(excel.sheetnames)
sheet = excel.active
sheet.title='My top 5 favourite Movies'
print(excel.sheetnames)
sheet.append(['MovieName','IMDBRating'])
source = requests.get("https://www.imdb.com/chart/top/",headers = {'User-Agent' : ''})
source.raise_for_status()

soup = BeautifulSoup(source.text,'html.parser')
movies = soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base").find_all('li')
for movie in movies:
  name=movie.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b51a3d33-7 huNpFl cli-title").a.text
  rating = movie.find('span',class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text
  if name == "1. The Shawshank Redemption" or name =="3. The Dark Knight" or name =="5. 12 Angry Men" or name =="8. Pulp Fiction" or name =="11. Forrest Gump":
    print(name,rating)
    sheet.append([name,rating])
    time.sleep(1)

excel.save('IMDB Movie Ratings.xlsx')