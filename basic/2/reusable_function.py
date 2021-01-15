def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
        return output


user_message = input("> ")
print(emoji_converter(user_message))
