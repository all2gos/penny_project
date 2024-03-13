import streamlit as st

try:

    if st.session_state.q4 != 'Ty':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')
        st.write('I swoją drogą to przy okazji rewelacyjne wyjście na wypadek gdyby coś Ci się wywaliło, wówczas nie klikasz wszystkiego od początku tylko wpisz tutaj odpowiedź z poprzedniej strony, żeby odrazu odblokować treść tej strony')
        st.session_state.q4 = st.text_input('Jeżeli coś się wywaliło na stronie, to wpisz tutaj odpowiedź na pytanie z poprzedniej strony')

    if st.session_state.q4 == 'Ty':

        st.session_state.q5 = st.text_input('Teraz będzie szybciutko, ciach pach pytanie i lecimy dalej. Podaj nazwę miejsca do jakiego poszliśmy pierwszy raz "nieformalnie"')


        h0 = st.button('Podpowiedź')
        
        if h0:
            st.write('Masz obsesję na punkcie tego miejsca')

        h1 = st.button('Duża podpowiedź')

        if h1:
            st.write('Cukiernia na Gaju')

        if (st.session_state.q5).lower().strip() == 'gigi':
            st.write('Tak! Był to jakiś wiosenny czwartek, w którym Bartek wypuścił nas bardzo wcześnie z zajęć. Przejdź do następnej podstrony')


except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')

