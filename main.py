"""Write
a program that choose a random website name from list and open it in your browser"""
import random
import webbrowser

web_list = ['www.google.com', 'www.youtube.com', 'www.canva.com']

val = random.randrange(0, len(web_list))

webbrowser.register('edge',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
webbrowser.get('edge').open(web_list[int(val)])


