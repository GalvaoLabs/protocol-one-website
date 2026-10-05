"""
Protocol One — ProtoCommunity
Site de apresentação institucional, construído em Streamlit (Python puro).

Para rodar localmente:

    pip install -r requirements.txt
    streamlit run app.py

Para hospedar de graça, veja o README.md (Streamlit Community Cloud).
"""

import streamlit as st


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Protocol One — ProtoCommunity",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# ESTILO
# Identidade visual:
# papel kraft + tinta escura + verde-pinho + vermelho de carimbo
# ============================================================

CSS = """
<style>

@import url(
    'https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@500;600;700;800'
    '&family=Space+Grotesk:wght@400;500;600;700'
    '&family=Caveat:wght@600;700&display=swap'
);

:root{
    --paper:#EFE7D8;
    --paper-dim:#E3D7BF;
    --ink:#201F2C;
    --ink-soft:#57536A;
    --pine:#2F5D50;
    --pine-deep:#1F4038;
    --stamp:#B23A2E;
    --line:rgba(32,31,44,0.16);
    --line-strong:rgba(32,31,44,0.32);
}


/* ============================================================
   BASE
   ============================================================ */

html,
body,
[data-testid="stAppViewContainer"] {
    background:var(--paper);
}

[data-testid="stHeader"]{
    background:transparent;
}

[data-testid="stAppViewContainer"]{
    overflow-x:hidden;
}

.main{
    background:var(--paper);
}

html,
body,
[class*="css"]{
    font-family:'Space Grotesk', sans-serif;
    color:var(--ink);
}

.block-container{
    width:100%;
    max-width:1180px;
    padding-top:2rem;
    padding-bottom:3rem;
    padding-left:clamp(1rem, 4vw, 2.5rem);
    padding-right:clamp(1rem, 4vw, 2.5rem);
}


/* ============================================================
   TIPOGRAFIA
   ============================================================ */

h1,
h2,
h3,
.display{
    font-family:'Big Shoulders Display', sans-serif !important;
    text-transform:uppercase;
    letter-spacing:0.01em;
    font-weight:700 !important;
    color:var(--ink);
}

.hero-title{
    font-family:'Big Shoulders Display', sans-serif;
    font-size:64px;
    line-height:0.98;
    text-transform:uppercase;
    letter-spacing:0.01em;
    font-weight:700;
    color:var(--ink);
    margin:0 0 18px 0;
}

.page-title{
    font-family:'Big Shoulders Display', sans-serif;
    font-size:48px;
    line-height:1;
    text-transform:uppercase;
    letter-spacing:0.01em;
    font-weight:700;
    color:var(--ink);
    margin:0 0 16px 0;
}

.section-title{
    font-family:'Big Shoulders Display', sans-serif;
    font-size:38px;
    line-height:1;
    text-transform:uppercase;
    font-weight:700;
    color:var(--ink);
    margin:0 0 18px 0;
}

.subsection-title{
    font-family:'Big Shoulders Display', sans-serif;
    font-size:32px;
    line-height:1;
    text-transform:uppercase;
    font-weight:700;
    color:var(--ink);
    margin:0 0 14px 0;
}

.hand{
    font-family:'Caveat', cursive;
    font-weight:700;
    color:var(--stamp);
}


/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"]{
    background:var(--ink);
    color:var(--paper);
}

[data-testid="stSidebar"] *{
    color:var(--paper) !important;
}

[data-testid="stSidebar"] a{
    text-decoration:none;
}

.sidebar-brand{
    font-family:'Big Shoulders Display', sans-serif;
    font-size:24px;
    font-weight:800;
    letter-spacing:0.02em;
}

.sidebar-subtitle{
    font-size:12px;
    opacity:0.7;
    margin-top:4px;
}

.sidebar-divider{
    border:none;
    border-top:1px solid rgba(239,231,216,0.2);
    margin:18px 0;
}


/* ============================================================
   COMPONENTES GERAIS
   ============================================================ */

.frame-tab{
    display:inline-block;
    max-width:100%;
    background:var(--ink);
    color:var(--paper) !important;
    font-family:'Caveat', cursive;
    font-weight:700;
    font-size:19px;
    line-height:1.2;
    padding:4px 18px 6px;
    border-radius:0 0 8px 8px;
    margin-bottom:18px;
}

.intro-text{
    font-size:19px;
    color:var(--ink-soft);
    max-width:70ch;
    line-height:1.55;
}

.body-text{
    line-height:1.7;
}

.muted-text{
    color:var(--ink-soft);
}

.narrow-text{
    max-width:70ch;
}

.rule{
    border:none;
    border-top:1px solid var(--line-strong);
    margin:36px 0;
}


/* ============================================================
   MÉTRICAS
   ============================================================ */

.stats-grid{
    display:grid;
    grid-template-columns:repeat(4, minmax(0, 1fr));
    gap:1px;
    background:var(--line-strong);
    border:1px solid var(--line-strong);
    margin-top:28px;
}

.stat{
    background:var(--paper);
    padding:20px 18px;
    min-width:0;
}

.stat-label{
    font-size:12px;
    color:var(--ink-soft);
    line-height:1.35;
    margin-bottom:6px;
}

.stat-value{
    font-family:'Big Shoulders Display', sans-serif;
    font-size:32px;
    line-height:1;
    font-weight:700;
    color:var(--ink);
}


/* ============================================================
   CHIPS
   ============================================================ */

.chip-row{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
    margin-top:8px;
}

.chip{
    border:1px solid var(--line-strong);
    padding:8px 14px;
    font-size:13px;
    font-weight:600;
    background:var(--paper-dim);
    border-radius:2px;
    max-width:100%;
}


/* ============================================================
   GRIDS
   ============================================================ */

.grid-4{
    display:grid;
    grid-template-columns:repeat(4, minmax(0, 1fr));
    gap:1px;
    background:var(--line-strong);
    border:1px solid var(--line-strong);
    margin-top:10px;
}

.grid-3{
    display:grid;
    grid-template-columns:repeat(3, minmax(0, 1fr));
    gap:1px;
    background:var(--line-strong);
    border:1px solid var(--line-strong);
    margin-top:10px;
}

.grid-2{
    display:grid;
    grid-template-columns:repeat(2, minmax(0, 1fr));
    gap:20px;
    margin-top:10px;
}


/* ============================================================
   NÚCLEOS / CÉLULAS
   ============================================================ */

.cell{
    background:var(--paper);
    padding:22px 20px;
    min-height:150px;
    min-width:0;
}

.cell .index{
    font-family:'Big Shoulders Display', sans-serif;
    font-size:14px;
    color:var(--stamp);
    font-weight:700;
}

.cell h4{
    font-size:18px;
    line-height:1.2;
    margin:8px 0 6px;
    text-transform:none;
    font-weight:700;
    overflow-wrap:anywhere;
}

.cell p{
    font-size:13.5px;
    color:var(--ink-soft);
    line-height:1.5;
    margin:0;
    overflow-wrap:anywhere;
}


/* ============================================================
   CARDS DE LIDERANÇA
   ============================================================ */

.card{
    border:1.5px solid var(--ink);
    background:var(--paper-dim);
    padding:20px 22px;
    border-radius:2px;
    min-width:0;
}

.card h4{
    font-size:13px;
    line-height:1.25;
    text-transform:uppercase;
    letter-spacing:0.06em;
    font-weight:700;
    color:var(--pine);
    margin:0 0 14px;
    padding-bottom:10px;
    border-bottom:1px solid var(--line-strong);
    overflow-wrap:anywhere;
}

.role-row{
    display:flex;
    align-items:flex-start;
    gap:10px;
    padding:9px 0;
    border-top:1px dashed var(--line-strong);
    font-size:13.5px;
    line-height:1.4;
    min-width:0;
}

.role-row:first-of-type{
    border-top:none;
}

.role-row span{
    overflow-wrap:anywhere;
}


/* ============================================================
   PILARES
   ============================================================ */

.pillars-grid{
    display:grid;
    grid-template-columns:repeat(3, minmax(0, 1fr));
    gap:1px;
    background:var(--line-strong);
    border:1px solid var(--line-strong);
    margin-top:10px;
}


/* ============================================================
   OBJETIVOS
   ============================================================ */

.obj-card{
    background:var(--paper);
    border:1.5px solid var(--line-strong);
    padding:22px 20px;
    border-radius:2px;
    min-width:0;
}

.obj-card .num{
    font-family:'Big Shoulders Display', sans-serif;
    font-size:30px;
    color:var(--ink-soft);
    font-weight:700;
}

.obj-card h4{
    font-size:18px;
    line-height:1.2;
    margin:8px 0 6px;
    text-transform:none;
    font-weight:700;
    overflow-wrap:anywhere;
}

.obj-card p{
    font-size:13.5px;
    color:var(--ink-soft);
    line-height:1.5;
    margin:0;
    overflow-wrap:anywhere;
}


/* ============================================================
   PIPELINE
   ============================================================ */

.filmstrip{
    display:grid;
    grid-template-columns:repeat(7, minmax(0, 1fr));
    border:1.5px solid var(--ink);
    margin-top:10px;
    min-width:0;
}

.film-cell{
    padding:18px 16px;
    background:var(--paper);
    border-right:1px dashed var(--line-strong);
    min-width:0;
}

.film-cell:last-child{
    border-right:none;
}

.film-cell .fnum{
    font-family:'Caveat', cursive;
    color:var(--stamp);
    font-size:19px;
    font-weight:700;
}

.film-cell h5{
    font-size:15px;
    line-height:1.25;
    margin:4px 0 4px;
    font-weight:700;
    overflow-wrap:anywhere;
}

.film-cell p{
    font-size:12px;
    color:var(--ink-soft);
    margin:0;
    line-height:1.4;
    overflow-wrap:anywhere;
}


/* ============================================================
   PARTICIPE
   ============================================================ */

.join-grid{
    display:grid;
    grid-template-columns:repeat(3, minmax(0, 1fr));
    gap:16px;
    margin-top:10px;
}

.join-card{
    background:var(--ink);
    color:var(--paper) !important;
    padding:22px 20px;
    border-radius:2px;
    min-width:0;
}

.join-card h4{
    font-size:19px;
    line-height:1.2;
    text-transform:none;
    color:var(--paper) !important;
    margin:0 0 6px;
    font-weight:700;
}

.join-card p{
    font-size:13.5px;
    color:rgba(239,231,216,0.75) !important;
    margin:0;
    line-height:1.5;
    overflow-wrap:anywhere;
}


/* ============================================================
   BOTÕES / CANAIS
   ============================================================ */

.channels{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    margin-top:10px;
}

a.channel-btn{
    display:inline-block;
    border:1.5px solid var(--ink);
    padding:10px 20px;
    text-decoration:none;
    font-weight:700;
    font-size:13px;
    letter-spacing:0.03em;
    text-transform:uppercase;
    color:var(--ink) !important;
    border-radius:2px;
    max-width:100%;
    overflow-wrap:anywhere;
}

.contact-email{
    font-size:22px;
    font-weight:700;
    overflow-wrap:anywhere;
    word-break:break-word;
}


/* ============================================================
   TABLET
   ============================================================ */

@media (max-width: 1000px){

    .stats-grid{
        grid-template-columns:repeat(2, minmax(0, 1fr));
    }

    .grid-4{
        grid-template-columns:repeat(2, minmax(0, 1fr));
    }

    .filmstrip{
        grid-template-columns:repeat(2, minmax(0, 1fr));
    }

    .film-cell{
        border-right:none;
        border-bottom:1px dashed var(--line-strong);
    }

    .film-cell:nth-child(odd){
        border-right:1px dashed var(--line-strong);
    }

    .film-cell:nth-last-child(-n+2){
        border-bottom:none;
    }

}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px){

    .block-container{
        padding-top:1.2rem;
        padding-bottom:2rem;
        padding-left:1rem;
        padding-right:1rem;
    }

    .hero-title{
        font-size:42px;
        line-height:0.98;
        margin-bottom:14px;
    }

    .page-title{
        font-size:38px;
        line-height:1;
    }

    .section-title{
        font-size:31px;
    }

    .subsection-title{
        font-size:28px;
    }

    .intro-text{
        font-size:16px;
        line-height:1.55;
    }

    .frame-tab{
        font-size:17px;
        padding:4px 14px 6px;
        margin-bottom:14px;
    }

    .stats-grid{
        grid-template-columns:repeat(2, minmax(0, 1fr));
        margin-top:22px;
    }

    .stat{
        padding:16px 14px;
    }

    .stat-label{
        font-size:11px;
    }

    .stat-value{
        font-size:28px;
    }

    .grid-4,
    .grid-3,
    .grid-2,
    .pillars-grid,
    .join-grid{
        grid-template-columns:1fr;
    }

    .grid-4,
    .grid-3{
        gap:1px;
    }

    .cell{
        min-height:auto;
        padding:20px 18px;
    }

    .card{
        padding:18px;
    }

    .role-row{
        font-size:13px;
        padding:10px 0;
    }

    .obj-card{
        padding:20px 18px;
    }

    .filmstrip{
        grid-template-columns:1fr;
    }

    .film-cell{
        border-right:none !important;
        border-bottom:1px dashed var(--line-strong);
        padding:17px 15px;
    }

    .film-cell:last-child{
        border-bottom:none;
    }

    .join-card{
        padding:20px 18px;
    }

    .channels{
        flex-direction:column;
        align-items:stretch;
    }

    a.channel-btn{
        width:100%;
        text-align:center;
        box-sizing:border-box;
        margin:0;
    }

    .contact-email{
        font-size:18px;
    }

    hr.rule{
        margin:28px 0;
    }

}


/* ============================================================
   MOBILE MUITO PEQUENO
   ============================================================ */

@media (max-width: 400px){

    .block-container{
        padding-left:0.8rem;
        padding-right:0.8rem;
    }

    .hero-title{
        font-size:36px;
    }

    .page-title{
        font-size:34px;
    }

    .section-title{
        font-size:28px;
    }

    .stats-grid{
        grid-template-columns:1fr;
    }

    .stat{
        padding:15px 14px;
    }

    .stat-value{
        font-size:26px;
    }

    .chip{
        width:100%;
        box-sizing:border-box;
        text-align:left;
    }

}

</style>
"""

