import tkinter as tk
import matplotlib.pyplot as plt
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pygame

selectlanguage = tk.Tk()
selectlanguage.geometry("800x480") 
selectlanguage.resizable(False, False)
selectlanguage.title("selectlanguage")

selectlanguagebg_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\SELECTLANGUAGE.png")
selectlanguagebg_label = tk.Label(selectlanguage, image=selectlanguagebg_image)
selectlanguagebg_label.place(x=0, y=0, relwidth=1, relheight=1)

def open_english():
 selectlanguage.destroy()
 show_selectmode()

def open_telugu():
 selectlanguage.destroy()
 show_selectmode()

def open_hindi():
 selectlanguage.destroy()
 show_selectmode()

selectlanguagebutton = tk.Button(selectlanguage, text="తెలుగు", font=("Comic Sans MS Bold", 24), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_telugu)
selectlanguagebutton.place(x=296, y=178, relwidth=0.28, relheight=0.085)

selectlanguagebutton = tk.Button(selectlanguage, text="हिंदी", font=("Comic Sans MS Bold", 24), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_hindi)
selectlanguagebutton.place(x=296, y=268, relwidth=0.28, relheight=0.085)

selectlanguagebutton = tk.Button(selectlanguage, text="ENGLISH", font=("Comic Sans MS Bold", 24), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_english)
selectlanguagebutton.place(x=296, y=358, relwidth=0.28, relheight=0.085)

def show_selectmode():
 selectmode = tk.Toplevel()
 selectmode.geometry("800x480") 
 selectmode.resizable(False, False)
 selectmode.title("selectmode")

 selectmodebg_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\SELECTMODE.png")
 selectmodebg_label = tk.Label(selectmode, image=selectmodebg_image)
 selectmodebg_label.place(x=0, y=0, relwidth=1, relheight=1)

 def open_kidshome():
  selectmode.destroy()
  show_home()

 def open_adultshome():
  selectmode.destroy()
  showadult_homeadults()

 selectmodebutton = tk.Button(selectmode, text="FOR ADULTS", font=("Comic Sans MS Bold", 18), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_adultshome)
 selectmodebutton.place(x=160, y=357, relwidth=0.22, relheight=0.06)

 selectmodebutton = tk.Button(selectmode, text="FOR KIDS", font=("Comic Sans MS Bold", 18), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_kidshome)
 selectmodebutton.place(x=470, y=357, relwidth=0.22, relheight=0.06)

 # Home page
 def show_home(): 
  home = tk.Toplevel()
  home.geometry("800x480") 
  home.resizable(False, False)
  home.title("HOME")

  homebg_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\1intro.png")
  homebg_label = tk.Label(home, image=homebg_image)
  homebg_label.place(x=0, y=0, relwidth=1, relheight=1)

  def open_instruction():
    home.destroy()
    show_instruction()

  homebutton = tk.Button(home, text="START TEST", font=("Comic Sans MS Bold", 16), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_instruction)
  homebutton.place(x=339, y=369, relwidth=0.194, relheight=0.056)

  def show_instruction():
   instruction_window = tk.Toplevel()
   instruction_window.geometry("800x480")
   instruction_window.resizable(False, False)
   instruction_window.title("instruction")
    
   instruction_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\2instruct.png")
   instruction_label = tk.Label(instruction_window, image=instruction_img)
   instruction_label.place(x=0, y=0, relwidth=1, relheight=1)
    
   pygame.mixer.init()

   def open_login():
     instruction_window.destroy()
     show_login()
    
   instruction_button = tk.Button(instruction_window, text="CONTINUE", font=("Comic Sans MS Bold", 16), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command= open_login)
   instruction_button.place(x=315, y=407, relwidth=0.192, relheight=0.056)
   instruction_window.mainloop()

 #login page
  def show_login():
   login = tk.Toplevel()
   login.title("login")
   login.geometry("800x480")
   login.resizable(False, False)
   login.title("instruction")

   bg_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\login.png")
   background_label = tk.Label(login, image=bg_image)
   background_label.place(relwidth=1, relheight=1)

   def update_entry(char):
        current_entry = login.focus_get()
        if isinstance(current_entry, tk.Entry):
            current_entry.insert(tk.END, char)

   def clear_entry():
        current_entry = login.focus_get()
        if isinstance(current_entry, tk.Entry):
            current_entry.delete(0, tk.END)
  
   def open_logintopure():
    global name
    name= name_entry.get()
    global age
    age= age_entry.get()
    global gender
    gender= gender_entry.get()
    pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_0_R.ogg")
    pygame.mixer.music.play()
    login.destroy()
    show_r250_0_page()
   
   global name_entry
   name_entry = tk.Entry(login, font=("Comic Sans MS Bold", 13), fg="#BF56CB",highlightthickness=0,bd=0)
   name_entry.place(x=365, y=91, relwidth=0.2, relheight=0.051)
   
   global age_entry
   age_entry = tk.Entry(login, font=("Comic Sans MS Bold", 13), fg="#BF56CB",highlightthickness=0,bd=0)
   age_entry.place(x=365, y=147, relwidth=0.2, relheight=0.051)

   global gender_entry
   gender_entry = tk.Entry(login, font=("Comic Sans MS Bold", 13), fg="#BF56CB",highlightthickness=0,bd=0)
   gender_entry.place(x=365, y=202, relwidth=0.2, relheight=0.051)

   submit_button = tk.Button(login, text="SUBMIT", font=("Comic Sans MS Bold", 16), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0,command=open_logintopure)
   submit_button.place(x=355, y=257, relwidth=0.128, relheight=0.051)

   keyboard_frame = tk.Frame(login)
   keyboard_frame.place(x=190, y=310)

   characters = [
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),
        ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'),
        ('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L','Z'),
        ('X', 'C', 'V', 'B', 'N', 'M','.',',',':'),
    ]

   for row, chars in enumerate(characters):
        for col, char in enumerate(chars):
            tk.Button(keyboard_frame, text=char, font=("Comic Sans MS Bold", 12), width=3, bg="#F15395", fg="white",activebackground="#F15395",activeforeground="white",command=lambda c=char: update_entry(c)).grid(row=row, column=col)

   tk.Button(keyboard_frame, text="Clc", font=("Comic Sans MS Bold", 12), width=3, bg="#F15395", fg="white",activebackground="#F15395",activeforeground="white", command=clear_entry).grid(row=3,column=9)
   login.mainloop()

  # R250_0 page 
  def show_r250_0_page():
   r250_0_window = tk.Toplevel()
   r250_0_window.geometry("800x480")
   r250_0_window.resizable(False, False)
   r250_0_window.title("R250_0")

   def blank1_page():
     r250_0_window.destroy() 
     show_blank1_page()
      
   pygame.mixer.init()

   def play_r250_10():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_10_R.ogg")
     pygame.mixer.music.play()
     r250_0_window.destroy()
     show_r250_10_page()

   r250_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
   r250_0_label = tk.Label(r250_0_window, image=r250_0_img)
   r250_0_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_0_YES_button = tk.Button(r250_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank1_page)
   r250_0_NO_button  = tk.Button(r250_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r250_10)

   r250_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_0_window.mainloop()

  # blank 1
  def show_blank1_page():
   blank1_window = tk.Toplevel()
   blank1_window.geometry("800x480")
   blank1_window.resizable(False, False)
   blank1_window.title("BLANK1")

   def warning1_page():
     blank1_window.destroy() 
     show_warning1_page()

   pygame.mixer.init()

   A = None

   def play_blank1tor500_0():
     global A
     A = 0
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     blank1_window.destroy()
     show_r500_0_page()
     
   blank1_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
   blank1_label = tk.Label(blank1_window , image=blank1_img)
   blank1_label.place(x=0, y=0, relwidth=1, relheight=1)

   blank1_YES_button = tk.Button(blank1_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning1_page)
   blank1_NO_button= tk.Button(blank1_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank1tor500_0)

   blank1_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   blank1_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)
  
   blank1_window.mainloop()

  # warning 1
  def show_warning1_page():
    warning1_window = tk.Toplevel()
    warning1_window.geometry("800x480")
    warning1_window.resizable(False, False)
    warning1_window.title("WARNING1")
      
    warning1_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
    warning1_label = tk.Label(warning1_window, image=warning1_image)
    warning1_label.place(x=0, y=0, relwidth=1, relheight=1)

    pygame.mixer.init()

    def open_warning1tor250_0():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_0_R.ogg")
     pygame.mixer.music.play()
     warning1_window.destroy()
     show_r250_0_page()

    warning1_button = tk.Button(warning1_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning1tor250_0)
    warning1_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
    warning1_window.mainloop()

  # R250_10 page
  def show_r250_10_page():
   r250_10_window = tk.Toplevel()
   r250_10_window.geometry("800x480")
   r250_10_window.resizable(False, False)
   r250_10_window.title("R250_10")

   pygame.mixer.init()

   def play_r250_10tor250_20():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_20_R.ogg")
     pygame.mixer.music.play()
     r250_10_window.destroy()
     show_r250_20_page()

   pygame.mixer.init()

   def open__r250_10tor500_0():
     global A
     A = 1
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_10_window.destroy()
     show_r500_0_page()

   r250_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
   r250_10_label = tk.Label(r250_10_window, image=r250_10_img)
   r250_10_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_10_YES_button = tk.Button(r250_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r250_10tor500_0)
   r250_10_NO_button  = tk.Button(r250_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r250_10tor250_20)

   r250_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_10_window.mainloop()

  # R250_20 page
  def show_r250_20_page():
   r250_20_window = tk.Toplevel()
   r250_20_window.geometry("800x480")
   r250_20_window.resizable(False, False)
   r250_20_window.title("R250_20")

   pygame.mixer.init()

   def play_r250_20tor250_30():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_30_R.ogg")
     pygame.mixer.music.play()
     r250_20_window.destroy()
     show_r250_30_page()

   pygame.mixer.init()

   def open__r250_20tor500_0():
     global A
     A = 2
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_20_window.destroy()
     show_r500_0_page()

   r250_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
   r250_20_label = tk.Label(r250_20_window, image=r250_20_img)
   r250_20_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_20_YES_button = tk.Button(r250_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r250_20tor500_0)
   r250_20_NO_button  = tk.Button(r250_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r250_20tor250_30)

   r250_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_20_window.mainloop()

  # R250_30 page
  def show_r250_30_page():
   r250_30_window = tk.Toplevel()
   r250_30_window.geometry("800x480")
   r250_30_window.resizable(False, False)
   r250_30_window.title("R250_30")

   pygame.mixer.init()

   def play_r250_30tor250_40():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_40_R.ogg")
     pygame.mixer.music.play()
     r250_30_window.destroy()
     show_r250_40_page()

   pygame.mixer.init()

   def open__r250_30tor500_0():
     global A
     A = 3
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_30_window.destroy()
     show_r500_0_page()

   r250_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
   r250_30_label = tk.Label(r250_30_window, image=r250_30_img)
   r250_30_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_30_YES_button = tk.Button(r250_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r250_30tor500_0)
   r250_30_NO_button  = tk.Button(r250_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r250_30tor250_40)

   r250_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_30_window.mainloop()

  # R250_40 page
  def show_r250_40_page():
   r250_40_window = tk.Toplevel()
   r250_40_window.geometry("800x480")
   r250_40_window.resizable(False, False)
   r250_40_window.title("R250_40")

   pygame.mixer.init()

   def play_r250_40tor250_50():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_50_R.ogg")
     pygame.mixer.music.play()
     r250_40_window.destroy()
     show_r250_50_page()

   pygame.mixer.init()

   def open__r250_40tor500_0():
     global A
     A = 4
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_40_window.destroy()
     show_r500_0_page()

   r250_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
   r250_40_label = tk.Label(r250_40_window, image=r250_40_img)
   r250_40_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_40_YES_button = tk.Button(r250_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r250_40tor500_0)
   r250_40_NO_button  = tk.Button(r250_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r250_40tor250_50)

   r250_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_40_window.mainloop()

  # R250_50 page
  def show_r250_50_page():
   r250_50_window = tk.Toplevel()
   r250_50_window.geometry("800x480")
   r250_50_window.resizable(False, False)
   r250_50_window.title("R250_50")

   pygame.mixer.init()

   def play_r250_50tor250_60():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_60_R.ogg")
     pygame.mixer.music.play()
     r250_50_window.destroy()
     show_r250_60_page()

   pygame.mixer.init()

   def open__r250_50tor500_0():
     global A
     A = 5
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_50_window.destroy()
     show_r500_0_page()

   r250_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
   r250_50_label = tk.Label(r250_50_window, image=r250_50_img)
   r250_50_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_50_YES_button = tk.Button(r250_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r250_50tor500_0)
   r250_50_NO_button  = tk.Button(r250_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r250_50tor250_60)

   r250_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_50_window.mainloop()

  # R250_60 page
  def show_r250_60_page():
    r250_60_window = tk.Toplevel()
    r250_60_window.geometry("800x480")
    r250_60_window.resizable(False, False)
    r250_60_window.title("R250_60")

    pygame.mixer.init()

    def play_r250_60tor250_70():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_70_R.ogg")
       pygame.mixer.music.play()
       r250_60_window.destroy()
       show_r250_70_page()

    pygame.mixer.init()

    def open__r250_60tor500_0():
       global A
       A = 6
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
       pygame.mixer.music.play()
       r250_60_window.destroy()
       show_r500_0_page()

    r250_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
    r250_60_label = tk.Label(r250_60_window, image=r250_60_img)
    r250_60_label.place(x=0, y=0, relwidth=1, relheight=1)

    r250_60_YES_button = tk.Button(r250_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r250_60tor500_0)
    r250_60_NO_button  = tk.Button(r250_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r250_60tor250_70)

    r250_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
    r250_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

    r250_60_window.mainloop() 

  # R250_70 page
  def show_r250_70_page():
     r250_70_window = tk.Toplevel()
     r250_70_window.geometry("800x480")
     r250_70_window.resizable(False, False)
     r250_70_window.title("R250_70")

     pygame.mixer.init()

     def play_r250_70tor250_80():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_80_R.ogg")
       pygame.mixer.music.play()
       r250_70_window.destroy()
       show_r250_80_page()

     pygame.mixer.init()

     def open__r250_70tor500_0():
       global A
       A = 7
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
       pygame.mixer.music.play()
       r250_70_window.destroy()
       show_r500_0_page()

     r250_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r250_70_label = tk.Label(r250_70_window, image=r250_70_img)
     r250_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r250_70_YES_button = tk.Button(r250_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r250_70tor500_0)
     r250_70_NO_button  = tk.Button(r250_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r250_70tor250_80)

     r250_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r250_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r250_70_window.mainloop() 

  # R250_80 page
  def show_r250_80_page():
     r250_80_window = tk.Toplevel()
     r250_80_window.geometry("800x480")
     r250_80_window.resizable(False, False)
     r250_80_window.title("R250_80")

     pygame.mixer.init()

     def play_r250_80tor500_0():
       global A
       A = 9
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
       pygame.mixer.music.play()
       r250_80_window.destroy()
       show_r500_0_page()

     pygame.mixer.init()

     def open__r250_80tor500_00():
       global A
       A = 8
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
       pygame.mixer.music.play()
       r250_80_window.destroy()
       show_r500_0_page()

     r250_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r250_80_label = tk.Label(r250_80_window, image=r250_80_img)
     r250_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r250_80_YES_button = tk.Button(r250_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r250_80tor500_00)
     r250_80_NO_button  = tk.Button(r250_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r250_80tor500_0)

     r250_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r250_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r250_80_window.mainloop()

  # R500_0 page
  def show_r500_0_page():
     r500_0_window = tk.Toplevel()
     r500_0_window.geometry("800x480")
     r500_0_window.resizable(False, False)
     r500_0_window.title("R500_0")

     def blank2_page():
       r500_0_window.destroy() 
       show_blank2_page()
      
     pygame.mixer.init()

     def play_r500_10():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_10_R.ogg")
       pygame.mixer.music.play()
       r500_0_window.destroy()
       show_r500_10_page()

     r500_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r500_0_label = tk.Label(r500_0_window, image=r500_0_img)
     r500_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_0_YES_button = tk.Button(r500_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank2_page)
     r500_0_NO_button  = tk.Button(r500_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r500_10)

     r500_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_0_window.mainloop()

  # blank 2
  def show_blank2_page():
     blank2_window = tk.Toplevel()
     blank2_window.geometry("800x480")
     blank2_window.resizable(False, False)
     blank2_window.title("blank2")

     def warning2_page():
       blank2_window.destroy() 
       show_warning2_page()

     pygame.mixer.init()
     B= None

     def play_blank2tor1000_0():
       global B
       B = 0  
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       blank2_window.destroy()
       show_r1000_0_page()
     
     blank2_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank2_label = tk.Label(blank2_window , image=blank2_img)
     blank2_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank2_YES_button = tk.Button(blank2_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning2_page)
     blank2_NO_button= tk.Button(blank2_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank2tor1000_0)

     blank2_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank2_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank2_window.mainloop()

  # warning2
  def show_warning2_page():
      warning2_window = tk.Toplevel()
      warning2_window.geometry("800x480")
      warning2_window.resizable(False, False)
      warning2_window.title("warning2")
      
      warning2_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning2_label = tk.Label(warning2_window, image=warning2_image)
      warning2_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning2tor500_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
        pygame.mixer.music.play()
        warning2_window.destroy()
        show_r250_0_page()

      warning2_button = tk.Button(warning2_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning2tor500_0)
      warning2_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning2_window.mainloop()

  # R500_10 page
  def show_r500_10_page():
     r500_10_window = tk.Toplevel()
     r500_10_window.geometry("800x480")
     r500_10_window.resizable(False, False)
     r500_10_window.title("R500_10")

     pygame.mixer.init()

     def play_r500_10tor500_20():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_20_R.ogg")
       pygame.mixer.music.play()
       r500_10_window.destroy()
       show_r500_20_page()

     pygame.mixer.init()

     def open__r500_10tor1000_0():
       global B
       B = 1
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_10_window.destroy()
       show_r1000_0_page()

     r500_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r500_10_label = tk.Label(r500_10_window, image=r500_10_img)
     r500_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_10_YES_button = tk.Button(r500_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r500_10tor1000_0)
     r500_10_NO_button  = tk.Button(r500_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r500_10tor500_20)

     r500_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_10_window.mainloop()

# R500_20 page
  def show_r500_20_page():
     r500_20_window = tk.Toplevel()
     r500_20_window.geometry("800x480")
     r500_20_window.resizable(False, False)
     r500_20_window.title("R500_20")

     pygame.mixer.init()

     def play_r500_20tor500_30():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_30_R.ogg")
       pygame.mixer.music.play()
       r500_20_window.destroy()
       show_r500_30_page()

     pygame.mixer.init()

     def open__r500_20tor1000_0():
       global B
       B = 2 
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_20_window.destroy()
       show_r1000_0_page()

     r500_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r500_20_label = tk.Label(r500_20_window, image=r500_20_img)
     r500_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_20_YES_button = tk.Button(r500_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r500_20tor1000_0)
     r500_20_NO_button  = tk.Button(r500_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r500_20tor500_30)

     r500_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_20_window.mainloop()

  # R500_30 page
  def show_r500_30_page():
     r500_30_window = tk.Toplevel()
     r500_30_window.geometry("800x480")
     r500_30_window.resizable(False, False)
     r500_30_window.title("R500_30")

     pygame.mixer.init()

     def play_r500_30tor500_40():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_40_R.ogg")
       pygame.mixer.music.play()
       r500_30_window.destroy()
       show_r500_40_page()

     pygame.mixer.init()

     def open__r500_30tor1000_0():
       global B
       B = 3
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_30_window.destroy()
       show_r1000_0_page()

     r500_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r500_30_label = tk.Label(r500_30_window, image=r500_30_img)
     r500_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_30_YES_button = tk.Button(r500_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r500_30tor1000_0)
     r500_30_NO_button  = tk.Button(r500_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r500_30tor500_40)

     r500_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_30_window.mainloop()

  # R500_40 page
  def show_r500_40_page():
     r500_40_window = tk.Toplevel()
     r500_40_window.geometry("800x480")
     r500_40_window.resizable(False, False)
     r500_40_window.title("R500_40")

     pygame.mixer.init()

     def play_r500_40tor500_50():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_50_R.ogg")
       pygame.mixer.music.play()
       r500_40_window.destroy()
       show_r500_50_page()

     pygame.mixer.init()

     def open__r500_40tor1000_0():
       global B
       B = 4
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_40_window.destroy()
       show_r1000_0_page()

     r500_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r500_40_label = tk.Label(r500_40_window, image=r500_40_img)
     r500_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_40_YES_button = tk.Button(r500_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r500_40tor1000_0)
     r500_40_NO_button  = tk.Button(r500_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r500_40tor500_50)

     r500_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_40_window.mainloop()

  # R500_50 page
  def show_r500_50_page():
     r500_50_window = tk.Toplevel()
     r500_50_window.geometry("800x480")
     r500_50_window.resizable(False, False)
     r500_50_window.title("R500_50")

     pygame.mixer.init()

     def play_r500_50tor500_60():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_60_R.ogg")
       pygame.mixer.music.play()
       r500_50_window.destroy()
       show_r500_60_page()

     pygame.mixer.init()

     def open__r500_50tor1000_0():
       global B
       B = 5
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_50_window.destroy()
       show_r1000_0_page()

     r500_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r500_50_label = tk.Label(r500_50_window, image=r500_50_img)
     r500_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_50_YES_button = tk.Button(r500_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r500_50tor1000_0)
     r500_50_NO_button  = tk.Button(r500_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r500_50tor500_60)

     r500_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_50_window.mainloop()

  # R500_60 page
  def show_r500_60_page():
     r500_60_window = tk.Toplevel()
     r500_60_window.geometry("800x480")
     r500_60_window.title("R500_60")

     pygame.mixer.init()

     def play_r500_60tor500_70():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_70_R.ogg")
       pygame.mixer.music.play()
       r500_60_window.destroy()
       show_r500_70_page()

     pygame.mixer.init()

     def open__r500_60tor1000_0():
       global B
       B = 6
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_60_window.destroy()
       show_r1000_0_page()

     r500_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r500_60_label = tk.Label(r500_60_window, image=r500_60_img)
     r500_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_60_YES_button = tk.Button(r500_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r500_60tor1000_0)
     r500_60_NO_button  = tk.Button(r500_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r500_60tor500_70)

     r500_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_60_window.mainloop()

  # R500_70 page
  def show_r500_70_page():
     r500_70_window = tk.Toplevel()
     r500_70_window.geometry("800x480")
     r500_70_window.resizable(False, False)
     r500_70_window.title("R500_70")

     pygame.mixer.init()

     def play_r500_70tor500_80():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_80_R.ogg")
       pygame.mixer.music.play()
       r500_70_window.destroy()
       show_r500_80_page()

     pygame.mixer.init()

     def open__r500_70tor1000_0():
       global B
       B = 7
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_70_window.destroy()
       show_r1000_0_page()

     r500_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r500_70_label = tk.Label(r500_70_window, image=r500_70_img)
     r500_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_70_YES_button = tk.Button(r500_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r500_70tor1000_0)
     r500_70_NO_button  = tk.Button(r500_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r500_70tor500_80)

     r500_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_70_window.mainloop()

  # R500_80 page
  def show_r500_80_page():
     r500_80_window = tk.Toplevel()
     r500_80_window.geometry("800x480")
     r500_80_window.resizable(False, False)
     r500_80_window.title("R500_80")

     pygame.mixer.init()

     def play_r500_80tor1000_0():
       global B
       B = 9
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_80_window.destroy()
       show_r1000_0_page()

     pygame.mixer.init()

     def open__r500_80tor1000_00():
       global B
       B = 8
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_80_window.destroy()
       show_r1000_0_page()

     r500_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r500_80_label = tk.Label(r500_80_window, image=r500_80_img)
     r500_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_80_YES_button = tk.Button(r500_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r500_80tor1000_00)
     r500_80_NO_button  = tk.Button(r500_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r500_80tor1000_0)

     r500_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_80_window.mainloop()

  # R1000_0 page
  def show_r1000_0_page():
     r1000_0_window = tk.Toplevel()
     r1000_0_window.geometry("800x480")
     r1000_0_window.resizable(False, False)
     r1000_0_window.title("R1000_0")

     def blank3_page():
       r1000_0_window.destroy() 
       show_blank3_page()
      
     pygame.mixer.init()

     def play_r1000_10():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_10_R.ogg")
       pygame.mixer.music.play()
       r1000_0_window.destroy()
       show_r1000_10_page()

     r1000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r1000_0_label = tk.Label(r1000_0_window, image=r1000_0_img)
     r1000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_0_YES_button = tk.Button(r1000_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank3_page)
     r1000_0_NO_button  = tk.Button(r1000_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r1000_10)

     r1000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_0_window.mainloop()

  # blank3
  def show_blank3_page():
     blank3_window = tk.Toplevel()
     blank3_window.geometry("800x480")
     blank3_window.resizable(False, False)
     blank3_window.title("blank3")

     def warning3_page():
      blank3_window.destroy() 
      show_warning3_page()

     pygame.mixer.init()
     C = None
     def play_blank3tor2000_0():
       global C
       C = 0
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       blank3_window.destroy()
       show_r2000_0_page()
     
     blank3_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank3_label = tk.Label(blank3_window , image=blank3_img)
     blank3_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank3_YES_button = tk.Button(blank3_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning3_page)
     blank3_NO_button= tk.Button(blank3_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank3tor2000_0)

     blank3_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank3_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank3_window.mainloop()

  # warning3
  def show_warning3_page():
      warning3_window = tk.Toplevel()
      warning3_window.geometry("800x480")
      warning3_window.resizable(False, False)
      warning3_window.title("warning3")
      
      warning3_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning3_label = tk.Label(warning3_window, image=warning3_image)
      warning3_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning3tor1000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
        pygame.mixer.music.play()
        warning3_window.destroy()
        show_r250_0_page()

      warning3_button = tk.Button(warning3_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning3tor1000_0)
      warning3_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning3_window.mainloop()

  # R1000_10 page
  def show_r1000_10_page():
     r1000_10_window = tk.Toplevel()
     r1000_10_window.geometry("800x480")
     r1000_10_window.resizable(False, False)
     r1000_10_window.title("R1000_10")

     pygame.mixer.init()

     def play_r1000_10tor1000_20():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_20_R.ogg")
       pygame.mixer.music.play()
       r1000_10_window.destroy()
       show_r1000_20_page()

     pygame.mixer.init()

     def open__r1000_10tor2000_0():
       global C
       C = 1
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_10_window.destroy()
       show_r2000_0_page()

     r1000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r1000_10_label = tk.Label(r1000_10_window, image=r1000_10_img)
     r1000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_10_YES_button = tk.Button(r1000_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r1000_10tor2000_0)
     r1000_10_NO_button  = tk.Button(r1000_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r1000_10tor1000_20)

     r1000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_10_window.mainloop()

  # R1000_20 page
  def show_r1000_20_page():
     r1000_20_window = tk.Toplevel()
     r1000_20_window.geometry("800x480")
     r1000_20_window.resizable(False, False)
     r1000_20_window.title("R1000_20")

     pygame.mixer.init()

     def play_r1000_20tor1000_30():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_30_R.ogg")
       pygame.mixer.music.play()
       r1000_20_window.destroy()
       show_r1000_30_page()

     pygame.mixer.init()

     def open__r1000_20tor2000_0():
       global C
       C = 2
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_20_window.destroy()
       show_r2000_0_page()

     r1000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r1000_20_label = tk.Label(r1000_20_window, image=r1000_20_img)
     r1000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_20_YES_button = tk.Button(r1000_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r1000_20tor2000_0)
     r1000_20_NO_button  = tk.Button(r1000_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r1000_20tor1000_30)

     r1000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_20_window.mainloop()

  # R1000_30 page
  def show_r1000_30_page():
     r1000_30_window = tk.Toplevel()
     r1000_30_window.geometry("800x480")
     r1000_30_window.resizable(False, False)
     r1000_30_window.title("R1000_30")

     pygame.mixer.init()

     def play_r1000_30tor1000_40():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_40_R.ogg")
       pygame.mixer.music.play()
       r1000_30_window.destroy()
       show_r1000_40_page()

     pygame.mixer.init()

     def open__r1000_30tor2000_0():
       global C
       C = 3
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_30_window.destroy()
       show_r2000_0_page()

     r1000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r1000_30_label = tk.Label(r1000_30_window, image=r1000_30_img)
     r1000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_30_YES_button = tk.Button(r1000_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r1000_30tor2000_0)
     r1000_30_NO_button  = tk.Button(r1000_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r1000_30tor1000_40)

     r1000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_30_window.mainloop()

  # R1000_40 page
  def show_r1000_40_page():
     r1000_40_window = tk.Toplevel()
     r1000_40_window.geometry("800x480")
     r1000_40_window.resizable(False, False)
     r1000_40_window.title("R1000_40")

     pygame.mixer.init()

     def play_r1000_40tor1000_50():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_50_R.ogg")
       pygame.mixer.music.play()
       r1000_40_window.destroy()
       show_r1000_50_page()

     pygame.mixer.init()

     def open__r1000_40tor2000_0():
       global C
       C = 4
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_40_window.destroy()
       show_r2000_0_page()

     r1000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r1000_40_label = tk.Label(r1000_40_window, image=r1000_40_img)
     r1000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_40_YES_button = tk.Button(r1000_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r1000_40tor2000_0)
     r1000_40_NO_button  = tk.Button(r1000_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r1000_40tor1000_50)

     r1000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_40_window.mainloop()

  # R1000_50 page
  def show_r1000_50_page():
     r1000_50_window = tk.Toplevel()
     r1000_50_window.geometry("800x480")
     r1000_50_window.resizable(False, False)
     r1000_50_window.title("R1000_50")

     pygame.mixer.init()

     def play_r1000_50tor1000_60():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_60_R.ogg")
       pygame.mixer.music.play()
       r1000_50_window.destroy()
       show_r1000_60_page()

     pygame.mixer.init()

     def open__r1000_50tor2000_0():
       global C
       C = 5
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_50_window.destroy()
       show_r2000_0_page()

     r1000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r1000_50_label = tk.Label(r1000_50_window, image=r1000_50_img)
     r1000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_50_YES_button = tk.Button(r1000_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r1000_50tor2000_0)
     r1000_50_NO_button  = tk.Button(r1000_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r1000_50tor1000_60)

     r1000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_50_window.mainloop()

  # R1000_60 page
  def show_r1000_60_page():
     r1000_60_window = tk.Toplevel()
     r1000_60_window.geometry("800x480")
     r1000_60_window.resizable(False, False)
     r1000_60_window.title("R1000_60")

     pygame.mixer.init()

     def play_r1000_60tor1000_70():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_70_R.ogg")
       pygame.mixer.music.play()
       r1000_60_window.destroy()
       show_r1000_70_page()

     pygame.mixer.init()

     def open__r1000_60tor2000_0():
       global C
       C = 6
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_60_window.destroy()
       show_r2000_0_page()

     r1000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r1000_60_label = tk.Label(r1000_60_window, image=r1000_60_img)
     r1000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_60_YES_button = tk.Button(r1000_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r1000_60tor2000_0)
     r1000_60_NO_button  = tk.Button(r1000_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r1000_60tor1000_70)

     r1000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_60_window.mainloop()

  # R1000_70 page
  def show_r1000_70_page():
     r1000_70_window = tk.Toplevel()
     r1000_70_window.geometry("800x480")
     r1000_70_window.resizable(False, False)
     r1000_70_window.title("R1000_70")

     pygame.mixer.init()

     def play_r1000_70tor1000_80():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_80_R.ogg")
       pygame.mixer.music.play()
       r1000_70_window.destroy()
       show_r1000_80_page()
 
     pygame.mixer.init()

     def open__r1000_70tor2000_0():
       global C
       C = 7
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_70_window.destroy()
       show_r2000_0_page()

     r1000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r1000_70_label = tk.Label(r1000_70_window, image=r1000_70_img)
     r1000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_70_YES_button = tk.Button(r1000_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r1000_70tor2000_0)
     r1000_70_NO_button  = tk.Button(r1000_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r1000_70tor1000_80)

     r1000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_70_window.mainloop()

  # R1000_80 page
  def show_r1000_80_page():
     r1000_80_window = tk.Toplevel()
     r1000_80_window.geometry("800x480")
     r1000_80_window.resizable(False, False)
     r1000_80_window.title("R1000_80")

     pygame.mixer.init()

     def play_r1000_80tor2000_0():
       global C
       C = 9
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_80_window.destroy()
       show_r2000_0_page()

     pygame.mixer.init()

     def open__r1000_80tor2000_00():
       global C
       C = 8
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_80_window.destroy()
       show_r2000_0_page()

     r1000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r1000_80_label = tk.Label(r1000_80_window, image=r1000_80_img)
     r1000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_80_YES_button = tk.Button(r1000_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r1000_80tor2000_00)
     r1000_80_NO_button  = tk.Button(r1000_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r1000_80tor2000_0)

     r1000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_80_window.mainloop()

  # R2000_0 page
  def show_r2000_0_page():
     r2000_0_window = tk.Toplevel()
     r2000_0_window.geometry("800x480")
     r2000_0_window.resizable(False, False)
     r2000_0_window.title("R2000_0")

     def blank4_page():
      r2000_0_window.destroy() 
      show_blank4_page()
      
     pygame.mixer.init()

     def play_r2000_10():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_10_R.ogg")
       pygame.mixer.music.play()
       r2000_0_window.destroy()
       show_r2000_10_page()

     r2000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r2000_0_label = tk.Label(r2000_0_window, image=r2000_0_img)
     r2000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_0_YES_button = tk.Button(r2000_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank4_page)
     r2000_0_NO_button  = tk.Button(r2000_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r2000_10)

     r2000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_0_window.mainloop()

  # blank4
  def show_blank4_page():
     blank4_window = tk.Toplevel()
     blank4_window.geometry("800x480")
     blank4_window.resizable(False, False)
     blank4_window.title("blank4")

     def warning4_page():
       blank4_window.destroy() 
       show_warning4_page()

     pygame.mixer.init()
     D = None

     def play_blank4tor4000_0():
       global D
       D = 0
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
       pygame.mixer.music.play()
       blank4_window.destroy()
       show_r4000_0_page()
     
     blank4_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank4_label = tk.Label(blank4_window , image=blank4_img)
     blank4_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank4_YES_button = tk.Button(blank4_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning4_page)
     blank4_NO_button= tk.Button(blank4_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank4tor4000_0)

     blank4_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank4_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank4_window.mainloop()

  # warning4
  def show_warning4_page():
      warning4_window = tk.Toplevel()
      warning4_window.geometry("800x480")
      warning4_window.resizable(False, False)
      warning4_window.title("warning4")
      
      warning4_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning4_label = tk.Label(warning4_window, image=warning4_image)
      warning4_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning4tor2000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
        pygame.mixer.music.play()
        warning4_window.destroy()
        show_r250_0_page()

      warning4_button = tk.Button(warning4_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning4tor2000_0)
      warning4_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning4_window.mainloop()

  # R2000_10 page
  def show_r2000_10_page():
     r2000_10_window = tk.Toplevel()
     r2000_10_window.geometry("800x480")
     r2000_10_window.resizable(False, False)
     r2000_10_window.title("R2000_10")

     pygame.mixer.init()

     def play_r2000_10tor2000_20():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_20_R.ogg")
       pygame.mixer.music.play()
       r2000_10_window.destroy()
       show_r2000_20_page()

     pygame.mixer.init()

     def open__r2000_10tor4000_0():
       global D
       D = 1
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
       pygame.mixer.music.play()
       r2000_10_window.destroy()
       show_r4000_0_page()

     r2000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r2000_10_label = tk.Label(r2000_10_window, image=r2000_10_img)
     r2000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_10_YES_button = tk.Button(r2000_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r2000_10tor4000_0)
     r2000_10_NO_button  = tk.Button(r2000_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r2000_10tor2000_20)

     r2000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_10_window.mainloop()

  # R2000_20 page
  def show_r2000_20_page():
     r2000_20_window = tk.Toplevel()
     r2000_20_window.geometry("800x480")
     r2000_20_window.resizable(False, False)
     r2000_20_window.title("R2000_20")

     pygame.mixer.init()

     def play_r2000_20tor2000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_30_R.ogg")
      pygame.mixer.music.play()
      r2000_20_window.destroy()
      show_r2000_30_page()

     pygame.mixer.init()

     def open__r2000_20tor4000_0():
      global D
      D = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_20_window.destroy()
      show_r4000_0_page()

     r2000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r2000_20_label = tk.Label(r2000_20_window, image=r2000_20_img)
     r2000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_20_YES_button = tk.Button(r2000_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r2000_20tor4000_0)
     r2000_20_NO_button  = tk.Button(r2000_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r2000_20tor2000_30)

     r2000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_20_window.mainloop()

  # R2000_30 page
  def show_r2000_30_page():
     r2000_30_window = tk.Toplevel()
     r2000_30_window.resizable(False, False)
     r2000_30_window.geometry("800x480")
     r2000_30_window.title("R2000_30")

     pygame.mixer.init()

     def play_r2000_30tor2000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_40_R.ogg")
      pygame.mixer.music.play()
      r2000_30_window.destroy()
      show_r2000_40_page()

     pygame.mixer.init()

     def open__r2000_30tor4000_0():
      global D
      D = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_30_window.destroy()
      show_r4000_0_page()

     r2000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r2000_30_label = tk.Label(r2000_30_window, image=r2000_30_img)
     r2000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_30_YES_button = tk.Button(r2000_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r2000_30tor4000_0)
     r2000_30_NO_button  = tk.Button(r2000_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r2000_30tor2000_40)

     r2000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_30_window.mainloop()

  # R2000_40 page
  def show_r2000_40_page():
     r2000_40_window = tk.Toplevel()
     r2000_40_window.geometry("800x480")
     r2000_40_window.resizable(False, False)
     r2000_40_window.title("R2000_40")

     pygame.mixer.init()

     def play_r2000_40tor2000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_50_R.ogg")
      pygame.mixer.music.play()
      r2000_40_window.destroy()
      show_r2000_50_page()

     pygame.mixer.init()

     def open__r2000_40tor4000_0():
      global D
      D = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_40_window.destroy()
      show_r4000_0_page()

     r2000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r2000_40_label = tk.Label(r2000_40_window, image=r2000_40_img)
     r2000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_40_YES_button = tk.Button(r2000_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r2000_40tor4000_0)
     r2000_40_NO_button  = tk.Button(r2000_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r2000_40tor2000_50)

     r2000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_40_window.mainloop()

  # R2000_50 page
  def show_r2000_50_page():
     r2000_50_window = tk.Toplevel()
     r2000_50_window.geometry("800x480")
     r2000_50_window.resizable(False, False)
     r2000_50_window.title("R2000_50")

     pygame.mixer.init()

     def play_r2000_50tor2000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_60_R.ogg")
      pygame.mixer.music.play()
      r2000_50_window.destroy()
      show_r2000_60_page()

     pygame.mixer.init()

     def open__r2000_50tor4000_0():
      global D
      D = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_50_window.destroy()
      show_r4000_0_page()

     r2000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r2000_50_label = tk.Label(r2000_50_window, image=r2000_50_img)
     r2000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_50_YES_button = tk.Button(r2000_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r2000_50tor4000_0)
     r2000_50_NO_button  = tk.Button(r2000_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r2000_50tor2000_60)

     r2000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_50_window.mainloop()

  # R2000_60 page
  def show_r2000_60_page():
     r2000_60_window = tk.Toplevel()
     r2000_60_window.geometry("800x480")
     r2000_60_window.resizable(False, False)
     r2000_60_window.title("R2000_60")

     pygame.mixer.init()

     def play_r2000_60tor2000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_70_R.ogg")
      pygame.mixer.music.play()
      r2000_60_window.destroy()
      show_r2000_70_page()

     pygame.mixer.init()

     def open__r2000_60tor4000_0():
      global D
      D = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_60_window.destroy()
      show_r4000_0_page()

     r2000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r2000_60_label = tk.Label(r2000_60_window, image=r2000_60_img)
     r2000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_60_YES_button = tk.Button(r2000_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r2000_60tor4000_0)
     r2000_60_NO_button  = tk.Button(r2000_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r2000_60tor2000_70)

     r2000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_60_window.mainloop()

  # R2000_70 page
  def show_r2000_70_page():
     r2000_70_window = tk.Toplevel()
     r2000_70_window.geometry("800x480")
     r2000_70_window.resizable(False, False)
     r2000_70_window.title("R2000_70")

     pygame.mixer.init()

     def play_r2000_70tor2000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_80_R.ogg")
      pygame.mixer.music.play()
      r2000_70_window.destroy()
      show_r2000_80_page()

     pygame.mixer.init()

     def open__r2000_70tor4000_0():
      global D
      D = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_70_window.destroy()
      show_r4000_0_page()

     r2000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r2000_70_label = tk.Label(r2000_70_window, image=r2000_70_img)
     r2000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_70_YES_button = tk.Button(r2000_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r2000_70tor4000_0)
     r2000_70_NO_button  = tk.Button(r2000_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r2000_70tor2000_80)

     r2000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_70_window.mainloop()

  # R2000_80 page
  def show_r2000_80_page():
     r2000_80_window = tk.Toplevel()
     r2000_80_window.geometry("800x480")
     r2000_80_window.resizable(False, False)
     r2000_80_window.title("R2000_80")

     pygame.mixer.init()

     def play_r2000_80tor4000_0():
      global D
      D = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_80_window.destroy()
      show_r4000_0_page()

     pygame.mixer.init()

     def open__r2000_80tor4000_00():
      global D
      D = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_80_window.destroy()
      show_r4000_0_page()

     r2000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r2000_80_label = tk.Label(r2000_80_window, image=r2000_80_img)
     r2000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_80_YES_button = tk.Button(r2000_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r2000_80tor4000_00)
     r2000_80_NO_button  = tk.Button(r2000_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r2000_80tor4000_0)

     r2000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_80_window.mainloop()

  # R4000_0 page
  def show_r4000_0_page():
     r4000_0_window = tk.Toplevel()
     r4000_0_window.geometry("800x480")
     r4000_0_window.resizable(False, False)
     r4000_0_window.title("R4000_0")

     def blank5_page():
      r4000_0_window.destroy() 
      show_blank5_page()
      
     pygame.mixer.init()

     def play_r4000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_10_R.ogg")
      pygame.mixer.music.play()
      r4000_0_window.destroy()
      show_r4000_10_page()

     r4000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r4000_0_label = tk.Label(r4000_0_window, image=r4000_0_img)
     r4000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_0_YES_button = tk.Button(r4000_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank5_page)
     r4000_0_NO_button  = tk.Button(r4000_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r4000_10)

     r4000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_0_window.mainloop()

  # blank5
  def show_blank5_page():
     blank5_window = tk.Toplevel()
     blank5_window.geometry("800x480")
     blank5_window.resizable(False, False)
     blank5_window.title("blank5")

     def warning5_page():
      blank5_window.destroy() 
      show_warning5_page()

     pygame.mixer.init()
     E = None

     def play_blank5tor8000_0():
      global E
      E = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      blank5_window.destroy()
      show_r8000_0_page()
     
     blank5_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank5_label = tk.Label(blank5_window , image=blank5_img)
     blank5_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank5_YES_button = tk.Button(blank5_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning5_page)
     blank5_NO_button= tk.Button(blank5_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank5tor8000_0)

     blank5_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank5_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank5_window.mainloop()

  # warning5
  def show_warning5_page():
      warning5_window = tk.Toplevel()
      warning5_window.geometry("800x480")
      warning5_window.resizable(False, False)
      warning5_window.title("warning5")
      
      warning5_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning5_label = tk.Label(warning5_window, image=warning5_image)
      warning5_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning5tor4000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
        pygame.mixer.music.play()
        warning5_window.destroy()
        show_r250_0_page()

      warning5_button = tk.Button(warning5_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning5tor4000_0)
      warning5_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning5_window.mainloop()

  # R4000_10 page
  def show_r4000_10_page():
     r4000_10_window = tk.Toplevel()
     r4000_10_window.geometry("800x480")
     r4000_10_window.resizable(False, False)
     r4000_10_window.title("R4000_10")

     pygame.mixer.init()

     def play_r4000_10tor4000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_20_R.ogg")
      pygame.mixer.music.play()
      r4000_10_window.destroy()
      show_r4000_20_page()

     pygame.mixer.init()

     def open__r4000_10tor8000_0():
      global E
      E = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_10_window.destroy()
      show_r8000_0_page()

     r4000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r4000_10_label = tk.Label(r4000_10_window, image=r4000_10_img)
     r4000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_10_YES_button = tk.Button(r4000_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r4000_10tor8000_0)
     r4000_10_NO_button  = tk.Button(r4000_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r4000_10tor4000_20)

     r4000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_10_window.mainloop()

  # R4000_20 page
  def show_r4000_20_page():
     r4000_20_window = tk.Toplevel()
     r4000_20_window.geometry("800x480")
     r4000_20_window.resizable(False, False)
     r4000_20_window.title("R4000_20")

     pygame.mixer.init()

     def play_r4000_20tor4000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_30_R.ogg")
      pygame.mixer.music.play()
      r4000_20_window.destroy()
      show_r4000_30_page()

     pygame.mixer.init()

     def open__r4000_20tor8000_0():
      global E
      E = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_20_window.destroy()
      show_r8000_0_page()

     r4000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r4000_20_label = tk.Label(r4000_20_window, image=r4000_20_img)
     r4000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_20_YES_button = tk.Button(r4000_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r4000_20tor8000_0)
     r4000_20_NO_button  = tk.Button(r4000_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r4000_20tor4000_30)

     r4000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_20_window.mainloop()

  # R4000_30 page
  def show_r4000_30_page():
     r4000_30_window = tk.Toplevel()
     r4000_30_window.geometry("800x480")
     r4000_30_window.resizable(False, False)
     r4000_30_window.title("R4000_30")

     pygame.mixer.init()

     def play_r4000_30tor4000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_40_R.ogg")
      pygame.mixer.music.play()
      r4000_30_window.destroy()
      show_r4000_40_page()

     pygame.mixer.init()

     def open__r4000_30tor8000_0():
      global E
      E = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_30_window.destroy()
      show_r8000_0_page()

     r4000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r4000_30_label = tk.Label(r4000_30_window, image=r4000_30_img)
     r4000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_30_YES_button = tk.Button(r4000_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r4000_30tor8000_0)
     r4000_30_NO_button  = tk.Button(r4000_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r4000_30tor4000_40)

     r4000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_30_window.mainloop()

  # R4000_40 page
  def show_r4000_40_page():
     r4000_40_window = tk.Toplevel()
     r4000_40_window.geometry("800x480")
     r4000_40_window.resizable(False, False)
     r4000_40_window.title("R4000_40")

     pygame.mixer.init()

     def play_r4000_40tor4000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_50_R.ogg")
      pygame.mixer.music.play()
      r4000_40_window.destroy()
      show_r4000_50_page()

     pygame.mixer.init()

     def open__r4000_40tor8000_0():
      global E
      E = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_40_window.destroy()
      show_r8000_0_page()

     r4000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r4000_40_label = tk.Label(r4000_40_window, image=r4000_40_img)
     r4000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_40_YES_button = tk.Button(r4000_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r4000_40tor8000_0)
     r4000_40_NO_button  = tk.Button(r4000_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r4000_40tor4000_50)

     r4000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_40_window.mainloop()

  # R4000_50 page
  def show_r4000_50_page():
     r4000_50_window = tk.Toplevel()
     r4000_50_window.geometry("800x480")
     r4000_50_window.resizable(False, False)
     r4000_50_window.title("R4000_50")

     pygame.mixer.init()

     def play_r4000_50tor4000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_60_R.ogg")
      pygame.mixer.music.play()
      r4000_50_window.destroy()
      show_r4000_60_page()

     pygame.mixer.init()

     def open__r4000_50tor8000_0():
      global E
      E = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_50_window.destroy()
      show_r8000_0_page()

     r4000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r4000_50_label = tk.Label(r4000_50_window, image=r4000_50_img)
     r4000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_50_YES_button = tk.Button(r4000_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r4000_50tor8000_0)
     r4000_50_NO_button  = tk.Button(r4000_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r4000_50tor4000_60)

     r4000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_50_window.mainloop()

  # R4000_60 page
  def show_r4000_60_page():
     r4000_60_window = tk.Toplevel()
     r4000_60_window.geometry("800x480")
     r4000_60_window.resizable(False, False)
     r4000_60_window.title("R4000_60")

     pygame.mixer.init()

     def play_r4000_60tor4000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_70_R.ogg")
      pygame.mixer.music.play()
      r4000_60_window.destroy()
      show_r4000_70_page()

     pygame.mixer.init()

     def open__r4000_60tor8000_0():
      global E
      E = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_60_window.destroy()
      show_r8000_0_page()

     r4000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r4000_60_label = tk.Label(r4000_60_window, image=r4000_60_img)
     r4000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_60_YES_button = tk.Button(r4000_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r4000_60tor8000_0)
     r4000_60_NO_button  = tk.Button(r4000_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r4000_60tor4000_70)

     r4000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_60_window.mainloop()

  # R4000_70 page
  def show_r4000_70_page():
     r4000_70_window = tk.Toplevel()
     r4000_70_window.geometry("800x480")
     r4000_70_window.resizable(False, False)
     r4000_70_window.title("R4000_70")

     pygame.mixer.init()

     def play_r4000_70tor4000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_80_R.ogg")
      pygame.mixer.music.play()
      r4000_70_window.destroy()
      show_r4000_80_page()

     pygame.mixer.init()

     def open__r4000_70tor8000_0():
      global E
      E = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_70_window.destroy()
      show_r8000_0_page()

     r4000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r4000_70_label = tk.Label(r4000_70_window, image=r4000_70_img)
     r4000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_70_YES_button = tk.Button(r4000_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r4000_70tor8000_0)
     r4000_70_NO_button  = tk.Button(r4000_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r4000_70tor4000_80)

     r4000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_70_window.mainloop()

  # R4000_80 page
  def show_r4000_80_page():
     r4000_80_window = tk.Toplevel()
     r4000_80_window.geometry("800x480")
     r4000_80_window.resizable(False, False)
     r4000_80_window.title("R4000_80")

     pygame.mixer.init()

     def play_r4000_80tor8000_0():
      global E
      E = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_80_window.destroy()
      show_r8000_0_page()

     pygame.mixer.init()

     def open__r4000_80tor8000_00():
      global E
      E = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_80_window.destroy()
      show_r8000_0_page()

     r4000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r4000_80_label = tk.Label(r4000_80_window, image=r4000_80_img)
     r4000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_80_YES_button = tk.Button(r4000_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r4000_80tor8000_00)
     r4000_80_NO_button  = tk.Button(r4000_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r4000_80tor8000_0)

     r4000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_80_window.mainloop()

  # R8000_0 page
  def show_r8000_0_page():
     r8000_0_window = tk.Toplevel()
     r8000_0_window.geometry("800x480")
     r8000_0_window.resizable(False, False)
     r8000_0_window.title("R8000_0")

     def blank6_page():
      r8000_0_window.destroy() 
      show_blank6_page()
      
     pygame.mixer.init()

     def play_r8000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_10_R.ogg")
      pygame.mixer.music.play()
      r8000_0_window.destroy()
      show_r8000_10_page()

     r8000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r8000_0_label = tk.Label(r8000_0_window, image=r8000_0_img)
     r8000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_0_YES_button = tk.Button(r8000_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank6_page)
     r8000_0_NO_button  = tk.Button(r8000_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r8000_10)

     r8000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_0_window.mainloop()

  # blank6
  def show_blank6_page():
     blank6_window = tk.Toplevel()
     blank6_window.geometry("800x480")
     blank6_window.resizable(False, False)
     blank6_window.title("blank6")

     def warning6_page():
      blank6_window.destroy() 
      show_warning6_page()

     pygame.mixer.init()
     F= None

     def play_blank6toL250_0():
      global F
      F = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      blank6_window.destroy()
      show_L250_0_page()
     
     blank6_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank6_label = tk.Label(blank6_window , image=blank6_img)
     blank6_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank6_YES_button = tk.Button(blank6_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning6_page)
     blank6_NO_button= tk.Button(blank6_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank6toL250_0)

     blank6_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank6_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank6_window.mainloop()

  # warning6
  def show_warning6_page():
      warning6_window = tk.Toplevel()
      warning6_window.geometry("800x480")
      warning6_window.resizable(False, False)
      warning6_window.title("warning6")
      
      warning6_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning6_label = tk.Label(warning6_window, image=warning6_image)
      warning6_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning6tor8000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
        pygame.mixer.music.play()
        warning6_window.destroy()
        show_r250_0_page()

      warning6_button = tk.Button(warning6_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning6tor8000_0)
      warning6_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning6_window.mainloop()

  # R8000_10 page
  def show_r8000_10_page():
     r8000_10_window = tk.Toplevel()
     r8000_10_window.geometry("800x480")
     r8000_10_window.resizable(False, False)
     r8000_10_window.title("R8000_10")

     pygame.mixer.init()

     def play_r8000_10tor8000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_20_R.ogg")
      pygame.mixer.music.play()
      r8000_10_window.destroy()
      show_r8000_20_page()

     pygame.mixer.init()

     def open__r8000_10toL250_0():
      global F
      F = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_10_window.destroy()
      show_L250_0_page()

     r8000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r8000_10_label = tk.Label(r8000_10_window, image=r8000_10_img)
     r8000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_10_YES_button = tk.Button(r8000_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r8000_10toL250_0)
     r8000_10_NO_button  = tk.Button(r8000_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r8000_10tor8000_20)

     r8000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_10_window.mainloop()

  # R8000_20 page
  def show_r8000_20_page():
     r8000_20_window = tk.Toplevel()
     r8000_20_window.geometry("800x480")
     r8000_20_window.resizable(False, False)
     r8000_20_window.title("R8000_20")

     pygame.mixer.init()

     def play_r8000_20tor8000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_30_R.ogg")
      pygame.mixer.music.play()
      r8000_20_window.destroy()
      show_r8000_30_page()

     pygame.mixer.init()

     def open__r8000_20toL250_0():
      global F
      F = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_20_window.destroy()
      show_L250_0_page()

     r8000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r8000_20_label = tk.Label(r8000_20_window, image=r8000_20_img)
     r8000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_20_YES_button = tk.Button(r8000_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r8000_20toL250_0)
     r8000_20_NO_button  = tk.Button(r8000_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r8000_20tor8000_30)

     r8000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_20_window.mainloop()

  # R8000_30 page
  def show_r8000_30_page():
     r8000_30_window = tk.Toplevel()
     r8000_30_window.geometry("800x480")
     r8000_30_window.resizable(False, False)
     r8000_30_window.title("R8000_30")

     pygame.mixer.init()

     def play_r8000_30tor8000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_40_R.ogg")
      pygame.mixer.music.play()
      r8000_30_window.destroy()
      show_r8000_40_page()

     pygame.mixer.init()

     def open__r8000_30toL250_0():
      global F
      F = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_30_window.destroy()
      show_L250_0_page()

     r8000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r8000_30_label = tk.Label(r8000_30_window, image=r8000_30_img)
     r8000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_30_YES_button = tk.Button(r8000_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r8000_30toL250_0)
     r8000_30_NO_button  = tk.Button(r8000_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r8000_30tor8000_40)

     r8000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_30_window.mainloop()

  # R8000_40 page
  def show_r8000_40_page():
     r8000_40_window = tk.Toplevel()
     r8000_40_window.geometry("800x480")
     r8000_40_window.resizable(False, False)
     r8000_40_window.title("R8000_40")

     pygame.mixer.init()

     def play_r8000_40tor8000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_50_R.ogg")
      pygame.mixer.music.play()
      r8000_40_window.destroy()
      show_r8000_50_page()

     pygame.mixer.init()

     def open__r8000_40toL250_0():
      global F
      F = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_40_window.destroy()
      show_L250_0_page()

     r8000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r8000_40_label = tk.Label(r8000_40_window, image=r8000_40_img)
     r8000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_40_YES_button = tk.Button(r8000_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r8000_40toL250_0)
     r8000_40_NO_button  = tk.Button(r8000_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r8000_40tor8000_50)

     r8000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_40_window.mainloop()

  # R8000_50 page
  def show_r8000_50_page():
     r8000_50_window = tk.Toplevel()
     r8000_50_window.geometry("800x480")
     r8000_50_window.resizable(False, False)
     r8000_50_window.title("R8000_50")

     pygame.mixer.init()

     def play_r8000_50tor8000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_60_R.ogg")
      pygame.mixer.music.play()
      r8000_50_window.destroy()
      show_r8000_60_page()

     pygame.mixer.init()

     def open__r8000_50toL250_0():
      global F
      F = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_50_window.destroy()
      show_L250_0_page()

     r8000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r8000_50_label = tk.Label(r8000_50_window, image=r8000_50_img)
     r8000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_50_YES_button = tk.Button(r8000_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r8000_50toL250_0)
     r8000_50_NO_button  = tk.Button(r8000_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r8000_50tor8000_60)

     r8000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_50_window.mainloop()

  # R8000_60 page
  def show_r8000_60_page():
     r8000_60_window = tk.Toplevel()
     r8000_60_window.geometry("800x480")
     r8000_60_window.resizable(False, False)
     r8000_60_window.title("R8000_60")

     pygame.mixer.init()

     def play_r8000_60tor8000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_70_R.ogg")
      pygame.mixer.music.play()
      r8000_60_window.destroy()
      show_r8000_70_page()

     pygame.mixer.init()

     def open__r8000_60toL250_0():
      global F
      F = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_60_window.destroy()
      show_L250_0_page()

     r8000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r8000_60_label = tk.Label(r8000_60_window, image=r8000_60_img)
     r8000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_60_YES_button = tk.Button(r8000_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r8000_60toL250_0)
     r8000_60_NO_button  = tk.Button(r8000_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r8000_60tor8000_70)

     r8000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_60_window.mainloop()

  # R8000_70 page
  def show_r8000_70_page():
     r8000_70_window = tk.Toplevel()
     r8000_70_window.geometry("800x480")
     r8000_70_window.resizable(False, False)
     r8000_70_window.title("R8000_70")

     pygame.mixer.init()

     def play_r8000_70tor8000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_80_R.ogg")
      pygame.mixer.music.play()
      r8000_70_window.destroy()
      show_r8000_80_page()

     pygame.mixer.init()

     def open__r8000_70toL250_0():
      global F
      F = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_70_window.destroy()
      show_L250_0_page()

     r8000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r8000_70_label = tk.Label(r8000_70_window, image=r8000_70_img)
     r8000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_70_YES_button = tk.Button(r8000_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r8000_70toL250_0)
     r8000_70_NO_button  = tk.Button(r8000_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r8000_70tor8000_80)

     r8000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_70_window.mainloop()

  # R8000_80 page
  def show_r8000_80_page():
     r8000_80_window = tk.Toplevel()
     r8000_80_window.geometry("800x480")
     r8000_80_window.resizable(False, False)
     r8000_80_window.title("R8000_80")

     pygame.mixer.init()

     def play_r8000_80toL250_0():
      global F
      F = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_80_window.destroy()
      show_L250_0_page()

     pygame.mixer.init()

     def open__r8000_80toL250_00():
      global F
      F = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_80_window.destroy()
      show_L250_0_page()

     r8000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     r8000_80_label = tk.Label(r8000_80_window, image=r8000_80_img)
     r8000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_80_YES_button = tk.Button(r8000_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__r8000_80toL250_00)
     r8000_80_NO_button  = tk.Button(r8000_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_r8000_80toL250_0)

     r8000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_80_window.mainloop()

  # L250_0 page
  def show_L250_0_page():
     L250_0_window = tk.Toplevel()
     L250_0_window.geometry("800x480")
     L250_0_window.resizable(False, False)
     L250_0_window.title("L250_0")

     def blank7_page():
      L250_0_window.destroy() 
      show_blank7_page()
      
     pygame.mixer.init()
     
     def play_L250_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_10_L.mp3")
      pygame.mixer.music.play()
      L250_0_window.destroy()
      show_L250_10_page()

     L250_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L250_0_label = tk.Label(L250_0_window, image=L250_0_img)
     L250_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_0_YES_button = tk.Button(L250_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank7_page)
     L250_0_NO_button  = tk.Button(L250_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L250_10)

     L250_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_0_window.mainloop()

  # blank7
  def show_blank7_page():
     blank7_window = tk.Toplevel()
     blank7_window.geometry("800x480")
     blank7_window.resizable(False, False)
     blank7_window.title("blank7")

     def warning7_page():
      blank7_window.destroy() 
      show_warning7_page()

     pygame.mixer.init()
     A1 = None

     def play_blank7toL500_0():
      global A1
      A1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      blank7_window.destroy()
      show_L500_0_page()
     
     blank7_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank7_label = tk.Label(blank7_window , image=blank7_img)
     blank7_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank7_YES_button = tk.Button(blank7_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning7_page)
     blank7_NO_button= tk.Button(blank7_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank7toL500_0)

     blank7_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank7_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank7_window.mainloop() 

  # warning7
  def show_warning7_page():
      warning7_window = tk.Toplevel()
      warning7_window.geometry("800x480")
      warning7_window.resizable(False, False)
      warning7_window.title("warning7")
      
      warning7_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning7_label = tk.Label(warning7_window, image=warning7_image)
      warning7_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning7toL250_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
        pygame.mixer.music.play()
        warning7_window.destroy()
        show_r250_0_page()

      warning7_button = tk.Button(warning7_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning7toL250_0)
      warning7_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning7_window.mainloop()

  # L250_10 page
  def show_L250_10_page():
     L250_10_window = tk.Toplevel()
     L250_10_window.geometry("800x480")
     L250_10_window.resizable(False, False)
     L250_10_window.title("L250_10")

     pygame.mixer.init()

     def play_L250_10toL250_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_20_L.mp3")
      pygame.mixer.music.play()
      L250_10_window.destroy()
      show_L250_20_page()

     pygame.mixer.init()

     def open__L250_10toL500_0():
      global A1
      A1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_10_window.destroy()
      show_L500_0_page()

     L250_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L250_10_label = tk.Label(L250_10_window, image=L250_10_img)
     L250_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_10_YES_button = tk.Button(L250_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L250_10toL500_0)
     L250_10_NO_button  = tk.Button(L250_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L250_10toL250_20)

     L250_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_10_window.mainloop()

  # L250_20 page
  def show_L250_20_page():
     L250_20_window = tk.Toplevel()
     L250_20_window.geometry("800x480")
     L250_20_window.resizable(False, False)
     L250_20_window.title("L250_20")

     pygame.mixer.init()

     def play_L250_20toL250_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_30_L.mp3")
      pygame.mixer.music.play()
      L250_20_window.destroy()
      show_L250_30_page()

     pygame.mixer.init()

     def open__L250_20toL500_0():
      global A1
      A1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_20_window.destroy()
      show_L500_0_page()

     L250_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L250_20_label = tk.Label(L250_20_window, image=L250_20_img)
     L250_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_20_YES_button = tk.Button(L250_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L250_20toL500_0)
     L250_20_NO_button  = tk.Button(L250_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L250_20toL250_30)

     L250_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_20_window.mainloop()

  # L250_30 page
  def show_L250_30_page():
     L250_30_window = tk.Toplevel()
     L250_30_window.geometry("800x480")
     L250_30_window.resizable(False, False)
     L250_30_window.title("L250_30")

     pygame.mixer.init()

     def play_L250_30toL250_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_40_L.mp3")
      pygame.mixer.music.play()
      L250_30_window.destroy()
      show_L250_40_page()

     pygame.mixer.init()

     def open__L250_30toL500_0():
      global A1
      A1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_30_window.destroy()
      show_L500_0_page()

     L250_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L250_30_label = tk.Label(L250_30_window, image=L250_30_img)
     L250_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_30_YES_button = tk.Button(L250_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L250_30toL500_0)
     L250_30_NO_button  = tk.Button(L250_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L250_30toL250_40)

     L250_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_30_window.mainloop()

  # L250_40 page
  def show_L250_40_page():
     L250_40_window = tk.Toplevel()
     L250_40_window.geometry("800x480")
     L250_40_window.resizable(False, False)
     L250_40_window.title("L250_40")

     pygame.mixer.init()

     def play_L250_40toL250_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_50_L.mp3")
      pygame.mixer.music.play()
      L250_40_window.destroy()
      show_L250_50_page()

     pygame.mixer.init()

     def open__L250_40toL500_0():
      global A1
      A1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_40_window.destroy()
      show_L500_0_page()

     L250_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L250_40_label = tk.Label(L250_40_window, image=L250_40_img)
     L250_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_40_YES_button = tk.Button(L250_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L250_40toL500_0)
     L250_40_NO_button  = tk.Button(L250_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L250_40toL250_50)

     L250_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_40_window.mainloop()

  # L250_50 page
  def show_L250_50_page():
     L250_50_window = tk.Toplevel()
     L250_50_window.geometry("800x480")
     L250_50_window.resizable(False, False)
     L250_50_window.title("L250_50")

     pygame.mixer.init()

     def play_L250_50toL250_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_60_L.mp3")
      pygame.mixer.music.play()
      L250_50_window.destroy()
      show_L250_60_page()

     pygame.mixer.init()

     def open__L250_50toL500_0():
      global A1
      A1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_50_window.destroy()
      show_L500_0_page()

     L250_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L250_50_label = tk.Label(L250_50_window, image=L250_50_img)
     L250_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_50_YES_button = tk.Button(L250_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L250_50toL500_0)
     L250_50_NO_button  = tk.Button(L250_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L250_50toL250_60)

     L250_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_50_window.mainloop()

  # L250_60 page
  def show_L250_60_page():
     L250_60_window = tk.Toplevel()
     L250_60_window.geometry("800x480")
     L250_60_window.resizable(False, False)
     L250_60_window.title("L250_60")

     pygame.mixer.init()

     def play_L250_60toL250_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_70_L.mp3")
      pygame.mixer.music.play()
      L250_60_window.destroy()
      show_L250_70_page()

     pygame.mixer.init()

     def open__L250_60toL500_0():
      global A1
      A1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_60_window.destroy()
      show_L500_0_page()

     L250_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L250_60_label = tk.Label(L250_60_window, image=L250_60_img)
     L250_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_60_YES_button = tk.Button(L250_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L250_60toL500_0)
     L250_60_NO_button  = tk.Button(L250_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L250_60toL250_70)

     L250_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_60_window.mainloop()

  # L250_70 page
  def show_L250_70_page():
     L250_70_window = tk.Toplevel()
     L250_70_window.geometry("800x480")
     L250_70_window.resizable(False, False)
     L250_70_window.title("L250_70")

     pygame.mixer.init()

     def play_L250_70toL250_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_80_L.mp3")
      pygame.mixer.music.play()
      L250_70_window.destroy()
      show_L250_80_page()

     pygame.mixer.init()

     def open__L250_70toL500_0():
      global A1
      A1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_70_window.destroy()
      show_L500_0_page()

     L250_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L250_70_label = tk.Label(L250_70_window, image=L250_70_img)
     L250_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_70_YES_button = tk.Button(L250_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L250_70toL500_0)
     L250_70_NO_button  = tk.Button(L250_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L250_70toL250_80)

     L250_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_70_window.mainloop()

   # L250_80 page
  def show_L250_80_page():
     L250_80_window = tk.Toplevel()
     L250_80_window.geometry("800x480")
     L250_80_window.resizable(False, False)
     L250_80_window.title("L250_80")

     pygame.mixer.init()

     def play_L250_80toL500_0():
      global A1
      A1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_80_window.destroy()
      show_L500_0_page()

     pygame.mixer.init()

     def open__L250_80toL500_00():
      global A1
      A1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_80_window.destroy()
      show_L500_0_page()

     L250_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L250_80_label = tk.Label(L250_80_window, image=L250_80_img)
     L250_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_80_YES_button = tk.Button(L250_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L250_80toL500_00)
     L250_80_NO_button  = tk.Button(L250_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L250_80toL500_0)

     L250_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_80_window.mainloop()

  # L500_0 page
  def show_L500_0_page():
     L500_0_window = tk.Toplevel()
     L500_0_window.geometry("800x480")
     L500_0_window.resizable(False, False)
     L500_0_window.title("L500_0")

     def blank8_page():
      L500_0_window.destroy() 
      show_blank8_page()
      
     pygame.mixer.init()

     def play_L500_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_10_L.mp3")
      pygame.mixer.music.play()
      L500_0_window.destroy()
      show_L500_10_page()

     L500_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L500_0_label = tk.Label(L500_0_window, image=L500_0_img)
     L500_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_0_YES_button = tk.Button(L500_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank8_page)
     L500_0_NO_button  = tk.Button(L500_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L500_10)

     L500_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_0_window.mainloop()

  # blank8
  def show_blank8_page():
     blank8_window = tk.Toplevel()
     blank8_window.geometry("800x480")
     blank8_window.resizable(False, False)
     blank8_window.title("blank8")

     def warning8_page():
      blank8_window.destroy() 
      show_warning8_page()

     pygame.mixer.init()
     B1=None

     def play_blank8toL1000_0():
      global B1
      B1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      blank8_window.destroy()
      show_L1000_0_page()
     
     blank8_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank8_label = tk.Label(blank8_window , image=blank8_img)
     blank8_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank8_YES_button = tk.Button(blank8_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning8_page)
     blank8_NO_button= tk.Button(blank8_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank8toL1000_0)

     blank8_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank8_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank8_window.mainloop()

  # warning8
  def show_warning8_page():
      warning8_window = tk.Toplevel()
      warning8_window.geometry("800x480")
      warning8_window.resizable(False, False)
      warning8_window.title("warning8")
      
      warning8_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning8_label = tk.Label(warning8_window, image=warning8_image)
      warning8_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning8toL500_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
        pygame.mixer.music.play()
        warning8_window.destroy()
        show_r250_0_page()

      warning8_button = tk.Button(warning8_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning8toL500_0)
      warning8_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning8_window.mainloop()

  # L500_10 page
  def show_L500_10_page():
     L500_10_window = tk.Toplevel()
     L500_10_window.geometry("800x480")
     L500_10_window.resizable(False, False)
     L500_10_window.title("L500_10")

     pygame.mixer.init()

     def play_L500_10toL500_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_20_L.mp3")
      pygame.mixer.music.play()
      L500_10_window.destroy()
      show_L500_20_page()

     pygame.mixer.init()

     def open__L500_10toL1000_0():
      global B1
      B1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_10_window.destroy()
      show_L1000_0_page()

     L500_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L500_10_label = tk.Label(L500_10_window, image=L500_10_img)
     L500_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_10_YES_button = tk.Button(L500_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L500_10toL1000_0)
     L500_10_NO_button  = tk.Button(L500_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L500_10toL500_20)

     L500_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_10_window.mainloop()

  # L500_20 page
  def show_L500_20_page():
     L500_20_window = tk.Toplevel()
     L500_20_window.geometry("800x480")
     L500_20_window.resizable(False, False)
     L500_20_window.title("L500_20")

     pygame.mixer.init()

     def play_L500_20toL500_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_30_L.mp3")
      pygame.mixer.music.play()
      L500_20_window.destroy()
      show_L500_30_page()

     pygame.mixer.init()

     def open__L500_20toL1000_0():
      global B1
      B1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_20_window.destroy()
      show_L1000_0_page()

     L500_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L500_20_label = tk.Label(L500_20_window, image=L500_20_img)
     L500_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_20_YES_button = tk.Button(L500_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L500_20toL1000_0)
     L500_20_NO_button  = tk.Button(L500_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L500_20toL500_30)

     L500_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_20_window.mainloop()

  # L500_30 page
  def show_L500_30_page():
     L500_30_window = tk.Toplevel()
     L500_30_window.geometry("800x480")
     L500_30_window.resizable(False, False)
     L500_30_window.title("L500_30")

     pygame.mixer.init()

     def play_L500_30toL500_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_40_L.mp3")
      pygame.mixer.music.play()
      L500_30_window.destroy()
      show_L500_40_page()

     pygame.mixer.init()

     def open__L500_30toL1000_0():
      global B1
      B1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_30_window.destroy()
      show_L1000_0_page()

     L500_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L500_30_label = tk.Label(L500_30_window, image=L500_30_img)
     L500_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_30_YES_button = tk.Button(L500_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L500_30toL1000_0)
     L500_30_NO_button  = tk.Button(L500_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L500_30toL500_40)

     L500_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_30_window.mainloop()

  # L500_40 page
  def show_L500_40_page():
     L500_40_window = tk.Toplevel()
     L500_40_window.geometry("800x480")
     L500_40_window.resizable(False, False)
     L500_40_window.title("L500_40")

     pygame.mixer.init()

     def play_L500_40toL500_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_50_L.mp3")
      pygame.mixer.music.play()
      L500_40_window.destroy()
      show_L500_50_page()

     pygame.mixer.init()

     def open__L500_40toL1000_0():
      global B1
      B1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_40_window.destroy()
      show_L1000_0_page()

     L500_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L500_40_label = tk.Label(L500_40_window, image=L500_40_img)
     L500_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_40_YES_button = tk.Button(L500_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L500_40toL1000_0)
     L500_40_NO_button  = tk.Button(L500_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L500_40toL500_50)

     L500_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_40_window.mainloop()

  # L500_50 page
  def show_L500_50_page():
     L500_50_window = tk.Toplevel()
     L500_50_window.geometry("800x480")
     L500_50_window.resizable(False, False)
     L500_50_window.title("L500_50")

     pygame.mixer.init()

     def play_L500_50toL500_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_60_L.mp3")
      pygame.mixer.music.play()
      L500_50_window.destroy()
      show_L500_60_page()

     pygame.mixer.init()

     def open__L500_50toL1000_0():
      global B1
      B1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_50_window.destroy()
      show_L1000_0_page()

     L500_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L500_50_label = tk.Label(L500_50_window, image=L500_50_img)
     L500_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_50_YES_button = tk.Button(L500_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L500_50toL1000_0)
     L500_50_NO_button  = tk.Button(L500_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L500_50toL500_60)

     L500_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_50_window.mainloop()

  # L500_60 page
  def show_L500_60_page():
     L500_60_window = tk.Toplevel()
     L500_60_window.geometry("800x480")
     L500_60_window.resizable(False, False)
     L500_60_window.title("L500_60")

     pygame.mixer.init()

     def play_L500_60toL500_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_70_L.mp3")
      pygame.mixer.music.play()
      L500_60_window.destroy()
      show_L500_70_page()

     pygame.mixer.init()

     def open__L500_60toL1000_0():
      global B1
      B1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_60_window.destroy()
      show_L1000_0_page()

     L500_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L500_60_label = tk.Label(L500_60_window, image=L500_60_img)
     L500_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_60_YES_button = tk.Button(L500_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L500_60toL1000_0)
     L500_60_NO_button  = tk.Button(L500_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L500_60toL500_70)

     L500_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_60_window.mainloop()

  # L500_70 page
  def show_L500_70_page():
     L500_70_window = tk.Toplevel()
     L500_70_window.geometry("800x480")
     L500_70_window.resizable(False, False)
     L500_70_window.title("L500_70")

     pygame.mixer.init()

     def play_L500_70toL500_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_80_L.mp3")
      pygame.mixer.music.play()
      L500_70_window.destroy()
      show_L500_80_page()

     pygame.mixer.init()

     def open__L500_70toL1000_0():
      global B1
      B1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_70_window.destroy()
      show_L1000_0_page()

     L500_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L500_70_label = tk.Label(L500_70_window, image=L500_70_img)
     L500_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_70_YES_button = tk.Button(L500_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L500_70toL1000_0)
     L500_70_NO_button  = tk.Button(L500_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L500_70toL500_80)

     L500_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_70_window.mainloop()

  # L500_80 page
  def show_L500_80_page():
     L500_80_window = tk.Toplevel()
     L500_80_window.geometry("800x480")
     L500_80_window.resizable(False, False)
     L500_80_window.title("L500_80")

     pygame.mixer.init()

     def play_L500_80toL1000_0():
      global B1
      B1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_80_window.destroy()
      show_L1000_0_page()

     pygame.mixer.init()

     def open__L500_80toL1000_00():
      global B1
      B1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_80_window.destroy()
      show_L1000_0_page()

     L500_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L500_80_label = tk.Label(L500_80_window, image=L500_80_img)
     L500_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_80_YES_button = tk.Button(L500_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L500_80toL1000_00)
     L500_80_NO_button  = tk.Button(L500_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L500_80toL1000_0)

     L500_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_80_window.mainloop()

  # L1000_0 page
  def show_L1000_0_page():
     L1000_0_window = tk.Toplevel()
     L1000_0_window.geometry("800x480")
     L1000_0_window.resizable(False, False)
     L1000_0_window.title("L1000_0")

     def blank9_page():
      L1000_0_window.destroy() 
      show_blank9_page()
      
     pygame.mixer.init()

     def play_L1000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_10_L.mp3")
      pygame.mixer.music.play()
      L1000_0_window.destroy()
      show_L1000_10_page()

     L1000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L1000_0_label = tk.Label(L1000_0_window, image=L1000_0_img)
     L1000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_0_YES_button = tk.Button(L1000_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank9_page)
     L1000_0_NO_button  = tk.Button(L1000_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L1000_10)

     L1000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_0_window.mainloop()

  # blank9
  def show_blank9_page():
     blank9_window = tk.Toplevel()
     blank9_window.geometry("800x480")
     blank9_window.resizable(False, False)
     blank9_window.title("blank9")

     def warning9_page():
      blank9_window.destroy() 
      show_warning9_page()

     pygame.mixer.init()
     C1 = None

     def play_blank9toL2000_0():
      global C1
      C1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      blank9_window.destroy()
      show_L2000_0_page()
     
     blank9_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank9_label = tk.Label(blank9_window , image=blank9_img)
     blank9_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank9_YES_button = tk.Button(blank9_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning9_page)
     blank9_NO_button= tk.Button(blank9_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank9toL2000_0)

     blank9_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank9_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank9_window.mainloop()

  # warning9
  def show_warning9_page():
      warning9_window = tk.Toplevel()
      warning9_window.geometry("800x480")
      warning9_window.resizable(False, False)
      warning9_window.title("warning9")
      
      warning9_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning9_label = tk.Label(warning9_window, image=warning9_image)
      warning9_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning9toL1000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
        pygame.mixer.music.play()
        warning9_window.destroy()
        show_r250_0_page()

      warning9_button = tk.Button(warning9_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning9toL1000_0)
      warning9_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning9_window.mainloop()

  # L1000_10 page
  def show_L1000_10_page():
     L1000_10_window = tk.Toplevel()
     L1000_10_window.geometry("800x480")
     L1000_10_window.resizable(False, False)
     L1000_10_window.title("L1000_10")

     pygame.mixer.init()

     def play_L1000_10toL1000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_20_L.mp3")
      pygame.mixer.music.play()
      L1000_10_window.destroy()
      show_L1000_20_page()

     pygame.mixer.init()

     def open__L1000_10toL2000_0():
      global C1
      C1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_10_window.destroy()
      show_L2000_0_page()

     L1000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L1000_10_label = tk.Label(L1000_10_window, image=L1000_10_img)
     L1000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_10_YES_button = tk.Button(L1000_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L1000_10toL2000_0)
     L1000_10_NO_button  = tk.Button(L1000_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L1000_10toL1000_20)

     L1000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_10_window.mainloop()

  # L1000_20 page
  def show_L1000_20_page():
     L1000_20_window = tk.Toplevel()
     L1000_20_window.geometry("800x480")
     L1000_20_window.resizable(False, False)
     L1000_20_window.title("L1000_20")

     pygame.mixer.init()

     def play_L1000_20toL1000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_30_L.mp3")
      pygame.mixer.music.play()
      L1000_20_window.destroy()
      show_L1000_30_page()

     pygame.mixer.init()

     def open__L1000_20toL2000_0():
      global C1
      C1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_20_window.destroy()
      show_L2000_0_page()

     L1000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L1000_20_label = tk.Label(L1000_20_window, image=L1000_20_img)
     L1000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_20_YES_button = tk.Button(L1000_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L1000_20toL2000_0)
     L1000_20_NO_button  = tk.Button(L1000_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L1000_20toL1000_30)

     L1000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_20_window.mainloop()

  # L1000_30 page
  def show_L1000_30_page():
     L1000_30_window = tk.Toplevel()
     L1000_30_window.geometry("800x480")
     L1000_30_window.resizable(False, False)
     L1000_30_window.title("L1000_30")

     pygame.mixer.init()

     def play_L1000_30toL1000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_40_L.mp3")
      pygame.mixer.music.play()
      L1000_30_window.destroy()
      show_L1000_40_page()

     pygame.mixer.init()

     def open__L1000_30toL2000_0():
      global C1
      C1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_30_window.destroy()
      show_L2000_0_page()

     L1000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L1000_30_label = tk.Label(L1000_30_window, image=L1000_30_img)
     L1000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_30_YES_button = tk.Button(L1000_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L1000_30toL2000_0)
     L1000_30_NO_button  = tk.Button(L1000_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L1000_30toL1000_40)

     L1000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_30_window.mainloop()

  # L1000_40 page
  def show_L1000_40_page():
     L1000_40_window = tk.Toplevel()
     L1000_40_window.geometry("800x480")
     L1000_40_window.resizable(False, False)
     L1000_40_window.title("L1000_40")

     pygame.mixer.init()

     def play_L1000_40toL1000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_50_L.mp3")
      pygame.mixer.music.play()
      L1000_40_window.destroy()
      show_L1000_50_page()

     pygame.mixer.init()

     def open__L1000_40toL2000_0():
      global C1
      C1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_40_window.destroy()
      show_L2000_0_page()

     L1000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L1000_40_label = tk.Label(L1000_40_window, image=L1000_40_img)
     L1000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_40_YES_button = tk.Button(L1000_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L1000_40toL2000_0)
     L1000_40_NO_button  = tk.Button(L1000_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L1000_40toL1000_50)

     L1000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_40_window.mainloop()

  # L1000_50 page
  def show_L1000_50_page():
     L1000_50_window = tk.Toplevel()
     L1000_50_window.geometry("800x480")
     L1000_50_window.resizable(False, False)
     L1000_50_window.title("L1000_50")

     pygame.mixer.init()

     def play_L1000_50toL1000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_60_L.mp3")
      pygame.mixer.music.play()
      L1000_50_window.destroy()
      show_L1000_60_page()

     pygame.mixer.init()

     def open__L1000_50toL2000_0():
      global C1
      C1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_50_window.destroy()
      show_L2000_0_page()

     L1000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L1000_50_label = tk.Label(L1000_50_window, image=L1000_50_img)
     L1000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_50_YES_button = tk.Button(L1000_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L1000_50toL2000_0)
     L1000_50_NO_button  = tk.Button(L1000_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L1000_50toL1000_60)

     L1000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_50_window.mainloop()

  # L1000_60 page
  def show_L1000_60_page():
     L1000_60_window = tk.Toplevel()
     L1000_60_window.geometry("800x480")
     L1000_60_window.resizable(False, False)
     L1000_60_window.title("L1000_60")

     pygame.mixer.init()

     def play_L1000_60toL1000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_70_L.mp3")
      pygame.mixer.music.play()
      L1000_60_window.destroy()
      show_L1000_70_page()

     pygame.mixer.init()

     def open__L1000_60toL2000_0():
      global C1
      C1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_60_window.destroy()
      show_L2000_0_page()

     L1000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L1000_60_label = tk.Label(L1000_60_window, image=L1000_60_img)
     L1000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_60_YES_button = tk.Button(L1000_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L1000_60toL2000_0)
     L1000_60_NO_button  = tk.Button(L1000_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L1000_60toL1000_70)

     L1000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_60_window.mainloop()

  # L1000_70 page
  def show_L1000_70_page():
     L1000_70_window = tk.Toplevel()
     L1000_70_window.geometry("800x480")
     L1000_70_window.resizable(False, False)
     L1000_70_window.title("L1000_70")

     pygame.mixer.init()

     def play_L1000_70toL1000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_80_L.mp3")
      pygame.mixer.music.play()
      L1000_70_window.destroy()
      show_L1000_80_page()

     pygame.mixer.init()

     def open__L1000_70toL2000_0():
      global C1
      C1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_70_window.destroy()
      show_L2000_0_page()

     L1000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L1000_70_label = tk.Label(L1000_70_window, image=L1000_70_img)
     L1000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_70_YES_button = tk.Button(L1000_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L1000_70toL2000_0)
     L1000_70_NO_button  = tk.Button(L1000_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L1000_70toL1000_80)

     L1000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_70_window.mainloop()

  # L1000_80 page
  def show_L1000_80_page():
     L1000_80_window = tk.Toplevel()
     L1000_80_window.geometry("800x480")
     L1000_80_window.resizable(False, False)
     L1000_80_window.title("L1000_80")

     pygame.mixer.init()

     def play_L1000_80toL2000_0():
      global C1
      C1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_80_window.destroy()
      show_L2000_0_page()

     pygame.mixer.init()

     def open__L1000_80toL2000_00():
      global C1
      C1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_80_window.destroy()
      show_L2000_0_page()

     L1000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L1000_80_label = tk.Label(L1000_80_window, image=L1000_80_img)
     L1000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_80_YES_button = tk.Button(L1000_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L1000_80toL2000_00)
     L1000_80_NO_button  = tk.Button(L1000_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L1000_80toL2000_0)

     L1000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_80_window.mainloop()

  # L2000_0 page
  def show_L2000_0_page():
     L2000_0_window = tk.Toplevel()
     L2000_0_window.geometry("800x480")
     L2000_0_window.resizable(False, False)
     L2000_0_window.title("L2000_0")

     def blank10_page():
      L2000_0_window.destroy() 
      show_blank10_page()
      
     pygame.mixer.init()

     def play_L2000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_10_L.mp3")
      pygame.mixer.music.play()
      L2000_0_window.destroy()
      show_L2000_10_page()

     L2000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L2000_0_label = tk.Label(L2000_0_window, image=L2000_0_img)
     L2000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_0_YES_button = tk.Button(L2000_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank10_page)
     L2000_0_NO_button  = tk.Button(L2000_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L2000_10)

     L2000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_0_window.mainloop()

  # blank10
  def show_blank10_page():
     blank10_window = tk.Toplevel()
     blank10_window.geometry("800x480")
     blank10_window.resizable(False, False)
     blank10_window.title("blank10")

     def warning10_page():
      blank10_window.destroy() 
      show_warning10_page()

     pygame.mixer.init()
     D1 =None

     def play_blank10toL4000_0():
      global D1
      D1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      blank10_window.destroy()
      show_L4000_0_page()
     
     blank10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank10_label = tk.Label(blank10_window , image=blank10_img)
     blank10_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank10_YES_button = tk.Button(blank10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning10_page)
     blank10_NO_button= tk.Button(blank10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank10toL4000_0)

     blank10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank10_window.mainloop()

  # warning10
  def show_warning10_page():
      warning10_window = tk.Toplevel()
      warning10_window.geometry("800x480")
      warning10_window.resizable(False, False)
      warning10_window.title("warning10")
      
      warning10_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning10_label = tk.Label(warning10_window, image=warning10_image)
      warning10_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning10toL2000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
        pygame.mixer.music.play()
        warning10_window.destroy()
        show_r250_0_page()

      warning10_button = tk.Button(warning10_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning10toL2000_0)
      warning10_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning10_window.mainloop()

  # L2000_10 page
  def show_L2000_10_page():
     L2000_10_window = tk.Toplevel()
     L2000_10_window.geometry("800x480")
     L2000_10_window.resizable(False, False)
     L2000_10_window.title("L2000_10")

     pygame.mixer.init()

     def play_L2000_10toL2000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_20_L.mp3")
      pygame.mixer.music.play()
      L2000_10_window.destroy()
      show_L2000_20_page()

     pygame.mixer.init()

     def open__L2000_10toL4000_0():
      global D1
      D1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_10_window.destroy()
      show_L4000_0_page()

     L2000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L2000_10_label = tk.Label(L2000_10_window, image=L2000_10_img)
     L2000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_10_YES_button = tk.Button(L2000_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L2000_10toL4000_0)
     L2000_10_NO_button  = tk.Button(L2000_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L2000_10toL2000_20)

     L2000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_10_window.mainloop()

  # L2000_20 page
  def show_L2000_20_page():
     L2000_20_window = tk.Toplevel()
     L2000_20_window.geometry("800x480")
     L2000_20_window.resizable(False, False)
     L2000_20_window.title("L2000_20")

     pygame.mixer.init()

     def play_L2000_20toL2000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_30_L.mp3")
      pygame.mixer.music.play()
      L2000_20_window.destroy()
      show_L2000_30_page()

     pygame.mixer.init()

     def open__L2000_20toL4000_0():
      global D1
      D1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_20_window.destroy()
      show_L4000_0_page()

     L2000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L2000_20_label = tk.Label(L2000_20_window, image=L2000_20_img)
     L2000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_20_YES_button = tk.Button(L2000_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L2000_20toL4000_0)
     L2000_20_NO_button  = tk.Button(L2000_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L2000_20toL2000_30)

     L2000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_20_window.mainloop()

  # L2000_30 page
  def show_L2000_30_page():
     L2000_30_window = tk.Toplevel()
     L2000_30_window.geometry("800x480")
     L2000_30_window.resizable(False, False)
     L2000_30_window.title("L2000_30")

     pygame.mixer.init()

     def play_L2000_30toL2000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_40_L.mp3")
      pygame.mixer.music.play()
      L2000_30_window.destroy()
      show_L2000_40_page()

     pygame.mixer.init()

     def open__L2000_30toL4000_0():
      global D1
      D1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_30_window.destroy()
      show_L4000_0_page()

     L2000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L2000_30_label = tk.Label(L2000_30_window, image=L2000_30_img)
     L2000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_30_YES_button = tk.Button(L2000_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L2000_30toL4000_0)
     L2000_30_NO_button  = tk.Button(L2000_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L2000_30toL2000_40)

     L2000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_30_window.mainloop()

  # L2000_40 page
  def show_L2000_40_page():
     L2000_40_window = tk.Toplevel()
     L2000_40_window.geometry("800x480")
     L2000_40_window.resizable(False, False)
     L2000_40_window.title("L2000_40")

     pygame.mixer.init()

     def play_L2000_40toL2000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_50_L.mp3")
      pygame.mixer.music.play()
      L2000_40_window.destroy()
      show_L2000_50_page()

     pygame.mixer.init()

     def open__L2000_40toL4000_0():
      global D1
      D1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_40_window.destroy()
      show_L4000_0_page()

     L2000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L2000_40_label = tk.Label(L2000_40_window, image=L2000_40_img)
     L2000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_40_YES_button = tk.Button(L2000_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L2000_40toL4000_0)
     L2000_40_NO_button  = tk.Button(L2000_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L2000_40toL2000_50)

     L2000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_40_window.mainloop()

  # L2000_50 page
  def show_L2000_50_page():
     L2000_50_window = tk.Toplevel()
     L2000_50_window.geometry("800x480")
     L2000_50_window.resizable(False, False)
     L2000_50_window.title("L2000_50")

     pygame.mixer.init()

     def play_L2000_50toL2000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_60_L.mp3")
      pygame.mixer.music.play()
      L2000_50_window.destroy()
      show_L2000_60_page()

     pygame.mixer.init()

     def open__L2000_50toL4000_0():
      global D1
      D1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_50_window.destroy()
      show_L4000_0_page()

     L2000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L2000_50_label = tk.Label(L2000_50_window, image=L2000_50_img)
     L2000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_50_YES_button = tk.Button(L2000_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L2000_50toL4000_0)
     L2000_50_NO_button  = tk.Button(L2000_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L2000_50toL2000_60)

     L2000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_50_window.mainloop()

  # L2000_60 page
  def show_L2000_60_page():
     L2000_60_window = tk.Toplevel()
     L2000_60_window.geometry("800x480")
     L2000_60_window.resizable(False, False)
     L2000_60_window.title("L2000_60")

     pygame.mixer.init()

     def play_L2000_60toL2000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_70_L.mp3")
      pygame.mixer.music.play()
      L2000_60_window.destroy()
      show_L2000_70_page()

     pygame.mixer.init()

     def open__L2000_60toL4000_0():
      global D1
      D1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_60_window.destroy()
      show_L4000_0_page()

     L2000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L2000_60_label = tk.Label(L2000_60_window, image=L2000_60_img)
     L2000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_60_YES_button = tk.Button(L2000_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L2000_60toL4000_0)
     L2000_60_NO_button  = tk.Button(L2000_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L2000_60toL2000_70)

     L2000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_60_window.mainloop()

  # L2000_70 page
  def show_L2000_70_page():
     L2000_70_window = tk.Toplevel()
     L2000_70_window.geometry("800x480")
     L2000_70_window.resizable(False, False)
     L2000_70_window.title("L2000_70")

     pygame.mixer.init()

     def play_L2000_70toL2000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_80_L.mp3")
      pygame.mixer.music.play()
      L2000_70_window.destroy()
      show_L2000_80_page()

     pygame.mixer.init()

     def open__L2000_70toL4000_0():
      global D1
      D1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_70_window.destroy()
      show_L4000_0_page()

     L2000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L2000_70_label = tk.Label(L2000_70_window, image=L2000_70_img)
     L2000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_70_YES_button = tk.Button(L2000_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L2000_70toL4000_0)
     L2000_70_NO_button  = tk.Button(L2000_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L2000_70toL2000_80)

     L2000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_70_window.mainloop()

  # L2000_80 page
  def show_L2000_80_page():
     L2000_80_window = tk.Toplevel()
     L2000_80_window.geometry("800x480")
     L2000_80_window.resizable(False, False)
     L2000_80_window.title("L2000_80")

     pygame.mixer.init()

     def play_L2000_80toL4000_0():
      global D1
      D1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_80_window.destroy()
      show_L4000_0_page()

     pygame.mixer.init()

     def open__L2000_80toL4000_00():
      global D1
      D1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_80_window.destroy()
      show_L4000_0_page()

     L2000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L2000_80_label = tk.Label(L2000_80_window, image=L2000_80_img)
     L2000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_80_YES_button = tk.Button(L2000_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L2000_80toL4000_00)
     L2000_80_NO_button  = tk.Button(L2000_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L2000_80toL4000_0)

     L2000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_80_window.mainloop()

  # L4000_0 page
  def show_L4000_0_page():
     L4000_0_window = tk.Toplevel()
     L4000_0_window.geometry("800x480")
     L4000_0_window.resizable(False, False)
     L4000_0_window.title("L4000_0")

     def blank11_page():
      L4000_0_window.destroy() 
      show_blank11_page()
      
     pygame.mixer.init()

     def play_L4000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_10_L.mp3")
      pygame.mixer.music.play()
      L4000_0_window.destroy()
      show_L4000_10_page()

     L4000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L4000_0_label = tk.Label(L4000_0_window, image=L4000_0_img)
     L4000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_0_YES_button = tk.Button(L4000_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank11_page)
     L4000_0_NO_button  = tk.Button(L4000_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L4000_10)

     L4000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_0_window.mainloop()

  # blank11
  def show_blank11_page():
     blank11_window = tk.Toplevel()
     blank11_window.geometry("800x480")
     blank11_window.resizable(False, False)
     blank11_window.title("blank11")

     def warning11_page():
      blank11_window.destroy() 
      show_warning11_page()

     pygame.mixer.init()
     E1=None
     def play_blank11toL8000_0():
      global E1
      E1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      blank11_window.destroy()
      show_L8000_0_page()
     
     blank11_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank11_label = tk.Label(blank11_window , image=blank11_img)
     blank11_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank11_YES_button = tk.Button(blank11_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning11_page)
     blank11_NO_button= tk.Button(blank11_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank11toL8000_0)

     blank11_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank11_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank11_window.mainloop()

  # warning11
  def show_warning11_page():
      warning11_window = tk.Toplevel()
      warning11_window.geometry("800x480")
      warning11_window.resizable(False, False)
      warning11_window.title("warning11")
      
      warning11_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning11_label = tk.Label(warning11_window, image=warning11_image)
      warning11_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning11toL4000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
        pygame.mixer.music.play()
        warning11_window.destroy()
        show_r250_0_page()

      warning11_button = tk.Button(warning11_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning11toL4000_0)
      warning11_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning11_window.mainloop()

  # L4000_10 page
  def show_L4000_10_page():
     L4000_10_window = tk.Toplevel()
     L4000_10_window.geometry("800x480")
     L4000_10_window.resizable(False, False)
     L4000_10_window.title("L4000_10")

     pygame.mixer.init()

     def play_L4000_10toL4000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_20_L.mp3")
      pygame.mixer.music.play()
      L4000_10_window.destroy()
      show_L4000_20_page()

     pygame.mixer.init()

     def open__L4000_10toL8000_0():
      global E1
      E1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_10_window.destroy()
      show_L8000_0_page()

     L4000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L4000_10_label = tk.Label(L4000_10_window, image=L4000_10_img)
     L4000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_10_YES_button = tk.Button(L4000_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L4000_10toL8000_0)
     L4000_10_NO_button  = tk.Button(L4000_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L4000_10toL4000_20)

     L4000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_10_window.mainloop()

  # L4000_20 page
  def show_L4000_20_page():
     L4000_20_window = tk.Toplevel()
     L4000_20_window.geometry("800x480")
     L4000_20_window.resizable(False, False)
     L4000_20_window.title("L4000_20")

     pygame.mixer.init()

     def play_L4000_20toL4000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_30_L.mp3")
      pygame.mixer.music.play()
      L4000_20_window.destroy()
      show_L4000_30_page()

     pygame.mixer.init()

     def open__L4000_20toL8000_0():
      global E1
      E1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_20_window.destroy()
      show_L8000_0_page()

     L4000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L4000_20_label = tk.Label(L4000_20_window, image=L4000_20_img)
     L4000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_20_YES_button = tk.Button(L4000_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L4000_20toL8000_0)
     L4000_20_NO_button  = tk.Button(L4000_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L4000_20toL4000_30)

     L4000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_20_window.mainloop()

  # L4000_30 page
  def show_L4000_30_page():
     L4000_30_window = tk.Toplevel()
     L4000_30_window.geometry("800x480")
     L4000_30_window.resizable(False, False)
     L4000_30_window.title("L4000_30")

     pygame.mixer.init()

     def play_L4000_30toL4000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_40_L.mp3")
      pygame.mixer.music.play()
      L4000_30_window.destroy()
      show_L4000_40_page()

     pygame.mixer.init()

     def open__L4000_30toL8000_0():
      global E1
      E1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_30_window.destroy()
      show_L8000_0_page()

     L4000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L4000_30_label = tk.Label(L4000_30_window, image=L4000_30_img)
     L4000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_30_YES_button = tk.Button(L4000_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L4000_30toL8000_0)
     L4000_30_NO_button  = tk.Button(L4000_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L4000_30toL4000_40)

     L4000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_30_window.mainloop()

  # L4000_40 page
  def show_L4000_40_page():
     L4000_40_window = tk.Toplevel()
     L4000_40_window.geometry("800x480")
     L4000_40_window.resizable(False, False)
     L4000_40_window.title("L4000_40")

     pygame.mixer.init()

     def play_L4000_40toL4000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_50_L.mp3")
      pygame.mixer.music.play()
      L4000_40_window.destroy()
      show_L4000_50_page()

     pygame.mixer.init()

     def open__L4000_40toL8000_0():
      global E1
      E1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_40_window.destroy()
      show_L8000_0_page()

     L4000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L4000_40_label = tk.Label(L4000_40_window, image=L4000_40_img)
     L4000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_40_YES_button = tk.Button(L4000_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L4000_40toL8000_0)
     L4000_40_NO_button  = tk.Button(L4000_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L4000_40toL4000_50)

     L4000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_40_window.mainloop()

  # L4000_50 page
  def show_L4000_50_page():
     L4000_50_window = tk.Toplevel()
     L4000_50_window.geometry("800x480")
     L4000_50_window.resizable(False, False)
     L4000_50_window.title("L4000_50")

     pygame.mixer.init()

     def play_L4000_50toL4000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_60_L.mp3")
      pygame.mixer.music.play()
      L4000_50_window.destroy()
      show_L4000_60_page()

     pygame.mixer.init()

     def open__L4000_50toL8000_0():
      global E1
      E1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_50_window.destroy()
      show_L8000_0_page()

     L4000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L4000_50_label = tk.Label(L4000_50_window, image=L4000_50_img)
     L4000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_50_YES_button = tk.Button(L4000_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L4000_50toL8000_0)
     L4000_50_NO_button  = tk.Button(L4000_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L4000_50toL4000_60)

     L4000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_50_window.mainloop()

  # L4000_60 page
  def show_L4000_60_page():
     L4000_60_window = tk.Toplevel()
     L4000_60_window.geometry("800x480")
     L4000_60_window.resizable(False, False)
     L4000_60_window.title("L4000_60")

     pygame.mixer.init()

     def play_L4000_60toL4000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_70_L.mp3")
      pygame.mixer.music.play()
      L4000_60_window.destroy()
      show_L4000_70_page()

     pygame.mixer.init()

     def open__L4000_60toL8000_0():
      global E1
      E1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_60_window.destroy()
      show_L8000_0_page()

     L4000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L4000_60_label = tk.Label(L4000_60_window, image=L4000_60_img)
     L4000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_60_YES_button = tk.Button(L4000_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L4000_60toL8000_0)
     L4000_60_NO_button  = tk.Button(L4000_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L4000_60toL4000_70)

     L4000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_60_window.mainloop()

  # L4000_70 page
  def show_L4000_70_page():
     L4000_70_window = tk.Toplevel()
     L4000_70_window.geometry("800x480")
     L4000_70_window.resizable(False, False)
     L4000_70_window.title("L4000_70")

     pygame.mixer.init()

     def play_L4000_70toL4000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_80_L.mp3")
      pygame.mixer.music.play()
      L4000_70_window.destroy()
      show_L4000_80_page()

     pygame.mixer.init()

     def open__L4000_70toL8000_0():
      global E1
      E1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_70_window.destroy()
      show_L8000_0_page()

     L4000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L4000_70_label = tk.Label(L4000_70_window, image=L4000_70_img)
     L4000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_70_YES_button = tk.Button(L4000_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L4000_70toL8000_0)
     L4000_70_NO_button  = tk.Button(L4000_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L4000_70toL4000_80)

     L4000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_70_window.mainloop()

  # L4000_80 page
  def show_L4000_80_page():
     L4000_80_window = tk.Toplevel()
     L4000_80_window.geometry("800x480")
     L4000_80_window.resizable(False, False)
     L4000_80_window.title("L4000_80")

     pygame.mixer.init()

     def play_L4000_80toL8000_0():
      global E1
      E1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_80_window.destroy()
      show_L8000_0_page()

     pygame.mixer.init()

     def open__L4000_80toL8000_00():
      global E1
      E1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_80_window.destroy()
      show_L8000_0_page()

     L4000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L4000_80_label = tk.Label(L4000_80_window, image=L4000_80_img)
     L4000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_80_YES_button = tk.Button(L4000_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L4000_80toL8000_00)
     L4000_80_NO_button  = tk.Button(L4000_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L4000_80toL8000_0)

     L4000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_80_window.mainloop()

  # L8000_0 page
  def show_L8000_0_page():
     L8000_0_window = tk.Toplevel()
     L8000_0_window.geometry("800x480")
     L8000_0_window.resizable(False, False)
     L8000_0_window.title("L8000_0")

     def blank12_page():
      L8000_0_window.destroy() 
      show_blank12_page()
      
     pygame.mixer.init()

     def play_L8000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_10_L.mp3")
      pygame.mixer.music.play()
      L8000_0_window.destroy()
      show_L8000_10_page()

     L8000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L8000_0_label = tk.Label(L8000_0_window, image=L8000_0_img)
     L8000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_0_YES_button = tk.Button(L8000_0_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=blank12_page)
     L8000_0_NO_button  = tk.Button(L8000_0_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L8000_10)

     L8000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_0_window.mainloop()

  # blank12
  def show_blank12_page():
     blank12_window = tk.Toplevel()
     blank12_window.geometry("800x480")
     blank12_window.resizable(False, False)
     blank12_window.title("blank12")

     def warning12_page():
      blank12_window.destroy() 
      show_warning12_page()

     pygame.mixer.init()
     F1=None

     def play_blank12tospeechtest_312():
      global F1
      F1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      blank12_window.destroy()
      show_speechtest_312_page()
     
     blank12_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     blank12_label = tk.Label(blank12_window , image=blank12_img)
     blank12_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank12_YES_button = tk.Button(blank12_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=warning12_page)
     blank12_NO_button= tk.Button(blank12_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_blank12tospeechtest_312)

     blank12_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank12_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank12_window.mainloop()

  # warning12
  def show_warning12_page():
      warning12_window = tk.Toplevel()
      warning12_window.geometry("800x480")
      warning12_window.resizable(False, False)
      warning12_window.title("warning12")
      
      warning12_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blank.png")
      warning12_label = tk.Label(warning12_window, image=warning12_image)
      warning12_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def open_warning12toL8000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
        pygame.mixer.music.play()
        warning12_window.destroy()
        show_r250_0_page()

      warning12_button = tk.Button(warning12_window, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open_warning12toL8000_0)
      warning12_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning12_window.mainloop()

  # L8000_10 page
  def show_L8000_10_page():
     L8000_10_window = tk.Toplevel()
     L8000_10_window.geometry("800x480")
     L8000_10_window.resizable(False, False)
     L8000_10_window.title("L8000_10")

     pygame.mixer.init()

     def play_L8000_10toL8000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_20_L.mp3")
      pygame.mixer.music.play()
      L8000_10_window.destroy()
      show_L8000_20_page()

     pygame.mixer.init()

     def open__L8000_10tospeechtest_312():
      global F1
      F1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_10_window.destroy()
      show_speechtest_312_page()

     L8000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L8000_10_label = tk.Label(L8000_10_window, image=L8000_10_img)
     L8000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_10_YES_button = tk.Button(L8000_10_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L8000_10tospeechtest_312)
     L8000_10_NO_button  = tk.Button(L8000_10_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L8000_10toL8000_20)

     L8000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_10_window.mainloop()

  # L8000_20 page
  def show_L8000_20_page():
     L8000_20_window = tk.Toplevel()
     L8000_20_window.geometry("800x480")
     L8000_20_window.resizable(False, False)
     L8000_20_window.title("L8000_20")

     pygame.mixer.init()

     def play_L8000_20toL8000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_30_L.mp3")
      pygame.mixer.music.play()
      L8000_20_window.destroy()
      show_L8000_30_page()

     pygame.mixer.init()

     def open__L8000_20tospeechtest_312():
      global F1
      F1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_20_window.destroy()
      show_speechtest_312_page()

     L8000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L8000_20_label = tk.Label(L8000_20_window, image=L8000_20_img)
     L8000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_20_YES_button = tk.Button(L8000_20_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L8000_20tospeechtest_312)
     L8000_20_NO_button  = tk.Button(L8000_20_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L8000_20toL8000_30)

     L8000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_20_window.mainloop()

  # L8000_30 page
  def show_L8000_30_page():
     L8000_30_window = tk.Toplevel()
     L8000_30_window.geometry("800x480")
     L8000_30_window.resizable(False, False)
     L8000_30_window.title("L8000_30")

     pygame.mixer.init()

     def play_L8000_30toL8000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_40_L.mp3")
      pygame.mixer.music.play()
      L8000_30_window.destroy()
      show_L8000_40_page()

     pygame.mixer.init()

     def open__L8000_30tospeechtest_312():
      global F1
      F1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_30_window.destroy()
      show_speechtest_312_page()

     L8000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L8000_30_label = tk.Label(L8000_30_window, image=L8000_30_img)
     L8000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_30_YES_button = tk.Button(L8000_30_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L8000_30tospeechtest_312)
     L8000_30_NO_button  = tk.Button(L8000_30_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L8000_30toL8000_40)

     L8000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_30_window.mainloop()

  # L8000_40 page
  def show_L8000_40_page():
     L8000_40_window = tk.Toplevel()
     L8000_40_window.geometry("800x480")
     L8000_40_window.resizable(False, False)
     L8000_40_window.title("L8000_40")

     pygame.mixer.init()

     def play_L8000_40toL8000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_50_L.mp3")
      pygame.mixer.music.play()
      L8000_40_window.destroy()
      show_L8000_50_page()

     pygame.mixer.init()

     def open__L8000_40tospeechtest_312():
      global F1
      F1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_40_window.destroy()
      show_speechtest_312_page()

     L8000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L8000_40_label = tk.Label(L8000_40_window, image=L8000_40_img)
     L8000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_40_YES_button = tk.Button(L8000_40_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L8000_40tospeechtest_312)
     L8000_40_NO_button  = tk.Button(L8000_40_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L8000_40toL8000_50)

     L8000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_40_window.mainloop()

  # L8000_50 page
  def show_L8000_50_page():
     L8000_50_window = tk.Toplevel()
     L8000_50_window.geometry("800x480")
     L8000_50_window.resizable(False, False)
     L8000_50_window.title("L8000_50")

     pygame.mixer.init()

     def play_L8000_50toL8000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_60_L.mp3")
      pygame.mixer.music.play()
      L8000_50_window.destroy()
      show_L8000_60_page()

     pygame.mixer.init()

     def open__L8000_50tospeechtest_312():
      global F1
      F1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_50_window.destroy()
      show_speechtest_312_page()

     L8000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L8000_50_label = tk.Label(L8000_50_window, image=L8000_50_img)
     L8000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_50_YES_button = tk.Button(L8000_50_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L8000_50tospeechtest_312)
     L8000_50_NO_button  = tk.Button(L8000_50_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L8000_50toL8000_60)

     L8000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_50_window.mainloop()

  # L8000_60 page
  def show_L8000_60_page():
     L8000_60_window = tk.Toplevel()
     L8000_60_window.geometry("800x480")
     L8000_60_window.resizable(False, False)
     L8000_60_window.title("L8000_60")

     pygame.mixer.init()

     def play_L8000_60toL8000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_70_L.mp3")
      pygame.mixer.music.play()
      L8000_60_window.destroy()
      show_L8000_70_page()

     pygame.mixer.init()

     def open__L8000_60tospeechtest_312():
      global F1
      F1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_60_window.destroy()
      show_speechtest_312_page()

     L8000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L8000_60_label = tk.Label(L8000_60_window, image=L8000_60_img)
     L8000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_60_YES_button = tk.Button(L8000_60_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L8000_60tospeechtest_312)
     L8000_60_NO_button  = tk.Button(L8000_60_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L8000_60toL8000_70)

     L8000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_60_window.mainloop()

  # L8000_70 page
  def show_L8000_70_page():
     L8000_70_window = tk.Toplevel()
     L8000_70_window.geometry("800x480")
     L8000_70_window.resizable(False, False)
     L8000_70_window.title("L8000_70")

     pygame.mixer.init()

     def play_L8000_70toL8000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_80_L.mp3")
      pygame.mixer.music.play()
      L8000_70_window.destroy()
      show_L8000_80_page()

     pygame.mixer.init()

     def open__L8000_70tospeechtest_312():
      global F1
      F1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_70_window.destroy()
      show_speechtest_312_page()

     L8000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L8000_70_label = tk.Label(L8000_70_window, image=L8000_70_img)
     L8000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_70_YES_button = tk.Button(L8000_70_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L8000_70tospeechtest_312)
     L8000_70_NO_button  = tk.Button(L8000_70_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L8000_70toL8000_80)

     L8000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_70_window.mainloop()

  # L8000_80 page
  def show_L8000_80_page():
     L8000_80_window = tk.Toplevel()
     L8000_80_window.geometry("800x480")
     L8000_80_window.resizable(False, False)
     L8000_80_window.title("L8000_80")

     pygame.mixer.init()

     def play_L8000_80tospeechtest_312():
      global F1
      F1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_80_window.destroy()
      show_speechtest_312_page()

     pygame.mixer.init()

     def open__L8000_80tospeechtest_312():
      global F1
      F1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_80_window.destroy()
      show_speechtest_312_page()

     L8000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigth.png")
     L8000_80_label = tk.Label(L8000_80_window, image=L8000_80_img)
     L8000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_80_YES_button = tk.Button(L8000_80_window, text="YES", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=open__L8000_80tospeechtest_312)
     L8000_80_NO_button  = tk.Button(L8000_80_window, text="NO", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=play_L8000_80tospeechtest_312)

     L8000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_80_window.mainloop()

  # speechtest_312 page
  def show_speechtest_312_page():
     speechtest_312_window = tk.Toplevel()
     speechtest_312_window.geometry("800x480")
     speechtest_312_window.resizable(False, False)
     speechtest_312_window.title("speechtest_312")

     speechtest_312_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_312_label = tk.Label(speechtest_312_window, image=speechtest_312_img)
     speechtest_312_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     G=None

     def openture__speechtest_312tospeechtest_396():
      global G
      G = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\396.mp3")
      pygame.mixer.music.play()
      speechtest_312_window.destroy()
      show_speechtest_396_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_312tospeechtest_396():
      global G
      G = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\396.mp3")
      pygame.mixer.music.play()
      speechtest_312_window.destroy()
      show_speechtest_396_page()

     speechtest_312_true_button = tk.Button(speechtest_312_window, text="3 1 2", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_312tospeechtest_396)
     speechtest_311_false_button  = tk.Button(speechtest_312_window, text="3 1 1", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_312tospeechtest_396)
     speechtest_212_false_button  = tk.Button(speechtest_312_window, text="2 1 2", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_312tospeechtest_396)
     speechtest_313_false_button  = tk.Button(speechtest_312_window, text="3 1 3", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_312tospeechtest_396)

     speechtest_313_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_212_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_311_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_312_true_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)

     speechtest_312_window.mainloop()

  # speechtest_396 page
  def show_speechtest_396_page():
     speechtest_396_window = tk.Toplevel()
     speechtest_396_window.geometry("800x480")
     speechtest_396_window.resizable(False, False)
     speechtest_396_window.title("speechtest_396")

     speechtest_396_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_396_label = tk.Label(speechtest_396_window, image=speechtest_396_img)
     speechtest_396_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     H=None

     def openture__speechtest_396tospeechtest_839():
      global H
      H = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\839.mp3")
      pygame.mixer.music.play()
      speechtest_396_window.destroy()
      show_speechtest_839_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_396tospeechtest_839():
      global H
      H = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\839.mp3")
      pygame.mixer.music.play()
      speechtest_396_window.destroy()
      show_speechtest_839_page()

     speechtest_396_true_button = tk.Button(speechtest_396_window, text="3 9 6", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_396tospeechtest_839)
     speechtest_469_false_button  = tk.Button(speechtest_396_window, text="4 6 9", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_396tospeechtest_839)
     speechtest_858_false_button  = tk.Button(speechtest_396_window, text="8 5 8", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_396tospeechtest_839)
     speechtest_389_false_button  = tk.Button(speechtest_396_window, text="3 8 9", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_396tospeechtest_839)

     speechtest_389_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_858_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_469_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_396_true_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)

     speechtest_396_window.mainloop()

  # speechtest_839 page
  def show_speechtest_839_page():
     speechtest_839_window = tk.Toplevel()
     speechtest_839_window.geometry("800x480")
     speechtest_839_window.resizable(False, False)
     speechtest_839_window.title("speechtest_839")

     speechtest_839_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_839_label = tk.Label(speechtest_839_window, image=speechtest_839_img)
     speechtest_839_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     I=None

     def openture__speechtest_839tospeechtest_958():
      global I
      I = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\958.mp3")
      pygame.mixer.music.play()
      speechtest_839_window.destroy()
      show_speechtest_958_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_839tospeechtest_958():
      global I
      I = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\958.mp3")
      pygame.mixer.music.play()
      speechtest_839_window.destroy()
      show_speechtest_958_page()

     speechtest_839_true_button = tk.Button(speechtest_839_window, text="8 3 9", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_839tospeechtest_958)
     speechtest_938_false_button  = tk.Button(speechtest_839_window, text="9 3 8", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_839tospeechtest_958)
     speechtest_856_false_button  = tk.Button(speechtest_839_window, text="8 5 6", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_839tospeechtest_958)
     speechtest_786_false_button  = tk.Button(speechtest_839_window, text="7 8 6", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_839tospeechtest_958)

     speechtest_938_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_856_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_786_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_839_true_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_839_window.mainloop()

  # speechtest_958 page
  def show_speechtest_958_page():
     speechtest_958_window = tk.Toplevel()
     speechtest_958_window.geometry("800x480")
     speechtest_958_window.resizable(False, False)
     speechtest_958_window.title("speechtest_958")

     speechtest_958_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_958_label = tk.Label(speechtest_958_window, image=speechtest_958_img)
     speechtest_958_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     J=None

     def openture__speechtest_958tospeechtest_262():
      global J
      J = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\462.mp3")
      pygame.mixer.music.play()
      speechtest_958_window.destroy()
      show_speechtest_262_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_958tospeechtest_262():
      global J
      J = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\462.mp3")
      pygame.mixer.music.play()
      speechtest_958_window.destroy()
      show_speechtest_262_page()

     speechtest_958_true_button = tk.Button(speechtest_958_window, text="9 5 8", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_958tospeechtest_262)
     speechtest_987_false_button  = tk.Button(speechtest_958_window, text="9 8 7", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_958tospeechtest_262)
     speechtest_865_false_button  = tk.Button(speechtest_958_window, text="8 6 5", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_958tospeechtest_262)
     speechtest_858_false_button  = tk.Button(speechtest_958_window, text="8 5 8", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_958tospeechtest_262)

     speechtest_987_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_865_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_858_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_958_true_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_958_window.mainloop()

  # speechtest_262 page
  def show_speechtest_262_page():
     speechtest_262_window = tk.Toplevel()
     speechtest_262_window.geometry("800x480")
     speechtest_262_window.resizable(False, False)
     speechtest_262_window.title("speechtest_262")

     speechtest_262_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_262_label = tk.Label(speechtest_262_window, image=speechtest_262_img)
     speechtest_262_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     K=None

     def openture__speechtest_262tospeechtest_862():
      global K
      K = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\862.mp3")
      pygame.mixer.music.play()
      speechtest_262_window.destroy()
      show_speechtest_862_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_262tospeechtest_862():
      global K
      K = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\862.mp3")
      pygame.mixer.music.play()
      speechtest_262_window.destroy()
      show_speechtest_862_page()

     speechtest_262_true_button = tk.Button(speechtest_262_window, text="4 6 2", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_262tospeechtest_862)
     speechtest_363_false_button  = tk.Button(speechtest_262_window, text="3 6 3", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_262tospeechtest_862)
     speechtest_362_false_button  = tk.Button(speechtest_262_window, text="3 6 2", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_262tospeechtest_862)
     speechtest_286_false_button  = tk.Button(speechtest_262_window, text="2 8 6", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_262tospeechtest_862)

     speechtest_363_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_362_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_286_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_262_true_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_262_window.mainloop()
     
  # speechtest_862 page
  def show_speechtest_862_page():
     speechtest_862_window = tk.Toplevel()
     speechtest_862_window.geometry("800x480")
     speechtest_862_window.resizable(False, False)
     speechtest_862_window.title("speechtest_862")

     speechtest_862_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_862_label = tk.Label(speechtest_862_window, image=speechtest_862_img)
     speechtest_862_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     L=None

     def openture__speechtest_862tospeechtest_218():
      global L
      L = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\218.mp3")
      pygame.mixer.music.play()
      speechtest_862_window.destroy()
      show_speechtest_218_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_862tospeechtest_218():
      global L
      L = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\218.mp3")
      pygame.mixer.music.play()
      speechtest_862_window.destroy()
      show_speechtest_218_page()

     speechtest_862_true_button = tk.Button(speechtest_862_window, text="8 6 2", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_862tospeechtest_218)
     speechtest_756_false_button  = tk.Button(speechtest_862_window, text="7 5 6", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_862tospeechtest_218)
     speechtest_686_false_button  = tk.Button(speechtest_862_window, text="6 8 6", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_862tospeechtest_218)
     speechtest_915_false_button  = tk.Button(speechtest_862_window, text="9 1 5", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_862tospeechtest_218)

     speechtest_756_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_686_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_915_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_862_true_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_862_window.mainloop()

  # speechtest_218 page
  def show_speechtest_218_page():
     speechtest_218_window = tk.Toplevel()
     speechtest_218_window.geometry("800x480")
     speechtest_218_window.resizable(False, False)
     speechtest_218_window.title("speechtest_218")

     speechtest_218_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_218_label = tk.Label(speechtest_218_window, image=speechtest_218_img)
     speechtest_218_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     M=None

     def openture__speechtest_218tospeechtest_920():
      global M
      M = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\920.mp3")
      pygame.mixer.music.play()
      speechtest_218_window.destroy()
      show_speechtest_920_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_218tospeechtest_920():
      global M
      M = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\920.mp3")
      pygame.mixer.music.play()
      speechtest_218_window.destroy()
      show_speechtest_920_page()

     speechtest_208_true_button = tk.Button(speechtest_218_window, text="2 0 8", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_218tospeechtest_920)
     speechtest_124_false_button  = tk.Button(speechtest_218_window, text="1 0 4", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_218tospeechtest_920)
     speechtest_329_false_button  = tk.Button(speechtest_218_window, text="3 0 9", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_218tospeechtest_920)
     speechtest_168_false_button  = tk.Button(speechtest_218_window, text="1 0 8", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_218tospeechtest_920)

     speechtest_124_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_329_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_168_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_208_true_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_218_window.mainloop()

  # speechtest_920 page
  def show_speechtest_920_page():
     speechtest_920_window = tk.Toplevel()
     speechtest_920_window.geometry("800x480")
     speechtest_920_window.resizable(False, False)
     speechtest_920_window.title("speechtest_920")

     speechtest_920_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_920_label = tk.Label(speechtest_920_window, image=speechtest_920_img)
     speechtest_920_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     N=None

     def openture__speechtest_920tospeechtest_025():
      global N
      N = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\025.mp3")
      pygame.mixer.music.play()
      speechtest_920_window.destroy()
      show_speechtest_025_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_920tospeechtest_025():
      global N
      N = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\025.mp3")
      pygame.mixer.music.play()
      speechtest_920_window.destroy()
      show_speechtest_025_page()

     speechtest_920_true_button = tk.Button(speechtest_920_window, text="9 2 0", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_920tospeechtest_025)
     speechtest_820_false_button  = tk.Button(speechtest_920_window, text="8 2 0", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_920tospeechtest_025)
     speechtest_760_false_button  = tk.Button(speechtest_920_window, text="7 6 0", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_920tospeechtest_025)
     speechtest_680_false_button  = tk.Button(speechtest_920_window, text="6 8 0", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_920tospeechtest_025)

     speechtest_820_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_760_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_680_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_920_true_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_920_window.mainloop()

  # speechtest_025 page
  def show_speechtest_025_page():
     speechtest_025_window = tk.Toplevel()
     speechtest_025_window.geometry("800x480")
     speechtest_025_window.resizable(False, False)
     speechtest_025_window.title("speechtest_025")

     speechtest_025_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_025_label = tk.Label(speechtest_025_window, image=speechtest_025_img)
     speechtest_025_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     O=None

     def openture__speechtest_025tospeechtest_593():
      global O
      O = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\593.mp3")
      pygame.mixer.music.play()
      speechtest_025_window.destroy()
      show_speechtest_593_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_025tospeechtest_593():
      global O
      O = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\593.mp3")
      pygame.mixer.music.play()
      speechtest_025_window.destroy()
      show_speechtest_593_page()

     speechtest_025_true_button = tk.Button(speechtest_025_window, text="0 2 5", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_025tospeechtest_593)
     speechtest_046_false_button  = tk.Button(speechtest_025_window, text="0 4 6", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_025tospeechtest_593)
     speechtest_065_false_button  = tk.Button(speechtest_025_window, text="0 6 5", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_025tospeechtest_593)
     speechtest_097_false_button  = tk.Button(speechtest_025_window, text="0 9 7", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_025tospeechtest_593)

     speechtest_097_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_046_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_065_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_025_true_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_025_window.mainloop()

  # speechtest_593 page
  def show_speechtest_593_page():
     speechtest_593_window = tk.Toplevel()
     speechtest_593_window.geometry("800x480")
     speechtest_593_window.resizable(False, False)
     speechtest_593_window.title("speechtest_593")

     speechtest_593_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_593_label = tk.Label(speechtest_593_window, image=speechtest_593_img)
     speechtest_593_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     P=None

     def openture__speechtest_593tospeechtest_106():
      global P
      P = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\106.mp3")
      pygame.mixer.music.play()
      speechtest_593_window.destroy()
      show_speechtest_106_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_593tospeechtest_106():
      global P
      P = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\106.mp3")
      pygame.mixer.music.play()
      speechtest_593_window.destroy()
      show_speechtest_106_page()

     speechtest_593_true_button = tk.Button(speechtest_593_window, text="5 9 3", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_593tospeechtest_106)
     speechtest_465_false_button  = tk.Button(speechtest_593_window, text="4 6 5", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_593tospeechtest_106)
     speechtest_972_false_button  = tk.Button(speechtest_593_window, text="9 7 2", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_593tospeechtest_106)
     speechtest_831_false_button  = tk.Button(speechtest_593_window, text="8 3 1", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_593tospeechtest_106)

     speechtest_465_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_972_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_831_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_593_true_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_593_window.mainloop()

  # speechtest_106 page
  def show_speechtest_106_page():
     speechtest_106_window = tk.Toplevel()
     speechtest_106_window.geometry("800x480")
     speechtest_106_window.resizable(False, False)
     speechtest_106_window.title("speechtest_106")

     speechtest_106_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_106_label = tk.Label(speechtest_106_window, image=speechtest_106_img)
     speechtest_106_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     Q=None

     def openture__speechtest_106tospeechtest_491():
      global Q
      Q = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\045.mp3")
      pygame.mixer.music.play()
      speechtest_106_window.destroy()
      show_speechtest_491_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_106tospeechtest_491():
      global Q
      Q = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\045.mp3")
      pygame.mixer.music.play()
      speechtest_106_window.destroy()
      show_speechtest_491_page()

     speechtest_106_true_button = tk.Button(speechtest_106_window, text="1 0 6", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_106tospeechtest_491)
     speechtest_208_false_button  = tk.Button(speechtest_106_window, text="2 0 8", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_106tospeechtest_491)
     speechtest_308_false_button  = tk.Button(speechtest_106_window, text="3 0 8", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_106tospeechtest_491)
     speechtest_402_false_button  = tk.Button(speechtest_106_window, text="4 0 2", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_106tospeechtest_491)

     speechtest_208_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_308_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_402_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_106_true_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_106_window.mainloop()

  # speechtest_491 page
  def show_speechtest_491_page():
     speechtest_491_window = tk.Toplevel()
     speechtest_491_window.geometry("800x480")
     speechtest_491_window.resizable(False, False)
     speechtest_491_window.title("speechtest_491")

     def calculate_and_displaygeneralresultsleft():
       total = A1 + B1 + C1  + D1 + E1 + F1
       if -1 < total <= 12:
         display_pageleft(1)
       elif 12 < total <= 24:
         display_pageleft(2)
       elif 24 < total <= 42:
         display_pageleft(3)
       elif 42 < total <=54:
         display_pageleft(4)
       else:
         print("total out of range") 

     def display_pageleft(page_number):
        if page_number == 1:
          normal_general_windowLEFT = tk.Toplevel()
          normal_general_windowLEFT.geometry("800x480")
          normal_general_windowLEFT.resizable(False, False)
          normal_general_windowLEFT.title("normal_general")

          def opennormal_resultsleft():
            normal_general_windowLEFT.destroy()
            show_results_page()

          normal_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\LEFTNORMAL.png")
          normal_general_label = tk.Label(normal_general_windowLEFT, image=normal_general_img)
          normal_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_normal_button = tk.Button(normal_general_windowLEFT, text="GET DETAILED RESULTS", font=("Comic Sans MS Bold", 18), bg="#008000", fg="white",activebackground="#008000",activeforeground="white",highlightthickness=0,bd=0,command=opennormal_resultsleft)
          getdetailedresults_normal_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          normal_general_windowLEFT.mainloop()
          print("Displaying normal results")

        elif page_number == 2:
          mild_general_windowLEFT = tk.Toplevel()
          mild_general_windowLEFT.geometry("800x480")
          mild_general_windowLEFT.resizable(False, False)
          mild_general_windowLEFT.title("mild_general")

          def openmild_resultsleft():
            mild_general_windowLEFT.destroy()
            show_results_page()

          mild_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\LEFTMILD.png")
          mild_general_label = tk.Label(mild_general_windowLEFT, image=mild_general_img)
          mild_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_mild_button = tk.Button(mild_general_windowLEFT, text="GET DETAILED RESULTS", font=("Comic Sans MS Bold", 18), bg="#6AC66B", fg="white",activebackground="#6AC66B",activeforeground="white",highlightthickness=0,bd=0,command=openmild_resultsleft)
          getdetailedresults_mild_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          mild_general_windowLEFT.mainloop()
          print("Displaying mild results")
        
        elif page_number == 3:
          moderate_general_windowLEFT = tk.Toplevel()
          moderate_general_windowLEFT.geometry("800x480")
          moderate_general_windowLEFT.resizable(False, False)
          moderate_general_windowLEFT.title("moderate_general")

          def openmoderate_resultsleft():
            moderate_general_windowLEFT.destroy()
            show_results_page()

          moderate_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\LEFTMODERATE.png")
          moderate_general_label = tk.Label(moderate_general_windowLEFT, image=moderate_general_img)
          moderate_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_moderate_button = tk.Button(moderate_general_windowLEFT, text="GET DETAILED RESULTS", font=("Comic Sans MS Bold", 18), bg="#FFCC4D", fg="white",activebackground="#FFCC4D",activeforeground="white",highlightthickness=0,bd=0,command=openmoderate_resultsleft)
          getdetailedresults_moderate_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          moderate_general_windowLEFT.mainloop()
          print("Displaying moderate results")
         
        
        elif page_number == 4:
          severe_general_windowLEFT = tk.Toplevel()
          severe_general_windowLEFT.geometry("800x480")
          severe_general_windowLEFT.resizable(False, False)
          severe_general_windowLEFT.title("severe_general")

          def opensevere_resultsleft():
            severe_general_windowLEFT.destroy()
            show_results_page()
          
          severe_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\LEFTSERVER.png")
          severe_general_label = tk.Label(severe_general_windowLEFT, image=severe_general_img)
          severe_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_severe_button = tk.Button(severe_general_windowLEFT, text="GET DETAILED RESULTS", font=("Comic Sans MS Bold", 18), bg="#BC1823", fg="white",activebackground="#BC1823",activeforeground="white",highlightthickness=0,bd=0,command=opensevere_resultsleft)
          getdetailedresults_severe_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          severe_general_windowLEFT.mainloop()
          print("Displaying severe results")

     def display_page(page_number):
        if page_number == 1:
          speechtest_491_window.destroy()
          normal_general_window = tk.Toplevel()
          normal_general_window.geometry("800x480")
          normal_general_window.resizable(False, False)
          normal_general_window.title("normal_general")

          def opennormal_results():
            normal_general_window.destroy()
            calculate_and_displaygeneralresultsleft()

          normal_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\RIGHTNORMAL.png")
          normal_general_label = tk.Label(normal_general_window, image=normal_general_img)
          normal_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_normal_button = tk.Button(normal_general_window, text="GET LEFT EAR RESULTS", font=("Comic Sans MS Bold", 18), bg="#008000", fg="white",activebackground="#008000",activeforeground="white",highlightthickness=0,bd=0,command=opennormal_results)
          getdetailedresults_normal_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          normal_general_window.mainloop()
          print("Displaying normal results")

        elif page_number == 2:
          speechtest_491_window.destroy()
          mild_general_window = tk.Toplevel()
          mild_general_window.geometry("800x480")
          mild_general_window.resizable(False, False)
          mild_general_window.title("mild_general")

          def openmild_results():
            mild_general_window.destroy()
            calculate_and_displaygeneralresultsleft()

          mild_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\RIGHTMILD.png")
          mild_general_label = tk.Label(mild_general_window, image=mild_general_img)
          mild_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_mild_button = tk.Button(mild_general_window, text="GET LEFT EAR RESULTS", font=("Comic Sans MS Bold", 18), bg="#6AC66B", fg="white",activebackground="#6AC66B",activeforeground="white",highlightthickness=0,bd=0,command=openmild_results)
          getdetailedresults_mild_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          mild_general_window.mainloop()
          print("Displaying mild results")
        
        elif page_number == 3:
          speechtest_491_window.destroy()
          moderate_general_window = tk.Toplevel()
          moderate_general_window.geometry("800x480")
          moderate_general_window.resizable(False, False)
          moderate_general_window.title("moderate_general")

          def openmoderate_results():
            moderate_general_window.destroy()
            calculate_and_displaygeneralresultsleft()

          moderate_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\RIGHTMODERATE.png")
          moderate_general_label = tk.Label(moderate_general_window, image=moderate_general_img)
          moderate_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_moderate_button = tk.Button(moderate_general_window, text="GET LEFT EAR RESULTS", font=("Comic Sans MS Bold", 18), bg="#FFCC4D", fg="white",activebackground="#FFCC4D",activeforeground="white",highlightthickness=0,bd=0,command=openmoderate_results)
          getdetailedresults_moderate_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          moderate_general_window.mainloop()
          print("Displaying moderate results")
         
        
        elif page_number == 4:
          speechtest_491_window.destroy()
          severe_general_window = tk.Toplevel()
          severe_general_window.geometry("800x480")
          severe_general_window.resizable(False, False)
          severe_general_window.title("severe_general")

          def opensevere_results():
            severe_general_window.destroy()
            calculate_and_displaygeneralresultsleft()
          
          severe_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\RIGHTSERVER.png")
          severe_general_label = tk.Label(severe_general_window, image=severe_general_img)
          severe_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_severe_button = tk.Button(severe_general_window, text="GET LEFT EAR RESULTS", font=("Comic Sans MS Bold", 18), bg="#BC1823", fg="white",activebackground="#BC1823",activeforeground="white",highlightthickness=0,bd=0,command=opensevere_results)
          getdetailedresults_severe_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          severe_general_window.mainloop()
          print("Displaying severe results") 

     R=None

     def calculate_and_displaygeneralresultsTRUE():
       global R
       R=1
       global total
       total = A + B + C  + D + E + F
       if -1 < total <= 12:
         display_page(1)
       elif 12 < total <= 24:
         display_page(2)
       elif 24 < total <= 42:
         display_page(3)
       elif 42 < total <=54:
         display_page(4)
       else:
         print("total out of range") 

     def calculate_and_displaygeneralresultsFALSE():
       global R
       R=0
       global total
       total = A + B + C + D + E + F
       if -1 < total <= 12:
         display_page(1)
       elif 12 < total <= 24:
         display_page(2)
       elif 24 < total <= 42:
         display_page(3)
       elif 42 < total <=54:
         display_page(4)
       else:
         print("total out of range") 
      
     speechtest_491_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speech.png")
     speechtest_491_label = tk.Label(speechtest_491_window, image=speechtest_491_img)
     speechtest_491_label.place(x=0, y=0, relwidth=1, relheight=1)


     speechtest_491_true_button = tk.Button(speechtest_491_window, text="0 4 5", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0,command=calculate_and_displaygeneralresultsTRUE)
     speechtest_246_false_button  = tk.Button(speechtest_491_window, text="2 4 6", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0,command=calculate_and_displaygeneralresultsFALSE)
     speechtest_297_false_button  = tk.Button(speechtest_491_window, text="0 9 7", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0,command=calculate_and_displaygeneralresultsFALSE)
     speechtest_389_false_button  = tk.Button(speechtest_491_window, text="3 8 9", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0,command=calculate_and_displaygeneralresultsFALSE)

     speechtest_246_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_297_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_389_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_491_true_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_491_window.mainloop()
   
   #RESULTS PAGE
  def show_results_page():
    results_window = tk.Toplevel()
    results_window.geometry("800x480")
    results_window.resizable(False, False)
    results_window.title("results")

    def open_homefromresults():
      results_window.destroy()
      home2()

    def openlearnmore():
      results_window.destroy()
      show_learnmore_page()
     
    speechsum = G + H + I + J + K + L + M + N + O + P + Q + R
    speechavg = (speechsum / 12)*100
    print("speechsum is ",speechsum)
    print("speechavg is ",speechavg)

    results_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\results.png")
    results_label = tk.Label( results_window, image= results_img)
    results_label.place(x=0, y=0, relwidth=1, relheight=1)

    speechsum_label = tk.Label(results_window, text=f"{speechsum}", font=("Comic Sans MS Bold", 9), fg="#BF56CB", bg="white" ,borderwidth=0)
    speechsum_label.place(x=600,y=319,relwidth=0.024,relheight=0.05)

    speechaverage_label = tk.Label(results_window, text=f"{speechavg:.2f}%", font=("Comic Sans MS Bold", 24), fg="#BF56CB", bg="white",borderwidth=0)
    speechaverage_label.place(x=555,y=265,relwidth=0.22,relheight=0.1)

    global total1
    total1 = A + B + C + D + E + F 
    if -1 < total1 <= 12:
       total1_label = tk.Label(results_window, text="NO HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#008000", bg="white" ,borderwidth=0)
       total1_label.place(x=555,y=125,relwidth=0.22,relheight=0.028)
    elif 12 < total1 <= 24:
       total1_label = tk.Label(results_window, text="MILD HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#6AC66B", bg="white" ,borderwidth=0)
       total1_label.place(x=555,y=125,relwidth=0.22,relheight=0.028)
    elif 24 < total1 <= 42:
       total1_label = tk.Label(results_window, text="MODERATE HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#FFCC4D", bg="white" ,borderwidth=0)
       total1_label.place(x=546,y=125,relwidth=0.25,relheight=0.028)
    elif 42 < total1 <=54:
       total1_label = tk.Label(results_window, text="SEVERE HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#BC1823", bg="white" ,borderwidth=0)
       total1_label.place(x=555,y=125,relwidth=0.22,relheight=0.028)
    else:
         print("total out of range") 

    global total2
    total2 = A1 + B1 + C1 + D1 + E1 + F1 
    if -1 < total2 <= 12:
       total2_label = tk.Label(results_window, text="NO HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#008000", bg="white" ,borderwidth=0)
       total2_label.place(x=555,y=179,relwidth=0.22,relheight=0.028)
    elif 12 < total2 <= 24:
       total2_label = tk.Label(results_window, text="MILD HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#6AC66B", bg="white" ,borderwidth=0)
       total2_label.place(x=555,y=179,relwidth=0.22,relheight=0.028)
    elif 24 < total2 <= 42:
       total2_label2 = tk.Label(results_window, text="MODERATE HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#FFCC4D", bg="white" ,borderwidth=0)
       total2_label2.place(x=546,y=179,relwidth=0.25,relheight=0.028)
    elif 42 < total2 <=54:
       total2_label = tk.Label(results_window, text="SEVERE HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#BC1823", bg="white" ,borderwidth=0)
       total2_label.place(x=555,y=179,relwidth=0.22,relheight=0.028)
    else:
         print("total out of range") 

    folder_name = r"C:\Users\prasa\OneDrive\Documents\audiogram_pdfs"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
   
    file_name = f"{name}_audiogram.pdf"
    pdf_path = os.path.join(folder_name, file_name)
    canvas = Canvas(pdf_path)
    c = Canvas(pdf_path, pagesize=letter)
   
    c.drawString(100, 750, f"Name: {name}")
    c.drawString(100, 730, f"Age: {age}")
    c.drawString(100, 710, f"Gender: {gender}")
    c.drawString(260, 685, "AUDIOGRAM")

    x_values = [250, 500, 1000, 2000, 4000, 8000]
    y_values = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    right=[A*10,B*10,C*10,D*10,E*10,F*10]
    left=[A1*10,B1*10,C1*10,D1*10,E1*10,F1*10]

    plt.clf()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Hearing Threshold (dB)')

    plt.plot(x_values, [20]*len(x_values), color='#008000')
    plt.plot(x_values, [40]*len(x_values), color='#6AC66B')
    plt.plot(x_values, [70]*len(x_values), color='#FFCC4D')
    plt.plot(x_values, [80]*len(x_values), color='#BC1823')
    plt.plot(x_values, right, marker='o',label='Right Ear', linestyle='-', color='#BF56CB')
    plt.plot(x_values, left, marker='o',label='Left Ear', linestyle='-', color='#F15395')
    
    plt.xscale('log')
    plt.xticks([250, 500, 1000, 2000, 4000, 8000], [250, 500, 1000, 2000, 4000, 8000])
    plt.yticks(y_values)
    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
    plt.legend()

    plot_path = "temp_graph.png"
    plt.savefig(plot_path)

    c.drawImage(plot_path, 100, 380, width=400, height=300)

    data = [["", "0dB", "10dB", "20dB", "30dB", "40dB", "50dB", "60dB", "70dB", "80dB"],
        ["250Hz", "", "", "", "", "", "", "", "", ""],
        ["500Hz", "", "", "", "", "", "", "", "", ""],
        ["1000Hz", "", "", "", "", "", "", "", "", ""],
        ["2000Hz", "", "", "", "", "", "", "", "", ""], 
        ["4000Hz", "", "", "", "", "", "", "", "", ""],
        ["8000Hz", "", "", "", "", "", "", "", "", ""]]
    
    if A == 0:
      data[1][1] = "✓"
      for i in range(2, len(data[1])):
        data[1][i] = "-"
    elif A == 1:   
      data[1][2] = "✓"
      for i in range(3, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 2):
        data[1][i] = "x"
    elif A == 2:  
     data[1][3] = "✓"
     for i in range(4, len(data[1])):
        data[1][i] = "-"
     for i in range(1, 3):
        data[1][i] = "x"
    elif A == 3:
     data[1][4] = "✓"
     for i in range(5, len(data[1])):
        data[1][i] = "-"
     for i in range(1, 4):
        data[1][i] = "x"  
    elif A == 4:
      data[1][5] = "✓"
      for i in range(6, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 5):
        data[1][i] = "x"
    elif A == 5:
      data[1][6] = "✓"
      for i in range(7, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 6):
        data[1][i] = "x"  
    elif A == 6:
      data[1][7] = "✓"
      for i in range(8, len(data[1])):
        data[1][i] = "-"   
      for i in range(1, 7):
        data[1][i] = "x"
    elif A == 7:
      data[1][8] = "✓"
      for i in range(9, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 8):
        data[1][i] = "x"
    elif A == 8:
      data[1][9] = "✓"
      for i in range(10, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 9):
        data[1][i] = "x"

    if B == 0:
      data[2][1] = "✓"
      for i in range(2, len(data[2])):
        data[2][i] = "-"
    elif B == 1:   
      data[2][2] = "✓"
      for i in range(3, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 2):
        data[2][i] = "x"
    elif B == 2:  
     data[2][3] = "✓"
     for i in range(4, len(data[2])):
        data[2][i] = "-"
     for i in range(1, 3):
        data[2][i] = "x"
    elif B == 3:
     data[2][4] = "✓"
     for i in range(5, len(data[2])):
        data[2][i] = "-"
     for i in range(1, 4):
        data[2][i] = "x"  
    elif B == 4:
      data[2][5] = "✓"
      for i in range(6, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 5):
        data[2][i] = "x"
    elif B == 5:
      data[2][6] = "✓"
      for i in range(7, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 6):
        data[2][i] = "x"  
    elif B == 6:
      data[2][7] = "✓"
      for i in range(8, len(data[2])):
        data[2][i] = "-"   
      for i in range(1, 7):
        data[2][i] = "x"
    elif B == 7:
      data[2][8] = "✓"
      for i in range(9, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 8):
        data[2][i] = "x"
    elif B == 8:
      data[2][9] = "✓"
      for i in range(10, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 9):
        data[2][i] = "x"

    if C == 0:
      data[3][1] = "✓"
      for i in range(2, len(data[3])):
        data[3][i] = "-"
    elif C == 1:   
      data[3][2] = "✓"
      for i in range(3, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 2):
        data[3][i] = "x"
    elif C == 2:  
     data[3][3] = "✓"
     for i in range(4, len(data[3])):
        data[3][i] = "-"
     for i in range(1, 3):
        data[3][i] = "x"
    elif C == 3:
     data[3][4] = "✓"
     for i in range(5, len(data[3])):
        data[3][i] = "-"
     for i in range(1, 4):
        data[3][i] = "x"  
    elif C == 4:
      data[3][5] = "✓"
      for i in range(6, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 5):
        data[3][i] = "x"
    elif C == 5:
      data[3][6] = "✓"
      for i in range(7, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 6):
        data[3][i] = "x"  
    elif C == 6:
      data[3][7] = "✓"
      for i in range(8, len(data[3])):
        data[3][i] = "-"   
      for i in range(1, 7):
        data[3][i] = "x"
    elif C == 7:
      data[3][8] = "✓"
      for i in range(9, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 8):
        data[3][i] = "x"
    elif C == 8:
      data[3][9] = "✓"
      for i in range(10, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 9):
        data[3][i] = "x"

    if D == 0:
      data[4][1] = "✓"
      for i in range(2, len(data[4])):
        data[4][i] = "-"
    elif D == 1:   
      data[4][2] = "✓"
      for i in range(3, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 2):
        data[4][i] = "x"
    elif D == 2:  
     data[4][3] = "✓"
     for i in range(4, len(data[4])):
        data[4][i] = "-"
     for i in range(1, 3):
        data[4][i] = "x"
    elif D == 3:
     data[4][4] = "✓"
     for i in range(5, len(data[4])):
        data[4][i] = "-"
     for i in range(1, 4):
        data[4][i] = "x"  
    elif D == 4:
      data[4][5] = "✓"
      for i in range(6, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 5):
        data[4][i] = "x"
    elif D == 5:
      data[4][6] = "✓"
      for i in range(7, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 6):
        data[4][i] = "x"  
    elif D == 6:
      data[4][7] = "✓"
      for i in range(8, len(data[4])):
        data[4][i] = "-"   
      for i in range(1, 7):
        data[4][i] = "x"
    elif D == 7:
      data[4][8] = "✓"
      for i in range(9, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 8):
        data[4][i] = "x"
    elif D == 8:
      data[4][9] = "✓"
      for i in range(10, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 9):
        data[4][i] = "x"

    if E == 0:
      data[5][1] = "✓"
      for i in range(2, len(data[5])):
        data[5][i] = "-"
    elif E == 1:   
      data[5][2] = "✓"
      for i in range(3, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 2):
        data[5][i] = "x"
    elif E == 2:  
     data[5][3] = "✓"
     for i in range(4, len(data[5])):
        data[5][i] = "-"
     for i in range(1, 3):
        data[5][i] = "x"
    elif E == 3:
     data[5][4] = "✓"
     for i in range(5, len(data[5])):
        data[5][i] = "-"
     for i in range(1, 4):
        data[5][i] = "x"  
    elif E == 4:
      data[5][5] = "✓"
      for i in range(6, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 5):
        data[5][i] = "x"
    elif E == 5:
      data[5][6] = "✓"
      for i in range(7, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 6):
        data[5][i] = "x"  
    elif E == 6:
      data[5][7] = "✓"
      for i in range(8, len(data[5])):
        data[5][i] = "-"   
      for i in range(1, 7):
        data[5][i] = "x"
    elif E == 7:
      data[5][8] = "✓"
      for i in range(9, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 8):
        data[5][i] = "x"
    elif E == 8:
      data[5][9] = "✓"
      for i in range(10, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 9):
        data[5][i] = "x"

    if F == 0:
      data[6][1] = "✓"
      for i in range(2, len(data[6])):
        data[6][i] = "-"
    elif F == 1:   
      data[6][2] = "✓"
      for i in range(3, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 2):
        data[6][i] = "x"
    elif F == 2:  
     data[6][3] = "✓"
     for i in range(4, len(data[6])):
        data[6][i] = "-"
     for i in range(1, 3):
        data[6][i] = "x"
    elif F == 3:
     data[6][4] = "✓"
     for i in range(5, len(data[6])):
        data[6][i] = "-"
     for i in range(1, 4):
        data[6][i] = "x"  
    elif F == 4:
      data[6][5] = "✓"
      for i in range(6, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 5):
        data[6][i] = "x"
    elif F == 5:
      data[6][6] = "✓"
      for i in range(7, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 6):
        data[6][i] = "x"  
    elif F == 6:
      data[6][7] = "✓"
      for i in range(8, len(data[6])):
        data[6][i] = "-"   
      for i in range(1, 7):
        data[6][i] = "x"
    elif F == 7:
      data[6][8] = "✓"
      for i in range(9, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 8):
        data[6][i] = "x"
    elif F == 8:
      data[6][9] = "✓"
      for i in range(10, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 9):
        data[6][i] = "x"
     
    colWidths = [100, 40, 40, 40, 40, 40, 40, 40, 40, 40]

    c.drawString(100, 350, "RIGHT EAR")
    for col in range(1, len(data[0])):
     c.drawString(100 + sum(colWidths[:col]), 350, str(data[0][col]))

    for row in range(1, len(data)):
     c.drawString(100, 350 - (row+1)*20, str(data[row][0]))
     for col in range(1, len(data[row])):
        c.drawString(100 + sum(colWidths[:col]), 350 - (row+1)*20, str(data[row][col]))

    data = [["", "0dB", "10dB", "20dB", "30dB", "40dB", "50dB", "60dB", "70dB", "80dB"],
        ["250Hz", "", "", "", "", "", "", "", "", ""],
        ["500Hz", "", "", "", "", "", "", "", "", ""],
        ["1000Hz", "", "", "", "", "", "", "", "", ""],
        ["2000Hz", "", "", "", "", "", "", "", "", ""], 
        ["4000Hz", "", "", "", "", "", "", "", "", ""],
        ["8000Hz", "", "", "", "", "", "", "", "", ""]]
    
    if A1 == 0:
      data[1][1] = "✓"
      for i in range(2, len(data[1])):
        data[1][i] = "-"
    elif A1 == 1:   
      data[1][2] = "✓"
      for i in range(3, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 2):
        data[1][i] = "x"
    elif A1 == 2:  
     data[1][3] = "✓"
     for i in range(4, len(data[1])):
        data[1][i] = "-"
     for i in range(1, 3):
        data[1][i] = "x"
    elif A1 == 3:
     data[1][4] = "✓"
     for i in range(5, len(data[1])):
        data[1][i] = "-"
     for i in range(1, 4):
        data[1][i] = "x"  
    elif A1 == 4:
      data[1][5] = "✓"
      for i in range(6, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 5):
        data[1][i] = "x"
    elif A1 == 5:
      data[1][6] = "✓"
      for i in range(7, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 6):
        data[1][i] = "x"  
    elif A1 == 6:
      data[1][7] = "✓"
      for i in range(8, len(data[1])):
        data[1][i] = "-"   
      for i in range(1, 7):
        data[1][i] = "x"
    elif A1 == 7:
      data[1][8] = "✓"
      for i in range(9, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 8):
        data[1][i] = "x"
    elif A1 == 8:
      data[1][9] = "✓"
      for i in range(10, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 9):
        data[1][i] = "x"

    if B1 == 0:
      data[2][1] = "✓"
      for i in range(2, len(data[2])):
        data[2][i] = "-"
    elif B1 == 1:   
      data[2][2] = "✓"
      for i in range(3, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 2):
        data[2][i] = "x"
    elif B1 == 2:  
     data[2][3] = "✓"
     for i in range(4, len(data[2])):
        data[2][i] = "-"
     for i in range(1, 3):
        data[2][i] = "x"
    elif B1 == 3:
     data[2][4] = "✓"
     for i in range(5, len(data[2])):
        data[2][i] = "-"
     for i in range(1, 4):
        data[2][i] = "x"  
    elif B1 == 4:
      data[2][5] = "✓"
      for i in range(6, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 5):
        data[2][i] = "x"
    elif B1 == 5:
      data[2][6] = "✓"
      for i in range(7, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 6):
        data[2][i] = "x"  
    elif B1 == 6:
      data[2][7] = "✓"
      for i in range(8, len(data[2])):
        data[2][i] = "-"   
      for i in range(1, 7):
        data[2][i] = "x"
    elif B1 == 7:
      data[2][8] = "✓"
      for i in range(9, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 8):
        data[2][i] = "x"
    elif B1 == 8:
      data[2][9] = "✓"
      for i in range(10, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 9):
        data[2][i] = "x"

    if C1 == 0:
      data[3][1] = "✓"
      for i in range(2, len(data[3])):
        data[3][i] = "-"
    elif C1 == 1:   
      data[3][2] = "✓"
      for i in range(3, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 2):
        data[3][i] = "x"
    elif C1 == 2:  
     data[3][3] = "✓"
     for i in range(4, len(data[3])):
        data[3][i] = "-"
     for i in range(1, 3):
        data[3][i] = "x"
    elif C1 == 3:
     data[3][4] = "✓"
     for i in range(5, len(data[3])):
        data[3][i] = "-"
     for i in range(1, 4):
        data[3][i] = "x"  
    elif C1 == 4:
      data[3][5] = "✓"
      for i in range(6, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 5):
        data[3][i] = "x"
    elif C1 == 5:
      data[3][6] = "✓"
      for i in range(7, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 6):
        data[3][i] = "x"  
    elif C1 == 6:
      data[3][7] = "✓"
      for i in range(8, len(data[3])):
        data[3][i] = "-"   
      for i in range(1, 7):
        data[3][i] = "x"
    elif C1 == 7:
      data[3][8] = "✓"
      for i in range(9, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 8):
        data[3][i] = "x"
    elif C1 == 8:
      data[3][9] = "✓"
      for i in range(10, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 9):
        data[3][i] = "x"

    if D1 == 0:
      data[4][1] = "✓"
      for i in range(2, len(data[4])):
        data[4][i] = "-"
    elif D1 == 1:   
      data[4][2] = "✓"
      for i in range(3, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 2):
        data[4][i] = "x"
    elif D1 == 2:  
     data[4][3] = "✓"
     for i in range(4, len(data[4])):
        data[4][i] = "-"
     for i in range(1, 3):
        data[4][i] = "x"
    elif D1 == 3:
     data[4][4] = "✓"
     for i in range(5, len(data[4])):
        data[4][i] = "-"
     for i in range(1, 4):
        data[4][i] = "x"  
    elif D1 == 4:
      data[4][5] = "✓"
      for i in range(6, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 5):
        data[4][i] = "x"
    elif D1 == 5:
      data[4][6] = "✓"
      for i in range(7, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 6):
        data[4][i] = "x"  
    elif D1 == 6:
      data[4][7] = "✓"
      for i in range(8, len(data[4])):
        data[4][i] = "-"   
      for i in range(1, 7):
        data[4][i] = "x"
    elif D1 == 7:
      data[4][8] = "✓"
      for i in range(9, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 8):
        data[4][i] = "x"
    elif D1 == 8:
      data[4][9] = "✓"
      for i in range(10, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 9):
        data[4][i] = "x"

    if E1 == 0:
      data[5][1] = "✓"
      for i in range(2, len(data[5])):
        data[5][i] = "-"
    elif E1 == 1:   
      data[5][2] = "✓"
      for i in range(3, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 2):
        data[5][i] = "x"
    elif E1 == 2:  
     data[5][3] = "✓"
     for i in range(4, len(data[5])):
        data[5][i] = "-"
     for i in range(1, 3):
        data[5][i] = "x"
    elif E1 == 3:
     data[5][4] = "✓"
     for i in range(5, len(data[5])):
        data[5][i] = "-"
     for i in range(1, 4):
        data[5][i] = "x"  
    elif E1 == 4:
      data[5][5] = "✓"
      for i in range(6, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 5):
        data[5][i] = "x"
    elif E1 == 5:
      data[5][6] = "✓"
      for i in range(7, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 6):
        data[5][i] = "x"  
    elif E1 == 6:
      data[5][7] = "✓"
      for i in range(8, len(data[5])):
        data[5][i] = "-"   
      for i in range(1, 7):
        data[5][i] = "x"
    elif E1 == 7:
      data[5][8] = "✓"
      for i in range(9, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 8):
        data[5][i] = "x"
    elif E1 == 8:
      data[5][9] = "✓"
      for i in range(10, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 9):
        data[5][i] = "x"

    if F1 == 0:
      data[6][1] = "✓"
      for i in range(2, len(data[6])):
        data[6][i] = "-"
    elif F1 == 1:   
      data[6][2] = "✓"
      for i in range(3, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 2):
        data[6][i] = "x"
    elif F1 == 2:  
     data[6][3] = "✓"
     for i in range(4, len(data[6])):
        data[6][i] = "-"
     for i in range(1, 3):
        data[6][i] = "x"
    elif F1 == 3:
     data[6][4] = "✓"
     for i in range(5, len(data[6])):
        data[6][i] = "-"
     for i in range(1, 4):
        data[6][i] = "x"  
    elif F1 == 4:
      data[6][5] = "✓"
      for i in range(6, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 5):
        data[6][i] = "x"
    elif F1 == 5:
      data[6][6] = "✓"
      for i in range(7, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 6):
        data[6][i] = "x"  
    elif F1 == 6:
      data[6][7] = "✓"
      for i in range(8, len(data[6])):
        data[6][i] = "-"   
      for i in range(1, 7):
        data[6][i] = "x"
    elif F1 == 7:
      data[6][8] = "✓"
      for i in range(9, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 8):
        data[6][i] = "x"
    elif F1 == 8:
      data[6][9] = "✓"
      for i in range(10, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 9):
        data[6][i] = "x"
     
    colWidths = [100, 40, 40, 40, 40, 40, 40, 40, 40, 40]

    c.drawString(100, 160, "LEFT EAR")
    for col in range(1, len(data[0])):
     c.drawString(100 + sum(colWidths[:col]), 160, str(data[0][col]))

    for row in range(1, len(data)):
     c.drawString(100, 160 - (row+1)*20, str(data[row][0]))
     for col in range(1, len(data[row])):
        c.drawString(100 + sum(colWidths[:col]), 160 - (row+1)*20, str(data[row][col]))
   
    c.save()

    os.remove(plot_path)

    def open_pdf():
     os.startfile(pdf_path)

    canvas = FigureCanvasTkAgg(plt.gcf(), master=results_window)
    canvas.draw()
    canvas.get_tk_widget().place(x=95,y=124, relwidth=0.5, relheight=0.5)

    global total3
    total3 = A + B + C + D + E + F 
    if 48 < total3:
       total3_label = tk.Label(results_window, text="HEARING THRESHOLDS ARE OUT OF THE TESTED RANGE", font=("Comic Sans MS Bold", 9), fg="#BC1823", bg="white" ,borderwidth=0)
       total3_label.place(x=80,y=362,relwidth=0.48,relheight=0.028)
    
    global total4
    total4 = A1 + B1 + C1 + D1 + E1 + F1 
    if 48 < total4:
       total4_label = tk.Label(results_window, text="HEARING THRESHOLDS ARE OUT OF THE TESTED RANGE", font=("Comic Sans MS Bold", 9), fg="#BC1823", bg="white" ,borderwidth=0)
       total4_label.place(x=80,y=362,relwidth=0.48,relheight=0.028)

    resultsLEARNMORE_button = tk.Button(results_window, text="LEARN MORE", font=("Comic Sans MS Bold", 16), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0,command=openlearnmore)
    resultsLEARNMORE_button.place(x=98, y=418, relwidth=0.18, relheight=0.07)

    resultstohome_button = tk.Button(results_window, text="HOME", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0,command=open_homefromresults)
    resultstohome_button.place(x=330, y=417, relwidth=0.16, relheight=0.07)

    print_results_button = tk.Button(results_window, text="PRINT RESULTS", font=("Comic Sans MS Bold", 14), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0,command=open_pdf)
    print_results_button.place(x=531, y=418, relwidth=0.194, relheight=0.07)

    results_window.mainloop()

  def show_learnmore_page():
    learnmore_window = tk.Toplevel()
    learnmore_window.geometry("800x480")
    learnmore_window.resizable(False, False)
    learnmore_window.title("learn more")

    def open_homefromlearnmore():
      learnmore_window.destroy()
      home2()

    learnmore_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\learnmore.png")
    learnmore_label = tk.Label( learnmore_window, image= learnmore_img)
    learnmore_label.place(x=0, y=0, relwidth=1, relheight=1)

    learnmoretohome_button = tk.Button(learnmore_window, text="HOME", font=("Comic Sans MS Bold", 21), bg="#BF56CB", fg="white",activebackground="#BF56CB",activeforeground="white",highlightthickness=0,bd=0,command=open_homefromlearnmore)
    learnmoretohome_button.place(x=350, y=412, relwidth=0.16, relheight=0.07)

    learnmore_window.mainloop()

   # Home page
  def home2():
   select1language = tk.Toplevel()
   select1language.geometry("800x480") 
   select1language.resizable(False, False)
   select1language.title("select1language")

   select1languagebg_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\SELECTLANGUAGE.png")
   select1languagebg_label = tk.Label(select1language, image=select1languagebg_image)
   select1languagebg_label.place(x=0, y=0, relwidth=1, relheight=1)

   def open_english():
    select1language.destroy()
    show_selectmode()

   def open_telugu():
    select1language.destroy()
    show_selectmode()

   def open_hindi():
    select1language.destroy
    show_selectmode()


   select1languagebutton = tk.Button(select1language, text="తెలుగు", font=("Comic Sans MS Bold", 24), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_telugu)
   select1languagebutton.place(x=296, y=178, relwidth=0.28, relheight=0.085)

   select1languagebutton = tk.Button(select1language, text="हिंदी", font=("Comic Sans MS Bold", 24), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_hindi)
   select1languagebutton.place(x=296, y=268, relwidth=0.28, relheight=0.085)

   select1languagebutton = tk.Button(select1language, text="ENGLISH", font=("Comic Sans MS Bold", 24), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_english)
   select1languagebutton.place(x=296, y=358, relwidth=0.28, relheight=0.085)
   select1language.mainloop()

  home.mainloop() 

 def showadult_homeadults(): 
  homeadults = tk.Toplevel()
  homeadults.geometry("800x480") 
  homeadults.resizable(False, False)
  homeadults.title("homeadults")

  homeadultsbg_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\1introadults.png")
  homeadultsbg_label = tk.Label(homeadults, image=homeadultsbg_image)
  homeadultsbg_label.place(x=0, y=0, relwidth=1, relheight=1)

  def openadult_instruction():
    homeadults.destroy()
    showadult_instruction()

  homeadultsbutton = tk.Button(homeadults, text="START TEST", font=("Comic Sans MS Bold", 16), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_instruction)
  homeadultsbutton.place(x=339, y=369, relwidth=0.194, relheight=0.056)

  def showadult_instruction():
   instruction_adultwindow = tk.Toplevel()
   instruction_adultwindow.geometry("800x480")
   instruction_adultwindow.resizable(False, False)
   instruction_adultwindow.title("instruction")
    
   instruction_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\2instructadults.png")
   instruction_label = tk.Label(instruction_adultwindow, image=instruction_img)
   instruction_label.place(x=0, y=0, relwidth=1, relheight=1)
    
   pygame.mixer.init()

   def openadult_loginadults():
     instruction_adultwindow.destroy()
     showadult_loginadults()
    
   instruction_button = tk.Button(instruction_adultwindow, text="CONTINUE", font=("Comic Sans MS Bold", 16), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command= openadult_loginadults)
   instruction_button.place(x=315, y=407, relwidth=0.192, relheight=0.056)
   instruction_adultwindow.mainloop()

  #loginadults page
  def showadult_loginadults():
   loginadults = tk.Toplevel()
   loginadults.title("loginadults")
   loginadults.geometry("800x480")
   loginadults.resizable(False, False)
   loginadults.title("instruction")

   bg_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\loginadults.png")
   background_label = tk.Label(loginadults, image=bg_image)
   background_label.place(relwidth=1, relheight=1)

   def update_entry(char):
        current_entry = loginadults.focus_get()
        if isinstance(current_entry, tk.Entry):
            current_entry.insert(tk.END, char)

   def clear_entry():
        current_entry = loginadults.focus_get()
        if isinstance(current_entry, tk.Entry):
            current_entry.delete(0, tk.END)
  
   def openadult_loginadults():
    global name
    name= name_entry.get()
    global age
    age= age_entry.get()
    global gender
    gender= gender_entry.get()
    pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_0_R.ogg")
    pygame.mixer.music.play()
    loginadults.destroy()
    showadult_r250_0_page()
   
   global name_entry
   name_entry = tk.Entry(loginadults, font=("Comic Sans MS Bold", 13), fg="#428EC2",highlightthickness=0,bd=0)
   name_entry.place(x=365, y=91, relwidth=0.2, relheight=0.051)
   
   global age_entry
   age_entry = tk.Entry(loginadults, font=("Comic Sans MS Bold", 13), fg="#428EC2",highlightthickness=0,bd=0)
   age_entry.place(x=365, y=147, relwidth=0.2, relheight=0.051)

   global gender_entry
   gender_entry = tk.Entry(loginadults, font=("Comic Sans MS Bold", 13), fg="#428EC2",highlightthickness=0,bd=0)
   gender_entry.place(x=365, y=202, relwidth=0.2, relheight=0.051)

   submit_button = tk.Button(loginadults, text="SUBMIT", font=("Comic Sans MS Bold", 16), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0,command=openadult_loginadults)
   submit_button.place(x=355, y=257, relwidth=0.128, relheight=0.051)

   keyboard_frame = tk.Frame(loginadults)
   keyboard_frame.place(x=190, y=310)

   characters = [
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),
        ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'),
        ('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L','Z'),
        ('X', 'C', 'V', 'B', 'N', 'M','.',',',':'),
    ]

   for row, chars in enumerate(characters):
        for col, char in enumerate(chars):
            tk.Button(keyboard_frame, text=char, font=("Comic Sans MS Bold", 12), width=3, bg="#99D1F7", fg="white",activebackground="#99D1F7",activeforeground="white",command=lambda c=char: update_entry(c)).grid(row=row, column=col)

   tk.Button(keyboard_frame, text="Clc", font=("Comic Sans MS Bold", 12), width=3, bg="#99D1F7", fg="white",activebackground="#99D1F7",activeforeground="white", command=clear_entry).grid(row=3,column=9)
   
   loginadults.mainloop()

  # R250_0 page 
  def showadult_r250_0_page():
   r250_0_adultwindow = tk.Toplevel()
   r250_0_adultwindow.geometry("800x480")
   r250_0_adultwindow.resizable(False, False)
   r250_0_adultwindow.title("R250_0")

   def blank1_page():
     r250_0_adultwindow.destroy() 
     showadult_blank1_page()
      
   pygame.mixer.init()

   def playadult_r250_10():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_10_R.ogg")
     pygame.mixer.music.play()
     r250_0_adultwindow.destroy()
     showadult_r250_10_page()

   r250_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
   r250_0_label = tk.Label(r250_0_adultwindow, image=r250_0_img)
   r250_0_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_0_YES_button = tk.Button(r250_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank1_page)
   r250_0_NO_button  = tk.Button(r250_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r250_10)

   r250_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_0_adultwindow.mainloop()

  # blank 1
  def showadult_blank1_page():
   blank1_adultwindow = tk.Toplevel()
   blank1_adultwindow.geometry("800x480")
   blank1_adultwindow.resizable(False, False)
   blank1_adultwindow.title("BLANK1")

   def warning1_page():
     blank1_adultwindow.destroy() 
     showadult_warning1_page()

   pygame.mixer.init()

   A = None

   def playadult_blank1tor500_0():
     global A
     A = 0
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     blank1_adultwindow.destroy()
     showadult_r500_0_page()
     
   blank1_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
   blank1_label = tk.Label(blank1_adultwindow , image=blank1_img)
   blank1_label.place(x=0, y=0, relwidth=1, relheight=1)

   blank1_YES_button = tk.Button(blank1_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning1_page)
   blank1_NO_button= tk.Button(blank1_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank1tor500_0)

   blank1_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   blank1_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)
  
   blank1_adultwindow.mainloop()

  # warning 1
  def showadult_warning1_page():
    warning1_adultwindow = tk.Toplevel()
    warning1_adultwindow.geometry("800x480")
    warning1_adultwindow.resizable(False, False)
    warning1_adultwindow.title("WARNING1")
      
    warning1_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
    warning1_label = tk.Label(warning1_adultwindow, image=warning1_image)
    warning1_label.place(x=0, y=0, relwidth=1, relheight=1)

    pygame.mixer.init()

    def openadult_warning1tor250_0():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_0_R.ogg")
     pygame.mixer.music.play()
     warning1_adultwindow.destroy()
     showadult_r250_0_page()

    warning1_button = tk.Button(warning1_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning1tor250_0)
    warning1_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
    warning1_adultwindow.mainloop()

  # R250_10 page
  def showadult_r250_10_page():
   r250_10_adultwindow = tk.Toplevel()
   r250_10_adultwindow.geometry("800x480")
   r250_10_adultwindow.resizable(False, False)
   r250_10_adultwindow.title("R250_10")

   pygame.mixer.init()

   def playadult_r250_10tor250_20():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_20_R.ogg")
     pygame.mixer.music.play()
     r250_10_adultwindow.destroy()
     showadult_r250_20_page()

   pygame.mixer.init()

   def openadult__r250_10tor500_0():
     global A
     A = 1
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_10_adultwindow.destroy()
     showadult_r500_0_page()

   r250_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
   r250_10_label = tk.Label(r250_10_adultwindow, image=r250_10_img)
   r250_10_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_10_YES_button = tk.Button(r250_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r250_10tor500_0)
   r250_10_NO_button  = tk.Button(r250_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r250_10tor250_20)

   r250_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_10_adultwindow.mainloop()

  # R250_20 page
  def showadult_r250_20_page():
   r250_20_adultwindow = tk.Toplevel()
   r250_20_adultwindow.geometry("800x480")
   r250_20_adultwindow.resizable(False, False)
   r250_20_adultwindow.title("R250_20")

   pygame.mixer.init()

   def playadult_r250_20tor250_30():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_30_R.ogg")
     pygame.mixer.music.play()
     r250_20_adultwindow.destroy()
     showadult_r250_30_page()

   pygame.mixer.init()

   def openadult__r250_20tor500_0():
     global A
     A = 2
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_20_adultwindow.destroy()
     showadult_r500_0_page()

   r250_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
   r250_20_label = tk.Label(r250_20_adultwindow, image=r250_20_img)
   r250_20_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_20_YES_button = tk.Button(r250_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r250_20tor500_0)
   r250_20_NO_button  = tk.Button(r250_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r250_20tor250_30)

   r250_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_20_adultwindow.mainloop()

  # R250_30 page
  def showadult_r250_30_page():
   r250_30_adultwindow = tk.Toplevel()
   r250_30_adultwindow.geometry("800x480")
   r250_30_adultwindow.resizable(False, False)
   r250_30_adultwindow.title("R250_30")

   pygame.mixer.init()

   def playadult_r250_30tor250_40():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_40_R.ogg")
     pygame.mixer.music.play()
     r250_30_adultwindow.destroy()
     showadult_r250_40_page()

   pygame.mixer.init()

   def openadult__r250_30tor500_0():
     global A
     A = 3
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_30_adultwindow.destroy()
     showadult_r500_0_page()

   r250_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
   r250_30_label = tk.Label(r250_30_adultwindow, image=r250_30_img)
   r250_30_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_30_YES_button = tk.Button(r250_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r250_30tor500_0)
   r250_30_NO_button  = tk.Button(r250_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r250_30tor250_40)

   r250_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_30_adultwindow.mainloop()

  # R250_40 page
  def showadult_r250_40_page():
   r250_40_adultwindow = tk.Toplevel()
   r250_40_adultwindow.geometry("800x480")
   r250_40_adultwindow.resizable(False, False)
   r250_40_adultwindow.title("R250_40")

   pygame.mixer.init()

   def playadult_r250_40tor250_50():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_50_R.ogg")
     pygame.mixer.music.play()
     r250_40_adultwindow.destroy()
     showadult_r250_50_page()

   pygame.mixer.init()

   def openadult__r250_40tor500_0():
     global A
     A = 4
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_40_adultwindow.destroy()
     showadult_r500_0_page()

   r250_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
   r250_40_label = tk.Label(r250_40_adultwindow, image=r250_40_img)
   r250_40_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_40_YES_button = tk.Button(r250_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r250_40tor500_0)
   r250_40_NO_button  = tk.Button(r250_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r250_40tor250_50)

   r250_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_40_adultwindow.mainloop()

  # R250_50 page
  def showadult_r250_50_page():
   r250_50_adultwindow = tk.Toplevel()
   r250_50_adultwindow.geometry("800x480")
   r250_50_adultwindow.resizable(False, False)
   r250_50_adultwindow.title("R250_50")

   pygame.mixer.init()

   def playadult_r250_50tor250_60():
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_60_R.ogg")
     pygame.mixer.music.play()
     r250_50_adultwindow.destroy()
     showadult_r250_60_page()

   pygame.mixer.init()

   def openadult__r250_50tor500_0():
     global A
     A = 5
     pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
     pygame.mixer.music.play()
     r250_50_adultwindow.destroy()
     showadult_r500_0_page()

   r250_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
   r250_50_label = tk.Label(r250_50_adultwindow, image=r250_50_img)
   r250_50_label.place(x=0, y=0, relwidth=1, relheight=1)

   r250_50_YES_button = tk.Button(r250_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r250_50tor500_0)
   r250_50_NO_button  = tk.Button(r250_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r250_50tor250_60)

   r250_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
   r250_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

   r250_50_adultwindow.mainloop()

  # R250_60 page
  def showadult_r250_60_page():
    r250_60_adultwindow = tk.Toplevel()
    r250_60_adultwindow.geometry("800x480")
    r250_60_adultwindow.resizable(False, False)
    r250_60_adultwindow.title("R250_60")

    pygame.mixer.init()

    def playadult_r250_60tor250_70():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_70_R.ogg")
       pygame.mixer.music.play()
       r250_60_adultwindow.destroy()
       showadult_r250_70_page()

    pygame.mixer.init()

    def openadult__r250_60tor500_0():
       global A
       A = 6
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
       pygame.mixer.music.play()
       r250_60_adultwindow.destroy()
       showadult_r500_0_page()

    r250_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
    r250_60_label = tk.Label(r250_60_adultwindow, image=r250_60_img)
    r250_60_label.place(x=0, y=0, relwidth=1, relheight=1)

    r250_60_YES_button = tk.Button(r250_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r250_60tor500_0)
    r250_60_NO_button  = tk.Button(r250_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r250_60tor250_70)

    r250_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
    r250_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

    r250_60_adultwindow.mainloop() 

  # R250_70 page
  def showadult_r250_70_page():
     r250_70_adultwindow = tk.Toplevel()
     r250_70_adultwindow.geometry("800x480")
     r250_70_adultwindow.resizable(False, False)
     r250_70_adultwindow.title("R250_70")

     pygame.mixer.init()

     def playadult_r250_70tor250_80():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\250_80_R.ogg")
       pygame.mixer.music.play()
       r250_70_adultwindow.destroy()
       showadult_r250_80_page()

     pygame.mixer.init()

     def openadult__r250_70tor500_0():
       global A
       A = 7
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
       pygame.mixer.music.play()
       r250_70_adultwindow.destroy()
       showadult_r500_0_page()

     r250_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r250_70_label = tk.Label(r250_70_adultwindow, image=r250_70_img)
     r250_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r250_70_YES_button = tk.Button(r250_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r250_70tor500_0)
     r250_70_NO_button  = tk.Button(r250_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r250_70tor250_80)

     r250_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r250_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r250_70_adultwindow.mainloop() 

  # R250_80 page
  def showadult_r250_80_page():
     r250_80_adultwindow = tk.Toplevel()
     r250_80_adultwindow.geometry("800x480")
     r250_80_adultwindow.resizable(False, False)
     r250_80_adultwindow.title("R250_80")

     pygame.mixer.init()

     def playadult_r250_80tor500_0():
       global A
       A = 9
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
       pygame.mixer.music.play()
       r250_80_adultwindow.destroy()
       showadult_r500_0_page()

     pygame.mixer.init()

     def openadult__r250_80tor500_00():
       global A
       A = 8
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
       pygame.mixer.music.play()
       r250_80_adultwindow.destroy()
       showadult_r500_0_page()

     r250_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r250_80_label = tk.Label(r250_80_adultwindow, image=r250_80_img)
     r250_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r250_80_YES_button = tk.Button(r250_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r250_80tor500_00)
     r250_80_NO_button  = tk.Button(r250_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r250_80tor500_0)

     r250_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r250_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r250_80_adultwindow.mainloop()

  # R500_0 page
  def showadult_r500_0_page():
     r500_0_adultwindow = tk.Toplevel()
     r500_0_adultwindow.geometry("800x480")
     r500_0_adultwindow.resizable(False, False)
     r500_0_adultwindow.title("R500_0")

     def blank2_page():
       r500_0_adultwindow.destroy() 
       showadult_blank2_page()
      
     pygame.mixer.init()

     def playadult_r500_10():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_10_R.ogg")
       pygame.mixer.music.play()
       r500_0_adultwindow.destroy()
       showadult_r500_10_page()

     r500_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r500_0_label = tk.Label(r500_0_adultwindow, image=r500_0_img)
     r500_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_0_YES_button = tk.Button(r500_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank2_page)
     r500_0_NO_button  = tk.Button(r500_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r500_10)

     r500_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_0_adultwindow.mainloop()

  # blank 2
  def showadult_blank2_page():
     blank2_adultwindow = tk.Toplevel()
     blank2_adultwindow.geometry("800x480")
     blank2_adultwindow.resizable(False, False)
     blank2_adultwindow.title("blank2")

     def warning2_page():
       blank2_adultwindow.destroy() 
       showadult_warning2_page()

     pygame.mixer.init()
     B= None

     def playadult_blank2tor1000_0():
       global B
       B = 0  
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       blank2_adultwindow.destroy()
       showadult_r1000_0_page()
     
     blank2_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank2_label = tk.Label(blank2_adultwindow , image=blank2_img)
     blank2_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank2_YES_button = tk.Button(blank2_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning2_page)
     blank2_NO_button= tk.Button(blank2_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank2tor1000_0)

     blank2_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank2_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank2_adultwindow.mainloop()

  # warning2
  def showadult_warning2_page():
      warning2_adultwindow = tk.Toplevel()
      warning2_adultwindow.geometry("800x480")
      warning2_adultwindow.resizable(False, False)
      warning2_adultwindow.title("warning2")
      
      warning2_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning2_label = tk.Label(warning2_adultwindow, image=warning2_image)
      warning2_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning2tor500_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_0_R.ogg")
        pygame.mixer.music.play()
        warning2_adultwindow.destroy()
        showadult_r250_0_page()

      warning2_button = tk.Button(warning2_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning2tor500_0)
      warning2_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning2_adultwindow.mainloop()

  # R500_10 page
  def showadult_r500_10_page():
     r500_10_adultwindow = tk.Toplevel()
     r500_10_adultwindow.geometry("800x480")
     r500_10_adultwindow.resizable(False, False)
     r500_10_adultwindow.title("R500_10")

     pygame.mixer.init()

     def playadult_r500_10tor500_20():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_20_R.ogg")
       pygame.mixer.music.play()
       r500_10_adultwindow.destroy()
       showadult_r500_20_page()

     pygame.mixer.init()

     def openadult__r500_10tor1000_0():
       global B
       B = 1
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_10_adultwindow.destroy()
       showadult_r1000_0_page()

     r500_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r500_10_label = tk.Label(r500_10_adultwindow, image=r500_10_img)
     r500_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_10_YES_button = tk.Button(r500_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r500_10tor1000_0)
     r500_10_NO_button  = tk.Button(r500_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r500_10tor500_20)

     r500_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_10_adultwindow.mainloop()

# R500_20 page
  def showadult_r500_20_page():
     r500_20_adultwindow = tk.Toplevel()
     r500_20_adultwindow.geometry("800x480")
     r500_20_adultwindow.resizable(False, False)
     r500_20_adultwindow.title("R500_20")

     pygame.mixer.init()

     def playadult_r500_20tor500_30():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_30_R.ogg")
       pygame.mixer.music.play()
       r500_20_adultwindow.destroy()
       showadult_r500_30_page()

     pygame.mixer.init()

     def openadult__r500_20tor1000_0():
       global B
       B = 2 
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_20_adultwindow.destroy()
       showadult_r1000_0_page()

     r500_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r500_20_label = tk.Label(r500_20_adultwindow, image=r500_20_img)
     r500_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_20_YES_button = tk.Button(r500_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r500_20tor1000_0)
     r500_20_NO_button  = tk.Button(r500_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r500_20tor500_30)

     r500_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_20_adultwindow.mainloop()

  # R500_30 page
  def showadult_r500_30_page():
     r500_30_adultwindow = tk.Toplevel()
     r500_30_adultwindow.geometry("800x480")
     r500_30_adultwindow.resizable(False, False)
     r500_30_adultwindow.title("R500_30")

     pygame.mixer.init()

     def playadult_r500_30tor500_40():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_40_R.ogg")
       pygame.mixer.music.play()
       r500_30_adultwindow.destroy()
       showadult_r500_40_page()

     pygame.mixer.init()

     def openadult__r500_30tor1000_0():
       global B
       B = 3
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_30_adultwindow.destroy()
       showadult_r1000_0_page()

     r500_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r500_30_label = tk.Label(r500_30_adultwindow, image=r500_30_img)
     r500_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_30_YES_button = tk.Button(r500_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r500_30tor1000_0)
     r500_30_NO_button  = tk.Button(r500_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r500_30tor500_40)

     r500_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_30_adultwindow.mainloop()

  # R500_40 page
  def showadult_r500_40_page():
     r500_40_adultwindow = tk.Toplevel()
     r500_40_adultwindow.geometry("800x480")
     r500_40_adultwindow.resizable(False, False)
     r500_40_adultwindow.title("R500_40")

     pygame.mixer.init()

     def playadult_r500_40tor500_50():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_50_R.ogg")
       pygame.mixer.music.play()
       r500_40_adultwindow.destroy()
       showadult_r500_50_page()

     pygame.mixer.init()

     def openadult__r500_40tor1000_0():
       global B
       B = 4
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_40_adultwindow.destroy()
       showadult_r1000_0_page()

     r500_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r500_40_label = tk.Label(r500_40_adultwindow, image=r500_40_img)
     r500_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_40_YES_button = tk.Button(r500_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r500_40tor1000_0)
     r500_40_NO_button  = tk.Button(r500_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r500_40tor500_50)

     r500_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_40_adultwindow.mainloop()

  # R500_50 page
  def showadult_r500_50_page():
     r500_50_adultwindow = tk.Toplevel()
     r500_50_adultwindow.geometry("800x480")
     r500_50_adultwindow.resizable(False, False)
     r500_50_adultwindow.title("R500_50")

     pygame.mixer.init()

     def playadult_r500_50tor500_60():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_60_R.ogg")
       pygame.mixer.music.play()
       r500_50_adultwindow.destroy()
       showadult_r500_60_page()

     pygame.mixer.init()

     def openadult__r500_50tor1000_0():
       global B
       B = 5
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_50_adultwindow.destroy()
       showadult_r1000_0_page()

     r500_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r500_50_label = tk.Label(r500_50_adultwindow, image=r500_50_img)
     r500_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_50_YES_button = tk.Button(r500_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r500_50tor1000_0)
     r500_50_NO_button  = tk.Button(r500_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r500_50tor500_60)

     r500_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_50_adultwindow.mainloop()

  # R500_60 page
  def showadult_r500_60_page():
     r500_60_adultwindow = tk.Toplevel()
     r500_60_adultwindow.geometry("800x480")
     r500_60_adultwindow.title("R500_60")

     pygame.mixer.init()

     def playadult_r500_60tor500_70():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_70_R.ogg")
       pygame.mixer.music.play()
       r500_60_adultwindow.destroy()
       showadult_r500_70_page()

     pygame.mixer.init()

     def openadult__r500_60tor1000_0():
       global B
       B = 6
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_60_adultwindow.destroy()
       showadult_r1000_0_page()

     r500_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r500_60_label = tk.Label(r500_60_adultwindow, image=r500_60_img)
     r500_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_60_YES_button = tk.Button(r500_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r500_60tor1000_0)
     r500_60_NO_button  = tk.Button(r500_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r500_60tor500_70)

     r500_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_60_adultwindow.mainloop()

  # R500_70 page
  def showadult_r500_70_page():
     r500_70_adultwindow = tk.Toplevel()
     r500_70_adultwindow.geometry("800x480")
     r500_70_adultwindow.resizable(False, False)
     r500_70_adultwindow.title("R500_70")

     pygame.mixer.init()

     def playadult_r500_70tor500_80():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\500_80_R.ogg")
       pygame.mixer.music.play()
       r500_70_adultwindow.destroy()
       showadult_r500_80_page()

     pygame.mixer.init()

     def openadult__r500_70tor1000_0():
       global B
       B = 7
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_70_adultwindow.destroy()
       showadult_r1000_0_page()

     r500_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r500_70_label = tk.Label(r500_70_adultwindow, image=r500_70_img)
     r500_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_70_YES_button = tk.Button(r500_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r500_70tor1000_0)
     r500_70_NO_button  = tk.Button(r500_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r500_70tor500_80)

     r500_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_70_adultwindow.mainloop()

  # R500_80 page
  def showadult_r500_80_page():
     r500_80_adultwindow = tk.Toplevel()
     r500_80_adultwindow.geometry("800x480")
     r500_80_adultwindow.resizable(False, False)
     r500_80_adultwindow.title("R500_80")

     pygame.mixer.init()

     def playadult_r500_80tor1000_0():
       global B
       B = 9
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_80_adultwindow.destroy()
       showadult_r1000_0_page()

     pygame.mixer.init()

     def openadult__r500_80tor1000_00():
       global B
       B = 8
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
       pygame.mixer.music.play()
       r500_80_adultwindow.destroy()
       showadult_r1000_0_page()

     r500_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r500_80_label = tk.Label(r500_80_adultwindow, image=r500_80_img)
     r500_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r500_80_YES_button = tk.Button(r500_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r500_80tor1000_00)
     r500_80_NO_button  = tk.Button(r500_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r500_80tor1000_0)

     r500_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r500_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r500_80_adultwindow.mainloop()

  # R1000_0 page
  def showadult_r1000_0_page():
     r1000_0_adultwindow = tk.Toplevel()
     r1000_0_adultwindow.geometry("800x480")
     r1000_0_adultwindow.resizable(False, False)
     r1000_0_adultwindow.title("R1000_0")

     def blank3_page():
       r1000_0_adultwindow.destroy() 
       showadult_blank3_page()
      
     pygame.mixer.init()

     def playadult_r1000_10():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_10_R.ogg")
       pygame.mixer.music.play()
       r1000_0_adultwindow.destroy()
       showadult_r1000_10_page()

     r1000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r1000_0_label = tk.Label(r1000_0_adultwindow, image=r1000_0_img)
     r1000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_0_YES_button = tk.Button(r1000_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank3_page)
     r1000_0_NO_button  = tk.Button(r1000_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r1000_10)

     r1000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_0_adultwindow.mainloop()

  # blank3
  def showadult_blank3_page():
     blank3_adultwindow = tk.Toplevel()
     blank3_adultwindow.geometry("800x480")
     blank3_adultwindow.resizable(False, False)
     blank3_adultwindow.title("blank3")

     def warning3_page():
      blank3_adultwindow.destroy() 
      showadult_warning3_page()

     pygame.mixer.init()
     C = None
     def playadult_blank3tor2000_0():
       global C
       C = 0
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       blank3_adultwindow.destroy()
       showadult_r2000_0_page()
     
     blank3_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank3_label = tk.Label(blank3_adultwindow , image=blank3_img)
     blank3_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank3_YES_button = tk.Button(blank3_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning3_page)
     blank3_NO_button= tk.Button(blank3_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank3tor2000_0)

     blank3_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank3_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank3_adultwindow.mainloop()

  # warning3
  def showadult_warning3_page():
      warning3_adultwindow = tk.Toplevel()
      warning3_adultwindow.geometry("800x480")
      warning3_adultwindow.resizable(False, False)
      warning3_adultwindow.title("warning3")
      
      warning3_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning3_label = tk.Label(warning3_adultwindow, image=warning3_image)
      warning3_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning3tor1000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_0_R.ogg")
        pygame.mixer.music.play()
        warning3_adultwindow.destroy()
        showadult_r250_0_page()

      warning3_button = tk.Button(warning3_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning3tor1000_0)
      warning3_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning3_adultwindow.mainloop()

  # R1000_10 page
  def showadult_r1000_10_page():
     r1000_10_adultwindow = tk.Toplevel()
     r1000_10_adultwindow.geometry("800x480")
     r1000_10_adultwindow.resizable(False, False)
     r1000_10_adultwindow.title("R1000_10")

     pygame.mixer.init()

     def playadult_r1000_10tor1000_20():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_20_R.ogg")
       pygame.mixer.music.play()
       r1000_10_adultwindow.destroy()
       showadult_r1000_20_page()

     pygame.mixer.init()

     def openadult__r1000_10tor2000_0():
       global C
       C = 1
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_10_adultwindow.destroy()
       showadult_r2000_0_page()

     r1000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r1000_10_label = tk.Label(r1000_10_adultwindow, image=r1000_10_img)
     r1000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_10_YES_button = tk.Button(r1000_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r1000_10tor2000_0)
     r1000_10_NO_button  = tk.Button(r1000_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r1000_10tor1000_20)

     r1000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_10_adultwindow.mainloop()

  # R1000_20 page
  def showadult_r1000_20_page():
     r1000_20_adultwindow = tk.Toplevel()
     r1000_20_adultwindow.geometry("800x480")
     r1000_20_adultwindow.resizable(False, False)
     r1000_20_adultwindow.title("R1000_20")

     pygame.mixer.init()

     def playadult_r1000_20tor1000_30():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_30_R.ogg")
       pygame.mixer.music.play()
       r1000_20_adultwindow.destroy()
       showadult_r1000_30_page()

     pygame.mixer.init()

     def openadult__r1000_20tor2000_0():
       global C
       C = 2
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_20_adultwindow.destroy()
       showadult_r2000_0_page()

     r1000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r1000_20_label = tk.Label(r1000_20_adultwindow, image=r1000_20_img)
     r1000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_20_YES_button = tk.Button(r1000_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r1000_20tor2000_0)
     r1000_20_NO_button  = tk.Button(r1000_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r1000_20tor1000_30)

     r1000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_20_adultwindow.mainloop()

  # R1000_30 page
  def showadult_r1000_30_page():
     r1000_30_adultwindow = tk.Toplevel()
     r1000_30_adultwindow.geometry("800x480")
     r1000_30_adultwindow.resizable(False, False)
     r1000_30_adultwindow.title("R1000_30")

     pygame.mixer.init()

     def playadult_r1000_30tor1000_40():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_40_R.ogg")
       pygame.mixer.music.play()
       r1000_30_adultwindow.destroy()
       showadult_r1000_40_page()

     pygame.mixer.init()

     def openadult__r1000_30tor2000_0():
       global C
       C = 3
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_30_adultwindow.destroy()
       showadult_r2000_0_page()

     r1000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r1000_30_label = tk.Label(r1000_30_adultwindow, image=r1000_30_img)
     r1000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_30_YES_button = tk.Button(r1000_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r1000_30tor2000_0)
     r1000_30_NO_button  = tk.Button(r1000_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r1000_30tor1000_40)

     r1000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_30_adultwindow.mainloop()

  # R1000_40 page
  def showadult_r1000_40_page():
     r1000_40_adultwindow = tk.Toplevel()
     r1000_40_adultwindow.geometry("800x480")
     r1000_40_adultwindow.resizable(False, False)
     r1000_40_adultwindow.title("R1000_40")

     pygame.mixer.init()

     def playadult_r1000_40tor1000_50():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_50_R.ogg")
       pygame.mixer.music.play()
       r1000_40_adultwindow.destroy()
       showadult_r1000_50_page()

     pygame.mixer.init()

     def openadult__r1000_40tor2000_0():
       global C
       C = 4
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_40_adultwindow.destroy()
       showadult_r2000_0_page()

     r1000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r1000_40_label = tk.Label(r1000_40_adultwindow, image=r1000_40_img)
     r1000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_40_YES_button = tk.Button(r1000_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r1000_40tor2000_0)
     r1000_40_NO_button  = tk.Button(r1000_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r1000_40tor1000_50)

     r1000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_40_adultwindow.mainloop()

  # R1000_50 page
  def showadult_r1000_50_page():
     r1000_50_adultwindow = tk.Toplevel()
     r1000_50_adultwindow.geometry("800x480")
     r1000_50_adultwindow.resizable(False, False)
     r1000_50_adultwindow.title("R1000_50")

     pygame.mixer.init()

     def playadult_r1000_50tor1000_60():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_60_R.ogg")
       pygame.mixer.music.play()
       r1000_50_adultwindow.destroy()
       showadult_r1000_60_page()

     pygame.mixer.init()

     def openadult__r1000_50tor2000_0():
       global C
       C = 5
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_50_adultwindow.destroy()
       showadult_r2000_0_page()

     r1000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r1000_50_label = tk.Label(r1000_50_adultwindow, image=r1000_50_img)
     r1000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_50_YES_button = tk.Button(r1000_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r1000_50tor2000_0)
     r1000_50_NO_button  = tk.Button(r1000_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r1000_50tor1000_60)

     r1000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_50_adultwindow.mainloop()

  # R1000_60 page
  def showadult_r1000_60_page():
     r1000_60_adultwindow = tk.Toplevel()
     r1000_60_adultwindow.geometry("800x480")
     r1000_60_adultwindow.resizable(False, False)
     r1000_60_adultwindow.title("R1000_60")

     pygame.mixer.init()

     def playadult_r1000_60tor1000_70():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_70_R.ogg")
       pygame.mixer.music.play()
       r1000_60_adultwindow.destroy()
       showadult_r1000_70_page()

     pygame.mixer.init()

     def openadult__r1000_60tor2000_0():
       global C
       C = 6
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_60_adultwindow.destroy()
       showadult_r2000_0_page()

     r1000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r1000_60_label = tk.Label(r1000_60_adultwindow, image=r1000_60_img)
     r1000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_60_YES_button = tk.Button(r1000_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r1000_60tor2000_0)
     r1000_60_NO_button  = tk.Button(r1000_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r1000_60tor1000_70)

     r1000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_60_adultwindow.mainloop()

  # R1000_70 page
  def showadult_r1000_70_page():
     r1000_70_adultwindow = tk.Toplevel()
     r1000_70_adultwindow.geometry("800x480")
     r1000_70_adultwindow.resizable(False, False)
     r1000_70_adultwindow.title("R1000_70")

     pygame.mixer.init()

     def playadult_r1000_70tor1000_80():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\1000_80_R.ogg")
       pygame.mixer.music.play()
       r1000_70_adultwindow.destroy()
       showadult_r1000_80_page()
 
     pygame.mixer.init()

     def openadult__r1000_70tor2000_0():
       global C
       C = 7
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_70_adultwindow.destroy()
       showadult_r2000_0_page()

     r1000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r1000_70_label = tk.Label(r1000_70_adultwindow, image=r1000_70_img)
     r1000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_70_YES_button = tk.Button(r1000_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r1000_70tor2000_0)
     r1000_70_NO_button  = tk.Button(r1000_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r1000_70tor1000_80)

     r1000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_70_adultwindow.mainloop()

  # R1000_80 page
  def showadult_r1000_80_page():
     r1000_80_adultwindow = tk.Toplevel()
     r1000_80_adultwindow.geometry("800x480")
     r1000_80_adultwindow.resizable(False, False)
     r1000_80_adultwindow.title("R1000_80")

     pygame.mixer.init()

     def playadult_r1000_80tor2000_0():
       global C
       C = 9
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_80_adultwindow.destroy()
       showadult_r2000_0_page()

     pygame.mixer.init()

     def openadult__r1000_80tor2000_00():
       global C
       C = 8
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
       pygame.mixer.music.play()
       r1000_80_adultwindow.destroy()
       showadult_r2000_0_page()

     r1000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r1000_80_label = tk.Label(r1000_80_adultwindow, image=r1000_80_img)
     r1000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r1000_80_YES_button = tk.Button(r1000_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r1000_80tor2000_00)
     r1000_80_NO_button  = tk.Button(r1000_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r1000_80tor2000_0)

     r1000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r1000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r1000_80_adultwindow.mainloop()

  # R2000_0 page
  def showadult_r2000_0_page():
     r2000_0_adultwindow = tk.Toplevel()
     r2000_0_adultwindow.geometry("800x480")
     r2000_0_adultwindow.resizable(False, False)
     r2000_0_adultwindow.title("R2000_0")

     def blank4_page():
      r2000_0_adultwindow.destroy() 
      showadult_blank4_page()
      
     pygame.mixer.init()

     def playadult_r2000_10():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_10_R.ogg")
       pygame.mixer.music.play()
       r2000_0_adultwindow.destroy()
       showadult_r2000_10_page()

     r2000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r2000_0_label = tk.Label(r2000_0_adultwindow, image=r2000_0_img)
     r2000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_0_YES_button = tk.Button(r2000_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank4_page)
     r2000_0_NO_button  = tk.Button(r2000_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r2000_10)

     r2000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_0_adultwindow.mainloop()

  # blank4
  def showadult_blank4_page():
     blank4_adultwindow = tk.Toplevel()
     blank4_adultwindow.geometry("800x480")
     blank4_adultwindow.resizable(False, False)
     blank4_adultwindow.title("blank4")

     def warning4_page():
       blank4_adultwindow.destroy() 
       showadult_warning4_page()

     pygame.mixer.init()
     D = None

     def playadult_blank4tor4000_0():
       global D
       D = 0
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
       pygame.mixer.music.play()
       blank4_adultwindow.destroy()
       showadult_r4000_0_page()
     
     blank4_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank4_label = tk.Label(blank4_adultwindow , image=blank4_img)
     blank4_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank4_YES_button = tk.Button(blank4_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning4_page)
     blank4_NO_button= tk.Button(blank4_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank4tor4000_0)

     blank4_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank4_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank4_adultwindow.mainloop()

  # warning4
  def showadult_warning4_page():
      warning4_adultwindow = tk.Toplevel()
      warning4_adultwindow.geometry("800x480")
      warning4_adultwindow.resizable(False, False)
      warning4_adultwindow.title("warning4")
      
      warning4_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning4_label = tk.Label(warning4_adultwindow, image=warning4_image)
      warning4_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning4tor2000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_0_R.ogg")
        pygame.mixer.music.play()
        warning4_adultwindow.destroy()
        showadult_r250_0_page()

      warning4_button = tk.Button(warning4_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning4tor2000_0)
      warning4_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning4_adultwindow.mainloop()

  # R2000_10 page
  def showadult_r2000_10_page():
     r2000_10_adultwindow = tk.Toplevel()
     r2000_10_adultwindow.geometry("800x480")
     r2000_10_adultwindow.resizable(False, False)
     r2000_10_adultwindow.title("R2000_10")

     pygame.mixer.init()

     def playadult_r2000_10tor2000_20():
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_20_R.ogg")
       pygame.mixer.music.play()
       r2000_10_adultwindow.destroy()
       showadult_r2000_20_page()

     pygame.mixer.init()

     def openadult__r2000_10tor4000_0():
       global D
       D = 1
       pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
       pygame.mixer.music.play()
       r2000_10_adultwindow.destroy()
       showadult_r4000_0_page()

     r2000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r2000_10_label = tk.Label(r2000_10_adultwindow, image=r2000_10_img)
     r2000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_10_YES_button = tk.Button(r2000_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r2000_10tor4000_0)
     r2000_10_NO_button  = tk.Button(r2000_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r2000_10tor2000_20)

     r2000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_10_adultwindow.mainloop()

  # R2000_20 page
  def showadult_r2000_20_page():
     r2000_20_adultwindow = tk.Toplevel()
     r2000_20_adultwindow.geometry("800x480")
     r2000_20_adultwindow.resizable(False, False)
     r2000_20_adultwindow.title("R2000_20")

     pygame.mixer.init()

     def playadult_r2000_20tor2000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_30_R.ogg")
      pygame.mixer.music.play()
      r2000_20_adultwindow.destroy()
      showadult_r2000_30_page()

     pygame.mixer.init()

     def openadult__r2000_20tor4000_0():
      global D
      D = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_20_adultwindow.destroy()
      showadult_r4000_0_page()

     r2000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r2000_20_label = tk.Label(r2000_20_adultwindow, image=r2000_20_img)
     r2000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_20_YES_button = tk.Button(r2000_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r2000_20tor4000_0)
     r2000_20_NO_button  = tk.Button(r2000_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r2000_20tor2000_30)

     r2000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_20_adultwindow.mainloop()

  # R2000_30 page
  def showadult_r2000_30_page():
     r2000_30_adultwindow = tk.Toplevel()
     r2000_30_adultwindow.resizable(False, False)
     r2000_30_adultwindow.geometry("800x480")
     r2000_30_adultwindow.title("R2000_30")

     pygame.mixer.init()

     def playadult_r2000_30tor2000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_40_R.ogg")
      pygame.mixer.music.play()
      r2000_30_adultwindow.destroy()
      showadult_r2000_40_page()

     pygame.mixer.init()

     def openadult__r2000_30tor4000_0():
      global D
      D = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_30_adultwindow.destroy()
      showadult_r4000_0_page()

     r2000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r2000_30_label = tk.Label(r2000_30_adultwindow, image=r2000_30_img)
     r2000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_30_YES_button = tk.Button(r2000_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r2000_30tor4000_0)
     r2000_30_NO_button  = tk.Button(r2000_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r2000_30tor2000_40)

     r2000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_30_adultwindow.mainloop()

  # R2000_40 page
  def showadult_r2000_40_page():
     r2000_40_adultwindow = tk.Toplevel()
     r2000_40_adultwindow.geometry("800x480")
     r2000_40_adultwindow.resizable(False, False)
     r2000_40_adultwindow.title("R2000_40")

     pygame.mixer.init()

     def playadult_r2000_40tor2000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_50_R.ogg")
      pygame.mixer.music.play()
      r2000_40_adultwindow.destroy()
      showadult_r2000_50_page()

     pygame.mixer.init()

     def openadult__r2000_40tor4000_0():
      global D
      D = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_40_adultwindow.destroy()
      showadult_r4000_0_page()

     r2000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r2000_40_label = tk.Label(r2000_40_adultwindow, image=r2000_40_img)
     r2000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_40_YES_button = tk.Button(r2000_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r2000_40tor4000_0)
     r2000_40_NO_button  = tk.Button(r2000_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r2000_40tor2000_50)

     r2000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_40_adultwindow.mainloop()

  # R2000_50 page
  def showadult_r2000_50_page():
     r2000_50_adultwindow = tk.Toplevel()
     r2000_50_adultwindow.geometry("800x480")
     r2000_50_adultwindow.resizable(False, False)
     r2000_50_adultwindow.title("R2000_50")

     pygame.mixer.init()

     def playadult_r2000_50tor2000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_60_R.ogg")
      pygame.mixer.music.play()
      r2000_50_adultwindow.destroy()
      showadult_r2000_60_page()

     pygame.mixer.init()

     def openadult__r2000_50tor4000_0():
      global D
      D = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_50_adultwindow.destroy()
      showadult_r4000_0_page()

     r2000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r2000_50_label = tk.Label(r2000_50_adultwindow, image=r2000_50_img)
     r2000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_50_YES_button = tk.Button(r2000_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r2000_50tor4000_0)
     r2000_50_NO_button  = tk.Button(r2000_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r2000_50tor2000_60)

     r2000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_50_adultwindow.mainloop()

  # R2000_60 page
  def showadult_r2000_60_page():
     r2000_60_adultwindow = tk.Toplevel()
     r2000_60_adultwindow.geometry("800x480")
     r2000_60_adultwindow.resizable(False, False)
     r2000_60_adultwindow.title("R2000_60")

     pygame.mixer.init()

     def playadult_r2000_60tor2000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_70_R.ogg")
      pygame.mixer.music.play()
      r2000_60_adultwindow.destroy()
      showadult_r2000_70_page()

     pygame.mixer.init()

     def openadult__r2000_60tor4000_0():
      global D
      D = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_60_adultwindow.destroy()
      showadult_r4000_0_page()

     r2000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r2000_60_label = tk.Label(r2000_60_adultwindow, image=r2000_60_img)
     r2000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_60_YES_button = tk.Button(r2000_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r2000_60tor4000_0)
     r2000_60_NO_button  = tk.Button(r2000_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r2000_60tor2000_70)

     r2000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_60_adultwindow.mainloop()

  # R2000_70 page
  def showadult_r2000_70_page():
     r2000_70_adultwindow = tk.Toplevel()
     r2000_70_adultwindow.geometry("800x480")
     r2000_70_adultwindow.resizable(False, False)
     r2000_70_adultwindow.title("R2000_70")

     pygame.mixer.init()

     def playadult_r2000_70tor2000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\2000_80_R.ogg")
      pygame.mixer.music.play()
      r2000_70_adultwindow.destroy()
      showadult_r2000_80_page()

     pygame.mixer.init()

     def openadult__r2000_70tor4000_0():
      global D
      D = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_70_adultwindow.destroy()
      showadult_r4000_0_page()

     r2000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r2000_70_label = tk.Label(r2000_70_adultwindow, image=r2000_70_img)
     r2000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_70_YES_button = tk.Button(r2000_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r2000_70tor4000_0)
     r2000_70_NO_button  = tk.Button(r2000_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r2000_70tor2000_80)

     r2000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_70_adultwindow.mainloop()

  # R2000_80 page
  def showadult_r2000_80_page():
     r2000_80_adultwindow = tk.Toplevel()
     r2000_80_adultwindow.geometry("800x480")
     r2000_80_adultwindow.resizable(False, False)
     r2000_80_adultwindow.title("R2000_80")

     pygame.mixer.init()

     def playadult_r2000_80tor4000_0():
      global D
      D = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_80_adultwindow.destroy()
      showadult_r4000_0_page()

     pygame.mixer.init()

     def openadult__r2000_80tor4000_00():
      global D
      D = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
      pygame.mixer.music.play()
      r2000_80_adultwindow.destroy()
      showadult_r4000_0_page()

     r2000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r2000_80_label = tk.Label(r2000_80_adultwindow, image=r2000_80_img)
     r2000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r2000_80_YES_button = tk.Button(r2000_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r2000_80tor4000_00)
     r2000_80_NO_button  = tk.Button(r2000_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r2000_80tor4000_0)

     r2000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r2000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r2000_80_adultwindow.mainloop()

  # R4000_0 page
  def showadult_r4000_0_page():
     r4000_0_adultwindow = tk.Toplevel()
     r4000_0_adultwindow.geometry("800x480")
     r4000_0_adultwindow.resizable(False, False)
     r4000_0_adultwindow.title("R4000_0")

     def blank5_page():
      r4000_0_adultwindow.destroy() 
      showadult_blank5_page()
      
     pygame.mixer.init()

     def playadult_r4000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_10_R.ogg")
      pygame.mixer.music.play()
      r4000_0_adultwindow.destroy()
      showadult_r4000_10_page()

     r4000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r4000_0_label = tk.Label(r4000_0_adultwindow, image=r4000_0_img)
     r4000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_0_YES_button = tk.Button(r4000_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank5_page)
     r4000_0_NO_button  = tk.Button(r4000_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r4000_10)

     r4000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_0_adultwindow.mainloop()

  # blank5
  def showadult_blank5_page():
     blank5_adultwindow = tk.Toplevel()
     blank5_adultwindow.geometry("800x480")
     blank5_adultwindow.resizable(False, False)
     blank5_adultwindow.title("blank5")

     def warning5_page():
      blank5_adultwindow.destroy() 
      showadult_warning5_page()

     pygame.mixer.init()
     E = None

     def playadult_blank5tor8000_0():
      global E
      E = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      blank5_adultwindow.destroy()
      showadult_r8000_0_page()
     
     blank5_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank5_label = tk.Label(blank5_adultwindow , image=blank5_img)
     blank5_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank5_YES_button = tk.Button(blank5_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning5_page)
     blank5_NO_button= tk.Button(blank5_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank5tor8000_0)

     blank5_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank5_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank5_adultwindow.mainloop()

  # warning5
  def showadult_warning5_page():
      warning5_adultwindow = tk.Toplevel()
      warning5_adultwindow.geometry("800x480")
      warning5_adultwindow.resizable(False, False)
      warning5_adultwindow.title("warning5")
      
      warning5_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning5_label = tk.Label(warning5_adultwindow, image=warning5_image)
      warning5_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning5tor4000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_0_R.ogg")
        pygame.mixer.music.play()
        warning5_adultwindow.destroy()
        showadult_r250_0_page()

      warning5_button = tk.Button(warning5_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning5tor4000_0)
      warning5_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning5_adultwindow.mainloop()

  # R4000_10 page
  def showadult_r4000_10_page():
     r4000_10_adultwindow = tk.Toplevel()
     r4000_10_adultwindow.geometry("800x480")
     r4000_10_adultwindow.resizable(False, False)
     r4000_10_adultwindow.title("R4000_10")

     pygame.mixer.init()

     def playadult_r4000_10tor4000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_20_R.ogg")
      pygame.mixer.music.play()
      r4000_10_adultwindow.destroy()
      showadult_r4000_20_page()

     pygame.mixer.init()

     def openadult__r4000_10tor8000_0():
      global E
      E = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_10_adultwindow.destroy()
      showadult_r8000_0_page()

     r4000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r4000_10_label = tk.Label(r4000_10_adultwindow, image=r4000_10_img)
     r4000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_10_YES_button = tk.Button(r4000_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r4000_10tor8000_0)
     r4000_10_NO_button  = tk.Button(r4000_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r4000_10tor4000_20)

     r4000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_10_adultwindow.mainloop()

  # R4000_20 page
  def showadult_r4000_20_page():
     r4000_20_adultwindow = tk.Toplevel()
     r4000_20_adultwindow.geometry("800x480")
     r4000_20_adultwindow.resizable(False, False)
     r4000_20_adultwindow.title("R4000_20")

     pygame.mixer.init()

     def playadult_r4000_20tor4000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_30_R.ogg")
      pygame.mixer.music.play()
      r4000_20_adultwindow.destroy()
      showadult_r4000_30_page()

     pygame.mixer.init()

     def openadult__r4000_20tor8000_0():
      global E
      E = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_20_adultwindow.destroy()
      showadult_r8000_0_page()

     r4000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r4000_20_label = tk.Label(r4000_20_adultwindow, image=r4000_20_img)
     r4000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_20_YES_button = tk.Button(r4000_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r4000_20tor8000_0)
     r4000_20_NO_button  = tk.Button(r4000_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r4000_20tor4000_30)

     r4000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_20_adultwindow.mainloop()

  # R4000_30 page
  def showadult_r4000_30_page():
     r4000_30_adultwindow = tk.Toplevel()
     r4000_30_adultwindow.geometry("800x480")
     r4000_30_adultwindow.resizable(False, False)
     r4000_30_adultwindow.title("R4000_30")

     pygame.mixer.init()

     def playadult_r4000_30tor4000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_40_R.ogg")
      pygame.mixer.music.play()
      r4000_30_adultwindow.destroy()
      showadult_r4000_40_page()

     pygame.mixer.init()

     def openadult__r4000_30tor8000_0():
      global E
      E = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_30_adultwindow.destroy()
      showadult_r8000_0_page()

     r4000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r4000_30_label = tk.Label(r4000_30_adultwindow, image=r4000_30_img)
     r4000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_30_YES_button = tk.Button(r4000_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r4000_30tor8000_0)
     r4000_30_NO_button  = tk.Button(r4000_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r4000_30tor4000_40)

     r4000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_30_adultwindow.mainloop()

  # R4000_40 page
  def showadult_r4000_40_page():
     r4000_40_adultwindow = tk.Toplevel()
     r4000_40_adultwindow.geometry("800x480")
     r4000_40_adultwindow.resizable(False, False)
     r4000_40_adultwindow.title("R4000_40")

     pygame.mixer.init()

     def playadult_r4000_40tor4000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_50_R.ogg")
      pygame.mixer.music.play()
      r4000_40_adultwindow.destroy()
      showadult_r4000_50_page()

     pygame.mixer.init()

     def openadult__r4000_40tor8000_0():
      global E
      E = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_40_adultwindow.destroy()
      showadult_r8000_0_page()

     r4000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r4000_40_label = tk.Label(r4000_40_adultwindow, image=r4000_40_img)
     r4000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_40_YES_button = tk.Button(r4000_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r4000_40tor8000_0)
     r4000_40_NO_button  = tk.Button(r4000_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r4000_40tor4000_50)

     r4000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_40_adultwindow.mainloop()

  # R4000_50 page
  def showadult_r4000_50_page():
     r4000_50_adultwindow = tk.Toplevel()
     r4000_50_adultwindow.geometry("800x480")
     r4000_50_adultwindow.resizable(False, False)
     r4000_50_adultwindow.title("R4000_50")

     pygame.mixer.init()

     def playadult_r4000_50tor4000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_60_R.ogg")
      pygame.mixer.music.play()
      r4000_50_adultwindow.destroy()
      showadult_r4000_60_page()

     pygame.mixer.init()

     def openadult__r4000_50tor8000_0():
      global E
      E = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_50_adultwindow.destroy()
      showadult_r8000_0_page()

     r4000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r4000_50_label = tk.Label(r4000_50_adultwindow, image=r4000_50_img)
     r4000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_50_YES_button = tk.Button(r4000_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r4000_50tor8000_0)
     r4000_50_NO_button  = tk.Button(r4000_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r4000_50tor4000_60)

     r4000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_50_adultwindow.mainloop()

  # R4000_60 page
  def showadult_r4000_60_page():
     r4000_60_adultwindow = tk.Toplevel()
     r4000_60_adultwindow.geometry("800x480")
     r4000_60_adultwindow.resizable(False, False)
     r4000_60_adultwindow.title("R4000_60")

     pygame.mixer.init()

     def playadult_r4000_60tor4000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_70_R.ogg")
      pygame.mixer.music.play()
      r4000_60_adultwindow.destroy()
      showadult_r4000_70_page()

     pygame.mixer.init()

     def openadult__r4000_60tor8000_0():
      global E
      E = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_60_adultwindow.destroy()
      showadult_r8000_0_page()

     r4000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r4000_60_label = tk.Label(r4000_60_adultwindow, image=r4000_60_img)
     r4000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_60_YES_button = tk.Button(r4000_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r4000_60tor8000_0)
     r4000_60_NO_button  = tk.Button(r4000_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r4000_60tor4000_70)

     r4000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_60_adultwindow.mainloop()

  # R4000_70 page
  def showadult_r4000_70_page():
     r4000_70_adultwindow = tk.Toplevel()
     r4000_70_adultwindow.geometry("800x480")
     r4000_70_adultwindow.resizable(False, False)
     r4000_70_adultwindow.title("R4000_70")

     pygame.mixer.init()

     def playadult_r4000_70tor4000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\4000_80_R.ogg")
      pygame.mixer.music.play()
      r4000_70_adultwindow.destroy()
      showadult_r4000_80_page()

     pygame.mixer.init()

     def openadult__r4000_70tor8000_0():
      global E
      E = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_70_adultwindow.destroy()
      showadult_r8000_0_page()

     r4000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r4000_70_label = tk.Label(r4000_70_adultwindow, image=r4000_70_img)
     r4000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_70_YES_button = tk.Button(r4000_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r4000_70tor8000_0)
     r4000_70_NO_button  = tk.Button(r4000_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r4000_70tor4000_80)

     r4000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_70_adultwindow.mainloop()

  # R4000_80 page
  def showadult_r4000_80_page():
     r4000_80_adultwindow = tk.Toplevel()
     r4000_80_adultwindow.geometry("800x480")
     r4000_80_adultwindow.resizable(False, False)
     r4000_80_adultwindow.title("R4000_80")

     pygame.mixer.init()

     def playadult_r4000_80tor8000_0():
      global E
      E = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_80_adultwindow.destroy()
      showadult_r8000_0_page()

     pygame.mixer.init()

     def openadult__r4000_80tor8000_00():
      global E
      E = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_0_R.ogg")
      pygame.mixer.music.play()
      r4000_80_adultwindow.destroy()
      showadult_r8000_0_page()

     r4000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r4000_80_label = tk.Label(r4000_80_adultwindow, image=r4000_80_img)
     r4000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r4000_80_YES_button = tk.Button(r4000_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r4000_80tor8000_00)
     r4000_80_NO_button  = tk.Button(r4000_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r4000_80tor8000_0)

     r4000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r4000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r4000_80_adultwindow.mainloop()

  # R8000_0 page
  def showadult_r8000_0_page():
     r8000_0_adultwindow = tk.Toplevel()
     r8000_0_adultwindow.geometry("800x480")
     r8000_0_adultwindow.resizable(False, False)
     r8000_0_adultwindow.title("R8000_0")

     def blank6_page():
      r8000_0_adultwindow.destroy() 
      showadult_blank6_page()
      
     pygame.mixer.init()

     def playadult_r8000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_10_R.ogg")
      pygame.mixer.music.play()
      r8000_0_adultwindow.destroy()
      showadult_r8000_10_page()

     r8000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r8000_0_label = tk.Label(r8000_0_adultwindow, image=r8000_0_img)
     r8000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_0_YES_button = tk.Button(r8000_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank6_page)
     r8000_0_NO_button  = tk.Button(r8000_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r8000_10)

     r8000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_0_adultwindow.mainloop()

  # blank6
  def showadult_blank6_page():
     blank6_adultwindow = tk.Toplevel()
     blank6_adultwindow.geometry("800x480")
     blank6_adultwindow.resizable(False, False)
     blank6_adultwindow.title("blank6")

     def warning6_page():
      blank6_adultwindow.destroy() 
      showadult_warning6_page()

     pygame.mixer.init()
     F= None

     def playadult_blank6toL250_0():
      global F
      F = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      blank6_adultwindow.destroy()
      showadult_L250_0_page()
     
     blank6_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank6_label = tk.Label(blank6_adultwindow , image=blank6_img)
     blank6_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank6_YES_button = tk.Button(blank6_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning6_page)
     blank6_NO_button= tk.Button(blank6_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank6toL250_0)

     blank6_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank6_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank6_adultwindow.mainloop()

  # warning6
  def showadult_warning6_page():
      warning6_adultwindow = tk.Toplevel()
      warning6_adultwindow.geometry("800x480")
      warning6_adultwindow.resizable(False, False)
      warning6_adultwindow.title("warning6")
      
      warning6_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning6_label = tk.Label(warning6_adultwindow, image=warning6_image)
      warning6_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning6tor8000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
        pygame.mixer.music.play()
        warning6_adultwindow.destroy()
        showadult_r250_0_page()

      warning6_button = tk.Button(warning6_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning6tor8000_0)
      warning6_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning6_adultwindow.mainloop()

  # R8000_10 page
  def showadult_r8000_10_page():
     r8000_10_adultwindow = tk.Toplevel()
     r8000_10_adultwindow.geometry("800x480")
     r8000_10_adultwindow.resizable(False, False)
     r8000_10_adultwindow.title("R8000_10")

     pygame.mixer.init()

     def playadult_r8000_10tor8000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_20_R.ogg")
      pygame.mixer.music.play()
      r8000_10_adultwindow.destroy()
      showadult_r8000_20_page()

     pygame.mixer.init()

     def openadult__r8000_10toL250_0():
      global F
      F = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_10_adultwindow.destroy()
      showadult_L250_0_page()

     r8000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r8000_10_label = tk.Label(r8000_10_adultwindow, image=r8000_10_img)
     r8000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_10_YES_button = tk.Button(r8000_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r8000_10toL250_0)
     r8000_10_NO_button  = tk.Button(r8000_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r8000_10tor8000_20)

     r8000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_10_adultwindow.mainloop()

  # R8000_20 page
  def showadult_r8000_20_page():
     r8000_20_adultwindow = tk.Toplevel()
     r8000_20_adultwindow.geometry("800x480")
     r8000_20_adultwindow.resizable(False, False)
     r8000_20_adultwindow.title("R8000_20")

     pygame.mixer.init()

     def playadult_r8000_20tor8000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_30_R.ogg")
      pygame.mixer.music.play()
      r8000_20_adultwindow.destroy()
      showadult_r8000_30_page()

     pygame.mixer.init()

     def openadult__r8000_20toL250_0():
      global F
      F = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_20_adultwindow.destroy()
      showadult_L250_0_page()

     r8000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r8000_20_label = tk.Label(r8000_20_adultwindow, image=r8000_20_img)
     r8000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_20_YES_button = tk.Button(r8000_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r8000_20toL250_0)
     r8000_20_NO_button  = tk.Button(r8000_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r8000_20tor8000_30)

     r8000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_20_adultwindow.mainloop()

  # R8000_30 page
  def showadult_r8000_30_page():
     r8000_30_adultwindow = tk.Toplevel()
     r8000_30_adultwindow.geometry("800x480")
     r8000_30_adultwindow.resizable(False, False)
     r8000_30_adultwindow.title("R8000_30")

     pygame.mixer.init()

     def playadult_r8000_30tor8000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_40_R.ogg")
      pygame.mixer.music.play()
      r8000_30_adultwindow.destroy()
      showadult_r8000_40_page()

     pygame.mixer.init()

     def openadult__r8000_30toL250_0():
      global F
      F = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_30_adultwindow.destroy()
      showadult_L250_0_page()

     r8000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r8000_30_label = tk.Label(r8000_30_adultwindow, image=r8000_30_img)
     r8000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_30_YES_button = tk.Button(r8000_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r8000_30toL250_0)
     r8000_30_NO_button  = tk.Button(r8000_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r8000_30tor8000_40)

     r8000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_30_adultwindow.mainloop()

  # R8000_40 page
  def showadult_r8000_40_page():
     r8000_40_adultwindow = tk.Toplevel()
     r8000_40_adultwindow.geometry("800x480")
     r8000_40_adultwindow.resizable(False, False)
     r8000_40_adultwindow.title("R8000_40")

     pygame.mixer.init()

     def playadult_r8000_40tor8000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_50_R.ogg")
      pygame.mixer.music.play()
      r8000_40_adultwindow.destroy()
      showadult_r8000_50_page()

     pygame.mixer.init()

     def openadult__r8000_40toL250_0():
      global F
      F = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_40_adultwindow.destroy()
      showadult_L250_0_page()

     r8000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r8000_40_label = tk.Label(r8000_40_adultwindow, image=r8000_40_img)
     r8000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_40_YES_button = tk.Button(r8000_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r8000_40toL250_0)
     r8000_40_NO_button  = tk.Button(r8000_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r8000_40tor8000_50)

     r8000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_40_adultwindow.mainloop()

  # R8000_50 page
  def showadult_r8000_50_page():
     r8000_50_adultwindow = tk.Toplevel()
     r8000_50_adultwindow.geometry("800x480")
     r8000_50_adultwindow.resizable(False, False)
     r8000_50_adultwindow.title("R8000_50")

     pygame.mixer.init()

     def playadult_r8000_50tor8000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_60_R.ogg")
      pygame.mixer.music.play()
      r8000_50_adultwindow.destroy()
      showadult_r8000_60_page()

     pygame.mixer.init()

     def openadult__r8000_50toL250_0():
      global F
      F = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_50_adultwindow.destroy()
      showadult_L250_0_page()

     r8000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r8000_50_label = tk.Label(r8000_50_adultwindow, image=r8000_50_img)
     r8000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_50_YES_button = tk.Button(r8000_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r8000_50toL250_0)
     r8000_50_NO_button  = tk.Button(r8000_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r8000_50tor8000_60)

     r8000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_50_adultwindow.mainloop()

  # R8000_60 page
  def showadult_r8000_60_page():
     r8000_60_adultwindow = tk.Toplevel()
     r8000_60_adultwindow.geometry("800x480")
     r8000_60_adultwindow.resizable(False, False)
     r8000_60_adultwindow.title("R8000_60")

     pygame.mixer.init()

     def playadult_r8000_60tor8000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_70_R.ogg")
      pygame.mixer.music.play()
      r8000_60_adultwindow.destroy()
      showadult_r8000_70_page()

     pygame.mixer.init()

     def openadult__r8000_60toL250_0():
      global F
      F = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_60_adultwindow.destroy()
      showadult_L250_0_page()

     r8000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r8000_60_label = tk.Label(r8000_60_adultwindow, image=r8000_60_img)
     r8000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_60_YES_button = tk.Button(r8000_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r8000_60toL250_0)
     r8000_60_NO_button  = tk.Button(r8000_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r8000_60tor8000_70)

     r8000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_60_adultwindow.mainloop()

  # R8000_70 page
  def showadult_r8000_70_page():
     r8000_70_adultwindow = tk.Toplevel()
     r8000_70_adultwindow.geometry("800x480")
     r8000_70_adultwindow.resizable(False, False)
     r8000_70_adultwindow.title("R8000_70")

     pygame.mixer.init()

     def playadult_r8000_70tor8000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\right\8000_80_R.ogg")
      pygame.mixer.music.play()
      r8000_70_adultwindow.destroy()
      showadult_r8000_80_page()

     pygame.mixer.init()

     def openadult__r8000_70toL250_0():
      global F
      F = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_70_adultwindow.destroy()
      showadult_L250_0_page()

     r8000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r8000_70_label = tk.Label(r8000_70_adultwindow, image=r8000_70_img)
     r8000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_70_YES_button = tk.Button(r8000_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r8000_70toL250_0)
     r8000_70_NO_button  = tk.Button(r8000_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r8000_70tor8000_80)

     r8000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_70_adultwindow.mainloop()

  # R8000_80 page
  def showadult_r8000_80_page():
     r8000_80_adultwindow = tk.Toplevel()
     r8000_80_adultwindow.geometry("800x480")
     r8000_80_adultwindow.resizable(False, False)
     r8000_80_adultwindow.title("R8000_80")

     pygame.mixer.init()

     def playadult_r8000_80toL250_0():
      global F
      F = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_80_adultwindow.destroy()
      showadult_L250_0_page()

     pygame.mixer.init()

     def openadult__r8000_80toL250_00():
      global F
      F = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_0_L.mp3")
      pygame.mixer.music.play()
      r8000_80_adultwindow.destroy()
      showadult_L250_0_page()

     r8000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     r8000_80_label = tk.Label(r8000_80_adultwindow, image=r8000_80_img)
     r8000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     r8000_80_YES_button = tk.Button(r8000_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__r8000_80toL250_00)
     r8000_80_NO_button  = tk.Button(r8000_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_r8000_80toL250_0)

     r8000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     r8000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     r8000_80_adultwindow.mainloop()

  # L250_0 page
  def showadult_L250_0_page():
     L250_0_adultwindow = tk.Toplevel()
     L250_0_adultwindow.geometry("800x480")
     L250_0_adultwindow.resizable(False, False)
     L250_0_adultwindow.title("L250_0")

     def blank7_page():
      L250_0_adultwindow.destroy() 
      showadult_blank7_page()
      
     pygame.mixer.init()
     
     def playadult_L250_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_10_L.mp3")
      pygame.mixer.music.play()
      L250_0_adultwindow.destroy()
      showadult_L250_10_page()

     L250_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L250_0_label = tk.Label(L250_0_adultwindow, image=L250_0_img)
     L250_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_0_YES_button = tk.Button(L250_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank7_page)
     L250_0_NO_button  = tk.Button(L250_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L250_10)

     L250_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_0_adultwindow.mainloop()

  # blank7
  def showadult_blank7_page():
     blank7_adultwindow = tk.Toplevel()
     blank7_adultwindow.geometry("800x480")
     blank7_adultwindow.resizable(False, False)
     blank7_adultwindow.title("blank7")

     def warning7_page():
      blank7_adultwindow.destroy() 
      showadult_warning7_page()

     pygame.mixer.init()
     A1 = None

     def playadult_blank7toL500_0():
      global A1
      A1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      blank7_adultwindow.destroy()
      showadult_L500_0_page()
     
     blank7_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank7_label = tk.Label(blank7_adultwindow , image=blank7_img)
     blank7_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank7_YES_button = tk.Button(blank7_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning7_page)
     blank7_NO_button= tk.Button(blank7_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank7toL500_0)

     blank7_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank7_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank7_adultwindow.mainloop() 

  # warning7
  def showadult_warning7_page():
      warning7_adultwindow = tk.Toplevel()
      warning7_adultwindow.geometry("800x480")
      warning7_adultwindow.resizable(False, False)
      warning7_adultwindow.title("warning7")
      
      warning7_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning7_label = tk.Label(warning7_adultwindow, image=warning7_image)
      warning7_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning7toL250_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
        pygame.mixer.music.play()
        warning7_adultwindow.destroy()
        showadult_r250_0_page()

      warning7_button = tk.Button(warning7_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning7toL250_0)
      warning7_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning7_adultwindow.mainloop()

  # L250_10 page
  def showadult_L250_10_page():
     L250_10_adultwindow = tk.Toplevel()
     L250_10_adultwindow.geometry("800x480")
     L250_10_adultwindow.resizable(False, False)
     L250_10_adultwindow.title("L250_10")

     pygame.mixer.init()

     def playadult_L250_10toL250_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_20_L.mp3")
      pygame.mixer.music.play()
      L250_10_adultwindow.destroy()
      showadult_L250_20_page()

     pygame.mixer.init()

     def openadult__L250_10toL500_0():
      global A1
      A1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_10_adultwindow.destroy()
      showadult_L500_0_page()

     L250_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L250_10_label = tk.Label(L250_10_adultwindow, image=L250_10_img)
     L250_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_10_YES_button = tk.Button(L250_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L250_10toL500_0)
     L250_10_NO_button  = tk.Button(L250_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L250_10toL250_20)

     L250_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_10_adultwindow.mainloop()

  # L250_20 page
  def showadult_L250_20_page():
     L250_20_adultwindow = tk.Toplevel()
     L250_20_adultwindow.geometry("800x480")
     L250_20_adultwindow.resizable(False, False)
     L250_20_adultwindow.title("L250_20")

     pygame.mixer.init()

     def playadult_L250_20toL250_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_30_L.mp3")
      pygame.mixer.music.play()
      L250_20_adultwindow.destroy()
      showadult_L250_30_page()

     pygame.mixer.init()

     def openadult__L250_20toL500_0():
      global A1
      A1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_20_adultwindow.destroy()
      showadult_L500_0_page()

     L250_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L250_20_label = tk.Label(L250_20_adultwindow, image=L250_20_img)
     L250_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_20_YES_button = tk.Button(L250_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L250_20toL500_0)
     L250_20_NO_button  = tk.Button(L250_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L250_20toL250_30)

     L250_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_20_adultwindow.mainloop()

  # L250_30 page
  def showadult_L250_30_page():
     L250_30_adultwindow = tk.Toplevel()
     L250_30_adultwindow.geometry("800x480")
     L250_30_adultwindow.resizable(False, False)
     L250_30_adultwindow.title("L250_30")

     pygame.mixer.init()

     def playadult_L250_30toL250_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_40_L.mp3")
      pygame.mixer.music.play()
      L250_30_adultwindow.destroy()
      showadult_L250_40_page()

     pygame.mixer.init()

     def openadult__L250_30toL500_0():
      global A1
      A1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_30_adultwindow.destroy()
      showadult_L500_0_page()

     L250_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L250_30_label = tk.Label(L250_30_adultwindow, image=L250_30_img)
     L250_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_30_YES_button = tk.Button(L250_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L250_30toL500_0)
     L250_30_NO_button  = tk.Button(L250_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L250_30toL250_40)

     L250_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_30_adultwindow.mainloop()

  # L250_40 page
  def showadult_L250_40_page():
     L250_40_adultwindow = tk.Toplevel()
     L250_40_adultwindow.geometry("800x480")
     L250_40_adultwindow.resizable(False, False)
     L250_40_adultwindow.title("L250_40")

     pygame.mixer.init()

     def playadult_L250_40toL250_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_50_L.mp3")
      pygame.mixer.music.play()
      L250_40_adultwindow.destroy()
      showadult_L250_50_page()

     pygame.mixer.init()

     def openadult__L250_40toL500_0():
      global A1
      A1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_40_adultwindow.destroy()
      showadult_L500_0_page()

     L250_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L250_40_label = tk.Label(L250_40_adultwindow, image=L250_40_img)
     L250_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_40_YES_button = tk.Button(L250_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L250_40toL500_0)
     L250_40_NO_button  = tk.Button(L250_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L250_40toL250_50)

     L250_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_40_adultwindow.mainloop()

  # L250_50 page
  def showadult_L250_50_page():
     L250_50_adultwindow = tk.Toplevel()
     L250_50_adultwindow.geometry("800x480")
     L250_50_adultwindow.resizable(False, False)
     L250_50_adultwindow.title("L250_50")

     pygame.mixer.init()

     def playadult_L250_50toL250_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_60_L.mp3")
      pygame.mixer.music.play()
      L250_50_adultwindow.destroy()
      showadult_L250_60_page()

     pygame.mixer.init()

     def openadult__L250_50toL500_0():
      global A1
      A1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_50_adultwindow.destroy()
      showadult_L500_0_page()

     L250_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L250_50_label = tk.Label(L250_50_adultwindow, image=L250_50_img)
     L250_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_50_YES_button = tk.Button(L250_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L250_50toL500_0)
     L250_50_NO_button  = tk.Button(L250_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L250_50toL250_60)

     L250_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_50_adultwindow.mainloop()

  # L250_60 page
  def showadult_L250_60_page():
     L250_60_adultwindow = tk.Toplevel()
     L250_60_adultwindow.geometry("800x480")
     L250_60_adultwindow.resizable(False, False)
     L250_60_adultwindow.title("L250_60")

     pygame.mixer.init()

     def playadult_L250_60toL250_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_70_L.mp3")
      pygame.mixer.music.play()
      L250_60_adultwindow.destroy()
      showadult_L250_70_page()

     pygame.mixer.init()

     def openadult__L250_60toL500_0():
      global A1
      A1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_60_adultwindow.destroy()
      showadult_L500_0_page()

     L250_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L250_60_label = tk.Label(L250_60_adultwindow, image=L250_60_img)
     L250_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_60_YES_button = tk.Button(L250_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L250_60toL500_0)
     L250_60_NO_button  = tk.Button(L250_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L250_60toL250_70)

     L250_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_60_adultwindow.mainloop()

  # L250_70 page
  def showadult_L250_70_page():
     L250_70_adultwindow = tk.Toplevel()
     L250_70_adultwindow.geometry("800x480")
     L250_70_adultwindow.resizable(False, False)
     L250_70_adultwindow.title("L250_70")

     pygame.mixer.init()

     def playadult_L250_70toL250_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\250_80_L.mp3")
      pygame.mixer.music.play()
      L250_70_adultwindow.destroy()
      showadult_L250_80_page()

     pygame.mixer.init()

     def openadult__L250_70toL500_0():
      global A1
      A1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_70_adultwindow.destroy()
      showadult_L500_0_page()

     L250_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L250_70_label = tk.Label(L250_70_adultwindow, image=L250_70_img)
     L250_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_70_YES_button = tk.Button(L250_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L250_70toL500_0)
     L250_70_NO_button  = tk.Button(L250_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L250_70toL250_80)

     L250_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_70_adultwindow.mainloop()

   # L250_80 page
  def showadult_L250_80_page():
     L250_80_adultwindow = tk.Toplevel()
     L250_80_adultwindow.geometry("800x480")
     L250_80_adultwindow.resizable(False, False)
     L250_80_adultwindow.title("L250_80")

     pygame.mixer.init()

     def playadult_L250_80toL500_0():
      global A1
      A1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_80_adultwindow.destroy()
      showadult_L500_0_page()

     pygame.mixer.init()

     def openadult__L250_80toL500_00():
      global A1
      A1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_0_L.mp3")
      pygame.mixer.music.play()
      L250_80_adultwindow.destroy()
      showadult_L500_0_page()

     L250_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L250_80_label = tk.Label(L250_80_adultwindow, image=L250_80_img)
     L250_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L250_80_YES_button = tk.Button(L250_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L250_80toL500_00)
     L250_80_NO_button  = tk.Button(L250_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L250_80toL500_0)

     L250_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L250_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L250_80_adultwindow.mainloop()

  # L500_0 page
  def showadult_L500_0_page():
     L500_0_adultwindow = tk.Toplevel()
     L500_0_adultwindow.geometry("800x480")
     L500_0_adultwindow.resizable(False, False)
     L500_0_adultwindow.title("L500_0")

     def blank8_page():
      L500_0_adultwindow.destroy() 
      showadult_blank8_page()
      
     pygame.mixer.init()

     def playadult_L500_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_10_L.mp3")
      pygame.mixer.music.play()
      L500_0_adultwindow.destroy()
      showadult_L500_10_page()

     L500_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L500_0_label = tk.Label(L500_0_adultwindow, image=L500_0_img)
     L500_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_0_YES_button = tk.Button(L500_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank8_page)
     L500_0_NO_button  = tk.Button(L500_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L500_10)

     L500_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_0_adultwindow.mainloop()

  # blank8
  def showadult_blank8_page():
     blank8_adultwindow = tk.Toplevel()
     blank8_adultwindow.geometry("800x480")
     blank8_adultwindow.resizable(False, False)
     blank8_adultwindow.title("blank8")

     def warning8_page():
      blank8_adultwindow.destroy() 
      showadult_warning8_page()

     pygame.mixer.init()
     B1=None

     def playadult_blank8toL1000_0():
      global B1
      B1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      blank8_adultwindow.destroy()
      showadult_L1000_0_page()
     
     blank8_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank8_label = tk.Label(blank8_adultwindow , image=blank8_img)
     blank8_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank8_YES_button = tk.Button(blank8_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning8_page)
     blank8_NO_button= tk.Button(blank8_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank8toL1000_0)

     blank8_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank8_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank8_adultwindow.mainloop()

  # warning8
  def showadult_warning8_page():
      warning8_adultwindow = tk.Toplevel()
      warning8_adultwindow.geometry("800x480")
      warning8_adultwindow.resizable(False, False)
      warning8_adultwindow.title("warning8")
      
      warning8_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning8_label = tk.Label(warning8_adultwindow, image=warning8_image)
      warning8_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning8toL500_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
        pygame.mixer.music.play()
        warning8_adultwindow.destroy()
        showadult_r250_0_page()

      warning8_button = tk.Button(warning8_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning8toL500_0)
      warning8_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning8_adultwindow.mainloop()

  # L500_10 page
  def showadult_L500_10_page():
     L500_10_adultwindow = tk.Toplevel()
     L500_10_adultwindow.geometry("800x480")
     L500_10_adultwindow.resizable(False, False)
     L500_10_adultwindow.title("L500_10")

     pygame.mixer.init()

     def playadult_L500_10toL500_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_20_L.mp3")
      pygame.mixer.music.play()
      L500_10_adultwindow.destroy()
      showadult_L500_20_page()

     pygame.mixer.init()

     def openadult__L500_10toL1000_0():
      global B1
      B1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_10_adultwindow.destroy()
      showadult_L1000_0_page()

     L500_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L500_10_label = tk.Label(L500_10_adultwindow, image=L500_10_img)
     L500_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_10_YES_button = tk.Button(L500_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L500_10toL1000_0)
     L500_10_NO_button  = tk.Button(L500_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L500_10toL500_20)

     L500_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_10_adultwindow.mainloop()

  # L500_20 page
  def showadult_L500_20_page():
     L500_20_adultwindow = tk.Toplevel()
     L500_20_adultwindow.geometry("800x480")
     L500_20_adultwindow.resizable(False, False)
     L500_20_adultwindow.title("L500_20")

     pygame.mixer.init()

     def playadult_L500_20toL500_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_30_L.mp3")
      pygame.mixer.music.play()
      L500_20_adultwindow.destroy()
      showadult_L500_30_page()

     pygame.mixer.init()

     def openadult__L500_20toL1000_0():
      global B1
      B1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_20_adultwindow.destroy()
      showadult_L1000_0_page()

     L500_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L500_20_label = tk.Label(L500_20_adultwindow, image=L500_20_img)
     L500_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_20_YES_button = tk.Button(L500_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L500_20toL1000_0)
     L500_20_NO_button  = tk.Button(L500_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L500_20toL500_30)

     L500_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_20_adultwindow.mainloop()

  # L500_30 page
  def showadult_L500_30_page():
     L500_30_adultwindow = tk.Toplevel()
     L500_30_adultwindow.geometry("800x480")
     L500_30_adultwindow.resizable(False, False)
     L500_30_adultwindow.title("L500_30")

     pygame.mixer.init()

     def playadult_L500_30toL500_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_40_L.mp3")
      pygame.mixer.music.play()
      L500_30_adultwindow.destroy()
      showadult_L500_40_page()

     pygame.mixer.init()

     def openadult__L500_30toL1000_0():
      global B1
      B1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_30_adultwindow.destroy()
      showadult_L1000_0_page()

     L500_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L500_30_label = tk.Label(L500_30_adultwindow, image=L500_30_img)
     L500_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_30_YES_button = tk.Button(L500_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L500_30toL1000_0)
     L500_30_NO_button  = tk.Button(L500_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L500_30toL500_40)

     L500_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_30_adultwindow.mainloop()

  # L500_40 page
  def showadult_L500_40_page():
     L500_40_adultwindow = tk.Toplevel()
     L500_40_adultwindow.geometry("800x480")
     L500_40_adultwindow.resizable(False, False)
     L500_40_adultwindow.title("L500_40")

     pygame.mixer.init()

     def playadult_L500_40toL500_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_50_L.mp3")
      pygame.mixer.music.play()
      L500_40_adultwindow.destroy()
      showadult_L500_50_page()

     pygame.mixer.init()

     def openadult__L500_40toL1000_0():
      global B1
      B1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_40_adultwindow.destroy()
      showadult_L1000_0_page()

     L500_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L500_40_label = tk.Label(L500_40_adultwindow, image=L500_40_img)
     L500_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_40_YES_button = tk.Button(L500_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L500_40toL1000_0)
     L500_40_NO_button  = tk.Button(L500_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L500_40toL500_50)

     L500_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_40_adultwindow.mainloop()

  # L500_50 page
  def showadult_L500_50_page():
     L500_50_adultwindow = tk.Toplevel()
     L500_50_adultwindow.geometry("800x480")
     L500_50_adultwindow.resizable(False, False)
     L500_50_adultwindow.title("L500_50")

     pygame.mixer.init()

     def playadult_L500_50toL500_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_60_L.mp3")
      pygame.mixer.music.play()
      L500_50_adultwindow.destroy()
      showadult_L500_60_page()

     pygame.mixer.init()

     def openadult__L500_50toL1000_0():
      global B1
      B1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_50_adultwindow.destroy()
      showadult_L1000_0_page()

     L500_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L500_50_label = tk.Label(L500_50_adultwindow, image=L500_50_img)
     L500_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_50_YES_button = tk.Button(L500_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L500_50toL1000_0)
     L500_50_NO_button  = tk.Button(L500_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L500_50toL500_60)

     L500_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_50_adultwindow.mainloop()

  # L500_60 page
  def showadult_L500_60_page():
     L500_60_adultwindow = tk.Toplevel()
     L500_60_adultwindow.geometry("800x480")
     L500_60_adultwindow.resizable(False, False)
     L500_60_adultwindow.title("L500_60")

     pygame.mixer.init()

     def playadult_L500_60toL500_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_70_L.mp3")
      pygame.mixer.music.play()
      L500_60_adultwindow.destroy()
      showadult_L500_70_page()

     pygame.mixer.init()

     def openadult__L500_60toL1000_0():
      global B1
      B1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_60_adultwindow.destroy()
      showadult_L1000_0_page()

     L500_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L500_60_label = tk.Label(L500_60_adultwindow, image=L500_60_img)
     L500_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_60_YES_button = tk.Button(L500_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L500_60toL1000_0)
     L500_60_NO_button  = tk.Button(L500_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L500_60toL500_70)

     L500_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_60_adultwindow.mainloop()

  # L500_70 page
  def showadult_L500_70_page():
     L500_70_adultwindow = tk.Toplevel()
     L500_70_adultwindow.geometry("800x480")
     L500_70_adultwindow.resizable(False, False)
     L500_70_adultwindow.title("L500_70")

     pygame.mixer.init()

     def playadult_L500_70toL500_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\500_80_L.mp3")
      pygame.mixer.music.play()
      L500_70_adultwindow.destroy()
      showadult_L500_80_page()

     pygame.mixer.init()

     def openadult__L500_70toL1000_0():
      global B1
      B1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_70_adultwindow.destroy()
      showadult_L1000_0_page()

     L500_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L500_70_label = tk.Label(L500_70_adultwindow, image=L500_70_img)
     L500_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_70_YES_button = tk.Button(L500_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L500_70toL1000_0)
     L500_70_NO_button  = tk.Button(L500_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L500_70toL500_80)

     L500_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_70_adultwindow.mainloop()

  # L500_80 page
  def showadult_L500_80_page():
     L500_80_adultwindow = tk.Toplevel()
     L500_80_adultwindow.geometry("800x480")
     L500_80_adultwindow.resizable(False, False)
     L500_80_adultwindow.title("L500_80")

     pygame.mixer.init()

     def playadult_L500_80toL1000_0():
      global B1
      B1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_80_adultwindow.destroy()
      showadult_L1000_0_page()

     pygame.mixer.init()

     def openadult__L500_80toL1000_00():
      global B1
      B1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_0_L.mp3")
      pygame.mixer.music.play()
      L500_80_adultwindow.destroy()
      showadult_L1000_0_page()

     L500_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L500_80_label = tk.Label(L500_80_adultwindow, image=L500_80_img)
     L500_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L500_80_YES_button = tk.Button(L500_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L500_80toL1000_00)
     L500_80_NO_button  = tk.Button(L500_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L500_80toL1000_0)

     L500_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L500_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L500_80_adultwindow.mainloop()

  # L1000_0 page
  def showadult_L1000_0_page():
     L1000_0_adultwindow = tk.Toplevel()
     L1000_0_adultwindow.geometry("800x480")
     L1000_0_adultwindow.resizable(False, False)
     L1000_0_adultwindow.title("L1000_0")

     def blank9_page():
      L1000_0_adultwindow.destroy() 
      showadult_blank9_page()
      
     pygame.mixer.init()

     def playadult_L1000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_10_L.mp3")
      pygame.mixer.music.play()
      L1000_0_adultwindow.destroy()
      showadult_L1000_10_page()

     L1000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L1000_0_label = tk.Label(L1000_0_adultwindow, image=L1000_0_img)
     L1000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_0_YES_button = tk.Button(L1000_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank9_page)
     L1000_0_NO_button  = tk.Button(L1000_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L1000_10)

     L1000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_0_adultwindow.mainloop()

  # blank9
  def showadult_blank9_page():
     blank9_adultwindow = tk.Toplevel()
     blank9_adultwindow.geometry("800x480")
     blank9_adultwindow.resizable(False, False)
     blank9_adultwindow.title("blank9")

     def warning9_page():
      blank9_adultwindow.destroy() 
      showadult_warning9_page()

     pygame.mixer.init()
     C1 = None

     def playadult_blank9toL2000_0():
      global C1
      C1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      blank9_adultwindow.destroy()
      showadult_L2000_0_page()
     
     blank9_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank9_label = tk.Label(blank9_adultwindow , image=blank9_img)
     blank9_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank9_YES_button = tk.Button(blank9_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning9_page)
     blank9_NO_button= tk.Button(blank9_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank9toL2000_0)

     blank9_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank9_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank9_adultwindow.mainloop()

  # warning9
  def showadult_warning9_page():
      warning9_adultwindow = tk.Toplevel()
      warning9_adultwindow.geometry("800x480")
      warning9_adultwindow.resizable(False, False)
      warning9_adultwindow.title("warning9")
      
      warning9_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning9_label = tk.Label(warning9_adultwindow, image=warning9_image)
      warning9_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning9toL1000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
        pygame.mixer.music.play()
        warning9_adultwindow.destroy()
        showadult_r250_0_page()

      warning9_button = tk.Button(warning9_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning9toL1000_0)
      warning9_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning9_adultwindow.mainloop()

  # L1000_10 page
  def showadult_L1000_10_page():
     L1000_10_adultwindow = tk.Toplevel()
     L1000_10_adultwindow.geometry("800x480")
     L1000_10_adultwindow.resizable(False, False)
     L1000_10_adultwindow.title("L1000_10")

     pygame.mixer.init()

     def playadult_L1000_10toL1000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_20_L.mp3")
      pygame.mixer.music.play()
      L1000_10_adultwindow.destroy()
      showadult_L1000_20_page()

     pygame.mixer.init()

     def openadult__L1000_10toL2000_0():
      global C1
      C1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_10_adultwindow.destroy()
      showadult_L2000_0_page()

     L1000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L1000_10_label = tk.Label(L1000_10_adultwindow, image=L1000_10_img)
     L1000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_10_YES_button = tk.Button(L1000_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L1000_10toL2000_0)
     L1000_10_NO_button  = tk.Button(L1000_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L1000_10toL1000_20)

     L1000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_10_adultwindow.mainloop()

  # L1000_20 page
  def showadult_L1000_20_page():
     L1000_20_adultwindow = tk.Toplevel()
     L1000_20_adultwindow.geometry("800x480")
     L1000_20_adultwindow.resizable(False, False)
     L1000_20_adultwindow.title("L1000_20")

     pygame.mixer.init()

     def playadult_L1000_20toL1000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_30_L.mp3")
      pygame.mixer.music.play()
      L1000_20_adultwindow.destroy()
      showadult_L1000_30_page()

     pygame.mixer.init()

     def openadult__L1000_20toL2000_0():
      global C1
      C1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_20_adultwindow.destroy()
      showadult_L2000_0_page()

     L1000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L1000_20_label = tk.Label(L1000_20_adultwindow, image=L1000_20_img)
     L1000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_20_YES_button = tk.Button(L1000_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L1000_20toL2000_0)
     L1000_20_NO_button  = tk.Button(L1000_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L1000_20toL1000_30)

     L1000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_20_adultwindow.mainloop()

  # L1000_30 page
  def showadult_L1000_30_page():
     L1000_30_adultwindow = tk.Toplevel()
     L1000_30_adultwindow.geometry("800x480")
     L1000_30_adultwindow.resizable(False, False)
     L1000_30_adultwindow.title("L1000_30")

     pygame.mixer.init()

     def playadult_L1000_30toL1000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_40_L.mp3")
      pygame.mixer.music.play()
      L1000_30_adultwindow.destroy()
      showadult_L1000_40_page()

     pygame.mixer.init()

     def openadult__L1000_30toL2000_0():
      global C1
      C1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_30_adultwindow.destroy()
      showadult_L2000_0_page()

     L1000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L1000_30_label = tk.Label(L1000_30_adultwindow, image=L1000_30_img)
     L1000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_30_YES_button = tk.Button(L1000_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L1000_30toL2000_0)
     L1000_30_NO_button  = tk.Button(L1000_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L1000_30toL1000_40)

     L1000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_30_adultwindow.mainloop()

  # L1000_40 page
  def showadult_L1000_40_page():
     L1000_40_adultwindow = tk.Toplevel()
     L1000_40_adultwindow.geometry("800x480")
     L1000_40_adultwindow.resizable(False, False)
     L1000_40_adultwindow.title("L1000_40")

     pygame.mixer.init()

     def playadult_L1000_40toL1000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_50_L.mp3")
      pygame.mixer.music.play()
      L1000_40_adultwindow.destroy()
      showadult_L1000_50_page()

     pygame.mixer.init()

     def openadult__L1000_40toL2000_0():
      global C1
      C1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_40_adultwindow.destroy()
      showadult_L2000_0_page()

     L1000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L1000_40_label = tk.Label(L1000_40_adultwindow, image=L1000_40_img)
     L1000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_40_YES_button = tk.Button(L1000_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L1000_40toL2000_0)
     L1000_40_NO_button  = tk.Button(L1000_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L1000_40toL1000_50)

     L1000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_40_adultwindow.mainloop()

  # L1000_50 page
  def showadult_L1000_50_page():
     L1000_50_adultwindow = tk.Toplevel()
     L1000_50_adultwindow.geometry("800x480")
     L1000_50_adultwindow.resizable(False, False)
     L1000_50_adultwindow.title("L1000_50")

     pygame.mixer.init()

     def playadult_L1000_50toL1000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_60_L.mp3")
      pygame.mixer.music.play()
      L1000_50_adultwindow.destroy()
      showadult_L1000_60_page()

     pygame.mixer.init()

     def openadult__L1000_50toL2000_0():
      global C1
      C1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_50_adultwindow.destroy()
      showadult_L2000_0_page()

     L1000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L1000_50_label = tk.Label(L1000_50_adultwindow, image=L1000_50_img)
     L1000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_50_YES_button = tk.Button(L1000_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L1000_50toL2000_0)
     L1000_50_NO_button  = tk.Button(L1000_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L1000_50toL1000_60)

     L1000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_50_adultwindow.mainloop()

  # L1000_60 page
  def showadult_L1000_60_page():
     L1000_60_adultwindow = tk.Toplevel()
     L1000_60_adultwindow.geometry("800x480")
     L1000_60_adultwindow.resizable(False, False)
     L1000_60_adultwindow.title("L1000_60")

     pygame.mixer.init()

     def playadult_L1000_60toL1000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_70_L.mp3")
      pygame.mixer.music.play()
      L1000_60_adultwindow.destroy()
      showadult_L1000_70_page()

     pygame.mixer.init()

     def openadult__L1000_60toL2000_0():
      global C1
      C1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_60_adultwindow.destroy()
      showadult_L2000_0_page()

     L1000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L1000_60_label = tk.Label(L1000_60_adultwindow, image=L1000_60_img)
     L1000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_60_YES_button = tk.Button(L1000_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L1000_60toL2000_0)
     L1000_60_NO_button  = tk.Button(L1000_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L1000_60toL1000_70)

     L1000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_60_adultwindow.mainloop()

  # L1000_70 page
  def showadult_L1000_70_page():
     L1000_70_adultwindow = tk.Toplevel()
     L1000_70_adultwindow.geometry("800x480")
     L1000_70_adultwindow.resizable(False, False)
     L1000_70_adultwindow.title("L1000_70")

     pygame.mixer.init()

     def playadult_L1000_70toL1000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\1000_80_L.mp3")
      pygame.mixer.music.play()
      L1000_70_adultwindow.destroy()
      showadult_L1000_80_page()

     pygame.mixer.init()

     def openadult__L1000_70toL2000_0():
      global C1
      C1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_70_adultwindow.destroy()
      showadult_L2000_0_page()

     L1000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L1000_70_label = tk.Label(L1000_70_adultwindow, image=L1000_70_img)
     L1000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_70_YES_button = tk.Button(L1000_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L1000_70toL2000_0)
     L1000_70_NO_button  = tk.Button(L1000_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L1000_70toL1000_80)

     L1000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_70_adultwindow.mainloop()

  # L1000_80 page
  def showadult_L1000_80_page():
     L1000_80_adultwindow = tk.Toplevel()
     L1000_80_adultwindow.geometry("800x480")
     L1000_80_adultwindow.resizable(False, False)
     L1000_80_adultwindow.title("L1000_80")

     pygame.mixer.init()

     def playadult_L1000_80toL2000_0():
      global C1
      C1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_80_adultwindow.destroy()
      showadult_L2000_0_page()

     pygame.mixer.init()

     def openadult__L1000_80toL2000_00():
      global C1
      C1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_0_L.mp3")
      pygame.mixer.music.play()
      L1000_80_adultwindow.destroy()
      showadult_L2000_0_page()

     L1000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L1000_80_label = tk.Label(L1000_80_adultwindow, image=L1000_80_img)
     L1000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L1000_80_YES_button = tk.Button(L1000_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L1000_80toL2000_00)
     L1000_80_NO_button  = tk.Button(L1000_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L1000_80toL2000_0)

     L1000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L1000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L1000_80_adultwindow.mainloop()

  # L2000_0 page
  def showadult_L2000_0_page():
     L2000_0_adultwindow = tk.Toplevel()
     L2000_0_adultwindow.geometry("800x480")
     L2000_0_adultwindow.resizable(False, False)
     L2000_0_adultwindow.title("L2000_0")

     def blank10_page():
      L2000_0_adultwindow.destroy() 
      showadult_blank10_page()
      
     pygame.mixer.init()

     def playadult_L2000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_10_L.mp3")
      pygame.mixer.music.play()
      L2000_0_adultwindow.destroy()
      showadult_L2000_10_page()

     L2000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L2000_0_label = tk.Label(L2000_0_adultwindow, image=L2000_0_img)
     L2000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_0_YES_button = tk.Button(L2000_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank10_page)
     L2000_0_NO_button  = tk.Button(L2000_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L2000_10)

     L2000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_0_adultwindow.mainloop()

  # blank10
  def showadult_blank10_page():
     blank10_adultwindow = tk.Toplevel()
     blank10_adultwindow.geometry("800x480")
     blank10_adultwindow.resizable(False, False)
     blank10_adultwindow.title("blank10")

     def warning10_page():
      blank10_adultwindow.destroy() 
      showadult_warning10_page()

     pygame.mixer.init()
     D1 =None

     def playadult_blank10toL4000_0():
      global D1
      D1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      blank10_adultwindow.destroy()
      showadult_L4000_0_page()
     
     blank10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank10_label = tk.Label(blank10_adultwindow , image=blank10_img)
     blank10_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank10_YES_button = tk.Button(blank10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning10_page)
     blank10_NO_button= tk.Button(blank10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank10toL4000_0)

     blank10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank10_adultwindow.mainloop()

  # warning10
  def showadult_warning10_page():
      warning10_adultwindow = tk.Toplevel()
      warning10_adultwindow.geometry("800x480")
      warning10_adultwindow.resizable(False, False)
      warning10_adultwindow.title("warning10")
      
      warning10_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning10_label = tk.Label(warning10_adultwindow, image=warning10_image)
      warning10_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning10toL2000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
        pygame.mixer.music.play()
        warning10_adultwindow.destroy()
        showadult_r250_0_page()

      warning10_button = tk.Button(warning10_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning10toL2000_0)
      warning10_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning10_adultwindow.mainloop()

  # L2000_10 page
  def showadult_L2000_10_page():
     L2000_10_adultwindow = tk.Toplevel()
     L2000_10_adultwindow.geometry("800x480")
     L2000_10_adultwindow.resizable(False, False)
     L2000_10_adultwindow.title("L2000_10")

     pygame.mixer.init()

     def playadult_L2000_10toL2000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_20_L.mp3")
      pygame.mixer.music.play()
      L2000_10_adultwindow.destroy()
      showadult_L2000_20_page()

     pygame.mixer.init()

     def openadult__L2000_10toL4000_0():
      global D1
      D1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_10_adultwindow.destroy()
      showadult_L4000_0_page()

     L2000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L2000_10_label = tk.Label(L2000_10_adultwindow, image=L2000_10_img)
     L2000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_10_YES_button = tk.Button(L2000_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L2000_10toL4000_0)
     L2000_10_NO_button  = tk.Button(L2000_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L2000_10toL2000_20)

     L2000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_10_adultwindow.mainloop()

  # L2000_20 page
  def showadult_L2000_20_page():
     L2000_20_adultwindow = tk.Toplevel()
     L2000_20_adultwindow.geometry("800x480")
     L2000_20_adultwindow.resizable(False, False)
     L2000_20_adultwindow.title("L2000_20")

     pygame.mixer.init()

     def playadult_L2000_20toL2000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_30_L.mp3")
      pygame.mixer.music.play()
      L2000_20_adultwindow.destroy()
      showadult_L2000_30_page()

     pygame.mixer.init()

     def openadult__L2000_20toL4000_0():
      global D1
      D1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_20_adultwindow.destroy()
      showadult_L4000_0_page()

     L2000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L2000_20_label = tk.Label(L2000_20_adultwindow, image=L2000_20_img)
     L2000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_20_YES_button = tk.Button(L2000_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L2000_20toL4000_0)
     L2000_20_NO_button  = tk.Button(L2000_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L2000_20toL2000_30)

     L2000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_20_adultwindow.mainloop()

  # L2000_30 page
  def showadult_L2000_30_page():
     L2000_30_adultwindow = tk.Toplevel()
     L2000_30_adultwindow.geometry("800x480")
     L2000_30_adultwindow.resizable(False, False)
     L2000_30_adultwindow.title("L2000_30")

     pygame.mixer.init()

     def playadult_L2000_30toL2000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_40_L.mp3")
      pygame.mixer.music.play()
      L2000_30_adultwindow.destroy()
      showadult_L2000_40_page()

     pygame.mixer.init()

     def openadult__L2000_30toL4000_0():
      global D1
      D1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_30_adultwindow.destroy()
      showadult_L4000_0_page()

     L2000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L2000_30_label = tk.Label(L2000_30_adultwindow, image=L2000_30_img)
     L2000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_30_YES_button = tk.Button(L2000_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L2000_30toL4000_0)
     L2000_30_NO_button  = tk.Button(L2000_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L2000_30toL2000_40)

     L2000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_30_adultwindow.mainloop()

  # L2000_40 page
  def showadult_L2000_40_page():
     L2000_40_adultwindow = tk.Toplevel()
     L2000_40_adultwindow.geometry("800x480")
     L2000_40_adultwindow.resizable(False, False)
     L2000_40_adultwindow.title("L2000_40")

     pygame.mixer.init()

     def playadult_L2000_40toL2000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_50_L.mp3")
      pygame.mixer.music.play()
      L2000_40_adultwindow.destroy()
      showadult_L2000_50_page()

     pygame.mixer.init()

     def openadult__L2000_40toL4000_0():
      global D1
      D1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_40_adultwindow.destroy()
      showadult_L4000_0_page()

     L2000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L2000_40_label = tk.Label(L2000_40_adultwindow, image=L2000_40_img)
     L2000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_40_YES_button = tk.Button(L2000_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L2000_40toL4000_0)
     L2000_40_NO_button  = tk.Button(L2000_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L2000_40toL2000_50)

     L2000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_40_adultwindow.mainloop()

  # L2000_50 page
  def showadult_L2000_50_page():
     L2000_50_adultwindow = tk.Toplevel()
     L2000_50_adultwindow.geometry("800x480")
     L2000_50_adultwindow.resizable(False, False)
     L2000_50_adultwindow.title("L2000_50")

     pygame.mixer.init()

     def playadult_L2000_50toL2000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_60_L.mp3")
      pygame.mixer.music.play()
      L2000_50_adultwindow.destroy()
      showadult_L2000_60_page()

     pygame.mixer.init()

     def openadult__L2000_50toL4000_0():
      global D1
      D1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_50_adultwindow.destroy()
      showadult_L4000_0_page()

     L2000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L2000_50_label = tk.Label(L2000_50_adultwindow, image=L2000_50_img)
     L2000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_50_YES_button = tk.Button(L2000_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L2000_50toL4000_0)
     L2000_50_NO_button  = tk.Button(L2000_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L2000_50toL2000_60)

     L2000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_50_adultwindow.mainloop()

  # L2000_60 page
  def showadult_L2000_60_page():
     L2000_60_adultwindow = tk.Toplevel()
     L2000_60_adultwindow.geometry("800x480")
     L2000_60_adultwindow.resizable(False, False)
     L2000_60_adultwindow.title("L2000_60")

     pygame.mixer.init()

     def playadult_L2000_60toL2000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_70_L.mp3")
      pygame.mixer.music.play()
      L2000_60_adultwindow.destroy()
      showadult_L2000_70_page()

     pygame.mixer.init()

     def openadult__L2000_60toL4000_0():
      global D1
      D1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_60_adultwindow.destroy()
      showadult_L4000_0_page()

     L2000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L2000_60_label = tk.Label(L2000_60_adultwindow, image=L2000_60_img)
     L2000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_60_YES_button = tk.Button(L2000_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L2000_60toL4000_0)
     L2000_60_NO_button  = tk.Button(L2000_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L2000_60toL2000_70)

     L2000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_60_adultwindow.mainloop()

  # L2000_70 page
  def showadult_L2000_70_page():
     L2000_70_adultwindow = tk.Toplevel()
     L2000_70_adultwindow.geometry("800x480")
     L2000_70_adultwindow.resizable(False, False)
     L2000_70_adultwindow.title("L2000_70")

     pygame.mixer.init()

     def playadult_L2000_70toL2000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\2000_80_L.mp3")
      pygame.mixer.music.play()
      L2000_70_adultwindow.destroy()
      showadult_L2000_80_page()

     pygame.mixer.init()

     def openadult__L2000_70toL4000_0():
      global D1
      D1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_70_adultwindow.destroy()
      showadult_L4000_0_page()

     L2000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L2000_70_label = tk.Label(L2000_70_adultwindow, image=L2000_70_img)
     L2000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_70_YES_button = tk.Button(L2000_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L2000_70toL4000_0)
     L2000_70_NO_button  = tk.Button(L2000_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L2000_70toL2000_80)

     L2000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_70_adultwindow.mainloop()

  # L2000_80 page
  def showadult_L2000_80_page():
     L2000_80_adultwindow = tk.Toplevel()
     L2000_80_adultwindow.geometry("800x480")
     L2000_80_adultwindow.resizable(False, False)
     L2000_80_adultwindow.title("L2000_80")

     pygame.mixer.init()

     def playadult_L2000_80toL4000_0():
      global D1
      D1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_80_adultwindow.destroy()
      showadult_L4000_0_page()

     pygame.mixer.init()

     def openadult__L2000_80toL4000_00():
      global D1
      D1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_0_L.mp3")
      pygame.mixer.music.play()
      L2000_80_adultwindow.destroy()
      showadult_L4000_0_page()

     L2000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L2000_80_label = tk.Label(L2000_80_adultwindow, image=L2000_80_img)
     L2000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L2000_80_YES_button = tk.Button(L2000_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L2000_80toL4000_00)
     L2000_80_NO_button  = tk.Button(L2000_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L2000_80toL4000_0)

     L2000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L2000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L2000_80_adultwindow.mainloop()

  # L4000_0 page
  def showadult_L4000_0_page():
     L4000_0_adultwindow = tk.Toplevel()
     L4000_0_adultwindow.geometry("800x480")
     L4000_0_adultwindow.resizable(False, False)
     L4000_0_adultwindow.title("L4000_0")

     def blank11_page():
      L4000_0_adultwindow.destroy() 
      showadult_blank11_page()
      
     pygame.mixer.init()

     def playadult_L4000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_10_L.mp3")
      pygame.mixer.music.play()
      L4000_0_adultwindow.destroy()
      showadult_L4000_10_page()

     L4000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L4000_0_label = tk.Label(L4000_0_adultwindow, image=L4000_0_img)
     L4000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_0_YES_button = tk.Button(L4000_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank11_page)
     L4000_0_NO_button  = tk.Button(L4000_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L4000_10)

     L4000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_0_adultwindow.mainloop()

  # blank11
  def showadult_blank11_page():
     blank11_adultwindow = tk.Toplevel()
     blank11_adultwindow.geometry("800x480")
     blank11_adultwindow.resizable(False, False)
     blank11_adultwindow.title("blank11")

     def warning11_page():
      blank11_adultwindow.destroy() 
      showadult_warning11_page()

     pygame.mixer.init()
     E1=None
     def playadult_blank11toL8000_0():
      global E1
      E1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      blank11_adultwindow.destroy()
      showadult_L8000_0_page()
     
     blank11_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank11_label = tk.Label(blank11_adultwindow , image=blank11_img)
     blank11_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank11_YES_button = tk.Button(blank11_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning11_page)
     blank11_NO_button= tk.Button(blank11_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank11toL8000_0)

     blank11_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank11_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank11_adultwindow.mainloop()

  # warning11
  def showadult_warning11_page():
      warning11_adultwindow = tk.Toplevel()
      warning11_adultwindow.geometry("800x480")
      warning11_adultwindow.resizable(False, False)
      warning11_adultwindow.title("warning11")
      
      warning11_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning11_label = tk.Label(warning11_adultwindow, image=warning11_image)
      warning11_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning11toL4000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
        pygame.mixer.music.play()
        warning11_adultwindow.destroy()
        showadult_r250_0_page()

      warning11_button = tk.Button(warning11_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning11toL4000_0)
      warning11_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning11_adultwindow.mainloop()

  # L4000_10 page
  def showadult_L4000_10_page():
     L4000_10_adultwindow = tk.Toplevel()
     L4000_10_adultwindow.geometry("800x480")
     L4000_10_adultwindow.resizable(False, False)
     L4000_10_adultwindow.title("L4000_10")

     pygame.mixer.init()

     def playadult_L4000_10toL4000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_20_L.mp3")
      pygame.mixer.music.play()
      L4000_10_adultwindow.destroy()
      showadult_L4000_20_page()

     pygame.mixer.init()

     def openadult__L4000_10toL8000_0():
      global E1
      E1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_10_adultwindow.destroy()
      showadult_L8000_0_page()

     L4000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L4000_10_label = tk.Label(L4000_10_adultwindow, image=L4000_10_img)
     L4000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_10_YES_button = tk.Button(L4000_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L4000_10toL8000_0)
     L4000_10_NO_button  = tk.Button(L4000_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L4000_10toL4000_20)

     L4000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_10_adultwindow.mainloop()

  # L4000_20 page
  def showadult_L4000_20_page():
     L4000_20_adultwindow = tk.Toplevel()
     L4000_20_adultwindow.geometry("800x480")
     L4000_20_adultwindow.resizable(False, False)
     L4000_20_adultwindow.title("L4000_20")

     pygame.mixer.init()

     def playadult_L4000_20toL4000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_30_L.mp3")
      pygame.mixer.music.play()
      L4000_20_adultwindow.destroy()
      showadult_L4000_30_page()

     pygame.mixer.init()

     def openadult__L4000_20toL8000_0():
      global E1
      E1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_20_adultwindow.destroy()
      showadult_L8000_0_page()

     L4000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L4000_20_label = tk.Label(L4000_20_adultwindow, image=L4000_20_img)
     L4000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_20_YES_button = tk.Button(L4000_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L4000_20toL8000_0)
     L4000_20_NO_button  = tk.Button(L4000_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L4000_20toL4000_30)

     L4000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_20_adultwindow.mainloop()

  # L4000_30 page
  def showadult_L4000_30_page():
     L4000_30_adultwindow = tk.Toplevel()
     L4000_30_adultwindow.geometry("800x480")
     L4000_30_adultwindow.resizable(False, False)
     L4000_30_adultwindow.title("L4000_30")

     pygame.mixer.init()

     def playadult_L4000_30toL4000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_40_L.mp3")
      pygame.mixer.music.play()
      L4000_30_adultwindow.destroy()
      showadult_L4000_40_page()

     pygame.mixer.init()

     def openadult__L4000_30toL8000_0():
      global E1
      E1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_30_adultwindow.destroy()
      showadult_L8000_0_page()

     L4000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L4000_30_label = tk.Label(L4000_30_adultwindow, image=L4000_30_img)
     L4000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_30_YES_button = tk.Button(L4000_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L4000_30toL8000_0)
     L4000_30_NO_button  = tk.Button(L4000_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L4000_30toL4000_40)

     L4000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_30_adultwindow.mainloop()

  # L4000_40 page
  def showadult_L4000_40_page():
     L4000_40_adultwindow = tk.Toplevel()
     L4000_40_adultwindow.geometry("800x480")
     L4000_40_adultwindow.resizable(False, False)
     L4000_40_adultwindow.title("L4000_40")

     pygame.mixer.init()

     def playadult_L4000_40toL4000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_50_L.mp3")
      pygame.mixer.music.play()
      L4000_40_adultwindow.destroy()
      showadult_L4000_50_page()

     pygame.mixer.init()

     def openadult__L4000_40toL8000_0():
      global E1
      E1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_40_adultwindow.destroy()
      showadult_L8000_0_page()

     L4000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L4000_40_label = tk.Label(L4000_40_adultwindow, image=L4000_40_img)
     L4000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_40_YES_button = tk.Button(L4000_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L4000_40toL8000_0)
     L4000_40_NO_button  = tk.Button(L4000_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L4000_40toL4000_50)

     L4000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_40_adultwindow.mainloop()

  # L4000_50 page
  def showadult_L4000_50_page():
     L4000_50_adultwindow = tk.Toplevel()
     L4000_50_adultwindow.geometry("800x480")
     L4000_50_adultwindow.resizable(False, False)
     L4000_50_adultwindow.title("L4000_50")

     pygame.mixer.init()

     def playadult_L4000_50toL4000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_60_L.mp3")
      pygame.mixer.music.play()
      L4000_50_adultwindow.destroy()
      showadult_L4000_60_page()

     pygame.mixer.init()

     def openadult__L4000_50toL8000_0():
      global E1
      E1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_50_adultwindow.destroy()
      showadult_L8000_0_page()

     L4000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L4000_50_label = tk.Label(L4000_50_adultwindow, image=L4000_50_img)
     L4000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_50_YES_button = tk.Button(L4000_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L4000_50toL8000_0)
     L4000_50_NO_button  = tk.Button(L4000_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L4000_50toL4000_60)

     L4000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_50_adultwindow.mainloop()

  # L4000_60 page
  def showadult_L4000_60_page():
     L4000_60_adultwindow = tk.Toplevel()
     L4000_60_adultwindow.geometry("800x480")
     L4000_60_adultwindow.resizable(False, False)
     L4000_60_adultwindow.title("L4000_60")

     pygame.mixer.init()

     def playadult_L4000_60toL4000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_70_L.mp3")
      pygame.mixer.music.play()
      L4000_60_adultwindow.destroy()
      showadult_L4000_70_page()

     pygame.mixer.init()

     def openadult__L4000_60toL8000_0():
      global E1
      E1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_60_adultwindow.destroy()
      showadult_L8000_0_page()

     L4000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L4000_60_label = tk.Label(L4000_60_adultwindow, image=L4000_60_img)
     L4000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_60_YES_button = tk.Button(L4000_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L4000_60toL8000_0)
     L4000_60_NO_button  = tk.Button(L4000_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L4000_60toL4000_70)

     L4000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_60_adultwindow.mainloop()

  # L4000_70 page
  def showadult_L4000_70_page():
     L4000_70_adultwindow = tk.Toplevel()
     L4000_70_adultwindow.geometry("800x480")
     L4000_70_adultwindow.resizable(False, False)
     L4000_70_adultwindow.title("L4000_70")

     pygame.mixer.init()

     def playadult_L4000_70toL4000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\4000_80_L.mp3")
      pygame.mixer.music.play()
      L4000_70_adultwindow.destroy()
      showadult_L4000_80_page()

     pygame.mixer.init()

     def openadult__L4000_70toL8000_0():
      global E1
      E1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_70_adultwindow.destroy()
      showadult_L8000_0_page()

     L4000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L4000_70_label = tk.Label(L4000_70_adultwindow, image=L4000_70_img)
     L4000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_70_YES_button = tk.Button(L4000_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L4000_70toL8000_0)
     L4000_70_NO_button  = tk.Button(L4000_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L4000_70toL4000_80)

     L4000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_70_adultwindow.mainloop()

  # L4000_80 page
  def showadult_L4000_80_page():
     L4000_80_adultwindow = tk.Toplevel()
     L4000_80_adultwindow.geometry("800x480")
     L4000_80_adultwindow.resizable(False, False)
     L4000_80_adultwindow.title("L4000_80")

     pygame.mixer.init()

     def playadult_L4000_80toL8000_0():
      global E1
      E1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_80_adultwindow.destroy()
      showadult_L8000_0_page()

     pygame.mixer.init()

     def openadult__L4000_80toL8000_00():
      global E1
      E1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_0_L.mp3")
      pygame.mixer.music.play()
      L4000_80_adultwindow.destroy()
      showadult_L8000_0_page()

     L4000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L4000_80_label = tk.Label(L4000_80_adultwindow, image=L4000_80_img)
     L4000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L4000_80_YES_button = tk.Button(L4000_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L4000_80toL8000_00)
     L4000_80_NO_button  = tk.Button(L4000_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L4000_80toL8000_0)

     L4000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L4000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L4000_80_adultwindow.mainloop()

  # L8000_0 page
  def showadult_L8000_0_page():
     L8000_0_adultwindow = tk.Toplevel()
     L8000_0_adultwindow.geometry("800x480")
     L8000_0_adultwindow.resizable(False, False)
     L8000_0_adultwindow.title("L8000_0")

     def blank12_page():
      L8000_0_adultwindow.destroy() 
      showadult_blank12_page()
      
     pygame.mixer.init()

     def playadult_L8000_10():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_10_L.mp3")
      pygame.mixer.music.play()
      L8000_0_adultwindow.destroy()
      showadult_L8000_10_page()

     L8000_0_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L8000_0_label = tk.Label(L8000_0_adultwindow, image=L8000_0_img)
     L8000_0_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_0_YES_button = tk.Button(L8000_0_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=blank12_page)
     L8000_0_NO_button  = tk.Button(L8000_0_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L8000_10)

     L8000_0_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_0_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_0_adultwindow.mainloop()

  # blank12
  def showadult_blank12_page():
     blank12_adultwindow = tk.Toplevel()
     blank12_adultwindow.geometry("800x480")
     blank12_adultwindow.resizable(False, False)
     blank12_adultwindow.title("blank12")

     def warning12_page():
      blank12_adultwindow.destroy() 
      showadult_warning12_page()

     pygame.mixer.init()
     F1=None

     def playadult_blank12tospeechtest_312():
      global F1
      F1 = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      blank12_adultwindow.destroy()
      showadult_speechtest_312_page()
     
     blank12_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     blank12_label = tk.Label(blank12_adultwindow , image=blank12_img)
     blank12_label.place(x=0, y=0, relwidth=1, relheight=1)

     blank12_YES_button = tk.Button(blank12_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=warning12_page)
     blank12_NO_button= tk.Button(blank12_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_blank12tospeechtest_312)

     blank12_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     blank12_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)


     blank12_adultwindow.mainloop()

  # warning12
  def showadult_warning12_page():
      warning12_adultwindow = tk.Toplevel()
      warning12_adultwindow.geometry("800x480")
      warning12_adultwindow.resizable(False, False)
      warning12_adultwindow.title("warning12")
      
      warning12_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\5blankadults.png")
      warning12_label = tk.Label(warning12_adultwindow, image=warning12_image)
      warning12_label.place(x=0, y=0, relwidth=1, relheight=1)

      pygame.mixer.init()

      def openadult_warning12toL8000_0():
        pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
        pygame.mixer.music.play()
        warning12_adultwindow.destroy()
        showadult_r250_0_page()

      warning12_button = tk.Button(warning12_adultwindow, text="RESTART TEST", font=("Comic Sans MS Bold", 19), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult_warning12toL8000_0)
      warning12_button.place(x=309, y=402, relwidth=0.24, relheight=0.062)
      
      warning12_adultwindow.mainloop()

  # L8000_10 page
  def showadult_L8000_10_page():
     L8000_10_adultwindow = tk.Toplevel()
     L8000_10_adultwindow.geometry("800x480")
     L8000_10_adultwindow.resizable(False, False)
     L8000_10_adultwindow.title("L8000_10")

     pygame.mixer.init()

     def playadult_L8000_10toL8000_20():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_20_L.mp3")
      pygame.mixer.music.play()
      L8000_10_adultwindow.destroy()
      showadult_L8000_20_page()

     pygame.mixer.init()

     def openadult__L8000_10tospeechtest_312():
      global F1
      F1 = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_10_adultwindow.destroy()
      showadult_speechtest_312_page()

     L8000_10_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L8000_10_label = tk.Label(L8000_10_adultwindow, image=L8000_10_img)
     L8000_10_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_10_YES_button = tk.Button(L8000_10_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L8000_10tospeechtest_312)
     L8000_10_NO_button  = tk.Button(L8000_10_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L8000_10toL8000_20)

     L8000_10_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_10_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_10_adultwindow.mainloop()

  # L8000_20 page
  def showadult_L8000_20_page():
     L8000_20_adultwindow = tk.Toplevel()
     L8000_20_adultwindow.geometry("800x480")
     L8000_20_adultwindow.resizable(False, False)
     L8000_20_adultwindow.title("L8000_20")

     pygame.mixer.init()

     def playadult_L8000_20toL8000_30():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_30_L.mp3")
      pygame.mixer.music.play()
      L8000_20_adultwindow.destroy()
      showadult_L8000_30_page()

     pygame.mixer.init()

     def openadult__L8000_20tospeechtest_312():
      global F1
      F1 = 2
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_20_adultwindow.destroy()
      showadult_speechtest_312_page()

     L8000_20_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L8000_20_label = tk.Label(L8000_20_adultwindow, image=L8000_20_img)
     L8000_20_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_20_YES_button = tk.Button(L8000_20_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L8000_20tospeechtest_312)
     L8000_20_NO_button  = tk.Button(L8000_20_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L8000_20toL8000_30)

     L8000_20_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_20_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_20_adultwindow.mainloop()

  # L8000_30 page
  def showadult_L8000_30_page():
     L8000_30_adultwindow = tk.Toplevel()
     L8000_30_adultwindow.geometry("800x480")
     L8000_30_adultwindow.resizable(False, False)
     L8000_30_adultwindow.title("L8000_30")

     pygame.mixer.init()

     def playadult_L8000_30toL8000_40():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_40_L.mp3")
      pygame.mixer.music.play()
      L8000_30_adultwindow.destroy()
      showadult_L8000_40_page()

     pygame.mixer.init()

     def openadult__L8000_30tospeechtest_312():
      global F1
      F1 = 3
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_30_adultwindow.destroy()
      showadult_speechtest_312_page()

     L8000_30_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L8000_30_label = tk.Label(L8000_30_adultwindow, image=L8000_30_img)
     L8000_30_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_30_YES_button = tk.Button(L8000_30_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L8000_30tospeechtest_312)
     L8000_30_NO_button  = tk.Button(L8000_30_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L8000_30toL8000_40)

     L8000_30_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_30_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_30_adultwindow.mainloop()

  # L8000_40 page
  def showadult_L8000_40_page():
     L8000_40_adultwindow = tk.Toplevel()
     L8000_40_adultwindow.geometry("800x480")
     L8000_40_adultwindow.resizable(False, False)
     L8000_40_adultwindow.title("L8000_40")

     pygame.mixer.init()

     def playadult_L8000_40toL8000_50():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_50_L.mp3")
      pygame.mixer.music.play()
      L8000_40_adultwindow.destroy()
      showadult_L8000_50_page()

     pygame.mixer.init()

     def openadult__L8000_40tospeechtest_312():
      global F1
      F1 = 4
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_40_adultwindow.destroy()
      showadult_speechtest_312_page()

     L8000_40_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L8000_40_label = tk.Label(L8000_40_adultwindow, image=L8000_40_img)
     L8000_40_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_40_YES_button = tk.Button(L8000_40_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L8000_40tospeechtest_312)
     L8000_40_NO_button  = tk.Button(L8000_40_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L8000_40toL8000_50)

     L8000_40_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_40_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_40_adultwindow.mainloop()

  # L8000_50 page
  def showadult_L8000_50_page():
     L8000_50_adultwindow = tk.Toplevel()
     L8000_50_adultwindow.geometry("800x480")
     L8000_50_adultwindow.resizable(False, False)
     L8000_50_adultwindow.title("L8000_50")

     pygame.mixer.init()

     def playadult_L8000_50toL8000_60():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_60_L.mp3")
      pygame.mixer.music.play()
      L8000_50_adultwindow.destroy()
      showadult_L8000_60_page()

     pygame.mixer.init()

     def openadult__L8000_50tospeechtest_312():
      global F1
      F1 = 5
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_50_adultwindow.destroy()
      showadult_speechtest_312_page()

     L8000_50_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L8000_50_label = tk.Label(L8000_50_adultwindow, image=L8000_50_img)
     L8000_50_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_50_YES_button = tk.Button(L8000_50_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L8000_50tospeechtest_312)
     L8000_50_NO_button  = tk.Button(L8000_50_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L8000_50toL8000_60)

     L8000_50_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_50_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_50_adultwindow.mainloop()

  # L8000_60 page
  def showadult_L8000_60_page():
     L8000_60_adultwindow = tk.Toplevel()
     L8000_60_adultwindow.geometry("800x480")
     L8000_60_adultwindow.resizable(False, False)
     L8000_60_adultwindow.title("L8000_60")

     pygame.mixer.init()

     def playadult_L8000_60toL8000_70():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_70_L.mp3")
      pygame.mixer.music.play()
      L8000_60_adultwindow.destroy()
      showadult_L8000_70_page()

     pygame.mixer.init()

     def openadult__L8000_60tospeechtest_312():
      global F1
      F1 = 6
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_60_adultwindow.destroy()
      showadult_speechtest_312_page()

     L8000_60_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L8000_60_label = tk.Label(L8000_60_adultwindow, image=L8000_60_img)
     L8000_60_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_60_YES_button = tk.Button(L8000_60_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L8000_60tospeechtest_312)
     L8000_60_NO_button  = tk.Button(L8000_60_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L8000_60toL8000_70)

     L8000_60_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_60_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_60_adultwindow.mainloop()

  # L8000_70 page
  def showadult_L8000_70_page():
     L8000_70_adultwindow = tk.Toplevel()
     L8000_70_adultwindow.geometry("800x480")
     L8000_70_adultwindow.resizable(False, False)
     L8000_70_adultwindow.title("L8000_70")

     pygame.mixer.init()

     def playadult_L8000_70toL8000_80():
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\pure tone\left\8000_80_L.mp3")
      pygame.mixer.music.play()
      L8000_70_adultwindow.destroy()
      showadult_L8000_80_page()

     pygame.mixer.init()

     def openadult__L8000_70tospeechtest_312():
      global F1
      F1 = 7
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_70_adultwindow.destroy()
      showadult_speechtest_312_page()

     L8000_70_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L8000_70_label = tk.Label(L8000_70_adultwindow, image=L8000_70_img)
     L8000_70_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_70_YES_button = tk.Button(L8000_70_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L8000_70tospeechtest_312)
     L8000_70_NO_button  = tk.Button(L8000_70_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L8000_70toL8000_80)

     L8000_70_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_70_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_70_adultwindow.mainloop()

  # L8000_80 page
  def showadult_L8000_80_page():
     L8000_80_adultwindow = tk.Toplevel()
     L8000_80_adultwindow.geometry("800x480")
     L8000_80_adultwindow.resizable(False, False)
     L8000_80_adultwindow.title("L8000_80")

     pygame.mixer.init()

     def playadult_L8000_80tospeechtest_312():
      global F1
      F1 = 9
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_80_adultwindow.destroy()
      showadult_speechtest_312_page()

     pygame.mixer.init()

     def openadult__L8000_80tospeechtest_312():
      global F1
      F1 = 8
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\312.mp3")
      pygame.mixer.music.play()
      L8000_80_adultwindow.destroy()
      showadult_speechtest_312_page()

     L8000_80_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\3rigthadults.png")
     L8000_80_label = tk.Label(L8000_80_adultwindow, image=L8000_80_img)
     L8000_80_label.place(x=0, y=0, relwidth=1, relheight=1)

     L8000_80_YES_button = tk.Button(L8000_80_adultwindow, text="YES", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openadult__L8000_80tospeechtest_312)
     L8000_80_NO_button  = tk.Button(L8000_80_adultwindow, text="NO", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=playadult_L8000_80tospeechtest_312)

     L8000_80_NO_button.place(x=463,  y=391, relwidth=0.156, relheight=0.072)
     L8000_80_YES_button.place(x=202, y=392, relwidth=0.156, relheight=0.072)

     L8000_80_adultwindow.mainloop()

  # speechtest_312 page
  def showadult_speechtest_312_page():
     speechtest_312_adultwindow = tk.Toplevel()
     speechtest_312_adultwindow.geometry("800x480")
     speechtest_312_adultwindow.resizable(False, False)
     speechtest_312_adultwindow.title("speechtest_312")

     speechtest_312_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_312_label = tk.Label(speechtest_312_adultwindow, image=speechtest_312_img)
     speechtest_312_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     G=None

     def openture__speechtest_312tospeechtest_396():
      global G
      G = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\396.mp3")
      pygame.mixer.music.play()
      speechtest_312_adultwindow.destroy()
      showadult_speechtest_396_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_312tospeechtest_396():
      global G
      G = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\396.mp3")
      pygame.mixer.music.play()
      speechtest_312_adultwindow.destroy()
      showadult_speechtest_396_page()

     speechtest_312_true_button = tk.Button(speechtest_312_adultwindow, text="3 1 2", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_312tospeechtest_396)
     speechtest_311_false_button  = tk.Button(speechtest_312_adultwindow, text="3 1 1", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_312tospeechtest_396)
     speechtest_212_false_button  = tk.Button(speechtest_312_adultwindow, text="2 1 2", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_312tospeechtest_396)
     speechtest_313_false_button  = tk.Button(speechtest_312_adultwindow, text="3 1 3", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_312tospeechtest_396)

     speechtest_313_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_212_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_311_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_312_true_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)

     speechtest_312_adultwindow.mainloop()

  # speechtest_396 page
  def showadult_speechtest_396_page():
     speechtest_396_adultwindow = tk.Toplevel()
     speechtest_396_adultwindow.geometry("800x480")
     speechtest_396_adultwindow.resizable(False, False)
     speechtest_396_adultwindow.title("speechtest_396")

     speechtest_396_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_396_label = tk.Label(speechtest_396_adultwindow, image=speechtest_396_img)
     speechtest_396_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     H=None

     def openture__speechtest_396tospeechtest_839():
      global H
      H = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\839.mp3")
      pygame.mixer.music.play()
      speechtest_396_adultwindow.destroy()
      showadult_speechtest_839_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_396tospeechtest_839():
      global H
      H = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\839.mp3")
      pygame.mixer.music.play()
      speechtest_396_adultwindow.destroy()
      showadult_speechtest_839_page()

     speechtest_396_true_button = tk.Button(speechtest_396_adultwindow, text="3 9 6", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_396tospeechtest_839)
     speechtest_469_false_button  = tk.Button(speechtest_396_adultwindow, text="4 6 9", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_396tospeechtest_839)
     speechtest_858_false_button  = tk.Button(speechtest_396_adultwindow, text="8 5 8", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_396tospeechtest_839)
     speechtest_389_false_button  = tk.Button(speechtest_396_adultwindow, text="3 8 9", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_396tospeechtest_839)

     speechtest_389_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_858_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_469_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_396_true_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)

     speechtest_396_adultwindow.mainloop()

  # speechtest_839 page
  def showadult_speechtest_839_page():
     speechtest_839_adultwindow = tk.Toplevel()
     speechtest_839_adultwindow.geometry("800x480")
     speechtest_839_adultwindow.resizable(False, False)
     speechtest_839_adultwindow.title("speechtest_839")

     speechtest_839_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_839_label = tk.Label(speechtest_839_adultwindow, image=speechtest_839_img)
     speechtest_839_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     I=None

     def openture__speechtest_839tospeechtest_958():
      global I
      I = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\958.mp3")
      pygame.mixer.music.play()
      speechtest_839_adultwindow.destroy()
      showadult_speechtest_958_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_839tospeechtest_958():
      global I
      I = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\958.mp3")
      pygame.mixer.music.play()
      speechtest_839_adultwindow.destroy()
      showadult_speechtest_958_page()

     speechtest_839_true_button = tk.Button(speechtest_839_adultwindow, text="8 3 9", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_839tospeechtest_958)
     speechtest_938_false_button  = tk.Button(speechtest_839_adultwindow, text="9 3 8", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_839tospeechtest_958)
     speechtest_856_false_button  = tk.Button(speechtest_839_adultwindow, text="8 5 6", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_839tospeechtest_958)
     speechtest_786_false_button  = tk.Button(speechtest_839_adultwindow, text="7 8 6", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_839tospeechtest_958)

     speechtest_938_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_856_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_786_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_839_true_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_839_adultwindow.mainloop()

  # speechtest_958 page
  def showadult_speechtest_958_page():
     speechtest_958_adultwindow = tk.Toplevel()
     speechtest_958_adultwindow.geometry("800x480")
     speechtest_958_adultwindow.resizable(False, False)
     speechtest_958_adultwindow.title("speechtest_958")

     speechtest_958_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_958_label = tk.Label(speechtest_958_adultwindow, image=speechtest_958_img)
     speechtest_958_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     J=None

     def openture__speechtest_958tospeechtest_262():
      global J
      J = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\462.mp3")
      pygame.mixer.music.play()
      speechtest_958_adultwindow.destroy()
      showadult_speechtest_262_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_958tospeechtest_262():
      global J
      J = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\462.mp3")
      pygame.mixer.music.play()
      speechtest_958_adultwindow.destroy()
      showadult_speechtest_262_page()

     speechtest_958_true_button = tk.Button(speechtest_958_adultwindow, text="9 5 8", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_958tospeechtest_262)
     speechtest_987_false_button  = tk.Button(speechtest_958_adultwindow, text="9 8 7", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_958tospeechtest_262)
     speechtest_865_false_button  = tk.Button(speechtest_958_adultwindow, text="8 6 5", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_958tospeechtest_262)
     speechtest_858_false_button  = tk.Button(speechtest_958_adultwindow, text="8 5 8", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_958tospeechtest_262)

     speechtest_987_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_865_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_858_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_958_true_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_958_adultwindow.mainloop()

  # speechtest_262 page
  def showadult_speechtest_262_page():
     speechtest_262_adultwindow = tk.Toplevel()
     speechtest_262_adultwindow.geometry("800x480")
     speechtest_262_adultwindow.resizable(False, False)
     speechtest_262_adultwindow.title("speechtest_262")

     speechtest_262_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_262_label = tk.Label(speechtest_262_adultwindow, image=speechtest_262_img)
     speechtest_262_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     K=None

     def openture__speechtest_262tospeechtest_862():
      global K
      K = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\862.mp3")
      pygame.mixer.music.play()
      speechtest_262_adultwindow.destroy()
      showadult_speechtest_862_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_262tospeechtest_862():
      global K
      K = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\862.mp3")
      pygame.mixer.music.play()
      speechtest_262_adultwindow.destroy()
      showadult_speechtest_862_page()

     speechtest_262_true_button = tk.Button(speechtest_262_adultwindow, text="4 6 2", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_262tospeechtest_862)
     speechtest_363_false_button  = tk.Button(speechtest_262_adultwindow, text="3 6 3", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_262tospeechtest_862)
     speechtest_362_false_button  = tk.Button(speechtest_262_adultwindow, text="3 6 2", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_262tospeechtest_862)
     speechtest_286_false_button  = tk.Button(speechtest_262_adultwindow, text="2 8 6", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_262tospeechtest_862)

     speechtest_363_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_362_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_286_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_262_true_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_262_adultwindow.mainloop()
     
  # speechtest_862 page
  def showadult_speechtest_862_page():
     speechtest_862_adultwindow = tk.Toplevel()
     speechtest_862_adultwindow.geometry("800x480")
     speechtest_862_adultwindow.resizable(False, False)
     speechtest_862_adultwindow.title("speechtest_862")

     speechtest_862_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_862_label = tk.Label(speechtest_862_adultwindow, image=speechtest_862_img)
     speechtest_862_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     L=None

     def openture__speechtest_862tospeechtest_218():
      global L
      L = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\218.mp3")
      pygame.mixer.music.play()
      speechtest_862_adultwindow.destroy()
      showadult_speechtest_218_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_862tospeechtest_218():
      global L
      L = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\218.mp3")
      pygame.mixer.music.play()
      speechtest_862_adultwindow.destroy()
      showadult_speechtest_218_page()

     speechtest_862_true_button = tk.Button(speechtest_862_adultwindow, text="8 6 2", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_862tospeechtest_218)
     speechtest_756_false_button  = tk.Button(speechtest_862_adultwindow, text="7 5 6", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_862tospeechtest_218)
     speechtest_686_false_button  = tk.Button(speechtest_862_adultwindow, text="6 8 6", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_862tospeechtest_218)
     speechtest_915_false_button  = tk.Button(speechtest_862_adultwindow, text="9 1 5", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_862tospeechtest_218)

     speechtest_756_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_686_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_915_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_862_true_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_862_adultwindow.mainloop()

  # speechtest_218 page
  def showadult_speechtest_218_page():
     speechtest_218_adultwindow = tk.Toplevel()
     speechtest_218_adultwindow.geometry("800x480")
     speechtest_218_adultwindow.resizable(False, False)
     speechtest_218_adultwindow.title("speechtest_218")

     speechtest_218_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_218_label = tk.Label(speechtest_218_adultwindow, image=speechtest_218_img)
     speechtest_218_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     M=None

     def openture__speechtest_218tospeechtest_920():
      global M
      M = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\920.mp3")
      pygame.mixer.music.play()
      speechtest_218_adultwindow.destroy()
      showadult_speechtest_920_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_218tospeechtest_920():
      global M
      M = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\920.mp3")
      pygame.mixer.music.play()
      speechtest_218_adultwindow.destroy()
      showadult_speechtest_920_page()

     speechtest_208_true_button = tk.Button(speechtest_218_adultwindow, text="2 0 8", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_218tospeechtest_920)
     speechtest_124_false_button  = tk.Button(speechtest_218_adultwindow, text="1 0 4", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_218tospeechtest_920)
     speechtest_329_false_button  = tk.Button(speechtest_218_adultwindow, text="3 0 9", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_218tospeechtest_920)
     speechtest_168_false_button  = tk.Button(speechtest_218_adultwindow, text="1 0 8", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_218tospeechtest_920)

     speechtest_124_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_329_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_168_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_208_true_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_218_adultwindow.mainloop()

  # speechtest_920 page
  def showadult_speechtest_920_page():
     speechtest_920_adultwindow = tk.Toplevel()
     speechtest_920_adultwindow.geometry("800x480")
     speechtest_920_adultwindow.resizable(False, False)
     speechtest_920_adultwindow.title("speechtest_920")

     speechtest_920_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_920_label = tk.Label(speechtest_920_adultwindow, image=speechtest_920_img)
     speechtest_920_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     N=None

     def openture__speechtest_920tospeechtest_025():
      global N
      N = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\025.mp3")
      pygame.mixer.music.play()
      speechtest_920_adultwindow.destroy()
      showadult_speechtest_025_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_920tospeechtest_025():
      global N
      N = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\025.mp3")
      pygame.mixer.music.play()
      speechtest_920_adultwindow.destroy()
      showadult_speechtest_025_page()

     speechtest_920_true_button = tk.Button(speechtest_920_adultwindow, text="9 2 0", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_920tospeechtest_025)
     speechtest_820_false_button  = tk.Button(speechtest_920_adultwindow, text="8 2 0", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_920tospeechtest_025)
     speechtest_760_false_button  = tk.Button(speechtest_920_adultwindow, text="7 6 0", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_920tospeechtest_025)
     speechtest_680_false_button  = tk.Button(speechtest_920_adultwindow, text="6 8 0", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_920tospeechtest_025)

     speechtest_820_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_760_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_680_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_920_true_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_920_adultwindow.mainloop()

  # speechtest_025 page
  def showadult_speechtest_025_page():
     speechtest_025_adultwindow = tk.Toplevel()
     speechtest_025_adultwindow.geometry("800x480")
     speechtest_025_adultwindow.resizable(False, False)
     speechtest_025_adultwindow.title("speechtest_025")

     speechtest_025_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_025_label = tk.Label(speechtest_025_adultwindow, image=speechtest_025_img)
     speechtest_025_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     O=None

     def openture__speechtest_025tospeechtest_593():
      global O
      O = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\593.mp3")
      pygame.mixer.music.play()
      speechtest_025_adultwindow.destroy()
      showadult_speechtest_593_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_025tospeechtest_593():
      global O
      O = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\593.mp3")
      pygame.mixer.music.play()
      speechtest_025_adultwindow.destroy()
      showadult_speechtest_593_page()

     speechtest_025_true_button = tk.Button(speechtest_025_adultwindow, text="0 2 5", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_025tospeechtest_593)
     speechtest_046_false_button  = tk.Button(speechtest_025_adultwindow, text="0 4 6", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_025tospeechtest_593)
     speechtest_065_false_button  = tk.Button(speechtest_025_adultwindow, text="0 6 5", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_025tospeechtest_593)
     speechtest_097_false_button  = tk.Button(speechtest_025_adultwindow, text="0 9 7", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_025tospeechtest_593)

     speechtest_097_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_046_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_065_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_025_true_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_025_adultwindow.mainloop()

  # speechtest_593 page
  def showadult_speechtest_593_page():
     speechtest_593_adultwindow = tk.Toplevel()
     speechtest_593_adultwindow.geometry("800x480")
     speechtest_593_adultwindow.resizable(False, False)
     speechtest_593_adultwindow.title("speechtest_593")

     speechtest_593_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_593_label = tk.Label(speechtest_593_adultwindow, image=speechtest_593_img)
     speechtest_593_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     P=None

     def openture__speechtest_593tospeechtest_106():
      global P
      P = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\106.mp3")
      pygame.mixer.music.play()
      speechtest_593_adultwindow.destroy()
      showadult_speechtest_106_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_593tospeechtest_106():
      global P
      P = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\106.mp3")
      pygame.mixer.music.play()
      speechtest_593_adultwindow.destroy()
      showadult_speechtest_106_page()

     speechtest_593_true_button = tk.Button(speechtest_593_adultwindow, text="5 9 3", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_593tospeechtest_106)
     speechtest_465_false_button  = tk.Button(speechtest_593_adultwindow, text="4 6 5", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_593tospeechtest_106)
     speechtest_972_false_button  = tk.Button(speechtest_593_adultwindow, text="9 7 2", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_593tospeechtest_106)
     speechtest_831_false_button  = tk.Button(speechtest_593_adultwindow, text="8 3 1", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_593tospeechtest_106)

     speechtest_465_false_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_972_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_831_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_593_true_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     
     speechtest_593_adultwindow.mainloop()

  # speechtest_106 page
  def showadult_speechtest_106_page():
     speechtest_106_adultwindow = tk.Toplevel()
     speechtest_106_adultwindow.geometry("800x480")
     speechtest_106_adultwindow.resizable(False, False)
     speechtest_106_adultwindow.title("speechtest_106")

     speechtest_106_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_106_label = tk.Label(speechtest_106_adultwindow, image=speechtest_106_img)
     speechtest_106_label.place(x=0, y=0, relwidth=1, relheight=1)

     pygame.mixer.init()
     Q=None

     def openture__speechtest_106tospeechtest_491():
      global Q
      Q = 1
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\045.mp3")
      pygame.mixer.music.play()
      speechtest_106_adultwindow.destroy()
      showadult_speechtest_491_page()

      pygame.mixer.init()
     
     def openfalse__speechtest_106tospeechtest_491():
      global Q
      Q = 0
      pygame.mixer.music.load(r"C:\Users\prasa\OneDrive\Documents\kids audiometer\audio files\speechtest\045.mp3")
      pygame.mixer.music.play()
      speechtest_106_adultwindow.destroy()
      showadult_speechtest_491_page()

     speechtest_106_true_button = tk.Button(speechtest_106_adultwindow, text="1 0 6", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openture__speechtest_106tospeechtest_491)
     speechtest_208_false_button  = tk.Button(speechtest_106_adultwindow, text="2 0 8", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_106tospeechtest_491)
     speechtest_308_false_button  = tk.Button(speechtest_106_adultwindow, text="3 0 8", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_106tospeechtest_491)
     speechtest_402_false_button  = tk.Button(speechtest_106_adultwindow, text="4 0 2", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0, command=openfalse__speechtest_106tospeechtest_491)

     speechtest_208_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_308_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_402_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_106_true_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_106_adultwindow.mainloop()

  # speechtest_491 page
  def showadult_speechtest_491_page():
     speechtest_491_adultwindow = tk.Toplevel()
     speechtest_491_adultwindow.geometry("800x480")
     speechtest_491_adultwindow.resizable(False, False)
     speechtest_491_adultwindow.title("speechtest_491")

     def calculate_and_displaygeneralresultsleft():
       total = A1 + B1 + C1  + D1 + E1 + F1
       if -1 < total <= 12:
         displayadult_pageleft(1)
       elif 12 < total <= 24:
         displayadult_pageleft(2)
       elif 24 < total <= 42:
         displayadult_pageleft(3)
       elif 42 < total <=54:
         displayadult_pageleft(4)
       else:
         print("total out of range") 

     def displayadult_pageleft(page_number):
        if page_number == 1:
          normal_general_adultwindowLEFT = tk.Toplevel()
          normal_general_adultwindowLEFT.geometry("800x480")
          normal_general_adultwindowLEFT.resizable(False, False)
          normal_general_adultwindowLEFT.title("normal_general")

          def opennormal_resultsleft():
            normal_general_adultwindowLEFT.destroy()
            showadult_results_page()

          normal_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\LEFTNORMAL.png")
          normal_general_label = tk.Label(normal_general_adultwindowLEFT, image=normal_general_img)
          normal_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_normal_button = tk.Button(normal_general_adultwindowLEFT, text="GET DETAILED RESULTS", font=("Comic Sans MS Bold", 18), bg="#008000", fg="white",activebackground="#008000",activeforeground="white",highlightthickness=0,bd=0,command=opennormal_resultsleft)
          getdetailedresults_normal_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          normal_general_adultwindowLEFT.mainloop()
          print("Displaying normal results")

        elif page_number == 2:
          mild_general_adultwindowLEFT = tk.Toplevel()
          mild_general_adultwindowLEFT.geometry("800x480")
          mild_general_adultwindowLEFT.resizable(False, False)
          mild_general_adultwindowLEFT.title("mild_general")

          def openmild_resultsleft():
            mild_general_adultwindowLEFT.destroy()
            showadult_results_page()

          mild_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\LEFTMILD.png")
          mild_general_label = tk.Label(mild_general_adultwindowLEFT, image=mild_general_img)
          mild_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_mild_button = tk.Button(mild_general_adultwindowLEFT, text="GET DETAILED RESULTS", font=("Comic Sans MS Bold", 18), bg="#6AC66B", fg="white",activebackground="#6AC66B",activeforeground="white",highlightthickness=0,bd=0,command=openmild_resultsleft)
          getdetailedresults_mild_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          mild_general_adultwindowLEFT.mainloop()
          print("Displaying mild results")
        
        elif page_number == 3:
          moderate_general_adultwindowLEFT = tk.Toplevel()
          moderate_general_adultwindowLEFT.geometry("800x480")
          moderate_general_adultwindowLEFT.resizable(False, False)
          moderate_general_adultwindowLEFT.title("moderate_general")

          def openmoderate_resultsleft():
            moderate_general_adultwindowLEFT.destroy()
            showadult_results_page()

          moderate_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\LEFTMODERATE.png")
          moderate_general_label = tk.Label(moderate_general_adultwindowLEFT, image=moderate_general_img)
          moderate_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_moderate_button = tk.Button(moderate_general_adultwindowLEFT, text="GET DETAILED RESULTS", font=("Comic Sans MS Bold", 18), bg="#FFCC4D", fg="white",activebackground="#FFCC4D",activeforeground="white",highlightthickness=0,bd=0,command=openmoderate_resultsleft)
          getdetailedresults_moderate_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          moderate_general_adultwindowLEFT.mainloop()
          print("Displaying moderate results")
         
        
        elif page_number == 4:
          severe_general_adultwindowLEFT = tk.Toplevel()
          severe_general_adultwindowLEFT.geometry("800x480")
          severe_general_adultwindowLEFT.resizable(False, False)
          severe_general_adultwindowLEFT.title("severe_general")

          def opensevere_resultsleft():
            severe_general_adultwindowLEFT.destroy()
            showadult_results_page()
          
          severe_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\LEFTSERVER.png")
          severe_general_label = tk.Label(severe_general_adultwindowLEFT, image=severe_general_img)
          severe_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_severe_button = tk.Button(severe_general_adultwindowLEFT, text="GET DETAILED RESULTS", font=("Comic Sans MS Bold", 18), bg="#BC1823", fg="white",activebackground="#BC1823",activeforeground="white",highlightthickness=0,bd=0,command=opensevere_resultsleft)
          getdetailedresults_severe_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          severe_general_adultwindowLEFT.mainloop()
          print("Displaying severe results")

     def displayadult_page(page_number):
        if page_number == 1:
          speechtest_491_adultwindow.destroy()
          normal_general_adultwindow = tk.Toplevel()
          normal_general_adultwindow.geometry("800x480")
          normal_general_adultwindow.resizable(False, False)
          normal_general_adultwindow.title("normal_general")

          def opennormal_results():
            normal_general_adultwindow.destroy()
            calculate_and_displaygeneralresultsleft()

          normal_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\RIGHTNORMAL.png")
          normal_general_label = tk.Label(normal_general_adultwindow, image=normal_general_img)
          normal_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_normal_button = tk.Button(normal_general_adultwindow, text="GET LEFT EAR RESULTS", font=("Comic Sans MS Bold", 18), bg="#008000", fg="white",activebackground="#008000",activeforeground="white",highlightthickness=0,bd=0,command=opennormal_results)
          getdetailedresults_normal_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          normal_general_adultwindow.mainloop()
          print("Displaying normal results")

        elif page_number == 2:
          speechtest_491_adultwindow.destroy()
          mild_general_adultwindow = tk.Toplevel()
          mild_general_adultwindow.geometry("800x480")
          mild_general_adultwindow.resizable(False, False)
          mild_general_adultwindow.title("mild_general")

          def openmild_results():
            mild_general_adultwindow.destroy()
            calculate_and_displaygeneralresultsleft()

          mild_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\RIGHTMILD.png")
          mild_general_label = tk.Label(mild_general_adultwindow, image=mild_general_img)
          mild_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_mild_button = tk.Button(mild_general_adultwindow, text="GET LEFT EAR RESULTS", font=("Comic Sans MS Bold", 18), bg="#6AC66B", fg="white",activebackground="#6AC66B",activeforeground="white",highlightthickness=0,bd=0,command=openmild_results)
          getdetailedresults_mild_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          mild_general_adultwindow.mainloop()
          print("Displaying mild results")
        
        elif page_number == 3:
          speechtest_491_adultwindow.destroy()
          moderate_general_adultwindow = tk.Toplevel()
          moderate_general_adultwindow.geometry("800x480")
          moderate_general_adultwindow.resizable(False, False)
          moderate_general_adultwindow.title("moderate_general")

          def openmoderate_results():
            moderate_general_adultwindow.destroy()
            calculate_and_displaygeneralresultsleft()

          moderate_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\RIGHTMODERATE.png")
          moderate_general_label = tk.Label(moderate_general_adultwindow, image=moderate_general_img)
          moderate_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_moderate_button = tk.Button(moderate_general_adultwindow, text="GET LEFT EAR RESULTS", font=("Comic Sans MS Bold", 18), bg="#FFCC4D", fg="white",activebackground="#FFCC4D",activeforeground="white",highlightthickness=0,bd=0,command=openmoderate_results)
          getdetailedresults_moderate_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          moderate_general_adultwindow.mainloop()
          print("Displaying moderate results")
         
        
        elif page_number == 4:
          speechtest_491_adultwindow.destroy()
          severe_general_adultwindow = tk.Toplevel()
          severe_general_adultwindow.geometry("800x480")
          severe_general_adultwindow.resizable(False, False)
          severe_general_adultwindow.title("severe_general")

          def opensevere_results():
            severe_general_adultwindow.destroy()
            calculate_and_displaygeneralresultsleft()
          
          severe_general_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\RIGHTSERVER.png")
          severe_general_label = tk.Label(severe_general_adultwindow, image=severe_general_img)
          severe_general_label.place(x=0, y=0, relwidth=1, relheight=1)

          getdetailedresults_severe_button = tk.Button(severe_general_adultwindow, text="GET LEFT EAR RESULTS", font=("Comic Sans MS Bold", 18), bg="#BC1823", fg="white",activebackground="#BC1823",activeforeground="white",highlightthickness=0,bd=0,command=opensevere_results)
          getdetailedresults_severe_button.place(x=242, y=396, relwidth=0.4, relheight=0.08)
      
          severe_general_adultwindow.mainloop()
          print("Displaying severe results") 

     R=None

     def calculate_and_displaygeneralresultsTRUE():
       global R
       R=1
       global total
       total = A + B + C  + D + E + F
       if -1 < total <= 12:
         displayadult_page(1)
       elif 12 < total <= 24:
         displayadult_page(2)
       elif 24 < total <= 42:
         displayadult_page(3)
       elif 42 < total <=54:
         displayadult_page(4)
       else:
         print("total out of range") 

     def calculate_and_displaygeneralresultsFALSE():
       global R
       R=0
       global total
       total = A + B + C + D + E + F
       if -1 < total <= 12:
         displayadult_page(1)
       elif 12 < total <= 24:
         displayadult_page(2)
       elif 24 < total <= 42:
         displayadult_page(3)
       elif 42 < total <=54:
         displayadult_page(4)
       else:
         print("total out of range") 
      
     speechtest_491_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\4speechadults.png")
     speechtest_491_label = tk.Label(speechtest_491_adultwindow, image=speechtest_491_img)
     speechtest_491_label.place(x=0, y=0, relwidth=1, relheight=1)


     speechtest_491_true_button = tk.Button(speechtest_491_adultwindow, text="0 4 5", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0,command=calculate_and_displaygeneralresultsTRUE)
     speechtest_246_false_button  = tk.Button(speechtest_491_adultwindow, text="2 4 6", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0,command=calculate_and_displaygeneralresultsFALSE)
     speechtest_297_false_button  = tk.Button(speechtest_491_adultwindow, text="0 9 7", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0,command=calculate_and_displaygeneralresultsFALSE)
     speechtest_389_false_button  = tk.Button(speechtest_491_adultwindow, text="3 8 9", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0,command=calculate_and_displaygeneralresultsFALSE)

     speechtest_246_false_button.place(x=603, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_297_false_button.place(x=423, y=269, relwidth=0.135, relheight=0.0725)
     speechtest_389_false_button.place(x=423, y=338, relwidth=0.135, relheight=0.0725)
     speechtest_491_true_button.place(x=603, y=269, relwidth=0.135, relheight=0.0725)
     
     speechtest_491_adultwindow.mainloop()
   
   #RESULTS PAGE
  def showadult_results_page():
    results_adultwindow = tk.Toplevel()
    results_adultwindow.geometry("800x480")
    results_adultwindow.resizable(False, False)
    results_adultwindow.title("results")

    def openadult_homeadultsadultsfromresults():
      results_adultwindow.destroy()
      homeadults2()

    def openlearnmore():
      results_adultwindow.destroy()
      showadult_learnmore_page()
     
    speechsum = G + H + I + J + K + L + M + N + O + P + Q + R
    speechavg = (speechsum / 12)*100
    print("speechsum is ",speechsum)
    print("speechavg is ",speechavg)

    results_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\resultsadults.png")
    results_label = tk.Label( results_adultwindow, image= results_img)
    results_label.place(x=0, y=0, relwidth=1, relheight=1)

    speechsum_label = tk.Label(results_adultwindow, text=f"{speechsum}", font=("Comic Sans MS Bold", 9), fg="#428EC2", bg="white" ,borderwidth=0)
    speechsum_label.place(x=600,y=319,relwidth=0.024,relheight=0.05)

    speechaverage_label = tk.Label(results_adultwindow, text=f"{speechavg:.2f}%", font=("Comic Sans MS Bold", 24), fg="#428EC2", bg="white",borderwidth=0)
    speechaverage_label.place(x=555,y=265,relwidth=0.22,relheight=0.1)

    global total1
    total1 = A + B + C + D + E + F 
    if -1 < total1 <= 12:
       total1_label = tk.Label(results_adultwindow, text="NO HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#008000", bg="white" ,borderwidth=0)
       total1_label.place(x=555,y=125,relwidth=0.22,relheight=0.028)
    elif 12 < total1 <= 24:
       total1_label = tk.Label(results_adultwindow, text="MILD HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#6AC66B", bg="white" ,borderwidth=0)
       total1_label.place(x=555,y=125,relwidth=0.22,relheight=0.028)
    elif 24 < total1 <= 42:
       total1_label = tk.Label(results_adultwindow, text="MODERATE HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#FFCC4D", bg="white" ,borderwidth=0)
       total1_label.place(x=546,y=125,relwidth=0.25,relheight=0.028)
    elif 42 < total1 <=54:
       total1_label = tk.Label(results_adultwindow, text="SEVERE HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#BC1823", bg="white" ,borderwidth=0)
       total1_label.place(x=555,y=125,relwidth=0.22,relheight=0.028)
    else:
         print("total out of range") 

    global total2
    total2 = A1 + B1 + C1 + D1 + E1 + F1 
    if -1 < total2 <= 12:
       total2_label = tk.Label(results_adultwindow, text="NO HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#008000", bg="white" ,borderwidth=0)
       total2_label.place(x=555,y=179,relwidth=0.22,relheight=0.028)
    elif 12 < total2 <= 24:
       total2_label = tk.Label(results_adultwindow, text="MILD HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#6AC66B", bg="white" ,borderwidth=0)
       total2_label.place(x=555,y=179,relwidth=0.22,relheight=0.028)
    elif 24 < total2 <= 42:
       total2_label2 = tk.Label(results_adultwindow, text="MODERATE HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#FFCC4D", bg="white" ,borderwidth=0)
       total2_label2.place(x=546,y=179,relwidth=0.25,relheight=0.028)
    elif 42 < total2 <=54:
       total2_label = tk.Label(results_adultwindow, text="SEVERE HEARING LOSS", font=("Comic Sans MS Bold", 10), fg="#BC1823", bg="white" ,borderwidth=0)
       total2_label.place(x=555,y=179,relwidth=0.22,relheight=0.028)
    else:
         print("total out of range") 

    folder_name = r"C:\Users\prasa\OneDrive\Documents\audiogram_pdfs"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
   
    file_name = f"{name}_audiogram.pdf"
    pdf_path = os.path.join(folder_name, file_name)
    canvas = Canvas(pdf_path)
    c = Canvas(pdf_path, pagesize=letter)
   
    c.drawString(100, 750, f"Name: {name}")
    c.drawString(100, 730, f"Age: {age}")
    c.drawString(100, 710, f"Gender: {gender}")
    c.drawString(260, 685, "AUDIOGRAM")

    x_values = [250, 500, 1000, 2000, 4000, 8000]
    y_values = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    right=[A*10,B*10,C*10,D*10,E*10,F*10]
    left=[A1*10,B1*10,C1*10,D1*10,E1*10,F1*10]

    plt.clf()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Hearing Threshold (dB)')

    plt.plot(x_values, [20]*len(x_values), color='#008000')
    plt.plot(x_values, [40]*len(x_values), color='#6AC66B')
    plt.plot(x_values, [70]*len(x_values), color='#FFCC4D')
    plt.plot(x_values, [80]*len(x_values), color='#BC1823')
    plt.plot(x_values, right, marker='o',label='Right Ear', linestyle='-', color='#428EC2')
    plt.plot(x_values, left, marker='o',label='Left Ear', linestyle='-', color='#99D1F7')
    
    plt.xscale('log')
    plt.xticks([250, 500, 1000, 2000, 4000, 8000], [250, 500, 1000, 2000, 4000, 8000])
    plt.yticks(y_values)
    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
    plt.legend()

    plot_path = "temp_graph.png"
    plt.savefig(plot_path)

    c.drawImage(plot_path, 100, 380, width=400, height=300)

    data = [["", "0dB", "10dB", "20dB", "30dB", "40dB", "50dB", "60dB", "70dB", "80dB"],
        ["250Hz", "", "", "", "", "", "", "", "", ""],
        ["500Hz", "", "", "", "", "", "", "", "", ""],
        ["1000Hz", "", "", "", "", "", "", "", "", ""],
        ["2000Hz", "", "", "", "", "", "", "", "", ""], 
        ["4000Hz", "", "", "", "", "", "", "", "", ""],
        ["8000Hz", "", "", "", "", "", "", "", "", ""]]
    
    if A == 0:
      data[1][1] = "✓"
      for i in range(2, len(data[1])):
        data[1][i] = "-"
    elif A == 1:   
      data[1][2] = "✓"
      for i in range(3, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 2):
        data[1][i] = "x"
    elif A == 2:  
     data[1][3] = "✓"
     for i in range(4, len(data[1])):
        data[1][i] = "-"
     for i in range(1, 3):
        data[1][i] = "x"
    elif A == 3:
     data[1][4] = "✓"
     for i in range(5, len(data[1])):
        data[1][i] = "-"
     for i in range(1, 4):
        data[1][i] = "x"  
    elif A == 4:
      data[1][5] = "✓"
      for i in range(6, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 5):
        data[1][i] = "x"
    elif A == 5:
      data[1][6] = "✓"
      for i in range(7, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 6):
        data[1][i] = "x"  
    elif A == 6:
      data[1][7] = "✓"
      for i in range(8, len(data[1])):
        data[1][i] = "-"   
      for i in range(1, 7):
        data[1][i] = "x"
    elif A == 7:
      data[1][8] = "✓"
      for i in range(9, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 8):
        data[1][i] = "x"
    elif A == 8:
      data[1][9] = "✓"
      for i in range(10, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 9):
        data[1][i] = "x"

    if B == 0:
      data[2][1] = "✓"
      for i in range(2, len(data[2])):
        data[2][i] = "-"
    elif B == 1:   
      data[2][2] = "✓"
      for i in range(3, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 2):
        data[2][i] = "x"
    elif B == 2:  
     data[2][3] = "✓"
     for i in range(4, len(data[2])):
        data[2][i] = "-"
     for i in range(1, 3):
        data[2][i] = "x"
    elif B == 3:
     data[2][4] = "✓"
     for i in range(5, len(data[2])):
        data[2][i] = "-"
     for i in range(1, 4):
        data[2][i] = "x"  
    elif B == 4:
      data[2][5] = "✓"
      for i in range(6, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 5):
        data[2][i] = "x"
    elif B == 5:
      data[2][6] = "✓"
      for i in range(7, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 6):
        data[2][i] = "x"  
    elif B == 6:
      data[2][7] = "✓"
      for i in range(8, len(data[2])):
        data[2][i] = "-"   
      for i in range(1, 7):
        data[2][i] = "x"
    elif B == 7:
      data[2][8] = "✓"
      for i in range(9, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 8):
        data[2][i] = "x"
    elif B == 8:
      data[2][9] = "✓"
      for i in range(10, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 9):
        data[2][i] = "x"

    if C == 0:
      data[3][1] = "✓"
      for i in range(2, len(data[3])):
        data[3][i] = "-"
    elif C == 1:   
      data[3][2] = "✓"
      for i in range(3, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 2):
        data[3][i] = "x"
    elif C == 2:  
     data[3][3] = "✓"
     for i in range(4, len(data[3])):
        data[3][i] = "-"
     for i in range(1, 3):
        data[3][i] = "x"
    elif C == 3:
     data[3][4] = "✓"
     for i in range(5, len(data[3])):
        data[3][i] = "-"
     for i in range(1, 4):
        data[3][i] = "x"  
    elif C == 4:
      data[3][5] = "✓"
      for i in range(6, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 5):
        data[3][i] = "x"
    elif C == 5:
      data[3][6] = "✓"
      for i in range(7, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 6):
        data[3][i] = "x"  
    elif C == 6:
      data[3][7] = "✓"
      for i in range(8, len(data[3])):
        data[3][i] = "-"   
      for i in range(1, 7):
        data[3][i] = "x"
    elif C == 7:
      data[3][8] = "✓"
      for i in range(9, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 8):
        data[3][i] = "x"
    elif C == 8:
      data[3][9] = "✓"
      for i in range(10, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 9):
        data[3][i] = "x"

    if D == 0:
      data[4][1] = "✓"
      for i in range(2, len(data[4])):
        data[4][i] = "-"
    elif D == 1:   
      data[4][2] = "✓"
      for i in range(3, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 2):
        data[4][i] = "x"
    elif D == 2:  
     data[4][3] = "✓"
     for i in range(4, len(data[4])):
        data[4][i] = "-"
     for i in range(1, 3):
        data[4][i] = "x"
    elif D == 3:
     data[4][4] = "✓"
     for i in range(5, len(data[4])):
        data[4][i] = "-"
     for i in range(1, 4):
        data[4][i] = "x"  
    elif D == 4:
      data[4][5] = "✓"
      for i in range(6, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 5):
        data[4][i] = "x"
    elif D == 5:
      data[4][6] = "✓"
      for i in range(7, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 6):
        data[4][i] = "x"  
    elif D == 6:
      data[4][7] = "✓"
      for i in range(8, len(data[4])):
        data[4][i] = "-"   
      for i in range(1, 7):
        data[4][i] = "x"
    elif D == 7:
      data[4][8] = "✓"
      for i in range(9, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 8):
        data[4][i] = "x"
    elif D == 8:
      data[4][9] = "✓"
      for i in range(10, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 9):
        data[4][i] = "x"

    if E == 0:
      data[5][1] = "✓"
      for i in range(2, len(data[5])):
        data[5][i] = "-"
    elif E == 1:   
      data[5][2] = "✓"
      for i in range(3, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 2):
        data[5][i] = "x"
    elif E == 2:  
     data[5][3] = "✓"
     for i in range(4, len(data[5])):
        data[5][i] = "-"
     for i in range(1, 3):
        data[5][i] = "x"
    elif E == 3:
     data[5][4] = "✓"
     for i in range(5, len(data[5])):
        data[5][i] = "-"
     for i in range(1, 4):
        data[5][i] = "x"  
    elif E == 4:
      data[5][5] = "✓"
      for i in range(6, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 5):
        data[5][i] = "x"
    elif E == 5:
      data[5][6] = "✓"
      for i in range(7, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 6):
        data[5][i] = "x"  
    elif E == 6:
      data[5][7] = "✓"
      for i in range(8, len(data[5])):
        data[5][i] = "-"   
      for i in range(1, 7):
        data[5][i] = "x"
    elif E == 7:
      data[5][8] = "✓"
      for i in range(9, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 8):
        data[5][i] = "x"
    elif E == 8:
      data[5][9] = "✓"
      for i in range(10, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 9):
        data[5][i] = "x"

    if F == 0:
      data[6][1] = "✓"
      for i in range(2, len(data[6])):
        data[6][i] = "-"
    elif F == 1:   
      data[6][2] = "✓"
      for i in range(3, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 2):
        data[6][i] = "x"
    elif F == 2:  
     data[6][3] = "✓"
     for i in range(4, len(data[6])):
        data[6][i] = "-"
     for i in range(1, 3):
        data[6][i] = "x"
    elif F == 3:
     data[6][4] = "✓"
     for i in range(5, len(data[6])):
        data[6][i] = "-"
     for i in range(1, 4):
        data[6][i] = "x"  
    elif F == 4:
      data[6][5] = "✓"
      for i in range(6, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 5):
        data[6][i] = "x"
    elif F == 5:
      data[6][6] = "✓"
      for i in range(7, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 6):
        data[6][i] = "x"  
    elif F == 6:
      data[6][7] = "✓"
      for i in range(8, len(data[6])):
        data[6][i] = "-"   
      for i in range(1, 7):
        data[6][i] = "x"
    elif F == 7:
      data[6][8] = "✓"
      for i in range(9, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 8):
        data[6][i] = "x"
    elif F == 8:
      data[6][9] = "✓"
      for i in range(10, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 9):
        data[6][i] = "x"
     
    colWidths = [100, 40, 40, 40, 40, 40, 40, 40, 40, 40]

    c.drawString(100, 350, "RIGHT EAR")
    for col in range(1, len(data[0])):
     c.drawString(100 + sum(colWidths[:col]), 350, str(data[0][col]))

    for row in range(1, len(data)):
     c.drawString(100, 350 - (row+1)*20, str(data[row][0]))
     for col in range(1, len(data[row])):
        c.drawString(100 + sum(colWidths[:col]), 350 - (row+1)*20, str(data[row][col]))

    data = [["", "0dB", "10dB", "20dB", "30dB", "40dB", "50dB", "60dB", "70dB", "80dB"],
        ["250Hz", "", "", "", "", "", "", "", "", ""],
        ["500Hz", "", "", "", "", "", "", "", "", ""],
        ["1000Hz", "", "", "", "", "", "", "", "", ""],
        ["2000Hz", "", "", "", "", "", "", "", "", ""], 
        ["4000Hz", "", "", "", "", "", "", "", "", ""],
        ["8000Hz", "", "", "", "", "", "", "", "", ""]]
    
    if A1 == 0:
      data[1][1] = "✓"
      for i in range(2, len(data[1])):
        data[1][i] = "-"
    elif A1 == 1:   
      data[1][2] = "✓"
      for i in range(3, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 2):
        data[1][i] = "x"
    elif A1 == 2:  
     data[1][3] = "✓"
     for i in range(4, len(data[1])):
        data[1][i] = "-"
     for i in range(1, 3):
        data[1][i] = "x"
    elif A1 == 3:
     data[1][4] = "✓"
     for i in range(5, len(data[1])):
        data[1][i] = "-"
     for i in range(1, 4):
        data[1][i] = "x"  
    elif A1 == 4:
      data[1][5] = "✓"
      for i in range(6, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 5):
        data[1][i] = "x"
    elif A1 == 5:
      data[1][6] = "✓"
      for i in range(7, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 6):
        data[1][i] = "x"  
    elif A1 == 6:
      data[1][7] = "✓"
      for i in range(8, len(data[1])):
        data[1][i] = "-"   
      for i in range(1, 7):
        data[1][i] = "x"
    elif A1 == 7:
      data[1][8] = "✓"
      for i in range(9, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 8):
        data[1][i] = "x"
    elif A1 == 8:
      data[1][9] = "✓"
      for i in range(10, len(data[1])):
        data[1][i] = "-"
      for i in range(1, 9):
        data[1][i] = "x"

    if B1 == 0:
      data[2][1] = "✓"
      for i in range(2, len(data[2])):
        data[2][i] = "-"
    elif B1 == 1:   
      data[2][2] = "✓"
      for i in range(3, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 2):
        data[2][i] = "x"
    elif B1 == 2:  
     data[2][3] = "✓"
     for i in range(4, len(data[2])):
        data[2][i] = "-"
     for i in range(1, 3):
        data[2][i] = "x"
    elif B1 == 3:
     data[2][4] = "✓"
     for i in range(5, len(data[2])):
        data[2][i] = "-"
     for i in range(1, 4):
        data[2][i] = "x"  
    elif B1 == 4:
      data[2][5] = "✓"
      for i in range(6, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 5):
        data[2][i] = "x"
    elif B1 == 5:
      data[2][6] = "✓"
      for i in range(7, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 6):
        data[2][i] = "x"  
    elif B1 == 6:
      data[2][7] = "✓"
      for i in range(8, len(data[2])):
        data[2][i] = "-"   
      for i in range(1, 7):
        data[2][i] = "x"
    elif B1 == 7:
      data[2][8] = "✓"
      for i in range(9, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 8):
        data[2][i] = "x"
    elif B1 == 8:
      data[2][9] = "✓"
      for i in range(10, len(data[2])):
        data[2][i] = "-"
      for i in range(1, 9):
        data[2][i] = "x"

    if C1 == 0:
      data[3][1] = "✓"
      for i in range(2, len(data[3])):
        data[3][i] = "-"
    elif C1 == 1:   
      data[3][2] = "✓"
      for i in range(3, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 2):
        data[3][i] = "x"
    elif C1 == 2:  
     data[3][3] = "✓"
     for i in range(4, len(data[3])):
        data[3][i] = "-"
     for i in range(1, 3):
        data[3][i] = "x"
    elif C1 == 3:
     data[3][4] = "✓"
     for i in range(5, len(data[3])):
        data[3][i] = "-"
     for i in range(1, 4):
        data[3][i] = "x"  
    elif C1 == 4:
      data[3][5] = "✓"
      for i in range(6, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 5):
        data[3][i] = "x"
    elif C1 == 5:
      data[3][6] = "✓"
      for i in range(7, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 6):
        data[3][i] = "x"  
    elif C1 == 6:
      data[3][7] = "✓"
      for i in range(8, len(data[3])):
        data[3][i] = "-"   
      for i in range(1, 7):
        data[3][i] = "x"
    elif C1 == 7:
      data[3][8] = "✓"
      for i in range(9, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 8):
        data[3][i] = "x"
    elif C1 == 8:
      data[3][9] = "✓"
      for i in range(10, len(data[3])):
        data[3][i] = "-"
      for i in range(1, 9):
        data[3][i] = "x"

    if D1 == 0:
      data[4][1] = "✓"
      for i in range(2, len(data[4])):
        data[4][i] = "-"
    elif D1 == 1:   
      data[4][2] = "✓"
      for i in range(3, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 2):
        data[4][i] = "x"
    elif D1 == 2:  
     data[4][3] = "✓"
     for i in range(4, len(data[4])):
        data[4][i] = "-"
     for i in range(1, 3):
        data[4][i] = "x"
    elif D1 == 3:
     data[4][4] = "✓"
     for i in range(5, len(data[4])):
        data[4][i] = "-"
     for i in range(1, 4):
        data[4][i] = "x"  
    elif D1 == 4:
      data[4][5] = "✓"
      for i in range(6, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 5):
        data[4][i] = "x"
    elif D1 == 5:
      data[4][6] = "✓"
      for i in range(7, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 6):
        data[4][i] = "x"  
    elif D1 == 6:
      data[4][7] = "✓"
      for i in range(8, len(data[4])):
        data[4][i] = "-"   
      for i in range(1, 7):
        data[4][i] = "x"
    elif D1 == 7:
      data[4][8] = "✓"
      for i in range(9, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 8):
        data[4][i] = "x"
    elif D1 == 8:
      data[4][9] = "✓"
      for i in range(10, len(data[4])):
        data[4][i] = "-"
      for i in range(1, 9):
        data[4][i] = "x"

    if E1 == 0:
      data[5][1] = "✓"
      for i in range(2, len(data[5])):
        data[5][i] = "-"
    elif E1 == 1:   
      data[5][2] = "✓"
      for i in range(3, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 2):
        data[5][i] = "x"
    elif E1 == 2:  
     data[5][3] = "✓"
     for i in range(4, len(data[5])):
        data[5][i] = "-"
     for i in range(1, 3):
        data[5][i] = "x"
    elif E1 == 3:
     data[5][4] = "✓"
     for i in range(5, len(data[5])):
        data[5][i] = "-"
     for i in range(1, 4):
        data[5][i] = "x"  
    elif E1 == 4:
      data[5][5] = "✓"
      for i in range(6, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 5):
        data[5][i] = "x"
    elif E1 == 5:
      data[5][6] = "✓"
      for i in range(7, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 6):
        data[5][i] = "x"  
    elif E1 == 6:
      data[5][7] = "✓"
      for i in range(8, len(data[5])):
        data[5][i] = "-"   
      for i in range(1, 7):
        data[5][i] = "x"
    elif E1 == 7:
      data[5][8] = "✓"
      for i in range(9, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 8):
        data[5][i] = "x"
    elif E1 == 8:
      data[5][9] = "✓"
      for i in range(10, len(data[5])):
        data[5][i] = "-"
      for i in range(1, 9):
        data[5][i] = "x"

    if F1 == 0:
      data[6][1] = "✓"
      for i in range(2, len(data[6])):
        data[6][i] = "-"
    elif F1 == 1:   
      data[6][2] = "✓"
      for i in range(3, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 2):
        data[6][i] = "x"
    elif F1 == 2:  
     data[6][3] = "✓"
     for i in range(4, len(data[6])):
        data[6][i] = "-"
     for i in range(1, 3):
        data[6][i] = "x"
    elif F1 == 3:
     data[6][4] = "✓"
     for i in range(5, len(data[6])):
        data[6][i] = "-"
     for i in range(1, 4):
        data[6][i] = "x"  
    elif F1 == 4:
      data[6][5] = "✓"
      for i in range(6, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 5):
        data[6][i] = "x"
    elif F1 == 5:
      data[6][6] = "✓"
      for i in range(7, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 6):
        data[6][i] = "x"  
    elif F1 == 6:
      data[6][7] = "✓"
      for i in range(8, len(data[6])):
        data[6][i] = "-"   
      for i in range(1, 7):
        data[6][i] = "x"
    elif F1 == 7:
      data[6][8] = "✓"
      for i in range(9, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 8):
        data[6][i] = "x"
    elif F1 == 8:
      data[6][9] = "✓"
      for i in range(10, len(data[6])):
        data[6][i] = "-"
      for i in range(1, 9):
        data[6][i] = "x"
     
    colWidths = [100, 40, 40, 40, 40, 40, 40, 40, 40, 40]

    c.drawString(100, 160, "LEFT EAR")
    for col in range(1, len(data[0])):
     c.drawString(100 + sum(colWidths[:col]), 160, str(data[0][col]))

    for row in range(1, len(data)):
     c.drawString(100, 160 - (row+1)*20, str(data[row][0]))
     for col in range(1, len(data[row])):
        c.drawString(100 + sum(colWidths[:col]), 160 - (row+1)*20, str(data[row][col]))
   
    c.save()

    os.remove(plot_path)

    def openadult_pdf():
     os.startfile(pdf_path)

    canvas = FigureCanvasTkAgg(plt.gcf(), master=results_adultwindow)
    canvas.draw()
    canvas.get_tk_widget().place(x=95,y=124, relwidth=0.5, relheight=0.5)

    global total3
    total3 = A + B + C + D + E + F 
    if 48 < total3:
       total3_label = tk.Label(results_adultwindow, text="HEARING THRESHOLDS ARE OUT OF THE TESTED RANGE", font=("Comic Sans MS Bold", 9), fg="#BC1823", bg="white" ,borderwidth=0)
       total3_label.place(x=80,y=362,relwidth=0.48,relheight=0.028)
    
    global total4
    total4 = A1 + B1 + C1 + D1 + E1 + F1 
    if 48 < total4:
       total4_label = tk.Label(results_adultwindow, text="HEARING THRESHOLDS ARE OUT OF THE TESTED RANGE", font=("Comic Sans MS Bold", 9), fg="#BC1823", bg="white" ,borderwidth=0)
       total4_label.place(x=80,y=362,relwidth=0.48,relheight=0.028)

    resultsLEARNMORE_button = tk.Button(results_adultwindow, text="LEARN MORE", font=("Comic Sans MS Bold", 16), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0,command=openlearnmore)
    resultsLEARNMORE_button.place(x=98, y=418, relwidth=0.18, relheight=0.07)

    resultstohomeadults_button = tk.Button(results_adultwindow, text="HOME", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0,command=openadult_homeadultsadultsfromresults)
    resultstohomeadults_button.place(x=330, y=417, relwidth=0.16, relheight=0.07)

    print_results_button = tk.Button(results_adultwindow, text="PRINT RESULTS", font=("Comic Sans MS Bold", 14), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0,command=openadult_pdf)
    print_results_button.place(x=531, y=418, relwidth=0.194, relheight=0.07)

    results_adultwindow.mainloop()

  def showadult_learnmore_page():
    learnmore_adultwindow = tk.Toplevel()
    learnmore_adultwindow.geometry("800x480")
    learnmore_adultwindow.resizable(False, False)
    learnmore_adultwindow.title("learn more")

    def openadult_homeadultsfromlearnmore():
      learnmore_adultwindow.destroy()
      homeadults2()

    learnmore_img = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\learnmoreadults.png")
    learnmore_label = tk.Label( learnmore_adultwindow, image= learnmore_img)
    learnmore_label.place(x=0, y=0, relwidth=1, relheight=1)

    learnmoretohomeadults_button = tk.Button(learnmore_adultwindow, text="HOME", font=("Comic Sans MS Bold", 21), bg="#428EC2", fg="white",activebackground="#428EC2",activeforeground="white",highlightthickness=0,bd=0,command=openadult_homeadultsfromlearnmore)
    learnmoretohomeadults_button.place(x=350, y=412, relwidth=0.16, relheight=0.07)

    learnmore_adultwindow.mainloop()

   # homeadults page
  def homeadults2():
   select2language = tk.Toplevel()
   select2language.geometry("800x480") 
   select2language.resizable(False, False)
   select2language.title("select2language")

   select2languagebg_image = tk.PhotoImage(file=r"C:\Users\prasa\OneDrive\Documents\kids audiometer\SELECTLANGUAGE.png")
   select2languagebg_label = tk.Label(select2language, image=select2languagebg_image)
   select2languagebg_label.place(x=0, y=0, relwidth=1, relheight=1)

   def open_english():
    select2language.destroy()
    show_selectmode()

   def open_telugu():
    select2language.destroy()
    show_selectmode()

   def open_hindi():
    select2language.destroy
    show_selectmode()


   select2languagebutton = tk.Button(select2language, text="తెలుగు", font=("Comic Sans MS Bold", 24), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_telugu)
   select2languagebutton.place(x=296, y=178, relwidth=0.28, relheight=0.085)

   select2languagebutton = tk.Button(select2language, text="हिंदी", font=("Comic Sans MS Bold", 24), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_hindi)
   select2languagebutton.place(x=296, y=268, relwidth=0.28, relheight=0.085)

   select2languagebutton = tk.Button(select2language, text="ENGLISH", font=("Comic Sans MS Bold", 24), bg="#F63E7B", fg="white",activebackground="#F63E7B",activeforeground="white",highlightthickness=0,bd=0, command=open_english)
   select2languagebutton.place(x=296, y=358, relwidth=0.28, relheight=0.085)
   select2language.mainloop() 
  homeadults.mainloop() 
 selectmode.mainloop()
selectlanguage.mainloop()