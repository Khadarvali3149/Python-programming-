import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_entry = tk.Entry(master, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please enter at least Name and Phone.")

    def view_contacts(self):
        if self.contacts:
            contact_info = ""
            for contact in self.contacts:
                contact_info += f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n\n"
            messagebox.showinfo("Contacts", contact_info)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")

    def search_contact(self):
        search_name = simpledialog.askstring("Search Contact", "Enter Name to search:")
        if search_name:
            found_contacts = [contact for contact in self.contacts if contact["Name"].lower() == search_name.lower()]
            if found_contacts:
                contact_info = ""
                for contact in found_contacts:
                    contact_info += f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n\n"
                messagebox.showinfo("Search Results", contact_info)
            else:
                messagebox.showinfo("Search Results", f"No contacts found with name: {search_name}")
        else:
            messagebox.showwarning("Warning", "Please enter a name to search.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
