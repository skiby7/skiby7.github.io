---
title: ZSH and Terminal Ricing
date: 2022-05-30 16:10
categories: [Linux]
tags: [zsh, linux, terminal, customization]
---

![Terminal](../../assets/img/terminal-rice.png)

# Install ZSH and change shell

```bash
sudo <package-manager install> zsh # apt install for Debian, dnf install for Fedora, etc.
chsh -s $(which zsh)
```
>**Note**: *in order to change shell for root user, rerun `chsh` with `sudo`.*

This should work on most distros. After the installation reboot or logout.

# Install oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
>**Note**: *running a script downloaded from the internet without checking what it does it's NOT recommended at all, so you can either open the link and check it or download the script and open it in your favorite text editor.*

Now the first time you open a terminal, it will prompt the config options for zsh, you can generate the default config or use a custom config. I'll skip it to install my favorite theme and import my `.zshrc` file:

## Spaceship theme
```bash
git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme" 
```

## `.zshrc` config file
```bash

export ZSH="/home/$USER/.oh-my-zsh"

ZSH_THEME="spaceship"

plugins=(git)

source $ZSH/oh-my-zsh.sh

EMOJI=(🚀 👽 ☕ 🐧 🍻 🔮 💾 🍪 🌍 🐫 🦊 🦄 ❄️ ⚡ 🎄 🌈 👻 )

function random_emoji {
  echo -n "$EMOJI[$RANDOM%$#EMOJI+1] "
}
SPACESHIP_CHAR_PREFIX="$(random_emoji)"
SPACESHIP_USER_SHOW="always"
SPACESHIP_USER_COLOR="cyan"
SPACESHIP_HOST_SHOW="always"
SPACESHIP_HOST_COLOR="#f241ac"
SPACESHIP_HOST_SHOW_FULL="false"
alias df='df -h /dev/sd* -x tmpfs -x devtmpfs'
alias fstab='sudo micro /etc/fstab'
SPACESHIP_NODE_SHOW="false"
```

# ZSH syntax highlighting

The give the final touch to this rice, you can install a syntax highlighter for ZSH:

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
cd zsh-syntax-highlighting
echo "source zsh-syntax-highlighting.zsh" >> ~/.zshrc
```
Here's my `.zshrc` file updated with syntax highlighting color scheme:

```bash
ZSH_HIGHLIGHT_STYLES[default]=none
ZSH_HIGHLIGHT_STYLES[unknown-token]=fg=009
ZSH_HIGHLIGHT_STYLES[reserved-word]=fg=009,standout
ZSH_HIGHLIGHT_STYLES[alias]=fg=129
ZSH_HIGHLIGHT_STYLES[builtin]=fg=075
ZSH_HIGHLIGHT_STYLES[function]=fg=003
ZSH_HIGHLIGHT_STYLES[command]=fg=014
ZSH_HIGHLIGHT_STYLES[precommand]=fg=009,underline
ZSH_HIGHLIGHT_STYLES[commandseparator]=none
ZSH_HIGHLIGHT_STYLES[hashed-command]=fg=009
ZSH_HIGHLIGHT_STYLES[path]=fg=003,italic
ZSH_HIGHLIGHT_STYLES[globbing]=fg=063
ZSH_HIGHLIGHT_STYLES[history-expansion]=fg=white,underline
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]=none
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]=none
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]=none
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]=fg=063
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]=fg=063
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]=fg=002
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]=fg=009
ZSH_HIGHLIGHT_STYLES[assign]=none
```

![sudo command](../../assets/img/rice-sudo-command.png) 
![alias path](../../assets/img/rice-alias-path.png) 
![function](../../assets/img/rice-function.png) 
