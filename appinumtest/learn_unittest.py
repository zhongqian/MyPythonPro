#coding:utf-8
'''
Created on 2016年7月7日

@author: Administrator
'''
import unittest

def addNum(a, b):
    return a + b

def subNum(a, b):
    return a - b

class TestFun(unittest.TestCase):
    #在test方法前执行
    def setUp(self):
        print 'do before class------'
    #在test方法后执行
    def tearDown(self):
        print 'do after class-------'
    
    #skip跳过该测试方法
#     @unittest.skip("skip")   
    def test_add(self):
        print 'test add--------'
        self.assertEqual(2, addNum(1, 1))
    
    def test_sub(self):
        print 'test sub--------'
        self.assertEqual(0, subNum(1, 1))

if __name__ == "__main__":

#使用unittest.()方法执行用例  
#   unittest.main()

#建了一个集合，把TestFun这个case类中的所有test方法都load进来，
#然后用unittest自带的runner来运行，verbosity=2就是显示详细信息
#这时case跑出来的结果就有了case名
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFun)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
#加入多个不同的类进行测试
#     suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFun)
#     suite2 = unittest.TestLoader().loadTestsFromTestCase(TestFun)
#     alltests = unittest.TestSuite([suite1, suite2])
#     unittest.TextTestRunner(verbosity=2).run(alltests)
#     

    