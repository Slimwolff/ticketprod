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
        self.tree.grid(row=20,column=0,padx=20, pady=20)
        # self.tree_scroll.config(command=self.tree.yview)

    def mount_table(self):

        df = read_csv()

        # reset table before add items
        self.tree.delete(*self.tree.get_children())
        

        self.tree["column"] = list(df.columns)
        self.tree["show"] = "headings"
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for row in df.itertuples(index=False): 
            self.tree.insert("", "end", text="SELECT", image=self.im_unchecked, values=row)

class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, text="Custom Label Frame")
        self.label.grid(row=0, column=0, padx=20)

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


        self.frame = Frame(master=self.mainFrame)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame.grid_propagate(False)

        self.selectionFrame = Frame(master=self.mainFrame)
        self.selectionFrame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        

        self.tree = Tree_view(master=self.frame)
        
        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.tree.mount_table)
        self.button.grid(row=0, column=0, padx=10, pady=10)

        self.input = customtkinter.CTkTextbox(self, corner_radius=20, width=200, height=30)
        self.input.grid(row=0, column=1, padx=5, pady=1)
    # open file (CSV) to the context
   


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
            return None
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