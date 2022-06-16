import matplotlib.pyplot as plt
import numpy as np
import itertools as it
import cv2

def format_ouput(A):
    return f"""
{A[0][0]} {A[0][1]} {A[0][2]} | {A[0][3]} {A[0][4]} {A[0][5]} | {A[0][6]} {A[0][7]} {A[0][8]}
{A[1][0]} {A[1][1]} {A[1][2]} | {A[1][3]} {A[1][4]} {A[1][5]} | {A[1][6]} {A[1][7]} {A[1][8]}
{A[2][0]} {A[2][1]} {A[2][2]} | {A[2][3]} {A[2][4]} {A[2][5]} | {A[2][6]} {A[2][7]} {A[2][8]}
---------------------
{A[3][0]} {A[3][1]} {A[3][2]} | {A[3][3]} {A[3][4]} {A[3][5]} | {A[3][6]} {A[3][7]} {A[3][8]}
{A[4][0]} {A[4][1]} {A[4][2]} | {A[4][3]} {A[4][4]} {A[4][5]} | {A[4][6]} {A[4][7]} {A[4][8]}
{A[5][0]} {A[5][1]} {A[5][2]} | {A[5][3]} {A[5][4]} {A[5][5]} | {A[5][6]} {A[5][7]} {A[5][8]}
---------------------
{A[6][0]} {A[6][1]} {A[6][2]} | {A[6][3]} {A[6][4]} {A[6][5]} | {A[6][6]} {A[6][7]} {A[6][8]}
{A[7][0]} {A[7][1]} {A[7][2]} | {A[7][3]} {A[7][4]} {A[7][5]} | {A[7][6]} {A[7][7]} {A[7][8]}
{A[8][0]} {A[8][1]} {A[8][2]} | {A[8][3]} {A[8][4]} {A[8][5]} | {A[8][6]} {A[8][7]} {A[8][8]}
"""

class SudokoSolover():
    def __init__(self, A):
       self.posb = [[[True for i in range(1,10)] for x in range(9)] for y in range(9)]
       self.A = A
       self.Initialize()

    def Initialize(self):
      for irow,row in enumerate(self.A):
        for icol, val in enumerate(row):
          if val!=0:
            self.posb[irow][icol]=[True for i in range(9)]
            #posb[irow][icol][val-1]=True


    #Todo this should later be done once into a dictionary
    def get_sub_indices(sel, irow,icol):
      subrow = irow//3
      subcol = icol//3

      startrow=subrow*3
      startcol=subcol*3
      return it.product(range(startrow,startrow+3),range(startcol,startcol+3))


    def update_pos(self):
      rows,cols = np.nonzero(self.A)
      for row,col in zip(rows,cols):
        val=self.A[row,col]

        self.posb[row][col]=[False for i in range(9)]
        self.posb[row][col][val-1]=True

        #loop over all other cells in that row and set value to False
        for runcol in range(9):
          if runcol!=col:
            self.posb[row][runcol][val-1]=False
        for runrow in range(9):
          if runrow!=row:
            self.posb[runrow][col][val-1]=False
        tuples = [t for t in self.get_sub_indices(row,col) if t!=(row,col)]
        for (runrow,runcol) in tuples:
          self.posb[runrow][runcol][val-1]=False

    def updateA(self):
      #check if a particular cell has only one possibility left
      for i,j in it.product(range(9),range(9)):
        if sum(self.posb[i][j])==1:
          val=self.posb[i][j].index(True)+1
          if self.A[i,j]!=val:
            self.A[i,j]=val

      #search for unique posb entries row-wise
      for irow in range(9):
        missingvals = [i for i in range(1,10) if i not in self.A[irow,:]]
        for val in missingvals:
           valstat=[x[val-1] for x in self.posb[irow][:]]
           if sum(valstat)==1:
              runrow=valstat.index(True)
              self.A[irow,runrow]=val

      #search for unique posb entries column-wise
      for icol in range(9):
        missingvals = [i for i in range(1,10) if i not in self.A[:,icol]]
        for val in missingvals:
           valstat=[x[val-1] for x in [i[icol] for i in self.posb]]
           if sum(valstat)==1:
              runrow=valstat.index(True)
              self.A[runrow,icol]=val

      #search for unique posb-entries subcell-wise
      for i in range(3):
        for j in range(3):
          startrow=i*3; startcol=j*3;
          tl=it.product(range(startrow,startrow+3),range(startcol,startcol+3))
          presentvals=[self.A[x] for x in tl if self.A[x]!=0]
          missingvals=[i+1 for i in range(9) if i+1 not in presentvals]
          for val in missingvals:
             count=0;
             pos=None;
             for row,col in tl:
               if self.posb[row][col][val-1]==True:
                  count=count+1
                  pos=(row,col)
             if count==1:
                print("Setting val="+str(val)+" at "+str(pos))

    def solve(self):
        for i in range(999):
            self.update_pos()
            # pos_print(posb)
            self.updateA()
        return self.A

if __name__ == "__main__":
    
    AA=np.loadtxt("in1.txt", delimiter=',', dtype=int)
    solver=SudokoSolover(AA)
    solution = solver.solve()

    img = np.zeros((900,900,3), np.uint8)

    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2

    cv2.line(img,(310,0),(310,900),color,5)
    cv2.line(img,(610,0),(610,900),color,5)
    cv2.line(img,(0,300),(900,300),color,5)
    cv2.line(img,(0,600),(900,600),color,5)

    for i in range(8):
      cv2.line(img,(110+i*100,0),(110+i*100,900),color,1)
      cv2.line(img,(0,98+i*100),(900,98+i*100),color,1)


    for row in range(9):
        for col in range(9):
            loc = (100*row+50, 100*col+50)
            img = cv2.putText(img, f"{solution[row][col]}", loc, font, fontScale, color, thickness, cv2.LINE_AA)


    plt.imshow(img)

    print("Solution\n", solution)


