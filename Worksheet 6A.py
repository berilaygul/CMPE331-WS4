"""
    Stage: Development-01
    @author:Beril Aygul, 119202033
    @author:Cihan Armagan Guner, 118204026
    
    Stage: Development-02:
    @author : Deniz Gunenc, 120200078
    @author : Ali Can Dogan, 120200068

    Code Review: 
    @author: Umut Kalay, 120202016
    @author: Giragos Başak, 119202045
"""

import tkinter as tk


class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()

    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.
        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """

    def _initializeGUI(self):
        self.lbl01 = tk.Label(text="Username")
        self.lbl02 = tk.Label(text="Password")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry(show="*")

        self.btn01 = tk.Button(text="Login")
        self.btn02 = tk.Button(text="Reset Pass")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)

    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """

    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)

    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.
        :param event: action event for detecting which button is clicked
    """

    def handle_click(self, event):
        # if the button is clicked login or exit
        if event.widget == self.btn01:
            self.login()
        # elif event.widget == self.btn02:
            # will be implemented

    def login(self):
        # open the new page after login
        self.window.destroy()
        NewPage()


class NewPage:
    # constructor
    def __init__(self):
        self.window = tk.Tk()
        # set the title of the window
        self.window.title("Book Search")

        # initialize GUI elements
        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()

    def _initializeGUI(self):
        # Login Message
        self.lblLoggedin = tk.Label(text="Successfully logged in")
        # Book Search
        self.lblBookNumber = tk.Label(text="Book Number:")
        self.txtBookNumber = tk.Entry()
        self.txtBookNumber.insert(0, "Enter number 1-5")
        # Book Name
        self.lblBookName = tk.Label(text="Book Name:")
        self.lblgetBookName = tk.Label(text="")
        # Book Code
        self.lblBookCode = tk.Label(text="Book Code:")
        self.lblgetBookCode = tk.Label(text="")
        # Search Button
        self.btnSearch = tk.Button(text="Search")
        self.btnSearch.bind("<Button-1>", self.handle_click)
        # Logout Button
        self.btnLogout = tk.Button(text="Logout")
        self.btnLogout.bind("<Button-1>", self.handle_click)

    def _addGUIElementsToFrame(self):
        # Set the layout of the GUI elements
        self.lblLoggedin.grid(row=0, column=0, padx=10, pady=5)
        self.lblBookNumber.grid(row=1, column=0, padx=10, pady=5)
        self.txtBookNumber.grid(row=1, column=1, padx=10, pady=5)
        self.lblBookName.grid(row=2, column=0, padx=10, pady=5)
        self.lblgetBookName.grid(row=2, column=1, padx=10, pady=5)
        self.lblBookCode.grid(row=3, column=0, padx=10, pady=5)
        self.lblgetBookCode.grid(row=3, column=1, padx=10, pady=5)
        self.btnSearch.grid(row=4, column=0, padx=10, pady=5)
        self.btnLogout.grid(row=4, column=1, padx=10, pady=5)

    def handle_click(self, event):
        # if the button is clicked, apply the related operation
        if event.widget == self.btnSearch:
            self.search()
        elif event.widget == self.btnLogout:
            self.logout()

    def search(self):
        # books list
        mybooks = [["169", "Harry Potter"], ["231", "Lord of the Rings"], ["420", "The Hobbit"], ["404", "The Alchemist"],
                   ["505", "The Little Prince"]]
        # get the book number from the text box
        bookNumber = self.txtBookNumber.get()
        # check if the book number is valid
        if bookNumber < "1" or bookNumber > "5":
            # if the book number is invalid, display the error message
            self.lblgetBookCode.config(text="Invalid book number")
            self.lblgetBookName.config(text=" Please enter a number between 1 and 5")
        else:
            # if the book number is valid, display the book code and name
            self.lblgetBookCode.config(text=mybooks[int(bookNumber) - 1][0])
            self.lblgetBookName.config(text=mybooks[int(bookNumber) - 1][1])

    def logout(self):
        # destroy the current window and open the login window
        self.window.destroy()
        LoginWindow()




# main method for testing the application
if __name__ == "__main__":
    LoginWindow()