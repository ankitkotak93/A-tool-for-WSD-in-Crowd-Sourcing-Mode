#!/usr/bin/env python

import pygtk
pygtk.require("2.0")
import gtk
import MySQLdb
user = ''
#user has the current user's name
host = 'localhost'
db_user = 'root' # mysql username
password = '' # my-sql password
database = 'WSD'
connection = MySQLdb.connect(host,db_user,password,database)
a_conn = connection.cursor()
#database informaion 
class Login():
	def destroy(self,widget,data=None):
		gtk.main_quit()
	def login(self,widget):
		global host,db_user,password,database
		a_conn.execute("select * from auth_user where email='"+self.combo.get_active_text()+"' && password='"+self.combo1.get_active_text()+"'") 
		login = a_conn.fetchall()
		if login:
			global user 
			user  = self.combo.get_active_text()
			base = Base()
			base.main()
			gtk.main_quit()
		else:
			self.label4.set_text('Invalid Login')
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(600, 200)
		self.window.connect("destroy",self.destroy)
		self.window.set_title("WSD TOOL")
		self.label1 = gtk.Label("WSD TOOL")
		self.label2 = gtk.Label("User Name:")
		self.label3 = gtk.Label("Key:")
		self.label4 = gtk.Label(" ")
		self.combo = gtk.combo_box_entry_new_text()
		self.combo1 = gtk.combo_box_entry_new_text()
	 	self.button1 = gtk.Button("Quit")
	 	self.button2 = gtk.Button("Next")
		self.button1.connect("clicked",self.destroy)
		self.button2.connect("clicked",self.login)
		self.box1 = gtk.VBox()
		self.box2 = gtk.HBox()
		self.box2.pack_start(self.button2)
		self.box2.pack_start(self.button1)
		self.box1.pack_start(self.label1)
		self.box1.pack_start(self.label4)
		self.box1.pack_start(self.label2)
		self.box1.pack_start(self.combo)
		self.box1.pack_start(self.label3)
		self.box1.pack_start(self.combo1)
		self.box1.pack_start(self.box2)
		self.window.add(self.box1)
		self.window.show_all()
	def main(self):
		gtk.main()
class Base():
	def destroy(self,widget,data=None):
		gtk.main_quit()
	def screen2(self,widget):
		a = self.combo.get_active_text()
		gtk.main_quit()
		base1 = Base1(a)
		base1.main(a)
	def __init__(self):
		f = open("words.txt","r")
		r = f.read()
		r = r.split()
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(600, 200)
		self.window.connect("destroy",self.destroy)
		self.window.set_title("WSD TOOL")
		self.label1 = gtk.Label("WSD TOOL")
		self.label2 = gtk.Label("Write your word or select from the dropdown:")
		self.combo = gtk.combo_box_entry_new_text()
		a_conn.execute("select word from words")
		r = a_conn.fetchall()
		for i in r:
				for j in i:
					self.combo.append_text(j)
	 	self.button1 = gtk.Button("Quit")
	 	self.button2 = gtk.Button("Next")
		self.button2.connect("clicked",self.screen2)
		self.button1.connect("clicked",self.destroy)
		self.box1 = gtk.VBox()
		self.box2 = gtk.HBox()
		self.box2.pack_start(self.button2)
		self.box2.pack_start(self.button1)
		self.box1.pack_start(self.label1)
		self.box1.pack_start(self.label2)
		self.box1.pack_start(self.combo)
		self.box1.pack_start(self.box2)
		self.window.add(self.box1)
		self.window.show_all()
		f.close()
	def main(self):
		gtk.main()

class Base1():
	def destroy(self,widget,data=None):
		gtk.main_quit()
	def screen3(self,widget):
		gtk.main_quit()
		base2 = Base2(self.a,self.combo.get_active_text())
		base2.main(self.a,self.combo.get_active_text(),self.textbox2.get_text())
	def __init__(self,a):
		self.a =a
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy",self.destroy)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(600,200)
		self.window.set_title("WSD TOOL")
		self.label0 = gtk.Label("WSD TOOL")
		self.label1 = gtk.Label("Write your own english sentence or select a English Sentence by the drop down:")
		self.combo = gtk.combo_box_entry_new_text()
		a_conn.execute("select sentences.esentence from sentences,words where words.word='"+self.a+"' and sentences.id=(select links.sid from links where links.wid=words.id)")
		word_selected = a_conn.fetchall()
		for i in word_selected:
				for j in i:
						self.combo.append_text(j)
		self.label2 = gtk.Label("Enter the Hindi Sentence:")
		self.textbox2 = gtk.Entry()
		self.button2 = gtk.Button("Next")
		self.button3 = gtk.Button("Exit")
		self.button3.connect("clicked",self.destroy)
		self.button2.connect("clicked",self.screen3)
		self.box1 = gtk.VBox()
		self.box2 = gtk.HBox()
		self.box3 = gtk.VBox()
		self.box1.pack_start(self.label0)
		self.box1.pack_start(self.label1)
		self.box1.pack_start(self.combo)
		self.box1.pack_start(self.label2)
		self.box1.pack_start(self.textbox2)
		self.box2.pack_start(self.button2)
		self.box2.pack_start(self.button3)
		self.box3.pack_start(self.box1)
		self.box3.pack_start(self.box2)
		self.window.add(self.box3)
		self.window.show_all()
	def main(self,a):
		self.a = a
		gtk.main()
