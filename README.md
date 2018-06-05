# coursera_mapreduce_demos
## demo1说明
这是一个利用map reduce程序实现Join的示例，其中FileA中是一行行的<word,totalcount>的文本，FileB中是一行行的<date word,count>的文本。<br/>
本例运行map&reduce程序后的结果是得到了形如<date word count totalcount>的文本，实现了将FileA和FileB中以word为key的关联。<br/>

## demo2说明
这是另外一个利用map reduce程序实现Join的示例。其中genchan\*中是一行行的<TVshow,channel>的文本，记录的是电视节目对应的频道；gennum\*中是一行行的<TVshow,viewer_count>，记录的是电视节目对应的观看人数。
本例运行map&reduce程序后的结果是得到了所有channel是ABC的节目对应的总观看人数，形式为<TVshow viewer_count>。可以用伪SQL描述如下：<br/>
*select sum(viewer_count) from FileA,FileB where FileA.TVshow=FileB.TVshow and FileB.channel='ABC' group by TVshow*
