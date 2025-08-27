import tkinter as tk


janela = tk.Tk()
janela.title('Bem-vindo ao Quiz de python!')
janela.geometry('700x600')


titulo = tk.Label(janela, text ='PyQuiz', font=('Bungee', 35, 'bold'), fg='darkblue')
titulo.pack()
titulo.place(x=265,y=30)

botao1 = tk.Button(janela, text = 'INICIAR QUIZ', width=13, height=2,font=('Bungee',20,'bold'),bg='darkblue',fg='yellow')
botao1.pack()
botao1.place(x=230, y=140)

botao2 = tk.Button(janela,text ='Nível Fácil',width=15,height=2,font=('Bungee', 15, 'bold'), bg='darkgreen', fg='white')
botao2.pack()
botao2.place(x=250, y=260)

botao3 = tk.Button(janela, text = 'Nível Médio', width=15, height=2,font=('Bungee', 15, 'bold'), bg='darkorange', fg='white')
botao3.pack()
botao3.place(x=250, y=350)

botao4 = tk.Button(janela, text = 'Nível Difícil',bg= 'red', fg='white', width=15,height=2,font=('Bungee', 15, 'bold'))
botao4.pack()
botao4.place(x=250, y=440)

janela.mainloop()