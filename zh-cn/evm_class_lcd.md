## class LCD – 液晶屏对象

小熊派开发板支持spi驱动的RGB565液晶屏， 像素为240x240.

### 构造函数

` class evm.LCD() `

 创建一个LCD对象，并初始化液晶屏驱动。

    
    
### 对象函数

` LCD.on()`

 打开液晶屏背景光。
 
 
` LCD.off()`

关闭液晶屏背景光。
 

` LCD.set_pixel(x, y)`

液晶屏在（x，y）坐标画一个点
 
 
` LCD. get_pixel(x, y)`

获取(x,y)坐标的颜色

 
` LCD.draw_line(x1, y1, x2, y2)`

画一条直线通过(x1, y1)、(x2, y2) 坐标


` LCD.draw_rect(x1, y1, w, h)`

画一个矩形在坐标(x1, y1)，宽高为w、 h


` LCD.draw_circle(x, y, radius)`

画一个圆形在坐标(x1, y1)，半径为radius


` LCD.fill_rect(x, y, w, h)`

填充一个矩形在坐标(x1, y1)，宽高为w、 h


` LCD.fill_circle(x, y, radius)`

填充一个圆形在坐标(x1, y1)，半径为radius


` LCD.draw_text(x, y, text)`

在(x, y) 坐标画字符串，字符串内容为text


` LCD.set_paint_color(rgb)`

设置绘制颜色，rgb值为RGB565格式


` LCD.set_background_color(rgb)`

设置 背景颜色，rgb值为RGB565格式
