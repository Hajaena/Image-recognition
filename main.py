# reconnaissance d'image
import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
import matplotlib.pyplot as plt
import os
import ttkbootstrap as ttk

save_dir = "detections/"
os.makedirs(save_dir, exist_ok=True)


# initialisation
fenetre = ttk.Window(themename="flatly")
fenetre.title("Image recognition")
fenetre.configure(bg="#A3D9A5")

fenetre.geometry("600x400")

image_path = ""
image_path2 = ""

def ouvrir_fichier():
    # Ouvrir une boite de dialogue
    image_path = filedialog.askopenfilename(
        title="Sélectionnez la 1ere image JPG ou PNG",
        filetypes=[("Fichier image", "*.jpg;*.png")]
    )
    if image_path:
        print(f"ok: {image_path}")

        # Charger le modèle YOLOv5
        model = YOLO("yolov5su.pt")  # Modèle recommandé avec performances améliorées

        # Effectuer une détection
        results1 = model(image_path)
        # results2 = model(image_path2)

        annotated_img1 = results1[0].plot()
        # annotated_img2 = results2[0].plot()

        # Convertir en image PIL et sauvegarder
        #Image.fromarray(annotated_img1).save("detections/result1.jpg")
        # Image.fromarray(annotated_img2).save("detections/result2.jpg")

        print(results1)
        # print(results2)

        # Sauvegarder les résultats dans un dossier
        # results1[0].save(save_dir="detections/")  # Enregistrer les résultats annotés
        # results2[0].save(save_dir="detections/")

        # extraxtion des resultat
        # boxe1 = results1

        # Afficher les résultats avec Matplotlib
        plt.imshow(results1[0].plot())
        plt.axis('off')
        plt.show()


    else:
        print("ok")


text1 = tk.Label(fenetre, text=" 🔍 Image Recognition", padx= 1000, pady= 12, font=("Verdana", 20, "bold"))
text1.pack( pady = 10)

bouton = ttk.Button(fenetre, text="🪴clic here to analyse an image ",bootstyle="success-outline", padding=20, command=ouvrir_fichier)
bouton.pack(pady = 100)

fenetre.mainloop()
