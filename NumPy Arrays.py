# NumPy (or Numpy) is a Linear Algebra Library for Python, the reason it is so important for Data Science with Python is that almost all of the libraries in the PyData Ecosystem rely on NumPy as one of their main building blocks.
# Numpy is also incredibly fast, as it has bindings to C libraries. For more info on why you would want to use Arrays instead of lists
# ## Installation Instructions
# It is highly recommended you install Python using the Anaconda distribution to make sure all underlying dependencies (such as Linear Algebra libraries) all sync up with the use of a conda install. If you have Anaconda, install NumPy by going to your terminal or command prompt and typing:
#     conda install numpy
# Install using pip
#     pip install numpy
# ## Using NumPy
# Once you've installed NumPy you can import it as a library:

import numpy as np


# Numpy has many built-in functions and capabilities. We won't cover them all but instead we will focus on some of the most important aspects of Numpy: vectors,arrays,matrices, and number generation. Let's start by discussing arrays.
# 
# # Numpy Arrays
# 
# NumPy arrays are the main way we will use Numpy throughout the course. Numpy arrays essentially come in two flavors: vectors and matrices. Vectors are strictly 1-d arrays and matrices are 2-d (but you should note a matrix can still have only one row or one column).
# 
# Let's begin our introduction by exploring how to create NumPy arrays.
# 
# ## Creating NumPy Arrays
# 
# ### From a Python List
# 
# We can create an array by directly converting a list or list of lists:

# In[2]:


my_list = [1,2,3]
my_list


# In[3]:


np.array(my_list)


# In[4]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix


# In[5]:


np.array(my_matrix)


# ## Built-in Methods
# 
# There are lots of built-in ways to generate Arrays

# ### arange
# 
# Return evenly spaced values within a given interval.

# In[6]:


np.arange(0,10)


# In[7]:


np.arange(0,11,2)


# ### zeros and ones
# 
# Generate arrays of zeros or ones

# In[8]:


np.zeros(3)


# In[9]:


np.zeros((5,5))


# In[10]:


np.ones(3)


# In[11]:


np.ones((3,3))


# ### linspace
# Return evenly spaced numbers over a specified interval.

# In[12]:


np.linspace(0,10,3)


# In[13]:


np.linspace(0,10,50)


# ## eye
# 
# Creates an identity matrix

# In[14]:


np.eye(4)


# ## Random 
# 
# Numpy also has lots of ways to create random number arrays:
# 
# ### rand
# Create an array of the given shape and populate it with
# random samples from a uniform distribution
# over ``[0, 1)``.

# In[15]:


np.random.rand(2)


# In[16]:


np.random.rand(5,5)


# ### randn
# 
# Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform:

# In[17]:


np.random.randn(2)


# In[18]:


np.random.randn(5,5)


# ### randint
# Return random integers from `low` (inclusive) to `high` (exclusive).

# In[19]:


np.random.randint(1,100)


# In[20]:


np.random.randint(1,100,10)


# ## Array Attributes and Methods
# 
# Let's discuss some useful attributes and methods or an array:

# In[21]:


arr = np.arange(25)
ranarr = np.random.randint(0,50,10)


# In[22]:


arr


# In[23]:


ranarr


# ## Reshape
# Returns an array containing the same data with a new shape.

# In[24]:


arr.reshape(5,5)


# ### max,min,argmax,argmin
# 
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax

# In[25]:


ranarr


# In[26]:


ranarr.max()


# In[27]:


ranarr.argmax()


# In[28]:


ranarr.min()


# In[29]:


ranarr.argmin()


# ## Shape
# 
# Shape is an attribute that arrays have (not a method):

# In[30]:


# Vector
arr.shape


# In[31]:


# Notice the two sets of brackets
arr.reshape(1,25)


# In[32]:


arr.reshape(1,25).shape


# In[33]:


arr.reshape(25,1)


# In[34]:


arr.reshape(25,1).shape


# ### dtype
# 
# You can also grab the data type of the object in the array:

# In[35]:


arr.dtype

