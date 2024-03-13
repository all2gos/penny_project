import streamlit as st

try:
    
    if st.session_state.q10 not in ['Opcja 1','Opcja 2','Opcja 3','Opcja 4']:
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')

    if st.session_state.q10 in ['Opcja 1','Opcja 2','Opcja 3','Opcja 4']:

        st.write('Wróćmy na chwilę do początków naszej relacji. Jak myślisz jaki jest pierwszy non-study related temat, który poruszyliśmy na komunikatorze tekstowym?')

        st.session_state.q11 = st.radio('Odpowiedz na powyższe pytanie:',('Puste pole','Wysłałem Ci zdjęcie znitrowanej kawy i ogólnie pogadaliśmy w związku z tym o kawie','Wysłałaś mi utwór Edyty Górniak i zaczęliśmy gadać ogólnie o naszych gustach muzycznych', 'Wysłałaś mi podcast z Draganem i Czajką i pogadaliśmy trochę o AI', 'Gadaliśmy na temat Eurowizji głównie skupiając się na jakości występów Blanki'))

        if st.session_state.q11 == 'Wysłałaś mi podcast z Draganem i Czajką i pogadaliśmy trochę o AI':
            st.write('Poprawna odpowiedź, która swoja zszokowała mnie tak bardzo, że aż musiałem ją tutaj zamieścić. No i swoją drogą dość ciekawy wydał mi się fakt, że całkiem niedawno mieliśmy z tego powtórkę, czyli znowu wysłałaś mi podcast z Tomkiem Czajką, tym razem na Kanale Zero. Lecisz dalej')

        else:
            st.write('Nie jest to poprawna odpowiedź')
except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')




