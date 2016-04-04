title: Vundle
date: Saturday, April 3, 2016
time: 2016_04_03
summary: Vundle 包管理软件, 用于管理vim的插件
tag: vim

# <center>Vundle 包管理软件</center>

Vundle基于Git获取Github上的各种Vim插件，可进行在线查找、安装、更新Vim插件，每个插件以单独目录存放，方便管理

## Vundle install
	git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle

## Vundle deploy

 	set nocompatible "与vi不一致
 	filetype off
 	set rtp+=~/.vim/bundle/vundle/ "载入特定目录插件
 	set rtp+=$HOME/.vim/bundle/vundle/ "Windows下
 	call vundle#rc()



## How to install plugin use Vundle

	vimscripts账号下的项目直接填写名称即可
	Bundle 'snipMate'
	"其它需填写用户/资源名称
	Bundle 'gmarik/vundle'
	"非github上资源:
	Bundle 'git://git.wincent.com/command-t.git'
	"indent
	Bundle 'php.vim-html-enhanced'
	"color
	Bundle 'Lucius'
	filetype plugin indent on 


## brief commands of Vundle

	:BundleList          - list configured bundles
	:BundleInstall(!)    - install(update) bundles
	:BundleSearch(!) foo - search(or refresh cache first) for foo
	:BundleClean(!)      - confirm(or auto-approve) removal of unused bundles
	see :h vundle for more details or wiki for FAQ
