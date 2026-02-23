import customtkinter
import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd



class Tree_view(): 
    def __init__(self, master, **kwargs):
        # self.tree_scroll = ttk.Scrollbar(master=master)
        # self.tree_scroll.pack(side="right", fill="y")
        # yscrollcommand=self.tree_scroll.set,
        self.im_unchecked = tk.PhotoImage(width=16, height=16) # Placeholder
        self.im_checked = tk.PhotoImage(width=16, height=16)   # Placeholder
        
        # Fill placeholders with colors so you can see them (Red/Green)
        self.im_unchecked.put(("gray",), to=(0, 0, 15, 15))
        self.im_checked.put(("green",), to=(0, 0, 15, 15))

        


        self.tree = ttk.Treeview(master=master)
        self.tree.grid(row=1, column=1, columnspan=4, sticky="nsew")

        self.scroll = ttk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        self.scroll.grid(row=0, column=1, sticky="ns")

        self.tree.configure(yscrollcommand=self.scroll.set)
        self.tree.bind("<Button-1>", self.on_click)

    def mount_table(self):

        df = read_csv()

        if df is None:
            return
        # reset table before add items
        self.tree.delete(*self.tree.get_children())

        

        self.tree["column"] = list(df.columns)
        self.tree["show"] = "headings"
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for row in df.itertuples(index=False): 
            self.tree.insert("", "end", text="SELECT", image=self.im_unchecked, values=row)

    def on_click(self, event):
        return
    
class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame, for example:

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Produção de Ticket")

        # configure window root grid system
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=8)
        self.grid_columnconfigure((0,1,2,3), weight=2)

        self.mainFrame = Frame(master=self)
        self.mainFrame.grid(row=1, column=0, columnspan=4 ,sticky="nsew")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure((0,1), weight=1)

        self.header = Frame(self)
        self.header.grid(row=0, column=0, sticky="news", padx=8, pady=8)
        self.header.grid_columnconfigure(2, weight=1)


        
        self.frame = Frame(master=self.mainFrame)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame.grid_rowconfigure((0), weight=1)
        self.frame.grid_rowconfigure((1), weight=8)
        self.frame.grid_rowconfigure((2), weight=1)
        self.frame.grid_columnconfigure((0,1,2,3), weight=2)
        
        self.frame.grid_propagate(False)
        self.left_header = Frame(self.frame, bg_color="transparent")
        self.left_header.grid(row=0, column=0, columnspan=4, sticky="ew")
        self.container = Frame(self.frame)
        self.container.grid(row=1, column=1, columnspan=4, sticky="nsew")


        self.selectionFrame = Frame(master=self.mainFrame)
        self.selectionFrame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        

        self.tree = Tree_view(master=self.container)
        
        
        # add widgets to app
        # self.button = customtkinter.CTkButton(self, command=self.tree.mount_table)
        # self.button.grid(row=0, column=0, padx=10, pady=10)

        self.btn_load = tk.Button(self.header, text="Carregar CSV", command=self.tree.mount_table)
        self.btn_load.grid(row=0, column=0, padx=4)
        self.btn_to_sel = tk.Button(self.header, text="Enviar selecionados →", command=read_csv)
        self.btn_to_sel.grid(row=0, column=1, padx=4)

        


def fill_table(table, df):
    table["column"] = list (df.columns)
    table["show"] = "heading"

    for col in table["column"]:
        table.heading(col, text=col)
        table.column(col, width=100)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        table.insert("", "end", values=row)
        

def read_csv():
    """ Read CSV and return Pandas data frame
    """
    try:
        filepath = filedialog.askopenfile() # get file path
        if filepath is None:
            return
    except:
        print("Error occured")

    df = pd.read_csv(
        filepath,
        sep=",",
        encoding="utf-8",
        dtype=str,
        parse_dates=False
    )
    return df

if __name__ == "__main__":
    app = App()
    app.mainloop()