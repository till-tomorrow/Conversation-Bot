# Conversational-Bot
Conversational Bots

•	Literature Survey:

1.	Neural Responding Machine for Short-Text Conversation , Link: http://arxiv.org/pdf/1503.02364v2.pdf
2.	Predicting the next sequence given the previous sequence or sequences using recurrent networks, Link: https://arxiv.org/pdf/1410.8206v4.pdf
3.	Neural Conversational Model, Link: http://arxiv.org/pdf/1506.05869v3.pdf
4.	Named Entity Recognition in Tweets, Link: http://turing.cs.washington.edu/papers/ritter-emnlp2011-twitter_ner.pdf
5.	A Neural Network Approach to Context-Sensitive Generation of Conversational Responses, Link: http://arxiv.org/pdf/1506.06714v1.pdf
6.	Attention with Intention for a Neural Network Conversation Model, Link: http://arxiv.org/pdf/1510.08565v3.pdf
7.	How to Generate a Good Word Embedding, Link: http://arxiv.org/pdf/1507.05523v1.pdf


•	High Level Architecture:
1. Data Collection:
- This could be done using the data available online using fashion domain websites or through some open source data, if available.
- We can create our own data which will be like a conversation between two people related to fashion domain.
2. Word Embeddings:
- Used Gensim to get the word embeddings.
3. Clustering:
- Used K-means clustering to cluster semantically similar words.
		
•	Sample Conversation:
U: Hi
C: Hello
U: I’m looking for green shirts with floral pattern.
C: This is what I’ve found for you … <URL with filters>
U: I’m looking for a small sized shirt.
C: This is what I have found for you… <URL with filters>

•	Intent Identification in the query made by the user:
- Currently we are focussing on “Search” as our intent, which we’ll be extending later.
- To identify our intent, we’re making use of POS in the query and lemmatization while pre-processing the query. POS is used for performing the lemmatization.
- After this, we get a Part of Speech tag for each word in the query. This is used in the later stages.

•	Approach for identifying entity (in the query) cluster:
- Type of clothing (TOC): Our system trains on the type of data which should cluster all the clothing types together. Once the user query comes in, we can search for all the nouns from the query (since TOC should be a noun). The noun which is present in the TOC cluster is our clothing type. Our API can only identify “dresses” as TOC at the moment. So, we can categorise them into “dress” and “not-a-dress”. 
- Color: After embeddings we should get a color cluster. Identify all the nouns in the query. Use those words to search in the cluster.
- Length: Three available, maxi, midi, mini. Need to identify these using a predefined dictionary.
- Size: Four available, S, M, L and XL. Need to identify these using a predefined dictionary.

