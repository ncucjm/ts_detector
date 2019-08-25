# ts_detector
工程目录

time_series_detector

    feature  特征提取文件
            ——> classification_feature 分类特征
            ——> fitting_feature 拟合特征
            ——> statistical_feature 统计特征
                            
    algorithm 算法文件
            ——> iforest
            ——> def __init__ 实现 1.模型加载,1)处理model = None情况.2)按 TS iist加载模型, 使用dict管理模型 2.模型参数加载.
            ——> def predict: 实现 模型预测 注意model = None的情况
            ——> def	trian: 实现 1.模型训练 2.模型保存 按TS的id名称保存 
            ——> def __extract_feature 实现苏算法的个性化特征提取, 继承feature类实现通用特征提取
                
    ------------------------------------------------------------
    model 模型保存文件
            ——> 按算法名称生成model子文件名称，例如：iforest  lstm 保存到本地太重,保存到数据库中
    ------------------------------------------------------------
    
    
    --------------------------------------------
    data 训练数据保存文件
            ——> 按算法名称生成model子文件名称       在项目中保存数据会导致项目太重了
    --------------------------------------------
 
    
    util 数据预处文件
            ——> 时间序列变换(归一化/采样)数据分割
            ——> 历史训练数据预处理 / 实时在县预测数据预处理
    
    check 校验文件
        ——>输入的校验

app

    common ——> 存放公共函数\常量
    
    dao ——> 数据管道实例
        
        file_os
        
        hive
        
        redis
        
        oracle
        
        ftp
    
        kafka
        
        mysql
        
        es
        
    service ——> 业务逻辑层/报文解析/业务逻辑定制规约
         
         
-----------------------
使用dict来管理多个模型
-----------------------

时间序列异常检测 问题解决流程:
1.分许数据,通过聚类算法找到可以用算法解决的问题
    聚类:形态学聚类,做序列归一化
    特征聚类:
    
    
    
2.算法分为两种类型
  离散点异常检测 ——> iforest
  时间序列异常监测 ——> arima

 