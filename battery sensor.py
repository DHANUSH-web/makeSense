# Simple battery status detection with GUI (Graphical User Interface)
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
from time import strftime
# from win10toast import ToastNotifier
import platform
import psutil

t = strftime("%H : %M : %S %p")
print(f"Started battery tracking, Time: {t}")

window = Tk()
window.title(f"{platform.system()} platform")
window['bg'] = "white"
window.geometry("720x380")
window.resizable(0, 0)
window.iconbitmap("D:\\Coursera (python)\\Spyder_Projects\\Battery_Sensor\\icon.ico")


# define time duration capacity
def durCap(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%dh %02dm %02ds" % (hours, minutes, seconds)


# defining the information for disp1
def disp1_info():
    os_lbl = platform.system()
    ps = psutil.sensors_battery()
    status_lbl = ps.power_plugged
    per_lbl = ps.percent
    duration_lbl = durCap(ps.secsleft).replace("-", "")
    os.config(text=f"Operating System: {os_lbl}")
    if status_lbl:
        status.config(text="Battery Status: Charging", pady=5)
        power.config(text="Power Plugged: Yes", pady=5)
    else:
        status.config(text="Battery Status: Not Charging", pady=5)
        power.config(text="Power Plugged: No", pady=5)
    per.config(text=f"Battery Percentage: {per_lbl}% remain", pady=5)
    duration.config(text=f"Expected Duration: {duration_lbl}", pady=5)
    ipVoltage.config(text="Input Voltage: 11.45 V", pady=5)
    ipCurrent.config(text="Input Current: 0.552 mA", pady=5)
    duration.after(300, disp1_info)


def disp2_graphics():
    get = psutil.sensors_battery()
    getp = get.percent
    charge_left.config(text=f"{getp}%")
    if getp <= 40:
        style.configure("grey.Horizontal.TProgressbar", background='red')
    elif getp in range(50, 80):
        style.configure("grey.Horizontal.TProgressbar", background='blue')
    else:
        style.configure("grey.Horizontal.TProgressbar", background='green')
    indicate['value'] = getp
    indicate.update_idletasks()
    charge_left.after(300, disp2_graphics)


def credit():
    name = "Dhanush H V"
    course = "Electronics and Communication Engineering"
    college = "ATME college of Engineering, Mysuru"
    pro = "Python"
    software = "PyCharm IDE"
    modules = "Tkinter, time, win10toast(not active), Platform, Psutil"
    message = f"""
    This simple app is developed for student project on developing windows applications\n
    Programmer      : {name}
    Qualification   : B.E
    Course          : {course}
    College         : {college}
    Written in      : {pro}
    Software        : {software}
    Modules used    : {modules}
    """
    messagebox.showinfo("Credits", message)
    print(message)


# def notifier(num, condition, work):
#     toast = ToastNotifier()
#     toast.show_toast("Warning:", f"Battery is {condition} to {num}%, please {work} the power plug",
#                      "alert.ico", 0)
loop_not = []
def notifier():
    get1 = psutil.sensors_battery()
    get2 = get1.percent
    is_plugged = get1.power_plugged
    lst = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    t = strftime("%H:%M:%S %p")

    if is_plugged:
        print(f"Charger plugged, Time: {t}")
        if (get2 in lst) and (get2 not in loop_not):
            print(f"Battery is charged to {get2}%, Time: {t}")
            loop_not.append(get2)
        elif get2 == 100 and (get2 not in loop_not):
            status.config(foreground="red")
            power.config(foreground="red")
            print(f"Battery is fully charged(100%, Time: {t}), please remove power plug inorder to avoid Over-Heating")
            messagebox.showwarning("WARNING!!", "Battery is fully charged please remove the power plug")
            loop_not.append(get2)

    else:
        if get2 in lst[0:5] and (get2 not in loop_not):
            status.config(foreground="black")
            print(f"Battery is drained to {get2}%, please plug the power adapter")
            loop_not.append(get2)
            
        elif get2 in lst and (get2 not in loop_not):
            print(f"Battery is drained to {get2}%, Time: {t}")
            loop_not.append(get2)
            
        elif get2 < 20 and (get2 not in loop_not):
            status.config(foreground="red")
            power.config(foreground="red")
            print(f"Battery low({get2}%), please plug the power adapter")
            loop_not.append(get2)
    ipCurrent.after(1000, notifier)

# frame contains all the information of your system
battery_info = Frame(window, relief="ridge", bd=2, background="white")
battery_info.pack(side="top", padx=12, pady=12, fill="x")

header = Label(battery_info, text="Battery Information", font=("Arial", 12, "bold"), background="white",
               foreground="black", pady=5)
header.pack(side="top")

# Information content display
content = Frame(window, relief="ridge", bd=2, background="white", height="300")
content.pack(side="top", padx=12, pady=12, fill="both", expand=True)

# disp1 is to display battery information
disp1 = Frame(content, bd=0, background="white")
disp1.pack(side="left", padx=12, pady=12, fill="y")

os = Label(disp1, font=("Arial", 12, "bold"), foreground="black", background="white")
os.pack(side="top")

status = Label(disp1, font=("Arial", 12, "bold"), foreground="black", background="white")
status.pack(side="top")

power = Label(disp1, font=("Arial", 12, "bold"), foreground="black", background="white")
power.pack(side="top")

per = Label(disp1, font=("Arial", 12, "bold"), foreground="black", background="white")
per.pack(side="top")

duration = Label(disp1, font=("Arial", 12, "bold"), foreground="black", background="white")
duration.pack(side="top")

ipVoltage = Label(disp1, font=("Arial", 12, "bold"), foreground="black", background="white")
ipVoltage.pack(side="top")

ipCurrent = Label(disp1, font=("Arial", 12, "bold"), foreground="black", background="white")
ipCurrent.pack(side="top")
disp1_info()

# disp2 is for battery charging graphics
disp2 = Frame(content, bd=0, background="white")
disp2.pack(side="right", padx=12, pady=12, fill="y")

charge_left = Label(disp2, font=("Arial", 45, "bold", "italic"), background="white", foreground="black")
charge_left.pack(side="top", padx=40, pady=30)

style = Style()
style.theme_use("default")
indicate = Progressbar(disp2, orient=HORIZONTAL, length=400, mode='determinate', style="grey.Horizontal.TProgressbar")
indicate.pack(side="top", padx=12, pady=12)
disp2_graphics()

notifier()

btn = Button(disp2, text="Credits", width=12, background="white", foreground="blue", bd=2, relief="ridge", command=credit,
             font=("Arial", 12, "bold"))
btn.pack(side="right", padx=12, pady=12)

window.mainloop()
