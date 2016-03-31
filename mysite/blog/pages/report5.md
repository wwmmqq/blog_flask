title: report5
date: 2015-03-24 10:00

# <center>基于窗口滑动的最值检测</center>
## 算法描述：
### 算法名字：AverageSlidingWindows
### 算法思想叙述：
	设窗口大小为w（一般大于等于3），待检测序列list的大小为L，我们让w从 3 增长到 L（每次加 1），在每个w大小下我们计算出整个list的窗口范围的最值点，并计算对应窗口下的最值点个数（此步得到：L-3个最值个数），然后取其平均值（记为：average_points）。最后我们把距points_average最近的窗口大小作为我们窗口体的最终大小(记为：w_final)。并把w_final窗口大小下的检查结果做为最终检查结果。
	
	
	也就是说: 我们无法确定窗口w的取值，所以我们把w的大小从小到大都跑一边，然后计算结果的平均值，最后取此平均值所对应的窗口大小w_final。
	

###输入kld数值序列，输出为检测到的异常点下标
本算法分为2个过程，1是确定窗口大小，2是取对应窗口大小下的异常点。

#### 版本3
	Input: list(L1,...,Ln);//Li 为每月星级分布图与前一个月的星级分布图的kld距离
	Output: 异常点下标
	w: 滑动窗口体大小
	
	resultset = [][]
	pointset = []
	for i = 3 to n do
	begin
		for j = 1 to n-w do
		begin 
			index = findmax(list, i, i+w-1);//寻找下标i到i+w-1中list的最大值所对应的下标
			add index in resultset[i]
		end
		put length(resultset[i]) in pointset;
	end
	average_point = sum(pointset)/length(pointset);
	w = nearest index of average_point; //选取距离average_point最近的窗口大小作为最终窗口
	return resultset[w]
	
	
#### 版本2：
	Input: list(L1,...,LN);//Li 为每月星级分布图与前一个月的星级分布图的kld距离
	Output: 异常点下标
	w: 滑动窗口体大小
	
	AverageSlidingWindows(list)
	
	result = [];
	pointset = [];
	for i = 3 to length(list) do
	begin
		for j = 1 to N-w do
		begin
			index = findmax(list, i, i+w-1); //寻找list中下标i到i+w-1中的最大值对应的下标
			add index in result;
		end
		put length(result) in pointset;
	end
	average_points = sum(pointset)/len(pointset); //计算最值点个数的平均值
	w = indexof(average_points); //选取average_points所对应的窗口大小作为最终窗口大小
	// 第一步w已经确定， 然后计算w下的最值点作为最终结果
	for j = 1 to N-w do
	begin
		index = findmax(list, i, i+w-1);
		add index in result;
	end
	return result;

####版本1：	
	Input:	list(L1 ,..., LN); Li 为每月星级分布图与前一月的星级分布图的kld距离
	Output: 异常点下标
	w : 为滑动窗口大小
	
	MaxbySlidingWindow(list, w)
	for i = 1 to N-w do 
	begin
		index = findmax(list, i , i+w-1); // 寻找list中下标i 到 i+w-1 中的最大值
		add index in result;
	end
	return result
	
	
	AverageWindowSize( list )
	resultset = []
	for i = 3 to length(list) do
	begin
		put length(MaxbySlidingWindow(list, i)) in resultset;
	end
	average_point = sum(resultset)/len(resultset);
	w = indexof(average_points); // 选取average_points所对应的窗口大小作为最终窗口大小
	
	return MaxbySlidingWindow(list, w)
	
