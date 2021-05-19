def emojis(texto, emoji, significado):
    i = 0
    nuevo = ""
    while i < len(texto):
        if emoji == texto[i:i + len(emoji)]:
            nuevo += f"{significado}" * len(emoji)
            i += len(emoji)
        else:
            nuevo += texto[i]
            i += 1
    print("Texto censurado: ", nuevo)

