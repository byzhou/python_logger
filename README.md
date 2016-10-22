#Simple Logger 

Instead of using printf everywhere and deleting them later, try to use logger
instead. In your python codes, wherever you want to put a debug point,
use:

```python
lg.debug("Hi, test here")
```
When you want to debug, instead of:

```python
python show_case.py
```

Execute this line:

```bash
python show_case.py --debug
```

When you want to run stress tests, you can ignore the debug points by not
turning on debug flag in the command line:

```python
python show_case.py
```

#Try these commands
They will show different levels of logs that you want to see. Remember, errors
will always show up!!!

```bash
python show_case.py --debug
python show_case.py --info
python show_case.py --error
```

#How to use it
Simply put log_style.py in your folder and import it in the main function. See
show_case.py

