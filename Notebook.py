#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import libutil
import libtable as lt
import libocr


# In[ ]:


images = libutil.pdf2images('data\\SIMPLE.pdf', zoom=2) # load images
image = images[0] # pick the first image
plt.figure(figsize=(8, 15))
plt.imshow(image, cmap='gray')
plt.show()


# In[ ]:


blur_thresh = 10 # <---- starting with a value of 10e a result similar to the
kernel_ratio=0.01
table_img = lt.get_tabular_image(image, blur_thresh=blur_thresh, kernel_ratio=kernel_rat
plt.figure(figsize=(8, 15))
plt.imshow(table_img, cmap='gray_r')
plt.show()


# In[ ]:


blur_thresh = 60 # <------- increased to 60
kernel_ratio=0.01
table_img = lt.get_tabular_image(image, blur_thresh=blur_thresh, kernel_ratio=kernel_rat
plt.figure(figsize=(8, 15))
plt.imshow(table_img, cmap='gray_r')
plt.show()


# In[ ]:


blur_thresh = 60
kernel_ratio=0.01
tables = lt.get_tables_in_image(image, blur_thresh=blur_thresh, kernel_ratio=kernel_rati
 min_cell_size=10, min_table_width_ratio=0.001)


# In[ ]:


imm = lt.get_tabled_mask(image, tables, thickness=2)
plt.figure(figsize=(8, 15))
plt.imshow(imm, cmap='gray')
plt.show()


# In[ ]:


table = tables[0]


# In[ ]:


imm = table.preview(numbered=True)
plt.figure(figsize=(15, 6))
plt.imshow(imm, cmap='gray')
plt.show()


# In[ ]:


table.fill_from_image(image, border_pad=1)


# In[ ]:


table.print(pad=3)


# In[ ]:


js = table.as_json(include_data=False, as_dict=False)
print(js)


# In[ ]:



images = libutil.pdf2images('data\\INVOICE.pdf', zoom=2)
image = images[0]
plt.figure(figsize=(8, 15))
plt.imshow(image, cmap='gray')
plt.show()


# In[ ]:


blur_thresh = 50
kernel_ratio=0.01
table_img = lt.get_tabular_image(image, blur_thresh=blur_thresh, kernel_ratio=kernel_rat
plt.figure(figsize=(8, 15))
plt.imshow(table_img, cmap='gray_r')
plt.show()


# In[ ]:


tables = lt.get_tables_in_image(image, blur_thresh=blur_thresh, kernel_ratio=kernel_rati
 min_cell_size=10, min_table_width_ratio=0.001)
imm = lt.get_tabled_mask(image, tables, thickness=2)
plt.figure(figsize=(8, 15))
plt.imshow(imm, cmap='gray')
plt.show()


# In[ ]:


tables[0].fill_from_image(image)
tables[0].print()


# In[ ]:



import cv2 as cv
image = cv.imread('data\\tabular.PNG')
plt.figure(figsize=(15, 6))
plt.imshow(image, cmap='gray')
plt.show()


# In[ ]:


blur_thresh = 50 # <--- I set a lower value here for demonstration
kernel_ratio=0.01
table_img = lt.get_tabular_image(image, blur_thresh=blur_thresh, kernel_ratio=kernel_rat
plt.figure(figsize=(15, 6))
plt.imshow(table_img, cmap='gray_r')
plt.show()


# In[ ]:


blur_thresh = 90
kernel_ratio=0.01
table_img = lt.get_tabular_image(image, blur_thresh=blur_thresh, kernel_ratio=kernel_rat
plt.figure(figsize=(15, 6))
plt.imshow(table_img, cmap='gray_r')
plt.show()


# In[ ]:


tables = lt.get_tables_in_image(image, blur_thresh=blur_thresh, kernel_ratio=kernel_rati
 min_cell_size=10, min_table_width_ratio=0.001)
imm = lt.get_tabled_mask(image, tables, thickness=2)
plt.figure(figsize=(15, 6))
plt.imshow(imm, cmap='gray')
plt.show()


# In[ ]:


tables[0].fill_from_image(image)
tables[0].print()


# In[ ]:




