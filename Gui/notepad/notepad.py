import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

# create class represet the programm
class Notepad:

    # interpreter to use tkinter with cli , creating tkinter window
	__root = Tk()

	# default window width and height
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(__root) # Text Widget is used where a user wants to insert multiline text fields. -  root window.
	__thisMenuBar = Menu(__root) # Toplevel menus are displayed just under the title bar of the root or any other toplevel windows.  various operations such as saving or opening a file
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0) # Adding File Menu and commands - master - options
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0) # Adding Edit Menu and commands - master - options
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0) # Adding Help Menu and commands - master - options
	
	# To add scrollbar
	__thisScrollBar = Scrollbar(__thisTextArea)	
	__file = None

    # constructor - with self , keys for arguments given
	def __init__(self,**kwargs):

		# Set icon
		try:
				self.__root.wm_iconbitmap("Notepad.ico")
		except:
				pass

		# Set window size (the default is 300x300)
		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			pass

		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			pass

		# Set the window text
		self.__root.title("Untitled - Notepad")

		# Center the window
		screenWidth = self.__root.winfo_screenwidth()
		screenHeight = self.__root.winfo_screenheight()
	
		# For left-align - where the window shown
		left = (screenWidth / 2) - (self.__thisWidth / 2)
		
		# For right-align
		top = (screenHeight / 2) - (self.__thisHeight /2)
		
		# For top and bottom - the geometry() method. This method is used to set the dimensions of the Tkinter window and is used to set the position of the main window on the user’s desktop.
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
											self.__thisHeight,
											left, top))

		# To make the textarea auto resizable - a non-zero weight causes a row or column to grow if there's extra space. The default is a weight of zero, which means the column will not grow if there's extra space
		self.__root.grid_rowconfigure(0, weight=1)
		self.__root.grid_columnconfigure(0, weight=1)

		# Add controls (widget)
		self.__thisTextArea.grid(sticky = N + E + S + W)
		
		# To open new file
		self.__thisFileMenu.add_command(label="New",
										command=self.__newFile)
		
		# To open a already existing file
		self.__thisFileMenu.add_command(label="Open",
										command=self.__openFile)
		
		# To save current file
		self.__thisFileMenu.add_command(label="Save",
										command=self.__saveFile)

		# To create a line in the dialog	
		self.__thisFileMenu.add_separator()										
		self.__thisFileMenu.add_command(label="Exit",
										command=self.__quitApplication)
		self.__thisMenuBar.add_cascade(label="File",
									menu=self.__thisFileMenu)	
		
  
  
		# To give a feature of cut
		self.__thisEditMenu.add_command(label="Cut",
										command=self.__cut)			
	
		# to give a feature of copy
		self.__thisEditMenu.add_command(label="Copy",
										command=self.__copy)		
		
		# To give a feature of paste
		self.__thisEditMenu.add_command(label="Paste",
										command=self.__paste)		
		
		# To give a feature of editing
		self.__thisMenuBar.add_cascade(label="Edit",
									menu=self.__thisEditMenu)	
		
  
  
		# To create a feature of description of the notepad
		self.__thisHelpMenu.add_command(label="About Notepad",
										command=self.__showAbout)
		self.__thisMenuBar.add_cascade(label="Help",
									menu=self.__thisHelpMenu)
  
  

		self.__root.config(menu=self.__thisMenuBar)
        # this will set the scroll bar to right and Y-axis -> veriscal
		self.__thisScrollBar.pack(side=RIGHT,fill=Y)				
		
		# Scrollbar will adjust automatically according to the content	
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
	
		
	def __quitApplication(self):
		self.__root.destroy() 

	def __showAbout(self):
		showinfo("Notepad","Created by ishiekh")

	def __openFile(self):
     
		self.__file = askopenfilename(defaultextension=".txt",
									filetypes=[("All Files","*.*"),
										("Text Documents","*.txt")])

		if self.__file == "":

			# no file to open
			self.__file = None
		else:
			
			# Try to open the file
			# set the window title
			self.__root.title(os.path.basename(self.__file) + " - Notepad")
			self.__thisTextArea.delete(1.0,END) # empty the prev content
            # open that file - read it
			file = open(self.__file,"r")
            # insert the data of that file into the textarea
			self.__thisTextArea.insert(1.0,file.read())
        
			file.close()

		
	def __newFile(self):
		self.__root.title("Untitled - Notepad")
		self.__file = None
		self.__thisTextArea.delete(1.0,END)

	def __saveFile(self):

		if self.__file == None:
			# Save as new file
			self.__file = asksaveasfilename(initialfile='Untitled.txt',
											defaultextension=".txt",
											filetypes=[("All Files","*.*"),
												("Text Documents","*.txt")])

			if self.__file == "":
				self.__file = None
			else:
				
				# Try to save the file
				file = open(self.__file,"w")
				file.write(self.__thisTextArea.get(1.0,END))
				file.close()
				
				# Change the window title
				self.__root.title(os.path.basename(self.__file) + " - Notepad")
				
			
		else:
			file = open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()

	def __cut(self):
		self.__thisTextArea.event_generate("<<Cut>>")

	def __copy(self):
		self.__thisTextArea.event_generate("<<Copy>>")

	def __paste(self):
		self.__thisTextArea.event_generate("<<Paste>>")

	def run(self):

		# Run main application
		self.__root.mainloop()




# Run main application
notepad = Notepad(width=600,height=400)
notepad.run()
