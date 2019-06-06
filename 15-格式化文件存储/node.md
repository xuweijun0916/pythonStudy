# 结构化文件存储
- xml,json,
- 为了解决不同设备之间信息交换
- xml,
- json
# xml文件
- 参考资料

- xml(extensiblemarkuplanguage),可扩展标记语言
    - 标记语言，语言中使用尖括号括起来的文本字符串标记
    - 可扩展，用户可以自己定义需要的标记
    - 例如：
        <Teacher>
            ```
            自定义标记Teacher
            在两个标记之间任何内容都应该跟Teacher相关 
            ```
        </Teacher>
    - 是w3c组织制定的一个标准
    - xml描述的是数据本身，即数据的结构和语义
    - HTML侧重于如何显示web页面中的数据
    
- xml文档的构成
    - 处理指令（可以认为一个文件内只有一个处理指令）
        - 最多只有一行
        - 且必须在第一行
        - 内容是与xml本身处理相关的一些声明或指令
        - 以xml关键字开头
        - 一般用于声明xml的版本和采用的
            - version属性是必须的
            - encoding属性用来指出xml解释器使用的编码
    - 根元素（一个文件内只有一个根元素）
        - 在整个xml文件中，可以把他看做一个树形结构
    - 子元素
    - 属性
    - 内容
        - 表明标签所存储的信息
    - 注释
        - 其说明作用的信息
        - 注释不能嵌套在标签里
        - 只有在注释的开始和结尾使用双短横线
        - 三短横线只能出现在注释开头二不能用在结尾
        
    - 保留字符的处理
        - xml中使用的符号可能跟实际符号相冲突，典型的就是左右尖括号
        - 使用实体引用（EntityReference）来表示保留字符
            <score></score> #有错误，xml中不能出现
            <score>score&gt;80</score> #使用实体引用
        - 把含有保留字符的部分放在CDATA块内部，CDATA把内部信息视为不需要转义
            <![CDATA[
                select name,age
                from atudent
                where score>80
                ]]>
        - 常用的需要转义的保留字符和对应实体引用
            - &:&amp;
            - <:&lt;
            - >:&gt;
            - ':&apos;
            - ":&quot;
            - 一共五个，每个实体引用都以&开头并且以分号结尾
    - xml标签的命名规则
        - pascal命名法
        - 用单间表示，第一个字母大写
        - 大小写严格区分
        - 配对的标签必须一致
          
    - 命名空间
        - 为了防止命名冲突
            ```
            <Student>
              <Name>LiuYing</Name>
              <Age>23</Age>
             </Student>
             <Room>
                  <Name>2014</Name>
                  <Location>1-23-1</Location>
             </Room>  
            ```    
        - 如果归并上述两个内容信息，会产生冲突
        ```
        <Schooler>
                  <Name>LiuYing</Name>
                  <Age>23</Age>
              <Name>2014</Name>
              <Location>1-23-1</Location>
          </Schooler>
          ```
        - 为了避免冲突，需要给可能冲突元素添加命名空间
        - xmlns:xml name space 的缩写
        ```
            <Schooler xmlns:student="http://my_student" xmlns:room="http://my_room">
                <student:Name>LiuYing</student:Name>
                <Age>23</Age>
                <romm:Name>2014</room:Name>
                <Location>1-23-1</Location>
            </Schooler>
        ```
# xml访问
## 读取
- xml读取分两个主要技术，SAX，DOM
- SAX（simple API for XML）:
    - 基于事件驱动的API
    - 利用SAX解析文档设计到解析器和事件处理两部分
    - 特点：
        - 快
        - 流式读取
        
- DOM
    - 是w3c规定的xml编程接口
    - 一个xml文件在缓存中以树形结构保存，读取
    - 用途
        - 定位浏览xml任何一个节点信息
        - 添加删除相应内容
    - minidom
        - minidom.parse(filename):加载读取的xml文件, filename也可以是xml代码
        - doc.documentElement:获取xml文档对象，一个xml文件只有一个对于的文档对象
        - node.getAttribute(attr_name):获取xml节点的属性值
        - node.getElementByTagName(tage_name)：得到一个节点对象集合
        - node.childNodes:得到所有孩子节点
        - node.childNodes[index].nodeValue:获取单个节点值
        - node.firstNode:得到第一个节点，等价于node.childNodes[0]
        - node.attributes[tage_name]
        - 案例v01

    - etree
        - 以树形结构来表示xml
        - root.getiterator:得到相应的可迭代的node集合
        - root.iter
        - find(node_name):查找指定node_name的节点,返回一个node
        - root.findall(node_name):返回多个node_name的节点
        - node.tag: node对应的tagename
        - node.text:node的文本值
        - node.attrib： 是node的属性的字典类型的内容
        - 案例v02
        
- xml文件写入
    - 更改
        - ele.set:修改属性
        - ele.append：添加子元素
        - ele.remove: 删除元素
        - 案例 v03
    - 生成创建
        - subelement, 案例v04
        - minidom写入，案例v05
        - etree创建，案例v06
        
# JSON
- 在线工具
    - https://www.sojson.com/
    - http://www.w3school.com.cn/json/
    - http://www.runoob.com/json/json-tutorial.html
- JSON(javascriptobjectnotation)
- 轻量级的数据交换格式，基于ECMAScript
- json格式是一个键值对形式的数据集
    - key:字符串
    - value:字符串，数字，列表，json
    - json使用大括号包裹
    - 键值对之间用逗号隔开
    student={ "name": "wangdapeng", "age": 18, "mobile":"13260446055" }
    
- json和python格式的对应

    - 字符串：字符串
    - 数字：数字
    - 队列：list
    - 对象：dict
    - 布尔值：布尔值
- python for json
    - json包
    - json和python对象的转换
        - json.dump():对数据编码，把python格式表示成json格式
        - json.loads():对数据解码，把json格式转换成python格式
    - python读取json文件
        - json.dump():把文件写入文件
        - json.load():把json文件读入python
    - 案例v07
    - 案例v08读取文件
    
# 正则表达式（RegularExpression,re）
- 是一个计算机科学的概念
- 用于使用单个字符串来描述，匹配符合某个规则的字符串
- 常常用来检索，替换某些模式的文本

# 正则的写法
- .（点号）:表示任意一个字符，除了\n，比如查找所有的一个字符 \.
- []:匹配中括号中列举的任意字符，比如[L,Y,0], LLY, Y0, LIU
- \d:任意一个数字
- \D:除了数字都可以
- \s:表示空格，tab键
- \S:除了空白字符
- \w:单词字符，就是a-z, A-Z, 0-9
- \W:除了\w里的内容
- ： 表示前面内容重复零次或者多次， \w
- +: 表示前面内容至少出现一次
- ？： 前面才出现的内容零次或者一次
- {m,n}:允许前面内容出现最少m次，最多n次
- ^:匹配字符串的开始
- $:匹配字符串的结尾
- \b:匹配单词的边界
- ():对正则表达式内容进行分组， 从第一个括号开始，编号逐渐增大
```
  验证一个数字： ^\d$
  必须有一个数字，最少一位：^\d+$
  只能出现数字，且位数为5-10位： ^\d{5,10}$
  注册者输入年龄，要求16岁以上，99岁以下： ^[16-99]$
  只能输入英文字符和数字： ^[A-Za-z0-9]$
  验证qq号码： [0-9]{5,12}
```
- \A: 只匹配字符串开头， \Aabcd, 则abcd
- \Z: 仅匹配字符串末尾， abcd\Z, abcd
- |: 左右任意一个
- (?P...): 分组，除了原来的编号再制定一个别名， (?P12345){2}， 1234512345
- (?P=name): 引用分组，

# xpath
- 在xml文件中查找信息的一套规则/语言,根据xml的元素或者属性进行遍历

# xpath 开发工具
- 开源的xpath表达式编辑工具：xmlQuire
- Chrome插件：xpath helper
- Firefox插件：xpath checker

# 选取节点
- nodename：选取此节点的所有子节点
- /:从根节点开始选取
    ```
    /student:没有结果
    /school:选区school节点
  
    ```
- //:选取节点，不考虑位置
        
        //age:选取出三个节点，一般组成列表返回
- .:选取当前节点
- ..:选取当前节点的父亲节点
- @：选取属性
- xpath中查找一般按照路径方法查找，以下是路径表示方法

        School/Teacher:返回Teacher节点
        School/Student:返回两个Student节点
        //Student:选取所有Sudent的节点，不考虑位置
        School//Age：选取School后代中所有Age节点
        //@other:选取other属性
        //Age[@Detail]:选取带有属性Detail的Age元素
        
# 谓语-Predicates
- /School/Student[1]:选取School下面的第一个Student节点
- /School/Student[last()]:选取School下面的最后一个Student节点
- /School/Student[last()-1]:选取School下面的倒数第二个Student节点
- /School/Student[position()<3]:选取School下面的前两个Student节点
- //Student[@score]:选取带有属性score的student节点
- //Student[@score="99"]:选取带有属性score并且属性值是99的student节点
- //Student[@score]/Age:选取带有属性score的student节点的子节点Age

# Xpath的一些操作
- |：或者

        //Student[@score] | //Teacher:选取带有属性score的student节点和teacher节点
- 其余不常见xpath运算符号包括+，-，*，div，>,<


            
    
        
        
        