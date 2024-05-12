import streamlit as st
import streamlit_shadcn_ui as ui
import matplotlib.pyplot as plt

from src.services.classifier import classify_text


def start_app():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.set_page_config(
        page_title="Generated Text Detection",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown("# :orange[Machine Generated Text Detection Service [Автомат 5]]")
    st.empty().markdown("&nbsp;")

    st.empty().markdown('''### {}'''.format("Ввод данных"),
                        help='Choose either 1 or 2 but not both. If both are selected 1 will be used.')
    option = st.radio(
        label='Выберите способ ввода',
        options=[
            'URL-ссылка',
            'PDF-файл',
            'Текстовое описание'
        ]
    )

    if option == 'PDF-файл':
        input_media = st.file_uploader(label='', type='pdf')

    else:
        mssg = "Прикрепите текст или URL-ссылку"
        input_media = st.text_input(
            mssg,
            label_visibility='visible'
        )
        if input_media is not None and "https" in input_media:
            input_url = input_media

    load_button = ui.button(text="Классифицировать",
                            key="load_button",
                            className="bg-orange-500 text-white")

    if load_button:
        st.empty().markdown('''### {}'''.format("Результат классификации"),
                            help='Choose either 1 or 2 but not both. If both are selected 1 will be used.')
        classify_data = classify_text(input_media)[0]
        classify_data = {data["label"]: data["score"] for data in classify_data}

        cols = st.columns(2)
        with cols[0]:
            labels = 'HUMAN', 'LLM-GENERATED'
            sizes = [classify_data["LABEL_1"], classify_data["LABEL_0"]]

            plt.figure(figsize=(8, 6), dpi=80)
            plt.pie(sizes, labels=labels, autopct='%1.1f%%')

            st.pyplot()
