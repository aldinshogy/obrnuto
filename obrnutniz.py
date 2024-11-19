import streamlit as st

def reverse_list(user_input):
    # Pretvaranje unosa u listu bez razmaka
    original_list = [element.strip() for element in user_input.split(',')]
    
    # Obrnuti redoslijed liste
    reversed_list = original_list[::-1]
    
    # Vrati obrnuti redoslijed kao string
    return ",".join(reversed_list)

# Naslov aplikacije
st.title("Obrni redoslijed liste")

# Unos korisnika
user_input = st.text_input("Unesite elemente liste odvojene zarezima (npr. 'Nema,Win 95,Win 98,Win 2000')")

# Obrnuti redoslijed i prikaz rezultata kada postoji unos
if user_input:
    result = reverse_list(user_input)
    st.write("Obrnuti redoslijed elemenata liste je:", result)