st.markdown(CSS, unsafe_allow_html=True)


# ============================================================
# CONTEÚDO
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
        "Marketing divulga só o que passou pelo controle de qualidade.",
    ),
]


CANAIS = {
    "YouTube": "https://youtube.com/@protocoloneoficial?si=n9Iz6yuJhs3W5KgM",
    "Instagram": "https://www.instagram.com/protocoloneofc?igsi=MWRjOWs1bmx3amx5cg==",
    "TikTok": "https://www.tiktok.com/@protocoloneoficial?_r=1&_t=ZS-99IfbZKurp4",
}

EMAIL_CONTATO = "protocolonecontato@gmail.com"


# ============================================================
# SIDEBAR / NAVEGAÇÃO
# ============================================================

st.sidebar.markdown(
    """
    <div class="sidebar-brand">PROTOCOL ONE</div>
    <div class="sidebar-subtitle">ProtoCommunity</div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    "<hr class='sidebar-divider'>",
    unsafe_allow_html=True,
)

pagina = st.sidebar.radio(
    "Navegação",
    ["O Projeto", "Estrutura", "Objetivos", "Participe"],
    label_visibility="collapsed",
)

st.sidebar.markdown(
    "<hr class='sidebar-divider'>",
    unsafe_allow_html=True,
)

st.sidebar.caption("Canais oficiais")

for nome, link in CANAIS.items():
    st.sidebar.markdown(f"[{nome}]({link})")

st.sidebar.caption(EMAIL_CONTATO)


# ============================================================
# PÁGINA: O PROJETO
# ============================================================

if pagina == "O Projeto":

    st.markdown(
        "<span class='frame-tab'>quadro 00 — abertura</span>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='hero-title'>Uma comunidade com disciplina de estúdio.</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="intro-text">
            A ProtoCommunity é o organismo criativo por trás do Protocol One:
            animação, histórias em quadrinhos, produção audiovisual e universos
            ficcionais construídos de forma colaborativa — com hierarquia clara,
            pipeline de produção formal e um lugar definido para cada pessoa que entra.
        </p>
        """,
        unsafe_allow_html=True,
    )

    stats_html = "".join(
        [
            """
            <div class="stat">
                <div class="stat-label">Núcleos organizacionais</div>
                <div class="stat-value">08</div>
            </div>
            """,
            """
            <div class="stat">
                <div class="stat-label">Frentes criativas ativas</div>
                <div class="stat-value">6+</div>
            </div>
            """,
            """
            <div class="stat">
                <div class="stat-label">Canais oficiais</div>
                <div class="stat-value">03</div>
            </div>
            """,
            """
            <div class="stat">
                <div class="stat-label">Etapas do pipeline</div>
                <div class="stat-value">07</div>
            </div>
            """,
        ]
    )

    st.markdown(
        f"<div class='stats-grid'>{stats_html}</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<hr class='rule'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<span class='frame-tab'>quadro 01 — o que é</span>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='section-title'>O que é a ProtoCommunity</div>",
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <p class="body-text">
                O Protocol One nasce dentro da ProtoCommunity, uma comunidade
                colaborativa organizada para funcionar com a seriedade de um
                estúdio profissional de produção criativa. Cada projeto atravessa
                etapas de roteiro, arte, animação, som e publicação antes de chegar
                ao público — e cada etapa tem um responsável claro.
            </p>

            <p class="body-text muted-text">
                Não é apenas um conjunto de grupos de conversa: é uma organização
                com hierarquia, responsabilidades definidas e fluxo de aprovação,
                que hoje usa o WhatsApp como ferramenta de trabalho, sem depender
                dele para existir.
            </p>
            """,
            unsafe_allow_html=True,
        )

    with c2:

        st.markdown(
            "<p style='font-weight:600; margin-bottom:6px;'>Frentes de atuação</p>",
            unsafe_allow_html=True,
        )

        frentes = [
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

        chips_html = "".join(
            f"<span class='chip'>{frente}</span>"
            for frente in frentes
        )

        st.markdown(
            f"<div class='chip-row'>{chips_html}</div>",
            unsafe_allow_html=True,
        )


# ============================================================
# PÁGINA: ESTRUTURA
# ============================================================

elif pagina == "Estrutura":

    st.markdown(
        "<span class='frame-tab'>quadro 02 — estrutura</span>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='page-title'>Oito núcleos. Um só rumo.</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="muted-text narrow-text">
            A ProtoCommunity está organizada em oito núcleos que cobrem desde
            a estratégia institucional até a entrega final de cada projeto ao público.
        </p>
        """,
        unsafe_allow_html=True,
    )

    cells = "".join(
        f"""
        <div class="cell">
            <span class="index">{numero}</span>
            <h4>{titulo}</h4>
            <p>{descricao}</p>
        </div>
        """
        for numero, titulo, descricao in NUCLEOS
    )

    st.markdown(
        f"<div class='grid-4'>{cells}</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<hr class='rule'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='subsection-title'>Estrutura de Liderança</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="muted-text narrow-text">
            A estrutura de liderança organiza as principais responsabilidades
            da ProtoCommunity, estabelecendo funções claras para a gestão,
            criação, produção e desenvolvimento dos projetos.
        </p>
        """,
        unsafe_allow_html=True,
    )

    cards_html = ""

    for titulo, papeis in LIDERANCA:

        rows = "".join(
            f"""
            <div class="role-row">
                <span>{cargo}</span>
            </div>
            """
            for cargo in papeis
        )

        cards_html += f"""
        <div class="card">
            <h4>{titulo}</h4>
            {rows}
        </div>
        """

    st.markdown(
        f"""
        <div class="grid-4"
             style="background:transparent; border:none; gap:16px;">
            {cards_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<hr class='rule'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='subsection-title'>Conselho Consultivo e Deliberativo</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="muted-text narrow-text">
            Órgão colegiado responsável pela salvaguarda institucional,
            fiscalização e deliberações estratégicas da ProtoCommunity.
        </p>
        """,
        unsafe_allow_html=True,
    )

    pilares = "".join(
        f"""
        <div class="cell">
            <h4>{nome}</h4>
            <p>{descricao}</p>
        </div>
        """
        for nome, descricao in [
            (
                "Fiscalização",
                "Delibera sobre questões estruturais e operacionais da organização.",
            ),
            (
                "Governança",
                "Decide mudanças na estrutura e no direcionamento estratégico.",
            ),
            (
                "Transparência",
                "Mantém o alinhamento ético e a cultura institucional vivos.",
            ),
        ]
    )

    st.markdown(
        f"<div class='pillars-grid'>{pilares}</div>",
        unsafe_allow_html=True,
    )


# ============================================================
# PÁGINA: OBJETIVOS
# ============================================================

elif pagina == "Objetivos":

    st.markdown(
        "<span class='frame-tab'>quadro 03 — objetivos</span>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='page-title'>Para onde estamos indo</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="muted-text narrow-text">
            Quatro objetivos orientam cada decisão da ProtoCommunity,
            do primeiro rascunho à publicação final.
        </p>
        """,
        unsafe_allow_html=True,
    )

    obj_html = "".join(
        f"""
        <div class="obj-card">
            <span class="num">{numero}</span>
            <h4>{titulo}</h4>
            <p>{descricao}</p>
        </div>
        """
        for numero, titulo, descricao in OBJETIVOS
    )

    st.markdown(
        f"""
        <div class="grid-4"
             style="background:transparent; border:none; gap:16px;">
            {obj_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<hr class='rule'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='subsection-title'>Como uma ideia vira entrega</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="muted-text narrow-text">
            Do conceito aprovado até o público, cada projeto segue um
            pipeline com etapas e responsáveis definidos.
        </p>
        """,
        unsafe_allow_html=True,
    )

    pipe_html = "".join(
        f"""
        <div class="film-cell">
            <span class="fnum">{numero}</span>
            <h5>{titulo}</h5>
            <p>{descricao}</p>
        </div>
        """
        for numero, titulo, descricao in PIPELINE
    )

    st.markdown(
        f"<div class='filmstrip'>{pipe_html}</div>",
        unsafe_allow_html=True,
    )


# ============================================================
# PÁGINA: PARTICIPE
# ============================================================

elif pagina == "Participe":

    st.markdown(
        "<span class='frame-tab'>quadro 04 — participe</span>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='page-title'>Faça parte do Protocol One</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="muted-text narrow-text">
            Criadores, parceiros, imprensa e apoiadores encontram aqui
            a porta de entrada certa para a ProtoCommunity.
        </p>
        """,
        unsafe_allow_html=True,
    )

    join_html = "".join(
        f"""
        <div class="join-card">
            <h4>{titulo}</h4>
            <p>{descricao}</p>
        </div>
        """
        for titulo, descricao in [
            (
                "Crie",
                "Contribua para projetos de animação, HQs e audiovisual de impacto real, dentro de um pipeline profissional.",
            ),
            (
                "Cresça",
                "Desenvolva suas habilidades em um ambiente colaborativo, com mentoria de quem já ocupa cargos de direção.",
            ),
            (
                "Conecte-se",
                "Faça parte de uma organização que valoriza qualidade, inovação e crescimento contínuo.",
            ),
        ]
    )

    st.markdown(
        f"<div class='join-grid'>{join_html}</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<hr class='rule'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='font-weight:600; margin-bottom:4px;'>Canais oficiais</p>",
        unsafe_allow_html=True,
    )

    canais_html = "".join(
        f"""
        <a class="channel-btn"
           href="{link}"
           target="_blank"
           rel="noopener noreferrer">
            {nome}
        </a>
        """
        for nome, link in CANAIS.items()
    )

    st.markdown(
        f"<div class='channels'>{canais_html}</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="muted-text narrow-text" style="margin-top:20px;">
            Criadores externos interessados em colaborar, jornalistas cobrindo
            nossos projetos, e apoiadores ou investidores que queiram fortalecer
            a ProtoCommunity são igualmente bem-vindos — escreva diretamente
            para a Diretoria pelo e-mail abaixo.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="margin-top:10px;">
            <span style="
                font-size:12px;
                text-transform:uppercase;
                letter-spacing:0.1em;
                color:var(--ink-soft);
            ">
                E-mail oficial de contato
            </span>
            <br>
            <span class="contact-email">
                {EMAIL_CONTATO}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )
