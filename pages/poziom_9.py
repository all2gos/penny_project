import streamlit as st

try:

    if (st.session_state.q8).lower().strip() != 'az':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')
        st.write('I swoją drogą to przy okazji rewelacyjne wyjście na wypadek gdyby coś Ci się wywaliło, wówczas nie klikasz wszystkiego od początku tylko wpisz tutaj odpowiedź z poprzedniej strony, żeby odrazu odblokować treść tej strony')
        (st.session_state.q8) = st.text_input('Jeżeli coś się wywaliło na stronie, to wpisz tutaj odpowiedź na pytanie z poprzedniej strony').lower().strip()


    if (st.session_state.q8).lower().strip() == 'az':

        st.write('No i tak rozpoczął się kolejny semestr na tym samym roku dla nas. Nie wiem jak Tobie, ale mi studiowanie na UPWr bardzo kojarzy się z jednym miejscem, czy wiesz co mam myśli?')

        st.session_state.q9 = st.text_input('Jakie miejsce najbardziej kojarzy mi się z Tobą i studiowaniem na UPWr?')

        if (st.session_state.q9).lower().strip() == 'wuwa':
            st.write('Oj tak, zawitalismy w tej kawiarni mnóstwo razy a jeszcze dużo więcej wspólnych kawek w tym miejscu przed nami. WUWA to również dla mnie miejsce dość symboliczne, kojarzące z kilkoma ważnymi wydarzeniami, które rzutują na losy naszej relacji')

            st.write('''

            Bo to w Wuwie pierwsze razy spędzaliśmy czas we dwójkę, a jednak wiadomo, że introwertyk zachowuje się zupełnie inaczej w takiej konfiguracji,
                    
            to w Wuwie dochodziłem do wniosku, że mało jest osób, z którymi rozmawia mi się tak dobrze i tak nieskrępowanie jak z Tobą,
                    
            to w Wuwie, co wydało mi się na tamtem czas bardzo dziwne, gdy Iwona powiedziała, że jestem do niej aseksualny Ty zamiast coś powiedzieć bardzo się zawstydziłaś co dało mi duże pole do overthinkowego popisu,
                    
            to w Wuwie słuchałaś głosówki od Janka, w której przed jego dziewczyną nazwał Cię moją dziewczyną (i nie planowałem tego fortela, naprawdę xD) a Ty zamiast mnie zjebać nie powiedziałaś niczego.
                    
            Nom, większą część naszej wspólnej historii można opowiedzieć nie ruszając się z Wuwy
                    
            Lecisz dalej
                    
    ''') 

except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')