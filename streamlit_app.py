import streamlit as st
import os
import openai
from PIL import Image

image = 'https://m.media-amazon.com/images/I/71+q4wh2+YL._UF1000,1000_QL80_.jpg'

tab1, tab2 = st.tabs(["Sing", "Quiz Me!"])

with tab1:
    st.title("Welcome to SongQuiz! 🎵")
    
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
    🎼Sing with GPT! Enter that line of lyric stuck in your head all day and jam with GPT.🎤
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
                st.markdown(conversation[-1]['content'].strip())  #output the results
            #print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
    
    if __name__ == '__main__':
        # call main function
        conversation = []
        conversation.append({'role': 'system', 'content': 'You are playing a game with the user. The user will give you a line of lyric from a song. You will return the next line.'})
        singnow(conversation)

with tab2:
    st.title("Welcome to SongQuiz! 🎵")
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model_id = 'gpt-3.5-turbo'
    
    def ChatGPT_conversation(conversation2):
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=conversation2
        )
        # api_usage = response['usage']
        # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
        # stop means complete
        # print(response['choices'][0].finish_reason)
        # print(response['choices'][0].index)
        conversation2.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
        return conversation2
    
    """
    🎼Think you are expert in realm of music? Test your knowledge!🎤
    """
    
    def quiznow(conversation2):
        st.subheader('\nWhat is the Next Line?\n')
        conversation2 = ChatGPT_conversation(conversation2)
        st.markdown(conversation2[-1]['content'].strip())
        conversation2.append({'role': 'user', 'content': 'What is the line immediately following your line and tell me the artist, song title and year of release'})
        st.write('\n')  # add spacing
        with st.expander("Show Answer", expanded=False):
            conversation2 = ChatGPT_conversation(conversation2)
            st.markdown(conversation2[-1]['content'].strip())  #output the results
            st.image(image)
            #html_string = "<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/48UPSzbZjgc449aqz8bxox?utm_source=generator" width="40%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>"
            #st.markdown(html_string, unsafe_allow_html=True)
            if st.button('Another one!'):
                st.experimental_rerun()
        #print('{0}: {1}\n'.format(conversation2[-1]['role'].strip(), conversation2[-1]['content'].strip()))

    if __name__ == '__main__':
        # call main function
        conversation2 = []
        conversation2.append({'role': 'system', 'content': 'You are playing a game with the user. You will provide a random line of lyric from a song without any other information'})
        quiznow(conversation2)

