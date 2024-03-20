#vlozenie modulu
import tkinter

#nastavenie platna
canvas = tkinter.Canvas(width=480,height=520,background="white")
canvas.pack()

#zadreklarovanie premennej
vyjadrenia = 0

#vytvorenie prazdneho zoznamu
hodiny_nie = {}

#otvorenie suboru
subor = open("spokojnost_1.txt","r")

def vykreslenie(): #funkcia na vykreslenie statistiky
    #nastavenie pociatocnych suradnic
    x = 10
    x1 = 3
    
    for i in range(0,24): #cyklus s opakovanim pre cisla 0-23
        #vykreslenie ciary
        canvas.create_line(x1,500,x1+15,500)

        #podmienka na vypisanie textu
        if i < 10:
            ii = "0"+str(i)
            
            canvas.create_text(x,510,text=ii,font="Arial 10",fill="red")
        else:
            canvas.create_text(x,510,text=i,font="Arial 10",fill="red")

        #zmena suradnic
        x += 20
        x1 += 20

for riadok in subor: #cyklus na prechadzanie riadkov v subore
    #nastavenie pomocnych premennych
    hodina = riadok[0]+riadok[1]
    spokojnost = riadok[6]+riadok[7]+riadok[8]

    #podmienka na pridanie do slovnika
    if spokojnost == "nie":
        vyjadrenia += 1

        if not hodina in hodiny_nie.keys():
            hodiny_nie[str(hodina)] = 0

        #zmena hodnoty v slovniku 
        hodiny_nie[str(hodina)] += 1

#nastavenie pomocnych premennych
max_hodina_nie = max(hodiny_nie, key=hodiny_nie.get)
max_zakaznici_nie = hodiny_nie.get(max_hodina_nie)

#vypisanie pozadovanych hodnot
print("Celkový počet negatívnych vyjadrení:",vyjadrenia)
print(max_hodina_nie+".","hodina mala najviac nespokojných zákazníkov:",max_zakaznici_nie)

for i in hodiny_nie.keys(): #cyklus na prechadzanie klucov v slovniku
    #nastavenie pomocnej premennej
    nie = hodiny_nie.get(str(i))

    #nastavenie pociatocnej/konecnej suradnice
    zaciatok_x = int(i) * 20 + 5
    koniec_y = 500 - (int(nie) * 10)

    #vykreslenie statistiky
    canvas.create_rectangle(zaciatok_x,500,zaciatok_x+10,koniec_y,fill="red")

    #vypisanie pozadovanej hodnoty
    print(i+".","hodina:",nie)

#privolanie funkcie
vykreslenie()

#zatvorenie suboru
subor.close()
