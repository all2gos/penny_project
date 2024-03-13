import streamlit as st
from PIL import Image

try:


    if st.session_state.q3 != 'zielony':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')
        st.write('I swoją drogą to przy okazji rewelacyjne wyjście na wypadek gdyby coś Ci się wywaliło, wówczas nie klikasz wszystkiego od początku tylko wpisz tutaj odpowiedź z poprzedniej strony, żeby odrazu odblokować treść tej strony')
        st.session_state.q3 = st.text_input('Jeżeli coś się wywaliło na stronie, to wpisz tutaj odpowiedź na pytanie z poprzedniej strony')

    if st.session_state.q3 == 'zielony':

        st.write('Z mojej perspektywy nasza znajomość na początku nie zwiastowała faktu, że będę pisał o niej quiz na Twoje urodziny. Praktycznie przez cały okres mojego studiowania Bioinformatics nie wyszliśmy specjalnie poza gadanie między zajęciami. Ale 26.03.2023 przeszliśmy na kolejny "etap". Pierwszy raz wymieniliśmy ze sobą wiadomość na msg! Pytanie:')

        st.session_state.q4 = st.radio('Kto z nas wysłał do tej drugiej osoby wiadomość jako pierwszy?',('Puste pole', 'Ty','ja'))

        if st.session_state.q4 == 'Ty':
            st.write('Tak! Ciekawe czy pamiętasz czego dotyczyła. Możesz o tym teraz pomyśleć. Jeżeli będziesz miała swój typ to naciśnij przycisk, żeby dowiedzieć się czy masz rację. Jeżeli to zrobisz to przejdź do następnej podstrony')
            b = st.button('Odpowiedź')
            if b:
                st.write('Miałaś pytania do pierwszego sprawozdania od kędzierskiego')

                st.write('Swoją drogą to bardzo zabawne jak te wiadomości wyglądały na początku')

                image1 = Image.open('C:\\Users\\stott\\Desktop\\PUK\\pages\\ss1.png')
                image2 = Image.open('C:\\Users\\stott\\Desktop\\PUK\\pages\\ss2.png')
                image3 = Image.open('C:\\Users\\stott\\Desktop\\PUK\\pages\\ss3.png')
                image4 = Image.open('C:\\Users\\stott\\Desktop\\PUK\\pages\\ss4.png')
                image5 = Image.open('C:\\Users\\stott\\Desktop\\PUK\\pages\\ss5.png')

                st.image(image1)
                st.image(image2)
                st.image(image3)
                st.image(image4)
                st.image(image5)

                st.write('Tak właśnie wyglądały nasze początki xDDD. Jeszcze z ciekawostek to znalazłem np. coś takiego')

                zodiak = Image.open('C:\\Users\\stott\\Desktop\\PUK\\pages\\zodiak.png')
                st.image(zodiak)
                st.write('Więc mówiłem to conajmniej dwukrotnie!')
                st.write('Zapraszam na kolejną podstronę')

        elif st.session_state.q4 == 'ja':
            st.write('No daj spokój, ja jestem okropną pizdą na początku znajomości')


    

except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')