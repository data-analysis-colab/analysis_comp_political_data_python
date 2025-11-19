# Analysis: _Comparative Political Data Set (1960–2022)_

## Overview

This project investigates the relationship between economic indicators, government spending, and electoral outcomes 
using the _Comparative Political Data Set_ (CPD) covering 1960–2022. It seeks to uncover how shifts in macroeconomic 
variables – such as **unemployment**, **inflation**, **GDP growth**, and **social security transfers** – correlate 
with **changes in government following elections**.

The analysis is structured in three stages:

1. **Data Preparation and Cleaning**
2. **Preliminary Correlation Exploration**
3. **In-Depth Analysis of Predictive Indicators**

## Skills Demonstrated

- **Data Cleaning & Wrangling**:  
Standardizing multi-country time-series data, handling missing values, harmonizing variables, and constructing 
derived indicators.
- **Exploratory Analysis**:  
Correlation analysis, cross-country comparisons, outlier detection, and trend identification.
- **Predictive Indicator Design**:  
Building trend measures, applying election-timing logic, aligning indicators with electoral cycles, and evaluating 
economic trends as predictors of government turnover.
- **Collaborative Research & Workflow Coordination**:  
Working closely and effectively with a colleague to design the analytical approach, divide responsibilities, review 
each other’s work, and maintain a clear, structured workflow – ensuring consistent methodology and high-quality results 
throughout the project.
- **Visualization**:  
Producing multi-decade plots, predictor comparison charts, and completeness diagnostics.
- **Python Analysis Workflow**:  
Pandas/NumPy operations, custom filtering functions, and structured multi-notebook analysis.
- **Political Science Application**:  
Applying macroeconomic voting theory and integrating multidisciplinary literature into empirical analysis.

## Project Stages

### 1. Data Preparation and Cleaning

Data Preparation: [Jupyter Notebook 1](01_data_preparation.ipynb)  
The CPD dataset is standardized to ensure temporal and cross-country comparability:

- Handled missing values and harmonized variable names
- Derived time-series metrics for longitudinal analysis

>Key findings:
>- Post-communist countries exhibit lower observation counts, mainly due to later dataset entry
   (1990–1993, Croatia: 2000).
>- Data completeness for these countries improves over time, as shown by shrinking observation count gaps.
>- Null-values in columns like `elect` and Gini indices are expected due to non-annual measurement.

Visualization: [Yearly Observation Counts for Post-Communist Countries (1993–2022)](figures/(01)_yearly_observation_count.png)

### 2. Preliminary Correlation Exploration

Correlation Exploration: [Jupyter Notebook 2](02_correlation_exploration.ipynb)  
Initial exploration identifies candidate relationships between socio-economic indicators and electoral outcomes.

#### a. Voter Turnout and Education Funding

- Examines correlation between government expenditure on education (`educexp_gov_ipol`) and voter turnout (`vturn`).
- Inspired by Burden (2009), Inkinen & Saari (2019), Chevalier & Doyle (2012).
- Country-level grouping and mean comparisons suggest a positive trend, albeit with outliers.
- Future work: analyze over time, include private education spending, and compare with other education-related metrics.

Visualization: [Average Government Education Spending vs. Voter Turnout (1960–2022)](figures/(02)_expenditure_education_voter_turnout.png)

#### b. Unemployment and Labor Market Initiatives

- Analyzes Germany’s unemployment rate alongside expenditures on training programs, recruitment incentives, public 
  sector job creation, and startup support.
- Observed covariation between unemployment and spending, though the causal direction remains unclear.
- Suggests further multi-country, lag-adjusted exploration.

Visualization: [Labor Market Expenditure vs. Unemployment Rate (Germany, 1960–2022)](figures/(03)_labor_market_training_unemp_gr.png)

#### c. Predictors of Election Outcomes

- Focus: whether macroeconomic and fiscal variables predict ideological cabinet changes (`gov_new`).
- Filters elections to exclude terms < 2 years using [filter_elect_column(df)](figures/(04)_function_filter_elect_column.png).
- Adjusts for lagged cabinet formation via an `elect_new_year` column that accounts for elections late in the year:

    ````
    df_cpd["elect_new_year"] = np.where(
        ((df_cpd["elect_filtered"].notnull()) & (df_cpd["gov_new"] == 1)) |
        ((df_cpd["elect_filtered"].dt.month >= 9) & (df_cpd["gov_new"].shift(-1) == 1)) & 
        (df_cpd["elect"].shift(-1).isnull()),
        df_cpd["elect_filtered"].dt.year, None)
    ````
