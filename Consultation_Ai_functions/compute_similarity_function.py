from sentence_transformers import SentenceTransformer, util

def compute_similarity(text1, text2):
    model_name = 'sentence-transformers/paraphrase-MiniLM-L6-v2'
    model = SentenceTransformer(model_name)
    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings1, embeddings2).item()
    similarity_percentage = similarity * 100
    return similarity_percentage
