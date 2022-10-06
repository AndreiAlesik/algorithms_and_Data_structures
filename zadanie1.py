import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
def read_algo(name):
    df = pd.read_csv(f'{name}.csv')
    df['average'] = df.drop(['generation', 'effort'], axis=1).mean(axis=1)
    return df

names = ['1ers', '1crs', '2crs', '1c', '2c']
frames = twocel_rs, twocel, cel_rs, cel, rsel = [read_algo(x) for x in names]
twocel.head()
meta = ['generation', 'effort', 'average']
labels = ['1-Evol-RS', '1-Coev-RS', '2-Coev-RS', '1-Coev', '2-Coev']
colors = ['blue', 'green', 'red', 'black', 'magenta']
markers = ['o', 'v', 'D', 's', 'd']

plt.rcParams.update({
    'axes.prop_cycle': matplotlib.cycler(color=colors),
    'font.family': 'serif', 'font.size': 8,
    'mathtext.fontset': 'dejavuserif',
    'xtick.direction': 'in', 'ytick.direction': 'in',
    'grid.linestyle': [1, 4],
})

fig,axes = plt.subplots(nrows=1, ncols=2)
fig.set_figwidth(15)

# lineplot (left)

ax1 = axes[0]

for i, df in enumerate(frames):
    ax1.plot(df.effort / 1000, df.average * 100,
             linewidth=0.9, label=labels[i], marker=markers[i],
             markevery=25, markersize=5,
             markeredgecolor='black', markeredgewidth=0.5)

ax1.grid()
ax1.legend(loc='lower right', numpoints=2, fontsize=9)
ax1.set_xlabel(r'Rozegranych gier ($\times 1000$)')
ax1.set_ylabel('Odsetek wygranych gier [%]')
ax1.set_xlim(0, 500)
ax1.set_ylim(60, 100)

ax1_1 = ax1.twiny()
ax1_1.set_xticks([0, 40, 80, 120, 160, 200])
ax1_1.set_xticklabels(range(0, 200 + 1, 40))

ax1_2 = ax1.twinx()
ax1_2.set_ylim(60, 100)
#ax1_2.set_yticks(range(60, 100 + 1, 5))
ax1_2.set_yticklabels([])

# boxplot (right)

boxes = [df.drop(meta, axis=1).values[-1] * 100 for df in frames]

ax2 = axes[1]
ax2.boxplot(boxes,
            showmeans=True,
            notch=True,
            boxprops={'color': 'blue'},
            whiskerprops={'color': 'blue', 'linestyle': '-', 'dashes': (6, 5)},
            meanprops={'marker': 'o', 'markersize': 4, 'markerfacecolor': 'blue', 'markeredgecolor': 'black'},
            medianprops={'color': 'red'},
            flierprops={'marker': '+', 'markersize': 4, 'markeredgewidth': 0.9, 'markerfacecolor': 'blue',
                        'markeredgecolor': 'blue'},
            capprops={'color': 'black'})

ax2.yaxis.tick_right()
ax2.grid()
ax2.set_ylim(60, 100)
ax2.set_xticklabels(labels, rotation=20)
#ax2.set_yticklabels(range(60, 100 + 1, 5))

ax2_1 = ax2.twiny()
ax2_1.set_xlim(-0.5, 4.5)
ax2_1.set_xticks(range(0, 5))
ax2_1.set_xticklabels([])

plt.savefig('zadanie1.png')