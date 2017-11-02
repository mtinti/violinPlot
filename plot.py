


import pandas as pd
import seaborn as sns
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
import numpy as np
#facilitate violin plot of a dataframe using
#seaborn
class ViolinPlot():
    def __init__(self, df = pd.DataFrame()):
        self.df = df
    
    def plot(self, cols=[], ax='', log=False):
        #rearrange columns (vertical stack)
        if len(cols) == 0:
            cols=self.df.columns
            #print cols
        selection =  self.df[cols]
        temp_1 = [selection[n].to_frame() for n in cols]
        temp_2 =[]
        for temp_df, col in zip(temp_1,cols):
            temp_df['col']=col
            temp_df.columns = ['value', 'col']
            temp_2.append(temp_df)
        temp_2 = pd.concat(temp_2,ignore_index=True)
        print temp_2.head()
        if log ==True:
            temp_2['value']=np.log10(temp_2['value'])
            temp_2 = temp_2.replace([np.inf, -np.inf], np.nan)
            temp_2.dropna(inplace=True)
        ax=sns.violinplot(x='col', y='value', data=temp_2, ax=ax)
        return ax
        

if __name__ == '__main__':
        in_df = pd.DataFrame.from_csv('in_data/df.txt',sep='\t')
        print in_df.head()
        cols = ['median_Reporter intensity '+str(n) for n in range(1,10)]  
        fig, ax = plt.subplots()
        vp = ViolinPlot(in_df)
        ax = vp.plot(cols=cols, ax=ax,log=True)
        xtick_position = range(len(cols))
        plt.xticks(xtick_position,  rotation=40,ha='right')
        #to use only number in ticks
        #plt.xticks(xtick_position,  xtick_position)
        #to change the tick labels
        #plt.xticks(xtick_position,  [str('a') for a in cols])
        plt.savefig('violin_plot.svg')
        plt.show()
