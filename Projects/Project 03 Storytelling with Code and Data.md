# Project 3: Storytelling with Code and Data

In this group project you will work with Jupyter Notebooks and create a computational narrative, that
is, tell a “story” with code and data. The project is designed to let you gain experience with loading,
cleaning, filtering, analyzing and visualizing data, and other data science practices.

Project 3 needs to be submitted through Blackboard by **March 30, 2022, 13:00**.
Make sure to include in the submission the documentation, all your code (as .py files), and if applicable 
any other relevant project files, combined into **one .zip file**.

## Documentation
Include a .txt or .pdf document with the following information:

1. Group members: write the name of all the members of your group and the tasks done for each one. Please also include members who did not participate in the project and why (for example, they dropped out of the course).
2. Project status: write all the project requirements and describe for each requirement if it is completed or not. For example, you can use a numerical scale (0 to 100) or a categorical scale (not done, partially completed, completed, expectations exceeded).
3. Running instructions: include the instructions or steps that are necessary to run the project with Python. This will help us grade your project, so please be very clear and specific. Include any library that is used and is not part of the Python Standard Library.

## Assignment
Computational narratives combine text, data and code to tell (often interactive) stories about various topics. Some even regard them as “papers of the future”, as they improve on transparency and reproducibility by design, which is important for Open Science. Here are some examples:

* [An open RNA-Seq data analysis pipeline tutorial with an example of reprocessing data from a recent Zika virus study](https://nbviewer.jupyter.org/github/maayanlab/Zika-RNAseq-Pipeline/blob/master/Zika.ipynb) 
* [An exploratory statistical analysis of the 2014 World Cup Final](https://nbviewer.jupyter.org/github/rjtavares/football-crunching/blob/master/notebooks/an%20exploratory%20data%20analysis%20of%20the%20world%20cup%20final.ipynb) 
* [An open science approach to a recent false-positive between solar activity and the Indian monsoon](https://nbviewer.jupyter.org/github/benlaken/Comment_BadruddinAslam2014/blob/master/Monsoon_analysis.ipynb) 
* [Analysis and visualization of a public OKCupid profile dataset using python and pandas](https://nbviewer.jupyter.org/github/lalelale/profiles_analysis/blob/master/profiles.ipynb) 
* [Particle-In-Cell Plasma Sim](https://nbviewer.jupyter.org/github/numerical-mooc/assignment-bank/blob/master/Lessons.and.Assignments/Particle.In.Cell.Simulations/PIC_Bonus_Notebook.ipynb) 
* [Visualization: Mapping Global Earthquake Activity](https://nbviewer.jupyter.org/github/ehmatthes/intro_programming/blob/master/notebooks/visualization_earthquakes.ipynb)

Currently, Jupyter Notebooks are the probably most popular format for computational narratives, so we
will use them, too. In addition to Python, you will need to “speak” Markdown for nice formatting of the
text cells. This [cheat sheet](https://sqlbak.com/blog/wp-content/uploads/2020/12/Jupyter-Notebook-Markdown-Cheatsheet2.pdf) summarizes the most important Markdown bits. You might also want to
have a look at these [coding standards](https://medium.com/@atma_mani/coding-standards-for-your-jupyter-notebooks-f4e2af7db3a9) for Jupyter Notebooks.

 Your task for this project is to develop a computational narrative around a dataset from the Dutch
central statistics office (Centraal Bureau voor de Statistiek, CBS). Start by going to the [CBS Open data
StatLine](https://opendata.cbs.nl/statline/portal.html?_la=en&_catalog=CBS) portal and choose a dataset. Download the relevant CSV files to work with. (There is also a
[Python library for accessing CBS open data](https://pypi.org/project/cbsodata/), but be aware that downloading the data every time you run
a script can be slow and cause unnecessary traffic, and of course it requires a stable internet
connection.) Then brainstorm about possible analyses that you could do on these data. It helps to think
about these in terms of research questions and (statistics) methods that can be used to answer them. 

_For example, we might have chosen the [“ICT knowledge and skills”](https://opendata.cbs.nl/statline/portal.html?_la=nl&_catalog=CBS&tableId=83428NED&_theme=472) data set. The data set contains information on the self-reported overall ICT skill levels (no, little, basic, advanced) and the presence of specific ICT-related skills (such as installing software, working with spreadsheet software, or writing computer programs) for different groups of people (such as men/women, age groups, educational levels). The data have been collected annually since 2015. Some possible questions and methods:_
* _How do the reported ICT skill levels differ between the groups? Possible methods: (Clustered) bar charts per skill with clusters of four bars (for no/low/medium/high skill levels) for each of the considered groups on the x-axis, and the percentage of the reported skill levels on the y-axis._
* _How have the reported skill levels changed over time? Possible methods: Line graphs per skill and group with the years on the x-axis, the percentage  of the reported skill levels on the y-axis and different colors for the lines to represent the different skill levels._

Choose at least as many analyses for your narrative as you have members in the group. As this course
focuses on how to program things with Python rather than on the data analyses methods themselves,
please use methods that you know or understand. If in doubt, keep it simple. The expectation for this
project is to use standard descriptive statistics methods. To read up on these, David Lane et al.’s free
online book [“Introduction to Statistics”](http://onlinestatbook.com/2/index.html) is a great reference. In
particular, Chapter 2 ([Graphing Distributions](http://onlinestatbook.com/2/graphing_distributions/)) and Chapter 3 ([Summarizing Distributions](http://onlinestatbook.com/2/summarizing_distributions/summarizing_distributions.html)) might be helpful to find suitable
descriptive statistics methods (and the correct English terms for them). If you are familiar with more
advanced methods, for example from your study program, you can also use them. In any case, pay
attention that the chosen methods are applicable to the kind of data you have. 

When you have chosen a dataset and collected analysis ideas, start sketching your computational
narrative and fill the notebook with life. 
Make sure that your project meets the following requirements:
1. The computational narrative is presented in one Jupyter Notebook.
2. Longer pieces of code, especially when not directly meaningful for the narrative (for example details of the data pre-processing when loading the data from the CSV files), are stored in separate .py modules and imported to the notebook.
3. The notebook has different sections, including introductory text with a description of the data set, data loading, the different analyses with explanations, a summary/conclusion, and possible references.
4. There are at least as many different data analyses as group members.

Feel free to be creative and add additional features. For example, integrate additional datasets in the
analysis, have a look into geovisualization or make analyses interactive. Of course, you can easily
challenge yourselves more in this project by trying more sophisticated analyses. The Python ecosystem
is full of interesting data science libraries, browse the web for inspiration.

## Tips
Ask your tutors for help and feedback early and regularly. Don’t wait until you are really stuck
somewhere. Often it is difficult to fix programming problems that are caused by poor design decisions
made early in the project.

Check the project grading rubric. This will give you a clearer idea of what is important to focus on.

You can share your project files through Blackboard. At some point you might also want to work
together on your code during a video call. Four out of several options to do that: 
* One of you shares their screen with Spyder and does the editing, while you discuss it together. 
* You use a collaborative coding environment like [https://repl.it/site/multiplayer](https://repl.it/site/multiplayer), and put the code back to Spyder/Blackboard when you are done there.
* Microsoft’s Visual Studio also supports live sharing and collaborative editing of code, see [https://visualstudio.microsoft.com/de/services/live-share/](https://visualstudio.microsoft.com/de/services/live-share/) for more information.
* CoCalc [https://cocalc.com/doc/jupyter-notebook.html](https://cocalc.com/doc/jupyter-notebook.html) offers services specifically for the
collaborative editing of Jupyter notebooks. They offer a free plan, which has some limitations,
but is probably sufficient for the project.
