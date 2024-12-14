# Understanding Data Analytics
Data analytics in simple terms is about understanding data by extracting useful information from it. It's a fascinating field that makes sense of the past and provides mechanisms to make valuable predictions about the future. The data analytics process involves *collecting, organising, analysing, and transforming* data into useful information, which drives decision-making. 

Analytical thinking is about identifying and defining a problem and then solving it by using data in an organised, step-by-step manner (Google Data Analytics Professional Certificate: [Foundations: Data, Data, Everywhere](https://www.coursera.org/learn/foundations-data?specialization=google-data-analytics)). A data analyst must have the relevant soft skills: communication, curiosity, problem solving, and creativity.

**Data Analysis** is the process of collecting and analysing data using several statistical and mathematical methods to reveal useful information.

## 📊 Different Types of Analytics
There are 4 main types of analytics that are specific to the respective needs of the data.
|Analytics Type   | Description                           |
|:---------------:|:--------------------------------------|
|Descriptive | It's the simplest analytics form that uses historical data to understand patterns. It does not change anything; it simply aggregates (summarises) and mines the data. The information can then be shared and visualised for further use. |
|Diagnostic | It searches for the **root** cause (the *why*) of behaviours using historical data. This type of analysis tries to understand the cause and correlation between different variables, using data discovery, probability, and regression analysis. |
|Predictive | Attempts to predict future outcomes from historical data using statistical and machine learning techniques. |
|Prescriptive | Uses AI, Algorithms, and Machine Learning to provide actions to be taken from the outcomes of predictive analysis. |

## ⛓️‍💥 The Data Analysis Process
There are different approaches that one can take when performing analytics. The following are the 5 most typical steps involved in a data analysis project:
1. 🧩 Understand the Problem: Know why you are performing an analysis use the follwing as guides:
     - Have a clear definition of the issue or problem to be solved;
     - Know the type of problem: prediction, categorising, pattern finding, and so on;
     - Create a hypothesis to test
     - Helpful Questions to ask:
         - What type of results is needed?
         - Who are the results for?
         - When should the project be completed?
2. 📦 Collect and Prepare the Data: Focus on collecting the relevant data from different relevant sources:
     - Types of Data Sources:
         - Primary or internal data: data that may be readily available from within an organisation;
         - Secondary data: customised data from outside sources;
         - Tertiary data: compiled sources of secondary data
     - Ensure that the data is reliable, original, comprehensive, current, and cited
     - Decide on which format the data should be collected in such as .csv,.txt,.xls, or .json
3. 🧹Clean the Data: Ensure that the data has integrity (accurate, trustworthy, complete, and consitent)
     - Involves dealing with missing values, changing data types and structures, taking random samples for analysis, and removing duplicates
4. 🔎 Analyze the Data: The acutal understanding of the data and using the correct techniques to solve the problem.
5. 🖼️ Visualise and Share the Data: Create different graphs and visuals to represent the findings of the analysis. Select the correct tool to share the findings with those that need it.

## ⚙️ Data Analysis Techniques
There are two types of data: quantitative and qualitative. __Quantitative__ data is data that can be measured (numerical), while __qualitative__ data is data that describes the characteristics of an object. Both types of data have there respective methods.
### Quantitative Techniques
1. Cluster Analysis: aka segmentation or taxonomy analysis is about grouping data into different segments or clusters based on their similarities (homogenous). It is used to find hidden patterns within data.
2. Regression Analysis: Mainly used in predictive analysis to understand the correlation betwwen variables and not the *cause and effect*. It looks at the other factors (independent variables) that may have a relationship with the dependent variable/s.
3. Monte Carlo Simulation: using different scenarios to arrive at a desired outcome.
4. Tine Series Analysis: identifies trends of a variable over time.
5. Cohort Analysis: places data into categories based on similarities and analyses the groups over time.

### Qualitative Techniques
1. Content Analysis: focuses on the frequency of categorical data and the meaning of its context. Can also be used with quantitative data.
2. Sentiment Analysis: evaluates the emotional tone from textual data. A great technique for dealing with customer satisfaction.
3. Thematic Analysis: groups qualitative data into categories based on the frequency that they appear.
4. Grounded Tehory Analysis: creates a hypothesis from the data that was collected and analysed.
5. Discourse Analysis: aims to understand the meaning behind data that is not quantitative.

## Data Analysis Tools
There are numerous tools that can be used in data analysis. The following are some key tools:
- Speadheets: Micorsoft and Google Sheets
- SQL: Structured Query Language for working with databases
- Visualisation Tools: Power BI and Tableau to make static or dynamic visuals
- Programming Languages: Python and R along with relevant libraries like pandas, ggplot, and seaborn are the main programming languages used.

## Business Intelligence
BI is the strategies, processes, and technologies organisations use to collect, analyse, and present data (information) in a meaningful way, to support decision-making. BI dashboards are used to convey important information in snapshots. Dashboards should be interactive, adaptive/responsive, consistent/standardised, relevant/meaningful, illustrative, and use clarity and simplicity.
### Business Metrics
**Conversion Rate (CR)** is the share of customers that make a purchase. Example if 10 people visit a store and 2 of those by something, the the CR is 20%. A **product/marketing funnel** is a sequence of CRs where each steps shows a conversion to the other.

## Data Warehousing
A data warehouse is a large repository for storing data organised in a structured manner. Online Analytical Processing (OLAP) allows you to interact with the data.Online Transaction Processing (OLTP) is the mechanism used to collect payment in online stores. OLTP databases are used to handle everyday transactions for businesses.

Data integration and ETL (Extract, Tranform, Load) involves the collection, transformation, and loading of data from various sources into the data warehouse.
1. Extracting data: process of receiving data from different source file like dbs, csv's and so on, or even from other tables in databases.
2. Transforming data: ensures that the data is cleaned and in the right format to meet the requirements of the warehouse:
     - Data Cleaning: identifying errors and inconsistencies like duplicates, missing values, and null values.
     - Data Integration: multiple data files are placed into a unified format or structure.
     - Data enrichment: adding additional data.
     - Data aggregation: summarising the data.
3. Loading data: the data is loaded in teh warehouse for querying.
     - There are several models of warehouses that the data can be loaded in.

Data Warehousing Models
- **Star Schema**: the center table is the fact table and the other tables surrounding it contains different types of business information such as products, customers, suppliers etc.
- **Snowflake Schema**: An extension of the snow flake where tables are further divided into more specific tables, like having a table for customer address opposed to just leaving it in the customer table.
- **Galaxy Schema**: multiple interconnect start schemas.

Types of OLAP:
- **MOLAP**: Multi-dimensional OLAPs store data in cubes making it efficient for complex queries. The cubes are organised in hierarchies and measures.
- **ROLAP**: data is stored in relational databases in a star or snowflake schema, that makes it efficient for scaling.
- **HOLAP**: combination of MOLAP (stores summary data), and ROLAP (stores detailed information).

OLAP engines and processing are the most value structures that allows the system to be effective. Ensuring that uses can interact with data in a fast, flexible, and insightful way. Aggreation and precomputation can be done in OLAP systems which is the summarising of data at certain levels. OLAP systems are designed to optimise querying by usng algorithms, indexing, and data retrieval methods. Front-end client tools include data visualisation and reporting tools, and adhoc querying tools.

## Cohorts Analysis
It is the process of grouping individuals into cohorts/groups based on common characteristics and tracking the behaviour over time. The reason for this is to discover insights on engagement, retention, and churn rates. Retention rate measures the percentage of cutomers who continue to engage with a product/service overtime. The chrun rate is the percentage of cumstomers that stop using a product over a specific period of time.