#!/usr/bin/env python
# coding=utf-8


#5.1　快速绘图


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

#接下来调用figure创建一个绘图对象，并且使它成为当前的绘图对象
#本例中所创建的图表窗口的宽度为8*80 = 640像素
plt.figure(figsize=(8,4))
#但是用工具栏中的保存按钮保存下来的png图像的大小是800*400像素
import matplotlib
print matplotlib.rcParams["savefig.dpi"]
#100

#下面的两行程序通过调用plot函数在当前的绘图对象中进行绘图
#label : 给所绘制的曲线一个名字，此名字在图示(legend)中显示。只要在字符串前后添加"$"符号，
#        matplotlib就会使用其内嵌的latex引擎绘制的数学公式。
#color : 指定曲线的颜色
#linewidth : 指定曲线的宽度
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")

#接下来通过一系列函数设置绘图对象的各个属性
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()

#xlabel : 设置X轴的文字
#ylabel : 设置Y轴的文字
#title : 设置图表的标题
#ylim : 设置Y轴的范围
#legend : 显示图示

#调用plt.show()显示出我们创建的所有绘图对象
plt.show()




#5.1.1　配置属性

#matplotlib所绘制的图的每个组成部分都对应有一个对象，我们可以通过调用这些对象的属性设置
#方法set_*或者pyplot的属性设置函数setp设置其属性值。例如plot函数返回一个 
#matplotlib.lines.Line2D 对象的列表

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, x*x) # plot返回一个列表，通过line,获取其第一个元素
# 调用Line2D对象的set_*方法设置属性值
line.set_antialiased(False)
# 同时绘制sin和cos两条曲线，lines是一个有两个Line2D对象的列表
lines = plt.plot(x, np.sin(x), x, np.cos(x)) #
# 调用setp函数同时配置多个Line2D对象的多个属性值
plt.setp(lines, color="r", linewidth=2.0)
#通过调用Line2D对象line的set_antialiased方法，关闭对象的反锯齿效果。或者通过调用
#plt.setp函数配置多个Line2D对象的颜色和线宽属性。

#我们可以通过调用Line2D对象的get_*方法，或者plt.getp函数获取对象的属性值：

line.get_linewidth()
#1.0
plt.getp(lines[0], "color") # 返回color属性
#'r'
plt.getp(lines[1]) # 输出全部属性
#alpha = 1.0
#animated = False
#antialiased or aa = True
#axes = Axes(0.125,0.1;0.775x0.8)
#... ...

#注意getp函数只能对一个对象进行操作，它有两种用法：
#指定属性名：返回对象的指定属性的值
#不指定属性名：打印出对象的所有属性和其值


#matplotlib的整个图表为一个Figure对象，此对象在调用plt.figure函数时返回，我们
#也可以通过plt.gcf函数获取当前的绘图对象：

f = plt.gcf()
plt.getp(f)
#alpha = 1.0
#animated = False
#...


#Figure对象有一个axes属性，其值为AxesSubplot对象的列表，每个AxesSubplot对象代表图表
#中的一个子图，前面所绘制的图表只包含一个子图，当前子图也可以通过plt.gca获得：

plt.getp(f, "axes")
#[<matplotlib.axes.AxesSubplot object at 0x05CDD170>]
plt.gca()
#<matplotlib.axes.AxesSubplot object at 0x05CDD170>

#用plt.getp可以发现AxesSubplot对象有很多属性，例如它的lines属性为此子图所包括的 
#Line2D 对象列表：

alllines = plt.getp(plt.gca(), "lines")
alllines
#<a list of 3 Line2D objects>
alllines[0] == line # 其中的第一条曲线就是最开始绘制的那条曲线
#True

#5.2　绘制多轴图



#一个绘图对象(figure)可以包含多个轴(axis)，在Matplotlib中用轴表示一个绘图区域，可以将
#其理解为子图。上面的第一个例子中，绘图对象只包括一个轴，因此只显示了一个轴(子图)。
#我们可以使用subplot函数快速绘制有多个轴的图表。subplot函数的调用形式如下：

#subplot(numRows, numCols, plotNum)

#subplot将整个绘图区域等分为numRows行 * numCols列个子区域，然后按照从左到右，从上到下
#的顺序对每个子区域进行编号，左上的子区域的编号为1。如果numRows，numCols和plotNum这三
#个数都小于10的话，可以把它们缩写为一个整数，例如subplot(323)和subplot(3,2,3)是相同的。
#subplot在plotNum指定的区域中创建一个轴对象。如果新创建的轴和之前创建的轴重叠的话，
#之前的轴将被删除。


