# [Python调用Java代码说明]()

# [注意点]()
* 在Python线程中如有调用java相关代码时,需要在Python线程体(run方法)中调用jpype.attachThreadToJVM()