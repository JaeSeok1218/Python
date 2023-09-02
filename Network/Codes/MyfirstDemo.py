#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import networkx as nx


# In[2]:


G = nx.DiGraph()
G.add_node('Alice')
G.add_node('Bob')
G.add_node('Chuck')
list(G.nodes())


# In[3]:


G.add_edge('Alice','Bob')
G.add_edge('Alice','Chuck')
G.add_edge('Bob','Alice')
G.add_edge('Bob','Chuck')
list(G.edges())


# In[4]:


nx.draw_circular(G,node_color='C0', node_size=2000, with_labels=True)
plt.show()


# In[5]:


positions = dict(OKC=(-97, 35),
                Dallas=(-96,32),
                KansasCity=(-94,39),
                Denver=(-104,39))
positions['OKC']


# In[6]:


G = nx.Graph()
G.add_nodes_from(positions)
G.nodes()


# In[7]:


drive_times = {('OKC','Dallas'):3,
              ('OKC','KansasCity'):5,
              ('KansasCity','Denver'):8,
              ('Denver','OKC'):9}


# In[8]:


G.add_edges_from(drive_times)
G.edges()


# In[9]:


nx.draw(G, positions,
       node_color='C1',
       node_shape='s',
       node_size=2500,
       with_labels=True)

nx.draw_networkx_edge_labels(G,positions,
                            edge_labels=drive_times)
plt.show()
