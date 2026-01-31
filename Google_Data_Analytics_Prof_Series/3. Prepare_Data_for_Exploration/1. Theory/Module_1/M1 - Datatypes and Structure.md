Selecting the right data:
![[Pasted image 20260123160936.png]]

*Scenario*
A grocery store chain purchases customer data from a credit card company. The grocer uses this data to identify its most loyal customers and offer them special promotions and discounts. What type of data is being used in this scenario?

--> So this type of scenario, the data that being used is `Second-Party` data.

<u>*Internal vs External Data*</u>
- Internal Data is data that generated within organization that used to monitor the organization operation
- External Data. data that acquired from outside sources that mostly used to analyze the market trend or context, trend and more. 

<u>*Discrete vs Continuous Data*</u> 
- Discrete data refers to all data that involves countable, distinct value (people in room)
- Continuous, includes any value within range, requiring measurement (height, temperature)

<u>*Nominal vs Ordinal Data*</u>
- Nominal refers unordered data that used for labeling and counting frequency (like gender, color)
- Ordinal refers data that can be categorized in order or rank and intervals between values are not equal. 

<u>*Wide and Long Data* </u>
- Wide Data is data in which every data subject has a single row with multiple columns to old the values of various of attributes of the subject 
- Long Data is data in which each row is one time point per subject, so subject will have data in multiple rows.

<u>*Data Modeling* </u>
Data modeling is a process of creating diagrams that visually represent how data is organized and structured
- It is used to organized data elements and how they related to one another.
- Helps keep data consistent and enable people not map 
- There are 3 most common types of data modeling process:
	- **Conceptual** - Business concept: high level view of data structure such as how data interacts across an organization 
	- Example, a conceptual data model may be used to define the business requirements for a new database. A conceptual data model doesn't contain technical details.
	- **Logical** - Data Entities focuses on the technical details of a database such as relationships, attributes, and entities.
	- For example, a logical data model defines how individual records are uniquely identified in a database. But it doesn't spell out actual names of database tables. That's the job of a physical data model.
	- **Physical** - Physical tables: Depicts how database operates 
		- A physical data model defines all entities and attributes used; for example, it includes table names, column names, and data types for the database.
![[Pasted image 20260127100709.png]]
- 2 popular techniques of modeling data are:
	- Entity Relationship Diagram (ERD)
	- Unified Modeling Language (UML)
- NOTE: As a junior data analyst, you won't be asked to design a data model but you might come across existing data models of organization that already has in place

## Reflection
**Scenario**: An entertainment website displays a start rating for a movie based on user reviews. Users can select from one to five whole stars to rate the movie. The star rating is an example of what type of data? Select all that apply.  
-> **Answer**: So this type of data are Discrete and Ordinal

Reflection Practice on [https://github.com/googlecreativelab/quickdraw-dataset](https://github.com/googlecreativelab/quickdraw-dataset)  
**Questions 1:**
Consider the doodles you found in the Quick, Draw! dataset:
- What did you notice as you explored drawings in different categories? Are there consistent themes among the pictures in a category? 
- If you didn’t know the category labels, how would you distinguish the pictures from one another? What would you look for?

**Answer**:
- As I explored different categories, I noticed that drawings varied in detail but shared clear visual similarities within each group. Many categories showed consistent shapes, proportions, and symbols, suggesting that people rely on common mental models when representing the same object quickly. And Without category labels, I would distinguish drawings by identifying repeated visual features such as outlines, dominant shapes, and typical components. I would look for patterns in structure, orientation, and relative size to group similar drawings together.
- Reflecting on the categories, some were easier to recognize due to strong visual conventions, while others overlapped and required more careful observation. This highlights how human perception naturally groups images based on shared features, even when individual drawings differ in style

**Questions 2** :
Consider what you know about structured and unstructured data and how it connects to the Quick, Draw! website:
- How would you describe the Quick, Draw! doodles you explored from a data point of view? For instance, how are these doodles organized? Would you be able to store this type of data in a database?
- How are these doodles different from or similar to other types of data that you have encountered?
- What about this data makes it unstructured?

**Answer**: 
- From a data perspective, Quick, Draw! doodles are collections of user-generated sketches organized by category labels and timestamps. Each doodle can be stored in a database as stroke coordinates with metadata, making storage possible, but requiring preprocessing to make the data suitable for analysis or modeling.
- These doodles are similar to image and sensor data I have encountered because they capture raw human input. However, they differ from structured data like tables or spreadsheets, as their meaning is not immediately explicit and must be inferred through patterns, shapes, and learned representations.
- The data is considered unstructured because it does not follow a fixed schema that directly describes meaning. The strokes and pixels do not inherently define categories or attributes, requiring interpretation, feature extraction, or machine learning to transform them into structured insights.