# WORKING WITH LOCATORS ON HTML
In Selenium automation, if the elements are not found by the general locators like id, class, name, etc. then XPath is used to find an element on the web page .

### Element: 
```html
<input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" role="combobox" spellcheck="false" title="Search" value="selenium python" aria-label="Search" data-ved="0ahUKEwi0_8Pj7dTrAhWxoXIEHXfhCykQ39UDCAo" xpath="1" style="">
```

### Tag
example: input - element with input 'tag'

### Attributes
describes the element to the browser to display on the GUI

selenium uses tags and attributes to find element(s) and do some action on these elements (using built-in method)


### Locating by CSS Selector
CSS Selectors are string patterns used to identify an element based on a combination of HTML tag, id, class, and attributes. Locating by CSS Selector is more complicated than the previous methods, but it is the most common locating strategy of advanced Selenium users because it can access even those elements that have no ID or name.

CSS Selectors have many formats, but we will only focus on the most common ones.

- Tag and ID
- Tag and class
- Tag and attribute
- Tag, class, and attribute
- Inner text

Locating by CSS Selector - Tag and ID
Again, we will use Facebook's Email text box in this example. As you can remember, it has an ID of "email," and we have already accessed it in the "Locating by ID" section. This time, we will use a CSS Selector with ID in accessing that very same element.
(hash (#) means ID, dot (.) means class)

**Syntax**

css=tag#id

**Description**
- tag = the HTML tag of the element being accessed|
- '# = the hash sign. This should always be present when using a CSS Selector with ID
- id = the ID of the element being accessed|


```css
#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input
```

### What is XPath in Selenium?

XPath in Selenium is an XML path used for navigation through the HTML structure of the page. It is a syntax or language for finding any element on a web page using XML path expression. XPath can be used for both HTML and XML documents to find the location of any element on a webpage using HTML DOM structure.

The basic format of XPath is explained below with screen shot.

![xpath](data/xpath.png)

**Syntax for XPath:**

XPath contains the path of the element situated at the web page. Standard syntax for creating XPath is.

    Xpath=//tagname[@attribute='value']

* // : Select current node.
* Tagname: Tagname of the particular node.
* @: Select attribute.
* Attribute: Attribute name of the node.
* Value: Value of the attribute.

**Example:**

copying the whole element: 

```html
<div id="result-stats" style="" xpath="1">About 27,600,000 results<nobr style=""> (0.44 seconds)&nbsp;</nobr></div>
```

xpath = "//div[@id='result-stats']"

crhome: "//form[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input"
chropath: "//div[@class='a4bIc']//input[@name='q']"
-----------------------------------
PyDev console: starting.
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
```python
result_msg = "About 31,100,000 results (0.39 seconds)"
result_msg = "About 31,100,000 results (0.39 seconds)"
result_num_str = result_msg.split()
print(result_num_str)
['About', '31,100,000', 'results', '(0.39', 'seconds)']
result_msg_list = result_msg.split()
print(result_msg_list)
['About', '31,100,000', 'results', '(0.39', 'seconds)']
result_num_str = result_msg_list[1]
result_num_str = result_msg_list[1].replace(',', '')
result_num = int(result_num_str)
if result_num > 20000000:
...     print("Test Passed")
... else: 
...     print("Test Failed")
...     
Test Passed
assert result_num > 20000000
assert result_num < 20000000
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AssertionError
result_time_str = result_msg_list[3]
result_time_str = result_msg_list[3].replace('(', '')
result_time = float(result_time_str)
assert result_time < 1
```



