class Base2():
	def destroy(self,widget,data=None):
		gtk.main_quit()
	def next1(self,widget):
		base3 = Base3(self.a,self.b)
		base3.main(self.a,self.b,self.c,self.combo.get_text())
		gtk.main_quit()
	def done(self,widget):
		#store to database
		#self of a,b,c and self.combo.get_active_text()
		gtk.main_quit()
	def __init__(self,a,b):
		self.a = a
		self.b = b
		#put the parts of speech in array r
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy",self.destroy)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(600,300)
		self.window.set_title("WSD TOOL")
		self.label = gtk.Label("WSD TOOL")
		self.label1 = gtk.Label("The parts of speech")
		self.label3 = gtk.Label("Click done if this information is enough.")
		self.combo = gtk.Label()
		a_conn.execute("select links.typ from links where links.wid = (select words.id from words where word='"+self.a+"') and links.sid=(select sentences.id from sentences where sentences.esentence='"+self.b+"')")
		pos = a_conn.fetchall()
		for i in pos:
				for j in i:
					self.combo.set_text(j)
		self.button = gtk.Button('Quit')
		self.button.connect("clicked",self.destroy)
		self.button1 = gtk.Button('Next')
		self.button1.connect('clicked',self.next1)
		self.button2 = gtk.Button('Done')
		self.button2.connect("clicked",self.done)
		self.box1 = gtk.HBox()
		self.box2 = gtk.VBox()
		self.box2.pack_start(self.label)
		self.box2.pack_start(self.label1)
		self.box2.pack_start(self.combo)
		self.box2.pack_start(self.label3)
		self.box1.pack_start(self.button2)
		self.box1.pack_start(self.button1)
		self.box1.pack_start(self.button)
		self.box2.pack_start(self.box1)
		self.window.add(self.box2)
		self.window.show_all()
	def main(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
		gtk.main()

class Base3():
	def destroy(self,widget,data=None):
		gtk.main_quit()
	def next1(self,widget):
		base4 = Base4()
		base4.main(self.a,self.b,self.c,self.d,self.combo.get_active_text())
		gtk.main_quit()
	def done(self,widget):
		#store to database
		#self of a,b,c,dand self.combo.get_active_text()
		gtk.main_quit()
	def __init__(self,a,b):
		#put the relations in array r
		self.a =a
		self.b = b
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy",self.destroy)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(600,300)
		self.window.set_title("WSD TOOL")
		self.label = gtk.Label("WSD TOOL")
		self.label1 = gtk.Label("Enter the responsible relations")
		self.label3 = gtk.Label("Click done if this information is enough.")
		self.combo = gtk.combo_box_entry_new_text()
		a_conn.execute("select rel_all.relation from rel_all where wid=(select words.id from words where word='"+self.a+"') and sid=(select sentences.id from sentences where esentence='"+self.b+"')")
		relation = a_conn.fetchall()
		for r in relation:
			for i in r:
				self.combo.append_text(i)
		self.button = gtk.Button('Quit')
		self.button.connect("clicked",self.destroy)
		self.button1 = gtk.Button('Next')
		self.button1.connect('clicked',self.next1)
		self.button2 = gtk.Button('Done')
		self.button2.connect("clicked",self.done)
		self.box1 = gtk.HBox()
		self.box2 = gtk.VBox()
		self.box2.pack_start(self.label)
		self.box2.pack_start(self.label1)
		self.box2.pack_start(self.combo)
		self.box2.pack_start(self.label3)
		self.box1.pack_start(self.button2)
		self.box1.pack_start(self.button1)
		self.box1.pack_start(self.button)
		self.box2.pack_start(self.box1)
		self.window.add(self.box2)
		self.window.show_all()
	def main(self,a,b,c,d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		gtk.main()

class Base4():
	def destroy(self,widget,data=None):
		gtk.main_quit()
	def done(self,widget):
		#store to database
		#self of a,b,c,d,e and self.combo.get_active_text()
		gtk.main_quit()
	def __init__(self):
		#put the sementics in array r
		r = ['Animate','Inanimate','Human','Place','Time']
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy",self.destroy)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(600,300)
		self.window.set_title("WSD TOOL")
		self.label = gtk.Label("WSD TOOL")
		self.label1 = gtk.Label("Enter the additional information:")
		self.combo = gtk.combo_box_entry_new_text()
		for i in r:
			self.combo.append_text(i)
		self.button = gtk.Button('Quit')
		self.button.connect("clicked",self.destroy)
		self.button2 = gtk.Button('Done')
		self.button2.connect("clicked",self.done)
		self.box1 = gtk.HBox()
		self.box2 = gtk.VBox()
		self.box2.pack_start(self.label)
		self.box2.pack_start(self.label1)
		self.box2.pack_start(self.combo)
		self.box1.pack_start(self.button2)
		self.box1.pack_start(self.button)
		self.box2.pack_start(self.box1)
		self.window.add(self.box2)
		self.window.show_all()
	def main(self,a,b,c,d,e):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.e = e
		gtk.main()


if __name__ == "__main__":
	base = Login()
	base.main()
