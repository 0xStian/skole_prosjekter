from tkinter import *
import tkinter.filedialog as filedialog
import hashlib


def start_hash_cracker():
    root = Tk()
    window_width, window_height = 1000, 500
    window_x_pos, window_y_pos = 500, 100
    root.geometry(f'{window_width}x{window_height}+{window_x_pos}+{window_y_pos}')
    root.title("Huldra Hash Cracker")
    
    
    root.configure(bg="black")
    root.resizable(False,False)


    def check_hash(password_list, hashes_list, hash_type):
        with open(hashes_list, 'r', encoding='latin-1') as hashes_list:
            for line in hashes_list:
                current_hash = line.strip()
                crack_hash(current_hash, hash_type, password_list)
                
                
    def crack_hash(hash, hash_type, password_list):
        with open(password_list, 'r', encoding='latin-1') as password_list:
            for line in password_list:
                current_password = line.strip()
                match hash_type:
                    case "md5": 
                        hashed_password = hashlib.md5(current_password.encode("utf-8")).hexdigest()
                    case "sha1": 
                        hashed_password = hashlib.sha1(current_password.encode("utf-8")).hexdigest()
                    case "sha256": 
                        hashed_password = hashlib.sha256(current_password.encode("utf-8")).hexdigest()
                    case "sha512": 
                        hashed_password = hashlib.sha512(current_password.encode("utf-8")).hexdigest()
                if hashed_password == hash:
                    hashes_output.insert(END, f"{hashed_password}:{current_password}\n")
    
    def start():
        hash_type = clicked.get().strip().lower()
        hash_path = hash_input_entry.get()
        passwords_path = password_input_entry.get()
        hashes_output.delete("1.0", "end")
        check_hash(passwords_path, hash_path, hash_type)

        
        
    def about():
        hashes_output.delete("1.0", "end")
        about="""
        About:
        
        This program is used for cracking hashes.
        It works by supplying a list of hashes and a list of password.
        It then hashes the password and if the hashed password matches
        with a hash,we would call it cracked.
        
        The program was made during a codejam, the objective was to
        convert an already existing hash cracker made in an earlier
        codejam into an interactive GUI."""
        hashes_output.insert(END, about)
        

    def input_hash_file():
        hash_path = filedialog.askopenfilename()
        hash_input_entry.delete(1, END) 
        hash_input_entry.insert(0, hash_path) 
    
    
    def input_password_file():
        password_path = filedialog.askopenfilename()
        password_input_entry.delete(1, END) 
        password_input_entry.insert(0, password_path) 


    # Title
    Label(root, text="<Huldra_Hash_Cracker>", font=("Terminal", 35, "bold"), bg="purple", fg="black").place(x=0, y=0, width=1000, height=75)


    # line break
    line1 = Frame(root, height=3, width=1000, bg="grey", relief='groove').place(x=0, y=75)
    line2 = Frame(root, height=3, width=400, bg="grey", relief='groove').place(x=0, y=160)
    line3 = Frame(root, height=3, width=400, bg="grey", relief='groove').place(x=0, y=245)
    line4 = Frame(root, height=3, width=400, bg="grey", relief='groove').place(x=0, y=335)
    line5 = Frame(root, height=500, width=3, bg="grey", relief='groove').place(x=400, y=75)


    # input hash file
    hash_path = Label(root, text="Hash File:", font=("System 10 bold"), bg="purple", fg="black")
    hash_path.place(x=10, y=90, width=110, height=30)
    hash_input_entry = Entry(root, text="", width=32, bg="grey")
    hash_input_entry.place(x=10, y=125)
    browse_path = Button(root, text="Browse", bg="light grey", command=input_hash_file)
    browse_path.place(x=210, y=125, width=60, height=21)

    # input password file
    password_path = Label(root, text="Password File:", font=("System 10 bold"), bg="purple", fg="black")
    password_path.place(x=10, y=175, width=110, height=30)
    password_input_entry = Entry(root, text="", width=32, bg="grey")
    password_input_entry.place(x=10, y=210)
    browse_path = Button(root, text="Browse", bg="light grey", command=input_password_file)
    browse_path.place(x=210, y=210, width=60, height=21)

    # hash type
    options = ["MD5", "SHA1", "SHA256", "SHA512"]
    clicked = StringVar()
    clicked.set( "Select" )
    Label(root, text="Select Hash Type:", font=("System", 15, "bold"), bg="purple", fg="black").place(x=10, y=260, width=140, height=30)
    hash_type_menu = OptionMenu( root, clicked, *options)
    hash_type_menu.config(bg="grey", fg="black", font=("System 10 bold"))
    hash_type_menu.place(x=155, y=260, width=110, height=30)

    # cracked hashes
    Label(root, text="Cracked Hashes", font=("System", 20, "bold"), bg="grey", fg="black").place(x=400, y=75, width=600, height=35)
    hashes_output = Text(root, bg="light grey")
    hashes_output.place(x=408, y=115, width=586, height=380)

    # menu button
    menu_button = Button(root, text='Back', command=NONE, font=("Fixedsys 5 bold"), bg="purple")
    menu_button.place(x=50, y=460, width=100, height=20)
    # about button
    about_button = Button(root, text='About?', command=about, font=("Fixedsys 5 bold"), bg="purple")
    about_button.place(x=150, y=460, width=100, height=20)
    # exit button
    exit_button = Button(root, text='Exit', command=root.destroy, font=("Fixedsys 5 bold"), bg="purple")
    exit_button.place(x=250, y=460, width=100, height=20)

    # start button
    begin_button = Button(root, text='Start', command=start, font=("Fixedsys 30 bold"), bg="purple")
    begin_button.place(x=50, y=360, width=300, height=100)

    
    root.mainloop()

start_hash_cracker()