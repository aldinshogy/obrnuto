import re
import streamlit as st

def reverse_list():
    user_input = input("Unesite elemente liste odvojene zarezima (npr. 'Nema, Win 95, Win 98, Win 2000'): ")
    

    original_list = [element.strip() for element in user_input.split(',')]
 
    reversed_list = original_list[::-1]
   
    print("Obrnuti redoslijed elemenata liste je:", reversed_list)


reverse_list()
