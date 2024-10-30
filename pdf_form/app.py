import os
from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'Datos Personales', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C', new_x='LMARGIN', new_y='NEXT')

    def add_person_data(self, data):
        self.set_font('Helvetica', '', 12)
        
        for key, value in data:
            self.cell(0, 10, f"{key}: {value}", new_x='LMARGIN', new_y='NEXT')
        self.ln(10)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Recibir los datos del formulario
        person_data = [
                ("Nombre", request.form.get("nombre", "")),
                ("Apellidos", request.form.get("apellidos", "")),
                ("Fecha de nacimiento", request.form.get("fecha_nacimiento", "")),
                ("Documento de Identidad", f"{request.form.get('documento_identidad', '')} {request.form.get('documento_input', '')}"),
                ("Teléfono", request.form.get("telefono", "")),
                ("Email", request.form.get("email", "")),
                ("Dirección", request.form.get("direccion", "")),
                ("Localidad", request.form.get("localidad", "")),
                ("Provincia", request.form.get("provincia", ""))
            ]

        # Crear el PDF
        pdf = PDF()
        pdf.add_page()
        pdf.add_person_data(person_data)

        # Asegurar que el directorio de salida existe
        app_dir = os.path.dirname(os.path.abspath(__file__)) # Usar la ubicación del archivo app.py como base
        output_dir = os.path.join(app_dir, "static", "output")
        os.makedirs(output_dir, exist_ok=True)

        # Guardar el PDF
        output_path = os.path.join(output_dir, "generated_file.pdf")
        pdf.output(output_path)

        # Verificar si el archivo se ha creado
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            return send_file(output_path, as_attachment=True)

        return "Error al generar el PDF", 500

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
