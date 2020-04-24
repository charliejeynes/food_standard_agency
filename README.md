# Food Safety in Wales 


The Food Standards Agency (FSA) is a non-ministerial government body that is responsible for food safety and hygiene in England, Wales and Northern Ireland. The FSA gathers information on public food practices by conducting surveys. The Food and You Survey (F&Y) is a flagship biennial study that explores the public's attitudes, knowledge and behaviour relating to food safety and production. Data is analysed and used to compile publicly available reports. 

Wales is demographically distinct to the rest of the UK, being less populous, more deprived, with a larger rural population. For this reason, the FSA was particularly concerned that its F&Y engagement activities do not reach some of the demographic groups in Wales, who may have associated food risks. The following specific questions were posed: 

* Does F&Y survey sampling reflect the true demographic profile of Wales? 
* What food risks are associated with undersampled groups, and what is their understanding of food labelling? 
* Are there any relationships between behaviours related to food safety, and can we predict food risk for specific groups or individuals?


## Team

James Doherty - [Private GitHub](https://github.com/jimmyd83) \
Lorena Garcia-Perez - [Private GitHub](https://github.com/lorena-gp) \
Charlie Jeynes - [Private GitHub](https://github.com/charliejeynes) \
Mishka Nemes - [Private GitHub](https://github.com/mihaelanemes) 


## Timeline

Science to Data Science Virtual School - 23rd of March to 24th of April 2020 \
Hosted and organised by [Pivigo](https://www.pivigo.com/)

## Data sources

[Food and You (F&Y) survey 2010-2018](https://data.gov.uk/dataset/6cae91e7-a5aa-45b4-880d-29b3b7ea93b0/food-and-you-wave-five): Food and You Waves 1-5 Data, csv file, dated on 09 September 2019 \
[Food and You (F&Y) survey guide](https://data.food.gov.uk/catalog/datasets/3f3ad1b7-8cf3-444b-abbf-f784ea4551e1): Select Wave 1 to 5 - Data user guide \
[Census 2011 - microdata with individual entries](https://www.ons.gov.uk/census/2011census/2011censusdata/censusmicrodata/securemicrodata): For data download (isg_regionv2.csv), an account needs to be created [here](https://www.ukdataservice.ac.uk/get-data/how-to-access/registration)


## Data wrangling 

**F&Y survey** - values encoded as 'Not applicable' or 'Not known' were encoded as `NaN`  - apart from the principle component analysis where the data was kept in its original state.  

**Census** - given the higher granularity of the data, data was aggregated to reflect the answer labels in F&Y in order to allow direct comparison. There were no missing values as all demographics were provided for each respondent.


## Repository structure

### `app`
* includes everything required to run the dashboard (the .ipynb file, together with a requirements.txt and the F&Y survey .csv data files). Instructions about which settings to use to run the app from the https://mybinder.org/ website are provided in a .png file. In order to have this app available for anyone online, the relevant files must be localted in a public repository. 

### `data`
*  `microdata_census2011_Wales_prepared.csv` has all the relevant demographic data from the 2011 Census. This includes only the Wales entries for 7 out of 120 original demographics.
*  `survey.csv` includes F&Y survey data from waves 1-5, for Wales, England and Northern Ireland
*  `survey_guide_values.csv` includes data to be parsed in the dictionary that translates answers names 
*  `survey_guide_variables.csv` includes data to be parsed in the dictionary that translates question names 

### `documents`
* `S2DS-2020_FSA_Wales_presentation.pdf` - project presentation for the S2DS programme, presented on 23rd of April 2020
* `S2DS-2020_FSA_Wales_case_study.pdf` - executive summary of the challenge, approach, findings, impact and recommendations 

### `graphs`
* Graphs within the PDFs starting with `foodBehaviour_` can also be visuialized in the dashboard provided here. A greater variety of graphs related to food behaviours by demographics can be visualized on demand by using the dahboard.
* All other PDFs contain graphs that can be plotted only by running the notebook. These are exhaustive in light of the current data.

### `notebooks` 
* `masterscript_with_markdown.ipynb` includes all the code developed for the project. For details, see below.



## Code

Data loading, data wrangling and data analysis are carried out in the `notebooks/masterscript_with_markdown`

### Dictionary 

Two dictionaries were built. The first one translates question names from their short version to their longer, comprehensible, version. The second is a nested dictionary that translates individual answers to each question from their numeric code to a meaningful answer. Their input data is provided in this repository.

### Custom bar plotting functions

`custom_barplots` is a custom plotting function that outputs horizontal barplots with the percentage of people giving a certain answer, and 95% confidence intervals error bars. The names for each of the relevant questions and answers are displayed automatically for each plot title, axis labels and legend thanks to the use of the two dictionaries built. \
`custom_lineplots` is a custom plotting function that ouputs lineplots showing the temporal evolution of the F&Y survey demographics, for Wales, England and Northern Ireland (whose results appear side-by-side, for ease of comparison between the trends for these UK countries). 95% confidence intervals error bars are also displayed, together with the number of respondents (n) and the specific percentage represented by each category. The names for each of the relevant questions and answers are displayed automatically for each plot title, axis labels and legend thanks to the use of the two dictionaries built.

### Data Visualization

Principal Component Analysis (PCA) is used to explore the raw data in order to understand global patterns present within the whole F&Y dataset for Wales.

A timeline of the evolution of the F&Y survey demographics is plotted using `custom_lineplots`. 

Demographic variables (age, gender, marital status, religion, health status, work status, deprivation) are compared between the F&Y survey and the census using `custom_barplots`. 

Demographic variables are also taken into consideration for the analysis of questions of interest related to food safety, using the F&Y survey data and `custom_barplots`.

### Statistical Analysis

To evaluate the significance of the differences under study, `chi square` statistical testing is carried out (being the survey and census datasets non-parametric).

### Correlation Analysis and Predictive Modelling

Correlation analysis is performed on the F&Y survey data to identify which features (questions and their respective answers) correlate the most, positevely or negatively, with the risk of suffering food poisoning.  A preliminary precitive model is also developed, which informs again about the set of the features most relevant for determining food poisoning risk. To fully assess the predictive capability of this model, further work is required.


## Interactive Dashboard

### On the notebook
The dashboard components can be executed within the notebook, where further instructions are included.

### On a website
In order to access the dashboard online:
* go to [Binder](https://mybinder.org/)
* select GitHub under __GitHub repository name or URL__ and insert the appropiate path name (for example, `my-repository/app`) for the remote open repository where the dashboard code is hosted (such as the `app` folder in here). 
* select URL under __Path to a notebook file (optional)__ and insert `voila/render/Food-and-You-survey_risks.ipynb`
