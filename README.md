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

# set key-value pair
lexicon.set("yellow", "sun")

# associate existing keys with a new and unique key
lexicon.attach("yellow", "hot")
lexicon.attach("yellow", "morning")
lexicon.attach("morning", "summer")
lexicon.attach("morning", "cold")

# disassociate 2nd key from the 1st key
lexicon.detach("summer", "cold")

# get the value of the specified key
object = lexicon.get("morning") # None

# get the value of the specified key with specified fallback
object = lexicon.get("night", fallback="moon")
```

## Did you know?
The repository name `namari` was inspired from the developer's noisy cat named Anna Marie, it also means as lead or guidance in Japanese.
