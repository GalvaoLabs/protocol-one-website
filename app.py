import streamlit as st

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Protocol One — ProtoCommunity",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    /* ========================================================
       PALETA
       ======================================================== */

    :root {
        --paper: #F7F6F2;
        --paper-soft: #EEECE5;
        --paper-card: #FFFFFF;

        --ink: #18272C;
        --ink-soft: #59676C;
        --ink-faint: #879297;

        --navy: #173F4A;
        --navy-deep: #102F38;

        --teal: #39757A;
        --teal-dark: #285B61;
        --teal-soft: #DCEBEC;

        --gold: #C6A263;
        --gold-soft: #EFE4CF;

        --line: rgba(24, 39, 44, 0.12);
        --line-strong: rgba(24, 39, 44, 0.24);

        --shadow: 0 10px 30px rgba(16, 47, 56, 0.07);
        --shadow-hover: 0 14px 34px rgba(16, 47, 56, 0.11);
    }

    /* ========================================================
       BASE
       ======================================================== */

    *,
    *::before,
    *::after {
        box-sizing: border-box;
    }

    html,
    body {
        width: 100%;
        max-width: 100%;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    body {
        background: var(--paper);
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] > .main,
    .main {
        background: var(--paper);
    }

    .block-container {
        width: 100%;
        max-width: 1280px;
        padding-top: 2rem;
        padding-bottom: 4rem;
        padding-left: clamp(1rem, 4vw, 3rem);
        padding-right: clamp(1rem, 4vw, 3rem);
        overflow-x: hidden;
    }

    html,
    body,
    [class*="css"] {
        font-family: "Space Grotesk", sans-serif;
        color: var(--ink);
    }

    h1,
    h2,
    h3,
    h4 {
        font-family: "Big Shoulders Display", sans-serif !important;
        color: var(--ink) !important;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }

    p {
        color: var(--ink-soft);
    }

    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                var(--navy-deep) 0%,
                #143841 100%
            );
        border-right: 1px solid rgba(255, 255, 255, 0.07);
    }

    section[data-testid="stSidebar"] * {
        color: #F4F7F5 !important;
    }

    .sidebar-logo {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 38px;
        line-height: 0.88;
        font-weight: 800;
        letter-spacing: 0.04em;
        color: #FFFFFF;
        margin-bottom: 0.3rem;
    }

    .sidebar-subtitle {
        color: #AFC7CA !important;
        font-size: 12px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 2rem;
    }

    .sidebar-label {
        color: #8FAEB2 !important;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin: 1.5rem 0 0.65rem;
    }

    .sidebar-email {
        color: #C9D7D9 !important;
        font-size: 12px;
        line-height: 1.5;
        overflow-wrap: anywhere;
        word-break: break-word;
    }

    /* ========================================================
       TÍTULOS
       ======================================================== */

    .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: var(--teal);
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-bottom: 0.9rem;
    }

    .eyebrow::before {
        content: "";
        width: 24px;
        height: 2px;
        background: var(--gold);
        display: inline-block;
        flex-shrink: 0;
    }

    .hero-title {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 68px;
        line-height: 0.92;
        font-weight: 700;
        letter-spacing: -0.015em;
        text-transform: uppercase;
        color: var(--ink);
        max-width: 920px;
        margin-bottom: 1.25rem;
        overflow-wrap: anywhere;
    }

    .section-title-lg {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 50px;
        line-height: 0.95;
        font-weight: 700;
        text-transform: uppercase;
        color: var(--ink);
        margin-bottom: 1rem;
        overflow-wrap: anywhere;
    }

    .section-title {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 36px;
        line-height: 1;
        font-weight: 700;
        text-transform: uppercase;
        color: var(--ink);
        margin-bottom: 0.8rem;
        overflow-wrap: anywhere;
    }

    .lead {
        font-size: 19px;
        line-height: 1.65;
        max-width: 850px;
        color: var(--ink-soft);
    }

    .body-copy {
        font-size: 16px;
        line-height: 1.7;
        color: var(--ink-soft);
    }

    .frame-tab {
        display: inline-block;
        max-width: 100%;
        padding: 7px 11px;
        margin-bottom: 1rem;
        border: 1px solid var(--line-strong);
        border-radius: 4px;
        color: var(--teal);
        background: rgba(255, 255, 255, 0.55);
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.13em;
        text-transform: uppercase;
        overflow-wrap: anywhere;
    }

    .accent-line {
        width: 72px;
        height: 4px;
        background: var(--gold);
        margin: 1.5rem 0 2rem;
    }

    .rule {
        height: 1px;
        width: 100%;
        background: var(--line);
        margin: 3rem 0;
    }

    /* ========================================================
       GRIDS
       ======================================================== */

    .grid-4,
    .grid-3,
    .grid-2 {
        display: grid;
        width: 100%;
        gap: 14px;
        min-width: 0;
    }

    .grid-4 {
        grid-template-columns: repeat(4, minmax(0, 1fr));
    }

    .grid-3 {
        grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    .grid-2 {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    /* ========================================================
       CARDS
       ======================================================== */

    .cell,
    .card,
    .obj-card,
    .join-card,
    .film-cell,
    .stat {
        min-width: 0;
        overflow-wrap: anywhere;
        word-break: normal;
    }

    .cell {
        min-height: 180px;
        padding: 20px;
        border: 1px solid var(--line);
        background: rgba(255, 255, 255, 0.62);
        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }

    .cell:hover {
        transform: translateY(-2px);
        border-color: rgba(57, 117, 122, 0.35);
        box-shadow: var(--shadow);
    }

    .cell-number {
        color: var(--gold);
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.1em;
        margin-bottom: 2rem;
    }

    .cell-title {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 23px;
        line-height: 1;
        font-weight: 700;
        text-transform: uppercase;
        color: var(--ink);
        margin-bottom: 0.65rem;
    }

    .cell-text {
        color: var(--ink-soft);
        font-size: 13px;
        line-height: 1.55;
    }

    .card {
        min-height: 190px;
        padding: 22px;
        border: 1px solid var(--line);
        background: var(--paper-card);
        box-shadow: var(--shadow);
        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-hover);
    }

    .card h3 {
        margin: 0 0 0.75rem;
        font-size: 25px;
    }

    .card p {
        margin: 0;
        font-size: 13px;
        line-height: 1.6;
    }

    /* ========================================================
       CHIPS / BADGES
       ======================================================== */

    .chip-row,
    .role-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 1rem;
        min-width: 0;
    }

    .chip,
    .pill,
    .badge {
        max-width: 100%;
        overflow-wrap: anywhere;
        word-break: normal;
    }

    .chip {
        display: inline-block;
        padding: 8px 11px;
        border: 1px solid var(--line);
        border-radius: 999px;
        background: var(--paper-card);
        color: var(--ink-soft);
        font-size: 12px;
        line-height: 1.25;
    }

    .chip:hover {
        border-color: rgba(57, 117, 122, 0.3);
    }

    .badge {
        display: inline-block;
        padding: 6px 9px;
        border-radius: 4px;
        background: var(--teal-soft);
        border: 1px solid rgba(57, 117, 122, 0.18);
        color: var(--teal);
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.07em;
    }

    .pill {
        display: inline-block;
        padding: 7px 10px;
        border: 1px solid var(--line);
        background: var(--paper-card);
        color: var(--ink-soft);
        border-radius: 999px;
        font-size: 11px;
    }

    /* ========================================================
       OBJETIVOS
       ======================================================== */

    .obj-card {
        padding: 25px;
        min-height: 210px;
        background:
            linear-gradient(
                145deg,
                var(--navy) 0%,
                var(--teal-dark) 100%
            );
        border: 1px solid rgba(255, 255, 255, 0.04);
        color: white;
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow);
    }

    .obj-card::after {
        content: "";
        position: absolute;
        width: 100px;
        height: 100px;
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 50%;
        right: -34px;
        bottom: -40px;
    }

    .obj-number {
        color: var(--gold);
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.1em;
        margin-bottom: 2rem;
    }

    .obj-title {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 25px;
        line-height: 1;
        text-transform: uppercase;
        color: #FFFFFF;
        margin-bottom: 0.8rem;
    }

    .obj-text {
        color: #DCE7E8;
        font-size: 13px;
        line-height: 1.6;
    }

    /* ========================================================
       PIPELINE
       ======================================================== */

    .filmstrip {
        display: grid;
        grid-template-columns: repeat(7, minmax(0, 1fr));
        gap: 8px;
        width: 100%;
    }

    .film-cell {
        min-height: 190px;
        padding: 17px;
        background: var(--paper-card);
        border: 1px solid var(--line);
        position: relative;
        box-shadow: 0 4px 15px rgba(16, 47, 56, 0.025);
    }

    .film-cell::before {
        content: "";
        display: block;
        width: 100%;
        height: 5px;
        background: var(--gold-soft);
        margin-bottom: 20px;
    }

    .film-number {
        font-size: 10px;
        color: var(--teal);
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-bottom: 1.3rem;
    }

    .film-title {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 21px;
        line-height: 1;
        text-transform: uppercase;
        color: var(--ink);
        margin-bottom: 0.7rem;
    }

    .film-text {
        font-size: 12px;
        line-height: 1.5;
        color: var(--ink-soft);
    }

    /* ========================================================
       ESTATÍSTICAS
       ======================================================== */

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 10px;
        margin-top: 2.2rem;
        width: 100%;
    }

    .stat {
        padding: 19px;
        border-top: 2px solid var(--teal);
        background: rgba(255, 255, 255, 0.62);
    }

    .stat-value {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 38px;
        line-height: 0.9;
        font-weight: 700;
        color: var(--navy);
        margin-bottom: 0.7rem;
    }

    .stat-label {
        color: var(--ink-soft);
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        line-height: 1.4;
    }

    /* ========================================================
       PARTICIPE
       ======================================================== */

    .join-card {
        padding: 28px;
        min-height: 215px;
        border: 1px solid var(--line);
        background: var(--paper-card);
        box-shadow: var(--shadow);
        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .join-card:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-hover);
    }

    .join-symbol {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 40px;
        color: var(--gold);
        line-height: 1;
        margin-bottom: 1.2rem;
    }

    .join-title {
        font-family: "Big Shoulders Display", sans-serif;
        font-size: 29px;
        font-weight: 700;
        text-transform: uppercase;
        color: var(--ink);
        margin-bottom: 0.7rem;
    }

    .join-text {
        font-size: 13px;
        line-height: 1.65;
        color: var(--ink-soft);
    }

    /* ========================================================
       LINKS
       ======================================================== */

    .channel-btn {
        display: inline-block;
        max-width: 100%;
        margin: 4px 5px 4px 0;
        padding: 11px 15px;
        border: 1px solid var(--line-strong);
        border-radius: 4px;
        background: var(--paper-card);
        color: var(--navy) !important;
        text-decoration: none !important;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.04em;
        transition:
            background 0.2s ease,
            color 0.2s ease,
            border-color 0.2s ease;
        overflow-wrap: anywhere;
        word-break: break-word;
    }

    .channel-btn:hover {
        background: var(--navy);
        color: #FFFFFF !important;
        border-color: var(--navy);
    }

    .contact-box {
        padding: 20px;
        border: 1px solid var(--line);
        background: rgba(255, 255, 255, 0.55);
        margin-top: 1.2rem;
    }

    .contact-label {
        color: var(--teal);
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.13em;
        text-transform: uppercase;
        margin-bottom: 0.45rem;
    }

    .contact-email {
        color: var(--ink);
        font-size: 15px;
        font-weight: 600;
        overflow-wrap: anywhere;
        word-break: break-word;
    }

    /* ========================================================
       STREAMLIT
       ======================================================== */

    [data-testid="stHorizontalBlock"],
    [data-testid="stMarkdownContainer"] {
        min-width: 0;
        max-width: 100%;
    }

    /* ========================================================
       TABLET
       ======================================================== */

    @media (max-width: 1100px) {

        .grid-4 {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }

        .filmstrip {
            grid-template-columns: repeat(4, minmax(0, 1fr));
        }

        .stats-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }

    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 700px) {

        .block-container {
            padding-top: 1.25rem;
            padding-bottom: 2.5rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-title {
            font-size: 43px;
            line-height: 0.94;
            max-width: 100%;
        }

        .section-title-lg {
            font-size: 36px;
            line-height: 0.96;
        }

        .section-title {
            font-size: 29px;
            line-height: 1;
        }

        .lead {
            font-size: 16px;
            line-height: 1.6;
        }

        .body-copy {
            font-size: 14px;
            line-height: 1.65;
        }

        .grid-4,
        .grid-3,
        .grid-2 {
            grid-template-columns: 1fr;
        }

        .stats-grid {
            grid-template-columns: 1fr 1fr;
        }

        .filmstrip {
            grid-template-columns: 1fr;
        }

        .film-cell,
        .cell,
        .card,
        .obj-card,
        .join-card {
            min-height: auto;
        }

        .cell-number,
        .obj-number {
            margin-bottom: 1.2rem;
        }

        [data-testid="stHorizontalBlock"] {
            flex-direction: column !important;
            gap: 1rem !important;
        }

        .channel-btn {
            display: block;
            width: 100%;
            margin: 7px 0;
            text-align: center;
        }

        .rule {
            margin: 2.2rem 0;
        }
    }

    /* ========================================================
       MOBILE PEQUENO
       ======================================================== */

    @media (max-width: 430px) {

        .block-container {
            padding-left: 0.85rem;
            padding-right: 0.85rem;
        }

        .hero-title {
            font-size: 37px;
        }

        .section-title-lg {
            font-size: 32px;
        }

        .section-title {
            font-size: 27px;
        }

        .lead {
            font-size: 15px;
        }

        .stats-grid {
            grid-template-columns: 1fr;
        }

        .stat-value {
            font-size: 34px;
        }

        .frame-tab {
            font-size: 9px;
            padding: 6px 8px;
            letter-spacing: 0.1em;
        }

        .cell,
        .card,
        .obj-card,
        .join-card,
        .film-cell {
            padding: 18px;
        }

        .cell-title {
            font-size: 21px;
        }

        .obj-title {
            font-size: 23px;
        }

        .film-title {
            font-size: 20px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# DADOS
# ============================================================

NUCLEOS = [
    (
        "01",
        "Administração e Diretoria",
        "Visão institucional, estratégia e coordenação geral de todas as áreas.",
    ),
    (
        "02",
        "Conselho",
        "Fiscalização e deliberação colegiada sobre mudanças estruturais.",
    ),
    (
        "03",
        "Jurídico e Propriedade Intelectual",
        "Proteção legal da obra, dos personagens e da própria organização.",
    ),
    (
        "04",
        "Financeiro e Administrativo",
        "Recursos, orçamento e prestação de contas transparente.",
    ),
    (
        "05",
        "Gestão de Pessoas",
        "Recrutamento, integração, desenvolvimento e mediação de conflitos.",
    ),
    (
        "06",
        "Pré-produção",
        "Roteiro, universo, personagens, cenários e storyboard.",
    ),
    (
        "07",
        "Arte, Animação e Pós-produção",
        "Concept art, ilustração, animação, edição, dublagem e som.",
    ),
    (
        "08",
        "Marketing e Comunidade",
        "Redes sociais, parcerias, sugestões e relacionamento com o público.",
    ),
]

LIDERANCA = [
    (
        "Direção Executiva",
        [
            "Direção-Geral",
            "Direção de Produção",
        ],
    ),
    (
        "Núcleo Criativo",
        [
            "Direção Criativa",
            "Direção de Personagens",
            "Direção de Dublagem",
        ],
    ),
    (
        "Arte e Produção Técnica",
        [
            "Direção de Arte",
            "Direção de Animação",
            "Direção de Pós-Produção",
        ],
    ),
    (
        "Gestão, Marketing e Governança",
        [
            "Direção de Marketing",
            "Direção Financeira",
            "Direção Jurídica",
        ],
    ),
]

OBJETIVOS = [
    (
        "01",
        "Conteúdo de alta qualidade",
        "Animações, HQs e produções audiovisuais que se destacam pelo cuidado criativo e técnico.",
    ),
    (
        "02",
        "Comunidade escalável",
        "Processos profissionais e colaborativos que crescem junto com a organização.",
    ),
    (
        "03",
        "Parcerias e alcance",
        "Parcerias estratégicas e expansão consistente da presença nas redes sociais.",
    ),
    (
        "04",
        "Formação de talentos",
        "Oportunidades reais de desenvolvimento profissional dentro de universos ficcionais memoráveis.",
    ),
]

PIPELINE = [
    (
        "01",
        "Ideia e conceito",
        "Direção Criativa propõe; Diretoria aprova o conceito.",
    ),
    (
        "02",
        "Roteiro",
        "Roteirista-Chefe escreve; Direção Criativa aprova.",
    ),
    (
        "03",
        "Storyboard",
        "Transforma o roteiro em sequência visual de planos.",
    ),
    (
        "04",
        "Animatic",
        "Valida timing e ritmo antes da animação completa.",
    ),
    (
        "05",
        "Animação e som",
        "Cenas animadas, dublagem final e design de som.",
    ),
    (
        "06",
        "Controle de qualidade",
        "Revisão final antes de qualquer publicação.",
    ),
    (
        "07",
        "Publicação",
        "Marketing divulga somente o que passou pelo controle de qualidade.",
    ),
]

FRENTES = [
    "Animação",
    "Histórias em quadrinhos",
    "Produção audiovisual",
    "Criação de personagens",
    "Construção de universos",
    "Edição de vídeo",
    "Dublagem",
    "Design de som",
    "Ilustração",
    "Conteúdo para redes sociais",
    "Marketing",
    "Parcerias externas",
]

CANAIS = {
    "YouTube": "https://youtube.com/@protocoloneoficial?si=n9Iz6yuJhs3W5KgM",
    "Instagram": "https://www.instagram.com/protocoloneofc?igsh=MWRjOWs1bmx3amx5cg==",
    "TikTok": "https://www.tiktok.com/@protocoloneoficial?_r=1&_t=ZS-99IfbZKurp4",
}

EMAIL_CONTATO = "protocolonecontato@gmail.com"

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-logo">PROTOCOL<br>ONE</div>
        <div class="sidebar-subtitle">ProtoCommunity</div>
        """,
        unsafe_allow_html=True,
    )

    pagina = st.radio(
        "NAVEGAÇÃO",
        [
            "O Projeto",
            "Estrutura",
            "Objetivos",
            "Participe",
        ],
    )

    st.markdown(
        '<div class="sidebar-label">Canais oficiais</div>',
        unsafe_allow_html=True,
    )

    for nome, url in CANAIS.items():
        st.markdown(
            f"""
            <a
                class="channel-btn"
                href="{url}"
                target="_blank"
                rel="noopener noreferrer"
            >
                {nome}
            </a>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="sidebar-label">Contato</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="sidebar-email">{EMAIL_CONTATO}</div>',
        unsafe_allow_html=True,
    )

# ============================================================
# PÁGINA — O PROJETO
# ============================================================

if pagina == "O Projeto":

    st.markdown(
        '<div class="frame-tab">Quadro 00 — Abertura</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="eyebrow">Protocol One / ProtoCommunity</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="hero-title">Uma comunidade com disciplina de estúdio.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="lead">
            O Protocol One é uma organização criativa voltada à construção
            de universos, personagens e produções audiovisuais, combinando
            criatividade, processos profissionais e desenvolvimento de talentos.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="accent-line"></div>',
        unsafe_allow_html=True,
    )

    STATS = [
        ("08", "Núcleos organizacionais"),
        ("6+", "Frentes criativas"),
        ("03", "Canais oficiais"),
        ("07", "Etapas do pipeline"),
    ]

    stats_html = '<div class="stats-grid">'

    for valor, label in STATS:
        stats_html += f"""
        <div class="stat">
            <div class="stat-value">{valor}</div>
            <div class="stat-label">{label}</div>
        </div>
        """

    stats_html += "</div>"

    st.markdown(
        stats_html,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="rule"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="frame-tab">Quadro 01 — O que é</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title-lg">O que é a ProtoCommunity</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="body-copy">
                A ProtoCommunity funciona como uma estrutura colaborativa
                para transformar ideias em projetos criativos concretos.
                A proposta une diferentes especialidades em torno de um
                mesmo universo institucional.
            </div>

            <br>

            <div class="body-copy">
                O objetivo é criar um ambiente onde produção artística,
                gestão, tecnologia, comunicação e estratégia possam trabalhar
                de maneira integrada.
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        chips_html = '<div class="chip-row">'

        for frente in FRENTES:
            chips_html += f'<span class="chip">{frente}</span>'

        chips_html += "</div>"

        st.markdown(
            chips_html,
            unsafe_allow_html=True,
        )

# ============================================================
# PÁGINA — ESTRUTURA
# ============================================================

elif pagina == "Estrutura":

    st.markdown(
        '<div class="frame-tab">Quadro 02 — Estrutura</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title-lg">Oito núcleos. Um só rumo.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="lead">
            A organização distribui suas responsabilidades em núcleos
            especializados, permitindo que cada área tenha uma função clara
            dentro do funcionamento geral do projeto.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="height:24px;"></div>',
        unsafe_allow_html=True,
    )

    nucleos_html = '<div class="grid-4">'

    for numero, titulo, descricao in NUCLEOS:

        nucleos_html += f"""
        <div class="cell">
            <div class="cell-number">{numero}</div>
            <div class="cell-title">{titulo}</div>
            <div class="cell-text">{descricao}</div>
        </div>
        """

    nucleos_html += "</div>"

    st.markdown(
        nucleos_html,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="rule"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Estrutura de Liderança</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="body-copy">
            A liderança é organizada por frentes de responsabilidade,
            conectando direção estratégica, produção criativa, gestão,
            marketing e governança.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="height:18px;"></div>',
        unsafe_allow_html=True,
    )

    lideranca_html = '<div class="grid-4">'

    for titulo, cargos in LIDERANCA:

        lideranca_html += f"""
        <div class="card">
            <h3>{titulo}</h3>
            <div class="role-row">
        """

        for cargo in cargos:
            lideranca_html += f'<span class="badge">{cargo}</span>'

        lideranca_html += """
            </div>
        </div>
        """

    lideranca_html += "</div>"

    st.markdown(
        lideranca_html,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="rule"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Conselho Consultivo e Deliberativo</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="body-copy">
            O Conselho atua como órgão colegiado de fiscalização,
            governança e deliberação sobre questões estruturais da
            organização, preservando coerência e transparência institucional.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="chip-row">
            <span class="pill">Governança</span>
            <span class="pill">Fiscalização</span>
            <span class="pill">Direcionamento estratégico</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="height:18px;"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="grid-3">

            <div class="cell">
                <div class="cell-title">Fiscalização</div>
                <div class="cell-text">
                    Delibera sobre questões estruturais e operacionais
                    da organização.
                </div>
            </div>

            <div class="cell">
                <div class="cell-title">Governança</div>
                <div class="cell-text">
                    Decide mudanças na estrutura e no direcionamento
                    estratégico.
                </div>
            </div>

            <div class="cell">
                <div class="cell-title">Transparência</div>
                <div class="cell-text">
                    Mantém o alinhamento ético e a cultura institucional vivos.
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# PÁGINA — OBJETIVOS
# ============================================================

elif pagina == "Objetivos":

    st.markdown(
        '<div class="frame-tab">Quadro 03 — Objetivos</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title-lg">O que queremos construir.</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="lead">
            O Protocol One busca estabelecer uma estrutura sustentável,
            criativa e profissional, capaz de transformar produção
            independente em projetos de longo prazo.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="height:24px;"></div>',
        unsafe_allow_html=True,
    )

    objetivos_html = '<div class="grid-4">'

    for numero, titulo, descricao in OBJETIVOS:

        objetivos_html += f"""
        <div class="obj-card">
            <div class="obj-number">{numero}</div>
            <div class="obj-title">{titulo}</div>
            <div class="obj-text">{descricao}</div>
        </div>
        """

    objetivos_html += "</div>"

    st.markdown(
        objetivos_html,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="rule"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Como uma ideia vira entrega</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="body-copy">
            O pipeline organiza o caminho entre conceito e publicação,
            reduzindo retrabalho e garantindo que cada produção passe
            pelas etapas necessárias antes de chegar ao público.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="height:18px;"></div>',
        unsafe_allow_html=True,
    )

    pipeline_html = '<div class="filmstrip">'

    for numero, titulo, descricao in PIPELINE:

        pipeline_html += f"""
        <div class="film-cell">
            <div class="film-number">{numero}</div>
            <div class="film-title">{titulo}</div>
            <div class="film-text">{descricao}</div>
        </div>
        """

    pipeline_html += "</div>"

    st.markdown(
        pipeline_html,
        unsafe_allow_html=True,
    )

# ============================================================
# PÁGINA — PARTICIPE
# ============================================================

elif pagina == "Participe":

    st.markdown(
        '<div class="frame-tab">Quadro 04 — Participe</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title-lg">Faça parte da ProtoCommunity</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="lead">
            O projeto foi pensado para reunir pessoas interessadas em criar,
            aprender e construir algo maior por meio de colaboração organizada.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="height:24px;"></div>',
        unsafe_allow_html=True,
    )

    participar_html = """
    <div class="grid-3">

        <div class="join-card">
            <div class="join-symbol">◈</div>
            <div class="join-title">Crie</div>
            <div class="join-text">
                Contribua para projetos de animação, HQs e audiovisual
                de impacto real, dentro de um pipeline profissional.
            </div>
        </div>

        <div class="join-card">
            <div class="join-symbol">◈</div>
            <div class="join-title">Cresça</div>
            <div class="join-text">
                Desenvolva suas habilidades em um ambiente prático
                e colaborativo, trocando conhecimento com outros criativos.
            </div>
        </div>

        <div class="join-card">
            <div class="join-symbol">◈</div>
            <div class="join-title">Conecte-se</div>
            <div class="join-text">
                Faça parte de uma organização focada na construção
                de universos e fortalecimento de comunidade.
            </div>
        </div>

    </div>
    """

    st.markdown(
        participar_html,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="rule"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Canais oficiais</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="body-copy">
            Acompanhe o desenvolvimento do Protocol One e conheça
            os próximos projetos, produções e iniciativas da comunidade.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="height:12px;"></div>',
        unsafe_allow_html=True,
    )

    canais_html = ""

    for nome, url in CANAIS.items():

        canais_html += f"""
        <a
            class="channel-btn"
            href="{url}"
            target="_blank"
            rel="noopener noreferrer"
        >
            {nome}
        </a>
        """

    st.markdown(
        canais_html,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="contact-box">

            <div class="contact-label">
                Contato institucional
            </div>

            <div class="contact-email">
                protocolonecontato@gmail.com
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="height:10px;"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="body-copy">
            Criadores, parceiros, imprensa e apoiadores interessados
            podem entrar em contato diretamente pelo canal institucional.
        </div>
        """,
        unsafe_allow_html=True,
    )
