import streamlit as st

# --- PAGE SETUP ---
page_1 = st.Page(
    "views/page_1.py",
    title="Exemplo MongoDB",
    icon=":material/savings:",
    default=True
)

page_2 = st.Page(
    "views/page_2.py",
    title="Página 2",
    icon=":material/settings:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Páginas": [page_1]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")

# --- RUN NAVIGATION ---
pg.run()
