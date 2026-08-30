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
    page_icon="logo.png" if False else None, # sem emoji no favicon; None usa o padrão
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# ESTILO (fiel à identidade visual: papel kraft, tinta escura,
# verde-pinho de destaque, vermelho de "carimbo")
# ============================================================
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&family=Caveat:wght@600;700&display=swap');

:root{
    --paper:#EFE7D8;
    --paper-dim:#E3D7BF;
    --ink:#201F2C;
    --ink-soft:#57536A;
    --pine:#2F5D50;
    --pine-deep:#1F4038;
    --stamp:#B23A2E;
    --line: rgba(32,31,44,0.16);
    --line-strong: rgba(32,31,44,0.32);
}

/* fundo geral do app */
[data-testid="stAppViewContainer"], .main {
    background: var(--paper);
}
[data-testid="stHeader"]{ background: transparent; }
[data-testid="stSidebar"]{
    background: var(--ink);
    color: var(--paper);
}
[data-testid="stSidebar"] * { color: var(--paper) !important; }

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    color: var(--ink);
}

h1, h2, h3, .display {
    font-family: 'Big Shoulders Display', sans-serif !important;
    text-transform: uppercase;
    letter-spacing: 0.01em;
    font-weight: 700 !important;
    color: var(--ink);
}

.hand { font-family: 'Caveat', cursive; font-weight: 700; color: var(--stamp); }

/* remove excesso de padding padrão do streamlit */
.block-container{ padding-top: 2rem; padding-bottom: 3rem; max-width: 1180px; }

/* -------- componentes reutilizáveis -------- */
.eyebrow{
    font-size:13px; font-weight:700; letter-spacing:0.14em; text-transform:uppercase;
    color:var(--pine); margin-bottom:10px;
}

.frame-tab{
    display:inline-block;
    background:var(--ink); color:var(--paper) !important;
    font-family:'Caveat', cursive; font-weight:700; font-size:19px;
    padding:4px 18px 6px; border-radius:0 0 8px 8px; margin-bottom:18px;
}

.chip-row{ display:flex; flex-wrap:wrap; gap:10px; margin-top:6px; }
.chip{
    border:1px solid var(--line-strong); padding:8px 14px; font-size:13px;
    font-weight:600; background:var(--paper-dim); border-radius:2px;
}

.grid-4{ display:grid; grid-template-columns:repeat(4,1fr); gap:1px;
    background:var(--line-strong); border:1px solid var(--line-strong); margin-top:10px; }
.grid-2{ display:grid; grid-template-columns:repeat(2,1fr); gap:20px; margin-top:10px; }
.grid-3{ display:grid; grid-template-columns:repeat(3,1fr); gap:1px;
    background:var(--line-strong); border:1px solid var(--line-strong); margin-top:10px; }

.cell{ background:var(--paper); padding:22px 20px; min-height:150px; }
.cell .index{ font-family:'Big Shoulders Display'; font-size:14px; color:var(--stamp); font-weight:700; }
.cell h4{ font-size:18px; margin:8px 0 6px; text-transform:none; font-weight:700; }
.cell p{ font-size:13.5px; color:var(--ink-soft); line-height:1.5; margin:0; }

.card{
    border:1.5px solid var(--ink); background:var(--paper-dim); padding:20px 22px; border-radius:2px;
}
.card h4{
    font-size:13px; text-transform:uppercase; letter-spacing:0.06em; font-weight:700;
    color:var(--pine); margin:0 0 14px; padding-bottom:10px; border-bottom:1px solid var(--line-strong);
}
.role-row{
    display:flex; justify-content:space-between; align-items:center; gap:10px;
    padding:8px 0; border-top:1px dashed var(--line-strong); font-size:13.5px;
}
.role-row:first-of-type{ border-top:none; }
.badge{
    font-size:11px; font-weight:700; letter-spacing:0.03em; text-transform:uppercase;
    padding:3px 9px; border-radius:2px;
}
.badge.active{ background:var(--pine); color:var(--paper); }
.badge.vago{ border:1px dashed var(--line-strong); color:var(--ink-soft); }

.pill{
    display:inline-block; border:1px solid var(--ink); padding:6px 14px; font-size:13px;
    font-weight:600; background:var(--paper); border-radius:2px; margin:0 6px 6px 0;
}

.obj-card{ background:var(--paper); border:1.5px solid var(--line-strong); padding:22px 20px; border-radius:2px; }
.obj-card .num{ font-family:'Big Shoulders Display'; font-size:30px; color:var(--ink-soft); font-weight:700; }
.obj-card h4{ font-size:18px; margin:8px 0 6px; text-transform:none; font-weight:700; }
.obj-card p{ font-size:13.5px; color:var(--ink-soft); line-height:1.5; margin:0; }

