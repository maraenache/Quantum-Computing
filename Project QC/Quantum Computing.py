# -*- coding: utf-8 -*-
"""tema.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yuWnh9mUGbv0dTSZJSqa2b_-lHZDtY5y
"""

!pip install qiskit qiskit-aer
!pip install pylatexenc

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt

"""1."""

X = [[1,3+3j,5],
     [7,9,complex(11,3)],
    [complex(18,-1),15-3j, 17j]]
def ex1(A):
    result = [[0,0,0],
              [0,0,0],
              [0,0,0]]

    for i in range(len(A)):
      for j in range(len(A[0])):
          result[j][i] = (A[i][j]).conjugate()
    for r in result:
      print(r)
ex1(X)

"""2."""

from numpy import *
from numpy import array
from numpy import tensordot
x = array([1,2-3j])
y = array([3+6j,complex(4,1)])
z = array([2+4j,2j])
def ex2(a,b,c):
  ab = tensordot(a, b, axes=0)#|ab>
  ca_bra = tensordot(c, a, axes=0).transpose().conjugate()
  #print(ab)
  
  #print(ca_bra)#<ca|
  rezultat=outer(ab,ca_bra)
  print(rezultat)
ex2(x,y,z)

"""3.a"""

from qiskit import *
circ=QuantumCircuit(2)
circ.cx(0,1)
circ.h(0)
circ.draw(output="mpl")

"""3.b"""

from qiskit import Aer
#matricea asociata circuitului
backend=Aer.get_backend('unitary_simulator')
job=backend.run(circ)
results=job.result()
U=results.get_unitary(circ,decimals=2)
print(U)

Ut=U.transpose().conjugate()
print(Ut)

I4 = [[1,0,0,0],
      [0,1,0,0],
      [0,0,1,0],
      [0,0,0,1]]
#print(I4)
A=np.dot(U,Ut)
B=np.dot(Ut,U)
D1=np.subtract(A,I4)#u*ut-i4
D2=np.subtract(B,I4)#ut*u-i4
norma1=np.linalg.norm(D1)
norma2=np.linalg.norm(D2)
#print(norma1,norma2)
if norma1<=0.05 and norma2<=0.05:
  print("Matricea este unitara")
else: 
  print("Matricea nu e unitara")

"""3.c"""

from qiskit import *
circuit=QuantumCircuit(2)
circuit.cx(0,1)
circuit.h(0)
circuit.measure_all()
circuit.draw(output="mpl")

#dupa masurare ce rezult obtin+histograma
import matplotlib.pyplot as plt
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circuit, shots=1000)
results=job.result()
count=results.get_counts()
print(count)
from qiskit.tools.visualization import plot_histogram
plot_histogram(count)
#rulez pe simulator

"""3.d"""

from numpy import *
from qiskit import Aer
from qiskit import QuantumCircuit
from qiskit.providers.aer import QasmSimulator
circuit=QuantumCircuit(2) #creeaza circuit de 2 qubiti
circuit.initialize('10')
circuit.h(0)
circuit.cx(0,1)

circuit.barrier()
circuit.cx(0,1)
circuit.h(0)

circuit.measure_all()

circuit.draw(output="mpl")

import matplotlib.pyplot as plt
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circuit, shots=1000)
results=job.result()
count=results.get_counts()
print(count)
from qiskit.tools.visualization import plot_histogram
plot_histogram(count)
#rulez pe simulator

"""4."""

def ex4():
  circuit4=QuantumCircuit(2)
  circuit4.x(0)
  circuit4.h(0)
  circuit4.cx(0,1)
  circuit4.h(1)
  circuit4.x(1)
ex4()
circuit4.draw()

from qiskit import Aer
#matricea asociata circuitului
backend=Aer.get_backend('unitary_simulator')
job=backend.run(circuit4)
results=job.result()
U=results.get_unitary(circuit4,decimals=2)
print(U)

"""5."""

