import streamlit as st

try:

    if st.session_state.q7 == 'Puste pole':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')
        st.write('I swoją drogą to przy okazji rewelacyjne wyjście na wypadek gdyby coś Ci się wywaliło, wówczas nie klikasz wszystkiego od początku tylko wpisz tutaj odpowiedź z poprzedniej strony, żeby odrazu odblokować treść tej strony')
        st.session_state.q7 = st.radio('Co się wydarzyło 27 lipca, a co sprawiło, że w mojej opinii nastąpił wtedy przełom w naszej znajomości?',('Puste pole','Byłem na weselu Dusz','Byłaś na randce'))

    if st.session_state.q7 != 'Puste pole':
        st.write('No i cytując klasyka: poszły konie po betonie. Od tamego momentu zaczęliśmy ze sobą pisać codziennie, często po nocach wysyłaliśmy sobie piosenki. Ja Ci pokazywałem Łonę, Ty mi Lanę i no tak to sobie trwało')
        st.write('To był jeszcze okres kiedy pracowałem w korporacji i to był też okres, w którym zacząłem zadawać sobie pytania czy przypadkiem nie chciałbym stworzyć z Tobą jeszcze bliższej relacji no i oczywiście zastanawiałem się co Tobie chodzi w tej kwestii po głowie')
        st.write('W sumie to pozwolę sobie w tym miejscu na moment szczególnej otwartości i przyznam, że mocno zastanawiałem się czy nasza relacja zyska czy straci w momencie, w którym trafimy razem na rok na UPWr (z powodów, które zostały już między nami omówione)')

        st.write('Ostatni na ten moment etap naszej znajomości rozpoczął się 1 października 2023 roku, kiedy znowu znaleźliśmy się w tej samej sali wykładowej')

        st.session_state.q8 = st.text_input('Podaj nazwę sali, w której widzieliśmy się pierwszy raz na UPWr')


        h0 = st.button('Podpowiedź')

        if h0:
            st.write('Nie mam tutaj na myśli sali, w której odbywały się pierwsze zajęcia. Używaj małych liter jbc')

        
        if (st.session_state.q8).lower().strip() == 'az':
            st.write('Dokładnie, inauguracja roku akademickiego to pierwsza rzecz, w której wspólnie uczestniczyliśmy na UPWr. Możesz przejść dalej')


except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')

    