import pymongo
from sentence_transformers import SentenceTransformer

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.sjz9f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.movies

# Load the embedding model locally
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(text) -> list[float]:
    embedding = model.encode(text)
    return embedding.tolist()

# Example usage
# embedding = generate_embeddings("you are doing great job, keep going")
# print(f"Embedding length: {len(embedding)}")
# print(f"First 5 values: {embedding}")


# Process first 50 documents with a 'plot' field
# documents = collection.find({"plot": {"$exists": True}}).limit(50)

# for doc in documents:
#     plot = doc.get("plot", "")
#     if not plot.strip():
#         continue  # Skip if plot is empty or missing

#     embedding = generate_embeddings(plot)

#     # Update document with the new 'embed_plot' field
#     collection.update_one(
#         {"_id": doc["_id"]},
#         {"$set": {"embed_plot": embedding}}
#     )

# print("✅ Done embedding and updating 50 documents!")

query = "The Shawshank Redemption"

result =collection.aggregate([
    {"$vectorSearch": {
        "queryVector": generate_embeddings(query),
        "path": "embed_plot",
        "numCandidates": 100,
        "limit": 4,
        "index": "vector_index_new",
        
    }}])

for document in result:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
# print("✅ Done embedding and updating 50 documents!")s
   
    