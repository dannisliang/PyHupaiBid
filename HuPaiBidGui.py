import tkinter.messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as tkst

class HuPaiBidGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("拍牌助手")
        self.root.wm_attributes('-topmost',1)
        self.root.geometry('228x260')
        self.root.resizable(0, 0)  
        self.create_menu()
        self.creat_widgets()
        self.root.mainloop()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label = "关于", command=self.about)
        self.root['menu'] = menu_bar

    def creat_widgets(self):
        self.frame_one = tk.Frame(self.root)
        self.time_sync_btn = ttk.Button(self.frame_one, text="模拟测试", command = self.time_sync)  
        self.time_sync_btn.pack(side = tk.LEFT, padx=1, pady=1)
        self.time_drift_lbl = ttk.Label(self.frame_one, text="时间微调:")
        self.time_drift_lbl.pack(side = tk.LEFT, padx=1, pady=1)    
        self.time_drift_input = ttk.Entry(self.frame_one, width=5, justify=tk.RIGHT)
        self.time_drift_input.pack(side = tk.LEFT, padx=1, pady=1) 
        self.time_drift_input.insert(tk.END, '-0.2')    
        self.drift_unit_lbl = ttk.Label(self.frame_one, text="秒")
        self.drift_unit_lbl.pack(side = tk.LEFT, padx=1, pady=1)           
        self.frame_one.pack(side = tk.TOP, expand = tk.YES, fill=tk.X)

        self.frame_two = tk.Frame(self.root)
        self.current_time_lbl = ttk.Label(self.frame_two, text="当前时间:")
        self.current_time_lbl.pack(side = tk.LEFT, padx=1, pady=1)
        self.current_time_display_lbl = ttk.Label(self.frame_two, text="11:29:00.00", relief="groove")
        self.current_time_display_lbl.pack(side = tk.LEFT, padx=1, pady=1)
        self.current_price_lbl = ttk.Label(self.frame_two, text="当前价格:")
        self.current_price_lbl.pack(side = tk.LEFT, padx=1, pady=1)
        self.current_price_display_lbl = ttk.Label(self.frame_two, text="86000", relief="groove")
        self.current_price_display_lbl.pack(side = tk.LEFT, padx=1, pady=1)
        self.frame_two.pack(side = tk.TOP)

        self.frame_three = tk.Frame(self.root)
        self.screnn_coordinate_calibration_btn = ttk.Button(self.frame_three, text="屏幕校准", command = self.screnn_coordinate_calibration)
        self.screnn_coordinate_calibration_btn.pack(side = tk.LEFT, expand = tk.YES, fill=tk.X, padx=1, pady=1)
        self.frame_three.pack(side = tk.TOP, expand = tk.YES, fill=tk.X) 

        self.frame_four = tk.Frame(self.root)
        self.frame_four_time_icon_lbl = ttk.Label(self.frame_four, text="预定时间") 
        self.frame_four_time_icon_lbl.grid(row=0, column=1, columnspan=2, padx=1, pady=1)
        self.frame_four_price_icon_lbl = ttk.Label(self.frame_four, text="自定义加价") 
        self.frame_four_price_icon_lbl.grid(row=0, column=3, padx=1, pady=1)        

        self.first_bid_lbl = ttk.Label(self.frame_four, text="第一次出价: ") 
        self.first_bid_lbl.grid(row=1, column=0, padx=1, pady=1)
        self.first_bid_time_prefix_lbl = ttk.Label(self.frame_four, text="11:29:") 
        self.first_bid_time_prefix_lbl.grid(row=1, column=1, padx=1, pady=1)
        self.first_bid_time_input = ttk.Entry(self.frame_four, width=4, justify=tk.LEFT)
        self.first_bid_time_input.grid(row=1, column=2, padx=1, pady=1)
        self.first_bid_time_input.insert(tk.END, '30')
        self.first_bid_price_input = ttk.Entry(self.frame_four, width=5, justify=tk.RIGHT)
        self.first_bid_price_input.grid(row=1, column=3, padx=1, pady=1)
        self.first_bid_price_input.insert(tk.END, '300')

        self.second_bid_lbl = ttk.Label(self.frame_four, text="第二次出价: ") 
        self.second_bid_lbl.grid(row=2, column=0, padx=1, pady=1)
        self.second_bid_time_prefix_lbl = ttk.Label(self.frame_four, text="11:29:") 
        self.second_bid_time_prefix_lbl.grid(row=2, column=1, padx=1, pady=1)        
        self.second_bid_time_input = ttk.Entry(self.frame_four, width=4, justify=tk.LEFT)
        self.second_bid_time_input.grid(row=2, column=2, padx=1, pady=1)
        self.second_bid_time_input.insert(tk.END, '48')
        self.second_bid_price_input = ttk.Entry(self.frame_four, width=5, justify=tk.RIGHT)
        self.second_bid_price_input.grid(row=2, column=3, padx=1, pady=1)
        self.second_bid_price_input.insert(tk.END, '600')  
        self.frame_four.pack(side = tk.TOP)

        self.frame_five = tk.Frame(self.root)
        self.log_display = tkst.ScrolledText(self.frame_five, wrap=tk.WORD)
        self.log_display.pack()  
        self.frame_five.pack(side = tk.TOP)      

    def screnn_coordinate_calibration(self):
        pass

    def time_sync(self):
        pass

    def about(self):
        tk.messagebox.showinfo('关于', 'Python版拍牌小助手\nwmpluto@gmail.com')