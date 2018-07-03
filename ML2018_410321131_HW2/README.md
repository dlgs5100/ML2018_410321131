# NDHU 2018 Machine learning assignment2

## Instruction
The dataset is the MNIST database of handwritten digits, available from http://yann.lecun.com/exdb/mnist, which has a training set of 60,000 examples and a test set of 10,000 examples.

## Algorithm 
Randrom forest model</br>
https://en.wikipedia.org/wiki/Random_forest</br>
Support vector machine(SVM)</br>
https://en.wikipedia.org/wiki/Support_vector_machine</br>

## Experiment result 


## Discussion 
Accuracy 直觀，但僅依靠高正確率並不能表示該分類器即為好的分類器</br>

AUC = 1，是完美分類器，採用這個預測模型時，不管設定什麼閾值都能得出完美預測。絕大多數預測的場合，不存在完美分類器。</br>
0.5 < AUC < 1，優於隨機猜測。這個分類器（模型）妥善設定閾值的話，能有預測價值。</br>
AUC = 0.5，跟隨機猜測一樣（例：丟銅板），模型沒有預測價值。</br>
0 < AUC < 0.5，比隨機猜測還差；但只要總是反預測而行，就優於隨機猜測。</br>
