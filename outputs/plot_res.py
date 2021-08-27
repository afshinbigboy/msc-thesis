import glob
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

font = {'weight' : 'normal',
        'size'   : 24}

mpl.rc('font', **font)



fns = (glob.glob("logs/*.txt"))

results = []
for fn in fns:
    with open(fn, 'r') as f:
        text = f.readlines()
        if len(text) < 5:
            continue
        n = fn.split('n')[1].split('_')[0]
        m = fn.split('m')[1].split('_')[0]

        if int(n)>30 or int(n)<6:
            continue

        last_error = text[-1].split('last_error')[-1][1:].split(',')[0]

        res = (int(n), int(m), float(last_error))
        results.append(res)


# plot  < n - error >
t = results.copy()
t = sorted(t, key=lambda x: x[0])
x = [i[0] for i in t]
y = [j[2] for j in t]

Xs = list(set(x))

data = []
for i in Xs:
    data.append([d[2] for d in results if d[0]==i])

plt.figure(figsize=[30,13])
plt.title('Best tree errors for different number of cells')
plt.xlabel('Number of Cells')
plt.ylabel('Error')
plt.violinplot(data, Xs, points=60, widths=0.7, showmeans=True,
                      showextrema=True, showmedians=True, bw_method=0.5)
plt.savefig('N_Err')
plt.close()





# # plot  < m - error >
# t = results.copy()
# t = sorted(t, key=lambda x: x[0])
# x = [i[1] for i in t]
# y = [j[2] for j in t]

# Xs = list(set(x))

# data = []
# for i in Xs:
#     data.append([d[2] for d in results if d[1]==i])

# plt.figure(figsize=[30,13])
# plt.title('Best tree errors for different number of mutations')
# plt.xlabel('Number of Mutations')
# plt.ylabel('Error')
# plt.violinplot(data, Xs, points=60, widths=0.7, showmeans=True,
#                       showextrema=True, showmedians=True, bw_method=0.5)
# plt.savefig('M_Err')
# plt.close()





# plot  < n - error >
t = results.copy()
t = sorted(t, key=lambda x: x[0])
x = [i[0] for i in t]
y = [j[2] for j in t]

Xs = list(set(x))

data = []
for i in Xs:
    data.append([d[2]/(d[0]*d[1]) for d in results if d[0]==i])

plt.figure(figsize=[30,13])
plt.title('Best tree mean-errors for different number of cells')
plt.xlabel('Number of Cells')
plt.ylabel('Mean-Error')
plt.violinplot(data, Xs, points=60, widths=0.7, showmeans=True,
                      showextrema=True, showmedians=True, bw_method=0.5)
plt.savefig('N_Err_mean')
plt.close()