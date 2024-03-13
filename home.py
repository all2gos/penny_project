import streamlit as st

st.set_page_config(page_title='Penny_Project', page_icon=':eyes:', layout='wide')


st.session_state.q0 = None
st.session_state.q1 = None
st.session_state.q2 = None
st.session_state.q3 = None
st.session_state.q4 = None
st.session_state.q5 = None
st.session_state.q6 = None
st.session_state.q7 = None
st.session_state.q8 = None
st.session_state.q9 = None
st.session_state.q10= None
st.session_state.q11 = None



st.write('No hej. Słuchaj co tu dużo mówić: postawiłaś poprzeczkę tak wysoko, że żeby jakkolwiek Ci dorównać postanowiłem, że napiszę Ci stronę urodzinową xD Nie jest to nic górnolotnego, wszak nie jestem frontendowcem, ale it is something ok?')
st.write('---------------------------')
st.write('Uznałem, że zrobię takie wspominki na temat naszej relacji w formie takiego nazwijmy to quizu, ale ofc dużo sobie pogadam jak to ja')
st.write('To jest instrukcja jak się tutaj poruszać dla Cb')
st.write('---------------------')
st.write('INSTRUKCJA DZIAŁANIA')
st.write('Przede wszystkim będę Ci tutaj zadawać pytania, na które będziesz musiała odpowiadać! Ale spokojnie, będą łatwe i milutkie, bo chodzi o to żebyś myślała w trakcie naszej wspólnej zabawy jaki jestem super, a nie żebyś mnie wyklinała przez trudność pytań')
q0 = st.radio('Przykładowe pytanie: Jaka jest moja ulubiona osoba?', ('Puste pole','Michał Pierdolony Owczarzak', 'Adam Ondra', 'Karolina Sekutowicz'))
if q0 != 'Puste pole':
    st.write('Poprawna odpowiedź! Przejdź do następnej podstrony wybierając ją z paska po lewej stronie')
    st.session_state.q0 = q0

dev = st.button('Ciekawostka #1')
if dev:
    st.write('Ciekawostka developerska: w pytaniach zamkniętych musiałem wstawiać odpowiedź o nazwie puste pole, ponieważ domyślnie zaznaczana jest pierwsza opcja co sugerowałoby Ci, która odpowiedź jest dobra')

secret = st.button('Ciekawostka #2')

if secret:
    st.write('Nie wiem, którą opcję zaznaczyłaś: mam nadzieję, że siebie: w każdym razie każda odpowiedź jest tutaj uznawana za poprawną c:')

