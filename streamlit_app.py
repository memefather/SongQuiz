import streamlit as st
import os
import openai

st.title("Welcome to SongQuiz! 🚀")

openai.api_key = os.getenv("OPENAI_API_KEY")
model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    # api_usage = response['usage']
    # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

"""
Test your knowledge.
"""

def singnow(conversation):
    input = st.text_input('', 'Near, far, wherever you are')
    if st.button('Sing!'):
        prompt = input
        conversation.append({'role': 'user', 'content': prompt})
        conversation = ChatGPT_conversation(conversation)
        st.write('\n')  # add spacing
        st.subheader('\nNext Line is\n')
        with st.expander("GPT sings", expanded=True):
            st.markdown('conversation[-1]['content'].strip()))  #output the results
        #print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

if __name__ == '__main__':
    # call main function
    conversation = []
    conversation.append({'role': 'system', 'content': 'You are playing a game with the user. The user will give you a line of lyric from a song. You will return the next line.'})
    singnow(conversation)
