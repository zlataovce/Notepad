from configparser import ConfigParser
from os import startfile, remove
from os.path import exists
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.simpledialog import askstring


class NotepadApp:
    def __init__(self, master=None):
        # build ui
        config = ConfigParser()
        config.read('config.ini')

        def textapp(tkroot):
            nonlocal config
            configuredbackground = config['NOTEPAD']['TextAppBackground']
            configuredforeground = config['NOTEPAD']['TextColor']
            textwindow = tk.Toplevel(tkroot)
            windowframe = tk.Frame(textwindow)
            textframe = tk.Frame(windowframe)
            text_1 = tk.Text(textframe)

            def fontchange(widget):
                confont = askstring("Notepad", "Type the font name.")
                confsize = askstring("Notepad", "Type the font size.")
                finallyfont = '{' + str(confont) + '} ' + str(confsize) + ' {}'
                widget.pack_forget()
                widget.config(font=finallyfont)
                widget.pack()

            font = config['NOTEPAD']['Font']
            fontsize = config['NOTEPAD']['Size']
            windowwidth = config['WINDOW']['Width']
            windowheight = config['WINDOW']['Height']
            geometrystring = str(windowwidth) + "x" + str(windowheight)
            finalfont = '{' + str(font) + '} ' + str(fontsize) + ' {}'
            text_1.config(background=configuredbackground, font=finalfont, foreground=configuredforeground)
            text_1.config(relief='flat', height=int(windowheight) - 5, width=int(windowwidth) - 5)
            text_1.pack(side='top')
            textframe.config(background=configuredbackground, height=int(windowheight) - 5, width=int(windowwidth) - 5,
                             pady='5')
            textframe.pack(side='top')
            textframe.pack_propagate(0)
            windowframe.config(background=configuredbackground, height=int(windowheight) - 5,
                               width=int(windowwidth) - 5)
            windowframe.pack(side='top')
            windowframe.pack_propagate(0)
            textwindow.config(background=configuredbackground, height=int(windowheight) - 5, width=int(windowwidth) - 5)
            textwindow.geometry(geometrystring)
            textwindow.resizable(False, False)
            textwindow.title('Note')

            def saveas(widget):
                filename = asksaveasfilename(defaultextension=".txt",
                                             filetypes=(("Text File (.txt)", "*.txt"), ("All Files", "*.*")))
                if filename == '':
                    return
                texts = widget.get(1.0, "end-1c")
                if exists(filename):
                    remove(filename)

                try:
                    with open(filename, "w") as file:
                        file.write(texts + "\n")
                except FileNotFoundError:
                    return

            def openfile(widget):
                filename = askopenfilename()
                if filename == '':
                    return
                try:
                    with open(filename, "r") as file:
                        texts = file.read()
                except FileNotFoundError:
                    return
                widget.insert(1.0, texts)

            menu_1 = tk.Menu(tkroot)
            menu_1.add('command', command=lambda: openfile(text_1), label='Open')
            menu_1.add('command', command=lambda: saveas(text_1), label='Save as')
            menu_1.add('command', command=lambda: fontchange(text_1), label='Format')
            textwindow.config(menu=menu_1)
            textwindow.mainloop()

        self.mainwindow = tk.Frame(master)
        self.titleframe = tk.Frame(self.mainwindow)
        self.title1 = tk.Label(self.titleframe)
        self.title1.config(background='#24292e', font='{Noto Sans} 20 {}', foreground='white', justify='left')
        self.title1.config(takefocus=False, text='Notepad')
        self.title1.pack(padx='10', side='left')
        self.title2 = tk.Label(self.titleframe)
        self.title2.config(background='#24292e', font='{Noto Sans} 12 {}', foreground='white', justify='left')
        self.title2.config(takefocus=False, text='v0.6.8')
        self.title2.pack(side='left')
        self.titleframe.config(background='#24292e', height='60', width='400')
        self.titleframe.pack(side='top')
        self.titleframe.pack_propagate(0)
        self.spacer1 = tk.Frame(self.mainwindow)
        self.spacer1.config(background='white', height='1', width='370')
        self.spacer1.pack(side='top')
        self.buttonframe = tk.Frame(self.mainwindow)
        self.plusimage = tk.PhotoImage(file="icons\\plus.png")
        self.plusbutton = tk.Button(self.buttonframe, image=self.plusimage,
                                    command=lambda: textapp(master))
        self.plusbutton.config(activebackground='#24292e', anchor='n', background='#24292e', cursor='arrow')
        self.plusbutton.config(relief='flat', takefocus=False)
        self.plusbutton.pack(padx='5', side='right')
        self.githubimage = tk.PhotoImage(file="icons\\github.png")
        self.githubbutton = tk.Button(self.buttonframe, image=self.githubimage, command=lambda: startfile("https"
                                                                                                          "://github"
                                                                                                          ".com"
                                                                                                          "/zlataovce"))
        self.githubbutton.config(activebackground='#24292e', anchor='n', background='#24292e', cursor='arrow')
        self.githubbutton.config(relief='flat', takefocus=False)
        self.githubbutton.pack(padx='5', side='left')
        self.buttonframe.config(background='#24292e', height='35', width='400')
        self.buttonframe.pack(side='bottom')
        self.buttonframe.pack_propagate(0)
        self.title1_1 = tk.Label(self.buttonframe)
        self.title1_1.config(background='#24292e', font='{Noto Sans} 14 {}', foreground='white', justify='left')
        self.title1_1.config(takefocus=False, text='by zlataovce')
        self.title1_1.pack(padx='10', side='left')
        self.mainwindow.config(background='#24292e', height='200', width='400')
        self.mainwindow.pack(side='top')
        self.mainwindow.pack_propagate(0)
        master.resizable(False, False)

        # Main widget
        self.mainwindow = self.mainwindow

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    import tkinter as tk

    root = tk.Tk()
    root.title("Notepad Menu")
    app = NotepadApp(root)
    app.run()
