def last_repeat(str):
    word_length = len(str)


    for last_index in range(word_length-1, -1, -1):

        last_repeat_char = str[last_index]



        for check_repeat in range(last_index-1):
            if last_repeat_char == str[check_repeat] and last_repeat_char != ' ':
                return last_repeat_char
    return None

