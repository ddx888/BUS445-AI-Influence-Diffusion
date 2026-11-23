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
        other_person = name.strip().upper()

        if other_person in participant_set and other_person != person:
            directed.add_edge(person, other_person)

mutual = nx.Graph()
mutual.add_nodes_from(participants)

for person, other_person in directed.edges():
    if directed.has_edge(other_person, person):
        mutual.add_edge(person, other_person)

either = nx.Graph()
either.add_nodes_from(participants)
either.add_edges_from(directed.edges())

def get_results(graph):
    people = graph.number_of_nodes()
    connections = graph.number_of_edges()
    possible_pairs = people * (people - 1) // 2
    groups = list(nx.connected_components(graph))

    return {
        "Participants": people,
        "Connections": connections,
        "Possible Pairs": possible_pairs,
        "Density": round(nx.density(graph), 4),
        "Average Degree": round(sum(dict(graph.degree()).values()) / people, 4),
        "Connected Components": len(groups),
        "Largest Component": max(len(group) for group in groups),
        "Isolated Participants": len(list(nx.isolates(graph)))
    }

results = pd.DataFrame({
    "Mutual Report Network": get_results(mutual),
    "Either Report Network": get_results(either)
})

print("Total Nominations:", directed.number_of_edges())
print(results)