"""Protocol One — ProtoCommunity (app Streamlit)."""

from html import escape as esc

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

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --paper: #F6F4EE;
    --paper-card: #FFFFFF;

    --ink: #12232A;
    --ink-soft: #4A5B61;

    --navy: #0F3A47;
    --navy-deep: #0A2630;

    --teal: #1F7A80;
    --teal-dark: #165A63;
    --teal-bright: #5FD0C8;
    --teal-soft: #D8EEEE;

    --gold: #D4A64A;
    --gold-deep: #8F6B1F;
    --gold-soft: #F3E6C8;

    --line: rgba(18, 35, 42, 0.12);
    --line-strong: rgba(18, 35, 42, 0.26);
    --shadow: 0 10px 30px rgba(10, 38, 48, 0.08);
    --shadow-hover: 0 14px 34px rgba(10, 38, 48, 0.14);
    --display: "Big Shoulders Display", sans-serif;

    /* Papéis semânticos: mudam entre claro e escuro */
    --heading-accent: var(--navy);
    --btn-bg: var(--navy);
    --teal-text: var(--teal);
    --gold-text: var(--gold-deep);
    --surface: rgba(255, 255, 255, 0.62);
    --glow: rgba(95, 208, 200, 0.14);

    color-scheme: light dark;
}

/* ---------- TEMA ESCURO NATIVO ---------- */

@media (prefers-color-scheme: dark) {
    :root {
        --paper: #0C1A20;
        --paper-card: #14282F;

        --ink: #EAF1F0;
        --ink-soft: #A9BDC0;

        --teal-soft: rgba(95, 208, 200, 0.13);

        --line: rgba(255, 255, 255, 0.12);
        --line-strong: rgba(255, 255, 255, 0.26);
        --shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
        --shadow-hover: 0 14px 34px rgba(0, 0, 0, 0.5);

        --heading-accent: #9ADAD6;
        --btn-bg: #1F7A80;
        --teal-text: #5FD0C8;
        --gold-text: #D4A64A;
        --surface: rgba(255, 255, 255, 0.04);
        --glow: rgba(95, 208, 200, 0.08);
    }
}

/* ---------- BASE ---------- */

*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background:
        radial-gradient(ellipse 70% 40% at 85% -5%, var(--glow), transparent 70%),
        var(--paper);
    font-family: "Space Grotesk", sans-serif;
    color: var(--ink);
}

.block-container {
    width: 100%;
    max-width: 1280px;
    padding: 2rem clamp(1rem, 4vw, 3rem) 4rem;
}

footer { visibility: hidden; }

.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
    font-family: var(--display);
    color: var(--ink);
    text-transform: uppercase;
    letter-spacing: 0.02em;
}

.stMarkdown p { color: var(--ink-soft); }

a:focus-visible, .stRadio label:focus-visible {
    outline: 2px solid var(--gold);
    outline-offset: 2px;
}

/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--navy-deep) 0%, #0E3340 100%);
    border-right: 1px solid rgba(255, 255, 255, 0.08);
}

