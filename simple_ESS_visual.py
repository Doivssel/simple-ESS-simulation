from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from simple_ESS import *

class GUI:
    
    def __init__(self,windows):
        """
        Parameters:
        windows: tk.Tk() instance
        
        Goal:
        Creating GUI"""
        self.windows=windows
        windows.title("ESS visual")
        windows.attributes('-fullscreen',True)
        windows.update()

        self.paraText=Label(windows,text="Parameters : ")
        self.max_foodText=Label(windows,text="Max_food : ")
        self.food_initText=Label(windows,text="Food_init : ")
        self.loss_foodText=Label(windows,text="Loss_food : ")
        self.value_foodText=Label(windows,text="Value_food : ")
        self.rep_foodText=Label(windows,text="Rep_food : ")
        self.fight_penaltyText=Label(windows,text="Fight_penalty : ")
        self.pop_sizeText=Label(windows,text="Pop_size : ")
        self.prob_egoistText=Label(windows,text="Prob_egoist : ")
        self.num_dayText=Label(windows,text="Num_day : ")

        self.paraText.grid(row=0,column=1,sticky=NSEW)
        self.max_foodText.grid(row=1,column=1,sticky=NSEW)
        self.food_initText.grid(row=2,column=1,sticky=NSEW)
        self.loss_foodText.grid(row=3,column=1,sticky=NSEW)
        self.value_foodText.grid(row=4,column=1,sticky=NSEW)
        self.rep_foodText.grid(row=5,column=1,sticky=NSEW)
        self.fight_penaltyText.grid(row=6,column=1,sticky=NSEW)
        self.pop_sizeText.grid(row=7,column=1,sticky=NSEW)
        self.prob_egoistText.grid(row=8,column=1,sticky=NSEW)
        self.num_dayText.grid(row=9,column=1,sticky=NSEW)

        self.max_foodEntry=Entry(windows)
        self.food_initEntry=Entry(windows)
        self.loss_foodEntry=Entry(windows)
        self.value_foodEntry=Entry(windows)
        self.rep_foodEntry=Entry(windows)
        self.fight_penaltyEntry=Entry(windows)
        self.pop_sizeEntry=Entry(windows)
        self.prob_egoistEntry=Entry(windows)
        self.num_dayEntry=Entry(windows)

        self.max_foodEntry.insert(0,"100")
        self.food_initEntry.insert(0,"5")
        self.loss_foodEntry.insert(0,"0.5")
        self.value_foodEntry.insert(0,"1")
        self.rep_foodEntry.insert(0,"10")
        self.fight_penaltyEntry.insert(0,"1")
        self.pop_sizeEntry.insert(0,"100")
        self.prob_egoistEntry.insert(0,"0.5")
        self.num_dayEntry.insert(0,"100")

        self.max_foodEntry.grid(row=1,column=2,sticky=NSEW)
        self.food_initEntry.grid(row=2,column=2,sticky=NSEW)
        self.loss_foodEntry.grid(row=3,column=2,sticky=NSEW)
        self.value_foodEntry.grid(row=4,column=2,sticky=NSEW)
        self.rep_foodEntry.grid(row=5,column=2,sticky=NSEW)
        self.fight_penaltyEntry.grid(row=6,column=2,sticky=NSEW)
        self.pop_sizeEntry.grid(row=7,column=2,sticky=NSEW)
        self.prob_egoistEntry.grid(row=8,column=2,sticky=NSEW)
        self.num_dayEntry.grid(row=9,column=2,sticky=NSEW)


        self.leaveButton=Button(windows,text="QUIT",command=windows.quit)
        self.SimulateButton=Button(windows,text='Simulate',command=self.simulate)

        self.leaveButton.grid(row=11,column=2,sticky=NSEW,columnspan=2)
        self.SimulateButton.grid(row=10,column=2,sticky=NSEW,columnspan=2)

        figure1=plt.Figure(figsize=(windows.winfo_width()*0.8,windows.winfo_height()*0.5), dpi=1)
        a=figure1.add_subplot(111)

        self.canvas1=FigureCanvasTkAgg(figure1, windows)
        self.canvas1.get_tk_widget().grid(row=0,column=0,rowspan=6)

        self.canvas2=FigureCanvasTkAgg(figure1, windows)
        self.canvas2.get_tk_widget().grid(row=6,column=0,rowspan=6)

    
    def simulate(self):
        """
        Parameters:
        None
        
        Goal:
        Function to execute when simulate button is pressed
        Update both canvas to show the proportion and individual graph
        
        Notes:
        Maybe add a visual of the ind going to food"""
        ess=ESS(
                int(self.max_foodEntry.get()),
                float(self.food_initEntry.get()),
                float(self.loss_foodEntry.get()),
                float(self.value_foodEntry.get()),
                float(self.rep_foodEntry.get()),
                float(self.fight_penaltyEntry.get()),
                int(self.pop_sizeEntry.get()),
                float(self.prob_egoistEntry.get()),
                int(self.num_dayEntry.get())
                )
        
        ess.simulation()
        abs=[i for i in range(ess.num_day)]
        figure1=plt.Figure(figsize=(windows.winfo_width()*0.008,windows.winfo_height()*0.005), dpi=100)
        plot1=figure1.add_subplot(111)
        plot1.plot(abs,ess.altruist,label="Altruist")
        plot1.plot(abs,ess.egoist,label="Egoist")
        plot1.set_title("Number of egoist/altruist per day")
        plot1.legend()
        plot1.set_xlabel("Days")
        plot1.set_ylabel("Number of individual")

        self.canvas1=FigureCanvasTkAgg(figure1, windows)
        self.canvas1.get_tk_widget().grid(row=0,column=0,rowspan=6)

        figure2=plt.Figure(figsize=(windows.winfo_width()*0.008,windows.winfo_height()*0.005), dpi=100)
        plot2=figure2.add_subplot(111)
        plot2.plot(abs,ess.prop_alt,label="Altruist")
        plot2.plot(abs,ess.prop_ego,label="Egoist")
        plot2.legend()
        plot2.set_title("Proportion of egoist/altruist per day")
        plot2.set_xlabel("Days")
        plot2.set_ylabel("Proportion")

        self.canvas2=FigureCanvasTkAgg(figure2, windows)
        self.canvas2.get_tk_widget().grid(row=6,column=0,rowspan=6)


windows=Tk()
interface=GUI(windows)
windows.update()
windows.mainloop()