import rw
import numpy as np

outfile='log.csv'
header=1

toygraphs=rw.Toygraphs({
        'numgraphs': 5,
        'graphtype': "steyvers",
        'numnodes': 50,
        'numlinks': 6,
        'prob_rewire': .3})

toydata=rw.Toydata({
        'numx': range(5,40),
        'trim': .7,
        'jump': 0.0,
        'jumptype': "stationary",
        'startX': "stationary"})

irts=rw.Irts({
        'data': [],
        'irttype': "gamma",
        'beta': (1/1.1), 
        'irt_weight': 0.9,
        'rcutoff': 20})

#TODO: add window params (c)?
fitinfo=rw.Fitinfo({
        'startGraph': "windowgraph_valid",
        'windowgraph_size': 2,
        'windowgraph_threshold': 2,
        'followtype': "avg", 
        'prior_samplesize': 10000,
        'recorddir': "records/",
        'prune_limit': 100,
        'triangle_limit': 100,
        'other_limit': 100})

# optionally, pass a methods argument
# methods=['fe','rw','uinvite','uinvite_irt','uinvite_prior','uinvite_irt_prior','windowgraph','windowgraph_valid'] 

for td in toydata:
    rw.toyBatch(toygraphs, td, outfile, irts=irts, fitinfo=fitinfo, start_seed=1, methods=['uinvite'],header=header,debug="T")
    header=0
