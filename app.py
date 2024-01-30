#import module
import openai
import json
import streamlit as st

# use "streamlit run app.py"
#functions

def get_key(file_name):
    '''
    Get openAI API Key
    '''
    with open(file_name,'r') as file:
        data = json.load(file)
        key = data['openai_key']
        return key


def get_response(prompt):
    '''
        get the chatgpt response of input prompt
    '''
    completion = openai.ChatCompletion.create(
        model = 'gpt-4-1106-preview',
        messages=[{"role": "system", "content": "You are a helpful and expert PYTHON refractor."},
                  {"role": "user", "content": prompt}],
        temperature = 0.2,
        #max_tokens=4096  # MAX 4096 FOR GPT4 PREVIEW
        
    )

    return completion['choices'][0]['message']['content']


#prompt text
text = '''
Please refactor the provided python code snippet to incorporate the following changes:

1. Properly add comments to explain the code when needed.
2. Follow naming conventions for variables and functions and function parameters.
3. Add appropriate type annotations to function parameters and return types.
4. Include docstrings for functions.
5. Organize imports in a clean and orderly manner and remove unnecessary modules.
6. Remove any unnecessary extra lines and spaces.
7. Use f-strings wherever required.
8. Must Use Python Class to divide code in multiple files (classes) and separate each class by '############################' incdication.
9. Provide all imports including class imports in app.py section (if applicable).
9. Refractor whole Code and don't leave any segment.

Below is the code snippet: (focus only on delete_folder_contents_and_add_none_file classes in provided code)

'''
#main code
def main():

    ##set the key
    openai.api_key  =  get_key('keys.json')

    #streamlit app
    title = ' <h2 style="color: aqua; text-align: center;">CODE REFACTOR 👨‍💻</h2>'
    subtitle = ' <h4 style="color: yellow; text-align: center;">A GPT 4 powered code refactor application for Python Language</h4>'
    st.markdown(title, unsafe_allow_html=True)
    st.markdown(subtitle, unsafe_allow_html=True)

    code = st.text_area("Your Original Code", placeholder="Paste your code here.", height=300)
    prompt  = text + code

    refactor_btn = st.button("Refactor")
    if refactor_btn:
        if len(code)>0:
            response = get_response(prompt)
            st.subheader("Refactored Code")
            st.code(response, language='python')
        else:
            st.warning("Please provide some code")



if __name__ == '__main__':
    main()