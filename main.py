def main():
    path = "books/frankenstein.txt"
    text = book_text(path)
    number_of_words = num_words_in_book(text)
    letter_count = letter_counting(text)
    print(f"THE NUMBER OF WORDS IN THIS DOCUMENT IS: {number_of_words}.")
    print (letter_count)


    #função para pegar o texto do livro
def book_text(path):
    with open(path) as text:
        return text.read()


    #função para conseguir o número de palavras no texto
def num_words_in_book(path):
    words = path.split()
    return len(words)

    #função para converter o texto para lowercase, e contar quantas letras de cada aparecem no livro.
def letter_counting(text):
    lowered_string = text.lower()
    dict = {}
    for value in lowered_string:
        if value in dict:
            dict[value] += 1
        else:
            dict[value] = 1
    return dict




main()