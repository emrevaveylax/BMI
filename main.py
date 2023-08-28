import tkinter as tk

def calculate_bmi():
    height = float(entry_height.get())
    weight = float(entry_weight.get())
    bmi = weight / (height / 100) ** 2
    result_label.config(text=f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        category_label.config(text="Durum: Zayıf")
    elif bmi < 24.9:
        category_label.config(text="Durum: Normal")
    elif bmi < 29.9:
        category_label.config(text="Durum: Kilolu")
    else:
        category_label.config(text="Durum: Obez")


#Arayüz
root = tk.Tk()
root.title("BMI Hesaplama")


#Boy Etikleti ve Giriş
label_height = tk.Label(root, text="Boy (cm):")
label_height.pack()
entry_height = tk.Entry(root)
entry_height.pack()

#Kilo Etiketi ve Giriş
label_weight = tk.Label(root, text="Kilo (kg):")
label_weight.pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

#Hesapla Butonu
calculate_button = tk.Button(root, text="Hesapla", command=calculate_bmi)
calculate_button.pack()

#BMI sonucu ve Durum Etiketi
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack()

category_label = tk.Label(root, text="", font=("Helvetica, 16"))
category_label.pack()


root.mainloop()