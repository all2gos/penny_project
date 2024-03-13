import streamlit as st




try:
    if st.session_state.q1 != 'dukaj':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')
        st.write('I swoją drogą to przy okazji rewelacyjne wyjście na wypadek gdyby coś Ci się wywaliło, wówczas nie klikasz wszystkiego od początku tylko wpisz tutaj odpowiedź z poprzedniej strony, żeby odrazu odblokować treść tej strony')
        st.session_state.q1 = st.text_input('Wpisz tutaj odpowiedź na pytanie z poprzedniej strony').lower().strip()

    if (st.session_state.q1).lower().strip() == 'dukaj':
        st.write('''
                Ok możemy uznać, że to faktyczny początek naszej zabawy. Jak nietrudno się domyślić myślałem bardzo dużo o tym co się działo w naszej relacji przez ostatni ponad rok (i musiałem grać głupa przy serniczku udając, że nie jestem na świezo z tymi wszystkimi wydarzeniami xDDD) i doszedłem do wniosku, że możemy wyróźnić w niej trzy główne wydarzenia, które w pewien
                sposób wyznaczają ramy pewnych etapów. Te etapy to:
                1) semestr studiów na PWr
                2) dość spontaniczy rozwój naszej znajomości (wrócimy do tego tematu szerzej)
                3) studia na UPWr

                Czas na pytanie!''')
        st.session_state.q2= st.text_input('Podaj datę naszego pierwszego spotkania na PWr (spoiler, to nie jest 1-03-2023 (przy okazji podałem poprawny format odpowiedzi))')

        if st.session_state.q2 == '28-02-2023':
            st.write('Tak! Nasze pierwsze zajęcia odbyły się we wtorek i był to Bioprocess Project. Przejdź do następnej podstrony')
        else:
            st.write('Niestety to nie jest dobra odpowiedź, sprawdź ew. czy użyłaś dobrego formatu typu DD-MM-RRRR')

except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')
    
