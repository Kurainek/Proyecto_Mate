import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 1. Creación del grafo ponderado G = (V, E, w)
G = nx.Graph()

# 2. Vértices (V): 15 ciudades principales de la India
ciudades = [
    "Nueva Delhi", "Jaipur", "Agra", "Lucknow", "Kanpur",
    "Varanasi", "Patna", "Bhopal", "Indore", "Ahmedabad",
    "Surat", "Mumbai", "Pune", "Hyderabad", "Bengaluru"
]
G.add_nodes_from(ciudades)

# 3. Aristas (E) y Pesos (w): Distancias de conducción reales de Google Maps (en kilómetros)
conexiones = [
    ("Nueva Delhi", "Jaipur", 280),
    ("Nueva Delhi", "Agra", 230),
    ("Agra", "Jaipur", 240),
    ("Agra", "Lucknow", 330),
    ("Lucknow", "Kanpur", 90),
    ("Kanpur", "Varanasi", 330),
    ("Varanasi", "Patna", 250),
    ("Jaipur", "Ahmedabad", 680),
    ("Ahmedabad", "Surat", 260),
    ("Surat", "Mumbai", 280),
    ("Mumbai", "Pune", 150),
    ("Pune", "Hyderabad", 560),
    ("Hyderabad", "Bengaluru", 570),
    ("Ahmedabad", "Indore", 390),
    ("Indore", "Bhopal", 190),
    ("Bhopal", "Agra", 540),
    ("Indore", "Jaipur", 600),
    ("Pune", "Bengaluru", 840),
    ("Mumbai", "Ahmedabad", 530),
    ("Hyderabad", "Mumbai", 710),
    ("Lucknow", "Varanasi", 300)
]
G.add_weighted_edges_from(conexiones)

# 4. Posiciones relativas aproximadas a la geografía real de la India para el gráfico
posiciones = {
    "Nueva Delhi": (4, 9),
    "Jaipur": (3, 8),
    "Agra": (5, 8),
    "Lucknow": (6, 7.5),
    "Kanpur": (5.5, 7),
    "Varanasi": (7, 6.5),
    "Patna": (8, 6.5),
    "Bhopal": (5, 5.5),
    "Indore": (4, 5.5),
    "Ahmedabad": (2, 5),
    "Surat": (2, 4),
    "Mumbai": (2, 3),
    "Pune": (3, 2.5),
    "Hyderabad": (5, 2),
    "Bengaluru": (4, 0)
}

