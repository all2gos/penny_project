import streamlit as st

try:

    if (st.session_state.q5) != 'gigi':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')
        st.write('I swoją drogą to przy okazji rewelacyjne wyjście na wypadek gdyby coś Ci się wywaliło, wówczas nie klikasz wszystkiego od początku tylko wpisz tutaj odpowiedź z poprzedniej strony, żeby odrazu odblokować treść tej strony')
        st.session_state.q5 = st.text_input('Jeżeli coś się wywaliło na stronie, to wpisz tutaj odpowiedź na pytanie z poprzedniej strony').lower().strip()

    if (st.session_state.q5).lower().strip() == 'gigi':

        st.write('Jak już wspomniałem rozkwit naszej relacji nie przypadał na okres studiowania na PWr dlatego zbliżamy się w sumie do końca tego etapu. Jak powinnas pamiętać nasza relacja internetowo rozwijała się na początku praktycznie wyłącznie na IG. Specjalnie na potrzeby tej strony cofnąłem się do początku naszych rozmów, żeby zobaczyć jak to tam wyglądało.')
        st.write('No i muszę przyznać, że zapamiętałem to trochę inaczej. Bo tak to wyglądało naprawdę:')
        st.write('''
                
                10 kwietnia wysyłasz do mnie pierwszą wiadomość na ig z komenatrzem odnośnie mojego wspinu na most

                później, 26 maja (czyli już po tym jak jebnąłem studiami) zaczepiam Cię gdy dodajesz na relację zdjęcie kawki ze swojego nowego ekspresu,

                15 lipca wrzucasz relację, którą bardzo dobrze pamiętam ale nie mam żadnego screena: przedstawiała ona kawałek Ciebie, ale na pierwszy plan wdzierał się kieliszek z jakimś winem, do którego przykleiła się podkładka, dodałaś wówczas napis w stylu "napój optymalny, podkładka nie",
                no i tym razem to już mega mocno poczułem się wywołany do tablicy i chyba jestem gotowy powiedzieć, że to była nasza pierwsza dłuższa "nieformalna" rozmowa, gadałaś trochę o robieniu przetworów z truskawek, ale też w jej wyniku pojawiła się propozycja, że mam dla Ciebie zrobić kawę z pewnym specyficznym dodatkiem...
    ''')
        
        st.session_state.q6 = st.text_input('Jaki nietypowy dodatek chciałaś żebym dodał do kawy tamtego dnia?')

        
        h0 = st.button('Podpowiedź')

        if h0:
            st.write('Był to alkohol i nie używaj polskich znaków jbc')

        if (st.session_state.q6).lower().strip() == 'wisniowka':
            st.write('Tak! Do następnej podstrony zapraszam')

    
except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')





