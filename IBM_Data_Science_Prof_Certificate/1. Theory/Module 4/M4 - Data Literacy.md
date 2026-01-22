_APIs and Web Scraping (Web harvesting, or web data extraction)_

- APIs and web services allow users to interact with data sources, returning data in various formats(JSON, XML) for analysis
- Web scraping extracts data from unstructured sources, enabling the collection of information from websites for various applications, such as price comparisons and sentiment analysis.
  - Popular web scraping tools such as `BeautifulSoup`, `Scrapy`, `Pandas`, `Selenium`

_Data Streams and RSS (Really Simple Syndication) Feeds_

- Data streams aggregate continuous data from sources like IoT devices and applications, useful for real-time analysis in various fields (e.g., finance, social media).
- RSS feeds capture updated data from online sources, providing a stream of information to users through feed readers.

Metadata is data that provides information about other data. This is the broad definition but we can look at the case or example below:

- 3 main metadata example:
  - Process metadata
    - Describes the processes that operate behind business systems such as data warehouse, accounting systems, or customer relationship management tools.
    - Process metadata for such systems includes tracking things like:
      - process start and end times
      - disk usage
      - where data was moved from and to, and
      - how many users access the system at any given time
  - Technical metadata
    - is metadata which defines the data structures in data repositories or platforms, primarily from a. technical perspective.
    - A data catalog, which is an inventory of tables that contain information, like:
      - the name of each database in the enterprise data warehouse
      - the name of each column present in each database
      - the names of every table that each column is contained in
      - the type of data that each column contains
    - Tables that record information about the tables stored in a database, like:
      - each table's name
      - the number of columns and rows each table has
  - Business metadata
    - Users who want to explore and analyze data within and outside the enterprise are typically interested in *data discovery*. They need to be able to find data which is meaningful and valuable to them and know where that data can be accessed from.
    - These business-minded users are thus interested in business metadata, which is information about the data described in readily interpretable ways, such as:
      - how the data is acquired
      - what the data is measuring or describing
      - the connection between the data and other data sources
        Business metadata also serves as documentation for the entire data warehouse system.

_Data Integration Overview_

- Defined as a discipline involving practices, techniques, and tools for ingesting, transforming, and combining data from various sources.
- Key usage scenarios include ensuring data consistency, master data management, data sharing, and data migration.

_Data Integration in Analytics_

- Involves accessing and transforming data from operational systems to provide a unified view for analytics.
- Example: Extracting customer data from sales, marketing, and finance systems to enable comprehensive analysis.

_Modern Data Integration Solutions_

- Typically feature pre-built connectors for diverse data sources, open-source architecture, and support for both batch and continuous data processing.
- Must accommodate big data sources and ensure portability across cloud environments, while addressing data quality, governance, and security needs.

_Choosing the Right Data Repository_

- Understand the use case: Determine if the data is structured, semi-structured, or unstructured, and identify performance requirements.
- Consider data characteristics: Assess the volume of data, whether it needs to be encrypted, and how frequently it will be accessed or updated.

_Access and Compatibility_

- Evaluate access needs: Decide if the data will be accessed frequently or if long-running queries will be performed.
- Check compatibility: Ensure the chosen repository integrates well with existing tools, programming languages, and processes.

_Scalability and Organizational Standards_

- Focus on scalability: Ensure the repository can grow with the organization’s needs.
- Adhere to organizational standards: Be aware of any preferred databases or repositories established by the organization for specific tasks.
  Glossary

