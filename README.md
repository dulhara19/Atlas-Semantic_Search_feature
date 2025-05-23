# MongoDB Vector Search: Movie Plot Recommendation System

This project demonstrates how to use **vector embeddings** and **semantic search** on movie plots using **MongoDB Atlas** and **SentenceTransformers**. The goal is to find semantically similar movie plots using AI-powered search rather than keyword matching.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**  
    Clone the project repository to your local machine:
    ```bash
    git clone https://github.com/dulhara19/Atlas-Semantic_Search_feature.git
    cd vectorDB
    ```

2. **Install Dependencies**  
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    Alternatively, you can install the dependencies individually:
    ```bash
    pip install pymongo sentence-transformers
    ```

3. **Set Up MongoDB Atlas**  
    - Create a MongoDB Atlas cluster if you don’t already have one.
    - Obtain your MongoDB connection string (URI) and update it in the script.

4. **Run the Script**  
    Execute the script to generate embeddings and perform semantic search:
    ```bash
    python movie_recs.py
    ```

5. **Test the Search**  
    Input a movie plot or query to find similar plots based on semantic similarity.

---

## Example Usage

Here’s an example of how to use the script:

1. Run the script:
    ```bash
    python movie_recs.py
    ```

2. Enter a movie plot or description when prompted:
    ```
    Enter a movie plot: A young wizard discovers his magical heritage and attends a school of witchcraft.
    ```

3. View the top-N similar movie plots returned by the system:
    ```
    Top 3 similar movie plots:
    1. A boy discovers he has magical powers and battles dark forces.
    2. A young girl finds herself in a magical world and must save it from evil.
    3. A group of friends uncover a hidden magical realm and protect it from danger.
    ```

Feel free to modify the script to customize the number of results or adjust the similarity threshold.

## Features

- Connects to MongoDB Atlas using PyMongo
- Uses `sentence-transformers` to generate vector embeddings of movie plots
- Stores the embeddings in MongoDB under a new field `embed_plot`
- Performs semantic similarity search using MongoDB Atlas Vector Search Index
- Retrieves the top-N most similar movie plots to a given query

---
## 🧰 Technologies Used

- Python 3.10+
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) – MongoDB driver
- [SentenceTransformers](https://www.sbert.net/) – to embed plot text into vector space
- MongoDB Atlas – for document storage and vector search
- Pretrained model: `all-MiniLM-L6-v2` (384-dimensional embeddings)

---

📌 Setup Instructions

- Clone the project or download the source code.
- Install required packages:
```bash
pip install pymongo sentence-transformers
```
Edit your MongoDB URI (already done in the code).Run the script to generate embeddings and do semantic search:
```bash
python movie_recs.py

```