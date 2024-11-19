import re
import streamlit as st

def reverse_list():
    # Unos korisnika
    user_input = input("Unesite elemente liste odvojene zarezima (npr. 'Nema,Win 95,Win 98,Win 2000'): ")
    
    # Pretvaranje unosa u listu bez razmaka
    original_list = [element.strip() for element in user_input.split(',')]
    
    # Obrnuti redoslijed liste
    reversed_list = original_list[::-1]
    
    # Prikaz rezultata bez razmaka u izlazu
    print("Obrnuti redoslijed elemenata liste je: " + ",".join(reversed_list))

# Poziv funkcije
reverse_list()
