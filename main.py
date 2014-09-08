import gtk, sys,urllib
import subprocess
global self

class PyApp(gtk.Window):

	global text
	global textbuffer

	def callback(self,widget,data=None):
		
		global textbuffer			
		content=textbuffer.get_text(textbuffer.get_start_iter() , textbuffer.get_end_iter())
		print content
		contents=content.split(' ')
		for word in contents: 
			try:			
				urllib.urlretrieve ("http://translate.google.com/translate_tts?tl=en&q="+word,"speak.mp3")
				print word
				#textbuffer.mark_text(textbuffer.get_start_iter(),textbuffer.get_start_iter()+3)				#urllib.urlretrieve ("http://tts-api.com/tts.mp3?q="+word,"voice.mp3")
				subprocess.call("rhythmbox speak.mp3")

			except Exception, e:
				print " No internet connection" + " " + str(e)	
		sys.exit(1)		
		self.destroy()

	def choose_file(self,widget,data=None):
		
		global textbuffer
		dialog = gtk.FileChooserDialog("Open..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)	
		filter = gtk.FileFilter()
		filter.set_name("PDF files")
		filter.add_pattern("*.pdf")
		dialog.add_filter(filter)
		response = dialog.run()

		if response == gtk.RESPONSE_OK:

			print dialog.get_filename(), 'selected'
			from pyPdf import PdfFileWriter, PdfFileReader
			pdf = PdfFileReader(file("kpeng.pdf", "rb"))
			content=""
			for i in range(0, pdf.getNumPages()):
				# Extract text from page and add to content
				content += pdf.getPage(i).extractText() + "/n"
		   		# Collapse whitespace
		    		content = " ".join(content.replace(u"/xa0", " ").strip().split()) 
			textbuffer.set_text(content);	    		

		elif response == gtk.RESPONSE_CANCEL:
			print 'Closed, no files selected'

		dialog.destroy()
	
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
		textbuffer.set_text("Enter your text here ")
		self.fixed.put(text,100,100)
		
		#sw = gtk.ScrolledWindow()
		#sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
		#sw.add(text)
		#self.fixed.put(sw,100,100)

		Check_button=gtk.Button("Generate Voice")
		Check_button.connect("clicked", self.callback, "cool button")
		Check_button.set_size_request(150, 40)
		self.fixed.put(Check_button, 600, 600)
		
		Check_button=gtk.Button("Choose PDF")
		Check_button.connect("clicked", self.choose_file, "cool button")
		Check_button.set_size_request(150, 40)
		self.fixed.put(Check_button, 600, 700)

		self.connect("destroy", gtk.main_quit)
		self.show_all()

PyApp()
gtk.main()
