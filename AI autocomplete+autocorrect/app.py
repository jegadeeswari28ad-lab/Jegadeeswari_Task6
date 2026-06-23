import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from model import (
    sentence_autocomplete,
    autocorrect,
    top_words,
    vocabulary_size,
    total_words
)

st.set_page_config(
    page_title="Smart AI Autocomplete & Autocorrect",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Smart AI Autocomplete & Autocorrect System")

st.markdown(
    """
    Dataset: Brown Corpus (NLTK)

    Features:
    - Autocomplete
    - Autocorrect
    - NLP Analytics Dashboard
    """
)

# ==================================
# USER INPUT
# ==================================

text = st.text_input(
    "Type a word or sentence"
)

if text:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🔮 Autocomplete Suggestions")

        suggestions = sentence_autocomplete(text)

        if suggestions:

            for s in suggestions:
                st.success(s)

        else:
            st.warning("No predictions found")

    with col2:

        st.subheader("✏️ Autocorrect Suggestions")

        corrections = autocorrect(text.split()[-1])

        if corrections:

            for c in corrections:
                st.info(c)

        else:
            st.warning("No correction found")


# ==================================
# ANALYTICS DASHBOARD
# ==================================

st.divider()

st.header("📊 NLP Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Vocabulary Size",
        vocabulary_size()
    )

with col2:

    st.metric(
        "Total Words",
        total_words()
    )

# ==================================
# TOP WORDS
# ==================================

st.subheader("📈 Top 20 Most Frequent Words")

top = top_words(20)

df = pd.DataFrame(
    top,
    columns=["Word", "Frequency"]
)

st.dataframe(df)

# ==================================
# BAR CHART
# ==================================

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    df["Word"],
    df["Frequency"]
)

ax.set_title("Top Word Frequencies")
ax.tick_params(axis="x", rotation=45)

st.pyplot(fig)