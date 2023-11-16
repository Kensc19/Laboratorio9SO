import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import librosa

# Función para cargar un archivo de audio
def cargar_audio():
    # Abre un cuadro de diálogo para seleccionar un archivo de audio
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.wav")])

    # Si el usuario seleccionó un archivo
    if archivo:
        # Obtiene el contenido del archivo de audio
        audio, _ = librosa.load(archivo)

        # Crea el espectrograma del audio
        spectrograma = librosa.amplitude_to_db(librosa.feature.melspectrogram(y=audio))

        # Muestra el espectrograma en una nueva ventana
        mostrar_spectrograma(spectrograma)

# Función para mostrar el espectrograma en una nueva ventana
def mostrar_spectrograma(spectrograma):
    # Crea una ventana secundaria para mostrar el espectrograma
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.geometry("300x200")
    ventana_secundaria.config(bg="blue")

    # Crea un lienzo para dibujar el espectrograma en la ventana secundaria
    lienzo = ctk.CTkCanvas(ventana_secundaria, width=spectrograma.shape[1], height=spectrograma.shape[0])
    lienzo.draw_spectrogram(spectrograma)

    # Muestra la ventana secundaria
    ventana_secundaria.mainloop()

# Función principal
def main():
    # Crea la ventana principal
    ventana_principal = tk.Tk()

    # Configura el tamaño de la ventana principal
    ventana_principal.geometry("300x200")

    # Crea el botón para agregar audio
    boton_agregar_audio = tk.Button(ventana_principal, text="Agregar audio", command=cargar_audio)
    boton_agregar_audio.grid(row=0, column=0, padx=10, pady=10)

    # Crea el botón para mostrar el espectrograma
    boton_mostrar = tk.Button(ventana_principal, text="Mostrar", command=cargar_audio)
    boton_mostrar.grid(row=0, column=1, padx=10, pady=10)

    ventana_principal.config(bg="light blue")
    # Muestra la ventana principal
    ventana_principal.mainloop()

if __name__ == "__main__":
    main()
