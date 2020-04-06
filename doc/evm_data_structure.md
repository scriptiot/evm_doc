## 1. evm_val_t

> 虚拟机通过evm_val_t来表示最基本的数据类型。

```
	typedef uint64_t evm_val_t;
```

+ evm_val_t相当于一个64位的整型数据，通常在单片机领域，大部分数据都是32位，包括指针地址。
+ EVM将外部数据包装成evm_val_t，通过标记方式，对数据进行分类。

---

## 2. EVM虚拟机支持的数据类型

+ 基础类型


```c
TYPE_NUMBER = 0, //数字类型
TYPE_HEAP_STRING,//堆字符串
TYPE_FOREIGN_STRING, //外部字符串
TYPE_BOOLEAN,//布尔
TYPE_FUNCTION,//函数
TYPE_NATIVE,//内置函数
TYPE_NULL,//空类
TYPE_UNDEFINED,//未定义类型
TYPE_NAN,//非法数字类型
TYPE_LIST,//数组类型
TYPE_BUFFER,//字节数组类型
TYPE_OBJECT,//对象类型
TYPE_CLASS,//类
TYPE_INT,//整数类型
TYPE_FRAME,//（虚拟机专用）
TYPE_FOREIGN,//（虚拟机专用）
```

+ 扩展类型

```c
TYPE_HEAP_STRING,
TYPE_LIST,
TYPE_BUFFER,
TYPE_OBJECT,
TYPE_CLASS,
```

+ 垃圾回收标记类型

```c
GC_NONE, 非法类型
GC_ROOT, 根作用域
GC_OBJECT, 对象
GC_NATIVE_OBJECT, 内置对象
GC_DICT, 字典
GC_CLASS, 类
GC_SET, 集合
GC_FUNC, 函数
GC_CLOSURE_FUNC, 闭包
GC_STATIC_FUNC, 静态函数
GC_LIST, 数组
GC_BUFFER, 字节数组
GC_BUFFER16, 16位数组
GC_BUFFER32, 32位数组
GC_BUFFER64, 64位数组
GC_BUFFER16_U, 无符号16位数组
GC_BUFFER32_U, 无符号32位数组
GC_BUFFER64_U, 无符号64位数组
GC_BUFFER_FLOAT, 浮点数组
GC_BUFFER_DOUBLE, 双精度浮点数组
GC_STRING, 堆字符串
GC_NUMBER, 数字
GC_BOOLEAN, 布尔
GC_TUPLE, 元组
GC_MODULE, 模块
GC_MEMBER, （虚拟机专用）
GC_MEMBER_KEYS, （虚拟机专用）
GC_MEMBER_VALS, （虚拟机专用）
```


## 3. evm_t

> 虚拟机对象

```
typedef struct evm_t{
    uint8_t err;
    const char * err_arg;
    char * file_name;
    uint32_t file_name_len;

    char * var_name;
    int var_name_len;

    heap_t * heap;
    evm_val_t * sp;
    evm_val_t * sp_base;
    int stack_size;
    evm_val_t root;
    evm_val_t scope;

    int32_t native_cnt;
    intptr_t * native_symbals;
    evm_val_t * native_tbl;
    int32_t module_size;
    int32_t module_cnt;
    intptr_t * module_symbals;
    evm_val_t * module_tbl;

    evm_const_pool_t * string_pool;
    evm_const_pool_t * number_pool;

    evm_val_t number_object;
}evm_t;

```


## 4. 常量

EVM虚拟机常量定义分为两种，一种是字符串常量，另外一种是数字常量。在虚拟机中，常量被分别保存在全局的常量池中：

```
evm_const_pool_t * string_pool; //字符串常量池
evm_const_pool_t * number_pool; //数字常量池
```

数字常量池是按添加顺序进行存储的，常量池中不会出现重复的数字。而字符串常量是按哈希表方式进行存储的，EVM虚拟机针对哈希表算法进行了优化，不仅提高的存取速度，同时满足了轻量化的哈希表扩容算法。


---

## 5. key值

EVM虚拟机访问字符串常量不是采用记录字符串在内存的地址值，而是通过获取key值而获取到字符串内容。所谓的key值是字符串在常量池中的值，为16位整型值。如果需要访问字符串内容，则需要通过下面的方法来获取：

```
char *evm_string_get(evm_t * e, uint16_t key);
```

如果要向常量池中增加字符串或者数字，可以使用下面的方法：

```
int evm_str_insert(evm_t *e, const char *str, int alloc);//添加字符串，返回key值
int evm_number_insert(evm_t *e, double num);//添加数字常量，返回key值
```

返回-1表示添加失败。

---
