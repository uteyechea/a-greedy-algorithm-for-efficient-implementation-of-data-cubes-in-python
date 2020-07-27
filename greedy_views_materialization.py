#!/usr/bin/env python
# coding: utf-8

# In[29]:


import operator


# ### Harinarayan, Rajaraman, Ullman Storage Costs 

# In[ ]:


#The order of the dictionary entries matter because...dependency,etc
lattice={
        'abcd':100,
        'abc':50,'acd':75,
        'ab':20,'ac':30,'cd':40,
        'a':1,'c':10
        }


# In[ ]:


views=list(lattice.keys())
views


# In[ ]:


selectedViews=['abcd'] #Always selected by default, also known as Top View


# In[17]:


def dependencyCheck(view,views):
    #compare dependency of view1 with view2
    #if views is a single element compare individual dependency if it is a set give a count 
    #and output a list of dependent views. 
    
    dependentViewsCount=0
    dependentViews=[]
    for anotherView in views:
        n=0
        for dimension in view:
            #print('dimension',dimension)
            for subDimension in anotherView:
                #print('sub dimension',subDimension)
                if dimension == subDimension: 
                    n+=1
                    #print('found, count ', n )
        if n == len(anotherView):
            dependentViews.append(anotherView)
            #print(n,len(anotherView))
            #print('dependent view found',dependentViewsCount)
    return dependentViews


# In[18]:


def additionalBenefit(views,lattice):
    benefit=[]
    minBenefit=0
    for v in views:
        if v not in selectedViews:
            #print(v)
            dependentViewsCount=dependencyCheck(selectedViews[-1],[v])
            if len(dependentViewsCount) <= 0:
                if lattice[v] < lattice[selectedViews[-1]]:
                    
                    addBenefit=abs(lattice[v]-lattice[selectedViews[-1]])
                    benefit.append((addBenefit,v))
                    
    if benefit:
        minBenefit=min(benefit)
        #print(minBenefit,v)
    return minBenefit


# In[23]:


def isConnected(view1,view2):
    isParent=dependencyCheck(view1,[view2])
    if len(isParent) > 0:
        return True
    else:
        return False


# In[24]:


isConnected('abc','a')


# In[53]:


def getParentView(view,lattice,selectedViews):
    parents=[]
    for v in lattice:
        if v != view:
            if isConnected(v,view):
                parents.append(v)
    #print(parents)
    #parents will alwayas have at least the top view
    newParent=selectedViews[0] # Top View
    for parent in parents:
            if parent in selectedViews:
                if lattice[parent]<lattice[newParent]: #select as parent the one with the smallest storage cost
                    newParent=parent
                    #print('newParent ',newParent)
    return newParent  


# In[ ]:


#Test if c which has two selected views as parents correctly chooses the cheapest one
#selectedViews=['abcd','abc','cd']
#getParentView('c',lattice,selectedViews)


# In[26]:


selectedViews[0]


# In[27]:


def getBenefit(views,lattice,selectedViews):
    B={}
    for view in lattice:
        storageCostDifference=0
        benefit=[]
        dependentViews=[]
        if view not in selectedViews:
            parent=getParentView(view,lattice,selectedViews)       
            storageCostDifference=abs(lattice[view]-lattice[parent])
            
            #Count the number of dependent Views
            view_dependentViews=dependencyCheck(view,views)
            
            
            materialized_view_dependentViews=[]
            #for selectedView in selectedViews:    
            #    parent=getParentView(view,lattice,selectedViews)
            #    if parent != selectedView and parent==selectedViews[0]:#Original
            #        materialized_view_dependentViews.extend(dependencyCheck(selectedView,views))
            
            
            for selectedView in selectedViews:
                if selectedView != parent and selectedView!=selectedViews[0]:
                    materialized_view_dependentViews.extend(dependencyCheck(selectedView,views))
                
                
                
                
            dependentViews=            set(view_dependentViews).difference(set(materialized_view_dependentViews))
            if dependentViews==set():
                dependentViews=set(view)
            #estimate the difference only for those selected nodes that are not parents
        
            addBenefit=additionalBenefit(views,lattice)
            if addBenefit and addBenefit[1]== view:  
                benefit.append((view,storageCostDifference,len(dependentViews),                dependentViews,storageCostDifference*len(dependentViews)+addBenefit[0]))
                B[view]=storageCostDifference*len(dependentViews)+addBenefit[0]
            else:
                benefit.append((view,storageCostDifference,len(dependentViews),                dependentViews,storageCostDifference*len(dependentViews)))
                B[view]=storageCostDifference*len(dependentViews)
                
        print(benefit)
        
        #Update Selected Views
        #B[view]=storageCostDifference*len(dependentViews)+addBenefit[0]
        
    update=max(B.items(), key=operator.itemgetter(1))[0]
    selectedViews.append(update)
        
    return selectedViews


# In[28]:


selectedViews=['abcd']
getBenefit(views,lattice,selectedViews)
selectedViews


# In[ ]:


getBenefit(views,lattice,selectedViews)
selectedViews


# In[ ]:


getBenefit(views,lattice,selectedViews)
selectedViews


# In[ ]:


getBenefit(views,lattice,selectedViews)
selectedViews


# In[ ]:


getBenefit(views,lattice,selectedViews)
selectedViews


# In[ ]:


getBenefit(views,lattice,selectedViews)
selectedViews


# In[ ]:


getBenefit(views,lattice,selectedViews)
selectedViews


# In[1]:


lattice 


# ### Trinidad Serna Improved Hypercube views materialization

# In[80]:


#Lattice views with only one dimension. Notation (storageCost,computationCost). 
#These values are specified by the user.
latticeDim1={
    'a':(19,5000), 'b':(5329,18000), 'c':(12,12),'d':(4,5) 
}

#For each view count and input the number of atributes in total for each dimension
atributes_perDimension={
    'a':24, 'b':2, 'c':4,'d':2 
}

#Full lattice with all the views, must use the letters of each dimension, i.e. a,b,c,etc to
#indicate the dependencies, for example acd is the parent view of ac,ad,cd,a,c and d.
lattice={
    'abcd': 53799,
    'abc':47133,'abd':18456,'acd':603,'bcd':32918,
    'ab':13973, 'ac':184, 'ad':58, 'bc':26058,'bd':8186,'cd':48,
    'a':19, 'b':5329, 'c':12,'d':4 
    
}

views=list(lattice.keys())
selectedViews=['abcd']

newLattice=lattice
for view in latticeDim1:
    newLattice[view]=latticeDim1[view]


# In[81]:


#Due to lack of time this algorithm will only work for up
#to views made of 4 dimensions maximum
def computationCost(lattice):
    latticeDim2={}
    latticeDim3={}
    latticeDim4={}
    for view in lattice:
        if len(view)==2: #select views at dim=2 or higher
            dimension=list(view)
            latticeDim2[view]=(lattice[view] ,                                lattice[ dimension[0] ][1]*lattice[ dimension[1] ][1]  
                              )
            #print(view,latticeDim2[view])
        
    for view in latticeDim2:
        newLattice[view]=latticeDim2[view]

            
    for view in lattice:
        if len(view)==3:
            dimension=list(view)
            view3dim=''.join(dimension[:2])
            latticeDim3[view]=( lattice[view],                               lattice[view3dim] [1] + lattice[view3dim][0] * lattice[dimension[-1]][1]
            
            )
            #print(view,latticeDim3[view])    
            
    for view in latticeDim3:
        newLattice[view]=latticeDim3[view]

    
    for view in lattice:
        if len(view)==4:
            dimension=list(view)
            view3dim=''.join(dimension[:2])
            view4dim=''.join(dimension[:3])
            latticeDim4[view]=( lattice[view],                               lattice[view3dim][1] +                               lattice[view4dim][0] * lattice[dimension[-1]][1]
                              )
            #print(view,latticeDim4[view])    
        
    for view in latticeDim4:
        newLattice[view]=latticeDim4[view]
    
    return newLattice


