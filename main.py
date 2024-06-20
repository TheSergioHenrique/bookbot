def main():
    path = "books/frankenstein.txt"
    text = book_text(path)
    number_of_words = num_words_in_book(text)
    print(f"THE NUMBER OF WORDS IN THIS DOCUMENT IS: {number_of_words}.")


    #função para pegar o texto do livro
def book_text(path):
    with open(path) as text:
        return text.read()


    #função para conseguir o número de palavras no texto
def num_words_in_book(path):
    words = path.split()
    return len(words)



main()