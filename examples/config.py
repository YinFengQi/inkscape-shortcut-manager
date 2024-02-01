import subprocess


def open_editor(filename):
    print("open minimal vim")

    subprocess.run([
        'gnome-terminal','--wait',
        # '-fn', 'xft:JetBrains mono nerd font:pixelsize=24',
        '--geometry', '60x8',
        '--title', 'latex input box',
        # '-background','gray40', '-cursorColor','gray80',
        '--', "nvim",
        "-u", "~/.config/nvim/minimal-tex-nvim.lua",
        f"{filename}",
    ])


def latex_document(latex):
    return r"""
        \documentclass[12pt,border=12pt]{standalone}
        \usepackage{amsfonts,amssymb,amsthm,amsmath,physics,extarrows}
        \begin{document}
    """ + latex + r"\end{document}"

config = {
    'rofi_theme': '~/.config/rofi/rofi-tokyonight/tokyonight.rasi',
    'font': 'JetBrains mono nerd font',
    'font_size': 10,
    'open_editor': open_editor,
    'latex_document': latex_document
}