#下面的程序创建3行2列共6个轴，通过axisbg参数给每个轴设置不同的背景颜色。

for idx, color in enumerate("rgbyck"):
    plt.subplot(320+idx+1, axisbg=color)
plt.show()


#如果希望某个轴占据整个行或者列的话，可以如下调用subplot：

plt.subplot(221) # 第一行的左图
plt.subplot(222) # 第一行的右图
plt.subplot(212) # 第二整行
plt.show()


#当绘图对象中有多个轴的时候，可以通过工具栏中的Configure Subplots按钮，交互式地调节
#轴之间的间距和轴与边框之间的距离。如果希望在程序中调节的话，可以调用subplots_adjust
#函数，它有left, right, bottom, top, wspace, hspace等几个关键字参数，这些参数的值都
#是0到1之间的小数，它们是以绘图区域的宽高为1进行正规化之后的坐标或者长度。

#5.3　配置文件
# http://old.sebug.net/paper/books/scipydoc/matplotlib_intro.html


#5.4　Artist对象

#matplotlib API包含有三层：

#backend_bases.FigureCanvas : 图表的绘制领域
#backend_bases.Renderer : 知道如何在FigureCanvas上如何绘图
#artist.Artist : 知道如何使用Renderer在FigureCanvas上绘图

#FigureCanvas和Renderer需要处理底层的绘图操作，例如使用wxPython在界面上绘图，或者使
#用PostScript绘制PDF。Artist则处理所有的高层结构，例如处理图表、文字和曲线等的绘制和
#布局。通常我们只和Artist打交道，而不需要关心底层的绘制细节。

#Artists分为简单类型和容器类型两种。简单类型的Artists为标准的绘图元件，例如Line2D、 
#Rectangle、 Text、AxesImage 等等。而容器类型则可以包含许多简单类型的Artists，使它们
#组织成一个整体，例如Axis、 Axes、Figure等。

#直接使用Artists创建图表的标准流程如下：

#创建Figure对象
#用Figure对象创建一个或者多个Axes或者Subplot对象
#调用Axies等对象的方法创建各种简单类型的Artists

#下面首先调用pyplot.figure辅助函数创建Figure对象，然后调用Figure对象的add_axes方法
#在其中创建一个Axes对象，add_axes的参数是一个形如[left, bottom, width, height]的列
#表，这些数值分别指定所创建的Axes对象相对于fig的位置和大小，取值范围都在0到1之间：

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0.15, 0.1, 0.7, 0.3])
#然后我们调用ax的plot方法绘图，创建一条曲线，并且返回此曲线对象(Line2D)。

line, = ax.plot([1,2,3],[1,2,1])
ax.lines
#[<matplotlib.lines.Line2D object at 0x0637A3D0>]
line
#<matplotlib.lines.Line2D object at 0x0637A3D0>
#ax.lines是一个为包含ax的所有曲线的列表，后续的ax.plot调用会往此列表中添加新的曲线。
#如果想删除某条曲线的话，直接从此列表中删除即可。

#Axes对象还包括许多其它的Artists对象，例如我们可以通过调用set_xlabel设置其X轴上的标题：

ax.set_xlabel("time")
#如果我们查看set_xlabel的源代码的话，会发现它是通过调用下面的语句实现的：

#self.xaxis.set_label_text(xlabel)
#如果我们一直跟踪下去，会发现Axes的xaxis属性是一个XAxis对象：

ax.xaxis
#<matplotlib.axis.XAxis object at 0x06343230>
#XAxis的label属性是一个Text对象：

ax.xaxis.label
#<matplotlib.text.Text object at 0x06343290>
#而Text对象的_text属性为我们设置的值：

ax.xaxis.label._text
#'time'
#这些对象都是Artists，因此也可以调用它们的属性获取函数来获得相应的属性：

ax.xaxis.label.get_text()
#'time'

#5.4.1　Artist的属性

#图表中的每个元素都用一个matplotlib的Artist对象表示，而每个Artist对象都有一大堆属性
#控制其显示效果。例如Figure对象和Axes对象都有patch属性作为其背景，它的值是一个
#Rectangle对象。通过设置此它的一些属性可以修改Figrue图表的背景颜色或者透明度等属性，
#下面的例子将图表的背景颜色设置为绿色：

