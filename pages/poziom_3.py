import streamlit as st


try:
    if st.session_state.q2 != '28-02-2023':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')
        st.write('I swoją drogą to przy okazji rewelacyjne wyjście na wypadek gdyby coś Ci się wywaliło, wówczas nie klikasz wszystkiego od początku tylko wpisz tutaj odpowiedź z poprzedniej strony, żeby odrazu odblokować treść tej strony')
        st.session_state.q2 = st.text_input('Jeżeli coś się wywaliło na stronie, to wpisz tutaj odpowiedź na pytanie z poprzedniej strony')



    if st.session_state.q2 == '28-02-2023':
        st.write('Nie będę tutaj jakoś szczególnie ukrywać, że od samego początku byłaś osobą, która nie tylko zwracała moją uwagę, ale też sprawiała na mnie bardzo duże wrażenie. Niech dowodem na to będzie kolejne pytanie')
        
        st.session_state.q3 = st.text_input('Podaj kolor górnego elementu garderoby, który miałaś na sobie pierwszego dnia zajęć na 1 semestrze Bioinformatics')

        hint_0 = st.button('Podpowiedź')

        if hint_0:
            st.write('Nie jest to kolor, który zakładasz często. Ogranicz się ogólnie do bardzo podstawowych kolorów')
        
        hint_1 = st.button('Duża podpowiedź')
        if hint_1:
            st.write('Gdybym miał dowód w latach 90" to ten kolor by został do niego wpisany')

        if (st.session_state.q3).lower().strip() == 'zielony':
            st.write('Tak! Nie jestem zbyt biegły w opisy odzieżowe, ale było to coś w stylu ciemnozielonej koszuli, a żeby udowodnić, że mam ejdetyczną pamięć to dodam, że poza tym miałaś wtedy na sobie jasnoniebieskie jeansy i jakieś czarne buty na obcasie. Lecisz dalej')



except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')