- Enables visual analysis of indicator trajectories around elections for selected countries.

### 3. In-Depth Analysis of Predictive Indicators

Predictive Analysis: [Jupyter Notebook 3](03_predictive_analysis.ipynb)

#### Objective

Quantify the predictive power of economic and fiscal indicators for government turnover, mapping multi-year economic 
shifts onto electoral cycles.

#### Predictor Variables

| Category                                           | Exemplification                                                     | Example Variables                                                                      |
|----------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Negatively evaluated (increases → disapproval)** | Unemployment, inflation, deficits, industrial disputes              | `unemp`, `inflation`, `deficit`, `nld`                                                 |
| **Positively evaluated (increases → approval)**    | GDP growth, social transfers, education spending, childcare, equity | `realgdpgr`, `sstran`, `outlays`, `educexp_gov_ipol`, `childcare_pmp`, `postfisc_gini` |

````
predictor_list_neg = ["unemp", "inflation", "deficit", "nld"]
predictor_list_pos = ["realgdpgr", "sstran", "outlays", "educexp_gov_ipol", "childcare_pmp", "postfisc_gini"]
predictor_list = predictor_list_neg + predictor_list_pos
````

#### Accounting for Election Timing

Since elections occur at varying times of year:

- Calculate mean election month per country
- Group countries into early-year vs. late-year election types
- Apply adjusted logic when attributing annual indicators to electoral terms

#### Analytical Procedure

1. Extract electoral terms (from `elect_filtered`) per country
2. Compute a year-to-year trend direction for each predictor
3. Identify increase/decrease periods and their average rates
4. Find intersections between economic trends and electoral terms
5. Determine whether trend magnitudes exceed country-specific averages
6. Link pre-election trend patterns to government change outcomes (`gov_new`)
7. Aggregate across countries to compute predictive percentages
8. Visualize comparative predictor strengths

**Results/Visualizations** (Sample)

| English                                                                                                   | German                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [Predictors for the Election of New Governments (Germany)](figures/(05a)_predictors_new_gov_ger.png)      | [Vorhersagefaktoren für die Wahl einer neuen Regierung (Deutschland)](figures/(05b)_vorhersagefaktoren_neuen_regierung_de.png)  |
| [Predictors for the Re-Election of Governments (Germany)](figures/(06a)_predictors_re_election_ger.png)   | [Vorhersagefaktoren für die Wiederwahl einer Regierung (Deutschlad)](figures/(06b)_vorhersagefaktoren_wiederwahl_de.png)        |
| [Combined Predictors for Election Outcomes (Germany)](figures/(07a)_combined_predictors_election_ger.png) | [Kombinierte Vorhersagefaktoren für Wahlausgänge (Deutschlad)](figures/(07b)_kombinierte_vohersagefaktoren_wahlausgänge_de.png) |

## Conclusion

This project provides a cross-national, time-series framework for examining how economic performance and fiscal 
policies relate to electoral dynamics over six decades. It integrates data cleaning, exploratory correlation, and 
structured causal inference design-laying the groundwork for predictive modeling of political outcomes.

## References

- Burden, B. C. (2009). ‘The dynamic effects of education on voter turnout’, *Electoral Studies*, Special issue on  
  The American Voter Revisited, 28/4: 540–9. DOI: 10.1016/j.electstud.2009.05.027
- Chevalier, A., & Doyle, O. (2012). ‘Schooling and Voter Turnout: Is There an American Exception?’.  
  SSRN Scholarly Paper, Rochester, NY: Social Science Research Network (https://papers.ssrn.com/abstract=2056729).
- Inkinen, S., & Saari, J. (2019). ‘The Educational Correlates of Voting: A Cross-sectional Study of  
  Finnish Undergraduates’ Turnout in the 2014 European Parliament Election’, *Scandinavian Political Studies*,  
  42/1: 1–24. DOI: 10.1111/1467-9477.12133
- Armingeon, Klaus, Sarah Engler, Lucas Leemann, and David Weisstanner (2024). ‘Comparative Political Data Set  
  (CPD) 1960–2022’, Zurich/Lueneburg/Lucerne: University of Zurich, Leuphana University Lueneburg, and University of Lucerne.

## Authors
Jan H. Schüttler (Linkedin), Behzad Nematipour ([linkedin](https://linkedin.com/in/behzad-nematipour-99b8b4399)) 