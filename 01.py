#!/usr/bin/env python
# coding: utf-8

# In[43]:


import hashlib


# In[44]:


msg = "hell"


# In[45]:


str.encode(msg)


# In[46]:


hashlib.sha256(str.encode(msg)).hexdigest()


# In[47]:


import os


# In[48]:


private_key = os.urandom(32).hex()


# In[49]:


private_key_version = '80' + private_key


# In[50]:


double_hash = hashlib.sha256(hashlib.sha256(bytes.fromhex(private_key_version)).digest()).hexdigest()


# In[51]:


checksum = double_hash[0 : 8]


# In[52]:


private_key_checksum = private_key_version + checksum


# In[53]:


private_key_checksum


# In[54]:


import base58


# In[55]:


base58.b58encode(bytes.fromhex(private_key_checksum))


# In[56]:


private_key


# In[57]:


import ecdsa


# In[58]:


_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
_b = 0x0000000000000000000000000000000000000000000000000000000000000007
_a = 0x0000000000000000000000000000000000000000000000000000000000000000
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
_Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8


# In[59]:


curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(_p, _a, _b)


# In[60]:


generator_secp256k1 = ecdsa.ellipticcurve.Point(curve_sacp256k1, _Gx, _Gy, _r)


# In[61]:


private_key


# In[62]:


secret = int(private_key, 16)


# In[63]:


ret = secret * generator_secp256k1


# In[64]:


ret.x()


# In[65]:


ret.y()


# In[66]:


type(ret.x())
type(ret.y())


# In[67]:


"%064x" % ret.x()


# In[68]:


"%064x" % ret.y()


# In[81]:


public_key = "04" + "%064x" % ret.x() + "%064x" % ret.y()


# In[82]:


str.upper(public_key)


# In[93]:


hash1 = hashlib.sha256(bytes.fromhex(public_key)).digest()


# In[94]:


hash2 = hashlib.new("ripemd160", hash1).digest()


# In[95]:


hash2.hex()


# In[96]:


public_key_version = "00" + hash2.hex()


# In[97]:


check = hashlib.sha256(hashlib.sha256(bytes.fromhex(public_key_version)).digest()).hexdigest()


# In[98]:


checksum = check[0 : 8]


# In[99]:


checksum


# In[100]:


address = base58.b58encode(bytes.fromhex(public_key_version + checksum))


# In[110]:


address


# In[ ]:




