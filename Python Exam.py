#!/usr/bin/env python
# coding: utf-8

# <H3>
# 1) Positive and Negative sentiments.
# <H3>

# In[5]:


comments=['Food is the worst here','He is an awesome player','She is the best','This pizza tastes awful','These burger are really nice']
comments=int(input("Enter the comments: ")
positive:['good','awesome','best','nice']
negative:['worst','awful']


# <H3>
# 2) Creating a dictionary.
# <H3>

# In[18]:


import math
dict={'Square':lambda a : a**2,'Cube':lambda a : a**3,'Squareroot':lambda a : a**(1/2)}
num=int(input())
result=0
for fun in dict:
    result+=dict[fun](num)
print(result)


# <H3>
# 3) Finding fruit taste from gn tuple
# <H3>

# In[25]:


Is_str = ['hello','Dear','hOw','ARe','You']
print("The original string is : " + str(Is_str))
res = list(filter(lambda c: c.isupper(), Is_str))
print("The uppercase characters in string are : " + str(res))


# <H3>
# 4) Second character uppercase
# <H3>

# In[26]:


Is_str = ['hello','Dear','hOw','ARe','You']
print("The original string is : " + str(Is_str))
res = list(filter(lambda c: c.isupper(), Is_str))
print("The uppercase characters in string are : " + str(res))


# <H3>
# 5) Dictionary of names
# <H3>

# In[68]:


dict = {'John':45, 'Shelly':65, 'Marry':35}

calc = lambda k: (k,  (d[k] / 9.81) * 1.622 )

r  = dict(calc(k) for k in d)

print(r)


# <H3>
# 6) First character is uppercase
# <H3>

# In[76]:


s1=["santa Maria","Hello World","Merry christmas","tHank You"]
chindex=0
if chindex==1:
         print(letter[1].upper()+""+letter[1:len(letter)], end=" ")
else:
         print(letter)


# <H3>
# 7) List(reduce function)
# <H3>

# In[86]:


A = {1, 2, 3, 4, 8} 
B = {2, 3, 8, 5, 6} 
C = {8, 4, 5, 3, 7} 
D = {6, 9, 8, 3} 
E = {9, 12, 3, 7, 6, 8, 4, 6, 21, 1, 6}
print(A.intersection(B))
print(A.intersection(C))
print(A.intersection(D))
print(A.intersection(E))
print(A.intersection(B, C, D, E))
     


# <H3>
# 8) Cummulative range
# <H3>

# In[63]:


Input_list=[9,5,7,8,5]
import itertools as it
l=[]
l=it.accumulate(list(enumerate(Input_list)),lambda x,y:(y[0],(x[1]*(x[0]+1)+y[1])/(y[0]+1)))
print(list(map(lambda x:x[1],l)))


# <H3>
# 9) Converting words into uppercase
# <H3>

# In[57]:


x=map(lambda x:x.upper(),['True', 'FALse', 'tRue', 'False', 'false'])
upperlist=list(x)
print(upperlist)


# <H3>
# 10) List of dates
# <H3>

# In[64]:


dateslist=['17-12-1949','22-04-2011','01-05-1993','19-02-2020']
l=[]
for i in dateslist:
    l.append(i[6:])
print(l)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




