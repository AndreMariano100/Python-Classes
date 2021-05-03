# -*-coding:utf-8 -*
# You must install tkfontchooser package before use it :
# pip install tkfontchooser

import tkinter
import tkfontchooser
import tkinter.font
import tkinter.ttk


class FontChooser(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.frame = tkinter.ttk.Frame(self)
        self.frame.pack(fill=tkinter.BOTH, expand=1)

        self.button = tkinter.ttk.Button(self.frame, command=self.OnButtonClick, text='Font...')
        self.button.place(x=10, y=10)

        self.label = tkinter.ttk.Label(self.frame,
                                       text="The quick brown fox jumps over the lazy dog.\n"
                                            "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.\n"
                                            "0123456789+-*/%~^&|=<>≤≥±÷≠{{[()]}},;:.?¿!¡\n"
                                            "àçéèêëïî@@°_#§$ù£€æœøπµ©®∞\\\"'\n"
                                            "ЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏ\n"
                                            "АБВГДЕЖЗИЙКЛМНОП\n"
                                            "亠亡亢亣交亥亦产亨亩亪享京亭亮亯\n"
                                            "亰亱亲亳亴亵亶亷亸亹人亻亼亽亾亿\n"
                                            "🐨")
        self.label.place(x=10, y=40)
        self.geometry('400x400+200+100')
        self.title('Font Chooser')

    def main(self=None):
        form = FontChooser()
        form.mainloop()

    def OnButtonClick(self):
        font = tkfontchooser.askfont()
        if font:
            font['family'] = font['family'].replace(' ', '\ ')
            fontStr = '%(family)s %(size)i %(weight)s %(slant)s' % font
            if font['underline']:
                fontStr += ' underline'
            if font['overstrike']:
                fontStr += ' overstrike'
            self.label['font'] = fontStr


if __name__ == '__main__':
    FontChooser.main()
