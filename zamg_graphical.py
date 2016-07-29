from bs4 import BeautifulSoup

import requests, pygame

pygame.init()
screen = pygame.display.set_mode((596,600))
bg = pygame.image.load("res/stmk.png")
logo = pygame.image.load("res/zamgLogo.png")
myfont = pygame.font.SysFont("monospace", 12)
pygame.display.set_caption('aktuelles Wetter in der Steiermark')
#url = input("Enter a website to extract the URL's from: ")

url = "www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/steiermark/temperatur/?mode=geo&druckang=red"
r  = requests.get("http://" +url)

data = r.text
names = ["Aigen","Mariazell","Muerzzuschlag","Leoben","Zeltweg","Deutschlandsberg","Bad Radkersburg","Fuerstenfeld","Graz","Murau", "Mooslandl"]
numbers = ["eins","zwei","drei","vier","fuenf","sechs","sieben","acht","neun","zehn","elf"]
pos = [(115,85), (315,16), (400,50),(305,120),(230,170),(310,260),(455,275),(470,205),(360,180),(140,170),(230,30)]
soup = BeautifulSoup(data, "html.parser")
Data = [None] * 11
symbol = [None] * 11
label = [None] * 11

timeData = soup.find_all('h2',{'class':'dynPageTextHead float_left no_margin_bottom'})
timeLabelText = timeData[0].text.strip()

title = myfont.render(timeLabelText, 1, (255,255,255))
credit = myfont.render("[ heger.me ] 2016", 1, (255,255,255))
screen.blit(title, (250, 355))
pygame.draw.rect(screen, (255,255,255), (270,400,320,140), 0)
screen.blit(credit, (465,575))
screen.blit(bg, (0,0))
screen.blit(logo, (250,400))
pygame.display.update()

#<h2 class="dynPageTextHead float_left no_margin_bottom">Aktuelle Messwerte der Wetterstationen von 09 Uhr</h2>

for b in range(0,11):
    Data[b] = soup.find_all('span',{'id':'oltemp_'+ numbers[b] +'_stmk'})
    symbol[b] = soup.find_all('img',{'id':'olimg_'+ numbers[b] + '_stmk'})




#temp2 = list(pos[0])[1]
#print(temp2)
#print(val[0].get('src')[-10:])

print("Temperaturskript")
print("Daten von http://www.zamg.ac.at")
print("zum Updaten bitte Beenden und neu starten")
print("Enter zum Beenden druecken")

for a in range(0,11):
    #print(names[a] + ": " + temp[a][0].text.strip())
    #print(symbol[a][0].get('src')[-10:])
    label[a] = myfont.render(names[a] + ": " + Data[a][0].text.strip(), 1, (153,0,0))
    temp1 = list(pos[a])[0] - 10
    temp2 = list(pos[a])[1] + 50
    screen.blit(label[a], (temp1,temp2))
    label[a] = myfont.render(names[a] + ": " + Data[a][0].text.strip(), 1, (255,255,255))
    screen.blit(label[a], (20,370+a*20))
    symbol[a] = pygame.image.load("res/"+symbol[a][0].get('src')[-10:])
    screen.blit(symbol[a], pos[a])


pygame.display.update()

input()