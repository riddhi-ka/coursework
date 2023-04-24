# Data Skills 2: Homework 3
### Text Processing

__Due Date: Monday, November 7th before midnight__

__Part 1: Natural Language Processing__

You are working as a research assistant at a think tank studying international refugees.  The senior researcher you work for tries to follow 
[the Refugee Brief](https://www.unhcr.org/refugeebrief/) from the UNHCR, but they have been too busy lately to keep up with it.  They ask you
to read in the reports and parse them using natural language processing.  They come out every Friday, except for around Christmas.  

Use basic web scraping to collect every report between the most recent (June 24th, 2022) and April  8th, 2022.  The first one can be found
 [here] (https://www.unhcr.org/refugeebrief/the-refugee-brief-24-june-2022/); use that to locate the rest.

Describe the sentiment of each article, and show which countries are discussed in the articles.

Output to save to your repo for this question:
  * question1.py file with the code - summary statistics can be displayed in your code
  * question1_plot.png file for a plot that shows sentiment over time
  
__Part 2: Parsing PDF Tables__

Not all text processing requires using NLP!  The document 2005proposal.pdf is from the 2005 Base Realignment and Closure (BRAC) Commission.  
This is a group that proposes military base changes in a process designed to insulate decisions from political interference.  Bases can be 
"realigned" - that is, gain or loose employment, they can be "closed" all together, or be unaffected.  The tables organize bases by which 
Metropolitan Statistical Area (MSA) they are a part of, followed by the proposed changes (details listed earlier in the document).

The PDF document is included only for your reference - the file you will be working from is named 2005proposal.pdf.txt, and is the result 
of parsing the PDF document to extract text.  It did not come out completely clean, however.  Your task is to study the text output, 
compare it to the source PDF, then write a script that takes in the text document and outputs a CSV document.  See the included image 
DS2_Python_HW3_answer_sample.png for the desired format.

Your code does not need Pandas - instead, recall the structure of a CSV document as we've discussed in class, and build that directly 
using containers and strings.  In addition to a file named question2.py, include your final question2.csv file in the repo.
