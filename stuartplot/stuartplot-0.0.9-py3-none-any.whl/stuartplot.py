import matplotlib.pyplot as plt

class Figure:

    def __init__(self, 
                figsize=(8, 8),
                title=None, 
                title_size=10,
                lay=(1, 1), 
                spacing=(.2, .2),
                **kwargs
                ):

        self.fig = plt.figure(figsize=figsize)
        self.fig.subplots_adjust(wspace=spacing[0], hspace=spacing[1], top=0.8)

        if title is not None:
            self.fig.suptitle(title, fontsize=title_size)

        self.axes = [self.fig.add_subplot(lay[0], lay[1], i) for i in range(1, lay[0]*lay[1]+1)]
        self.indices = lay[0]*lay[1]

    def label(self, axis, labels=(None, None, None), sizes=(15,15,15)):
        
        if labels[0] is not None:
            self.axes[axis].set_title(labels[0], fontsize=sizes[0])

        if labels[1] is not None:
            self.axes[axis].set_xlabel(labels[1], fontsize=sizes[1])

        if labels[2] is not None:
            self.axes[axis].set_ylabel(labels[2], fontsize=sizes[2])

    def show(self, legend_size=13, **kwargs):

        for ax in self.axes:
            ax.tick_params(labelsize=15)

            if ax.get_legend_handles_labels()[1] != []:
                ax.legend(fontsize=legend_size)
        
        plt.show()