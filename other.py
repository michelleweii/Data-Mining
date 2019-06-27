# psi = np.frompyfunc(r8_psi,1,1)

def compute_ks(data):
    #按照样本为正样本的概率值升序排序 ，也即坏样本的概率从高到低排序
    sorted_list = data.sort_values(['predict_proba'], ascending=[True])
    total_good=sorted_list['label'].sum()
    total_bad = sorted_list.shape[0] - total_good
    max_ks = 0.0
    good_count = 0.0
    bad_count = 0.0
    for index, row in sorted_list.iterrows(): #按照标签和每行拆开
        if row['label'] == 0:
            bad_count +=1
        else:
            good_count +=1
        val = abs(bad_count/total_bad - good_count/total_good)
        max_ks = max(max_ks, val)
    return max_ks

# test_pd=pd.DataFrame()
# y_predict_proba=est.predict_proba(X_test)[:,1]#取被分为正样本的概率那一列
# Y_test_1=np.array(Y_test)
# test_pd['label']=Y_test_1
# test_pd['predict_proba']=y_predict_proba
# print ("测试集 KS:",compute_ks(test_pd))