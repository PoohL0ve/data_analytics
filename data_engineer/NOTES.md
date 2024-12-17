# Data Engineer

## Understanding Data Engineering
The data workflow:
- Data Collection and Storage -> Data Preparation -> Exploration and Visualisation -> Experimentation and Prediction

Data engineers are responsible for the first step in the workflow. They lay the ground work for Data Analyst, Scientist and Engineers. Data Engineers deliver the right data in the most suitable form to persons interested in it, as efficiently as possible.

Responsibilities:
- Collect data from different sources.
- Optimise databases for analysis.
- Remove corrupted data
- Develop, construct, test, and maintain data architectures such as
    - databases and processes to handle large amounts of data.

Big Data is constructed of Five Vs:
- **Volume**: the size, how much?
- **Variety**: the kind or type.
- **Velocity**: frequency of data generation and process.
- **Veracity**: trustworthiness and accuracy of the data sources.
- **Value**: how useful is the data?

Data Engineers enable Data Scientists.
|Data Engineer           | Data Scientist   |
|:----------------------:|:----------------:|
| Ingest and store data| Exploit data|
| Set up databases | Access Databases |
| Build data pipelines | Use pipeline outputs |
| Strong software skills| Strong analytical skills|

**Data pipelines** automate the flow of data from one place to another, providing accurate, up-to-data, and relevant data. Pipelines ensure an efficient flow of data:
- **Automate**
    - Extracting
    - Transforming
    - Combining
    - Validating
    - Loading
- **Reduce**
    - Human Intervention
    - Errors
    - Time it takes data to flow

ETL is a framework for dividing data pipelines. Sometimes it may not be followed and data may be loaded directly to a system.

### Data Storage
**Structured data** is organised and easy to search. The data is modeled in rows and columns with defined types. They are stored in relational databases and the data can be grouped to form relations. About 20% of data is structured.

**Semi-structured** data is less rigid and uses NoSQL databases with file formats like json, XML, and YAML. They can be ggrouped by it's strenous.

Unstructured data does not follow a model, making hard to search and organise. It is usually text, picture, sound, or videos. They are normally stores in datalakes, although they can be found in data warehouses and databases. Most of the data is unstructured. AI can be used to organise and structure data.

| Data Lakes           | Data Warehouse           |
|:--------------------:|:------------------------:|
| Store the raw data | Store specific data for specific use|
|Can take petabytes (1mil Gbs)| Relatively small |
|Stores all data structures| Enforce a structured format |
|Cost-effictive| More costly to update|
|Difficult to analyse| Optimised for analysis|
| Requires an up-to-date catelog| Does not |
|Used by data scientist| Used by data analyst and business analyst|
|Big data, real time analytics| Adhoc, read only queries|

A data catelog keeps track of where the source of the data, who owns the data, where the data is used and how often it is updated. It is good practice in terms of data governance and it ensures reproducibility. It is also good for reliability, scalability, speed, and autonomy.

A database has a general definition, while a data warehouse is a type of database.

### Moving and Processing Data
Data processing is about converting raw data into meaningful information. It involves converting data types from one type to another. It is good for organising data and can help by saving memory usage.

**Scheduling** is the glue of the system that holds each piee and organise how they work together. It runs tasks in a specific order and resolves all dependencies. Types of scheduling:
- Manual
- Automatically run at a specific time
- Sensor schelduling: Automatically run if a specific condition is met.

Data can be ingested in batches, which is groups at intervals. Batch data is often cheaper. Data can be streamed where data is send through the pipeline as soon as it is updated.

Parallel computing/processing is necessary for memory and processing power. It splits tasks into smaller ones and distribute them to different computers.