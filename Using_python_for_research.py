import matplotlib.pyplot as plt
import numpy as np

x=np.logspace(-1,1,40)
y1=x**2
y2=x**1.5
plt.loglog(x,y1,"bo-",linewidth=2,markersize=4,label="first")
plt.loglog(x,y2,"gs-",linewidth=2,markersize=6,label="second")
plt.xlabel("x")
plt.ylabel("y")
plt.axis([-2,12,-5,105])
plt.legend(loc="upper left")


x=np.random.normal(size=1000)
plt.hist(x)
plt.hist(x,normed=True)
plt.hist(x,normed=True,bins=np.linspace(-5,5,21))


plt.figure()
plt.subplot(221)
plt.hist(x,bins=30)
plt.subplot(222)
plt.hist(x,bins=30,normed=True)
plt.subplot(223)
plt.hist(x,bins=30,cumulative=30)
plt.subplot(224)
plt.hist(x,bins=30,normed=True,cumulative=True,histtype="step")


import random

rolls=[]
for k in range(100):
    rolls.append(random.choice(range(1,7)))
plt.hist(rolls,bins=np.linspace(0.5,6.5,7))



ys=[]
for rep in range(100000):
    y=0
    for k in range(10):
        x=random.choice(range(1,7))
        y+=x
    ys.append(y)
plt.hist(ys)
plt.hist(ys,normed=True)

import time
start_time=time.clock()
x=np.random.randint(1,7,(100000,10))
Y=np.sum(x,axis=1)
plt.hist(Y);
end_time=time.clock()
print(end_time-start_time)


delta_x=np.random.normal(0,1,(2,5))
X=np.cumsum(delta_x,axis=1)
plt.plot(X[0],X[1],"ro-")
plt.savefig("rw.pdf")


x_0=np.array([[0],[0]])
delta_x=np.random.normal(0,1,(2,5))
X=np.concatenate((x_0,np.cumsum(delta_x,axis=1)),axis=1)
plt.plot(X[0],X[1],"ro-")
plt.savefig("rw2.pdf")


plt.figure()
plt.subplot(121)
plt.plot(X[0],X[1],'ro-')
plt.subplot(122)
plt.plot(X[0],X[1],"ro-",linewidth=0.5,markersize=3)



def read_seq(inputfile):
    '''reads and returns the input sequence with special characters removed'''
    with open(inputfile,'r') as f:
        seq=f.read()
    seq=seq.replace('\n','')
    seq=seq.replace('\r','')
    return seq



inputfile='dna.txt'
with open(inputfile,'r') as f:
    seq=f.read()




inputfile='dna.txt'
f=open(inputfile,'r')
seq=f.read()
seq=seq.replace('\n','')
seq=seq.replace('\r','')

def translate(seq):
    '''translate a string contaning a nuceotide sequence into a string containing
    the corresponding sequence of amino acids'''
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    protein=""
    if len(seq)%3 == 0:
        for i in range(0,len(seq),3):
            codon=seq[i:i+3]
            protein += table[codon]
    return protein


text="This is my test text. we're keeping this text short to keep things manageable"

def count_words(text):
    '''count the number of times each word occurs in text(str)'''
    text=text.lower()
    skips=[".",",",";",":",'"',"'"]
    for ch in skips:
        text=text.replace(ch,"")
        
    word_counts={}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word]+=1
        else:
            word_counts[word]=1
    return word_counts

from collections import Counter

def count_words_fast(text):
    text=text.lower()
    skips=[".",",",";",":",'"',"'"]
    for ch in skips:
        text=text.replace(ch,"")
        
    word_counts=Counter(text.split(' '))
    return word_counts

def read_book(title_path):
    '''read a book and return it as a string,utf8 is dominat character encoding for the web'''
    with open(title_path,'r',encoding='utf8') as current_file:
        text=current_file.read()
        text=text.replace('\n','').replace('\r','')
    return text

def word_stats(word_counts):
    '''return number of unique words and word frequencies'''
    num_unique=len(word_counts)
    counts=word_counts.values()
    return (num_unique,counts)

text=read_book("./English/shakespeare/Romeo and Juliet.txt")
word_counts=count_words(text)
(num_unique,counts)=word_stats(word_counts)
print(num_unique,sum(counts))


text=read_book("./German/shakespeare/Romeo und Julia.txt")
word_counts=count_words(text)
(num_unique,counts)=word_stats(word_counts)
print(num_unique,sum(counts))