from qiskit import Aer
#input= vector
X=array([complex(0.71,0),complex(0,0),complex(0,0),complex(0.71,0)])
#print(X)
def ex5(A):
  M=[[0,0],[0,0]]
  M[0][0]=A[0]
  M[0][1]=A[1]
  M[1][0]=A[2]
  M[1][1]=A[3] # partea reala la a 2 a + imaginara la a 2 a
  P_q0_0=M[0][0].real*M[0][0].real+M[0][0].imag*M[0][0].imag+M[0][1].real*M[0][1].real+M[0][1].imag*M[0][1].imag
  P_q0_1=M[1][0].real*M[1][0].real+M[1][0].imag*M[1][0].imag+ M[1][1].real*M[1][1].real+M[1][1].imag*M[1][1].imag
  P_q1_0=M[0][0].real*M[0][0].real+M[0][0].imag*M[0][0].imag+ M[1][0].real*M[1][0].real+ M[1][0].imag*M[1][0].imag
  P_q1_1=M[1][1].real*M[1][1].real+M[1][1].imag*M[1][1].imag+M[0][1].real*M[0][1].real+M[0][1].imag*M[0][1].imag
  print(P_q0_0)
  print(P_q0_1)
  print(P_q1_0)
  print(P_q1_1)
  P_00=M[0][0].real*M[0][0].real+M[0][0].imag*M[0][0].imag
  P_01=M[0][1].real*M[0][1].real+M[0][1].imag*M[0][1].imag
  P_10=M[1][0].real*M[1][0].real+M[1][0].imag*M[1][0].imag
  P_11=M[1][1].real*M[1][1].real+M[1][1].imag*M[1][1].imag
  if((P_00==P_q0_0*P_q1_0) and (P_01==P_q0_0*P_q1_1) and (P_10==P_q0_1*P_q1_0) and (P_11==P_q0_1*P_q1_1)):
      print("E necorelata")#return FALSE
  else: 
      print("Entagled")#return TRUE
ex5(X)

"""6."""

import matplotlib.pyplot as plt
from qiskit import *
from qiskit.quantum_info import Operator
from qiskit.compiler import transpile
import numpy as np
from math import *
import math
import numpy
from qiskit.qasm import pi
from qiskit.circuit.controlledgate import ControlledGate
from qiskit.circuit.gate import Gate
from qiskit.circuit.quantumregister import QuantumRegister
circuit=QuantumCircuit(3)
phi=pi/4
theta=acos((1/sqrt(3)))
circuit.ry(phi,0)
circuit.cry(theta,0,1)
circuit.x(2)
circuit.cx(0,2)
circuit.cx(1,0)
circuit.draw(output='mpl')
#w gate

circuit.measure_all()
simulator = Aer.get_backend('qasm_simulator')

job = simulator.run(transpile(circuit,backend=simulator),shots=1024)
result = job.result()
counts = result.get_counts()
print(counts)

import matplotlib.pyplot as plt
import numpy as np
from math import *
import math
import numpy
from qiskit.qasm import pi
from qiskit.circuit.controlledgate import ControlledGate
from qiskit.circuit.gate import Gate
from qiskit.circuit.quantumregister import QuantumRegister
psi_zero=QuantumCircuit(3)
phi=2*acos((1/sqrt(3)))
psi_zero.ry(phi,0)
psi_zero.ch(0,1)
psi_zero.cx(1,2)
psi_zero.cx(0,1)
psi_zero.x(0)
#psi 0
psi_zero.p(2*pi/3, 2)
psi_zero.p(4*pi/3, 1)
psi_zero.draw(output="mpl")
#circuit.measure_all()
#simulator = Aer.get_backend('qasm_simulator')

#job = simulator.run(transpile(psi_zero,backend=simulator),shots=1024)
#result = job.result()
#counts = result.get_counts()
#print(counts)

Wt=Warning.transpose().conjugate()
#M e operatorul unitar in care ajung in starea W
print(Wt)