fig = plt.figure()
fig.show()
fig.patch.set_color("g")
fig.canvas.draw()
#patch的color属性通过set_color函数进行设置，属性修改之后并不会立即反映到图表的显示上，
#还需要调用fig.canvas.draw()函数才能够更新显示。

#下面是Artist对象都具有的一些属性：

#alpha : 透明度，值在0到1之间，0为完全透明，1为完全不透明
#animated : 布尔值，在绘制动画效果时使用
#axes : 此Artist对象所在的Axes对象，可能为None
#clip_box : 对象的裁剪框
#clip_on : 是否裁剪
#clip_path : 裁剪的路径
#contains : 判断指定点是否在对象上的函数
#figure : 所在的Figure对象，可能为None
#label : 文本标签
#picker : 控制Artist对象选取
#transform : 控制偏移旋转
#visible : 是否可见
#zorder : 控制绘图顺序
#Artist对象的所有属性都通过相应的 get_* 和 set_* 函数进行读写，例如下面的语句将alpha
#属性设置为当前值的一半：

fig.set_alpha(0.5*fig.get_alpha())
#如果你想用一条语句设置多个属性的话，可以使用set函数：

fig.set(alpha=0.5, zorder=2)
#使用前面介绍的 matplotlib.pyplot.getp 函数可以方便地输出Artist对象的所有属性名和值。

plt.getp(fig.patch)
#    aa = True
#    alpha = 1.0
#    animated = False
#    antialiased or aa = True
#    ... ...


#5.4.2　Figure容器
#现在我们知道如何观察和修改已知的某个Artist对象的属性，接下来要解决如何找到指定的Artist
#对象。前面我们介绍过Artist对象有容器类型和简单类型两种，这一节让我们来详细看看容器类型的内容。

#最大的Artist容器是matplotlib.figure.Figure，它包括组成图表的所有元素。图表的背景是
#一个Rectangle对象，用Figure.patch属性表示。当你通过调用add_subplot或者add_axes方法
#往图表中添加轴(子图时)，这些子图都将添加到Figure.axes属性中，同时这两个方法也返回添加
#进axes属性的对象，注意返回值的类型有所不同，实际上AxesSubplot是Axes的子类。

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.3])
ax1
#<matplotlib.axes.AxesSubplot object at 0x056BCA90>
ax2
#<matplotlib.axes.Axes object at 0x056BC910>
fig.axes
#[<matplotlib.axes.AxesSubplot object at 0x056BCA90>,
#<matplotlib.axes.Axes object at 0x056BC910>]

#为了支持pylab中的gca()等函数，Figure对象内部保存有当前轴的信息，因此不建议直接对
#Figure.axes属性进行列表操作，而应该使用add_subplot, add_axes, delaxes等方法进行
#添加和删除操作。但是使用for循环对axes中的每个元素进行操作是没有问题的，下面的语句
#打开所有子图的栅格。

for ax in fig.axes: ax.grid(True)

#Figure对象可以拥有自己的文字、线条以及图像等简单类型的Artist。缺省的坐标系统为像素
#点，但是可以通过设置Artist对象的transform属性修改坐标系的转换方式。最常用的Figure对
#象的坐标系是以左下角为坐标原点(0,0)，右上角为坐标(1,1)。下面的程序创建并添加两条直线
#到fig中：

from matplotlib.lines import Line2D
fig = plt.figure()
line1 = Line2D([0,1],[0,1], transform=fig.transFigure, figure=fig, color="r")
line2 = Line2D([0,1],[1,0], transform=fig.transFigure, figure=fig, color="g")
fig.lines.extend([line1, line2])
fig.show()

#注意为了让所创建的Line2D对象使用fig的坐标，我们将fig.TransFigure赋给Line2D对象的
#transform属性；为了让Line2D对象知道它是在fig对象中，我们还设置其figure属性为fig；
#最后还需要将创建的两个Line2D对象添加到fig.lines属性中去。
#
#Figure对象有如下属性包含其它的Artist对象：
#
#axes : Axes对象列表
#patch : 作为背景的Rectangle对象
#images : FigureImage对象列表，用来显示图片
#legends : Legend对象列表
#lines : Line2D对象列表
#patches : patch对象列表
#texts : Text对象列表，用来显示文字


#5.4.3　Axes容器
#Axes容器是整个matplotlib库的核心，它包含了组成图表的众多Artist对象，并且有许多方法函
#数帮助我们创建、修改这些对象。和Figure一样，它有一个patch属性作为背景，当它是笛卡尔坐
#标时，patch属性是一个Rectangle对象，而当它是极坐标时，patch属性则是Circle对象。例如
#下面的语句设置Axes对象的背景颜色为绿色：

fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_facecolor("green")
#当你调用Axes的绘图方法（例如plot），它将创建一组Line2D对象，并将所有的关键字参数传递
#给这些Line2D对象，并将它们添加进Axes.lines属性中，最后返回所创建的Line2D对象列表：

x, y = np.random.rand(2, 100)
line, = ax.plot(x, y, "-", color="blue", linewidth=2)
line
#<matplotlib.lines.Line2D object at 0x03007030>
ax.lines
#[<matplotlib.lines.Line2D object at 0x03007030>]
#注意plot返回的是一个Line2D对象的列表，因为我们可以传递多组X,Y轴的数据，一次绘制多条曲线。

#与plot方法类似，绘制直方图的方法bar和绘制柱状统计图的方法hist将创建一个Patch对象的
#列表，每个元素实际上都是Patch的子类Rectangle，并且将所创建的Patch对象都添加进
#Axes.patches属性中：

ax = fig.add_subplot(111)
n, bins, rects = ax.hist(np.random.randn(1000), 50, facecolor="blue")
rects
#<a list of 50 Patch objects>
rects[0]
#<matplotlib.patches.Rectangle object at 0x05BC2350>
ax.patches[0]
#<matplotlib.patches.Rectangle object at 0x05BC2350>

#一般我们不会直接对Axes.lines或者Axes.patches属性进行操作，而是调用add_line或者
#add_patch等方法，这些方法帮助我们完成许多属性设置工作：

fig = plt.figure()
ax = fig.add_subplot(111)
rect = matplotlib.patches.Rectangle((1,1), width=5, height=12)
print rect.get_axes() # rect的axes属性为空
#None
rect.get_transform() # rect的transform属性为缺省值
#BboxTransformTo(Bbox(array([[  1.,   1.],
#       [  6.,  13.]])))
ax.add_patch(rect) # 将rect添加进ax
#<matplotlib.patches.Rectangle object at 0x05C34E50>
rect.get_axes() # 于是rect的axes属性就是ax
#<matplotlib.axes.AxesSubplot object at 0x05C09CB0>
# rect的transform属性和ax的transData相同
rect.get_transform()
#... # 太长，省略
ax.transData
#... # 太长，省略
ax.get_xlim() # ax的X轴范围为0到1，无法显示完整的rect
#(0.0, 1.0)
ax.dataLim._get_bounds() # 数据的范围和rect的大小一致
#(1.0, 1.0, 5.0, 12.0)
ax.autoscale_view() # 自动调整坐标轴范围
ax.get_xlim() # 于是X轴可以完整显示rect
#(1.0, 6.0)
plt.show()
#通过上面的例子我们可以看出，add_patch方法帮助我们设置了rect的axes和transform属性。

#下面详细列出Axes包含各种Artist对象的属性：

#artists : Artist对象列表
#patch : 作为Axes背景的Patch对象，可以是Rectangle或者Circle
#collections : Collection对象列表
#images : AxesImage对象列表
#legends : Legend对象列表
#lines : Line2D对象列表
#patches : Patch对象列表
#texts : Text对象列表
#xaxis : XAxis对象
#yaxis : YAxis对象
#下面列出Axes的创建Artist对象的方法：
#
#Axes的方法	  所创建的对象	添加进的列表
#annotate	  Annotate	       texts
#bars      	  Rectangle	       patches
#errorbar	Line2D,Rectangle	 lines,patches
#fill         Polygon	       patches
#hist	        Rectangle       patches
#imshow	  AxesImage	       images
#legend	   Legend	       legends
#plot	         Line2D	        lines
#scatter  PolygonCollection	Collections
#text     	   Text	       texts
#下面以绘制散列图(scatter)为例，验证一下：

fig = plt.figure()
ax = fig.add_subplot(111)
t = ax.scatter(np.random.rand(20), np.random.rand(20))
t # 返回值为CircleCollection对象
#<matplotlib.collections.CircleCollection object at 0x06004230>
ax.collections # 返回的对象已经添加进了collections列表中
#[<matplotlib.collections.CircleCollection object at 0x06004230>]
fig.show()
t.get_sizes() # 获得Collection的点数
#20


#5.4.4　Axis容器

