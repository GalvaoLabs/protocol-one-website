# Protocol One — Site Institucional

### Website desenvolvido por GalvaoLabs para a ProtoCommunity

Site institucional desenvolvido em **Python + Streamlit** para apresentar a estrutura, os objetivos, os processos e os canais oficiais da **ProtoCommunity / Protocol One**.

O projeto faz parte do portfólio de **Miguel Henrique** ([GalvaoLabs](https://github.com/GalvaoLabs)), sendo um trabalho de desenvolvimento web realizado para uma organização/projeto de terceiros.

> **Importante:** Miguel Henrique / GalvaoLabs é responsável pelo desenvolvimento técnico deste website. A GalvaoLabs não é proprietária nem responsável pela gestão do Protocol One / ProtoCommunity.

---

## Sobre o projeto

O website foi desenvolvido para transformar as informações institucionais da ProtoCommunity em uma interface web organizada, responsiva e visualmente consistente.

A aplicação apresenta:

- informações gerais sobre o projeto;
- estrutura organizacional;
- núcleos e áreas de atuação;
- estrutura de liderança;
- objetivos;
- pipeline de produção;
- formas de participação;
- canais oficiais e contato.

A interface foi construída com foco em **clareza, organização e identidade visual**, utilizando uma combinação de Python, Streamlit, HTML e CSS.

---

## Desenvolvimento

O projeto foi desenvolvido por **Miguel Henrique — GalvaoLabs** como uma aplicação web em Streamlit.

Entre os principais aspectos trabalhados estão:

- construção da interface em Streamlit;
- criação de componentes HTML reutilizáveis;
- estilização personalizada com CSS;
- layout responsivo;
- navegação entre páginas;
- organização dos dados em estruturas Python;
- adaptação da interface para desktop, tablet e mobile;
- integração da identidade visual do projeto;
- organização do código para facilitar futuras alterações.

---

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| **Python** | Linguagem principal |
| **Streamlit** | Framework da aplicação web |
| **HTML** | Estrutura e componentes da interface |
| **CSS** | Identidade visual e responsividade |
| **Google Fonts** | Tipografia |
| **Git / GitHub** | Versionamento e distribuição |

---

## Estrutura do projeto

```text
Protocol-One/
│
├── app.py
├── logo.png
├── requirements.txt
├── LICENSE
└── README.md
```

### Arquivos

**`app.py`**  
Arquivo principal da aplicação. Contém a estrutura do site, navegação, dados institucionais, componentes e estilos personalizados.

**`logo.png`**  
Logotipo utilizado na Sidebar da aplicação. O arquivo é um material relacionado à identidade visual do Protocol One / ProtoCommunity.

**`requirements.txt`**  
Lista de dependências necessárias para executar o projeto.

**`LICENSE`**  
Define os direitos e as restrições aplicáveis ao código desenvolvido neste repositório, além de esclarecer a propriedade dos materiais pertencentes ao Protocol One / ProtoCommunity.

**`README.md`**  
Documentação técnica e contextualização do projeto.

---

## Interface

A interface utiliza uma identidade visual baseada em:

- preto e tons neutros;
- âmbar como cor de destaque;
- tipografia **Big Shoulders Display**;
- tipografia **Space Grotesk**;
- cards e grids;
- Sidebar de navegação;
- efeitos de interação;
- layout responsivo;
- suporte a tema claro e escuro conforme as preferências do sistema.

---

## Estrutura do website

### O Projeto

Apresenta a proposta da ProtoCommunity, suas características e suas principais frentes criativas.

### Estrutura

Apresenta os núcleos organizacionais, a estrutura de liderança e o Conselho.

### Objetivos

Apresenta os objetivos institucionais e o processo utilizado para transformar uma ideia em uma produção.

### Participe

Apresenta formas de acompanhar os canais oficiais e entrar em contato com a organização.

---

## Pipeline apresentado

O website apresenta um pipeline de produção dividido em **7 etapas**:

```text
01 — Ideia e conceito
02 — Roteiro
03 — Storyboard
04 — Animatic
05 — Animação e som
06 — Controle de qualidade
07 — Publicação
```

O pipeline é apresentado como parte do conteúdo institucional do website.

---

## Rodar localmente

Clone o repositório e instale as dependências:

```bash
git clone SEU_REPOSITORIO
cd Protocol-One
pip install -r requirements.txt
```

Depois, execute:

```bash
streamlit run app.py
```

A aplicação ficará disponível localmente em:

```text
http://localhost:8501
```

---

## Hospedagem

O projeto pode ser hospedado utilizando serviços compatíveis com aplicações Streamlit.

### Streamlit Community Cloud

O Streamlit Community Cloud é uma opção simples para publicar aplicações Streamlit diretamente a partir de um repositório GitHub.

Fluxo básico:

1. Publicar o projeto no GitHub;
2. Acessar o Streamlit Community Cloud;
3. Conectar a conta do GitHub;
4. Selecionar o repositório;
5. Selecionar `app.py` como arquivo principal;
6. Realizar o deploy.

Após a publicação, alterações enviadas ao repositório podem ser utilizadas para atualizar a aplicação.

---

## Editando o conteúdo

Grande parte do conteúdo institucional está organizada em listas Python no início do arquivo `app.py`.

Entre as principais estruturas estão:

```python
NUCLEOS
LIDERANCA
CONSELHO
OBJETIVOS
PIPELINE
FRENTES
CANAIS
```

Isso permite alterar nomes, descrições, cargos, etapas e canais sem precisar modificar a estrutura principal da aplicação.

Por exemplo:

```python
PIPELINE = [
    (
        "01",
        "Ideia e conceito",
        "Descrição da etapa.",
    ),
]
```

A estrutura pode ser modificada conforme as necessidades do projeto.

---

## Responsabilidade e autoria

Este repositório reúne o **desenvolvimento técnico do website** e materiais necessários para sua apresentação e funcionamento.

### Miguel Henrique / GalvaoLabs

Responsável pelo **desenvolvimento, implementação e estrutura técnica** da aplicação presente neste repositório.

O código-fonte desenvolvido especificamente para a aplicação é de autoria de **Miguel Henrique / GalvaoLabs**, conforme os termos estabelecidos na [LICENSE](LICENSE).

### Protocol One / ProtoCommunity

O **Protocol One / ProtoCommunity** é o projeto apresentado pelo website.

Seu nome, marca, logotipos, textos institucionais, informações organizacionais, conceitos e demais materiais criativos ou institucionais relacionados não são propriedade de Miguel Henrique ou da GalvaoLabs.

Esses materiais permanecem pertencentes aos seus respectivos titulares e não são licenciados pela licença deste repositório.

> A presença de materiais do Protocol One / ProtoCommunity neste repositório não concede autorização para sua reprodução, modificação ou redistribuição.

---

## Licença

O **código-fonte desenvolvido por Miguel Henrique / GalvaoLabs** está sujeito aos termos definidos no arquivo [LICENSE](LICENSE).

Materiais pertencentes ao Protocol One / ProtoCommunity, incluindo sua marca, identidade visual e conteúdo institucional, permanecem sujeitos aos direitos de seus respectivos titulares.

Consulte a [LICENSE](LICENSE) para obter as condições completas.

---

## GalvaoLabs

A **GalvaoLabs** é a identidade utilizada por Miguel Henrique para reunir projetos, estudos e experimentos relacionados a tecnologia, programação e desenvolvimento.

Conheça outros projetos no GitHub:

**[github.com/GalvaoLabs](https://github.com/GalvaoLabs)**

**Tech • Estudos • Evolução**

> *Só sei que nada sei.*

---

## Status

**Projeto de portfólio — Em desenvolvimento.**

O projeto pode receber alterações futuras de interface, conteúdo, responsividade e funcionalidades conforme as necessidades do website.

---

<div align="center">

### GALVAOLABS

**Tech • Estudos • Evolução**

</div>
