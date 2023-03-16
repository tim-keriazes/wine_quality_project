# Predicting the Quality Score of Wine Using Machine Learning
By: [Luis Arce](https://github.com/LuisVArce)
, [Tim Keriazes](https://github.com/tim-keriazes), [Joshua Mayes](https://github.com/MrEnigmamgine)

## Readme Outline
- [Project Description](#project_desc)  
    - [Scenario](#scenario)
    - [Goals](#goals)
        - [Deliverables](#deliverables)
    - [Project Dependencies](#dependencies)

- [About the data](#data)
    - Scope
    - Acquiring
    - Preparing
    - Data Dictionary
    - Key Findings

- [Project Planning](#plan)  
    - Hypothesis
    - Steps
    - Conclusion



# About the project <a name="project_desc"></a>

## Red Wine From the Vihno Verde Region in Portugal - Predicting the Quality Score Using Machine Learning

{Our project examines 11 quantitative features of red/white wine data sets from the Vihno Verde region of Portugal. Using the physicochemical features/breakdown of the wine, we built a predictive machine learning model with a target variable of quality score. Our insights, discoveries, and modeling offer a distinct advantage to wine producers/stakeholders/distributors by using a wine's chemical composition and predicting its associated quality score.}

> __Agile Story__  
    As a `wine producer`  
    I want `predictions of wine quality`  
    So that `I can make better wine`  

## Goals

- MVP Goal : Predict quality score using simple regession model using existing features. RMSE ~1

### Deliverables

- CodeUP Quality README file
- Final Report Notebook
- Slide-driven presentation

## Reproducing this project

{Are there any special considerations one must take to run this project on another machine?  Usually yes.  The most common considerations have been filled out already below.}

### Dependencies

This project makes use of several technologies that will need to be installed
* [![python-shield](https://img.shields.io/badge/Python-3-blue?&logo=python&logoColor=white)
    ](https://www.python.org/)
* [![jupyter-shield](https://img.shields.io/badge/Jupyter-notebook-orange?logo=jupyter&logoColor=white)
    ](https://jupyter.org/)
* [![numpy-shield](https://img.shields.io/badge/Numpy-grey?&logo=numpy)
    ](https://numpy.org/)
* [![pandas-shield](https://img.shields.io/badge/Pandas-grey?&logo=pandas)
    ](https://pandas.pydata.org/)
* [![matplotlib-shield](https://img.shields.io/badge/Matplotlib-grey.svg?)
    ](https://matplotlib.org)
* [![seaborn-shield](https://img.shields.io/badge/Seaborn-grey?&logoColor=white)
    ](https://seaborn.pydata.org/)
* [![scipy-shield](https://img.shields.io/badge/SciPy-grey?&logo=scipy&logoColor=white)
    ](https://scipy.org/)
* [![sklearn-shield](https://img.shields.io/badge/_-grey?logo=scikitlearn&logoColor=white&label=scikit-learn)
    ](https://scikit-learn.org/stable/)

Dependencies can be installed quickly with just a few lines of code.
```
%pip install notebook
%pip install numpy
%pip install pandas
%pip install matplotlib
%pip install seaborn
%pip install scipy
%pip install sklearn
```


# About the data

{Our data is sourced from data.world}

## Scope

The dataset includes 6,497 observations. 0 of which contain nulls and 1,177 of which are duplicates.

5320 observations remain after cleaning, 1359 of which are red wines and 3961 of which are white wines.

## Acquiring

{Both the red and white wine data sets were pulled as .csv files from data.world. }

## Preparing

{The acquired data was in relatively good condition. We checked for nulls, reformatted the features to be more python friendly, and found a decent portion of duplicate data that we had to remove}

## Data Dictionary
---
| **Variable Name** | **Explanation** | **Unit** | **Values** |
| :---: | :---: | :---: | :---: |
| Fixed Acidity |  Acids that do not evaporate readily (Tartaric Acid) | g/L | Float |
| Volatile Acidity | Acids evaporate readily (Acetic acid) | g/L | Float |
| Citric Acid | level of Citric acid | g/L | Float |
| Residual Sugar | Sugar that remains after fermenation | g/L | Float |
| Chlorides | Sodium Chloride content | g/L | Float |
| Free Sulfur Dioxide | Levels of free, gaseous sulfur dioxide | mg/L | Float |
| Total Sulfur Dioxide | Total Level of Sulfur Dioxide | mg/L | Float |
| Density | Density in relation to water | g/cm^3 | Float |
| pH| Acidity of the wine | 1-14 | Float |
| Sulphates | Level of potassium sulfate | g/L | Float |
| Alcohol | Alcohol by Volume per wine | ABV% | Float |
| Quality |  The median value of at least 3 independent evualations by wine experts| 1-10 | Integer | 
| Ions |  The aggregations of ions | g/L | Float |
| Hydronium |  Reverse engineered pH to a continuous variable| mol/L | Float |
|  Additives |  An aggregation of all the additives in the dataset| g/L | Float |



# Project Planning <a name="plan"></a>

Our project makes use of [Trello](https://trello.com/invite/b/QJuhQCLq/e6f31d6c42f14e6e43ac38b3d6775e58/winequality) to manage the individual steps and backlong of the project.


## Initial Hypotheses

- Sugar and alcohol content directly to correlates to wine density
- For white wines, the higher acid content the higher quality
- For red wines, residual sugar content lowers quality score
- Sulfates will have negative impact on quality for both
- High volitile acid content lowers quality for both
- White and red wines may need predicted separately

## Final Results Summary
- The polynomial regressor was the best performing model on both the red and the white wine data sets
- Following the evaluation and extensive modeling, we narrowed down the feature set to the following: ['volatile_acidity','citric_acid','density','alcohol','ions','hydronium','additives']
- We established baselines for use in the model using the mean quality score on the red wine set, and the median quality score on the white wine set.
- We evaluated our models performance using RMSE:
    - Red Wine: on the test set of .738 beating the RMSE on the baseline of .816 by .078
    - White Wine: on the test set of .838 beating the RMSE on the baseline of .893 by .055

## Next Steps
- We would like to look at determining which features were the best features and adjusting accordingly. We found that the features we selected for final modeling yielded the greatest improvement in RMSE versus baseline, but potentially another combination of features/clusters could prove valueable. .
- We would love to increase our data set size and feature set size, potentially exploring things like vintage year, type of grape, fermentation time, or any other details on the wine making process in general.

