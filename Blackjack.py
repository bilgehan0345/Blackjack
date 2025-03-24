from time import sleep
import random
class Games:
    def __init__(self):
        self.chooseClass = ['Maça','Kare','Kupa','Sinek']
        self.chooseNumber = ['A','2','3','4','5','6','7','8','9','10','Bacak','Kız','Papaz']
        self.mylist = []
        self.botlist = []
        self.choosedCards = []
    def FindSum(self,list,x=''):
        sum = 0
        ACount = 1
        for i in list:
            try:
                int(i[-1])
                sum += int(i[-1])
                if i[-1]=='0':
                    sum+=10
            except ValueError:
                if i[-1]=='A':
                    pass
                else:
                    sum += 10
        AList = []
        for i in list:
            if i[-1]=='A':
                AList.append(i)
        for i in AList:
            if len(AList)==1:
                if i[-1]=='A':
                    if sum<=10:
                        if list==self.botlist:
                            if x=='Text':
                                print("Botun As'ı 11 Olarak Seçilmiştir.")
                        else:
                            if x=='Text':
                                print("As'ınız 11 Olarak Seçilmiştir.")
                        sum += 11
                        break
                    else:
                        if list!=self.botlist:
                            if x=='Text':
                                print("Botun As'ı 1 Olarak Seçilmiştir.")
                        else:
                            if x=='Text':
                                print("As'ınız 1 Olarak Seçilmiştir.")
                        sum += 1
                        break
            elif len(AList)==2:
                if i[-1]=='A':
                    if sum<=9:
                        if list==self.botlist:
                            if x=='Text':
                                print(f"Botun As({ACount})'ı 11 Olarak Seçilmiştir.")
                        else:
                            if x=='Text':
                                print(f"As({ACount})'ınız 11 Olarak Seçilmiştir.")
                        sum += 11
                    else:
                        if list==self.botlist:
                            if x=='Text':
                                print(f"Botun As({ACount})'ı 1 Olarak Seçilmiştir.")
                        else:
                            if x=='Text':
                                print(f"As({ACount})'ınız 1 Olarak Seçilmiştir.")
                        sum += 1
                    ACount += 1
            elif len(AList)==3:
                if i[-1]=='A':
                    if sum<=8:
                        if list==self.botlist:
                            if x=='Text':
                                print(f"Botun As({ACount})'ı 11 Olarak Seçilmiştir.")
                        else:
                            if x=='Text':
                                print(f"As({ACount})'ınız 11 Olarak Seçilmiştir.")
                        sum += 11
                    else:
                        if list==self.botlist:
                            if x=='Text':
                                print(f"Botun As({ACount})'ı 1 Olarak Seçilmiştir.")
                        else:
                            if x=='Text':
                                print(f"As({ACount})'ınız 1 Olarak Seçilmiştir.")
                        sum += 1
                    ACount += 1
            elif len(AList)==4:
                if i[-1]=='A':
                    if sum<=7:
                        if list==self.botlist:
                            if x=='Text':
                                print(f"Botun As({ACount})'ı 11 Olarak Seçilmiştir.")
                        else:
                            if x=='Text':
                                print(f"As({ACount})'ınız 11 Olarak Seçilmiştir.")
                        sum += 11
                    else:
                        if list==self.botlist:
                            if x=='Text':
                                print(f"Botun As({ACount})'ı 1 Olarak Seçilmiştir.")
                        else:
                            if x=='Text':
                                print(f"As({ACount})'ınız 1 Olarak Seçilmiştir.")
                        sum += 1
                    ACount += 1         
        return sum
    def ChooseCardtoBot(self):
        botcard = f'{random.choice(self.chooseClass)}-{random.choice(self.chooseNumber)}'
        if botcard in self.choosedCards:
            self.ChooseCardtoBot()
        else:
                self.botlist.append(botcard)
                self.choosedCards.append(botcard)
    def ChooseCardtoMe(self):
        mycard = f'{random.choice(self.chooseClass)}-{random.choice(self.chooseNumber)}'
        if mycard in self.choosedCards:
            self.ChooseCardtoMe()
        else:
            self.mylist.append(mycard)
            self.choosedCards.append(mycard)
    def Blackjack(self):
            self.ChooseCardtoBot()
            self.ChooseCardtoMe()
            sleep(0.4)
            while True:
                print('Kartlar Dağıtılıyor...')
                sleep(0.5) 
                print(f'Botun Kartları : {self.botlist}')
                print(f'Botun Toplam : {self.FindSum(self.botlist,'Text')}')
                print(f'Senin Kartların : {self.mylist}')
                print(f'Senin Toplam : {self.FindSum(self.mylist,'Text')}')
                sleep(0.4)
                if self.FindSum(self.mylist)>21 and self.FindSum(self.botlist)>21:
                    sleep(0.4)
                    print('İkinizde Kaybettiniz.')
                    sleep(0.4)
                    self.mylist = []
                    self.botlist = []
                    self.choosedCards = []
                    break
                elif self.FindSum(self.mylist)<=21 and self.FindSum(self.botlist)>21:
                    sleep(0.4)
                    print('Kazandınız')
                    sleep(0.4)
                    self.mylist = []
                    self.botlist = []
                    self.choosedCards = []
                    break
                elif self.FindSum(self.mylist)==21 and self.FindSum(self.botlist)==21:
                    sleep(0.4)
                    print('İkinizde Kazandınız.')
                    sleep(0.4)
                    self.mylist = []
                    self.botlist = []
                    self.choosedCards = []
                    break
                elif self.FindSum(self.mylist)>21 and self.FindSum(self.botlist)<=21:
                    sleep(0.4)
                    print('Bot Kazandı.')
                    sleep(0.4)
                    self.mylist = []
                    self.botlist = []
                    self.choosedCards = []
                    break
                elif self.FindSum(self.mylist)==21 and self.FindSum(self.botlist)!=21:
                    sleep(0.4)
                    print('Kazandınız.')
                    whosWin='IWin'
                    sleep(0.4)
                    self.mylist = []
                    self.botlist = []
                    self.choosedCards = []
                    break
                elif self.FindSum(self.mylist)!=21 and self.FindSum(self.botlist)==21:
                    sleep(0.4)
                    print('Bot Kazandı.')
                    sleep(0.4)
                    self.mylist = []
                    self.botlist = []
                    self.choosedCards = []
                    break
                elif self.FindSum(self.mylist)<21 and self.FindSum(self.botlist)<21:
                    sleep(0.5)                   
                    process = input('1-Kart Çek\n2-Pas\n')
                    if process=='1':
                        self.ChooseCardtoMe()
                        if self.FindSum(self.botlist)<=11:
                            self.ChooseCardtoBot()
                            sleep(0.4)
                            print('Bot Kart Çekmeyi Seçti.')
                            sleep(0.4)
                        else:
                            if self.FindSum(self.mylist)>11:
                                sleep(0.4)
                                print('Bot Pas Geçmeyi Seçti.')
                                sleep(0.4)
                                continue
                    elif process=='2':
                        if self.FindSum(self.botlist)<=11:
                            self.ChooseCardtoBot()
                            sleep(0.4)
                            print('Bot Kart Çekmeyi Seçti.')
                            sleep(0.4)
                        else:
                            if self.FindSum(self.mylist)>self.FindSum(self.botlist):
                                self.ChooseCardtoBot()
                                print('Bot Kart Çekmeyi Seçti.')
                                sleep(0.4)
                                continue
                            elif self.FindSum(self.botlist)==self.FindSum(self.mylist):
                                sleep(0.4)
                                print('Bot Pas Geçmeyi Seçti.')
                                sleep(0.4)
                                print('Berabere.')
                                self.mylist = []
                                self.botlist = []
                                self.choosedCards = []
                                sleep(0.4)
                                break
                            elif self.FindSum(self.botlist)>self.FindSum(self.mylist):
                                sleep(0.4)
                                print('Bot Pas Geçmeyi Seçti.')
                                sleep(0.4)
                                print('Bot Kazandı.')
                                self.mylist = []
                                self.botlist = []
                                self.choosedCards = []
                                sleep(0.4)
                                break
                    else:
                        sleep(0.4)
                        print('Lütfen 1 veya 2 Geğerlerinden Birini Giriniz.')
                        continue
game = Games()
game.Blackjack()