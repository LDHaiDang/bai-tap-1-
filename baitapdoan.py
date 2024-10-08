import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Datsan:
    def __init__(self, customer_name, field_number, amount):
        self.customer_name = customer_name
        self.field_number = field_number
        self.amount = amount

class Quanlysanbong:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Sân Bóng")

        self.bookings = []

        self.setup_ui()

    def setup_ui(self):
        self.tab_control = ttk.Notebook(self.root)

        # Tab 1: Nhập thông tin khách hàng
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Đặt Sân")

        self.customer_name_label = tk.Label(self.tab1, text="Tên Khách Hàng:")
        self.customer_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.customer_name_entry = tk.Entry(self.tab1)
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.field_number_label = tk.Label(self.tab1, text="Số Sân:")
        self.field_number_label.grid(row=1, column=0, padx=10, pady=10)
        self.field_number_entry = tk.Entry(self.tab1)
        self.field_number_entry.grid(row=1, column=1, padx=10, pady=10)

        self.amount_label = tk.Label(self.tab1, text="Số Tiền:")
        self.amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.tab1)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_booking_button = tk.Button(self.tab1, text="Thêm", command=self.add_booking)
        self.add_booking_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Tab 2: Hiển thị tổng số tiền và số sân đã đặt
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text="Thống Kê")

        self.total_amount_label = tk.Label(self.tab2, text="Tổng Số Tiền Thu Được:")
        self.total_amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.total_amount_value = tk.Label(self.tab2, text="0")
        self.total_amount_value.grid(row=0, column=1, padx=10, pady=10)

        self.total_fields_label = tk.Label(self.tab2, text="Tổng Số Sân Đã Đặt:")
        self.total_fields_label.grid(row=1, column=0, padx=10, pady=10)
        self.total_fields_value = tk.Label(self.tab2, text="0")
        self.total_fields_value.grid(row=1, column=1, padx=10, pady=10)

        self.details_label = tk.Label(self.tab2, text="Chi Tiết Khách Hàng:")
        self.details_label.grid(row=2, column=0, padx=10, pady=10)
        self.details_listbox = tk.Listbox(self.tab2, width=50)
        self.details_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.tab_control.pack(expand=1, fill='both')

    def add_booking(self):  
        customer_name = self.customer_name_entry.get()
        field_number = self.field_number_entry.get()
        amount = self.amount_entry.get()

        if customer_name and field_number and amount:
            try:
                amount = int(amount)
                new_booking = Datsan(customer_name, field_number, amount)
                self.bookings.append(new_booking)
                self.update_statistics()
                messagebox.showinfo("Thông báo", "Đặt sân thành công!")
            except ValueError:
                messagebox.showerror("Cảnh báo", "Số tiền phải là một số")
        else:
            messagebox.showerror("Cảnh báo", "Tất cả các trường đều bắt buộc")

    def update_statistics(self):
        total_amount = sum(booking.amount for booking in self.bookings)
        total_fields = len(self.bookings)

        self.total_amount_value.config(text=str(total_amount))
        self.total_fields_value.config(text=str(total_fields))

        self.details_listbox.delete(0, tk.END)
        for booking in self.bookings:
            self.details_listbox.insert(tk.END, f"Tên: {booking.customer_name}, Sân: {booking.field_number}, Tiền: {booking.amount} VND")

if __name__ == "__main__":
    root = tk.Tk()
    app = Quanlysanbong(root)
    root.mainloop()
