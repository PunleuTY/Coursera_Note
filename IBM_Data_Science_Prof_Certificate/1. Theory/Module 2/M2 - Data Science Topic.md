# Cloud Computing topic
-  **Cloud computing** delivers on-demand IT resources such as Networks, Servers, Storage, Applications, Services, Data Centers. Over the internet on a pay-for-use basis. 
- Cloud Computing consists of 
	- 5 characteristics 
		- ==On-demand self-service== means that you get access to cloud resources such as processing power, storage, and network you need, using just simple interface, without requiring human interaction. 
		- ==Broad network access==, cloud computing resources can be accessed via the network through standard mechanisms and platforms such as mobile phones, tablets, laptops and workstation 
		- ==Resource pooling== is the practice of combining computing resources(like servers, storage, network) from multiple sources into a shared pool, dynamically assigning them to multiple users(tenants) as needed
		- ==Rapid elasticity== 
		- ==Measured service==, resource usage (storage, processing, bandwidth) is monitored, controlled, and reported, allowing for pay-per-use billing
	- 3 deployment models
		- Public Cloud
		- Private Cloud
		- Hybrid Cloud 
	- 3 service models
		- IaaS
		- PaaS
		- SaaS
# Big Data topic
Big data refers to the dynamic, large, and disparate volumes of data being created by people, tools, and machines.
- It requires new innovative and scalable technology to collect, host, and analytically process the vast amount of data gathered in order to derive real-time business insight that related to consumers, risk, profit, performance, productivity management, and enhanced shareholder value. 
- The V's of Big Data
	- `Velocity` is the speed at which the data is created and how fast it moves. 
	-  `Volume` is the amount of data qualifying as big data.
	- `Value` is the value the data provides 
	- `Variety` is the diversity that exists in the types of data 
	- `Veracity` is the data quality and accuracy 
- Tools that can be used to working with big data such as ``Apache Spark``, `Hadoop`. 
	- **Apache Hadoop** is a collection of tools that provides distributed storage and processing of big data.
		- Distributed storage and processing of big data across ==clusters of computers==
		- Hadoop can scale up from a single node to any number of nodes, each offering local storage and computation.
		- Provides Reliable scalable and cost-effective solution for storage with no format requirements
		- ==Benefits==:
			- Better real-time data-driven decisions
			- Improved data access and analysis
			- Data offload and consolidation 
		- 4 main components of Hadoop are :
			- ==Hadoop distributed file system (HDFS)== is a storage system for big data that runs on multiple commodity hardware connected through a network. 
				- provides scalable and reliable big data storage by <u>partitioning files over multiple nodes</u>
				- splits large files across multiple computers, allowing parallel access to them
				- replicates file blocks on different nodes to prevent data loss. 
			- ==Yet another resource negotiator (YARN)==
			-  MapReduce
			- Hadoop Common 
	- **Apache Hive** is a data warehouse for data query and analysis that built on top of Hadoop.
		- An open-source data warehouse software for reading, writing, and managing large dataset files that are stored directly in either HDFS or other data storage system such sa Apache HBase
	- **Apache Spark** is distributed analytics framework for complex real-time data analytics. 

Big data processing technologies provides ways to work with large sets of structured, semi-structured, and unstructured data so that value can be derived from big data. 

- ==Data mining== is started after appropriately processed, transformed, and stored, which is the steps to discovering hidden patterns, trends and anomalies in large dataset using techniques from data analysis include parametric and non-parametric, ML algorithms, statistics method. 
  
  Data Mining is the process of automatically searching and analyzing data to discover patterns which involves data preprocessing the use of various tools, from visualization to machine learning models. 
  
	- Data Mining process steps:
		- `Setting goal` - Identify key questions
		- `Select data` - Identify data sources
		- `Process data` - Clean the data
		- `Transform data` - Determine storage needs
		- `Data mine` - Determine methods and analyze
		- `Evaluate` - Assess outcomes, and share results
	- After result have been extracted from Data Mining process, we can perform formal evaluation of the results, which include testing the predictive capabilities of the models on observed data to see how effective and efficient the algorithms have been reproducing data which typically called "in-sample forecast".
		- In-sample forecast is the process of predicts outcomes using *<u>the sample historical data</u>* that model was trained on, evaluating how well the models fits with past data. 
	- **TLDR**; 
	  Data mining and evaluating the results becomes an iterative process such that the analysts use better and improved algorithms to improve the quality of results generated in light of the feedback received from the key stakeholders.

