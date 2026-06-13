import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuración de página con estética premium y limpia
st.set_page_config(
    page_title="CakePopPR - Cotizaciones",
    page_icon="assets/logo_cakepoppr.png",
    layout="centered"
)

# Estilos personalizados basados en la identidad visual de CakePopPR
st.markdown("""
    <style>
    .subtitle { 
        color: #D4A59A; 
        font-size: 16px; 
        text-align: center; 
        font-style: italic; 
        margin-bottom: 25px; 
    }

    .stCheckbox label { 
        font-weight: bold; 
        color: #4A2E2B; 
    }

    .stButton>button { 
        background-color: #4A2E2B; 
        color: white; 
        border-radius: 20px; 
        border: none; 
        width: 100%; 
        font-weight: bold; 
    }

    .stButton>button:hover { 
        background-color: #D4A59A; 
        color: #4A2E2B; 
    }

    div[data-testid="stExpander"] { 
        background-color: #FDFBF7; 
        border-radius: 8px; 
        border-left: 4px solid #D4A59A; 
        margin-bottom: 10px; 
    }
    </style>
""", unsafe_allow_html=True)

# Logo oficial de CakePopPR
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])

with col_logo2:
    st.image("assets/logo_cakepoppr.png", width=280)

# Subtítulo del sistema
st.markdown(
    '<div class="subtitle">Sistema de Cotizaciones de Cookies Personalizadas</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">CakePopPR 🍪</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Sistema de Cotizaciones de Cookies Personalizadas</div>', unsafe_allow_html=True)

# Base de datos extraída directamente de tu 'Price Lookup'
@st.cache_data
def cargar_precios_oficiales():
    return {
        # 2" Royal Icing
        '2"|Royal Icing|12': 21.00, '2"|Royal Icing|24': 42.00, '2"|Royal Icing|36': 63.00, '2"|Royal Icing|48': 84.00,
        '2"|Royal Icing|100': 175.00, '2"|Royal Icing|200': 350.00, '2"|Royal Icing|300': 525.00, '2"|Royal Icing|500': 875.00, '2"|Royal Icing|700': 1225.00,
        # 2" Fondant
        '2"|Fondant|12': 26.04, '2"|Fondant|24': 52.08, '2"|Fondant|36': 78.12, '2"|Fondant|48': 104.16,
        '2"|Fondant|100': 217.00, '2"|Fondant|200': 434.00, '2"|Fondant|300': 651.00, '2"|Fondant|500': 1085.00, '2"|Fondant|700': 1519.00,
        # 2.5" Royal Icing
        '2.5"|Royal Icing|12': 31.08, '2.5"|Royal Icing|24': 62.16, '2.5"|Royal Icing|36': 93.24, '2.5"|Royal Icing|48': 124.32,
        '2.5"|Royal Icing|100': 259.00, '2.5"|Royal Icing|200': 518.00, '2.5"|Royal Icing|300': 777.00, '2.5"|Royal Icing|500': 1295.00, '2.5"|Royal Icing|700': 1813.00,
        # 2.5" Fondant
        '2.5"|Fondant|12': 35.64, '2.5"|Fondant|24': 71.28, '2.5"|Fondant|36': 106.92, '2.5"|Fondant|48': 142.56,
        '2.5"|Fondant|100': 297.00, '2.5"|Fondant|200': 594.00, '2.5"|Fondant|300': 891.00, '2.5"|Fondant|500': 1485.00, '2.5"|Fondant|700': 2079.00,
        # 3" Royal Icing
        '3"|Royal Icing|12': 41.40, '3"|Royal Icing|24': 82.80, '3"|Royal Icing|36': 124.20, '3"|Royal Icing|48': 165.60,
        '3"|Royal Icing|100': 345.00, '3"|Royal Icing|200': 690.00, '3"|Royal Icing|300': 1035.00, '3"|Royal Icing|500': 1725.00, '3"|Royal Icing|700': 2415.00,
        # 3" Fondant
        '3"|Fondant|12': 48.00, '3"|Fondant|24': 96.00, '3"|Fondant|36': 144.00, '3"|Fondant|48': 192.00,
        '3"|Fondant|100': 400.00, '3"|Fondant|200': 800.00, '3"|Fondant|300': 1200.00, '3"|Fondant|500': 2000.00, '3"|Fondant|700': 2800.00,
        # 4" Royal Icing
        '4"|Royal Icing|12': 65.52, '4"|Royal Icing|24': 131.04, '4"|Royal Icing|36': 196.56, '4"|Royal Icing|48': 262.08,
        '4"|Royal Icing|100': 546.00, '4"|Royal Icing|200': 1092.00, '4"|Royal Icing|300': 1638.00, '4"|Royal Icing|500': 2730.00, '4"|Royal Icing|700': 3822.00,
        # 4" Fondant
        '4"|Fondant|12': 72.00, '4"|Fondant|24': 144.00, '4"|Fondant|36': 216.00, '4"|Fondant|48': 288.00,
        '4"|Fondant|100': 600.00, '4"|Fondant|200': 1200.00, '4"|Fondant|300': 1800.00, '4"|Fondant|500': 3000.00, '4"|Fondant|700': 4200.00
    }

