# namari
Many-to-one keys-value pair relationship Python object manager.

![](/resources/banner.png)

## Usage
Install the latest namari package, upcoming versions might introduce unannounced changes, so a virtual environment is a must have before installation.
```bash
pip install --upgrade namari
```

To integrate namari into your Python codes, check the code snippet below:
```python
from namari import Namari

# initialize
lexicon = Namari()

# initialize with filename
lexicon = Namari("filename.json")

# clear contents
lexicon.clear()

# set key-value pair
lexicon.set("yellow", "sun")

# check if key existing
if lexicon.contains("yellow"):
    print("Exists")

# associate an existing key with another value
lexicon.attach("yellow", "hot")
lexicon.attach("yellow", "morning")
lexicon.attach("yellow", "tea")
lexicon.attach("morning", "summer")
lexicon.attach("morning", "cold")
lexicon.attach("morning", "tea")

# associate an existing key with a unique value
lexicon.attach("morning", "tea", unique=True)

# disassociate 2nd key from the 1st key
lexicon.detach("summer", "cold")

# get the value of the specified key
object = lexicon.get("morning") # None

# get the value of the specified key with specified fallback
object = lexicon.get("night", fallback="moon")

# get the first parent of child
parent = lexicon.findFirst("summer", fallback=None)
parents = lexicon.findAll("tea")

# count contents
count = lexicon.count()

# check if empty
if lexicon.is_empty():
    print("Empty")

# iterate over all keys-value pairs
for keys, value in lexicon.items():
    print(type(keys)) # list
    print("\n".join(keys))
    print(value)
```

## Did you know?
The repository name `namari` was inspired from the developer's noisy cat named Anna Marie, it also means as lead or guidance in Japanese.