class AplicacionRutaOptima:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Proyecto Final: Matemática Discreta - Ruta Óptima en Auto (India)")
        self.ventana.geometry("1150x750")
        
        # Paleta de colores: Negro, Azul, Blanco
        self.BG_MAIN = "#000000"       
        self.BG_PANEL = "#121212"      
        self.FG_TEXT = "#ffffff"       
        self.COLOR_AZUL = "#0055ff"    
        self.BG_TEXTBOX = "#1e1e1e"    
        
        self.ventana.configure(bg=self.BG_MAIN)

        # Panel Izquierdo: Controles
        panel_izquierdo = tk.Frame(ventana, width=320, bg=self.BG_PANEL, padx=20, pady=20, bd=0)
        panel_izquierdo.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(panel_izquierdo, text="CONFIGURACIÓN", font=("Arial", 14, "bold"), bg=self.BG_PANEL, fg=self.COLOR_AZUL).pack(pady=(10, 20))

        tk.Label(panel_izquierdo, text="Ciudad de Origen:", font=("Arial", 11, "bold"), bg=self.BG_PANEL, fg=self.FG_TEXT).pack(anchor="w", pady=(5, 2))
        self.combo_origen = ttk.Combobox(panel_izquierdo, values=sorted(ciudades), state="readonly", font=("Arial", 10))
        self.combo_origen.pack(fill=tk.X, pady=5)
        self.combo_origen.set("Nueva Delhi")

        tk.Label(panel_izquierdo, text="Ciudad de Destino:", font=("Arial", 11, "bold"), bg=self.BG_PANEL, fg=self.FG_TEXT).pack(anchor="w", pady=(15, 2))
        self.combo_destino = ttk.Combobox(panel_izquierdo, values=sorted(ciudades), state="readonly", font=("Arial", 10))
        self.combo_destino.pack(fill=tk.X, pady=5)
        self.combo_destino.set("Bengaluru")

        self.btn_calcular = tk.Button(panel_izquierdo, text="Calcular Ruta Óptima", font=("Arial", 11, "bold"), 
                                      bg=self.COLOR_AZUL, fg=self.FG_TEXT, activebackground="#0033cc", activeforeground=self.FG_TEXT,
                                      command=self.calcular_ruta_optima, cursor="hand2", relief="flat", pady=8)
        self.btn_calcular.pack(fill=tk.X, pady=30)

        tk.Label(panel_izquierdo, text="RESULTADOS", font=("Arial", 12, "bold"), bg=self.BG_PANEL, fg=self.COLOR_AZUL).pack(anchor="w", pady=(10, 5))
        
        self.txt_resultados = tk.Text(panel_izquierdo, height=18, width=30, font=("Consolas", 10), bg=self.BG_TEXTBOX, fg=self.FG_TEXT, bd=0, highlightthickness=1, highlightbackground=self.COLOR_AZUL, wrap=tk.WORD, padx=10, pady=10)
        self.txt_resultados.pack(fill=tk.BOTH, expand=True)
        self.txt_resultados.config(state="disabled")

        # Panel Derecho: Gráfico
        self.panel_derecho = tk.Frame(ventana, bg=self.BG_MAIN)
        self.panel_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.fig.patch.set_facecolor('#ffffff') 
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.panel_derecho)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        self.actualizar_grafico(ruta_optima=None)

    def actualizar_grafico(self, ruta_optima=None):
        self.ax.clear()
        self.ax.set_facecolor('#ffffff')
        self.ax.set_title("Red de Carreteras en India - Algoritmo de Dijkstra", fontdict={'fontsize': 13, 'fontweight': 'bold', 'color': '#000000'})

        # 1. Dibujar nodos y aristas base
        nx.draw_networkx_nodes(G, posiciones, ax=self.ax, node_color=self.COLOR_AZUL, node_size=350)
        nx.draw_networkx_edges(G, posiciones, ax=self.ax, edge_color="#d3d3d3", width=1.2)
        
        # Mostrar los pesos (distancias) en las aristas
        labels_pesos = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, posiciones, edge_labels=labels_pesos, ax=self.ax, font_size=7, font_color="#555555")

        # 2. Dibujar la ruta resaltada si existe
        if ruta_optima:
            aristas_ruta = [(ruta_optima[i], ruta_optima[i+1]) for i in range(len(ruta_optima)-1)]
            # Dibujar nodos y aristas de la ruta en negro
            nx.draw_networkx_nodes(G, posiciones, ax=self.ax, nodelist=ruta_optima, node_color="#000000", node_size=400)
            nx.draw_networkx_edges(G, posiciones, ax=self.ax, edgelist=aristas_ruta, edge_color="#000000", width=3.5)

        # Desplazamos la posición en 'Y' +0.3 para que el texto flote por encima del nodo
        pos_labels = {nodo: (coords[0], coords[1] + 0.3) for nodo, coords in posiciones.items()}
        
        # Dibujamos las etiquetas con un fondo blanco suave para que no se tachen con las líneas
        nx.draw_networkx_labels(
            G, 
            pos_labels, 
            ax=self.ax, 
            font_size=8, 
            font_weight="bold", 
            font_color="#000000",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.8, pad=0.5)
        )

        self.ax.axis('off')
        self.canvas.draw()

    def calcular_ruta_optima(self):
        origen = self.combo_origen.get()
        destino = self.combo_destino.get()

        if origen == destino:
            messagebox.showwarning("Atención", "La ciudad de origen y destino deben ser diferentes.")
            return

        try:
            ruta = nx.dijkstra_path(G, source=origen, target=destino, weight='weight')
            costo_total = nx.dijkstra_path_length(G, source=origen, target=destino, weight='weight')

            # Cálculo de tiempo en auto 
            velocidad_auto_kmh = 80 
            tiempo_horas = costo_total / velocidad_auto_kmh
            
            horas = int(tiempo_horas)
            minutos = int((tiempo_horas - horas) * 60)

            recorrido_texto = " ➔\n ".join(ruta)
            
            reporte = (
                f"DESDE:  {origen}\n"
                f"HASTA:  {destino}\n"
                f"{'-'*25}\n"
                f"RECORRIDO ÓPTIMO:\n {recorrido_texto}\n"
                f"{'-'*25}\n"
                f"DISTANCIA TOTAL:\n 📍 {costo_total} km\n\n"
                f"TIEMPO DE VIAJE:\n 🚗 {horas}h {minutos}m\n"
                f" (a {velocidad_auto_kmh} km/h)"
            )

            self.txt_resultados.config(state="normal")
            self.txt_resultados.delete("1.0", tk.END)
            self.txt_resultados.insert(tk.END, reporte)
            self.txt_resultados.config(state="disabled")

            self.actualizar_grafico(ruta_optima=ruta)

        except nx.NetworkXNoPath:
            messagebox.showerror("Error", "No se encontró un camino entre las ciudades seleccionadas.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionRutaOptima(root)
    root.mainloop()