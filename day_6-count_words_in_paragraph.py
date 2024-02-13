# Count number of words in a paragraph

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vitae sodales erat. Praesent dapibus leo quis " \
       "lobortis accumsan. Donec congue dignissim bibendum. Aenean vitae ligula finibus, eleifend nunc sed, feugiat " \
       "ligula. Maecenas sit amet pretium nulla, nec dignissim nisi. Nam luctus libero nec quam lobortis luctus. " \
       "Fusce tempus ligula magna. Vestibulum convallis justo felis, nec porta velit elementum nec. Nullam eu porttitor" \
       " lectus, ac elementum sapien. Phasellus egestas risus sed libero egestas consectetur. Ut facilisis et odio eget" \
       " malesuada. Vivamus feugiat metus vel tempor blandit. Quisque viverra dapibus ex non aliquet. Praesent tristique " \
       "eros nisl, non mollis risus tincidunt id. Nulla eu neque mattis, malesuada libero eu, venenatis sem. Aliquam in " \
       "pharetra justo. Nulla sapien velit, ullamcorper nec enim condimentum, maximus tempor risus. Ut commodo leo at " \
       "felis faucibus varius. Nullam et orci cursus, tempor nunc at, malesuada turpis. Mauris quis nisl non nisl" \
       " blandit tincidunt."

words_in_text = text.split()
number_of_words = len(words_in_text)
print("Number of words in text is {}".format(number_of_words))
