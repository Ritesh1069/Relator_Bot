#gcn model made by ritesh which was further optimized by Aishwarya
import torch
import torch.nn as nn
import torch.nn.functional as F
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data
import numpy as np
import filter_dataset
from pyvis import network as net

# df = pd.read_csv("/random_data.csv")
# user_name = input("Enter user name: ")
# gender = input("Enter gender: ")
# df1 = pd.read_csv("profile_dataNewest.csv")
user_name = "Ashley1"
df1 = pd.read_csv("R:/Git/Relator_Bot/test datasets/1000_location.csv")
df = filter_dataset.filter_ds(user_name, df1)
torch.manual_seed(34)

def gcn_main():
    G = nx.Graph()
    label = {}
    likes = {}
    search = {}

    for i, (user, category) in enumerate(zip(df['first_name'], df['categories'])):
        label[i] = user  # Use index as node label
        search[user] = i
        G.add_node(i, title=user, label=user)
        likes[user] = category
        
    for u in range(len(label)):
        for v in range(len(label)):
            if u != v:
                categories1 = set(likes[label[u]].split(','))
                categories2 = set(likes[label[v]].split(','))
                common_categories = categories1.intersection(categories2)
                union_categories = categories1.union(categories2)
                similarity_score = float(len(common_categories) / len(union_categories)) * 100
                if common_categories:
                    G.add_edge(u, v, weight=similarity_score)

    if G.number_of_edges() == 0:
        print("Error: The graph has no edges.")
        return

    edges = list(G.edges())

    x = torch.randn(len(label), 16)
    # print("output:", x)   #tensor output display
    edge_index = torch.tensor(edges).t().contiguous()
    data = Data(x=x, edge_index=edge_index)

    gcn_model = GCNModel(input_dim=16, hidden_dim=32, output_dim=1)

    gcn_output = gcn_model(data)

    visualize_graph(G, label, search, gcn_output, likes)

    # return gcn_output

class GCNModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GCNModel, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, output_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        return x 

def visualize_graph(G, label, search, gcn_output, likes):
    # pos = nx.shell_layout(G)
    # nx.draw(G, pos, labels=label, with_labels=True, node_size=500)
    # plt.draw()
    # plt.show() #graph display
    
    user_index = search.get(user_name)
    if user_index is not None:
        get_score(G, label, user_index, gcn_output, likes)
    else:
        print("User not found.")

    nt = net.Network(notebook=True, cdn_resources='remote', height="900px", width="100%", bgcolor="#222222", font_color="white")
    nt.barnes_hut()
    nt.from_nx(G, default_node_size=100, show_edge_weights=True, edge_scaling=True)
    neighbor_map = nt.get_adj_list()
    
    for node in nt.nodes:
        neighbors = neighbor_map[node["id"]]
        neighbor_labels = "\n".join(label[i] for i in neighbors)
        node["title"] += " Neighbors: \n" + neighbor_labels
        node["value"] = len(neighbor_map[node["id"]])

    nt.prep_notebook()
    print("\nUsers data stored in: ")
    nt.show(f'UserData/{user_name}.html')

def get_score(G, label, user_index, gcn_output, likes):
    user_score = {}
    user_embedding = gcn_output[user_index].detach().numpy()
    for other_user_index in range(len(label)):
        if user_index != other_user_index:
            other_user_embedding = gcn_output[other_user_index].detach().numpy()
            similarity_score = float(
                1.0 / (1.0 + np.linalg.norm(user_embedding - other_user_embedding))  # Cosine similarity
            )
            user_score[other_user_index] = similarity_score

    print("Compatibility Scores: ")
    for other_user_index, score in sorted(user_score.items(), key=lambda x: x[1], reverse=True):
        common_categories = set(likes[label[user_index]].split(',')).intersection(set(likes[label[other_user_index]].split(',')))
        if common_categories:
            print(f"{label[user_index]} --> {label[other_user_index]}: {score}\nCommon Categories: {', '.join(common_categories)}")

gcn_main()