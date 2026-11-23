import pandas as pd
import networkx as nx
from pathlib import Path

df = pd.read_excel(Path(__file__).parent / "form.xlsx")    


print("Excel file loaded successfully")

participant_col = next(
    col for col in df.columns
    if "participant code" in col.lower()
)

connection_col = next(
    col for col in df.columns
    if "who else" in col.lower()
)

df = df.dropna(subset=[participant_col])

participants = df[participant_col].astype(str).str.strip().tolist()
participant_set = set(participants)

directed = nx.DiGraph()
directed.add_nodes_from(participants)

for _, row in df.iterrows():
    person = str(row[participant_col]).strip()
    answer = row[connection_col]

    if pd.isna(answer):
        continue

    answer = str(answer).strip()

    if answer.lower() == "nobody":
        continue

    names = answer.replace(";", ",").split(",")

    for name in names:                                 
        name = name.strip()                             
        if name in participant_set and name != person:  
            directed.add_edge(person, name)             

results = pd.DataFrame({                                
    "Participant": participants,                        
    "Nominations Made": [directed.out_degree(p) for p in participants],    
    "Nominations Received": [directed.in_degree(p) for p in participants],  
})                                                      

print(results)

results.to_excel(Path(__file__).parent / "AI_Network_Summary.xlsx")