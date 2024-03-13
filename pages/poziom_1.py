import streamlit as st

try:
    if st.session_state.q0 == None:
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')

    else:
        st.write('No i świetnie o to chodzi, poza zadaniami zamkniętymi, których ogólnie będzie mało, przewiduje zadania otwarte, w których odpowiedź to JEDNO SŁOWO, ew. format, który będę przedstawiać przy konkretnym pytaniu. Żeby zatwierdzić odpowiedź musisz wcisnąć enter')
        st.write('Przykładowo:')
        q1 = st.text_input('Kto łączy mnie, Ciebie i Bartka Szyję?')

        if q1.lower().strip() == 'dukaj':
            st.session_state.q1 = 'dukaj'
            st.write('Poprawna odpowiedź! Możesz przejść do następnej podstrony')

        st.write('PS. Jbc, to przewiduje czasem jakieś podpowiedzi, które pojawią się po naciśnięciu przycisku takiego jak ten:')

        hint_0 = st.button('Podpowiedź')

        if hint_0:
            st.write('Nikt z nas nie zna go osobiście')
        
        hint_1 = st.button('Duża podpowiedź')
        if hint_1:
            st.write('Pisarz :)')
        
        st.write('Ofc chodzi o to żebyś rozwiązała ten quiz, ale żeby nie było za łatwo, to po poprawne odpowiedzi zapraszam bezpośrednio do mnie z pytaniami')


        secret = st.button('Ciekawostka #1')

        if secret:
            st.write('Ciekawostka developerska: dzięki pomocy funkcji strip i lower nie ma znaczenia ile spacji wpiszesz przed/po danym słowie ani jakich wielkości liter użyjesz: program sam wprowadzi odpowiednie korekty! Ale na wszelki wypadek staraj się unikać nadmiercnyh spacji i dużych liter bo mogłem gdzieś zapomnieć xDDD')

        wine = st.button('Ciekawostka na temat wina')

        if wine:
            st.write('Skoro jesteśmy na stronie, na której wspominam Bartka to chciałem też dać znać, że brał on czynny udział w wyborze wina dla Ciebie. Polecił Ukraińskie lub Gruzińskie wino ze szczepu Muscat. Po wizycie w trzech sklepach i czytaniu wielu etykiet najbliższe co znalazłem to Muscat z Mołdawii. Mołdawia sąsiaduje z Ukrainą więc jest nieżle, ok?')

except AttributeError:
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')
