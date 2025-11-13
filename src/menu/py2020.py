import streamlit as st
import streamlit_antd_components as sac

def main():


    tabs = sac.tabs([
        sac.TabsItem(label='Resumo'),
        sac.TabsItem(label='Participantes'),
        sac.TabsItem(label='Tutoriais'),
        sac.TabsItem(label='Palestras'),
        sac.TabsItem(label='Feedback'),
        ], align='center', use_container_width=True)
    
    if tabs == 'Resumo':
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("Aqui você encontrará o resumo do evento Python Brasil 2020...LOREM IPSUM DOLOR SIT AMET, CONSETETUR SADIPSCING ELIT, SED DIAM NONUMY EIRMOD TEMPOR INVIDUNT UT LABORE ET DOLORE MAGNA ALIQUYAM ERAT, SED DIAM VOLUPTUA. AT VERO EOS ET ACCUSAMUS ET IUSTO ODIO DIGNISSIMOS DUCI MUS BLANDIT PRAESENTIUM VOLUPTATUM DELENITI ATQUE CORRUPTI QUOS DOLLORES ET QUAS MOL ESTIAS NOSTRUM ODIT FUGIT, SED QUIA CONSEQUUNTUR MAGNI DOLOR EUM FUGIAT VOLUPTAS SIT ASPERIORES REPELLENDUS AUTEM QUIA VOLUPTAS SIT ASPERIORES REPELLENDUS AUTEM QUIA VOLUPTAS SIT ASPERIORES REPELLENDUS AUTEM.")
        with col2:
            st.image("./assets/pybr2020-logo-colorido.png", 
                  caption="Logo oficial da Python Brasil 2020",
                  use_column_width=True,
                  output_format="auto"
        )
    
    elif tabs == 'Participantes':
        st.text("Aqui você encontrará informações sobre os participantes do evento.")

    elif tabs == 'Tutoriais':
        st.text("Aqui você encontrará informações sobre os tutoriais do evento.")

    elif tabs == 'Palestras':
        st.text("Aqui você encontrará informações sobre as palestras do evento.")

    elif tabs == 'Feedback':
        st.text("Aqui você encontrará informações sobre o feedback do evento.")