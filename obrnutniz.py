import re
import streamlit as st

def reverse_list():
    user_input = input("Unesite elemente liste odvojene zarezima")
    
    original_list = [element.strip() for element in user_input.split(',')]
    
    reversed_list = original_list[::-1]
    
    print("Obrnuti redoslijed je: " + ",".join(reversed_list))

reverse_list()
