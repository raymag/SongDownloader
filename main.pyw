#======================
#==Codado=Por=Magno==
#=====================

import json as js, webbrowser as wb, time as tm
from tkinter import *

m = open('pull.json', 'r') #pull.json está sendo usado como banco de dados
songList = js.load(m) #songList guarda a lista de links das músicas no youtube
m.close()

def load(): #Está função atualiza a songList com novos links do arquivo pull.json
      m = open('pull.json', 'r')
      songList = js.load(m)
      m.close()

def download(): #Realiza o download das músicas usando o site youtubeinmp3
      url = 'http://www.youtubeinmp3.com/fetch/?video={}'
      for i in songList: 
            x = url.format(i)
            wb.open(x) #Para cada música, uma nova guia será iniciada no navegador padrão
            tm.sleep(3)

def add(): #Adiciona os links à lista de endereços das músicas
      global songList
      link = etLink.get()
      if ' ' in link: #Caso haja espaços, a string será quebrada em vários links
            y = link.split(' ')
            for i in y:
                  songList.append(i)
      else:
            songList.append(link)
      m = open('pull.json', 'w') #Tudo será salvo no arquivo pull.json
      js.dump(songList, m)
      m.close()

def remove(): #Como o nome já diz, irá remover todos os links do arquivo pull
      global songList
      songList = []
      m = open('pull.json', 'w')
      js.dump(songList, m)
      m.close()

#Parte destinada aos mecanismos gráficos
j = Tk()
j['bg'] = '#222'
j.title('SongDownloader')
font = ('Verdana', 10)
btDown = Button(j, text='Download', command=download, fg = '#f22', width=30, font=font)
btDown.pack()
btLoad = Button(j, text='Carregar', command=load, fg = '#22f', width=30, font=font)
btLoad.pack()
etLink = Entry(j, width=30, font=font, fg='#2f2')
etLink.pack()
btAdd = Button(j, text='Adicionar', command=add, fg = '#22f', width=30, font=font)
btAdd.pack()
btRemove = Button(j, text='Remover Todos', command=remove, fg = '#f22', width=30, font=font)
btRemove.pack()
j.mainloop()
