from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
#import PIL.ImageGrab as ImageGrab

class paint:
	def __init__(self,root):
		self.root = root
		self.root.title("Paint")
		self.root.geometry("800x520")
		self.root.configure(background = 'white')
		self.root.resizable(0,0)
		self.pen_color="black"
		self.eraser_color = "white"
		#adding widgets to tkinter window
		self.color_frame = LabelFrame(self.root,text="Color",font=('arial',15),bd=4,relief=RIDGE,bg="white")
		self.color_frame.place(x = 0,y = 0, width =98, height = 195)
		colors = ['#ff0000', '#00ff00', '#0000ff' , '#ffff00', '#00ffff', '#ff00ff','#ffffff', '#000000', '#99ffcc', '#ff99cc']
		i = j = 0
		for color in colors:
			Button(self.color_frame,bg = color,bd =2, relief=RIDGE,width=2,command = lambda col=color:self.select_color(col)).grid(row = i, column = j)
			i += 1
			if i==5:
				i = 0
				j+=1 
		self.eraser_button = Button(self.root, text = "Eraser",bd = 4,bg="white",command = self.eraser,width = 8,relief=RIDGE)
		self.eraser_button.place(x = 0,y = 207)
		self.clear_button = Button(self.root, text = "Clear",bd = 4,bg="white",command = lambda:self.canvas.delete("all"),width = 8,relief=RIDGE)
		self.clear_button.place(x = 0,y = 247)
		self.canvas_color = Button(self.root, text = "Canvas",bd = 4,bg="white",command = self.canvas,width = 8,relief=RIDGE)
		self.canvas_color.place(x = 0,y = 287)
		
		
		#creating a scale for pen and eraser size..
		
		self.pen_size_scale_frame = LabelFrame(self.root, text="Size", bd=5,bg='white',font=('arial', 15,'bold'),relief=RIDGE)
		self.pen_size = Scale(self.pen_size_scale_frame,orient=VERTICAL,from_=50,to=0,length=170)
		self.pen_size.set(1)
		self.pen_size.grid(row=0,column=1,padx=15)
		
		#creating canvas
		
		self.canvas = Canvas(self.root,bg='white',bd=5,relief=GROOVE, height=488,width=680)
		self.canvas.place(x=105,y=7)
		self.pen_size_scale_frame.place(x=0,y=325,height=190,width=98)
		
		#bind canvas with mouse drag
		self.canvas.bind("<B1-Motion>",self.paint)
		
		#function creation
	def paint(self,event):
		x1,y1 = (event.x-2),(event.y-2)
		x2,y2 = (event.x+2),(event.y+2)
		
		self.canvas.create_oval(x1,y1,x2,y2,fill=self.pen_color,outline=self.pen_color,width=self.pen_size.get())
	def select_color(self,col):
		self.pen_color =col
	
	def eraser(self):
		self.pen_color = self.eraser_color
		
	def canvas(self):
		color = colorchooser.askcolor()
		self.canvas.configure(background = color[1])
		self.eraser_color = color[1]
		
if __name__ =="__main__":
	root = Tk()
	p = paint(root)
	root.mainloop()
	
		
		
