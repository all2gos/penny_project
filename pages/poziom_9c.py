import streamlit as st



try:
    if st.session_state.q11 != 'Wysłałaś mi podcast z Draganem i Czajką i pogadaliśmy trochę o AI':
        st.write('Jak już może zauważyłaś to po lewej stronie znajduje się nawigator zakładek. I juz pewnie myślisz, że można to jakoś obejść i sobie wbić do ostatniej strony czy coś, ale nic z tego, bo tak długo póki odpowiedź ze strony poprzedniej nie zostanie wpisana poprawnie, tak długo treść tych podstron pozostanie niewidoczna!')
        st.write('--------------')

    if st.session_state.q11 == 'Wysłałaś mi podcast z Draganem i Czajką i pogadaliśmy trochę o AI':

        st.write('Brawo dotarłaś do końca naszej wspaniałem zabawy. Nie chciałem tego jakoś przesadnie przedłużać, bo to też nie o to chodzi. Mam nadzieję, że fajnie się bawiłaś wspominając nasze początki i wspólne miłe chwile.')

        st.write('Kończę ten quiz na poziomie 9c')

        dev = st.button('Ciekawostka')
        if dev:
            st.write('Ciekawostka deweloperska: po osiągnięciu poziomu 9 nie mogłem wpisać poziomu 10, bo pliki ze względu na numery są inaczej sortowane i wówczas 10 poziom by się znajdował między poziomem 1 i 2) Nie planowałem skończyć na poziomie 9c, ale w sumie spoko, że jest tu trochę symboliki. Skoro jednak tak dobrze mi idzie nie zbieganie do tego tematu, to nie będę tego bardziej rozwijać xd')

        st.write('Cieszę się, że pojawiłaś się w moim życiu, że jesteś osobą, dla której chce mi się pisać stronę o naszej relacji. Zresztą chyba nie jest dla Ciebie dużym zaskoczeniem jak ważna dla mnie jesteś, bo na swój pokrętny sposób (mam nadzieję) daję Ci o tym regularnie znać i liczę, że jesteś tego świadoma')

        st.write('Mam nadzieję, że nasza relacja będzie się wciąż rozwijać, żebym na przyszły rok miał jeszcze więcej materiału źródłowego i mógł zrealizować fajniejsze pomysły')

        st.write('Mam nadzieję, że nie przeszkadzała Ci dość biedna warstwa wizualna całego przedsięwzięcia, ale ani ze mnie esteta, ani frontendowiec więc starałem się nadrobić co mogłem gadaniem xD')

        st.write('Nie wiem czy mogę Ci czegoś szczególnego życzyć, jak wiesz nie specjalnie sympatyzuję z tym formalizmem. Ale gdybym miał zrobić to szybko acz konkretnie, to życzyłbym Ci radości z życia i poczucia spełnienia: nieważne gdzie, z kim i w jakiej formie miałyby one nadejść')

        st.write('Widzimy się przy następnej okazji, albo przy braku okazji, albo za trzy okazje, ze mną to nigdy nie wiadomo Paaaaaaaa <3')



except AttributeError:
    
    st.write('Jeżeli widzisz ten komunikat to przejdż do katalogu domowego i wróć na tę stronę')