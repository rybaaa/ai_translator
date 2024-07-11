from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import streamlit as st
import openai
import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")


# Extract data from text
def translate(input):
    template = """As an tranlation expert, translate from english to continental portuguese: {sentence}
        """
    prompt_template = PromptTemplate(input_variables=["sentence"], template=template)
    llm = OpenAI(temperature=.7)
    full_response=llm(prompt_template.format(sentence=input))
    
    return full_response

print(translate("Hello world!"))

def main():
    st.set_page_config(page_title="Translator")
    st.title("Translator AI Assistant...🤖")
    
    title = st.text_input("Your word")
            
    

#Invoking main function
if __name__ == '__main__':
    main()