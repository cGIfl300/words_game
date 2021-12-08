# Tech documentation of Words Game

This documentation describes the main class and the way to use them.

## WordsGame

Simply instance it using:

```python
app = WordsGame()
```  

Instancing **WordsGame** don't load the database. Before instancing **
WordsGame** you should review the source code, by default the database path is *
data\mydb.json* you can change it.

### Changing the database path

To change the database path you need to change the value of the attribute *
data_base_path*.

```python
app = WordsGame()
app.data_base_path = "c:\\new_path.json" # Using our own database
```  

### Acquiring a new file

Thus you can add new words to the database, the file must be unicode encoded.

```python  
app = WordsGame()
app.acquirer(filepath) # filepath is a string
```  

The acquisition model use [unidecode](https://pypi.org/project/Unidecode/) to
convert local accents, example:

```  
été => ete
```  

Once this is done, it convert the file to lowercase and remove not allowed
characters, by default we allow "[a-z]- ".  
The new word list is joined to the existing one (if any) and we remove twins to
maintain a clean words list.  
**Acquiring a new file don't save it to disk!**

### Save the words list to disk

To save the actual words list to disk, use:

```python  
app = WordsGame()
app.acquirer(filepath) # filepath is a string
app.save()
```  

The file will be saved to *app.data_base_path*. Using our JSON format.

### Load the words list from disk

To load the actual words list from disk, use:

```python  
app = WordsGame()
app.load()
```  

The database will be loaded from *self.data_base_path*. Using our JSON format.

### Retrieve words from an URL

To retrieve words from an URL, use:

```python  
app = WordsGame()
app.get_from_url(url)
```  

The words will be loaded from *url*.  
**Acquiring from an URL don't save it to disk!**

### Search for Words

I built differents search engines. Here they are.

#### Word with missing letters

Example: "B _ _ L D"  
This is the basic function *find_word* who can do that. It returns a list of
available words from the database, if none, an empty list. You must use dots *.*
for unknown letters.

```python  
app = WordsGame()
app.load()  
guess = app.find_word("b..ld") # Will return ['build'] if build is in the database, off course.
```  