window = Tk()
window.geometry("300x200")
window.title("Images downloader")

search_key_var = StringVar(value="")
directory_var = StringVar(value=path.expanduser("~\\Desktop"))
images_number_var = StringVar(value="")


Label(window, text="Directory :").pack()
Entry(window, textvariable=directory_var).pack(fill=X)
Button(window, text="Select directory", command=ask_directory).pack()

Label(window, text="Number of images :").pack()
Spinbox(window, state="readonly", from_=1, to=30, textvariable=images_number_var).pack()

Label(window, text="Search keyword :").pack()
Entry(window, textvariable=search_key_var).pack(fill=X)

Button(window, text="Download", command=partial(download, search_key_var, directory_var, images_number_var)).pack()


window.mainloop()
