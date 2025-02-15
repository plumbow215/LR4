import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo, showerror

root = tkinter.Tk()
root.title('Tkinter File Reader')
root.resizable(True, True)
root.geometry('500x300')

def select_file():
    target = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if target:
        try:
            with open(target, 'r') as file:
                content = file.read()
            
            showinfo(
                title='Selected File',
                message=f"File: {target}\n\nContent:\n{content}"
            )
        except Exception as e:
            showerror(title='Error', message=f"An error occurred: {e}")
    else:
        showinfo(title='No Selection', message='No file was selected.')

select_button = ttk.Button(root, text='Select Text File', command=select_file)
select_button.pack(pady=20)

root.mainloop()
