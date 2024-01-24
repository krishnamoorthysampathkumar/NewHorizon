from config import model, df
import torch


def most_similar_row(incident_string):
    incident_string_embedding = torch.tensor(model.encode(incident_string))
    cosi = torch.nn.CosineSimilarity(dim=0)
    df["similarity"] = df["embeddings"].apply(lambda x: cosi(incident_string_embedding, x).item())
    closest_matched_rows = df.nlargest(2,["similarity"])
    list_of_matches = []
    for i in closest_matched_rows.index:
        row_dict = {}
        row_dict["similarity_score"] = closest_matched_rows["similarity"][i]
        row_dict["runbook_title"] = closest_matched_rows["runbook_title"][i]
        row_dict["runbook_link"] = closest_matched_rows["runbook_link"][i]
        list_of_matches.append(row_dict) 
    
    return list_of_matches