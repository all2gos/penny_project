import streamlit as st
from PIL import Image

try:
   

    if st.session_state.q9 != 'wuwa':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')
        st.write('I swoją drogą to przy okazji rewelacyjne wyjście na wypadek gdyby coś Ci się wywaliło, wówczas nie klikasz wszystkiego od początku tylko wpisz tutaj odpowiedź z poprzedniej strony, żeby odrazu odblokować treść tej strony')
        (st.session_state.q9) = st.text_input('Jeżeli coś się wywaliło na stronie, to wpisz tutaj odpowiedź na pytanie z poprzedniej strony').lower().strip()

    if st.session_state.q9 == 'wuwa':

        st.write('Czy Ty zdajesz sobie sprawę, że my nie mamy żadnego wspólnego zdjęcia? xD Albo inaczej: ja nie dysponuję takowym. Postawiłem sobie to pytanie przed chwilą i jeżeli dysponujesz materiałem wizualnym na którym znajdujemy się oboje to możesz mi dać znać, bo moje archiwa są w tym temacie puste')

        st.write('A jak już jesteśmy przy zdjęciach, to możesz spróbować zgadnąć, na którym z tych zdjęć moim zdaniem wyglądasz najładniej:')

        image1 = Image.open('pages/karo1.jpg')
        image2 = Image.open('pages/karo2.jpg')
        image3 = Image.open('pages/karo3.jpg')
        image4 = Image.open('pages/karo4.jpg')


        st.image(image1, caption='Karolina w opcji nr1', width=400)
        st.image(image2, caption = 'Karolina w opcji nr2', width=400)
        st.image(image3, caption = 'Karolina w opcji nr3', width=400)
        st.image(image4, caption='Karolina w opcji nr4', width=400)

        st.session_state.q10 = st.radio('Na którym zdjęciu wyglądasz najbardziej zjawiskowo?',('Puste pole','Opcja 1','Opcja 2','Opcja 3','Opcja 4'))

        if st.session_state.q10 != 'Puste pole':
            st.write('Dokładnie tak, Ty to jednak znasz mnie na wylot. Lecisz dalej')

            s = st.button('Sekretna Prawda')

            if s:
                st.write('Wiesz o tym, że nieważne co byś zaznaczyła to odpowiedź była by prawidłowa, bo zawsze wyglądasz zjawiskowo, prawda?')

except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')

        