import os
book_dir="./Books"

import pandas as pd
stats=pd.DataFrame(columns=('language','author','title','length','unique'))
title_num=1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir+'/'+language):
        for title in os.listdir(book_dir+'/'+language+'/'+author):
            inputfile=book_dir+'/'+language+'/'+author+'/'+title
            print(inputfile)
            text=read_book(inputfile)
            (num_unique,counts)=word_stats(count_words(text))
            stats.loc[title_num]=language,author.capitalize(),title.replace('.txt',''),sum(counts),num_unique
            title_num+=1
import pandas as pd
table=pd.DataFrame(columns=('name','age'))
table.loc[1]='james',22
table.loc[2]='hess',23


import matplotlib.pyplot as plt
plt.plot(stats.length,stats.unique,'bo-')
plt.loglog(stats.length,stats.unique,'bo-')

plt.figure(figsize=(10,10))
subset=stats[stats.language=="English"]
plt.loglog(subset.length,subset.unique,'o',label="English",color="crimson")
subset=stats[stats.language=="French"]
plt.loglog(subset.length,subset.unique,'o',label="French",color="forestgreen")
subset=stats[stats.language=="German"]
plt.loglog(subset.length,subset.unique,'o',label="German",color="orange")
subset=stats[stats.language=="Portuguese"]
plt.loglog(subset.length,subset.unique,'o',label="Portuguese",color="blueviolet")

plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique")
plt.savefig('lang_plot.pdf')
import numpy as np

def distance(p1,p2):
    return np.sqrt(np.sum(np.power(p2-p1,2)))

p1=np.array([1,1])
p2=np.array([4,4])
distance(p1,p2)



import random
def majority_vote(votes):
    vote_counts={}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote]+=1
        else:
            vote_counts[vote]=1
            
    winners=[]
    max_counts=max(vote_counts.values())
    for vote,count in vote_counts.items():
        if count==max_counts:
            winners.append(vote)
    return random.choice(winners)

votes=[1,2,3,1,2,3,1,2,3,3,3,3]
vote_counts=majority_vote(votes)
max_counts=max(vote_counts.values())



import scipy.stats as ss
def majority_vote_short(votes):
    '''return the most common element in votes'''
    mode,count = ss.mstats.mode(votes)
    return mode

points=np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p = np.array([2.5,2])

def find_nearest_neighbors(p,points,k=5):
    '''find the k nearest neighbors of p and return their indices'''
    distances=np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i]=distance(p,points[i])
    ind=np.argsort(distances)
    return ind[:k]
    

import matplotlib.pyplot as plt
plt.plot(points[:,0],points[:,1],"ro")
plt.plot(p[0],p[1],'bo')
plt.axis([0.5,3.5,0.5,3.5])

def knn_predict(p,points,outcomes,k=5):
    ind = find_nearest_neighbors(p,points,k)
    return majority_vote(outcomes[ind])
    
outcomes=np.array([0,0,0,0,1,1,1,1,1])  



def generate_synth_data(n=50):
    '''creat two sets of points from bivariate normal distrubutions'''
    points=np.concatenate((ss.norm(0,1).rvs((n,2)),ss.norm(1,1).rvs((n,2))),axis=0)
    outcomes=np.concatenate((np.repeat(0,n),np.repeat(1,n)))
    return (points,outcomes)
n=1000
(points,outcomes)=generate_synth_data(n)
plt.figure()
plt.plot(points[:n,0],points[:n,1],'ro',markersize=2)
plt.plot(points[n:,0],points[n:,1],'bo',markersize=2)
plt.savefig('bivardata.pdf')

def make_prediction_grid(predictors,outcomes,limits,h,k):
    '''classify each point on the prediction grid'''
    (x_min,x_max,y_min,y_max)=limits
    xs=np.arange(x_min,x_max,h)
    ys=np.arange(y_min,y_max,h)
    xx,yy=np.meshgrid(xs,ys)
    prediction_grid=np.zeros(xx.shape,dtype=int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p=np.array([x,y])
            prediction_grid[j,i]=knn_predict(p,predictors,outcomes,k)
    return (xx,yy,prediction_grid)


def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)

(predictors,outcomes)=generate_synth_data(1000)
k=5;filename="knn_synth_5.pdf";limits=(-3,4,-3,4);h=0.1
(xx,yy,prediction_grid)=make_prediction_grid(predictors,outcomes,limits,h,k)
plot_prediction_grid(xx,yy,prediction_grid,filename)


