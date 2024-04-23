from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GooGLE_API_KEY"))