section[data-testid="stSidebar"] * { color: #F4F7F5 !important; }

.sidebar-logo {
    font-family: var(--display);
    font-size: 38px;
    line-height: 0.88;
    font-weight: 800;
    letter-spacing: 0.04em;
    margin-bottom: 0.3rem;
}

.sidebar-subtitle {
    font-size: 12px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

section[data-testid="stSidebar"] .sidebar-subtitle { color: #A9D6D6 !important; }

.sidebar-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin: 1.5rem 0 0.65rem;
}

section[data-testid="stSidebar"] .sidebar-label { color: var(--teal-bright) !important; }

/* Links da sidebar (fundo escuro): texto claro, hover dourado.
   Seletor mais específico para vencer o "section[...] *" acima. */
section[data-testid="stSidebar"] a.side-link {
    display: block;
    margin: 0 0 8px;
    padding: 10px 14px;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 4px;
    background: transparent;
    color: #F4F7F5 !important;
    text-decoration: none !important;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.04em;
    transition: background 0.2s ease, color 0.2s ease, border-color 0.2s ease;
}

section[data-testid="stSidebar"] a.side-link:hover {
    background: var(--gold);
    border-color: var(--gold);
    color: var(--navy-deep) !important;
}

/* Item selecionado do menu: dourado em vez do vermelho padrão do Streamlit */
section[data-testid="stSidebar"] label[data-baseweb="radio"]:has(input:checked) > div:first-child {
    background-color: var(--gold) !important;
    border-color: var(--gold) !important;
}

section[data-testid="stSidebar"] label[data-baseweb="radio"]:has(input:checked) {
    font-weight: 700;
}

section[data-testid="stSidebar"] a.side-email {
    font-size: 12px;
    overflow-wrap: anywhere;
    text-decoration: underline;
}

/* ---------- TIPOGRAFIA ---------- */

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: var(--teal-text);
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
    flex-shrink: 0;
}

.hero-title, .section-title-lg, .section-title {
    font-family: var(--display);
    font-weight: 700;
    text-transform: uppercase;
    color: var(--ink);
    overflow-wrap: break-word;
}

.hero-title {
    font-size: 68px;
    line-height: 0.92;
    letter-spacing: -0.015em;
    max-width: 920px;
    margin-bottom: 1.25rem;
}

.section-title-lg { font-size: 50px; line-height: 0.95; margin-bottom: 1rem; }
.section-title    { font-size: 36px; line-height: 1;    margin-bottom: 0.8rem; }

.lead      { font-size: 19px; line-height: 1.65; max-width: 850px; color: var(--ink-soft); }
.body-copy { font-size: 16px; line-height: 1.7; color: var(--ink-soft); margin-bottom: 1rem; }

.frame-tab {
    display: inline-block;
    max-width: 100%;
    padding: 7px 11px;
    margin-bottom: 1rem;
    border: 1px solid var(--line-strong);
    border-radius: 4px;
    color: var(--teal-text);
    background: var(--surface);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
}

.accent-line { width: 72px; height: 4px; background: var(--gold); margin: 1.5rem 0 2rem; }
.rule        { height: 1px; width: 100%; background: var(--line); margin: 3rem 0; }
.spacer      { height: 24px; }
.spacer-sm   { height: 18px; }

/* ---------- GRIDS ---------- */

.grid-4, .grid-3, .grid-2, .filmstrip, .stats-grid {
    display: grid;
    width: 100%;
    gap: 14px;
    min-width: 0;
}

.grid-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.filmstrip { grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 8px; }
.stats-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; margin-top: 2.2rem; }

.cell, .card, .obj-card, .join-card, .film-cell, .stat {
    min-width: 0;
    overflow-wrap: break-word;
    hyphens: auto;
}

/* ---------- CARDS ---------- */

.cell {
    min-height: 180px;
    padding: 20px;
    border: 1px solid var(--line);
    background: var(--surface);
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.cell:hover {
    transform: translateY(-2px);
    border-color: rgba(31, 122, 128, 0.4);
    box-shadow: var(--shadow);
}

.cell-number, .obj-number {
    color: var(--gold-text);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.1em;
    margin-bottom: 2rem;
}

.cell-title {
    font-family: var(--display);
    font-size: 23px;
    line-height: 1;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--ink);
    margin-bottom: 0.65rem;
}

.cell-text { color: var(--ink-soft); font-size: 13px; line-height: 1.55; }

.card {
    min-height: 190px;
    padding: 22px;
    border: 1px solid var(--line);
    background: var(--paper-card);
    box-shadow: var(--shadow);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover { transform: translateY(-2px); box-shadow: var(--shadow-hover); }

.card-title {
    font-family: var(--display);
    font-size: 25px;
    line-height: 1;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--ink);
    margin-bottom: 0.75rem;
}

/* ---------- CHIPS / BADGES ---------- */

.chip-row, .role-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 1rem; min-width: 0; }

.chip, .pill, .badge { max-width: 100%; overflow-wrap: break-word; }

.chip {
    display: inline-block;
    padding: 8px 11px;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: var(--paper-card);
    color: var(--heading-accent);
    font-size: 12px;
    line-height: 1.25;
}

.chip:hover { border-color: rgba(31, 122, 128, 0.4); background: var(--teal-soft); }

.badge {
    display: inline-block;
    padding: 6px 9px;
    border-radius: 4px;
    background: var(--teal-soft);
    border: 1px solid rgba(31, 122, 128, 0.22);
    color: var(--teal-text);
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

/* ---------- OBJETIVOS ---------- */

.obj-card {
    position: relative;
    overflow: hidden;
    padding: 25px;
    min-height: 210px;
    background: linear-gradient(145deg, var(--navy) 0%, var(--teal-dark) 100%);
    border: 1px solid rgba(255, 255, 255, 0.04);
    box-shadow: var(--shadow);
}

.obj-card:nth-child(2) { background: linear-gradient(145deg, var(--teal-dark) 0%, var(--teal) 100%); }
.obj-card:nth-child(3) { background: linear-gradient(145deg, var(--navy-deep) 0%, var(--navy) 100%); }
.obj-card:nth-child(4) { background: linear-gradient(145deg, var(--teal) 0%, var(--teal-dark) 100%); }

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

.obj-title {
    font-family: var(--display);
    font-size: 25px;
    line-height: 1;
    text-transform: uppercase;
    color: #FFFFFF;
    margin-bottom: 0.8rem;
}

.obj-number { color: var(--gold); }

.obj-text { color: #D6ECEC; font-size: 13px; line-height: 1.6; }

/* ---------- PIPELINE ---------- */

.film-cell {
    min-height: 190px;
    padding: 17px;
    background: var(--paper-card);
    border: 1px solid var(--line);
    box-shadow: 0 4px 15px rgba(16, 47, 56, 0.025);
}

.film-cell::before {
    content: "";
    display: block;
    width: 100%;
    height: 5px;
    background: linear-gradient(90deg, var(--gold) 0%, var(--teal) 100%);
    margin-bottom: 20px;
}

.film-number { font-size: 10px; color: var(--teal-text); font-weight: 700; letter-spacing: 0.08em; margin-bottom: 1.3rem; }

.film-title {
    font-family: var(--display);
    font-size: 21px;
    line-height: 1;
    text-transform: uppercase;
    color: var(--ink);
    margin-bottom: 0.7rem;
}

.film-text { font-size: 12px; line-height: 1.5; color: var(--ink-soft); }

/* ---------- ESTATÍSTICAS ---------- */

.stat { padding: 19px; border-top: 3px solid var(--teal); background: var(--paper-card); box-shadow: var(--shadow); }
.stat:nth-child(even) { border-top-color: var(--gold); }

.stat-value {
    font-family: var(--display);
    font-size: 38px;
    line-height: 0.9;
    font-weight: 700;
    color: var(--heading-accent);
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

/* ---------- PARTICIPE ---------- */

.join-card {
    padding: 28px;
    min-height: 215px;
    border: 1px solid var(--line);
    background: var(--paper-card);
    box-shadow: var(--shadow);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.join-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-hover); }

.join-symbol { font-family: var(--display); font-size: 40px; color: var(--gold); line-height: 1; margin-bottom: 1.2rem; }

.join-title {
    font-family: var(--display);
    font-size: 29px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--ink);
    margin-bottom: 0.7rem;
}

.join-text { font-size: 13px; line-height: 1.65; color: var(--ink-soft); }

/* Botões da área principal (fundo claro) */
a.btn {
    display: inline-block;
    margin: 4px 8px 4px 0;
    padding: 12px 18px;
    border: 1px solid var(--btn-bg);
    border-radius: 4px;
    background: var(--btn-bg);
    color: #FFFFFF !important;
    text-decoration: none !important;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    transition: background 0.2s ease, color 0.2s ease, border-color 0.2s ease;
}

a.btn:hover { background: var(--gold); border-color: var(--gold); color: var(--navy-deep) !important; }

a.btn.ghost { background: transparent; color: var(--heading-accent) !important; border-color: var(--line-strong); }
a.btn.ghost:hover { background: var(--btn-bg); border-color: var(--btn-bg); color: #FFFFFF !important; }

/* ---------- STREAMLIT ---------- */

[data-testid="stHorizontalBlock"], [data-testid="stMarkdownContainer"] { min-width: 0; max-width: 100%; }

/* ---------- TABLET ---------- */

@media (max-width: 1100px) {
    .grid-4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .filmstrip { grid-template-columns: repeat(4, minmax(0, 1fr)); }
    .stats-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

/* ---------- MOBILE ---------- */

@media (max-width: 700px) {
    .block-container { padding: 1.25rem 1rem 2.5rem; }

    .hero-title { font-size: 43px; line-height: 0.94; }
    .section-title-lg { font-size: 36px; line-height: 0.96; }
    .section-title { font-size: 29px; }
    .lead { font-size: 16px; line-height: 1.6; }
    .body-copy { font-size: 14px; line-height: 1.65; }

    .grid-4, .grid-3, .grid-2, .filmstrip { grid-template-columns: 1fr; }
    .stats-grid { grid-template-columns: 1fr 1fr; }

    .film-cell, .cell, .card, .obj-card, .join-card { min-height: auto; }
    .cell-number, .obj-number { margin-bottom: 1.2rem; }

    [data-testid="stHorizontalBlock"] { flex-direction: column !important; gap: 1rem !important; }

    a.btn { display: block; margin: 7px 0; text-align: center; }
    .rule { margin: 2.2rem 0; }
}

/* ---------- MOBILE PEQUENO ---------- */

@media (max-width: 430px) {
    .block-container { padding-left: 0.85rem; padding-right: 0.85rem; }

    .hero-title { font-size: 37px; }
    .section-title-lg { font-size: 32px; }
    .section-title { font-size: 27px; }
    .lead { font-size: 15px; }

    .stats-grid { grid-template-columns: 1fr; }
    .stat-value { font-size: 34px; }

    .frame-tab { font-size: 9px; padding: 6px 8px; letter-spacing: 0.1em; }

    .cell, .card, .obj-card, .join-card, .film-cell { padding: 18px; }
    .cell-title { font-size: 21px; }
    .obj-title { font-size: 23px; }
    .film-title { font-size: 20px; }
}

/* ---------- ACESSIBILIDADE ---------- */

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { transition: none !important; }
    .cell:hover, .card:hover, .join-card:hover { transform: none; }
}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# ============================================================
# DADOS
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
    ("Direção Executiva", ["Direção-Geral", "Direção de Produção"]),
    ("Núcleo Criativo", ["Direção Criativa", "Direção de Personagens", "Direção de Dublagem"]),
    ("Arte e Produção Técnica", ["Direção de Arte", "Direção de Animação", "Direção de Pós-Produção"]),
    ("Gestão, Marketing e Governança", ["Direção de Marketing", "Direção Financeira", "Direção Jurídica"]),
]

CONSELHO = [
    ("Fiscalização", "Acompanha as decisões e a operação da organização, verificando se tudo segue o que foi acordado."),
    ("Governança", "Delibera sobre mudanças na estrutura e no direcionamento estratégico."),
    ("Transparência", "Mantém o alinhamento ético e a cultura institucional vivos."),
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
    ("07", "Publicação", "Marketing divulga somente o que passou pelo controle de qualidade."),
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

PARTICIPE = [
    ("Crie", "Contribua para projetos de animação, HQs e audiovisual de impacto real, dentro de um pipeline profissional."),
    ("Cresça", "Desenvolva suas habilidades em um ambiente prático e colaborativo, trocando conhecimento com outros criativos."),
    ("Conecte-se", "Faça parte de uma organização focada na construção de universos e fortalecimento de comunidade."),
]

# Links sem parâmetros de rastreamento (si, igsh, _r, _t).
CANAIS = {
    "YouTube": "https://youtube.com/@protocoloneoficial",
    "Instagram": "https://www.instagram.com/protocoloneofc",
    "TikTok": "https://www.tiktok.com/@protocoloneoficial",
}

EMAIL_CONTATO = "protocolonecontato@gmail.com"

PAGINAS = ["O Projeto", "Estrutura", "Objetivos", "Participe"]

# ============================================================
# HELPERS
# ============================================================


def render(html: str) -> None:
    """Renderiza HTML no Streamlit.

    O Markdown trata linhas indentadas com 4+ espaços como bloco de código
    e linhas em branco encerram blocos HTML. Por isso o HTML é compactado
    em uma única linha antes de ser enviado.
    """
    compact = " ".join(line.strip() for line in html.splitlines() if line.strip())
    st.markdown(compact, unsafe_allow_html=True)


def frame_tab(texto: str) -> None:
    render(f'<div class="frame-tab">{esc(texto)}</div>')


def spacer(small: bool = False) -> None:
    render(f'<div class="{"spacer-sm" if small else "spacer"}"></div>')


def rule() -> None:
    render('<div class="rule"></div>')


def grid(css_class: str, items: list[str]) -> None:
    render(f'<div class="{css_class}">{"".join(items)}</div>')


def link_button(label: str, url: str, ghost: bool = False) -> str:
    cls = "btn ghost" if ghost else "btn"
    return (
        f'<a class="{cls}" href="{esc(url, quote=True)}" '
        f'target="_blank" rel="noopener noreferrer">{esc(label)}</a>'
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    render(
        """
        <div class="sidebar-logo">PROTOCOL<br>ONE</div>
        <div class="sidebar-subtitle">ProtoCommunity</div>
        """
    )

    pagina = st.radio("Navegação", PAGINAS, label_visibility="collapsed", key="pagina")

    render('<div class="sidebar-label">Canais oficiais</div>')
    render(
        "".join(
            f'<a class="side-link" href="{esc(url, quote=True)}" '
            f'target="_blank" rel="noopener noreferrer">{esc(nome)}</a>'
            for nome, url in CANAIS.items()
        )
    )

    render('<div class="sidebar-label">Contato</div>')
    render(
        f'<a class="side-email" href="mailto:{esc(EMAIL_CONTATO, quote=True)}">'
        f"{esc(EMAIL_CONTATO)}</a>"
    )

# ============================================================
# PÁGINAS
# ============================================================


def pagina_projeto() -> None:
    frame_tab("Quadro 00 — Abertura")
    render('<div class="eyebrow">Protocol One / ProtoCommunity</div>')
    render('<div class="hero-title">Uma comunidade com disciplina de estúdio.</div>')
    render(
        """
        <div class="lead">
            O Protocol One é uma organização criativa voltada à construção
            de universos, personagens e produções audiovisuais, combinando
            criatividade, processos profissionais e desenvolvimento de talentos.
        </div>
        """
    )
    render('<div class="accent-line"></div>')

    stats = [
        (len(NUCLEOS), "Núcleos organizacionais"),
        (len(FRENTES), "Frentes criativas"),
        (len(CANAIS), "Canais oficiais"),
        (len(PIPELINE), "Etapas do pipeline"),
    ]
    grid(
        "stats-grid",
        [
            f'<div class="stat"><div class="stat-value">{valor:02d}</div>'
            f'<div class="stat-label">{esc(label)}</div></div>'
            for valor, label in stats
        ],
    )

    rule()
    frame_tab("Quadro 01 — O que é")
    render('<div class="section-title-lg">O que é a ProtoCommunity</div>')

    col1, col2 = st.columns(2)

    with col1:
        render(
            """
            <div class="body-copy">
                A ProtoCommunity funciona como uma estrutura colaborativa
                para transformar ideias em projetos criativos concretos.
                A proposta une diferentes especialidades em torno de um
                mesmo universo institucional.
            </div>
            <div class="body-copy">
                O objetivo é criar um ambiente onde produção artística,
                gestão, tecnologia, comunicação e estratégia possam trabalhar
                de maneira integrada.
            </div>
            """
        )

    with col2:
        chips = "".join(f'<span class="chip">{esc(f)}</span>' for f in FRENTES)
        render(f'<div class="chip-row">{chips}</div>')


def pagina_estrutura() -> None:
    frame_tab("Quadro 02 — Estrutura")
    render('<div class="section-title-lg">Oito núcleos. Um só rumo.</div>')
    render(
        """
        <div class="lead">
            A organização distribui suas responsabilidades em núcleos
            especializados, permitindo que cada área tenha uma função clara
            dentro do funcionamento geral do projeto.
        </div>
        """
    )
    spacer()

    grid(
        "grid-4",
        [
            f'<div class="cell"><div class="cell-number">{esc(n)}</div>'
            f'<div class="cell-title">{esc(t)}</div>'
            f'<div class="cell-text">{esc(d)}</div></div>'
            for n, t, d in NUCLEOS
        ],
    )

    rule()
    render('<div class="section-title">Estrutura de Liderança</div>')
    render(
        """
        <div class="body-copy">
            A liderança é organizada por frentes de responsabilidade,
            conectando direção estratégica, produção criativa, gestão,
            marketing e governança.
        </div>
        """
    )
    spacer(small=True)

    grid(
        "grid-4",
        [
            f'<div class="card"><div class="card-title">{esc(titulo)}</div>'
            f'<div class="role-row">'
            + "".join(f'<span class="badge">{esc(c)}</span>' for c in cargos)
            + "</div></div>"
            for titulo, cargos in LIDERANCA
        ],
    )

    rule()
    render('<div class="section-title">Conselho Consultivo e Deliberativo</div>')
    render(
        """
        <div class="body-copy">
            O Conselho atua como órgão colegiado de fiscalização,
            governança e deliberação sobre questões estruturais da
            organização, preservando coerência e transparência institucional.
        </div>
        """
    )
    render(
        """
        <div class="chip-row">
            <span class="pill">Governança</span>
            <span class="pill">Fiscalização</span>
            <span class="pill">Direcionamento estratégico</span>
        </div>
        """
    )
    spacer(small=True)

    grid(
        "grid-3",
        [
            f'<div class="cell"><div class="cell-title">{esc(t)}</div>'
            f'<div class="cell-text">{esc(d)}</div></div>'
            for t, d in CONSELHO
        ],
    )


def pagina_objetivos() -> None:
    frame_tab("Quadro 03 — Objetivos")
    render('<div class="section-title-lg">O que queremos construir.</div>')
    render(
        """
        <div class="lead">
            O Protocol One busca estabelecer uma estrutura sustentável,
            criativa e profissional, capaz de transformar produção
            independente em projetos de longo prazo.
        </div>
        """
    )
    spacer()

    grid(
        "grid-4",
        [
            f'<div class="obj-card"><div class="obj-number">{esc(n)}</div>'
            f'<div class="obj-title">{esc(t)}</div>'
            f'<div class="obj-text">{esc(d)}</div></div>'
            for n, t, d in OBJETIVOS
        ],
    )

    rule()
    render('<div class="section-title">Como uma ideia vira entrega</div>')
    render(
        """
        <div class="body-copy">
            O pipeline organiza o caminho entre conceito e publicação,
            reduzindo retrabalho e garantindo que cada produção passe
            pelas etapas necessárias antes de chegar ao público.
        </div>
        """
    )
    spacer(small=True)

    grid(
        "filmstrip",
        [
            f'<div class="film-cell"><div class="film-number">{esc(n)}</div>'
            f'<div class="film-title">{esc(t)}</div>'
            f'<div class="film-text">{esc(d)}</div></div>'
            for n, t, d in PIPELINE
        ],
    )


def pagina_participe() -> None:
    frame_tab("Quadro 04 — Participe")
    render('<div class="section-title-lg">Faça parte da ProtoCommunity</div>')
    render(
        """
        <div class="lead">
            O projeto foi pensado para reunir pessoas interessadas em criar,
            aprender e construir algo maior por meio de colaboração organizada.
        </div>
        """
    )
    spacer()

    grid(
        "grid-3",
        [
            f'<div class="join-card"><div class="join-symbol">◈</div>'
            f'<div class="join-title">{esc(t)}</div>'
            f'<div class="join-text">{esc(d)}</div></div>'
            for t, d in PARTICIPE
        ],
    )

    rule()
    render('<div class="section-title">Como entrar</div>')
    render(
        """
        <div class="body-copy">
            Acompanhe os canais oficiais ou fale diretamente com a equipe
            para saber como contribuir.
        </div>
        """
    )

    botoes = [link_button(nome, url) for nome, url in CANAIS.items()]
    botoes.append(
        f'<a class="btn ghost" href="mailto:{esc(EMAIL_CONTATO, quote=True)}">'
        "Enviar e-mail</a>"
    )
    render("".join(botoes))


# ============================================================
# ROTEAMENTO
# ============================================================

ROTAS = {
    "O Projeto": pagina_projeto,
    "Estrutura": pagina_estrutura,
    "Objetivos": pagina_objetivos,
    "Participe": pagina_participe,
}

ROTAS[pagina]()
