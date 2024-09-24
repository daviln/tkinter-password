from tkinter import *
from tkinter import messagebox  # Added to use messagebox for error and success messages

class Password():
    '''
    This class is a reusable passwords entry form.
    A password needs to be entered and confirmed. 
    The rules of password creation are:
        Passwords must be a minimum length of 8 characters.
        Passwords can only contain alpha or numeric characters, no special characters e.g. space, @, #, &, etc.
        Passwords must contain at least one upper case letter.
        Passwords must contain at least one lower case letter.
        Passwords must contain at least one number.
        Password must be entered twice and must match.

    Passwords are initially displayed using only the * character instead of what the user types in.
    There should be a button available to switch the display of both passwords to the actual text 
    instead of just *'s. The button should toggle between actual characters and * characters only. 
    '''
    def __init__(self):

        #create main window

        self.pwd = None
        self.root = Tk()
        w = self.root.winfo_screenwidth() // 4
        h = self.root.winfo_screenheight() // 4
        self.root.geometry(f'{w}x{h}')
        self.root.title('Create password')

        #add instructions
        self.instr_frame = Frame()
        self.instr_message = Message(self.instr_frame, width=w, text='Passwords must be a minimum length of 8 characters.' +
        '\nPasswords can only contain alpha or numeric characters, no special characters e.g. space, @, #, &, etc.' +
        '\nPasswords must contain at least one upper case letter.' +
        '\nPasswords must contain at least one lower case letter.' +
        '\nPasswords must contain at least one number.\n')
        
        self.instr_message.grid(column=0, row=0)
        self.instr_frame.pack(side=TOP, expand=NO, fill='none', anchor='w')

        # Get user entries
        self.entry_frame = Frame(width=w)
        self.p1_label = Label(self.entry_frame, text='Enter a password')
        self.p1_label.grid(row=1, column=0)
        self.p1_entry = Entry(self.entry_frame)
        self.p1_entry.config(show='*')
        self.p1_entry.grid(row=1, column=1)

        self.p2_label = Label(self.entry_frame, text='Re-enter password')
        self.p2_label.grid(row=3, column=0)
        self.p2_entry = Entry(self.entry_frame)
        self.p2_entry.config(show='*')
        self.p2_entry.grid(row=3, column=1)

        self.show_pwd = Button(self.entry_frame, text='Show password', command=self.show_password)
        self.show_pwd.grid(row=5, column=1)

        self.confirm_button = Button(self.entry_frame, text='Confirm password', command=self.confirm_password)
        self.confirm_button.grid(row=7, column=1)  # Removed () from confirm_password

        self.entry_frame.pack(side=TOP, expand=NO, fill='none', anchor='w')

        #wait for users events
        self.root.mainloop()

    def show_password(self):  # toggle display of * or password
        if self.p1_entry.cget('show') == '*':
            self.show_pwd.configure(text='Hide Password')
            self.p1_entry.config(show='')
            self.p2_entry.config(show='')
        else:
            self.p2_entry.config(show='*')
            self.p1_entry.config(show='*')
            self.show_pwd.configure(text='Show Password')

    def confirm_password(self):  # verify password conforms to rules
        uc = False  # flag for upper case
        lc = False  # flag for lower case
        nu = False  # flag for numeric
        sc = False  # flag for special character

        p = self.p1_entry.get()
        if len(p) >= 8:
            for x in p:
                if x.isupper():
                    uc = True
                if x.islower():  # Check for lowercase letters
                    lc = True
                if x.isdigit():
                    nu = True
                if not x.isalnum():
                    sc = True
        if not uc or not lc or not nu or sc:
            messagebox.showerror(title='Error', message='Invalid password entered')
        else:
            if self.p2_entry.get() == self.p1_entry.get():  # Corrected comparison
                self.pwd = self.p1_entry.get()
                messagebox.showinfo(title='Success', message='Password set successfully.')
                self.root.quit() #switch destroy for quit to ensure no handles
            else:
                messagebox.showerror(title='Error', message='Passwords do not match.')
   
    def get_password(self):  # return the password
        return self.pwd


if __name__ == '__main__':
    p = Password().get_password()
    if p:
        print(p)
