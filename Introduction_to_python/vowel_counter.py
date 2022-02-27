def vowel_counter(string):
    vowel_count = 0

    for char in string:
        if char in 'aeiou':
            vowel_count = vowel_count + 1

    return vowel_count

def main():
    while( 1 == 1):
        word = input('Enter a word:')

        if (word == '-1'):
            break
        else:
            print('number of vowels',vowel_counter(word))


if __name__ == '__main__':
    main()