k=50;filename="knn_synth_50.pdf";limits=(-3,4,-3,4);h=0.1
(xx,yy,prediction_grid)=make_prediction_grid(predictors,outcomes,limits,h,k)
plot_prediction_grid(xx,yy,prediction_grid,filename)



from sklearn import datasets
iris=datasets.load_iris()

predictors=iris.data[:,0:2]
outcomes=iris.target
plt.plot(predictors[outcomes==0][:,0],predictors[outcomes==0][:,1],'ro')
plt.plot(predictors[outcomes==1][:,0],predictors[outcomes==0][:,1],'go')
plt.plot(predictors[outcomes==2][:,0],predictors[outcomes==0][:,1],'bo')
plt.savefig('iris.pdf')

k=5;filename="iris_grid.pdf";limits=(4,8,1.5,4.5);h=0.1
(xx,yy,prediction_grid)=make_prediction_grid(predictors,outcomes,limits,h,k)
plot_prediction_grid(xx,yy,prediction_grid,filename)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(predictors,outcomes)
sk_predictions=knn.predict(predictors)

plt.plot(sk_predictions,'r',markersize=1)
plt.savefig('sk_prediction.pdf')


my_predictions=np.array([knn_predict(p,predictors,outcomes,5) for p in predictors])

print(100*np.mean(sk_predictions==my_predictions))
print(100*np.mean(sk_predictions==outcomes))
print(100*np.mean(my_predictions==outcomes))



data={'name':['tim','pan','jim','san'],
      'age':[23,12,34,53],
      'zip':['13423','43241','23421','52342']}


whisky=pd.read_csv('whiskies.txt')
whisky['region']=pd.read_csv('regions.txt')
whisky.head()
whisky.columns
flavors=whisky.iloc[:,2:14]


import matplotlib.pyplot as plt

corr_flavors=pd.DataFrame.corr(flavors)
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig('corr_flavors.pdf')



corr_whisky=pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis('tight')
plt.colorbar()
plt.savefig('corr_whisky.pdf')


from sklearn.cluster.bicluster import SpectralCoclustering
model=SpectralCoclustering(n_clusters=6,random_state=0)
model.fit(corr_whisky)

model.rows_
np.sum(model.rows_,axis=1)
np.sum(model.rows_,axis=0)
model.row_labels_

whisky['Group']=pd.Series(model.row_labels_,index=whisky.index)
whisky=whisky.loc[np.argsort(model.row_labels_)]
whisky=whisky.reset_index(drop=True)

correlations=pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations=np.array(correlations)


plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.subplot(122)
plt.pcolor(correlations)
plt.title('Rearranged')
plt.axis('tight')
plt.colorbar()
plt.savefig('correlations.pdf')




data=pd.Series([1,2,3,4])
data=data.loc[[3,0,1,2]]
data=data.reset_index(drop=True)






birddata=pd.read_csv('bird_tracking.csv')

birddata.info()
birddata.head()

import matplotlib.pyplot as plt
import numpy as np
ix=birddata.bird_name=='Eric'
x,y=birddata.longitude[ix],birddata.latitude[ix]
plt.plot(x,y,'.')


bird_names=pd.unique(birddata.bird_name)
for bird_name in bird_names:
    ix=birddata.bird_name==bird_name
    x,y=birddata.longitude[ix],birddata.latitude[ix]
    plt.plot(x,y,label=bird_name)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.legend(loc='lower right')
plt.savefig('3bird_traj.pdf')



ix=birddata.bird_name=='Eric'
speed=birddata.speed_2d[ix]
ind=np.isnan(speed)
plt.hist(speed[~ind])
plt.savefig('hist.pdf')

plt.figure(figsize=(8,4))
ix=birddata.bird_name=="Eric"
speed=birddata.speed_2d[ix]
ind=np.isnan(speed)
plt.hist(speed[~ind],bins=np.linspace(0,30,20),normed=True)
plt.xlabel('2D speed (m/s)')
plt.ylabel('frequency')


birddata.speed_2d.plot(kind='hist',range=[0,30])
plt.xlabel("2D speed m/s")


import datetime
datetime.datetime.today()
date_str=birddata.date_time[0]

datetime.datetime.strptime(date_str[:-3],"%Y-%m-%d %H:%M:%S")

timestamps=[]
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3],"%Y-%m-%d %H:%M:%S"))

birddata['timestamp']=pd.Series(timestamps,index=birddata.index)

times=birddata.timestamp[birddata.bird_name=="Eric"]
elapsed_time=[time-times[0] for time in times]
plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1))
plt.xlabel('observation')
plt.ylabel('Elapsed time(days)')



data=birddata[birddata.bird_name=="Eric"]
times=data.timestamp
elapsed_time=[time-times[0] for time in times]
elapsed_days = np.array(elapsed_time)/datetime.timedelta(days=1)

next_day=1
inds=[]
daily_mean_speed=[]
for (i,t) in enumerate(elapsed_days):
    if t<next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day+=1
        inds=[]

plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel('day')
plt.ylabel('mean speed(m/s)')
plt.savefig('bird_daily_mean_speed.pdf')



import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj=ccrs.Mercator()

plt.figure(figsize=(10,10))
ax=plt.axes(projection=proj)
ax.set_extent((-25.0,20.0,52.0,10.0))

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS,linestyle=':')

bird_names=pd.unique(birddata.bird_name)
for name in bird_names:
    ix=birddata['bird_name']==name
    x,y=birddata.longitude[ix],birddata.latitude[ix]
    ax.plot(x,y,transform=ccrs.Geodetic(),label=name)
    
plt.legend(loc='upper left')
plt.savefig('map_birdtracking.pdf')












import networkx as nx
G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(['u','v'])

G.add_edge(1,2)
G.add_edge('u','v')
G.add_edges_from([(1,3),(1,4),(1,5),(1,6)])
G.add_edge('u','w')

G.remove_node(2)

G.remove_nodes_from([4,5])

G.remove_edge(1,3)

G.remove_edges_from([(1,2),('u','v')])

G.number_of_nodes()
G.number_of_edges()


G=nx.karate_club_graph()
import matplotlib.pyplot as plt
nx.draw(G,with_labels=True,node_color='lightblue',edge_colors='red')
plt.savefig('karate_graph.pdf')

G.degree()

G.degree()[33]
G.degree(33)


G.number_of_edges()
G.number_of_nodes()


from scipy.stats import bernoulli
bernoulli.rvs(p=0.2)

N=20
p=0.2

# create empty graph
# add all N nodes in the graph
# loop over all pairs of nodes
    # add an edge with prob p
def er_graph(N,p):
    '''Generate an ER graph'''
    G= nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1<node2 and bernoulli.rvs(p=p):
                G.add_edge(node1,node2)
    return G          
nx.draw(er_graph(50,0.08),node_size=40,node_color='red')
plt.savefig('er1.pdf')     

def plot_degree_distribution(G):
    plt.hist(list(G.degree().values()),histtype='step')
    plt.xlabel('Degree $k$')
    plt.ylabel('$p(k)$')
    plt.title('Degree distribution')

G1=er_graph(500,0.08)
plot_degree_distribution(G1)
G2=er_graph(500,0.08)
plot_degree_distribution(G2)
G3=er_graph(500,0.08)
plot_degree_distribution(G3)
plt.savefig('hist3.pdf')

import numpy as np

A1=np.loadtxt('adj_allVillageRelationships_vilno_1.csv',delimiter=',')
A2=np.loadtxt('adj_allVillageRelationships_vilno_2.csv',delimiter=',')

G1=nx.to_networkx_graph(A1)
G2=nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print('number of nodes: %d' %G.number_of_nodes())
    print('nubmer of edges: %d' %G.number_of_edges())
    print('Average degree:%.2f' %np.mean(list(G.degree().values())))


basic_net_stats(G1)
basic_net_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig('village_hist.pdf')


gen=nx.connected_component_subgraphs(G1)
g=gen.__next__()
type(g)
g.number_of_nodes()
len(gen.__next__())
len(G1)
G1.number_of_nodes()



gen=nx.connected_component_subgraphs(G1)
G1_LCC=max(nx.connected_component_subgraphs(G1),key=len)
G2_LCC=max(nx.connected_component_subgraphs(G2),key=len)
len(G1_LCC)
len(G2_LCC)

G1_LCC.number_of_nodes() / G1.number_of_nodes()
G2_LCC.number_of_nodes() / G2.number_of_nodes()


plt.figure()
nx.draw(G1_LCC,node_color='red',edge_color='gray',node_size=20)
plt.savefig('village1.pdf')
plt.figure()
nx.draw(G2_LCC,node_color='green',edge_color='gray',node_size=20)
plt.savefig('village2.pdf')



