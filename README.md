# ts_detector
工程目录

feature  特征提取文件
        ——> classification_feature 分类特征
	——> fitting_feature 拟合特征
	——> statistical_feature 统计特征


algorithm 算法文件
 	——> iforest
		——> def __init__ 实现 1.模型加载,1)处理model = None情况.2)按 TS iist加载模型, 使用dict管理模型 2.模型参数加载.
		——> def predict: 实现 模型预测 注意model = None的情况，
		——> def	trian: 实现 1.模型训练 2.模型保存 按TS的id名称保存 
		——> def __extract_feature 实现苏算法的个性化特征提取, 继承feature类实现通用特征提取


model 模型保存文件
	——> 按算法名称生成model子文件名称，例如：iforest  lstm

data 训练数据保存文件
	——> 按算法名称生成model子文件名称，


util 数据预处文件
	——> 时间序列变换，数据分割

check 校验文件
	——>各种输入的校验





-----------------------
使用dict来管理多个模型


