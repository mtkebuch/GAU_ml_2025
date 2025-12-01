from practise import numpy1 as np

#14
text = "i love watermelon"
N = 5

parts=np.array([text[i:i+N] for i in range(0,len(text),N)])
print(parts)

#16
#statikuri
A= np.array([[3,4],[3,2]])
B= np.array([[5,6],[7,9]])

C=A+B
print(C)

#shemtxveviti
C=np.random.randint(1,10,(2,2))
D=np.random.randint(1,10,(2,2))
E=C+D
print(E)

#18
#static

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
C=np.dot(A,B)
print(C)

#random
X=np.random.randint(1,10,(2,2))
Y=np.random.randint(1,10,(2,2))
XY=np.dot(X,Y)
print(XY)

#20
matrix = np.random.randint(0,10,(10,10))
print("Original matrix:\n", matrix)

num=int(input("Enter a number to remove:"))

matrix[matrix==num] = 0
print("\nMatrix after removal:\n",matrix)

#23
cheeseboard=np.zeros((8,8),dtype=int)

cheeseboard[1::2,::2]=1
cheeseboard[::2,1::2]=1

print(cheeseboard)



