# Geneate graphs from real data

import networkx as nx
import rw
import numpy as np

#subs=['S101','S102','S103','S104','S105','S106','S107','S108','S109','S110',
#      'S111','S112','S113','S114','S115','S116','S117','S118','S119','S120']
subs=['S1','S2','S3','S4','S5','S7','S8','S9','S10','S11','S12','S13']

toydata=rw.Toydata({
        'numx': 3,
        'trim': 1,
        'jump': 0.0,
        'jumptype': "stationary",
        'priming': 0.0,
        'startX': "stationary"})

fitinfo=rw.Fitinfo({
        'startGraph': "fully_connected",
        'windowgraph_size': 2,
        'windowgraph_threshold': 2,
        'followtype': "avg", 
        'prior_samplesize': 10000,
        'recorddir': "records/",
        'directed': False,
        'prune_limit': np.inf,
        'triangle_limit': np.inf,
        'other_limit': np.inf})

toygraphs=rw.Toygraphs({
        'numgraphs': 1,
        'graphtype': "steyvers",
        'numnodes': 280,
        'numlinks': 6,
        'prob_rewire': .3})

irts=rw.Irts({
        'data': [],
        'irttype': "exgauss",
        'lambda': 0.721386887,
        'sigma': 6.58655566,
        'irt_weight': 0.95,
        'rcutoff': 20})

for subj in subs:
    print subj
    category="animals"
    Xs, items, irts.data, numnodes=rw.readX(subj,category,'./Spring2016/results_cleaned.csv',ignorePerseverations=True)
    toydata.numx = len(Xs)

    # u-invite
    uinvite_graph, bestval=rw.uinvite(Xs, toydata, numnodes, fitinfo=fitinfo)

    # rw
    rw_graph=rw.noHidden(Xs, numnodes)

    # windowgraph
    window_graph=rw.windowGraph(Xs, numnodes, td=toydata, valid=0, fitinfo=fitinfo)
    
    g=nx.to_networkx_graph(rw_graph)
    g2=nx.to_networkx_graph(window_graph)
    g3=nx.to_networkx_graph(uinvite_graph)

    nx.relabel_nodes(g, items, copy=False)
    nx.relabel_nodes(g2, items, copy=False)
    nx.relabel_nodes(g3, items, copy=False)

    rw.write_csv([g, g2, g3],subj+".csv",subj) # write multiple graphs
