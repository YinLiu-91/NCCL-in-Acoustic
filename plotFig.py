# 读取二进制输出文件并画图
from email.policy import default
from fileinput import filename
import numpy as np 
import matplotlib.pyplot as  plt 
import argparse

if __name__=="__main__":
    parser=argparse.ArgumentParser() 
    parser.add_argument('-nx',type=int,default=512)
    parser.add_argument('-ny',type=int,default=512)
    parser.add_argument('-nfiles',type=int,default=11)
    parser.add_argument('-iMovie',type=int,default=100)
    args=parser.parse_args()
    nx=args.nx
    ny=args.ny

    totalSteps=args.iMovie*(args.nfiles-1)

    for i in np.linspace(0,totalSteps,args.nfiles,dtype=int):
        # 读取数据文件，小端，float=4字节，数量为nx*ny
        fileName='./snap_at_step_'+np.str(i)+'.data'
        magic=np.fromfile(fileName,dtype='<f4',count=nx*ny,sep='',offset=0)
        data=magic.reshape(nx,ny)

        x=np.linspace(-1,1,nx)
        y=np.linspace(-1,1,ny)
        X,Y=np.meshgrid(x,y)
        figSize=10
        plt.figure(figsize=(figSize,figSize))
        handle=plt.contourf(X,Y,data,alpha=0.5,cmap=plt.cm.rainbow)
        c=plt.gca().set_aspect(1)
        plt.xticks(())
        plt.yticks(())
        plt.title('TStep: '+np.str(i))
        figName='TStep'+np.str(i)+'.jpeg'
        plt.savefig(figName)
        # plt.show()