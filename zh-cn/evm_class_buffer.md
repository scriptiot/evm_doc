## 平台支持

| API     |    OS|
| :-------- | --------:|
| buf.compare| Linux，RT-Thread, Zephyr |
| buf.copy| Linux，RT-Thread, Zephyr |
| buf.equals| Linux，RT-Thread, Zephyr |
| buf.fill|   Linux，RT-Thread, Zephyr  | 
| buf.from|   Linux，RT-Thread, Zephyr  |
| buf.slice|  Linux，RT-Thread, Zephyr  |
| buf.toString|  Linux，RT-Thread, Zephyr  | 
| buf.write|  Linux，RT-Thread, Zephyr | 
| buf.writeUInt8| Linux，RT-Thread, Zephyr |
| buf.writeUInt16LE| Linux，RT-Thread, Zephyr |
| buf.writeUInt32LE| Linux，RT-Thread, Zephyr |
| buf.readInt8|   Linux，RT-Thread, Zephyr  | 
| buf.readUInt8|   Linux，RT-Thread, Zephyr  |
| buf.readUInt16LE|  Linux，RT-Thread, Zephyr  |

### Buffer

` new Buffer(size) `

+ size {integer} buffer大小.

```javascript
var Buffer = require('buffer');

var buffer = new Buffer(5);
```
    
` new Buffer(buffer) `

+ buffer {Buffer} 缓存数组.

```javascript
var Buffer = require('buffer');

var buffer1 = new Buffer(5);
var buffer2 = new Buffer(buffer1);
```

` new Buffer(str[, encoding]) `

+ str {string} 字符串.
+ encoding {string} 编码格式.

```javascript
var Buffer = require('buffer');

var buffer = new Buffer(String.fromCharCode(65));

// prints: 1
console.log(buffer);

var buffer = new Buffer(String.fromCharCode(128));

// prints: 2
console.log(buffer);

var buffer = new Buffer(String.fromCharCode(2048));

// prints: 3
console.log(buffer);

var buffer = new Buffer('4142', 'hex');

// prints: AB
console.log(buffer);
```

` new Buffer(array) `

+ array {Array} 数字数组.

```javascript
var buffer = new Buffer([65, 256 + 65, 65 - 256, 65.1]);

// prints: AAAA
console.log(buffer);
```

` Buffer.byteLength(str, encoding) `

+ str {string} 字符串.
+ encoding {string} 字符串编码.
+ Returns: {integer} 返回字符串的字节缓存长度.

```javascript
var Buffer = require('buffer');

// prints: 1
console.log(Buffer.byteLength(String.fromCharCode(65)));

// prints: 2
console.log(Buffer.byteLength(String.fromCharCode(128)));

// prints: 3
console.log(Buffer.byteLength(String.fromCharCode(2048)));

// prints: 2
console.log(Buffer.byteLength('4142', 'hex'));
```

` Buffer.concat(list) `

+ list {Array} buffer对象列表.

```javascript
var Buffer = require('buffer');

var buffer = Buffer.concat([ new Buffer('He'),
                             new Buffer('llo'),
                             new Buffer(' wo'),
                             new Buffer('rld') ])

// prints: Hello world
console.log(buffer);
```

` Buffer.from(array) `

+ array {Array} 数字数组.
+ Returns: {Buffer} 返回包含数组元素的缓存对象。

```javascript
var Buffer = require('buffer');

var source = new Buffer[65, 66, 67];
var buffer = Buffer.from(source);

//prints: ABC
console.log(buffer.toString());
```

` Buffer.from(string[,encoding]) `

+ str {String} 字符串.
+ encoding {String} 编码格式.
+ Returns: {Buffer} 返回包含字符串元素的缓存对象。

```javascript
var Buffer = require('buffer');

var buffer = Buffer.from('4142','hex');

//prints: AB
console.log(buffer.toString());
```

` Buffer.from(buffer) `

+ buffer {Buffer} 缓存对象.
+ Returns: {Buffer} 返回buffer的拷贝对象。

```javascript
var Buffer = require('buffer');

var source = new Buffer(12);
var buffer = Buffer.from(source);
```

` Buffer.from(arrayBuffer[, byteOffset[, length]]) `

+ arrayBuffer {ArrayBuffer} Arraybuffer 或者 TypedArray。
+ byteOffset {Number} 索引偏移位置. 默认: 0.
+ length {Number} 数组长度. 默认: arrayBuffer.length - byteOffset.
+ Returns: {Buffer} 返回包含arrayBuffer的指定范围元素的缓存对象。

