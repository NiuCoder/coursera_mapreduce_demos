# coursera_mapreduce_demos
## demo1说明
这是一个利用map reduce程序实现Join的示例，其中FileA中是一行行的<word,totalcount>的文本，FileB中是一行行的<date word,count>的文本。<br/>
本例运行map&reduce程序后的结果是得到了形如(date word count totalcount)的文本，实现了将FileA和FileB中以word为key的关联。<br/>

## demo2说明
这是另外一个利用map reduce程序实现Join的示例。其中genchan\*中是一行行的<TVshow,channel>的文本，记录的是电视节目对应的频道；gennum\*中是一行行的<TVshow,viewer_count>，记录的是电视节目对应的观看人数。
本例运行map&reduce程序后的结果是得到了所有channel是ABC的节目对应的总观看人数，形式为<TVshow viewer_count>。可以用伪SQL描述如下：<br/>
*select sum(viewer_count) from FileA,FileB where FileA.TVshow=FileB.TVshow and FileB.channel='ABC' group by TVshow*<br/>

make_join2data.py是一个辅助生成随机文本的程序。

## command说明
- 利用vim创建的map&reduce程序需要首先添加可执行程序chmod +x \*.py
- 在执行map&reduce命令之前可以在本地测试map&reduce程序，本地测试mapper的命令为：cat join2_gen*|./join2_mapper.py，得到的是map后的中间结果
- map和reduce之间有一个shuffle&sort的过程，因此该命令可以构建reduce的真实输入：cat join2_gen*|./join2_mapper.py|sort
- 如果map程序没问题，可以进一步测试reduce程序，命令为：cat join2_gen*|./join2_mapper.py|sort|./join2_reducer.py
- 如果文件过大，可以cat文件中的一部分到一个小文件，如cat join2_genchanB.txt |head -100 > test.txt，然后在小文件上进行测试和调试
- hadoop streaming命令通常形如：hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \<br/>
    -input /user/cloudera/input/join2 \<br/>
    -output /user/cloudera/output_join2 \<br/>
    -mapper /home/cloudera/join1_mapper.py \<br/>
    -reducer /home/cloudera/join1_reducer.py<br/>
- hadoop streaming命令中-input和-output后边都是HDFS上目录，因此需要首先将本地文件put进去，命令为hdfs dfs -put join2* /user/cloudera/input/join2；而-output后边的HDFS目录必须是一个不存在的目录，否则已存在的话无法执行成功，这是hadoop的机制，以防覆盖已有数据
