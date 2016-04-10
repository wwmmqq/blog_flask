title: records of building this blog
date: Monday, April 10, 2016
time: 2016_04_10
summary: 主要记录了本博客相关的开发经验
tags: python,flask


##代码高亮
选择了highlightjs对markdown中的代码进行高亮（只是应为它简单）
### highlight

	highlight 会自动去寻找代码中的 <pre><code>...</code></pre> 部分，并高亮其中的代码。

### 如何使用 highlightjs
	<link rel="stylesheet" type="text/css" href="/blog/static/css/github.css" />
	//引入代码高亮的语法样式

	<script src="/blog/static/js/highlight.pack.js"></script>
	//引入highlight的核心js文件

	<script>hljs.initHighlightingOnLoad();</script>
	//执行hightlight，需要用到jquery
