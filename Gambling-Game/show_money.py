from Gamblers import Gamblers as Gamblers
import matplotlib.pyplot as plt
from pylab import *
# mpl.rcParams['font.sans-serif'] = ['SimHei']
class show_money:

    def __init__(self,number = 100):
        self.number = number
    
    def show(self,rounds = 100,money = 100):

        self.rounds = rounds
        self.money = money
        
        test = Gamblers(self.number,self.money)
        x_values = range(1,self.number+1,1)
        variances = []
        for l in range(int(self.rounds/9+1)):
            all_y_values = [[] for i in range(0,9)]
            all_max_values = [[] for i in range(0,9)]

            plt.style.use('seaborn')
            fig, ax = plt.subplots(3,3,figsize = (14,10))
            for round in range(0,9):

                y_values = test.start_Gambling()
                self.variance = float(0)
                for v in range(self.number-1):
                    self.variance += pow(y_values[v]-self.money,2)
                
                self.variance = pow(self.variance/self.number,0.5)
                variances.append(self.variance)
                all_y_values[round] = y_values[:]

                y_max = max(y_values)
                x_y_max = y_values.index(y_max)
                max_indexs = []
                for x_value in x_values:
                    if y_values[x_value-1] == y_max:    
                        max_indexs.append(x_value)

                all_max_values[round] = max_indexs[:]

            print(all_y_values)
            print(all_max_values)
            print(variances)
            count = 0
            for i in range(0,3):
                for j in range(0,3):
                    count += 1
                    if 9*l+count <= self.rounds:
                        try:
                            ax[i,j].bar(x = x_values,height = all_y_values[count-1],color='indianred', alpha=0.8)
                        except:
                            continue
                        else:
                            
                            title = f"Gambling_Round_{9*l+count}"
                            title += f"\nNow winner is {all_max_values[count-1]}"
                            ax[i,j].set_title(title,fontsize = 16)
                            ax[i,j].set_xlabel("Serial Number",fontsize = 12)
                            ax[i,j].set_ylabel("Money",fontsize = 12)
                            ax[i,j].tick_params(axis='both',labelsize = 12)

                            for x_2 in all_max_values[count-1]:
                                ax[i,j].bar(x = x_2,height = all_y_values[count-1][x_2-1],color='indianred', alpha=0.8)
                #ax[0].bar(x = x_value,height = y_max,color='steelblue', alpha=0.8)
                

            plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.3,hspace=0.7)
            x_label = range(1,self.number+1,1)
            filename = f"fig{l}.png"
            plt.savefig(f"C:/Users/Republic/Desktop/Gambling_results/{filename}")
        
        x_variance = list(range(1,self.rounds+1))
        y_variance = variances
        plt.style.use('seaborn')
        fig2,ax2 = plt.subplots()
        title = f"Variance"
        ax2.plot(x_variance,y_variance[:self.rounds],c = 'indianred',linewidth = 2)
        ax2.set_title(title,fontsize = 16)
        ax2.set_xlabel("Serial Number",fontsize = 12)
        ax2.set_ylabel("Variances",fontsize = 12)
        ax2.tick_params(axis='both',labelsize = 12)
        filename = f"Variance.png"
        plt.savefig(f"C:/Users/Republic/Desktop/Gambling_results/{filename}")

show1 = show_money(10)
#几个人
show1.show(200,100)
#几回合,起始钱币

