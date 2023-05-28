import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Module5Class:
    def __init__(self):
        pass

    def execute(self):
        np.random.seed(0)
        df = pd.DataFrame(data={'a': np.random.randint(0, 100, 30),
                                'b': np.random.randint(0, 100, 30),
                                'c': np.random.randint(0, 100, 30)})
        fig, ax = plt.subplots(3, 1, figsize=(15, 18))
        ax[0].bar(df.index.values, df['a'], color='blue')
        ax[0].set_ylabel('a')
        for i in range(df.shape[0]):
            ax[0].text(i, df['a'][i] + 1, df['a'][i], horizontalalignment='center')
        ax[0].legend(['a'])
        ax[1].bar(df.index.values, df['b'], color='orange')
        ax[1].set_ylabel('b')
        for i in range(df.shape[0]):
            ax[1].text(i, df['b'][i] + 1, df['b'][i], horizontalalignment='center')
        ax[1].legend(['b'])
        ax[2].bar(df.index.values, df['a'], color='blue')
        ax[2].bar(df.index.values, df['b'], bottom=df['a'], color='orange')
        ax[2].set_ylabel('c')
        for i in range(df.shape[0]):
            ax[2].text(i, df['a'][i] + df['b'][i] + 1, df['a'][i] + df['b'][i], horizontalalignment='center')
        ax[2].legend(['a', 'b'])

        plt.savefig('module5_plot.png')  # Save the plot as an image file

        # Open a new window in a web browser to display the plot
        import webbrowser
        webbrowser.open('module5_plot.png')

        plt.show()
