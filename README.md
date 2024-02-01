# Inkscape shortcut manager

*A shortcut manager that speeds up drawing (mathematical) figures in [Inkscape](https://inkscape.org/).*
本仓库 fork 自 [Castel 的仓库](https://github.com/gillescastel/inkscape-figures), 他真的好强啊呜呜呜

## Problem

此程序用来更快地在 inkscape 中画图, Castel 大神在笔记里用它做的图如下


![Elliptic curve](./examplefigures/fig_1.png)

![Complex Analysis](./examplefigures/fig_2.png)


## Solution

这个快捷键管理器可以监听传入 inkscape 的键盘输入, 并将它们转化为自定义的操作.


- **按下组合键可以快速更改选中对象的样式**
  - <kbd>d</kbd>+<kbd>a</kbd> 对应 **d**otted **a**rrow, <kbd>f</kbd>+<kbd>s</kbd> 会 **f**ills the selection in gray and adds a **s**troke.
  - 想要 **d**otted and **f**illed, 就按 <kbd>f</kbd> + <kbd>d</kbd>.
  - <kbd>s</kbd>, <kbd>a</kbd>, <kbd>d</kbd>, <kbd>g</kbd>, <kbd>h</kbd>, <kbd>x</kbd>, <kbd>e</kbd>, <kbd>b</kbd>, <kbd>f</kbd>, <kbd>w</kbd> 这些键的组合会给出各种组合样式.
  - 如果想要非组合的样式, 比如单纯的 **d**otted stroke but no filling, 那就按 <kbd>Space</kbd>+<kbd>d</kbd>. 在映射规则里, <kbd>Space</kbd> 用作占位符.


- **保存自定义的样式和形状.** 按下 <kbd>Shift+S</kbd> 或者 <kbd>Shift+A</kbd> , 然后在弹出窗口内输入名字, 这会保存选中部分的 style 或者 object. 调用它们时, 按下 <kbd>s</kbd> 或 <kbd>a</kbd> 并输入名字 \(无弹出窗口\). 按键映射中没有的样式可以通过这个手动保存.


- **用你自己的编辑器插入 LaTeX 公式.**
  - 按下 <kbd>t</kbd> 会打开一个特殊的最小化 vim 窗口 \(当然可以配置成你喜欢的编辑器\). 写入 LaTeX 代码并保存, shortcut manager 会自动将它放入 Inkscape 中.
  - 按下 <kbd>Shift+T</kbd> 的操作也类似, 但它会把你所写的公式与 `~/.config/inkscape-shortcut-manager/config.py` 中的 LaTX 模板拼成一个完整可编译的 LaTeX 文件, 并将编译得到的 `.pdf` 文件转换成 `.svg` 文件, 通过剪贴板插入到 Inkscape 内.

  
- **更顺手的常用功能键盘映射**. 画图时, 右手握着鼠标, Castel 把常用功能都放到了键盘左侧. Press <kbd>w</kbd> for pencil, <kbd>x</kbd> to toggle snapping, <kbd>f</kbd> for Bézier, <kbd>z</kbd> to undo, <kbd>Shift</kbd>+<kbd>z</kbd> to delete and <kbd>\`</kbd> to dis/enable the shortcut manager.

强烈推荐阅读一下 Castel 大神的 [博客文章](https://castel.dev/post/lecture-notes-2), 这篇博客中的按键映射图如下 \(单个按键的样式需要与占位符 <kbd>Space</kbd> 一同按下\).

![按键对应](https://castel.dev/static/d6340105c5f1f48d6bbbe4ca4d1e7e48/44b06/default-styles-keys2.png)

## Installing

这份代码只在 GNU/Linux 上可以运行, 并要求 Python ≥ 3.6.
并且有如下的外部依赖:

- `Xlib` 用于键盘事件的监听
- `pdflatex` 和 `pdf2svg` 来在 Inkscape 中插入编译好的 LaTeX 公式
- `xclip` 调用剪贴板传递文件, copy 样式
- `rofi` 作为 picker 为保存的样式命名

运行 `python3 main.py` 然后打开 Inkscape 窗口就可以使用快捷键了 \(虽然程序中可以 detect existing window, 但本人在 ubuntu 23.0, xorg 上实测时并不可用\).

## Configuration

程序会读取在 `~/.config/inkscape-shortcut-manager/config.py` 的配置文件, 在使用 vim 输入公式时会调用. rofi 主题, 公式源码字体, LaTeX 模板都从 `~/.config/inkscape-shortcut-manager/config.py` 中读取.
在 `examples` 目录下是我本人使用的配置.

## Related

Castel 大神的另一个仓库\(适用 MacOS\)

* [Inkscape figure manager](https://github.com/gillescastel/inkscape-figures)