# In[82]:


newLattice = computationCost(newLattice)
newLattice


# In[83]:


def probabilityOfChange(atributes_perDimension,lattice,accepted_probability_of_db_change_in_literature):
    totalElements={}
    probability={}
    for view in lattice:
        countElements=0
        dimensions=list(view)
        for dimension in dimensions:
            if dimension in atributes_perDimension: #Consistency check for notation
                countElements+=atributes_perDimension[dimension]
        
        totalElements[view]=countElements+len(view)
        #print(view,totalElements[view])
        
    max_totalElements_key=max(totalElements, key=totalElements.get)
    for view in lattice:
        probability[view]= totalElements[view] *         accepted_probability_of_db_change_in_literature /         totalElements[max_totalElements_key]
        
    return probability


# In[84]:


probability=probabilityOfChange(atributes_perDimension,newLattice,0.2)
probability


# In[85]:


lattice={
    'abcd': 53799,
    'abc':47133,'abd':18456,'acd':603,'bcd':32918,
    'ab':13973, 'ac':184, 'ad':58, 'bc':26058,'bd':8186,'cd':48,
    'a':19, 'b':5329, 'c':12,'d':4 
}


# In[86]:


lattice


# In[87]:


def getGreedyBenefit(views,lattice,selectedViews):
    B={}
    for view in lattice:
        storageCostDifference=0
        benefit=[]
        dependentViews=[]
        if view not in selectedViews:
            parent=getParentView(view,lattice,selectedViews)       
            storageCostDifference=abs(lattice[view]-lattice[parent])
            
            #Count the number of dependent Views
            view_dependentViews=dependencyCheck(view,views)     
            
            materialized_view_dependentViews=[]
            
            for selectedView in selectedViews:
                if selectedView != parent and selectedView!=selectedViews[0]:
                    materialized_view_dependentViews.extend(dependencyCheck(selectedView,views))
                
            dependentViews=            set(view_dependentViews).difference(set(materialized_view_dependentViews))
            if dependentViews==set():
                dependentViews=set(view)
            #estimate the difference only for those selected nodes that are not parents
        
            addBenefit=additionalBenefit(views,lattice)
            if addBenefit and addBenefit[1]== view:  
                benefit.append((view,storageCostDifference,len(dependentViews),                dependentViews,storageCostDifference*len(dependentViews)+addBenefit[0]))
                B[view]=storageCostDifference*len(dependentViews)+addBenefit[0]
            else:
                benefit.append((view,storageCostDifference,len(dependentViews),                dependentViews,storageCostDifference*len(dependentViews)))
                B[view]=storageCostDifference*len(dependentViews)
                
        #print(benefit)

    #Select the view with the highest benefit    
    #update=max(B.items(), key=operator.itemgetter(1))[0]
    #selectedViews.append(update)
        
    return B


# In[88]:


greedyBenefit=getGreedyBenefit(views,lattice,selectedViews)
greedyBenefit


# In[97]:


def getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability):
    newBenefit={}
    fq={}
    for view in views:
        if view not in selectedViews:
            fq[view]=len(dependencyCheck(view,views))
            newBenefit[view]=            greedyBenefit[view] * fq[view] -             (            (newLattice[view][1] / fq[view] ) *            (1.0 + probability[view]) 
            )
            
            print (view,greedyBenefit[view] * fq[view],                    newLattice[view][1] / fq[view],                   (1 + probability[view]), newBenefit[view])
    
    #Select the view with the highest benefit    
    update=max(newBenefit.items(), key=operator.itemgetter(1))[0]
    selectedViews.append(update)
    
    print(selectedViews)


# In[98]:


selectedViews=['abcd']
getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability)


# In[100]:


getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability)


# In[101]:


getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability)


# In[102]:


getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability)


# In[103]:


getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability)


# In[104]:


getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability)


# In[105]:


getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability)


# In[106]:


getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability)


# In[107]:


getTriniBenefit(views,selectedViews,greedyBenefit,newLattice,probability)


# In[ ]:




