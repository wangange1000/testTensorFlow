# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:53:21 2018

@author: Administrator
"""
"""
@code: 1051739153@qq.com
"""

def regionQuery(self, P, eps):
    result=[]
    for d in self.dataSet:
        if(((d[0]-p[0])**2 + (d[1]-p[1])**2)**0.5)<=eps:
            result.append(d)
    return result

def expandCluster(self, point, NeighbourPoints, C, eps, MintPts):
    C.addPoint(point)
    for p in NeighbourPoints:
        if p not in self.visited:
            self.visited.append(p)
            np = self.regionQuery(p, eps)
            if len(np) >= MinPts:
                for n in np:
                    if n not in NeighborPoints:
                        NeighborPoints.append(n)
        for c in self.Clusters:
            if not c.has(p):
                if not C.has(p):
                    C.addPoint(p)
        if len(self.Clusters)==0:
            if not C.has(p):
                C.addPoint(p)
    self.Clusters.append(C)
    
def dbscan(self, D, eps, MinPts):
    self.dataSet = D
    C = -1
    Noise = cluster('Noise')
    
    for point in D:
        if point not in self.visited:
            self.visited.append(point)
            NeighborPoints = self.regionQuery(point, eps)
            
            if len(NeighborPoints)<MinPts:
                Noise.addPoint(point)
            else:
                name = 'Cluster' + str(self.count)
                C = cluster(name)
                self.count+=1
                self.expandCluster(point, NeighborPoints, C , eps, MinPts)
                
if __name=='__main__':
    