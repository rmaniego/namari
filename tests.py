from namari import Namari

alphabet = "abcdefghijklmnopqrstuvwxyz "
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum elementum mauris mattis, varius lectus eu, mattis neque. Nam faucibus posuere mi, ac malesuada tortor dictum egestas. Aenean et ipsum est. Morbi et nisl felis. In maximus ultricies ex, quis interdum massa maximus eget. Suspendisse efficitur vel sapien id tincidunt. Aenean hendrerit, urna non ornare suscipit, dui magna luctus justo, sit amet gravida sem quam a dolor. Praesent posuere non massa non lobortis. Sed elementum id turpis quis tempor. Proin vestibulum magna laoreet nisl facilisis finibus. Vivamus ut ornare sem."
lorem = "".join([x for x in lorem if x.lower() in alphabet])

lexicon = Namari("test.namari.json")

print("\n\n# of items:", lexicon.count())
print("\nClearing items...")
lexicon.clear()

if lexicon.is_empty():
    print("\n\nPopulating dataset...")
    for word in lorem.split(" "):
        lexicon.set(word, word)
        lexicon.attach(word, 0)
        lexicon.attach(word, word.lower())
        lexicon.attach(word, word.upper())
        lexicon.attach(word, word.title())
        lexicon.attach(word, word.capitalize())
        lexicon.detach(word, 0)
        count = lexicon.count()
        item = lexicon.get(word.lower(), "hello, world")
        print(f"#{count} {item}")

print("[check]")
print("Contains \"lorem\":", lexicon.contains("lorem"))
print("Contains \"hello\":", lexicon.contains("hello"))


print("\n\n[keys]")
print(lexicon.keys())
keys = [str(x) for x in lexicon.keys()]
print(",".join(keys))


print("\n\n[values]")
print(",".join(lexicon.values()))


print("\n[dataset]")
for keys, value in lexicon.items():
    print(f" - {keys}: {value}")

print("\n# of items:", lexicon.count())
