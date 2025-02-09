from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time 
import wavio as wv




root = Tk()
root.geometry("600x700+400+80")
root.resizable(False , False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")


def start_record():
    freq = 44100 
    dur = int(duration.get())
    recording = sound.rec(dur * freq , samplerate = freq , channels = 2 )

    # ----- TIMER -----
    try:
        temp = int(duration.get())
    except:
        print("Enter the right value")

    while temp > 0:
        root.update()
        time.sleep(1)
        temp -= 1

        if temp == 0:
            messagebox.showinfo("Time Countdown")
        
        Label(text=f"{str(temp)}" , font="arial 40" , width=4 , background="#4a4a4a").place(x=240 , y=590)

    sound.wait()
    write("recording.wav" , freq , recording)



# ----- ICON -----

image_icon = PhotoImage(file="Record.png")
root.iconphoto(False , image_icon)

# ----- LOGO -----

photo = PhotoImage(file="Record.png")
logo_image = Label(image=photo , background="#4a4a4a")
logo_image.pack(padx= 5 , pady=5)

# ----- NAME -----

Label(text = "Voice Recorder" , font="arial 30 bold" , background= "#4a4a4a" , fg="white").pack()

# ----- ENTRY BOX -----

duration = StringVar()
entry = Entry(root , textvariable=duration, font="arial 30" , width=15 ).pack(pady=10)
Label(text="Enter time in seconds that you want to record" , font="arial 15" , background="#4a4a4a" , fg="white").pack()

# ----- BUTTON -----

record = Button(root , font="arial 20" , text="Record" , bg="#111111" , fg="white" , border=0 , command = start_record).pack(pady=30)





root.mainloop()
