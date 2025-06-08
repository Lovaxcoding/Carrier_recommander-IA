import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

model = joblib.load('model.pkl')
le_interest = joblib.load('le_interest.pkl')
le_skills = joblib.load('le_skills.pkl')
le_edu = joblib.load('le_edu.pkl')
le_career = joblib.load('le_career.pkl')

def predict():
    try:
        interest = le_interest.transform([entry_interest.get()])[0]
        skill = le_skills.transform([entry_skills.get()])[0]
        edu = le_edu.transform([entry_edu.get()])[0]

        inputs = np.array([[interest, skill, edu]])
        pred = model.predict(inputs)[0]
        label = le_career.inverse_transform([pred])[0]

        messagebox.showinfo("Résultat", f"Carrière recommandée : {label}")
    except:
        messagebox.showerror("Erreur", "Entrées invalides. Vérifiez les valeurs.")

root = tk.Tk()
root.title("Recommandeur de carrière")

tk.Label(root, text="Centre d'intérêt :").grid(row=0, column=0)
entry_interest = tk.Entry(root)
entry_interest.grid(row=0, column=1)

tk.Label(root, text="Compétence principale :").grid(row=1, column=0)
entry_skills = tk.Entry(root)
entry_skills.grid(row=1, column=1)

tk.Label(root, text="Niveau d'études :").grid(row=2, column=0)
entry_edu = tk.Entry(root)
entry_edu.grid(row=2, column=1)

tk.Button(root, text="Recommander", command=predict).grid(row=3, columnspan=2, pady=10)

tk.Label(root, text="Exemples valides :").grid(row=4, column=0, columnspan=2)
tk.Label(root, text="Intérêts : Science, Arts, Math, People, Business").grid(row=5, column=0, columnspan=2)
tk.Label(root, text="Compétences : Data Analysis, Creativity, Problem Solving, Communication, Leadership").grid(row=6, column=0, columnspan=2)
tk.Label(root, text="Études : High School, Bachelor, Master").grid(row=7, column=0, columnspan=2)

root.mainloop()
