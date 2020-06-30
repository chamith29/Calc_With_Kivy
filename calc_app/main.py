import kivy
kivy.require('1.9.1')
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class making(BoxLayout):
    def btn1(self):
        self.lbl.text=self.lbl.text+self.btt1.text
    def btn2(self):
        self.lbl.text=self.lbl.text+self.btt2.text
    def btn3(self):
        self.lbl.text=self.lbl.text+self.btt3.text
    def btn4(self):
        self.lbl.text=self.lbl.text+self.btt4.text
    def btn5(self):
        self.lbl.text=self.lbl.text+self.btt5.text
    def btn6(self):
        self.lbl.text=self.lbl.text+self.btt6.text
    def btn7(self):
        self.lbl.text=self.lbl.text+self.btt7.text
    def btn8(self):
        self.lbl.text=self.lbl.text+self.btt8.text
    def btn9(self):
        self.lbl.text=self.lbl.text+self.btt9.text
    def btn10(self):
        self.lbl.text=self.lbl.text+self.btt10.text
    def btn11(self):
        self.lbl.text=self.lbl.text+self.btt11.text
    def btn12(self):
        self.lbl.text=self.lbl.text+self.btt12.text
    def btn13(self):
        self.lbl.text=''
    def btn14(self):
        self.lbl.text=self.lbl.text+self.btt14.text
    def btn15(self):
        try:
            ans = str(eval(self.lbl.text))
            self.lbl.text = ans
        except:
            self.lbl.text='Error'
    def btn16(self):
        self.lbl.text=self.lbl.text+self.btt16.text


class calcApp(App):
    def build(self):
        return making()
running=calcApp()
running.run()