# **pycefr**
## *Identifying Python3 Code Level Using the CERFL Framework as Inspiration*

### What is this project about?
The goal of pycefrl is to create a tool capable of obtaining an evaluation inspired by the [''Common European Framework of Reference for Languages''](https://en.wikipedia.org/wiki/Common_European_Framework_of_Reference_for_Languages) for code written in the Python programming language, version 3.

With this tool it is possible to analyze the level of GitHub repositories (and their developers) or code snippets in Python3.



### How does it work?

To put it into operation you have to follow the steps below:
1. Edit the 'configuration.cfg' file with the level assignment of your choice. If you want to use the default ones (recommended), just go to step 2.
2. Execute the file 'dict.py' to generate a level dictionary.
   ```
   python3 dict.py
   ```
3. Execute the main program 'pycerfl.py' in three different ways:

    * Analyze a directory.
      ```
      python3 pycerfl.py directory <name_path>
      ```
    * Analyze a GitHub repository.
      ```
      python3 pycerfl.py repo <name_urlclone>
      ```
    * Analyze a GitHub user.
      ```
      python3 pycerfl.py user <name_user>
      ```
4. After that, this program will generate two types of formats to view the results:
    * **JSON**: data.json
    * **CSV**: data.csv

  Both of them including following information:
  * Repository name
  * File name
  * Class of element
  * Start Line
  * End Line
  * Displacement
  * Level of element


5. If you want to visualize the results on a web page:

    * Run the file 'main.js' to create the page 'index.html'. You will get one web page for each repository.
      ```
      node main.js
      ```


## Of Interest

We are trying to obtain a consolidated version of Python levels, for this purpose, we propose this survey is to ask you how you would assign those levels to Python structures.

This is the long version of the survey. The time to fill out the survey is approx. 15 minutes. https://forms.gle/pA71ajFx1HVaZMYq9

There is a shorter version of the survey (survey time is approx. 5 minutes) here, in case you do not have that much time: https://forms.gle/rFXFmqs5LnnHopUb6 (you can also take first the short version and then the long one if you want).

Thank you very much!
