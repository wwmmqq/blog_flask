title: ohmyzsh
date: Sunday, April 3, 2016
time: 2016_04_03
summary: ohmyzsh 的使用
tag: linux

# 终极shell
shell是Linux/Unix的外壳,它负责外界与内核的交互，接收用户或其他应用程序的命令,然后把这些命令转化成内核能理解的语言,传给内核,内核执行完后再把结果返回用户或应用程序.</br>

Linux/Unix提供了很多种Shell,常用的Shell有sh\bash\csh等<br>
	cat /etc/shells
zsh配置很复杂，但是极为强大。

# oh my zsh 让zsh容易使用

## install 
Ubuntu:</pr>
	sudo apt-get install zsh
	chsh -s /bin/zsh //安装完成后设置当前用户使用zsh
	wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
Mac:</pr>
	//自动安装
	wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
	//手动安装
	git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
	cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

## my deploy 
	
	#my own  alias
	alias cls="clear"
	alias vi="/usr/local/bin/vim"
	alias la="ls -all"
	alias ll="ls -l"
	alias grep="grep --color=auto"
	alias -s py=vi
	alias -s c=vi
	alias -s cpp=vi
	alias -s zip='unzip'


	#my git alias
	alias gs="git status"
	alias gd="git diff"
	alias ga="git add"
	alias gm="git commit -m"


	#autojump
	[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh

	#mysql
	alias mysql=/usr/local/mysql/bin/mysql
	alias mysqladmin=/usr/local/mysql/bin/mysqladmin
	alias mysqldump=/usr/local/mysql/bin/mysqldump

	export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting

## auto junmp
###install
	Mac: brew install autojump
	Ubuntu: get https://github.com/downloads/joelthelion/autojump/autojump_v21.1.2.tar.gz
			./install.sh
			把以下代码加入.zshrc
			[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh
###use
智能跳转，安装了autojump之后，zsh 会自动记录你访问过的目录，通过 j + 目录名 可以直接进行目录跳转，而且目录名支持模糊匹配和自动补全</br>
目录浏览和跳转：输入 d，即可列出你在这个会话里访问的目录列表，输入列表前的序号，即可直接跳转。
