#Simple Logger 

Instead of using printf every where and delete them later. Use logger instead.
In the python code, whenever you want to put a debug point in it, use:

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

When you want to run stress test, you want to ignore the debug points. All you
need to do is not to turn on debug point.

#Try these commands, they can show different levels of logs that you want to
see. Remember error will always show up!!!

```bash
python show_case.py --debug
python show_case.py --info
python show_case.py --error
```

#To use it
Simply put log_style.py in your folder and import it in the main function of
your python script. See show_case.py

