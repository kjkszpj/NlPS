# NlPS
你敢看我怎么一天写完NLP PJ吗？

by Peijie You

>   甚麼時候　誰答應過
 
>   天亮會否定所有黑夜

>   我們擁有的　多不過付出的一切

>   ------林夕

真是缘分, 最后决定使用LDA模型来对历年NIPS进行数据挖掘.

---

##  Design

-   wash data
    -   pdf to text, (标题, 作者, 简介, 正文, 页数, ) tuple for every paper
    -   tokenize(sent & word)
-   lda
-   fine tune
-   history
-   announce dataset
-   fast enough for LDA?

##  demo
-   topic show
-   log likelihood curve
-   word freq
-   comparison
    -   dict vs stem
    -   different dictionary
-   topic for single doc
-   handcraft vs random pick
-   history

##  todo

-   interval thing
-   stop word thing
-   history thing?

##  Problem arised

-   stop word in scholar
-   命名实体?
-   stem-100的奇怪现象
-   取什么频率区间内的word, dimension curse or just OK?
-   长尾?
-   dict rather than list
-   主题 is NOT 方向

##  Other
-   Python2 this time
-   http://cs.stanford.edu/people/karpathy/nips2015/

##  Requirement
-   python2
-   pdfminer
-   lda

---

##  Thank You

游沛杰(13307130325@fudan.edu.cn)