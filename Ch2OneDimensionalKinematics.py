#Two balls (one red and one blue) move at constant speeds
#across the floor, as viewed from above. The distance 
#grid is in cm, and the times are shown in seconds. Can 
#you determine the speed of each ball? 

import tkinter as tk

class Application(tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master):
		self.grid()
		self.createWidgets()
		
	def createWidgets(self):
	self.quitButton = tk.Button(self, text="Quit",
		command = self.quit)
	self.quitButton.grid()

app = Application()
app.master.title("Sample Application")
app.mainloop()