psi_unu=QuantumCircuit(3)
phi=2*acos((1/sqrt(3)))
psi_unu.ry(phi,0)
psi_unu.ch(0,1)
psi_unu.cx(1,2)
psi_unu.cx(0,1)
psi_unu.x(0)
#psi 1
psi_unu.p(2*pi/3, 1)
psi_unu.p(4*pi/3, 2)
psi_unu.draw(output="mpl")
#psi_unu.measure_all()
#simulator = Aer.get_backend('qasm_simulator')

#job = simulator.run(transpile(psi_unu,backend=simulator),shots=1024)
#result = job.result()
#counts = result.get_counts()
#print(counts)

#transpose().conjugate()
import matplotlib.pyplot as plt
import numpy as np
from math import *
import math
import numpy
from qiskit.circuit.controlledgate import ControlledGate
from qiskit.circuit.gate import Gate
from qiskit.circuit.quantumregister import QuantumRegister
mpz=QuantumCircuit(3);# matricea de transformat in psi zero
mpz.p(2*pi/3, 2)
mpz.p(4*pi/3, 1)
mpz.draw(output='mpl')

mpu=QuantumCircuit(3)
mpu.p(2*pi/3, 2)
mpu.p(4*pi/3, 1)
mpu.draw(output='mpl')
#mpu.measure_all()

from qiskit import Aer
#matricea asociata circuitului care converteste din W ub psi 0
backend=Aer.get_backend('unitary_simulator')
job=backend.run(mpz)
results=job.result()
U0=results.get_unitary(mpz,decimals=2)#matricea asoc lui u0
print(U0)

U0t=U0.transpose().conjugate()
print (U0t) #U dagger asociat operatorului daca aplic Ut pe stare psi 0 ar trebui sa se transforme in W

from qiskit import Aer
#matricea asociata circuitului care converteste din W ub psi 1
backend=Aer.get_backend('unitary_simulator')
job=backend.run(mpu)
results=job.result()
U1=results.get_unitary(mpu,decimals=2)#matricea asoc lui u1
print(U1)

U1t=U1.transpose().conjugate()
print (U1t) #U dagger asociat operatorului daca aplic Ut pe stare psi 1 ar trebui sa se transforme in W

from qiskit.quantum_info import Statevector, Operator
from qiskit.circuit.library.data_preparation import StatePreparation
from qiskit import *

#alt mod de a reprezenta starile input
w = math.cos(2 * math.pi / 3) + 1j * math.sin(2 * math.pi / 3)
psi_zero_vector = np.array([1, w, 0, 0, w * w, 0, 0, 0]) / math.sqrt(3)
psi_unu_vector = np.array([1, w * w, 0, 0, w, 0, 0, 0]) / math.sqrt(3)

def ex6():
  #primim stare de input psi
  #aplic U0t pentru a o aduce in starea W
  #aplic inversul circuitului pentru a o aduce in starea 000
  #if masuram qubitii si rezultatul ne da starea |000> :
  return 1 //qubitul se afla in starea psi0
  #else
  #return 0 //qubitul se afla in starea psi1
ex6(psi_zero)
ex6(psi_unu)

"""Descriere: Primim ca input una din starile psi_zero sau psi_unu. Cum am procedat pentru psi_zero: Am construit starea psi_zero in 2 pasi. (Pas 1) Am plecat de la starea initiala |000> si am construit circuitul pentru a ajunge la starea W ( 1/sqrt(3)*(|001>+|010>+|100>). (Pas2) Dupa am aplicat I⊗P*P⊗P pentru a ajunge la starea psi0.Asemanator pentru psi_unu. Ce e diferit e ca la sfarist am aplicat I⊗P⊗P*P.  Am construit operatorul U0 care transforma in starea psi zero. Daca aplicam inversul circuitului, U0 dagger (notat U0t) ar trebui sa ajungem la starea W, si daca aplicam inversul circuitului de la (pas1). Daca de la starea input ajungem prin U0t si prin inversul circuitului "circuit" la starea initiala, ne oprim si returnam 0.Daca de la starea input ajungem prin U1t si prin inversul circuitului "circuit" la starea initiala, ne oprim si returnam 1."""