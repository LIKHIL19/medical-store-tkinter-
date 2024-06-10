import tkinter as tk
from PIL import Image, ImageTk

class Medicine:
    def _init_(self, name, problem, cost, quantity=0, total_cost_for_medicine=0):
        self.name = name
        self.problem = problem
        self.cost = cost
        self.quantity = quantity
        self.total_cost_for_medicine = total_cost_for_medicine

def suggest_medicine(problem):
    if problem == "headache":
        return Medicine("Aspirin", "headache", 10)
    elif problem == "fever":
        return Medicine("Paracetamol", "fever", 20)
    elif problem == "cough":
        return Medicine("Cough Syrup", "cough", 80)
    elif problem == "flu":
        return Medicine("Tamiflu", "flu", 20)
    elif problem == "allergies":
        return Medicine("Claritin", "allergies", 30)
    elif problem == "stomachache":
        return Medicine("Pepto-Bismol", "stomachache", 40)
    elif problem == "sore throat":
        return Medicine("Throat Lozenges", "sore throat", 30)
    elif problem == "back pain":
        return Medicine("Ibuprofen", "back pain", 30)
    else:
        return Medicine("Unavailable", "Unknown", 0)

def calculate_medicine():
    choice = int(selected_choice.get())
    problems = [
        "headache", "fever", "cough", "flu",
        "allergies", "stomachache", "sore throat", "back pain"
    ]
    problem = problems[choice - 1] if 1 <= choice <= 8 else "Unknown"

    medicine = suggest_medicine(problem)

    if medicine.name != "Unavailable":
        quantity = int(quantity_entry.get())
        medicine.quantity = quantity

        medicine.total_cost_for_medicine = medicine.cost * medicine.quantity
        medicines.append(medicine)

        total_cost = sum(med.total_cost_for_medicine for med in medicines)
        total_medicines = sum(med.quantity for med in medicines)

        total_bill_label.config(text=f"Total Medicines: {total_medicines}\nTotal Bill: Rs.{total_cost}")

        # Show summary of each medicine taken
        update_medicines_details()

def on_submit():
    calculate_medicine()
    selected_choice.set(0)
    quantity_entry.delete(0, tk.END)

def update_medicines_details():
    summary_text = "\n".join([f"{med.name}: Quantity - {med.quantity}, Total Cost - Rs.{med.total_cost_for_medicine}" for med in medicines])
    medicines_details_text.delete(1.0, tk.END)
    medicines_details_text.insert(tk.END, summary_text)

# Create tkinter window
root = tk.Tk()
root.title("Pharmacy")
root.geometry("600x550")
root.configure(bg="white")

new_width = 500
new_height = 500


heading_label = tk.Label(root, text="Pharmacy", font=("Arial", 20), bg="beige")
heading_label.pack(pady=10)

home_frame = tk.Frame(root, bg="white", padx=10, pady=10)
home_frame.pack(pady=20)

selected_choice = tk.IntVar()
medicines = []

choice_label = tk.Label(home_frame, text="Select your health problem:", font=("Arial", 12))
choice_label.pack()

for i, problem in enumerate([
    "Headache", "Fever", "Cough", "Flu",
    "Allergies", "Stomachache","Sore Throat", "Back Pain"
], start=1):
    tk.Radiobutton(home_frame, text=problem, variable=selected_choice, value=i, font=("Arial", 10)).pack()

quantity_label = tk.Label(home_frame, text="Enter quantity (if applicable):", font=("Arial", 12))
quantity_label.pack()

quantity_entry = tk.Entry(home_frame)
quantity_entry.pack()

submit_button = tk.Button(home_frame, text="Submit", command=on_submit, font=("Arial", 12))
submit_button.pack()

bill_frame = tk.Frame(root, bg="white", padx=10, pady=10)
bill_frame.pack(pady=20)

total_bill_heading = tk.Label(bill_frame, text="Total Bill", font=("Arial", 16))
total_bill_heading.pack()

total_bill_label = tk.Label(bill_frame, text="", font=("Arial", 14), bg="white", height=10, width=40)
total_bill_label.pack(padx=5, pady=5)

medicines_details_text = tk.Text(bill_frame, font=("Arial", 12), bg="white", height=20, width=50)
medicines_details_text.pack()

def update_bill_display():
    total_cost = sum(med.total_cost_for_medicine for med in medicines)
    total_medicines = sum(med.quantity for med in medicines)
    total_bill_label.config(text=f"Total Medicines: {total_medicines}\nTotal Bill: Rs.{total_cost}")
    update_medicines_details()

bill_frame.after(100, update_bill_display)

root.mainloop()