.filmstrip{ display:flex; overflow-x:auto; border:1.5px solid var(--ink); margin-top:10px; }
.film-cell{ flex:1 0 170px; padding:18px 16px; border-right:1px dashed var(--line-strong); background:var(--paper); }
.film-cell:last-child{ border-right:none; }
.film-cell .fnum{ font-family:'Caveat'; color:var(--stamp); font-size:19px; font-weight:700; }
.film-cell h5{ font-size:15px; margin:4px 0 4px; font-weight:700; }
.film-cell p{ font-size:12px; color:var(--ink-soft); margin:0; line-height:1.4; }

.join-card{ background:var(--ink); color:var(--paper) !important; padding:22px 20px; border-radius:2px; }
.join-card h4{ font-size:19px; text-transform:none; color:var(--paper) !important; margin:0 0 6px; font-weight:700; }
.join-card p{ font-size:13.5px; color:rgba(239,231,216,0.75) !important; margin:0; line-height:1.5; }

hr.rule{ border:none; border-top:1px solid var(--line-strong); margin:36px 0; }

a.channel-btn{
    display:inline-block; border:1.5px solid var(--ink); padding:10px 20px; text-decoration:none;
    font-weight:700; font-size:13px; letter-spacing:0.03em; text-transform:uppercase;
    color:var(--ink) !important; margin:0 10px 10px 0; border-radius:2px;
}

