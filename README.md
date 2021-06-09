# **TFG**
## *IDENTIFYING THE PYTHON CODE LEVEL USING THE CERFL FRAMEWORK AS INSPIRATION*

### What is this project about?
The objective of this Final Degree Project is to create a tool capable of obtaining an evaluation inspired by the [''Common European Framework of Reference for Languages''](https://en.wikipedia.org/wiki/Common_European_Framework_of_Reference_for_Languages) for code written in the Python programming language, version 3.

Through this tool, it will be possible to analyze the level of GitHub repositories (and their developers) or code snippets in this language.



### How does it work?

To put it into operation you have to follow the steps below:
1. Configure the 'configuration.cfg' file with the level assignment of your choice.
2. Execute the file 'dict.py' to generate a level dictionary.
   ```
   python3 dict.py
   ```
3. Execute the main program 'main.py' in three different ways:

    * Analyze a directory
      ```
      python3 main.py directory name_path
      ```
    * Analyze a Github repository
     ```
     python3 main.py repo name_urlclone
     ```
    * Analyze a Github user
     ```
     python3 main.py user name_user
     ```
4. After that, this program will generate two types of formats to view the results:
    * **json**
    * **csv**

  Both indicating:
  * Repository name
  * File name
  * Class of element
  * Start Line
  * End Line
  * Displacement
  * Level of element


5. If you want to visualize the results on a web page:

    * Run the file 'main.js' to create the page 'index.html'. You will get one web page for each repository.


## Of interest
We are trying to obtain a consolidated version of Python levels, for this purpose, we propose this survey is to ask you how you would assign those levels to Python structures.

This is the long version of the survey. The time to fill out the survey is approx. 15 minutes. https://forms.gle/pA71ajFx1HVaZMYq9

There is a shorter version of the survey (survey time is approx. 5 minutes) here, in case you do not have that much time: https://forms.gle/rFXFmqs5LnnHopUb6 (you can also take first the short version and then the long one if you want).

Thank you very much!
