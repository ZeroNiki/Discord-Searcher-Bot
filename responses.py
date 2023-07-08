from youtube_search import YoutubeSearch

def get_response(message: str) -> str:
    user_send = message.lower()

    history = []

    if user_send == "!help":
        return "`Command prefix = '!'\n?<key_word> - send in private\n<key_word> - start search and send result search"

    if user_send:
        key_word = user_send[1:].lower() 

        search_yt = YoutubeSearch(key_word, max_results=1).to_dict()
        search_key = "id"

        banned_word = ['xxx', 'porn', ' ']

        if key_word in banned_word:
            return 'Write correct key word'
        else:
            for res in search_yt:
                res_link = f'https://www.youtube.com/watch?v={res.get(search_key)}'
                return res_link

        
    return 'I did not understand what you wrote. Please send "!help"'
    