precios_dict = cargar_precios_oficiales()

# Seccón 1: Información del Cliente
st.markdown('<h3 style="color: #4A2E2B; font-size: 18px;">1. Detalles del Cliente y Entrega</h3>', unsafe_allow_html=True)
c_info1, c_info2 = st.columns(2)
with c_info1:
    nombre_cliente = st.text_input("Nombre del Cliente", value="Amarilis")
    telefono_cliente = st.text_input("Teléfono", value="787-429-7753")
with c_info2:
    fecha_recogido = st.date_input("Fecha de Recogido", datetime.strptime("2026-11-25", "%Y-%m-%d").date())
    lugar_recogido = st.text_input("Lugar de Recogido", value="Las Piedras")

fecha_hoy = datetime.now().date()
fecha_validez = fecha_hoy + timedelta(days=5)

# Sección 2: Configuración de Opciones (Replicando las 4 columnas del Excel)
st.markdown('<h3 style="color: #4A2E2B; font-size: 18px;">2. Configuración de Opciones (Hasta 4 alternativas)</h3>', unsafe_allow_html=True)

lista_tamanos = ['2"', '2.5"', '3"', '4"']
lista_acabados = ['Royal Icing', 'Fondant']
lista_cantidades = [12, 24, 36, 48, 100, 200, 300, 500, 700]

opciones_validas = []

for i in range(1, 5):
    # Valores predeterminados idénticos a tu plantilla de prueba
    def_inc = True
    def_sz = '2"' if i <= 2 else '2.5"'
    def_fn = 'Royal Icing' if i % 2 != 0 else 'Fondant'
    
    with st.expander(f"OPCIÓN {i}", expanded=(i==1)):
        incluir = st.checkbox("Incluir en cotización", value=def_inc, key=f"inc_{i}")
        if incluir:
            col_sz, col_fn, col_qty = st.columns(3)
            with col_sz:
                sz = st.selectbox("Tamaño", lista_tamanos, index=lista_tamanos.index(def_sz), key=f"sz_{i}")
            with col_fn:
                fn = st.selectbox("Acabado", lista_acabados, index=lista_acabados.index(def_fn), key=f"fn_{i}")
            with col_qty:
                qty = st.selectbox("Cantidad", lista_cantidades, index=0, key=f"qty_{i}")
                
            key_lookup = f"{sz}|{fn}|{qty}"
            subtotal = precios_dict.get(key_lookup, 0.0)
            
            # Cálculos financieros precisos
            ivu = round(subtotal * 0.115, 4)
            total = round(subtotal + ivu, 4)
            
            opciones_validas.append({
                "id": f"OPTION {i}",
                "sz": sz,
                "fn": fn,
                "qty": qty,
                "subtotal": subtotal,
                "ivu": ivu,
                "total": total
            })

