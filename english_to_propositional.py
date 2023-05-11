# This is the first of two project I made for the Discrete mathematics course in my second semester of the second year at EJust

# It basically accepts a bunch of statements separated by commas and dots, separates them, extracts the propositional logic keywords then removes them, assigns each unique statement an ascii character, decides which statement are related so they can be put together with the keyword they share, and finally apply one of three inference rules

# limitations include: (One statement cannot have more than one keyword, keyword 'if' must come at the beginning of a sentence, you have to explicitely use 'not' because using words like don't, can't, etc.. doesn't count as a keyword.)

keywords = {
  'if': ' ',
  'then': '->',
  'implies': '->',
  'not': '~',
  'and': '^',
  'or': '|',
}

#############################


def english_to_symbol(sentence):
  start = 0
  end = 0

  parts = []

  for i in sentence:
    if i == "," or i == ".":
      parts.append(sentence[start:end].lower())
      start = end + 2

    end += 1

  # print(parts, "\n")

  characterStart = 65
  dict_counter = 0
  symbols = {}

  for sentence in parts:
    words = sentence.split(" ")
    keywordsFound = ''

    for word in words:
      if word in keywords:
        keywordsFound = keywords[word]
        words.remove(word)

    symbols[str(dict_counter)] = [' '.join(words), keywordsFound]
    dict_counter += 1

  letters_dict = {}
  for i in range(len(symbols)):
    if symbols[str(i)][0] in letters_dict:
      continue
    else:
      letters_dict[symbols[str(i)][0]] = chr(characterStart)
      characterStart += 1

  for value in letters_dict:
    print("'", value, "'", "is equivelant to: ", letters_dict[value])

  print("\n")

  for key in symbols:
    print(symbols[key][0])

  print("\n")

  print(symbols)
  print("\n")
  generate_word(symbols, letters_dict)


#############################


def generate_word(symbols_dict, letters_dict):
  counter = -1
  sentences = [[] for key in symbols_dict]
  for key in symbols_dict:
    if symbols_dict[key][1] == ' ' or symbols_dict[key][1] == '':
      counter += 1
      sentences[counter].append(letters_dict[symbols_dict[key][0]])
    else:
      sentences[counter].append(symbols_dict[key][1])
      sentences[counter].append(letters_dict[symbols_dict[key][0]])

  for words in sentences:
    print(' '.join(words))

  #print(sentences)
  apply_inference_rules(sentences, symbols_dict)

#############################


def apply_inference_rules(symbols_double_list, symbols_dict):
  for list in symbols_double_list:

    if (len(list) > 1):
      # modus ponens
      if list[1] == '->' and [list[0]] in symbols_double_list:
        print("Using Modus Ponens, these statements: \n", " ".join(list),
              " and ", list[0])
        print("Resolve into: ", list[2])
      # disjunctive syllogism

      elif list[1] == '->' and [list[0], '~'] in symbols_double_list:
        print("Using Disjunctive Syllogism, these statements: \n",
              " ".join(list), " and ~", list[0])
        print("Resolve into: ~", list[2])

      # simplification
      elif list[1] == '^':
        print("Using simplification this statement: \n", " ".join(list))
        print("Resolve into: ", list[0])


english_to_symbol(
  "If the patient is shaking, then there is a chance he is ill. The patient is shaking."
)
