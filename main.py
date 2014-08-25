import gtk, sys,urllib
import subprocess
global self

class PyApp(gtk.Window):
	global text
	global textbuffer

	def callback(self,widget,data=None):			
		print textbuffer.text
		#urllib.urlretrieve ("http://translate.google.com/translate_tts?tl=en&q="+word,"voice.mp3")
		urllib.urlretrieve ("http://tts-api.com/tts.mp3?q="+word,"voice.mp3")
		subprocess.call("cvlc voice.mp3")		
		self.destroy()

	def __init__(self):
		super(PyApp, self).__init__()
		
		global text
		global textbuffer

		self.set_title("Speak Out")
		self.set_size_request(800, 800)
		self.set_position(gtk.WIN_POS_CENTER)

		self.fixed = gtk.Fixed()
		self.add(self.fixed)
		
		text = gtk.TextView()
		textbuffer = text.get_buffer()
		textbuffer.set_text("Enter your text here")
		self.fixed.put(text,100,100)

		Check_button=gtk.Button("Generate Voice")
		Check_button.connect("clicked", self.callback, "cool button")
		Check_button.set_size_request(150, 40)
		self.fixed.put(Check_button, 600, 600)
		
		self.connect("destroy", gtk.main_quit)
		self.show_all()

PyApp()
gtk.main()
