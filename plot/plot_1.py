import matplotlib.pyplot as plt

# x=[1,2,3,4]
# y=[10,20,30,40]

# x = [1,2,4,8]
# y = [10,30,50,90]
# plt.plot(x,y)
# plt.title("Line plot")
# plt.xlabel("x-lable")
# plt.ylabel("y-lable")
# plt.show()

# x = [1, 2, 3, 4]
# y1 = [10, 20, 25, 30]
# y2 = [15, 25, 15, 35]
# plt.plot(x, y1, label="xyz")
# plt.plot(x, y2, label="abc")
# plt.legend()
# plt.title("Multiple Lines")
# plt.show()
# marker="o"

# x = [1,2,4,8]
# y = [10,30,50,90]
# plt.plot(x,y ,marker="o",linestyle='--',color='red')
# plt.title("dashed line")
# plt.show()

x = [1,2,4,8]
y = [10,30,50,90]
# plt.figure(facecolor='lightblue') 
# plt.gca().set_facecolor('lightgreen')
# plt.plot(x,y)
# plt.grid(True)
# plt.title('Show Grid')
# plt.show()

# size=[10,200,3000,40000]

# plt.scatter(x,y,s=size,color='red')
# plt.grid(True)
# plt.show()

# x=['x','y','z','a','b']
# y=[100,400,500,80,670]
# space=(0.2,0.1,0.075,0,0)
# clr=['pink','red','green','yellow','blue']

# plt.pie(y,labels=x,color=clr,autopct="%1.1f%%",explode=space,shadow=True)
# plt.title("Pie chart")
# plt.show()

label=['x','y','z','a','b']
y=[100,400,500,80,670]
x=[1,1,1,1,1]
clr=['pink','red','green','yellow','blue']
plt.bar(label,y,x,color=clr,hatch='/')
plt.grid(True)
plt.title("Bar chart")
plt.show()