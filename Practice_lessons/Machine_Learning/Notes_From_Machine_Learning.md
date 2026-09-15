\--------In 90's why the AI fail's-------

* AI Winters were mostly due to scalability issues related to data size and computing power. Please review the Modern AI lesson.





###### **Applications**:



AI solutions include speech recognition, computer vision, assisted medical diagnosis, robotics, and others.   





**Artificial Intelligence:**



It is creating system that mimic human intelligence.



**Machine Learning:**



It is subset of AI, which can learn from data. Algorithms whose performance increases when they exposed to more data over time.



**Deep Learning:**



It is a specialised subset of Machine Learning, which is used with multi-layered neural networks.



Cutting Edge means "the most modern, advanced, and newest stage of development activities.



###### **What doesn't comes under AI and its subsets such as ML, DL:**



* As, we use "**rule-based method**" even through we increased more data to train. This rule-based training on heavy data or huge data will not helpful to improve the accuracy or prediction matching exactly. So, this will not comes under any of AI and its subsets.





##### **First We can go through Machine Learning:**



It is using data to learn patterns to predict the output using of statistical learning models.



* "The study and construction of programs are not explicitly programmed, but learns patterns as they are exposed to more data over time."



* "These programs are repeatedly learn from seeing data, rather than being explicitly programmed by humans.



In Machine Learning, They are two types of learning's:


**Supervised Learning:** 

* Supervised Learning: It is having labels, which means training data has labels, learn by learning models using ml models to predict testing data(unseen) output as labels.



* Structured data is information organized into a predefined format, layout, or schema, making it easily readable and searchable by both humans and machines
* 

**Example:**



* Animals data has labels cat, dog, etc., it will go under training using machine learning models then it will test on unseen (testing data) then predict them as output with labels.





DATA contains          Machine Learning

Labels ---------------->   Models ----------------> Output with Labels.

&#x20;



**Unsupervised Learning:**

* Unsupervised Learning: It doesn't have any labels for training and testing, instead it will learn using features or patterns(clues) of the data and predict it as output with labels or without labels based on data structure.

**Example**:

* Suppose a flowers data set need to predict which type of flower each one, and the dataset contains three types of flowers of same species.
* So, using of petals width, length and sepal width, length using of these features we need to decide which one belongs to which flower type as output.

  * Like, it width and length contains 4.5,3.5 then it belongs to type-1 category, otherwise if the data features matches to any other type of flower then it belongs to those categories.



DATASET ------------> Data Features/patterns(characteristics) training on dataset---------> Machine learning model-------------->Output prediction as labels or without labels.





###### **Machine Learning vs Deep Learning:**



###### **Machine Learning Pipeline:**



**Classic Machine Learning ------> image of a man -------> determine the features (like eyes, nose, eye brows etc.,)------>training with machine learning models-------> Output as labels.**





###### **Deep Learning Pipeline:**



**Image of a person (huge dataset)-------> learns the patterns or features by neural network and applying the model along with layers -------> predicts its output.**





Limitations:



* If the data is less then machine learning models will do better job and data is frequently changes/updated/not steady then the machine learning do better job.



* If the data is huge then deep learning models will give better results, like image classification.







If we take images, it doesn't have labels for input, then it would consider as unsupervised learning.



Now, by taking those image classification's(unsupervised data/unstructured data). we need to go through either features from pixel by pixel within an image. This will address by deep learning models, as traditional machine learning methods fails to achieve it.



and also if the features of each pixel as an individual, we can lose the spatial relationship of the pixels, as the pixels in the image are huge amount. so, machine learning models fails to achieve while deep learning will be doing great with the image feature learning's.









###### **Background and Tools using for Machine Learning and Deep Learning:**

###### 

NumPy -- used for numerical methods.

Pandas -- used for to read the data as data frames.

Matplotlib \& Seaborn -- used for visualisation of data and results.

ScikitLearn -- used for Machine Learning.

TensorFlow \& Keras -- used for Deep Learning specifically.



---



**Steps to follow from end-to-end pipeline:**



* **problem statement -- First we need to pick a problem statement, means it will research or start the process for that problem statement.**
* **Data collection -- next, we need to pick up suitable data or create data by collecting with labels or without labels.**
* **Data Exploration \& Preprocessing -- Next, we need to clean and organise the data into meaningful way/understandable way. (Determine how to clean your data such that you can use it to train a model.)**
* **Modelling -- Build a model to solve this problem or use suitable machine learning models/deep learning models for solving using data.**
* **Validation -- test and validate it on unseen data using the same model, for getting clearance of upto how much this model is telling the truth or lying it.**
* **Deployment or Decision Making -- if it works well then deploy it on cloud platform ex- streamlit, aws, gcp etc., otherwise make a decision with peers or co-leaders where it will improve.** 





###### Machine Learning Frequently used **Vocabulary**



* Target -- category or value that we are trying to predict. (results)
* Features -- the data that are meaningful information which will helpful for prediction of target/results.
* Example/Observation -- a single data point within a row(one row).
* Label -- the target value for a single data point.