| Term                                                  | Definition                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tab-separated values (TSVs)                           | Delimited text files where the delimiter is a tab. Use as an alternative to CSV when literal commas are present in text data                                                                                                                                                       |
| Comma-separated values (CSVs)                         | Delimited text files where the delimiter is a comma. Used to store structured data.                                                                                                                                                                                                |
| Delimited text file formats                           | Text files are used to store data where each line or row has values separated by a delimiter. A delimiter is a sequence of one or more characters specifying the boundary between values. Common delimiters include comma, tab, colon, vertical bar, and space.                    |
| ACID-compliance                                       | Ensuring data accuracy and consistency through Atomicity, Consistecy, Isolation, and Duratbility (ACID) in database transaction                                                                                                                                                    |
| Cloud-based Integration Platform as a Service (iPaaS) | A type of NoSQL database that organizes data in cells grouped as columns, often used for systems requiring high write request volume and storage of time-series or IoT data.                                                                                                       |
| Column-based Database                                 | A type of NoSQL database that organizes data in cells grouped as columns, often used for systems requiring high write request volume and storage of time-series or IoT data.                                                                                                       |
| Data at rest                                          | Data that is stored and not actively in motion, typically residing in a database or storage system for various purposes, including backup.                                                                                                                                         |
| Data integration                                      | A discipline involving practices, architectural techniques, and tools that enable organizations to ingest, transform, combine, and provision data across various data types, used for purposes such as data consistency, master data management, data sharing, and data migration. |
| Data Lake                                             | A data repository for storing large volumes of structured, semi-structured, and unstructured data in its native format, facilitating agile data exploration and analysis.                                                                                                          |
| Data mart                                             | A subset of a data warehouse designed for specific business functions or user communities, providing isolated security and performance for focused analytics.                                                                                                                      |
| Data pipeline                                         | A comprehensive data movement process that covers the entire journey of data from source systems to destination systems, which includes data integration as a key component.                                                                                                       |
| Data repository                                       | A general term referring to data that has been collected, organized, and isolated for business operations or data analysis. It can include databases, data warehouses, and big data stores.                                                                                        |
| Data warehouse                                        | A central repository that consolidates data from various sources through the Extract, Transform, and Load (ETL) process, making it accessible for analytics and business intelligence.                                                                                             |
| Document-based Database                               | A type of NoSQL database that stores each record and its associated data within a single document, allowing flexible indexing, ad hoc queries, and analytics over collections of documents.                                                                                        |
| ETL process                                           | The Extract, Transform, and Load process for data integration involves extracting data from various sources, transforming it into a usable format, and loading it into a repository.                                                                                               |
| Graph-based Database                                  | A type of NoSQL database that uses a graphical model to represent and store data, ideal for visualizing, analyzing, and discovering connections between interconnected data points.                                                                                                |
| Key-value store                                       | A type of NoSQL database where data is stored as key-value pairs, with the key serving as a unique identifier and the value containing data, which can be simple or complex.                                                                                                       |
| Portability                                           | The capability of data integration tools to be used in various environments, including single-cloud, multi-cloud, or hybrid-cloud scenarios, provides flexibility in deployment options.                                                                                           |
| Pre-built connectors                                  | Cataloged connectors and adapters that simplify connecting and building integration flows with diverse data sources like databases, flat files, social media, APIs, CRM, and ERP applications.                                                                                     |
| Relational databases (RDBMSes)                        | Databases that organize data into a tabular format with rows and columns, following a well-defined structure and schema.                                                                                                                                                           |
| Scalability                                           | The ability of a data repository to grow and expand its capacity to handle increasing data volumes and workload demands over time.                                                                                                                                                 |
| Schema                                                | The predefined structure that describes the organization and format of data within a database, indicating the types of data allowed and their relationships.                                                                                                                       |
| Streaming data                                        | Data that is continuously generated and transmitted in real-time requires specialized handling and processing to capture and analyze.                                                                                                                                              |
| Use cases for relational databases                    | Applications such as Online Transaction Processing (OLTP), Data Warehouses (OLAP), and IoT solutions where relational databases excel.                                                                                                                                             |
| Vendor lock-in                                        | A situation where a user becomes dependent on a specific vendor's technologies and solutions, making it challenging to switch to other platforms.                                                                                                                                  |