```javascript
var source = new ArrayBuffer(12);
var buffer = Buffer.from(source, 0, 2);

//prints: 2
console.log(buffer.length);
var typed_source = new Uint8Array([65,66]);
var arr_buff = Buffer.from(typed_source1.buffer, 0, 2);

//prints: AB
console.log(buff.toString('utf-8'));
```


` Buffer.isBuffer(obj) `

+ obj {Object} 对象。
+ Returns: {boolean} 返回bool值。

```javascript
var Buffer = require('buffer');

// prints: true
console.log(Buffer.isBuffer(new Buffer(1)));

// prints: false
console.log(Buffer.isBuffer('str'));
```


` buf.length `

缓存对象容量长度。


```javascript
var Buffer = require('buffer');

var buffer = new Buffer([0xc8, 0x80]);

// prints: 2
console.log(buffer.length);

var str = buffer.toString();

// prints: 1
console.log(str.length);
```


` buf.compare(otherBuffer) `

+ otherBuffer {Buffer} 待比较的缓存对象.
+ Returns: {integer}

这个函数用来比较两个缓存对象内容是否相同。如果两个对象相同，返回0；如果当前对象缓存长度大于待比较的缓存对象的长度，返回1；小于则返回-1.


```javascript
var Buffer = require('buffer');

var buffer = new Buffer([0xc8, 0x80]);

// prints: 2
console.log(buffer.length);

var str = buffer.toString();

// prints: 1
console.log(str.length);
```


` buf.copy(targetBuffer[, targetStart[, sourceStart[, sourceEnd]]]) `

+ targetBuffer {Buffer} 缓存对象.
+ targetStart {Integer} 默认值：0
+ sourceEnd {integer} 默认值: buf.length
+ Returns: {integer} 拷贝的字节长度.


```javascript
var Buffer = require('buffer');

var buffer1 = new Buffer('Hello XY world!');
var buffer2 = new Buffer('<JS>');

buffer2.copy(buffer1, 6, 1, 3);

// prints: Hello JS world!
console.log(buffer1);
```


` buf.equals(otherBuffer) `

+ otherBuffer {Buffer} 待比较缓存对象.
+ Returns: {boolean}


```javascript
var Buffer = require('buffer');

var buffer1 = new Buffer('AB');
var buffer2 = new Buffer('4142', 'hex');
var buffer3 = new Buffer('A');

// prints: true
console.log(buffer1.equals(buffer2));

// prints: false
console.log(buffer1.equals(buffer3));
```


` buf.fill(value) `

+ value {integer} 待填充的值.
+ Returns: {Buffer} 原始缓存对象.


```javascript
var Buffer = require('buffer');

var buffer = new Buffer('Hello');

buffer.fill(65);

// prints: AAAAA
console.log(buffer);

buffer.fill(66 - 256);

// prints: BBBBB
console.log(buffer);
```


` buf.slice([start[, end]]) `

+ start {integer} 默认值: 0
+ end {integer} 默认值: buf.length
+ Returns: {Buffer} 新创建的缓存对象.


```javascript
var Buffer = require('buffer');

var buffer = new Buffer('This is JavaScript!!!');

// prints: JavaScript
console.log(buffer.slice(8, 18));
```

` buf.toString([start[, end]]) `

+ start {integer} 默认值: 0
+ end {integer} 默认值: buf.length
+ Returns: {string}。


```javascript
var Buffer = require('buffer');

var buffer = new Buffer('DEFG');

// prints: EF
console.log(buffer.toString(1, 3));

// prints: 44454647
console.log(buffer.toString('hex'));
```


` buf.write(string[, offset[, length]]) `

+ string {string} 写入缓存对象的数据.
+ offset {integer} 写入数据的起始地址. 默认值: 0
+ length {integer} 写入数据的长度. 默认值: buffer.length - offset.
+ Returns: {integer} 返回写入数据的总长度.


```javascript
var Buffer = require('buffer');

var buffer = new Buffer('......');
buffer.write('AB');
buffer.write('XY', 3);

// prints: AB.XY.
console.log(buffer);

var buffer = new Buffer('......');
buffer.write('ABCDEF', 1, 3);

// prints: .ABC..
console.log(buffer);
```


` buf.writeUInt8(value, offset[, noAssert]) `

+ string {string} 写入缓存对象的数据.
+ offset {integer} 写入数据的起始地址. 默认值: 0
+ length {integer} 写入数据的长度. 默认值: buffer.length - offset.
+ Returns: {integer} 返回写入数据的总长度.


```javascript
var Buffer = require('buffer');

var buffer = new Buffer('......');
buffer.write('AB');
buffer.write('XY', 3);

// prints: AB.XY.
console.log(buffer);

var buffer = new Buffer('......');
buffer.write('ABCDEF', 1, 3);

// prints: .ABC..
console.log(buffer);
```

