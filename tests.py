from namari import Namari

alphabet = "abcdefghijklmnopqrstuvwxyz "
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum elementum mauris mattis, varius lectus eu, mattis neque. Nam faucibus posuere mi, ac malesuada tortor dictum egestas. Aenean et ipsum est. Morbi et nisl felis. In maximus ultricies ex, quis interdum massa maximus eget. Suspendisse efficitur vel sapien id tincidunt. Aenean hendrerit, urna non ornare suscipit, dui magna luctus justo, sit amet gravida sem quam a dolor. Praesent posuere non massa non lobortis. Sed elementum id turpis quis tempor. Proin vestibulum magna laoreet nisl facilisis finibus. Vivamus ut ornare sem."
lorem = "".join([x for x in lorem if x.lower() in alphabet])

lexicon = Namari()

for word in lorem.split(" "):
    lexicon.set(word, word)
    lexicon.attach(word, 0)
    lexicon.attach(word, word.lower())
    lexicon.attach(word, word.upper())
    lexicon.attach(word, word.title())
    lexicon.attach(word, word.capitalize())
    lexicon.detach(word, 0)
    print(lexicon.get(word.lower(), "hello, world"))
