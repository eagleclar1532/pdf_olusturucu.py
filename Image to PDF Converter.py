import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
    
class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()
        

    def initialize_ui(self):
        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        #Resim seçme düğmesi
        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_images_button.pack(pady=5)

        #Seçili resimleri görüntülemek için liste kutusu
        self.selected_images_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # PDF name entry
        pdf_name_label = tk.Label(self.root, text="PDF Output Name:")
        pdf_name_label.pack(pady=5)
        pdf_name_entry = tk.Entry(self.root, textvariable=self.pdf_name)
        pdf_name_entry.pack(pady=5)

        # Convert to PDF button
        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_to_pdf)
        convert_button.pack(pady=10)

    def select_images(self):
        # Open file dialog to select image files
        filetypes = [("Image files", "*.jpg;*.jpeg;*.png")]
        image_files = filedialog.askopenfilenames(title="Select Images", filetypes=filetypes)
        self.image_paths = list(image_files)

        # Update the listbox with selected images
        self.selected_images_listbox.delete(0, tk.END)
        for image_path in self.image_paths:
            self.selected_images_listbox.insert(tk.END, os.path.basename(image_path))

    def convert_to_pdf(self):
        if not self.image_paths:
            messagebox.showerror("Error", "No images selected")
            return

        if not self.pdf_name.get():
            messagebox.showerror("Error", "Please enter a name for the output PDF")
            return

        images = []
        for image_path in self.image_paths:
            img = Image.open(image_path)
            img = img.convert("RGB")  # Ensure all images are in RGB mode
            images.append(img)

        # Save as PDF
        output_path = f"{self.pdf_name.get()}.pdf"
        images[0].save(output_path, save_all=True, append_images=images[1:])
        messagebox.showinfo("Success", f"PDF created successfully: {output_path}")

def main():
    root = tk.Tk()
    root.title("Image to PDF")
    root.geometry("400x600")
    converter = ImageToPDFConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
