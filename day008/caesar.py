ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(word, process, shift):
  limitted_shift = shift % len(ALPHABET)
  lword = list(word.lower())
  ashift = limitted_shift * (-1 if process.upper() in ['D', 'DECRYPT'] else 1)

  result = [(ALPHABET[ALPHABET.index(lword[i]) +
                      ashift]) if lword[i] in ALPHABET else lword[i]
            for i in range(len(lword))]
  return ''.join(result)
