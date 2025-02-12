from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time 
import wavio as wv
import numpy as np




root = Tk()
root.geometry("600x700+400+80")
root.resizable(False , False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")

recording = None
start_time = None
recording_active = False
audio_data = []

def callback(indata , frames , time , status):

    if status:
        print(status)
    if recording_active:
        audio_data.append(indata.copy())



def update_timer():

    if recording_active:
        elapsed_time = int(time.time() - start_time)
        timer_label.config(text = f"Recording : {elapsed_time} second")
        root.after(1000 , update_timer)


def start_record():
    # freq = 44100 
    # dur = int(duration.get())
    # recording = sound.rec(dur * freq , samplerate = freq , channels = 2 )

    global recording , recording_active , audio_data , start_time
    if not recording_active:
        audio_data = []
        recording_active = True
        start_time = time.time()
        timer_label.config(text = "Recording: 0 sec")
        update_timer()

        start_button.config(state = DISABLED)
        stop_button.config(state = NORMAL) 

        recording = sound.InputStream(callback = callback , samplerate= 96000 , channels= 2 , dtype="float32")
        recording.start()


def stop_record():
    global recording_active , recording

    if recording_active:
        recording_active = False
        timer_label.config(text= "Recording stopped")

        recording.stop()
        recording.close()

        #NumPy dizisine çevirip kaydetme:

        audio_array = np.concatenate(audio_data , axis=0)
        wv.write("recording.wav", audio_array, 96000, sampwidth=4)  # 32-bit float için

        Message.showinfo("Sucess " , "Recording saved successfully!")

        start_button.config(state= NORMAL)
        stop_button.config(state= DISABLED)


    # ----- TIMER -----
    # try:
    #     temp = int(duration.get())
    # except:
    #     print("Enter the right value")

    # while temp > 0:
    #     root.update()
    #     time.sleep(1)
    #     temp -= 1

    #     if temp == 0:
    #         messagebox.showinfo("Time Countdown")
        
    #     Label(text=f"{str(temp)}" , font="arial 40" , width=4 , background="#4a4a4a").place(x=240 , y=590)

    # sound.wait()
    # write("recording.wav" , freq , recording)

timer_label = Label(text = "Voice Recorder" , font = "Arial 15" , background = "#4a4a4a" , fg = "white")
timer_label.pack()



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

# duration = StringVar()
# entry = Entry(root , textvariable=duration, font="arial 30" , width=15 ).pack(pady=10)
# Label(text="Enter time in seconds that you want to record" , font="arial 15" , background="#4a4a4a" , fg="white").pack()

# ----- BUTTONS -----

start_button = Button(root , font="arial 20" , text = "Start" , background = "green" , fg = "white" , border = 0 , command = start_record) 
start_button.pack(pady=10)

stop_button = Button(root , font = "arial 20" , text = "Stop" , background = "red" , fg = "white" , border = 0, command = stop_record)
stop_button.pack(pady=10)




root.mainloop()
