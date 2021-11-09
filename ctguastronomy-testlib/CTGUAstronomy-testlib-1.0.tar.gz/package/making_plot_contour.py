import matplotlib.pyplot as plt
from astropy.io import fits
from astrodendro import Dendrogram

"""
Dendrogram code  
计算类别，进行聚类
"""
# 读入fits文件
image = fits.getdata(r'data\PerA_Extn2MASS_F_Gal.fits')
our_image = fits.getdata(r'data\hdu0_mosaic_L.fits')
our_image_1 = our_image[0, :, :]
# 计算Dendrogram类型的实体，包含树干、分支和叶子，均为列表数据
d = Dendrogram.compute(our_image_1, min_value=2.0, min_delta=1., min_npix=10)

p = d.plotter()
# 创建图形窗口
fig = plt.figure()
# 画区域 图
ax = fig.add_subplot(2, 1, 1)
ax.imshow(image, origin='lower', interpolation='nearest', cmap=plt.cm.Blues, vmax=4.0)

# Plot the whole tree
p.plot_tree(ax, color='black')

# Highlight two branches

# 将不同区域高亮显示出来
p.plot_contour(ax, structure=6, lw=3, colors='red')
# p.plot_contour(ax, structure=16, lw=3, colors='orange')
# Add axis labels
ax.set_xlabel("Structure")
ax.set_ylabel("Flux")

# 画树形图
ax = fig.add_subplot(2, 1, 2)

# Plot the whole tree
p.plot_tree(ax, colors='black')

# Highlight two branches

# p.plot_tree(ax, colors='red')
# p.plot_tree(ax, colors='orange')

# Add axis labels
ax.set_xlabel("Structure")
ax.set_ylabel("Flux")

# 显示结果
fig.show()