# Sección 3: Cálculos del Resumen y Generación del Mensaje
if opciones_validas:
    subtotal_total = sum(o['subtotal'] for o in opciones_validas)
    ivu_total = sum(o['ivu'] for o in opciones_validas)
    gran_total = sum(o['total'] for o in opciones_validas)
    
    st.markdown('<h3 style="color: #4A2E2B; font-size: 18px;">3. Resumen Financiero Automático</h3>', unsafe_allow_html=True)
    
    # Mostrar tarjetas con los totales globales
    c_card1, c_card2, c_card3 = st.columns(3)
    c_card1.metric("Subtotal", f"${subtotal_total:,.2f}")
    c_card2.metric("IVU (11.5%)", f"${ivu_total:,.2f}")
    c_card3.metric("Total General", f"${gran_total:,.2f}")
    
    # Construcción exacta del formato 'QUOTE TEMPLATE' para WhatsApp
    texto_whatsapp = f"""Cotización de Cookies Personalizadas

*Cliente:* {nombre_cliente}
*Teléfono:* {telefono_cliente}
*Fecha de cotización:* {fecha_hoy.strftime('%Y-%m-%d')}
*Fecha de recogido:* {fecha_recogido.strftime('%Y-%m-%d')}
*Lugar de recogido:* {lugar_recogido}
*Cotización válida hasta:* {fecha_validez.strftime('%Y-%m-%d')}

--------------------------------------------
*Opciones seleccionadas para enviar al cliente:*
"""
    for o in opciones_validas:
        texto_whatsapp += f"""
• *{o['id']}:* Galletas de {o['sz']} ({o['fn']})
  *Cantidad:* {o['qty']} unidades
  *Subtotal:* ${o['subtotal']:,.2f} | *IVU:* ${o['ivu']:,.2f}
  *Total:* ${o['total']:,.2f}
"""
        
    texto_whatsapp += f"""--------------------------------------------
*Resumen de Totales:*
Subtotal Combinado: ${subtotal_total:,.2f}
IVU 11.5%: ${ivu_total:,.2f}
*Total Neto Orden:* ${gran_total:,.2f}

Gracias por confiar en CakePopPR 💙

*Notas importantes:*
• La cotización incluye IVU de 11.5%.
• Los precios pueden variar si se añaden diseños complejos, empaques especiales, cambios de tamaño o elementos personalizados adicionales.
• Para reservar la fecha se recomienda confirmar la orden y el método de pago.
• La fecha y el lugar de recogido se confirman según disponibilidad de CakePopPR.

📆 *Validez de la cotización:*
• 5 días naturales.
• 24 horas si la fecha de entrega es dentro de las próximas dos semanas o antes.

🎨 *Personalización del diseño:*
• El diseño será inspirado en el ejemplo provisto, buscando lograr una apariencia lo más parecida posible.
• Sin embargo, pueden haber ligeras variaciones en colores, sprinkles u otros detalles, dependiendo de la disponibilidad en los comercios al momento de adquirir los materiales.

📍 *Recogido:*
• Se coordina previamente en Las Piedras, PR.

💵 *Depósito requerido:*
• 50% del total para reservar la fecha (No reembolsable).

💰 *Saldo pendiente:*
• Debe liquidarse el día de la entrega.
"""

    st.markdown('<h3 style="color: #4A2E2B; font-size: 18px;">4. Mensaje Completo para enviar al Cliente</h3>', unsafe_allow_html=True)
    st.text_area("Haz clic en cualquier parte del cuadro, selecciona todo (Ctrl+A / Cmd+A), copia y pega en WhatsApp:", texto_whatsapp, height=380)
else:
    st.info("Selecciona e incluye al menos una opción en la parte superior para calcular la cotización.")
