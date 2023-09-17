from bs4 import BeautifulSoup
import requests

source2 = requests.get(
    "https://www.timeanddate.com/on-this-day/february/6", headers={"User-Agent": ""}
)
source2.raise_for_status()

soup2 = BeautifulSoup(source2.text, "html.parser")
personalities = soup2.find("div", class_="otd-life__block").find_all("li")
file = open(
    "Personalities_born.txt", "w", encoding="utf-8"
)  # Specify encoding as utf-8
file.write("\n\n" + ".....PERSONALITIES I SHARE MY BIRTHDAY WITH ..... " + "\n\n")
print("\n\n" + ".....PERSONALITIES I SHARE MY BIRTHDAY WITH ..... " + "\n\n")
for person in personalities:
    name2 = person.find("h3", class_="otd-title").text
    print(name2)
    file.write("\n\n" + name2)


source1 = requests.get(
    "https://www.britannica.com/more-on-this-day/February-6", headers={"User-Agent": ""}
)
source1.raise_for_status()

soup1 = BeautifulSoup(source1.text, "html.parser")

# Find all div elements with the class "card-body"
card_bodies = soup1.find_all("div", attrs={"class": "card-body"})

file.write("\n\n" + "......IMPORTANT EVENTS HAPPENED ON MY BIRTHDAY....... " + "\n\n")
print("\n\n" + "......IMPORTANT EVENTS HAPPENED ON MY BIRTHDAY....... " + "\n\n")
# Loop through each element in card_bodies and extract the text
for card_body in card_bodies:
    name1 = card_body.text
    data1 = str(name1)
    print(data1)
    file.write("\n\n" + data1)


file.flush()
file.close()
