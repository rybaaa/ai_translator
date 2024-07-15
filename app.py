from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import streamlit as st
import openai
import os
from dotenv import find_dotenv, load_dotenv
from annotated_text import annotated_text



load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")


# Extract data from text
def translate(input, from_language, to_language):
    template = """As a translation expert, translate from {from_language} to {to_language}: {sentence}
        """
    prompt_template = PromptTemplate(input_variables=["sentence", "from_language", "to_language"], template=template)
    llm = OpenAI(temperature=.7)
    full_response=llm(prompt_template.format(sentence=input, from_language=from_language, to_language=to_language))
    
    return full_response


def main():
    st.set_page_config(page_title="Translator")
    st.title("Translator AI Assistant...🤖")
    
    languages = ["English", "French", "German", "Polish", "Continental Portuguese", "Brazillian Portuguese", "Spanish",  "Russian", "Ukrainian"]
    
    option_from = st.selectbox(
        "Choose which language needs to be translated",
        (languages)
    )
    option_to = st.selectbox(
        "Choose which language to translate into",
        (languages)
    )
    
    prompt = st.text_input("Your prompt")
    
    if prompt:
        st.divider()
        st.write(annotated_text("Searching for: ",(prompt, "", "#8ef")))
        st.divider()
        response = translate(prompt, option_from, option_to)
        st.write(annotated_text("The answer is: ",(response, "", "#8ef")))     
        
   
    

#Invoking main function
if __name__ == '__main__':
    main()