# Inkscape shortcut manager

*A shortcut manager that speeds up drawing (mathematical) figures in [Inkscape](https://inkscape.org/).*
本仓库 fork 自 [Castel 的仓库](https://github.com/gillescastel/inkscape-figures), 他真的好强啊呜呜呜

## Problem

此程序用来更快地在 inkscape 中画图, Castel 大神在笔记里用它做的图如下


![Elliptic curve](./examplefigures/fig_1.png)

![Complex Analysis](./examplefigures/fig_2.png)


## Solution

这个快捷键管理器可以监听传入 inkscape 的键盘输入, 并将它们转化为自定义的操作.


- **按下组合键可以快速更改选中对象的样式**  <kbd>d</kbd>+<kbd>a</kbd> 对应 **d**otted **a**rrow, <kbd>f</kbd>+<kbd>s</kbd> **f**ills the selection in gray and adds a **s**troke.

-You want a circle that's **d**otted and **f**illed? Press <kbd>f</kbd> + <kbd>d</kbd>. Try pressing combinations of <kbd>s</kbd>, <kbd>a</kbd>, <kbd>d</kbd>, <kbd>g</kbd>, <kbd>h</kbd>, <kbd>x</kbd>, <kbd>e</kbd>, <kbd>b</kbd>, <kbd>f</kbd>, <kbd>w</kbd>. Being able to combine these common styles by pressing key chords feels quite intuitive after a while.
- **Save custom styles and objects.** Press <kbd>Shift+S</kbd> or <kbd>Shift+A</kbd> to give a style or object a name. Use it by pressing <kbd>s</kbd> or <kbd>a</kbd> and typing the name. For common styles that aren't covered by the key chords, this comes in handy.
- **Use your editor to write LaTeX.** Pressing <kbd>t</kbd> opens an instance of vim (or any editor you want). Write some LaTeX, close it, and the shortcut manager pastes the text in the figure. Pressing <kbd>Shift+T</kbd> does the same but renders the LaTeX as an svg and adds it to the document.
- **Ergonomic shortcuts for frequently used functions**. Press <kbd>w</kbd> for pencil, <kbd>x</kbd> to toggle snapping, <kbd>f</kbd> for Bézier, <kbd>z</kbd> to undo, <kbd>Shift</kbd>+<kbd>z</kbd> to delete and <kbd>\`</kbd> to dis/enable the shortcut manager.

For more details and context, feel free to read my [blog post](https://castel.dev/post/lecture-notes-2).

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
