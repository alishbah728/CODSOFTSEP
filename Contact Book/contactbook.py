import tkinter as tk
from tkinter import messagebox

# Create an empty list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Name and Phone fields are required.")

# Function to update the contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, contact["Name"] + " - " + contact["Phone"])

# Function to clear the input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to search for a contact
def search_contact():
    search_text = search_entry.get().lower()
    matching_contacts = [contact for contact in contacts if search_text in contact["Name"].lower() or search_text in contact["Phone"]]
    contact_listbox.delete(0, tk.END)
    for contact in matching_contacts:
        contact_listbox.insert(tk.END, contact["Name"] + " - " + contact["Phone"])

# Function to view selected contact details
def view_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        contact = contacts[index]
        messagebox.showinfo("Contact Details", f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
    else:
        messagebox.showwarning("Warning", "Please select a contact from the list.")

# Function to delete a contact
def delete_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        contacts.pop(index)
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Please select a contact from the list.")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create and place input fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Create and place buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

# Create and place the contact listbox
contact_listbox = tk.Listbox(root, width=40, height=10)
contact_listbox.pack()

# Update the contact list initially
update_contact_list()

# Run the Tkinter main loop
root.mainloop()
