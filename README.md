# Food Safety in Wales 


The Food Standards Agency (FSA) is a non-ministerial government body that is responsible for food safety and hygiene in England, Wales and Northern Ireland. The FSA gathers information on public food practices by conducting surveys. The Food and You Survey (F&Y) is a flagship biennial study that explores the public's attitudes, knowledge and behaviour relating to food safety and production. Data is analysed and used to compile publicly available reports. 

Wales is demographically distinct to the rest of the UK, being less populous, more deprived, with a larger rural population. For this reason, the FSA was particularly concerned that its F&Y engagement activities do not reach some of the demographic groups in Wales, who may have associated food risks. The following specific questions were posed: 

* Does F&Y survey sampling reflect the true demographic profile of Wales? 
* What food risks are associated with undersampled groups, and what is their understanding of food labelling? 
* Are there any relationships between behaviours related to food safety, and can we predict food risk for specific groups or individuals?


## Team

James Doherty - [Private GitHub](https://github.com/jimmyd83) \
Lorena Garcia Perez - [Private GitHub](https://github.com/lorena-gp) \
Charlie Jeynes - [Private GitHub](https://github.com/charliejeynes) \
Mishka Nemes - [Private GitHub](https://github.com/mihaelanemes) 


## Timeline

Science to Data Science Virtual School - 23rd of March to 24th of April 2020 \
Hosted and organised by [Pivigo](https://www.pivigo.com/)

## Data sources

[Food and You (F&Y) survey 2010-2018](https://data.gov.uk/dataset/6cae91e7-a5aa-45b4-880d-29b3b7ea93b0/food-and-you-wave-five): Food and You Waves 1-5 Data, csv file, dated on 09 September 2019 \
[Food and You (F&Y) survey guide](https://data.food.gov.uk/catalog/datasets/3f3ad1b7-8cf3-444b-abbf-f784ea4551e1): Select Wave 1 to 5 - Data user guide \
[Census 2011 - microdata with individual entries](https://www.ons.gov.uk/census/2011census/2011censusdata/censusmicrodata/securemicrodata): For data download (isg_regionv2.csv), an account needs to be created [here](https://www.ukdataservice.ac.uk/get-data/how-to-access/registration)


To note the datasets can be swapped for other data, and this can be amended in Line 2 of the masterscript.

## Data wrangling 

**F&Y** - missing values in the questions answers encoded by negative value when respondents did not answer questions are all encoded as `NaN` \
**Census** - given the higher granularity of the data, data was aggregated to reflect the answer labels in F&Y in order to allow direct comparison. There were no missing values as all demographics were provided for each respondent.


## Repository structure

**`app`** - includes everything required to run the dashboard. The .ipynb file, together with the software requirements and the F&Y .csv files \
`**data**` 
* the `microdata_census2011_Wales_prepared.csv` has all the comparable demographic data from the Census 2011. This includes only the Wales entries for ~7/120 demographics

## Masterscript

The data loading, data wrangling and data analysis (all below functions) are compiled in the `notebooks/masterscript_with_markdown`

### Dictionary 

A nested dictionary was built in order to rename values and variables to comprehensible and meaningful names. The input data is the F&Y survey guide.

### Custom bar plotting functions

`custom_barplots` is the main function that plots the data that is parsed when the function is called. The output is horizontal barplots that indicate the confidence intervals (variation in the data) and the mean percentage values. It calls the dictionary to input the relevant question and answer names in the axis labels and the legend. \
`custom_lineplots` takes the F&Y data to plot it over time (i.e. survey years) and yields a group of plots side by side that can illustrate how a certain variable changes over temporally according to a third variable (e.g. country). The output is  lineplots that indicate the confidence intervals (variation in the data) and the number of respondents in each category. It calls the dictionary to input the relevant question and answer names in the axis labels and the legend. 



### Exploratory Data Analysis

Principal Component Analysis (PCA) was used to explore the raw data in order to understand generic patterns when inputing all the data from F&Y.


### Data Analysis and Visualization

A timeline of percentage representation of F&Y demographics is plotted for the F&Y only using `custom_lineplots`. 

Demographic variables (age, gender, marital status, religion, health status, work status, deprivation) are compared between F&Y and Census using `custom_barplots`. 

A similar analysis can be applied on selected questions of interest related to risky food behaviour, but only on data collected from F&Y as the census presents demographic data only.
 

### Statistical Analysis

The statistical analysis carried out here is using `chi square` as the data is non-parametric (due to the categorical values nature). It tests for statistical significance between different subgroups of data.

### Correlation Analysis



## Interactive Dashboard


### In the notebook

Instructions on how to run the dashboard yourself are provided in the notebook. 

### On Binder 

In order to run the dashboard online, without the need to run the script, it can be accessed as below:
* go to [Binder](https://mybinder.org/) to launch the repository held remotely 
* select GitHub under __GitHub repository name or URL__ and insert `lorena-gp/food-standards-agency_app`
* select URL under __Path to a notebook file (optional)__ and insert `voila/render/Food-and-You-survey_risks.ipynb`

### Using the app code provided in the `app` folder

## Licensing

This note is to remind the FSA team that an appropriate software licence should be issued. 
