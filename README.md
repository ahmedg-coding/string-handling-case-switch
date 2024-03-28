# String Handling Case Switch

## Description
This Python program provides functions to manipulate strings by switching the case of characters and words alternatively. The program enhances text processing capabilities by allowing users to easily modify the case of characters and words within a given string.


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Author](#author)
- [License](#license)


## Installation
To install and run this program locally, follow these steps:  

1. Ensure you have Python installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/).
2. Download or clone the `alternative.py` file from this repository to your local machine.


## Usage
Once you've installed the program, follow these steps to use it:  

1. Open the `alternative.py` file in a text editor or Python IDE of your choice.
2. Modify the 'char_switch_example' variable to contain the desired text you wish to switch the case of characters of.
3. Modify the 'word_switch_example' variable to contain the desired text you wish to switch the case of words of.
4. Save and run the program.
5. Or run the program wihtout making any changes to understand how it works, the output will be in relation to the default text stored in the variables mentioned above.
6. Or import the module or copy the functions `switch_character_case` and `switch_word_case` into your own Python project.   
   Use the functions with appropriate string inputs to switch the case of characters and words alternately.


## Examples
```python
# Example 1: Switching the Case of Characters  
char_switch_example = "Hello World"  
character_result = switch_character_case(char_switch_example)  
print(character_result)  # Expected Output: "HeLlO wOrLd"  

# Example 2: Switching the Case of Words  
word_switch_example = "I am learning to code"  
word_result = switch_word_case(word_switch_example)  
print(word_result)  # Expected Output: "i AM learning TO code"  
```


## Author
Ahmed G.


## License
This project is licensed under the [MIT License](LICENSE).
