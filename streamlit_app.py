import streamlit as st
import os
import openai

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
    🎼Think you are expert in realm of music? Test your knowledge!🎤
    """
    
    def quiznow(conversation):
        st.subheader('\nWhat is the Next Line?\n')
        conversation = ChatGPT_conversation(conversation)
        st.markdown(conversation[-1]['content'].strip())
        input = st.text_input('enter next line here', '')
        if st.button('Rock it!'):
            prompt = input
            conversation.append({'role': 'user', 'content': prompt})
            conversation = ChatGPT_conversation(conversation)
            st.write('\n')  # add spacing
            with st.expander("GPT judge", expanded=True):
                st.markdown(conversation[-1]['content'].strip())  #output the results
                if st.button('Another one!'):
                    st.experimental_rerun()
            #print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    if __name__ == '__main__':
        # call main function
        conversation = []
        conversation.append({'role': 'system', 'content': 'You are playing a game with the user. You will provide a line of lyrics from a song after this prompt and the user will guess the next line. If the answer is correct or close enough, reply "Yeah! You got it!" If incorrect, provide the right answer along with the song title, artist and year of release'})
        quiznow(conversation)

