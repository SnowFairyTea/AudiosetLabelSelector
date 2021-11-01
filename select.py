import os
import csv
import sys

TARGETLABELS=[
    'Speech',
    'Animal',
    'Wind',
    'Music',
    'Silence',

]

DIR = os.path.dirname(os.path.abspath(__file__))
print(DIR)
#argvは
#0:選別するラベル名が書かれたファイルのパス
#1,2,3:eval,balanced_train,unbalanced_trainのそれぞれの抜く数
#
#
def main():
    preprocess()
    argv=sys.argv
    if(len(argv) > 1):
        target = ReadInputfile(argv[1])
        print(target)
        labels = SelectLabels(target)
    else:
        labels=SelectLabels(TARGETLABELS)

    num=[]
    if(len(argv) > 2):
        num.append(ReadInputfile(argv[2]))

    else:
        num.append(1000)
    print("balanced_train:",num)
    

    if(len(argv) > 3):
        num.append(ReadInputfile(argv[3]))
        
    else:
        num.append(num[0]//2)
    print("eval:",num)

    if(len(argv) > 4):
        num.append(ReadInputfile(argv[4]))
        
    else:
        num.append(0)
    print("unbalanced_train:",num)

    #filename=SelectFilename()
    

    CreateFiles(labels,  num)
    print('終了しました!!!')

def preprocess():
    try:
        os.mkdir(os.path.join(DIR,'result',"blanced_train"))
    except:
        None
    try:
        os.mkdir(os.path.join(DIR,'result',"eval"))
    except:
        None
    try:
        os.mkdir(os.path.join(DIR,'result',"unblanced_train"))
    except:
        None
    

#labels:['作成するファイル名','ラベルの実態']の配列
####filename:選別したいファイル名
#num:ファイルに書き込む数の配列
def CreateFiles(labels,  num=[100,50,0]):
    for label in labels:
        result=list()


        #blanced_trainを作成
        with open(DIR+'/target/' + 'balanced_train_segments.csv') as f:
            for line in f.readlines():
                if (line.find(label[1]) >= 0):
                    result.append(line)
        with open(os.path.join(DIR,'result',"blanced_train",label[0]+'.csv'), mode='w') as f:
            f.writelines(result[0 : num[0]])

        #evalを作成
        with open(DIR+'/target/' + 'eval_segments.csv') as f:
            
            for line in f.readlines():
                if (line.find(label[1]) >= 0):
                    result.append(line)
        with open(os.path.join(DIR,'result',"eval",label[0]+'.csv'), mode='w') as f:
            f.writelines(result[0 : num[1]])

        #unblanced_trainを作成
        with open(DIR+'/target/' + 'unbalanced_train_segments.csv') as f:
            for line in f.readlines():
                if (line.find(label[1]) >= 0):
                    result.append(line)
        with open(os.path.join(DIR,'result',"unblanced_train",label[0]+'.csv'), mode='w') as f:
            f.writelines(result[0 : num[2]])

#配列targetの要素をラベルに含む行のリストをCreateFileに流せる形式で返す
#class_labels_indices.csvを参照して['クラス名','ラベルの実態']
def SelectLabels(target):
    result=list()
    with open(DIR+'/target/class_labels_indices.csv') as f:
        lines=csv.reader(f, delimiter=',', doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        
        for line in lines:
            
            if(line[2] in target):
                result.append(line[3:0:-1])
    with open(DIR+'/result/labels.csv', mode='w') as f:
        for i in result:
            f.write(','.join(i) + '\n')
    return result

# 
def SelectFilename():
    csvlist=['eval_segments.csv',
            'balanced_train_segments.csv',
            'unbalanced_train_segments.csv'
            ]
    print('以下のファイル名を数字で選ぶかファイル名を入力してください')
    for i in range(len(csvlist)):
        print(str(i)+' : '+csvlist[i])
    s=input('ファイル名か番号:\n')
    try:
        
        r = csvlist[int(s)]
    except:
        r = s
    finally:
        return r

#ファイル名を投げるとファイルの内容が1行ずつ配列に入って帰ってくる
def ReadInputfile(argv):
    r=[]
    with open(argv) as f:
        for i in f.read().splitlines():
            r.append(i)
    return r



if __name__ == '__main__':
    main()