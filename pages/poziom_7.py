import streamlit as st

try:

    if (st.session_state.q6).lower().strip() != 'wisniowka':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')
        st.write('I swoją drogą to przy okazji rewelacyjne wyjście na wypadek gdyby coś Ci się wywaliło, wówczas nie klikasz wszystkiego od początku tylko wpisz tutaj odpowiedź z poprzedniej strony, żeby odrazu odblokować treść tej strony')
        st.session_state.q6 = st.text_input('Jeżeli coś się wywaliło na stronie, to wpisz tutaj odpowiedź na pytanie z poprzedniej strony').lower().strip()


    if (st.session_state.q6).lower().strip() == 'wisniowka':

        st.write('''
    szczerze mówiąc to totalnie nie pamiętałem, że te wydarzenia były najpierw, nie pamiętałem też kolejnej dość ważnej sytuacji, która miała miejsce 25 lipca: postanowiłem głównie zainspirowany tym, że przeczytałem Myśli Nieuczesane wysłać Ci aforyzm,
                na co zareagowałaś bardzo entuzjastycznie i zażyczyłaś sobie aforyzmu codziennie. Ja totalnie szczerze uznałem to za idealny pretekst żeby móc do Ciebie często pisać xDD. No i teraz w końcu, konkretnie 27 lipca dochodzimy do dnia,
                który zapamiętałem jako ten, w którym nasza znajomość weszła na nowy poziom. Mam wrażenie, że właśnie od tego dnia nasz kontakt bardzo się zintensyfikował. Gdybym miał sztywno postawić granice między kolejnymi etapami: pierwszą postawiłbym 28 lutego, a drugą 27 lipca. Czy pamietasz, albo inaczej, czy domyślasz się jakie wydarzenie mam na myśli?''')
        

        st.session_state.q7 = st.radio('Co się wydarzyło 27 lipca, a co sprawiło, że w mojej opinii nastąpił wtedy przełom w naszej znajomości?',('Puste pole','Byłem na weselu Dusz','Byłaś na randce'))

        if st.session_state.q7 != 'Puste pole':
            st.write('Prawda jest taka, że obie te sytuacje miały miejsce 27 lipca. Nie pamiętam dużo z tego wesela. Przypomnę, że ograłem wtedy kolesia w szachy będąc najebanym albo nawoływałem alpaki, więc miałaś silną konkurencję w kategorii most memorial moments a jednak się załapałaś bez większego kłopotu xD')


except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')