# src: https://kldavenport.com/pure-python-decision-trees/#our-data
# originally from Programming Collective Intelligence: Building Smart Web 2.0 Applications 
# by Toby Segaran
# amazon link: 
# https://www.amazon.com/Programming-Collective-Intelligence-Building-Applications/dp/0596529325
# Slight adoption to the code for Python 3.

import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

my_data=[['slashdot','USA','yes',18,'None'],
        ['google','France','yes',23,'Premium'],
        ['reddit','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['reddit','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['reddit','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]

class decisionnode:
    def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col=col # column index of criteria being tested
        self.value=value # vlaue necessary to get a true result
        self.tb=tb # true decision nodes 
        self.fb=fb # false decision nodes

        # only if leaf node -- no split could have a positive gain
        self.results=results # dict of results for a branch, None for everything except endpoints


def divideset(rows,column,value):
    # Make a function that tells us if a row is in the first group 
    # (true) or the second group (false)
    split_function=None
    # for numerical values
    if isinstance(value,int) or isinstance(value,float):
        split_function=lambda row:row[column]>=value
    # for nominal values
    else:
        split_function=lambda row:row[column]==value
   
   # Divide the rows into two sets and return them
    set1=[row for row in rows if split_function(row)] # if split_function(row) 
    set2=[row for row in rows if not split_function(row)]
    return (set1,set2)

def uniquecounts(rows):
    results={}
    for row in rows:
        # The result is the last column
        r=row[len(row)-1]
        if r not in results: results[r]=0
        results[r]+=1
    return results

# using `defaultdict` -- should produce the same results
from collections import defaultdict
def uniquecounts_dd(rows):
    results = defaultdict(lambda: 0)
    for row in rows:
        r = row[len(row)-1]
        results[r]+=1
    return dict(results)


# Entropy is the sum of p(x)log(p(x)) across all the different possible results
def entropy(rows):
    from math import log
    log2=lambda x:log(x)/log(2)  
    results=uniquecounts(rows)
    # Now calculate the entropy
    ent=0.0
    for r in results.keys():
        # current probability of class
        p=float(results[r])/len(rows) 
        ent=ent-p*log2(p)
    return ent


def buildtree(rows, scorefun=entropy):
    if len(rows) == 0: return decisionnode()
    current_score = scorefun(rows)
    logging.info(f"\n\n>>>Building New Tree\n>>>Current Score: {current_score:0.6f}")
    best_gain = 0.0
    best_criteria = None
    best_sets = None

    column_count = len(rows[0]) - 1 # last column is result
    logging.info(f"Number of features: {column_count}")
    for col in range(column_count):
        logging.info(f"currently considering column {col+1}")
        # find different values in this column
        column_values = set([row[col] for row in rows])
        logging.info(f"... which contains {column_values}")
        
        # for each possible value, try to divide on that value
        for value in column_values:
            
            set1, set2 = divideset(rows, col, value)

            # Information gain
            p = float(len(set1)) / len(rows)
            gain = current_score - p*scorefun(set1) - (1-p)*scorefun(set2)
            logging.info(f"splitting on {value} has a gain of {gain:0.6f}")
            if gain > best_gain and len(set1) > 0 and len(set2) > 0:
                best_gain = gain
                best_criteria = (col, value)
                best_sets = (set1, set2)
                logging.info(f"\n*best gain* => column {col+1} - split on {value}\n")

    if best_gain > 0:
        trueBranch = buildtree(best_sets[0])
        falseBranch = buildtree(best_sets[1])
        return decisionnode(col=best_criteria[0], value=best_criteria[1],
                tb=trueBranch, fb=falseBranch)
    else:
        return decisionnode(results=uniquecounts(rows))

def printtree(tree,indent=''):
    # Is this a leaf node?
    if tree.results!=None:
        print(str(tree.results))
    else:
        # Print the criteria
        print('Column ' + str(tree.col)+' : '+str(tree.value)+'? ')

        # Print the branches
        print(indent+'True->',)
        printtree(tree.tb,indent+'  ')
        print (indent+'False->',)
        printtree(tree.fb,indent+'  ')

tree = buildtree(my_data)
printtree(tree)
