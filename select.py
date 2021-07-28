import os
import csv

TARGETLABELS=[
    'Speech',
    'Animal',
    'Wind',
    'Music',
    'Silence',

]

def main():
    filename=SelectFilename()
    labels=SelectLabels(TARGETLABELS)

    CreateFiles(labels, filename, 50)
    print('終了しました!!!')
#labels:['作成するファイル名','ラベルの実態']の配列
#filename:選別したいファイル名
#num:ファイルに書き込む数
def CreateFiles(labels, filename, num=1000):
    for label in labels:
        result=list()

        with open('target/' + filename) as f:
            
            for line in f.readlines():
                if (line.find(label[1]) >= 0):
                    result.append(line)
        with open('result/'+label[0]+'.csv', mode='w') as f:
            f.writelines(result[0 : num])

#targetの要素と等しい列のラベルをCreateFileに流せる形式で返す
def SelectLabels(target):
    result=list()
    with open('target/class_labels_indices.csv') as f:
        lines=csv.reader(f, delimiter=',', doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        
        for line in lines:
            
            if(line[2] in target):
                result.append(line[3:0:-1])
    with open('result/labels.csv', mode='w') as f:
        for i in result:
            f.write(','.join(i) + '\n')
    return result

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





if __name__ == '__main__':
    main()