@media (max-width: 900px){
    .grid-4{ grid-template-columns:repeat(2,1fr); }
    .grid-2{ grid-template-columns:1fr; }
    .grid-3{ grid-template-columns:1fr; }
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ============================================================
# CONTEÚDO (fonte: ProtoCommunity — Estrutura Organizacional)
# ============================================================
NUCLEOS = [
    ("01", "Administração e Diretoria", "Visão institucional, estratégia e coordenação geral de todas as áreas."),
    ("02", "Conselho", "Fiscalização e deliberação colegiada sobre mudanças estruturais."),
    ("03", "Jurídico e Propriedade Intelectual", "Proteção legal da obra, dos personagens e da própria organização."),
    ("04", "Financeiro e Administrativo", "Recursos, orçamento e prestação de contas transparente."),
    ("05", "Gestão de Pessoas", "Recrutamento, integração, desenvolvimento e mediação de conflitos."),
    ("06", "Pré-produção", "Roteiro, universo, personagens, cenários e storyboard."),
    ("07", "Arte, Animação e Pós-produção", "Concept art, ilustração, animação, edição, dublagem e som."),
    ("08", "Marketing e Comunidade", "Redes sociais, parcerias, sugestões e relacionamento com o público."),
]

LIDERANCA = [
    ("Direção executiva", [("Diretora-Geral", "Nicole", True), ("Diretor de Produção", "Vago", False)]),
    ("Núcleo criativo", [("Diretor Criativo", "Arthur", True), ("Diretora de Personagens", "Nicole", True), ("Diretora de Dublagem", "Nicole", True)]),
    ("Arte e produção técnica", [("Diretor de Arte", "Vago", False), ("Diretor de Animação", "Vago", False), ("Diretor de Pós-Produção", "Vago", False)]),
    ("Gestão, marketing e governança", [("Diretor de Marketing", "Igor", True), ("Diretor Financeiro", "Miguel", True), ("Diretor Jurídico", "Miguel", True)]),
]

OBJETIVOS = [
    ("01", "Conteúdo de alta qualidade", "Animações, HQs e produções audiovisuais que se destacam pelo cuidado criativo e técnico."),
    ("02", "Comunidade escalável", "Processos profissionais e colaborativos que crescem junto com a organização."),
    ("03", "Parcerias e alcance", "Parcerias estratégicas e expansão consistente da presença nas redes sociais."),
    ("04", "Formação de talentos", "Oportunidades reais de desenvolvimento profissional dentro de universos ficcionais memoráveis."),
]

PIPELINE = [
    ("01", "Ideia e conceito", "Direção Criativa propõe; Diretoria aprova o conceito."),
    ("02", "Roteiro", "Roteirista-Chefe escreve; Direção Criativa aprova."),
    ("03", "Storyboard", "Transforma o roteiro em sequência visual de planos."),
    ("04", "Animatic", "Valida timing e ritmo antes da animação completa."),
    ("05", "Animação e som", "Cenas animadas, dublagem final e design de som."),
    ("06", "Controle de qualidade", "Revisão final antes de qualquer publicação."),
    ("07", "Publicação", "Marketing divulga só o que passou pelo controle de qualidade."),
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
    "<div style='font-family:\"Big Shoulders Display\"; font-size:24px; font-weight:800; "
    "letter-spacing:0.02em;'>PROTOCOL ONE</div>"
    "<div style='font-size:12px; opacity:0.7; margin-top:4px;'>ProtoCommunity</div>",
    unsafe_allow_html=True,
)
st.sidebar.markdown("<hr style='border-color:rgba(239,231,216,0.2);'>", unsafe_allow_html=True)

pagina = st.sidebar.radio(
    "Navegação",
    ["O Projeto", "Estrutura", "Objetivos", "Participe"],
    label_visibility="collapsed",
)

st.sidebar.markdown("<hr style='border-color:rgba(239,231,216,0.2);'>", unsafe_allow_html=True)
st.sidebar.caption("Canais oficiais")
for nome, link in CANAIS.items():
    st.sidebar.markdown(f"[{nome}]({link})")
st.sidebar.caption(EMAIL_CONTATO)


# ============================================================
# PÁGINA: O PROJETO
# ============================================================
if pagina == "O Projeto":
    st.markdown("<span class='frame-tab'>quadro 00 — abertura</span>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size:64px;'>Uma comunidade com disciplina de estúdio.</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size:19px; color:var(--ink-soft); max-width:70ch; line-height:1.55;'>"
        "A ProtoCommunity é o organismo criativo por trás do Protocol One: animação, histórias em "
        "quadrinhos, produção audiovisual e universos ficcionais construídos de forma colaborativa "
        "— com hierarquia clara, pipeline de produção formal e um lugar definido para cada pessoa "
        "que entra.</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Núcleos organizacionais", "08")
    col2.metric("Frentes criativas ativas", "6+")
    col3.metric("Canais oficiais", "03")
    col4.metric("Etapas do pipeline", "16")

    st.markdown("<hr class='rule'>", unsafe_allow_html=True)

    st.markdown("<span class='frame-tab'>quadro 01 — o que é</span>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:38px;'>O que é a ProtoCommunity</h2>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            "<p style='line-height:1.7;'>O Protocol One nasce dentro da ProtoCommunity, uma comunidade "
            "colaborativa organizada para funcionar com a seriedade de um estúdio profissional de "
            "produção criativa. Cada projeto atravessa etapas de roteiro, arte, animação, som e "
            "publicação antes de chegar ao público — e cada etapa tem um responsável claro.</p>"
            "<p style='line-height:1.7; color:var(--ink-soft);'>Não é apenas um conjunto de grupos de "
            "conversa: é uma organização com hierarquia, responsabilidades definidas e fluxo de "
            "aprovação, que hoje usa o WhatsApp como ferramenta de trabalho, sem depender dele para "
            "existir.</p>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown("<p style='font-weight:600; margin-bottom:6px;'>Frentes de atuação</p>", unsafe_allow_html=True)
        frentes = [
            "Animação", "Histórias em quadrinhos", "Produção audiovisual", "Criação de personagens",
            "Construção de universos", "Edição de vídeo", "Dublagem", "Design de som",
            "Ilustração", "Conteúdo para redes sociais", "Marketing", "Parcerias externas",
        ]
        chips_html = "".join(f"<span class='chip'>{f}</span>" for f in frentes)
        st.markdown(f"<div class='chip-row'>{chips_html}</div>", unsafe_allow_html=True)


# ============================================================
# PÁGINA: ESTRUTURA
# ============================================================
elif pagina == "Estrutura":
    st.markdown("<span class='frame-tab'>quadro 02 — estrutura</span>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size:48px;'>Oito núcleos. Um só rumo.</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color:var(--ink-soft); max-width:70ch;'>A ProtoCommunity está organizada em oito "
        "núcleos que cobrem desde a estratégia institucional até a entrega final de cada projeto ao "
        "público.</p>",
        unsafe_allow_html=True,
    )

    cells = "".join(
        f"<div class='cell'><span class='index'>{i}</span><h4>{titulo}</h4><p>{desc}</p></div>"
        for i, titulo, desc in NUCLEOS
    )
    st.markdown(f"<div class='grid-4'>{cells}</div>", unsafe_allow_html=True)

    st.markdown("<hr class='rule'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:32px;'>Liderança inicial</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color:var(--ink-soft);'>Um time enxuto sustenta hoje toda a estrutura em fase de "
        "fundação — cargos vagos permanecem no organograma, prontos para serem ocupados.</p>",
        unsafe_allow_html=True,
    )

    cards_html = ""
    for titulo, papeis in LIDERANCA:
        rows = "".join(
            f"<div class='role-row'><span>{cargo}</span>"
            f"<span class='badge {'active' if ativo else 'vago'}'>{pessoa}</span></div>"
            for cargo, pessoa, ativo in papeis
        )
        cards_html += f"<div class='card'><h4>{titulo}</h4>{rows}</div>"
    st.markdown(f"<div class='grid-4' style='background:transparent; border:none; gap:16px;'>{cards_html}</div>", unsafe_allow_html=True)

    st.markdown("<hr class='rule'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:32px;'>Conselho Consultivo e Deliberativo</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color:var(--ink-soft); max-width:70ch;'>Órgão colegiado responsável pela "
        "salvaguarda institucional, fiscalização e deliberações estratégicas da ProtoCommunity.</p>"
        "<div>"
        "<span class='pill'>Nicole</span><span class='pill'>Miguel</span><span class='pill'>Igor</span>"
        "</div>",
        unsafe_allow_html=True,
    )
    pilares = "".join(
        f"<div class='cell'><h4>{nome}</h4><p>{desc}</p></div>"
        for nome, desc in [
            ("Fiscalização", "Delibera sobre questões estruturais e operacionais da organização."),
            ("Governança", "Decide mudanças na estrutura e no direcionamento estratégico."),
            ("Transparência", "Mantém o alinhamento ético e a cultura institucional vivos."),
        ]
    )
    st.markdown(f"<div class='grid-3'>{pilares}</div>", unsafe_allow_html=True)


# ============================================================
# PÁGINA: OBJETIVOS
# ============================================================
elif pagina == "Objetivos":
    st.markdown("<span class='frame-tab'>quadro 03 — objetivos</span>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size:48px;'>Para onde estamos indo</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color:var(--ink-soft); max-width:70ch;'>Quatro objetivos orientam cada decisão da "
        "ProtoCommunity, do primeiro rascunho à publicação final.</p>",
        unsafe_allow_html=True,
    )

    obj_html = "".join(
        f"<div class='obj-card'><span class='num'>{num}</span><h4>{titulo}</h4><p>{desc}</p></div>"
        for num, titulo, desc in OBJETIVOS
    )
    st.markdown(f"<div class='grid-4' style='background:transparent; border:none; gap:16px;'>{obj_html}</div>", unsafe_allow_html=True)

    st.markdown("<hr class='rule'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:32px;'>Como uma ideia vira entrega</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color:var(--ink-soft); max-width:70ch;'>Do conceito aprovado até o público, cada "
        "projeto segue um pipeline com etapas e responsáveis definidos.</p>",
        unsafe_allow_html=True,
    )
    pipe_html = "".join(
        f"<div class='film-cell'><span class='fnum'>{num}</span><h5>{titulo}</h5><p>{desc}</p></div>"
        for num, titulo, desc in PIPELINE
    )
    st.markdown(f"<div class='filmstrip'>{pipe_html}</div>", unsafe_allow_html=True)


# ============================================================
# PÁGINA: PARTICIPE
# ============================================================
elif pagina == "Participe":
    st.markdown("<span class='frame-tab'>quadro 04 — participe</span>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size:48px;'>Faça parte do Protocol One</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color:var(--ink-soft); max-width:70ch;'>Criadores, parceiros, imprensa e "
        "apoiadores encontram aqui a porta de entrada certa para a ProtoCommunity.</p>",
        unsafe_allow_html=True,
    )

    join_html = "".join(
        f"<div class='join-card'><h4>{titulo}</h4><p>{desc}</p></div>"
        for titulo, desc in [
            ("Crie", "Contribua para projetos de animação, HQs e audiovisual de impacto real, dentro de um pipeline profissional."),
            ("Cresça", "Desenvolva suas habilidades em um ambiente colaborativo, com mentoria de quem já ocupa cargos de direção."),
            ("Conecte-se", "Faça parte de uma organização que valoriza qualidade, inovação e crescimento contínuo."),
        ]
    )
    st.markdown(f"<div class='grid-3' style='background:transparent; border:none; gap:16px;'>{join_html}</div>", unsafe_allow_html=True)

    st.markdown("<hr class='rule'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:600; margin-bottom:4px;'>Canais oficiais</p>", unsafe_allow_html=True)
    canais_html = "".join(f"<a class='channel-btn' href='{link}' target='_blank'>{nome}</a>" for nome, link in CANAIS.items())
    st.markdown(canais_html, unsafe_allow_html=True)

    st.markdown(
        "<p style='color:var(--ink-soft); max-width:70ch; margin-top:20px;'>Criadores externos "
        "interessados em colaborar, jornalistas cobrindo nossos projetos, e apoiadores ou "
        "investidores que queiram fortalecer a ProtoCommunity são igualmente bem-vindos — escreva "
        "diretamente para a Diretoria pelo e-mail abaixo.</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='margin-top:10px;'><span style='font-size:12px; text-transform:uppercase; "
        f"letter-spacing:0.1em; color:var(--ink-soft);'>E-mail oficial de contato</span><br>"
        f"<span style='font-size:22px; font-weight:700;'>{EMAIL_CONTATO}</span></div>",
        unsafe_allow_html=True,
    )