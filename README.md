# iMotions Data Processing

This repository contains various scripts for processing data from [iMotions](https://imotions.com).
This readme will attempt to orient whichever poor soul is as unfortunate as to
have to deal with the raw .txt output from this program.

# The Big Problem
The *fundamental problem* with the .txt raw data output by iMotions is 
that **it conceals the true nature of the data!** It may *look* like
straightforward tabular data but it is in fact multiple concurrently updating measurements
happening at different times and different frequencies, and if you are not aware
if this you will start performing calculations with duplicated values. Instead of
being honest about the complexity of the underlying data, iMotions will use *constant interpolation* 
to forward-fill the values. To learn the ins and outs of Time Series analysis (which is what this data 
actually requires) [watch this PyCon tutorial.](https://youtu.be/zmfe2RaX-14)

Here's why this is bad:
* It hides the fact that the data is (badly) interpolated.
* Constant interpolation is not as accurate as other methods of interpolation. This becomes an issue when 
comparing low-frequency data (0-10Hz) with high-frequency data (60-256Hz+).
* The file sizes are HUGE due to all of the duplicate values.
* iMotions does not provide enough fine-grained control over what values are exported, often giving you a lot
of unwanted raw measurement values.

Half the battle when dealing with the .txt format is filtering out all the excess garbage to get
the data that actually matters. I have worked on studies where the process of cleaning these files
resulted in a 99.5% reduction (not a typo!) in file size. THEN if you want to do any particularly sophisticated
analysis you end up putting the results into a database so you can use SQL. 

If only iMotions provided a more direct way to access the internal database...

# Data Details
The raw .txt data format is a tab-delimited table of values. The first row after the file metadata (prefixed with `#`) 
contains the column headers. There is a set of columns common to all files with metadata such as the name of the 
subject, export date, study name, and the most important column, **`EventSource`**. The `EventSource` column contains a
list of events separated by the pipe character, `|`. The rest of the columns each correspond to exactly one event source,
and the `EventSource` column lists the sensors which have new data in that row. A column will *only* contain new
data if its corresponding event name is listed in the `EventSource` column. All other columns on that row can be ignored.

It's worth re-reading the last paragraph one or two more times, because it's important to understand which values in a
row matter and which are just duplicates.

# Cleaning Data
Cleaning a file involves:
 1. Removing rows which do not contain a relevant EventSource
 2. Removing irrelevant columns
 3. Removing rows with invalid data (**SEE NEXT SECTION**)

# **_A WARNING ABOUT MULTIPLE EVENT SOURCES_** 
If multiple event sources are included, you need to figure out how to handle cases where two events are included in a
row and one event has valid data and the other one does not. This is another fundamental problem with the tabular text 
format. The only true solution to this is to properly normalize the data into a database for further processing. 
**_Only using this code as a first-pass cleaning to reduce file size before importing into a database!_** 

# This Repository
This repository has code that I have actively used to do the first-pass processing of file for many research
studies. This process has evolved over 1.5 years to the form you see now, but it is not all that polished because it was
only ever written for me to get the most immediate job done.

The file `pandas_filter.py` has working code for cleaning files. I recommend finishing up the `DataProcess` module and 
using those functions, but in the meantime the code there will suffice. The primary function that actually performs
the data cleaning is called `process_file` in `utils.py`. Any custom filtering logic will need to be manually added to 
this function, and modified depending on the events being cleaned. `process_file` accepts a list of event sources and
looks up the columns names and types from `sensors.py`, returning a filtered pandas DataFrame. Note that data types 
should be defined using numpy.float64 for any numeric types. 

The `DataProcess` module addresses the issue of having to constantly modify the filtering code by adding filtering rules
to the sensor definitions, but it still a WIP. It does not, however, solve the problem of removing invalid data when 
filtering for multiple event sources.

I recommend using PyCharm to work on this code, because it is awesome. You can import this project into PyCharm with the
instructions here: https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html

This project relies upon `pandas`, a powerful library for Python. Review the following to avoid making severe performance
mistakes: https://www.youtube.com/watch?v=4JwpDGrMsJE&list=PLB-iOhOaPYindAFJPEQOFyzbSxqMZNwKF&index=12&t=0s