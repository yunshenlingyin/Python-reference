import numpy as np
import matplotlib.pyplot as plt

def find_seta(Z):
    Z=np.array(Z)
    result=[]
    for i in Z:
        seta=np.arctan(i.imag/i.real)
        if i.real<0:
            seta+=np.pi
        result.append(seta)
    return np.array(result)


seta_i=np.linspace(0,90,100)
seta_i_store=np.radians(seta_i)
n_t,n_i=1.5,1
E_0=[1+1j]
seta_t=np.arcsin(n_i*np.sin(seta_i_store)/n_t)
r_v_e=(n_i*np.cos(seta_i_store)-n_t*np.cos(seta_t))/(n_i*np.cos(seta_i_store)+n_t*np.cos(seta_t))
r_p_e=(n_t*np.cos(seta_i_store)-n_i*np.cos(seta_t))/(n_t*np.cos(seta_i_store)+n_i*np.cos(seta_t))
#t_v=2*n_i*np.cos(seta_i_store)/(n_i*np.cos(seta_i_store)+n_t*np.cos(seta_t))
#t_p=2*n_i*np.cos(seta_i_store)/(n_t*np.cos(seta_i_store)+n_i*np.cos(seta_t))
n_t,n_i=1,1.5
seta_t=np.arcsin(n_i*np.sin(seta_i_store)/n_t+0j)
r_v_i=(n_i*np.cos(seta_i_store)-n_t*np.cos(seta_t))/(n_i*np.cos(seta_i_store)+n_t*np.cos(seta_t))
r_p_i=(n_t*np.cos(seta_i_store)-n_i*np.cos(seta_t))/(n_t*np.cos(seta_i_store)+n_i*np.cos(seta_t))
E_r_v_i=(find_seta(E_0*r_v_i)-find_seta(E_0)[0])/np.pi
E_r_p_i=(find_seta(E_0*r_p_i)-find_seta(E_0)[0])/np.pi
E_r_v_e=(find_seta(E_0*r_v_e)-find_seta(E_0)[0])/np.pi
E_r_p_e=(find_seta(E_0*r_p_e)-find_seta(E_0)[0])/np.pi
#E_t_v=find_seta(E_0*t_v)-find_seta(E_0)[0]
#E_t_p=find_seta(E_0*t_p)-find_seta(E_0)[0]

fig=plt.figure(figsize=(6,10))

plt.subplot(221)
plt.plot(seta_i,E_r_v_i,label='r_v_internal')
plt.legend(loc='upper left')
plt.xticks(range(0,100,10))
plt.yticks(np.linspace(0,1,6))
plt.subplot(222)
plt.plot(seta_i,E_r_p_i,label='r_p_internal')
plt.legend(loc='lower right')
plt.xticks(range(0,100,10))
plt.yticks(np.linspace(0,1,6))
plt.subplot(223)
plt.plot(seta_i,E_r_v_e,label='t_v_external')
plt.legend(loc='lower right')
plt.xticks(range(0,100,10))
plt.yticks(np.linspace(0,1,6))
plt.subplot(224)
plt.plot(seta_i,E_r_p_e,label='t_p_external')
plt.legend(loc='upper left')
plt.xticks(range(0,100,10))
plt.yticks(np.linspace(0,1,6))

plt.show()