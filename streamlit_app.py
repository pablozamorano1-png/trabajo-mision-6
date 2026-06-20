import streamlit as st
import pandas as pd

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================
st.set_page_config(
    page_title="Portafolio Gerencial Directivo",
    page_icon="💼",
    layout="wide"
)

# ============================================================
# ESTILO VISUAL: AZUL CORPORATIVO, SOBRIO Y PROFESIONAL
# ============================================================
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: linear-gradient(135deg, #f4f8fa 0%, #eef5f9 45%, #f7fbfd 100%);
        }

        .main-title {
            padding: 1.5rem 1.7rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 55%, #60a5fa 100%);
            color: white;
            box-shadow: 0 14px 35px rgba(37, 99, 235, 0.15);
            margin-bottom: 1.2rem;
        }

        .main-title h1 {
            margin: 0;
            font-size: 2.15rem;
            line-height: 1.15;
            font-weight: 800;
            color: white !important;
        }

        .main-title p {
            margin-top: .65rem;
            font-size: 1.02rem;
            opacity: .95;
            color: white !important;
        }

        .section-card {
            padding: 1.25rem 1.35rem;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.85);
            border: 1px solid rgba(37, 99, 235, 0.15);
            box-shadow: 0 10px 25px rgba(30, 58, 138, 0.05);
            margin-bottom: 1rem;
            color: #1e293b;
        }

        .soft-card {
            padding: 1.05rem 1.15rem;
            border-radius: 16px;
            background: #ffffffcc;
            border-left: 6px solid #2563eb;
            box-shadow: 0 8px 22px rgba(37, 99, 235, 0.06);
            min-height: 155px;
            margin-bottom: 1rem;
        }

        .mini-card {
            padding: .95rem 1rem;
            border-radius: 16px;
            background: #ffffffd9;
            border: 1px solid #dbeafe;
            box-shadow: 0 6px 18px rgba(37, 99, 235, 0.04);
            min-height: 135px;
            margin-bottom: 1rem;
            color: #1e3a8a;
        }

        .concept-pill {
            display: inline-block;
            padding: .35rem .7rem;
            margin: .18rem .18rem .18rem 0;
            border-radius: 999px;
            background: #e0f2fe;
            color: #0369a1;
            font-weight: 700;
            font-size: .86rem;
            border: 1px solid #bae6fd;
        }

        h1, h2, h3, h4, h5 {
            color: #1e3a8a;
        }

        div[data-testid="stMetricValue"] {
            color: #2563eb;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: .4rem;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: #ffffffb8;
            border-radius: 999px;
            padding: .6rem 1rem;
            border: 1px solid #dbeafe;
            color: #64748b;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #bae6fd, #e0f2fe) !important;
            color: #1e3a8a !important;
            font-weight: 800;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# FUNCIONES DE APOYO VISUAL
# ============================================================
def hero(titulo: str, bajada: str):
    st.markdown(f'<div class="main-title"><h1>{titulo}</h1><p>{bajada}</p></div>', unsafe_allow_html=True)

def card(titulo: str, texto: str, icono: str = "🔹"):
    st.markdown(f'<div class="soft-card"><h3>{icono} {titulo}</h3><p>{texto}</p></div>', unsafe_allow_html=True)

def mini_card(titulo: str, texto: str, icono: str = "•"):
    st.markdown(f'<div class="mini-card"><h4>{icono} {titulo}</h4><p>{texto}</p></div>', unsafe_allow_html=True)



def concepto(nombre: str):
    st.markdown(f"<span class='concept-pill'>{nombre}</span>", unsafe_allow_html=True)

# ============================================================
# BASES DE CONTENIDO REUTILIZABLES
# ============================================================
MAPA_AREAS = {
    "📊 Dirección / Gerencia": {
        "titulo": "Alta Dirección / Gerencia",
        "rol": "Define el rumbo del negocio, prioriza recursos y alinea a todas las áreas bajo una estrategia común.",
        "decisiones": [
            "Definir metas, prioridades y foco competitivo.",
            "Aprobar inversiones, presupuestos y políticas generales.",
            "Resolver tensiones entre crecimiento, servicio y rentabilidad."
        ],
        "conecta": ["💰 Finanzas", "📈 Comercial / Ventas", "📦 Compras y Abastecimiento", "⚙️ Operaciones y Bodega", "🚦 Control de Gestión"],
        "color": "#1e3a8a"
    },
    "💰 Finanzas": {
        "titulo": "Finanzas y Contabilidad",
        "rol": "Transforma los movimientos de la empresa en información económica útil para cuidar liquidez, costo y rentabilidad.",
        "decisiones": [
            "Validar costos reales y márgenes del negocio.",
            "Controlar caja, presupuesto y estructura financiera.",
            "Definir alertas sobre riesgos de liquidez o rentabilidad."
        ],
        "conecta": ["📊 Dirección / Gerencia", "📈 Comercial / Ventas", "📦 Compras y Abastecimiento", "⚙️ Operaciones y Bodega", "🚦 Control de Gestión"],
        "color": "#ca8a04"
    },
    "📈 Comercial / Ventas": {
        "titulo": "Comercial / Ventas",
        "rol": "Capta la demanda, administra la relación con clientes y genera los ingresos de la empresa.",
        "decisiones": [
            "Segmentar clientes y definir cobertura comercial.",
            "Priorizar cuentas clave, ofertas y canales de venta.",
            "Proyectar demanda para orientar compras y stock."
        ],
        "conecta": ["📊 Dirección / Gerencia", "📦 Compras y Abastecimiento", "⚙️ Operaciones y Bodega", "💰 Finanzas", "🚦 Control de Gestión"],
        "color": "#dc2626"
    },
    "📦 Compras y Abastecimiento": {
        "titulo": "Compras y Abastecimiento",
        "rol": "Asegura la disponibilidad de insumos y productos en la cantidad y momento correctos.",
        "decisiones": [
            "Definir qué comprar, cuánto comprar y cuándo comprar.",
            "Seleccionar proveedores y coordinar reposición o importación.",
            "Balancear nivel de servicio con uso eficiente del capital."
        ],
        "conecta": ["📊 Dirección / Gerencia", "📈 Comercial / Ventas", "⚙️ Operaciones y Bodega", "💰 Finanzas", "🚦 Control de Gestión"],
        "color": "#a16207"
    },
    "⚙️ Operaciones y Bodega": {
        "titulo": "Operaciones y Bodega",
        "rol": "Administra el flujo físico del negocio: recepción, almacenamiento, control de stock y despacho.",
        "decisiones": [
            "Priorizar productos críticos y controlar quiebres o sobrestock.",
            "Validar movimientos de inventario, kardex y diferencias físicas.",
            "Coordinar ejecución operativa para cumplir la promesa comercial."
        ],
        "conecta": ["📊 Dirección / Gerencia", "📈 Comercial / Ventas", "📦 Compras y Abastecimiento", "💰 Finanzas", "🚦 Control de Gestión"],
        "color": "#0f766e"
    },
    "🚦 Control de Gestión": {
        "titulo": "Control de Gestión",
        "rol": "Monitorea desempeño, integra indicadores y convierte los datos del negocio en seguimiento gerencial.",
        "decisiones": [
            "Definir KPI y tableros de seguimiento.",
            "Detectar desvíos entre plan, operación y resultado.",
            "Escalar alertas y apoyar la mejora continua."
        ],
        "conecta": ["📊 Dirección / Gerencia", "💰 Finanzas", "📈 Comercial / Ventas", "📦 Compras y Abastecimiento", "⚙️ Operaciones y Bodega"],
        "color": "#7c3aed"
    },
}

AREAS_RESUMEN = {
    "🛒 Comercial": {
        "pasos": [
            "Levantar ventas, frecuencia y tipo de cliente.",
            "Segmentar la cartera según valor, recurrencia y potencial.",
            "Definir cobertura, propuestas y canal de atención.",
            "Asignar vendedores y medir resultados comerciales."
        ],
        "herramientas": ["Excel", "Tablas dinámicas", "Segmentación", "Indicadores comerciales", "IA", "Dashboards"]
    },
    "📦 Operaciones": {
        "pasos": [
            "Revisar stock, ventas históricas y productos sin movimiento.",
            "Clasificar SKU y detectar quiebres o sobrestock.",
            "Proyectar demanda y planificar compras/abastecimiento.",
            "Validar kardex, movimientos e inconsistencias operativas."
        ],
        "herramientas": ["Excel", "ABC", "Pareto", "Kardex", "Planificación de compras", "Control de inventario"]
    },
    "💰 Finanzas": {
        "pasos": [
            "Reunir diarios, costos, inventarios y movimientos contables.",
            "Validar calidad del dato y calcular costos reales.",
            "Construir estados financieros e indicadores clave.",
            "Interpretar resultados, riesgos y decisiones para la gerencia."
        ],
        "herramientas": ["Excel", "Balance 8 columnas", "EEFF", "Flujo de caja", "Indicadores", "Visualización"]
    }
}

def render_relational_graph(selected_area: str):
    node_lines = []
    for area, meta in MAPA_AREAS.items():
        selected = area == selected_area
        style = '"rounded,filled,bold"' if selected else '"rounded,filled"'
        fillcolor = meta['color'] if selected else '#f8fafc'
        fontcolor = 'white' if selected else '#1e293b'
        penwidth = '2.4' if selected else '1.1'
        node_lines.append(
            f'"{area}" [shape=box style={style} fillcolor="{fillcolor}" fontcolor="{fontcolor}" color="{meta["color"]}" penwidth={penwidth}];'
        )
    edge_lines = []
    for dest in MAPA_AREAS[selected_area]['conecta']:
        edge_lines.append(
            f'"{selected_area}" -> "{dest}" [color="{MAPA_AREAS[selected_area]["color"]}" penwidth=2.1 arrowsize=0.8];'
        )
    dot = "digraph G {\nrankdir=LR;\nnode [fontname=Helvetica fontsize=11 margin=0.18];\n" + "\n".join(node_lines + edge_lines) + "\n}"
    st.graphviz_chart(dot, use_container_width=True)


def render_step_block(area_key: str):
    resumen = AREAS_RESUMEN[area_key]
    st.markdown("### 🧭 Pasos resumidos para resolver la problemática")
    cols = st.columns([1.45, 1])
    with cols[0]:
        pasos_html = "".join([f"<li>{paso}</li>" for paso in resumen['pasos']])
        st.markdown(
            f"<div class='soft-card' style='min-height:220px;'><h4>Secuencia general de trabajo</h4><ol style='margin-top:.45rem; padding-left:1.15rem;'>{pasos_html}</ol></div>",
            unsafe_allow_html=True
        )
    with cols[1]:
        st.markdown("<div class='soft-card' style='min-height:220px;'><h4>🧰 Herramientas útiles</h4>", unsafe_allow_html=True)
        for h in resumen['herramientas']:
            concepto(h)
        st.markdown("</div>", unsafe_allow_html=True)

# BANNER PRINCIPAL CON DISEÑO SOBRIO
hero(
    "📊 Portafolio Interactivo Colectivo: Pensamiento Gerencial y Ciclo de la Empresa",
    "Una guía estratégica para comprender la organización como un sistema integrado, conectando sus áreas funcionales mediante la toma de decisiones basada en datos."
)

st.caption("Versión ejecutiva superior: analítica por macroáreas estratégicas, con mapas interactivos de procesos corporativos.")

# PESTAÑAS PRINCIPALES
tab1, tab2, tab3, tab4 = st.tabs([
    "🏢 Empresa y pensamiento gerencial",
    "📈 Madurez Estratégica por Áreas",
    "🔗 Flujo del pensamiento gerencial",
    "🧠 Reflexión final"
])

# ============================================================
# TAB 1: EMPRESA Y PENSAMIENTO GERENCIAL
# ============================================================
with tab1:
    st.header("1. El Motor Principal: Introducción general al concepto de empresa")

    st.markdown(
        """
        <div class="section-card">
        <b>Idea central:</b> Una empresa no es una estructura estática de tareas aisladas. 
        Es un <b>sistema vivo e integrado</b> compuesto por recursos, procesos y decisiones estratégicas orientadas a resolver una necesidad en el mercado y generar valor económico sostenible.
        </div>
        """,
        unsafe_allow_html=True
    )

    col_izq, col_der = st.columns([1.1, 1])

    with col_izq:
        st.subheader("🧬 ¿Qué es el Pensamiento Gerencial?")
        st.write(
            "Es la capacidad de desarrollar un **criterio analítico y crítico** para tomar decisiones defendibles bajo incertidumbre. "
            "Implica transicionar de un rol puramente operativo (ejecutar tareas aisladas) a un **rol estratégico** (comprender el impacto sistémico de la tarea en toda la organización)."
        )
        st.info(
            "💼 **La Sincronización Sistémica:** Tal como se aprecia en el mapa del ecosistema corporativo inferior, la firma es un conjunto de engranajes donde "
            "Finanzas, Operaciones (Compras y Bodega), Comercial y Control de Gestión interactúan de forma dependiente y coordinada."
        )
        

        # --- MAPA CONCEPTUAL INTERACTIVO CONSTRUIDO EN CÓDIGO ---
        st.markdown("### 🗺️ Mapa del Ecosistema Empresarial")
        st.caption("Seleccione un nodo del sistema para ver su rol principal, las decisiones que toma y sus conexiones con las demás áreas.")

        area_seleccionada = st.pills(
            "Selecciona un nodo corporativo:",
            list(MAPA_AREAS.keys()),
            selection_mode="single",
            default="📊 Dirección / Gerencia"
        )

        meta = MAPA_AREAS[area_seleccionada]
        st.markdown(
            f"<div class='mini-card' style='border-left: 6px solid {meta['color']}; background-color: #f8fafc; margin-bottom: .8rem;'><h4 style='margin-bottom:.45rem;'>{meta['titulo']}</h4><p><b>Rol principal:</b> {meta['rol']}</p></div>",
            unsafe_allow_html=True
        )

        c_map_1, c_map_2 = st.columns([1.05, 1])
        with c_map_1:
            st.markdown("#### 🔗 Relaciones del nodo")
            render_relational_graph(area_seleccionada)
        with c_map_2:
            st.markdown("#### 🧠 Decisiones que toma")
            for i, decision in enumerate(meta["decisiones"], start=1):
                st.markdown(
                    f"<div class='mini-card' style='min-height: 88px; border-left: 5px solid {meta['color']}; background-color: #ffffff;'><b>Decisión {i}</b><br>{decision}</div>",
                    unsafe_allow_html=True
                )

        st.markdown(f"**Áreas con las que se conecta directamente:** {', '.join(meta['conecta'])}")

    with col_der:
        st.subheader("⚙️ Funciones Básicas del Administrador")
        funciones = pd.DataFrame({
            "Función": ["Planificar", "Organizar", "Dirigir", "Controlar"],
            "Criterio Gerencial Aplicado": [
                "Definir objetivos de negocio, prever la demanda futura y diseñar planes de acción eficientes.",
                "Asignar recursos escasos, estructurar responsabilidades del personal y sincronizar departamentos.",
                "Comunicar visiones estratégicas, liderar basándose en evidencia empírica y coordinar equipos.",
                "Medir desviaciones mediante analítica visual, auditar costos y aplicar correcciones oportunas."
            ]
        })
        st.dataframe(funciones, use_container_width=True, hide_index=True)

    st.markdown("---")

    st.subheader("🎛️ Lentes del Criterio Profesional: Cambiar de enfoque para decidir mejor")
    st.write("Un directivo exitoso alterna dinámicamente sus marcos de pensamiento según las complejidades del escenario:")

    lente = st.radio(
        "Selecciona un lente gerencial para examinar su utilidad práctica:",
        ["⚙️ Enfoque Sistémico", "♟️ Enfoque Estratégico", "🔍 Enfoque Crítico"],
        horizontal=True
    )

    if "Sistémico" in lente:
        st.info("**Pensamiento sistémico:** Permite comprender las relaciones causa-efecto. Muestra que un error en el ingreso de bodega altera el costeo de importaciones, distorsiona los márgenes y vicia el Balance General final.")
    elif "Estratégico" in lente:
        st.info("**Pensamiento estratégico:** Centrado en la sostenibilidad del negocio a largo plazo. No solo soluciona la urgencia de hoy, sino que evalúa si las ofertas de hoy comprometen la liquidez o la capacidad física de mañana.")
    else:
        st.info("**Pensamiento crítico:** Desafía los datos preliminares. Obliga al equipo directivo a cuestionar anomalías operativas (como un 'costo negativo') antes de validar los precios de venta de la firma.")

    # ============================================================
    # SECCIÓN: LOS 4 CONCEPTOS CRÍTICOS DEL TALLER
    # ============================================================
    st.markdown("---")
    st.subheader("🚀 Pilares Estratégicos: Los 4 Conceptos Críticos del Taller")
    st.write("Los pilares fundamentales que transformaron nuestra teoría en una gestión directiva real:")

    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown(
            """
            <div class="mini-card" style="border-left: 5px solid #1e3a8a; min-height: 250px;">
                <h4>📦 1. El Inventario como Dinero Congelado</h4>
                <p><b>Lo importante:</b> Romper el mito de que <i>"mientras más stock tengamos, mejor"</i>. Aprendimos que tener cajas acumulando polvo en bodega es sinónimo de asfixia financiera.</p>
                <p style="font-size: 0.9rem; color: #1e3a8a;"><b>El criterio clave:</b> Al analizar la cobertura entendimos la trampa del promedio: para calcular el promedio de ventas se deben considerar los 6 meses completos del semestre, porque mantener el producto ahí costó dinero real todo ese tiempo. Con la clasificación ABC aprendimos a no perder tiempo: el foco del gerente debe estar en el 20% de los productos que pagan los sueldos (Clase A) y en liquidar los productos 'fantasmas' (Clase Z) que tienen venta $0.</p>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="mini-card" style="border-left: 5px solid #2563eb; min-height: 250px;">
                <h4>🛠️ 3. La Rigurosidad Operativa y los Errores Humanos</h4>
                <p><b>Lo importante:</b> Los sistemas informáticos (como un ERP) no son mágicos; dependen de la disciplina de las personas que ingresan los datos.</p>
                <p style="font-size: 0.9rem; color: #1e3a8a;"><b>El criterio clave:</b> Al auditar el Kardex valorizado enfrentamos el misterio de los 'costos negativos'. Comprendimos que la matemática no se equivoca, sino que refleja fallas de proceso humano: el equipo digitalizó las ventas antes de registrar formalmente la llegada del barco con las compras. Un CEO eficiente mapea estos desfases para reordenar los procesos del personal en la bodega.</p>
            </div>
            """, unsafe_allow_html=True
        )
    with cc2:
        st.markdown(
            """
            <div class="mini-card" style="border-left: 5px solid #3b82f6; min-height: 250px;">
                <h4>🔗 2. La Coherencia en la Planificación o "Efecto Pirámide"</h4>
                <p><b>Lo importante:</b> La empresa no puede ser un caos donde cada área opera de forma aislada. Comercial y Operaciones deben hablar exactamente el mismo idioma.</p>
                <p style="font-size: 0.9rem; color: #1e3a8a;"><b>El criterio clave:</b> En el forecasting descubrimos que no se puede proyectar la venta de un cable suelto sin mirar el panorama general: las proyecciones individuales por SKU deben sumar exactamente lo mismo que las metas corporativas de sus Familias y Subfamilias. Si esa pirámide no es coherente, Operaciones mandará a pedir barcos a Asia con mercadería que Comercial no planea vender.</p>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="mini-card" style="border-left: 5px solid #0284c7; min-height: 250px;">
                <h4>⚖️ 4. La Cuadratura Financiera y la Verdad de los Datos</h4>
                <p><b>Lo importante:</b> En los negocios, todo lo que entra tiene que salir; la contabilidad es exacta y transparente.</p>
                <p style="font-size: 0.9rem; color: #1e3a8a;"><b>El criterio clave:</b> La cuadratura total es el examen de control definitivo. Si el inventario inicial, más lo que se compró, menos lo que se vendió, no calza con el stock físico de la bodega, hay un problema crítico (mermas, robos o errores de digitación). El concepto central aquí es la trazabilidad: un buen administrador puede rastrear cada peso y cada tornillo desde que cruza la aduana hasta que llega al cliente final.</p>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("---")
    st.subheader("📊 Clasificación General del Tablero de Juego")
    st.write("Las empresas comerciales y del sector terciario centran su gestión en coordinar eficientemente los flujos financieros y de stock:")
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(label="🎯 Por Actividad", value="Sector Terciario / Comercial", delta="B2B / B2C / Importadoras")
        st.write("El foco absoluto radica en los clientes, las propuestas de valor y la velocidad de rotación física del producto.")
    with m2:
        st.metric(label="📏 Por Tamaño", value="Mediana Empresa (Pyme)", delta="Estructuras Flexibles")
        st.write("Exige liderazgos integrales capaces de conectar los datos de compras y ventas de forma directa sin burocracia.")
    with m3:
        st.metric(label="⚖️ Por Capital", value="Empresa Privada", delta="Maximización del Margen")
        st.write("Busca proteger la rentabilidad de los accionistas asegurando liquidez y controlando estrictamente las mermas.")

# ============================================================
# TAB 2: MATRIZ DE MADUREZ POR ÁREAS
# ============================================================
with tab2:
    st.header("🏢 2. El Escenario: Evolución por Áreas Estratégicas")

    st.markdown(
        """
        <div class="section-card">
        Para consolidar el progreso del semestre, organizamos la evolución del criterio directivo en 
        <b>tres grandes macroáreas corporativas</b>. Ninguna de estas áreas opera de forma aislada: 
        cada decisión comercial impacta los flujos logísticos y se valida finalmente en los estados financieros.
        </div>
        """,
        unsafe_allow_html=True
    )

    if "area_activa" not in st.session_state:
        st.session_state.area_activa = "🛒 Comercial"

    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        if st.button("📈 Área Comercial y Ventas", use_container_width=True): st.session_state.area_activa = "🛒 Comercial"
    with col_btn2:
        if st.button("📦 Área de Operaciones y Bodega", use_container_width=True): st.session_state.area_activa = "📦 Operaciones"
    with col_btn3:
        if st.button("💰 Área de Finanzas y Contabilidad", use_container_width=True): st.session_state.area_activa = "💰 Finanzas"

    st.markdown("---")

    # MACROÁREA 1: COMERCIAL
    if st.session_state.area_activa == "🛒 Comercial":
        st.subheader("📈 Área Comercial: Gestión Estratégica de Clientes y Oferta de Valor")
        
        c1, c2, c3 = st.columns(3)
        with c1: mini_card("Objetivo Primario", "Maximizar la contribución de la cartera diseñando ofertas a la medida del mercado.", "🎯")
        with c2: mini_card("Problema de Partida", "Equipos de venta desgastados por atender con el mismo esfuerzo a clientes masivos y cuentas clave.", "⚠️")
        with c3: mini_card("Ecosistema de Conceptos", "Clientes, Propuestas de Valor, Planificación y Segmentación.", "🔗")
        
        col_text1, col_text2 = st.columns(2)
        with col_text1:
            st.markdown("### 🔄 Evolución del Aprendizaje Gerencial")
            st.write("""
            Al inicio del ciclo, nuestra perspectiva comercial era lineal: empujar volumen de ventas a cualquier costo sin una estrategia clara. 
            A lo largo del proceso, comprendimos que una cartera comercial requiere una **planificación** analítica rigurosa. 
            
            Aprendimos a clasificar a los **clientes** según su valor y recurrencia, distinguiendo las lógicas de negociación relacional (B2B) frente a las dinámicas masivas (B2C). Formulamos **propuestas** comerciales competitivas y altamente personalizadas para optimizar la conversión de la fuerza de ventas.
            """)
        with col_text2:
            st.markdown("### 🛠️ Obstáculos Superados y Criterio Profesional")
            st.error("**El Quiebre Superado:** Aprender a no depender ciegamente de los algoritmos de la tecnología; entrenamos el criterio para auditar y estructurar cada entregable antes de presentarlo al mercado.")
            st.success("**Uso en la Empresa Real:** Nos faculta para diseñar planes de cobertura comercial eficientes, fijar comisiones basadas en **márgenes** reales y liderar equipos comerciales modernos utilizando herramientas de analítica y **visualización** corporativa.")

        render_step_block("🛒 Comercial")

    # MACROÁREA 2: OPERACIONES
    elif st.session_state.area_activa == "📦 Operaciones":
        st.subheader("📦 Área de Operaciones: Sincronización de Bodega, Logística y Abastecimiento")
        
        c1, c2, c3 = st.columns(3)
        with c1: mini_card("Objetivo Primario", "Garantizar la continuidad del negocio optimizando la rotación física del producto y mitigando mermas.", "🎯")
        with c2: mini_card("Problema de Partida", "Bodegas colapsadas con stock obsoleto conviviendo con quiebres críticos en los productos estrella.", "⚠️")
        with c3: mini_card("Ecosistema de Conceptos", "Inventario, Kardex Valorizado, Abastecimiento, Importaciones y Clasificación ABC.", "🔗")
        
        col_text1, col_text2 = st.columns(2)
        with col_text1:
            st.markdown("### 🔄 Evolución del Aprendizaje Gerencial")
            st.write("""
            Nuestra inmersión operativa comenzó concibiendo la bodega de forma intuitiva como un mero almacén estático. El análisis detallado del **Kardex** físico nos abrió los ojos para entender el verdadero impacto financiero del **inventario** inmovilizado.
            
            Con la técnica ABC de Pareto, aprendimos a priorizar los esfuerzos del personal en los SKU críticos para el negocio. La madurez del área se consolidó al enfrentar el proceso de **importaciones**, donde logramos conectar de forma lógica la travesía de traer contenedores desde el extranjero con un modelo de **abastecimiento** sincronizado con las proyecciones comerciales de la firma.
            """)
        with col_text2:
            st.markdown("### 🛠️ Obstáculos Superados y Criterio Profesional")
            st.error("**El Quiebre Superado:** Trabajar y limpiar bases de datos operativas reales que contenían inconsistencias, logrando balancear las presiones comerciales frente a las restricciones de espacio físico.")
            st.success("**Uso en la Empresa Real:** Diseñar políticas eficientes de compras internacionales y control de stock en firmas comerciales, protegiendo activamente el capital de trabajo de la organización.")

        render_step_block("📦 Operaciones")

    # MACROÁREA 3: FINANZAS
    elif st.session_state.area_activa == "💰 Finanzas":
        st.subheader("💰 Área de Finanzas y Contabilidad: Control de Gestión y Estructura Financiera")
        
        c1, c2, c3 = st.columns(3)
        with c1: mini_card("Objetivo Primario", "Traducir los hechos económicos operativos en información contable fidedigna para el gobierno corporativo.", "🎯")
        with c2: mini_card("Problema de Partida", "Inconsistencias contables y desfases en los ERP ('costos negativos') que invalidaban la toma de decisiones.", "⚠️")
        with c3: mini_card("Ecosistema de Conceptos", "Costos Reales, Sueldos, Cotizaciones, Márgenes y Estados Financieros.", "🔗")
        
        col_text1, col_text2 = st.columns(2)
        with col_text1:
            st.markdown("### 🔄 Evolución del Aprendizaje Gerencial")
            st.write("""
            En esta área descubrimos el verdadero lenguaje de los negocios. Comenzamos analizando **costos** básicos, pero avanzamos rápidamente a entender la complejidad de auditar planillas operativas, integrando el cálculo legal de **sueldos** junto con sus respectivas **cotizaciones** previsionales.
            
            Todo este ecosistema de información maduró de forma definitiva al consolidar los registros diarios en un Balance de Ocho Columnas y Estados Financieros completos. Esto nos permitió auditar los **márgenes** reales de contribución y utilizar técnicas avanzadas de **visualización** de **datos** para presentar la salud del negocio a nivel directivo.
            """)
        with col_text2:
            st.markdown("### 🛠️ Obstáculos Superados y Criterio Profesional")
            st.error("**El Quiebre Superado:** Superar el simple cuadre numérico tradicional de celdas; escalamos hacia una mentalidad directiva que interpreta indicadores de liquidez, rentabilidad y riesgo.")
            st.success("**Uso en la Empresa Real:** Nos faculta para estructurar presupuestos eficientes, auditar costos de internación reales y rendir cuentas transparentes ante un Directorio mediante tableros de control automatizados.")

        render_step_block("💰 Finanzas")

# ============================================================
# TAB 3: FLUJO DEL PENSAMIENTO GERENCIAL
# ============================================================
with tab3:
    st.header("3. Conectando los puntos: El flujo del pensamiento gerencial")

    st.write(
        "En la empresa real, los problemas no aparecen separados por capítulos independientes. "
        "Todo funciona como un efecto dominó: inventario, costos, clientes, planificación y contabilidad se conectan entre sí."
    )

    paso = st.select_slider(
        "Desliza para ver cómo avanza el ciclo de análisis estratégico:",
        options=[
            "Paso 1: Diagnóstico",
            "Paso 2: Foco",
            "Paso 3: Anticipar",
            "Paso 4: Traducción financiera"
        ]
    )

    st.markdown("---")

    if paso == "Paso 1: Diagnóstico":
        st.subheader("🔍 Paso 1: Diagnosticar la realidad física")
        st.write(
            "Antes de decidir, el gerente debe saber dónde está parado. Esto comienza en bodega: qué productos existen, cuánto rotan, cuánto cuestan y qué problemas presentan."
        )
        col1, col2 = st.columns(2)
        with col1:
            mini_card(
                "Inventario acumulado",
                "Cuando hay productos estancados, la empresa tiene capital inmovilizado. No es solo espacio ocupado: es dinero que no se convierte en ventas.",
                "📦"
            )
        with col2:
            mini_card(
                "Quiebre de stock",
                "Cuando falta un producto importante, ventas pierde oportunidades, el cliente se molesta y puede migrar a la competencia.",
                "⚠️"
            )
        with st.expander("Ver conceptos del diagnóstico operativo"):
            st.write("**Kardex:** Registro de entradas, salidas y saldos de inventario. Permite conocer rotación, disponibilidad y valorización.")
            st.write("**Costo real:** Costo que considera compras, importaciones, mermas, fletes, ajustes y errores de registro.")
            st.write("**Dato crítico:** Si el costo de bodega está mal calculado, cualquier utilidad futura será una ilusión poco confiable.")

    elif paso == "Paso 2: Foco":
        st.subheader("🎯 Paso 2: Priorizar productos y clientes")
        st.write(
            "Los recursos organizacionales son escasos: tiempo, vendedores, capital, espacio y capacidad de análisis. "
            "Por eso, el pensamiento gerencial exige decidir dónde enfocar con precisión los esfuerzos de la firma."
        )
        col1, col2 = st.columns(2)
        with col1:
            st.info("**📦 Productos:** No todos los SKU tienen la misma rentabilidad ni la misma rotación. La clasificación ABC ayuda a distinguir productos estratégicos de productos secundarios.")
            with st.expander("Detalle: Clasificación ABC"):
                st.write("- **Clase A:** Productos críticos, de alto valor o alta contribución. No pueden faltar en bodega.")
                st.write("- **Clase B:** Productos intermedios, de control normal y relevancia moderada.")
                st.write("- **Clase C / Sin Venta:** Productos de bajo impacto, candidatos a liquidación para liberar caja.")
        with col2:
            st.info("**🤝 Clientes:** No todos requieren el mismo tipo de atención comercial. La segmentación permite asignar eficientemente la fuerza de ventas.")
            with st.expander("Detalle: Lógicas B2B y B2C"):
                st.write("- **B2B (Corporativo):** Venta a empresas. Relación técnica, relacional, de largo plazo y con alta personalización.")
                st.write("- **B2C (Masivo):** Venta al consumidor final. Relación transaccional, rápida y gestionada por canales digitales.")

    elif paso == "Paso 3: Anticipar":
        st.subheader("🔮 Paso 3: Anticipar el futuro")
        st.write(
            "Cuando ya se conoce qué productos rotan, cuánto cuestan, cuáles son prioritarios y quiénes son los clientes relevantes, la empresa puede proyectar con bases sólidas."
        )
        st.success(
            "El puente definitivo entre ventas y operaciones se llama **planificación de compras**. Su objetivo es estimar unidades futuras para comprar con inteligencia: suficiente stock para vender, pero sin ahogar la caja."
        )
        with st.expander("Ver conceptos clave de planificación"):
            st.write("**Demanda esperada (Forecast):** Unidades que probablemente se venderán en un periodo futuro basándose en datos históricos.")
            st.write("**Abastecimiento:** Proceso de decidir qué comprar, cuánto comprar y cuándo comprar para cubrir la cadena de suministro.")
            st.write("**Riesgos Cruzados:** El sobrestock inmoviliza caja; el quiebre destruye la promesa comercial hacia el mercado.")

    else:
        st.subheader("⚖️ Paso 4: Traducir la operación a información financiera")
        st.write(
            "Todo el esfuerzo comercial y operativo termina reflejándose de forma transparente en la contabilidad gerencial. "
            "Las decisiones de compras, ventas, inventarios y sueldos se transforman en estados financieros consolidados."
        )
        col1, col2, col3 = st.columns(3)
        with col1: mini_card("Balance General", "Muestra los activos, pasivos y patrimonio. Permite auditar la posición de estabilidad financiera de la empresa.", "📘")
        with col2: mini_card("Estado de Resultados", "Muestra ingresos, costos y gastos. Permite saber con precisión si la empresa ganó o perdió en el ejercicio.", "📊")
        with col3: mini_card("Flujo de Efectivo", "Muestra las entradas y salidas reales de dinero, evaluando la liquidez inmediata para sobrevivir.", "💧")
        
        st.warning(
            "La pregunta ejecutiva final es: ¿Ganamos o perdimos dinero?, ¿Tenemos liquidez para responder compromisos?, ¿Cuáles son los riesgos estratégicos y qué decisiones debe tomar la Alta Gerencia?"
        )

    st.markdown("---")
    st.markdown(
        """
        <div class="section-card">
        💡 <b>Criterio Directivo:</b> Los libros de cálculo, las fórmulas y la Inteligencia Artificial pueden entregar datos procesados, 
        pero ninguna herramienta toma decisiones de dirección por sí sola. Las compañías las lideran profesionales con criterio integral, 
        capaces de defender sus decisiones considerando contexto, mitigación de riesgos y realidad económica.
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# TAB 4: REFLEXIÓN FINAL (SIMULADOR EJECUTIVO DE CASOS CRÍTICOS)
# ============================================================
with tab4:
    st.header("4. Reflexión ejecutiva e integración de aprendizajes")
    st.write(
        "Seleccione un escenario organizativo de alta complejidad para evaluar cómo el análisis y el criterio resuelven las desviaciones del negocio:"
    )

    opcion = st.selectbox(
        "Elige un escenario corporativo crítico para auditar con criterio directivo:",
        [
            "🔹 Escenario A: La bodega está colapsada, pero Comercial reclama quiebres de stock continuos.",
            "🔹 Escenario B: Las planillas de costos muestran descalces y hay sospechas de pérdidas en el margen.",
            "🔹 Escenario C: El Directorio exige sustentar el plan de expansión estratégica basado en la salud del negocio."
        ]
    )

    st.markdown("---")

    if "Escenario A" in opcion:
        st.subheader("📦 Diagnóstico de Operaciones: Sincronización Comercial-Abastecimiento")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("""
            ### 🧠 ¿Qué aprendimos?
            Que el inventario inmovilizado destruye la caja. El uso del **Kardex** y la clasificación ABC permite segmentar el catálogo de productos y estructurar una **planificación** científica de compras basada en la rotación real.
            """)
        with col2:
            st.success("""
            ### 💎 ¿Qué valor tuvo?
            Nos enseñó a no operar por intuición. Comprendimos que los desbalances operativos se solucionan creando un puente de **datos** integrados entre las áreas de compras y ventas corporativas.
            """)
        with col3:
            st.warning("""
            ### 🔮 ¿Cómo usarlo en el futuro?
            Estableciendo políticas automáticas de reaprovisionamiento y stock de seguridad, liderando comités mensuales de **abastecimiento** para evitar quiebres y sobrestocks que dañen la liquidez de la firma.
            """)

    elif "Escenario B" in opcion:
        st.subheader("💰 Diagnóstico Financiero: Auditoría de Costos Reales y Remuneraciones")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("""
            ### 🧠 ¿Qué aprendimos?
            A construir el costo real integrando de forma rigurosa los fletes de **importaciones**, mermas de bodega y la carga financiera fija del personal (cálculo de **sueldos** y sus respectivas **cotizaciones** previsionales).
            """)
        with col2:
            st.success("""
            ### 💎 ¿Qué valor tuvo?
            Desarrollar un ojo clínico y un pensamiento crítico: si la base contable arrastra errores o ignora leyes sociales, los **márgenes** calculados serán ficticios y las utilidades reportadas una mera ilusión contable.
            """)
        with col3:
            st.warning("""
            ### 🔮 ¿Cómo usarlo en el futuro?
            Nos capacita para visar las matrices de precios de productos importados, controlar presupuestos corporativos eficientes y tomar decisiones basadas en **costos reales** auditados, protegiendo la rentabilidad de la firma.
            """)

    else:
        st.subheader("⚖️ Diagnóstico de Dirección: Consolidación Financiera y Visualización")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("""
            ### 🧠 ¿Qué aprendimos?
            A sintetizar transacciones de libros contables en Estados Financieros y a formular **propuestas** comerciales competitivas y segmentar mercados.
            """)
        with col2:
            st.success("""
            ### 💎 ¿Qué valor tuvo?
            Comprender el poder de la **visualización** avanzada para traducir grandes volúmenes de datos áridos en un tablero ejecutivo claro, permitiendo evaluar la salud de todo el negocio en un solo segundo.
            """)
        with col3:
            st.warning("""
            ### 🔮 ¿Cómo usarlo en el futuro?
            Presentando informes interactivos de control de gestión ante directorios o inversionistas, defendiendo decisiones estratégicas con argumentos financieros sólidos y evaluando riesgos de forma cuantitativa.
            """)

    st.markdown("---")

    st.markdown(
        """
        <div class="section-card">
        <h3>🤝 Conclusión Consolidada de la Dupla Gerencial</h3>
        <p>
        A lo largo de este trayecto académico comprendimos que <b>las empresas son sistemas vivos, dinámicos e interconectados</b>. 
        El verdadero valor del curso no radicó únicamente en dominar softwares o planillas, sino en forjar nuestro <b>criterio gerencial</b>. 
        Las herramientas digitales proveen los datos, pero corresponde a los líderes transformar esa analítica en decisiones estratégicas defendibles. 
        </p>
        <p><b>Nos despedimos del ciclo con el mapa de control integral de la organización en mente: desde el movimiento primario en la bodega hasta el veredicto definitivo de los Estados Financieros corporativos.</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.text_area(
        "✍️ Espacio para comentarios o notas del profesor evaluador:",
        "Excelente integración de conceptos y madurez en el análisis cuantitativo por macroáreas estratégicas."
    )