# Glossary

| Term                            | Definition                                                                                                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Big Data Cluster                | A distributed computing environment comprising thousands or tens of thousands of interconnected computers that collectively store and process large datasets.                  |
| Chief Data Officer (CDO)        | An emerging role responsible for overseeing data-related initiatives, governance, and strategies, ensuring that data plays a central role in digital transformation efforts.   |
| Chief Information Officer (CIO) | An executive is responsible for managing an organization's information technology and computer systems, contributing to technology-related aspects of digital transformation.  |
| Data Algorithms                 | Computational procedures and mathematical models used to process and analyze data made accessible in the cloud for data scientists to deploy on large datasets efficiently.    |
| Data Replication                | A strategy in which data is duplicated across multiple nodes in a cluster to ensure data durability and availability, reducing the risk of data loss due to hardware failures. |

# AI AND DATA SCIENCE 
- **Machine Learning ML** is a subset of AI that enables computers to learn from data without explicit programming.
- **Deep Learning DL** is a specialised form of ML, use neural networks to simulate human decision-making and improve accuracy over time. 

*<u>Understanding the distinction between AI and DS</u>*
- Data Science encompasses the methods extracting insights from data, involving various disciplines like mathematics and statistics. 
- AI focuses on enabling machines to learn and make decisions, while DS is broader, incorporating AI techniques to analyze data. 

*<u>Generative AI Overview</u>*
- Generative AI is a subset of artificial intelligence that creates new data rather than just analyzing existing data.
- It utilizes deep learning models like Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs) to learn patterns from large datasets.

*<u>Applications of Generative AI</u>*

- In natural language processing, tools like OpenAI’s GPT-3 generate human-like text, enhancing content creation.
- In healthcare, generative AI synthesizes medical images, aiding in training for medical professionals.

<u>Role of Data Scientists</u>

- Data scientists use generative AI to create synthetic data, augmenting datasets with similar properties to real data for model training.
- Generative AI automates coding and generates business insights, allowing data scientists to focus on higher-level analytical tasks.

# Glossary 

| Term | Definition | Video where the term is introduced |
|------|------------|-----------------------------------|
| Artificial Neural Networks | Collections of small computing units (neurons) that process data and learn to make decisions over time. | Artificial Intelligence and Data Science |
| Bayesian Analysis | A statistical technique that uses Bayes' theorem to update probabilities based on new evidence. | Applications of Machine Learning |
| Business Insights | Accurate insights and reports generated by generative AI can be updated as data evolves, enhancing decision-making and uncovering hidden patterns. | Generative AI and Data Science |
| Cluster Analysis | The process of grouping similar data points together based on certain features or attributes. | Neural Networks and Deep Learning |
| Coding Automation | Using generative AI to automatically generate and test software code for constructing analytical models, freeing data scientists to focus on higher-level tasks. | Generative AI and Data Science |
| Data Mining | The process of automatically searching and analyzing data to discover patterns and insights that were previously unknown. | Artificial Intelligence and Data Science |
| Decision Trees | A type of machine learning algorithm used for decision-making by creating a tree-like structure of decisions. | Applications of Machine Learning |
| Deep Learning Models | Includes Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs) that create new data instances by learning patterns from large datasets. | Generative AI and Data Science |
| Five V's of Big Data | Characteristics used to describe big data: Velocity, Volume, Variety, Veracity, and Value. | Neural Networks and Deep Learning |
| Generative AI | A subset of AI that focuses on creating new data, such as images, music, text, or code, rather than just analyzing existing data. | Generative AI and Data Science |
| Market Basket Analysis | Analyzing which goods tend to be bought together, often used for marketing insights. | Neural Networks and Deep Learning |
| Naive Bayes | A simple probabilistic classification algorithm based on Bayes' theorem. | Applications of Machine Learning |
| Natural Language Processing (NLP) | A field of AI that enables machines to understand, generate, and interact with human language, revolutionizing content creation and chatbots. | Generative AI and Data Science |
| Precision vs. Recall | Metrics used to evaluate the performance of classification models. | Applications of Machine Learning |
| Predictive Analytics | Using machine learning techniques to predict future outcomes or events. | Neural Networks and Deep Learning |
| Synthetic Data | Artificially generated data with properties similar to real data, used to augment datasets and improve model training. | Generative AI and Data Science |