#Axis容器包括坐标轴上的刻度线、刻度文本、坐标网格以及坐标轴标题等内容。刻度包括主刻度和副
#刻度，分别通过Axis.get_major_ticks和Axis.get_minor_ticks方法获得。每个刻度线都是一
#个XTick或者YTick对象，它包括实际的刻度线和刻度文本。为了方便访问刻度线和文本，Axis对象
#提供了get_ticklabels和get_ticklines方法分别直接获得刻度线和刻度文本：
pl = plt.figure()
pl.plot([1,2,3],[4,5,6])
#[<matplotlib.lines.Line2D object at 0x0AD3B670>]
pl.show()
axis = pl.gca().xaxis
axis.get_ticklocs() # 获得刻度的位置列表
#array([ 1. ,  1.5,  2. ,  2.5,  3. ])
axis.get_ticklabels() # 获得刻度标签列表
#<a list of 5 Text major ticklabel objects>
[x1.get_text() for x1 in axis.get_ticklabels()] # 获得刻度的文本字符串
#[u'1.0', u'1.5', u'2.0', u'2.5', u'3.0']
axis.get_ticklines() # 获得主刻度线列表，图的上下刻度线共10条
#<a list of 10 Line2D ticklines objects>
axis.get_ticklines(minor=True) # 获得副刻度线列表
#<a list of 0 Line2D ticklines objects>
#获得刻度线或者刻度标签之后，可以设置其各种属性，下面设置刻度线为绿色粗线，文本为红色并且旋转45度：

for label in axis.get_ticklabels():
    label.set_color("red")
    label.set_rotation(45)
    label.set_fontsize(16)

for line in axis.get_ticklines():
    line.set_color("green")
    line.set_markersize(25)
    line.set_markeredgewidth(3)
    
    
#上面的例子中，获得的副刻度线列表为空，这是因为用于计算副刻度的对象缺省为NullLocator，
#它不产生任何刻度线；而计算主刻度的对象为AutoLocator，它会根据当前的缩放等配置自动计算
#刻度的位置：

axis.get_minor_locator() # 计算副刻度的对象
#<matplotlib.ticker.NullLocator instance at 0x0A014300>
axis.get_major_locator() # 计算主刻度的对象
#<matplotlib.ticker.AutoLocator instance at 0x09281B20>

#我们可以使用程序为Axis对象设置不同的Locator对象，用来手工设置刻度的位置；设置Formatter
#对象用来控制刻度文本的显示。下面的程序设置X轴的主刻度为pi/4，副刻度为pi/20，并且主刻度
#上的文本以pi为单位：

# -*- coding: utf-8 -*-
import matplotlib.pyplot as pl
from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np
x = np.arange(0, 4*np.pi, 0.01)
y = np.sin(x)
pl.figure(figsize=(8,4))
pl.plot(x, y)
ax = pl.gca()

def pi_formatter(x, pos):
    """
    比较罗嗦地将数值转换为以pi/4为单位的刻度文本
    """
    m = np.round(x / (np.pi/4))
    n = 4
    if m%2==0: m, n = m/2, n/2
    if m%2==0: m, n = m/2, n/2
    if m == 0:
        return "0"
    if m == 1 and n == 1:
        return "$\pi$"
    if n == 1:
        return r"$%d \pi$" % m
    if m == 1:
        return r"$\frac{\pi}{%d}$" % n
    return r"$\frac{%d \pi}{%d}$" % (m,n)

# 设置两个坐标轴的范围
pl.ylim(-1.5,1.5)
pl.xlim(0, np.max(x))

# 设置图的底边距
pl.subplots_adjust(bottom = 0.15)

pl.grid() #开启网格

# 主刻度为pi/4
ax.xaxis.set_major_locator( MultipleLocator(np.pi/4) )

# 主刻度文本用pi_formatter函数计算
ax.xaxis.set_major_formatter( FuncFormatter( pi_formatter ) )

# 副刻度为pi/20
ax.xaxis.set_minor_locator( MultipleLocator(np.pi/20) )

# 设置刻度文本的大小
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(16)
pl.show()
#关于刻度的定位和文本格式的东西都在matplotlib.ticker中定义，程序中使用到如下两个类：

#MultipleLocator : 以指定值的整数倍为刻度放置刻度线
#FuncFormatter : 使用指定的函数计算刻度文本，他会传递给所指定的函数两个参数：刻度值和刻
#度序号，程序中通过比较笨的办法计算出刻度值所对应的刻度文本

#此外还有很多预定义的Locator和Formatter类，详细内容请参考相应的API文档。
































































